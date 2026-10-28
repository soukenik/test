#!/usr/bin/env python3
"""Záloha MyHeritage Family Tree Builder (.ftb = SQLite) -> GEDCOM a přehled přímé linie.

Použití (z kořene projektu):
  python3 -I tools/ftb_export.py <strom.ftb> <vystup.ged>
      celý strom jako GEDCOM pro tools/ged_import.py (bez adres, e-mailů, telefonů a rodných čísel)
  python3 -I tools/ftb_export.py <strom.ftb> <vystup.ged> "Jméno Příjmení" <rok narození> <linie.md> [složka s Photos]
      navíc přehled přímých předků této osoby (Kekulého čísla): všechna fakta, poznámky,
      PŮVOD údajů (cizí stromy přes Smart Match) a připojené fotky/dokumenty.

Záloha z MyHeritage (ZIP se souborem <strom>.ftb a složkou Photos/) není GEDCOM, ale databáze SQLite.
ZIP rozbal do vlastní složky v dokumenty/. Na Windows spouštěj `python -I -X utf8 tools/ftb_export.py …`.
"""
import html, os, pathlib, re, sqlite3, sys
from collections import defaultdict
for _s in (sys.stdout, sys.stderr):   # UTF-8 výstup i na Windows bez -X utf8 (cp1250 neumí třeba „→“)
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

SKIP_TAGS = {"ADDR", "EMAIL", "PHON", "WWW", "FAX", "IDNO", "SSN"}   # kontakty a čísla dokladů do exportu nepatří
TAG_MAP = {"BAPM": "CHR"}                                          # křest – ged_import zná jen CHR


def skip(tag, ftype, val):
    """Kontakty žijících lidí: samostatné fakty ADDR/EMAIL/PHON…, RESI s takovým typem
    a RESI, jejichž text je XML z formuláře adresy (<Address1>, <Email>, <Phone>, <City>…)."""
    return tag in SKIP_TAGS or (tag == "RESI" and (ftype in SKIP_TAGS or val.lstrip().startswith("<")))


def txt(b):
    if b is None:
        return ""
    s = b.decode("utf-8", "replace") if isinstance(b, bytes) else str(b)
    if any("\x80" <= ch <= "\x9f" for ch in s):   # jazyk 0 bývá cp1250 přečtený jako latin-1
        try:
            s = s.encode("latin-1").decode("cp1250")
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass
    return s.strip()


def date_text(b):
    """Datum je zabalené (protobuf): 0x0A, délka, text „4 MAR 1973“."""
    if not b:
        return ""
    if b[0] != 0x0A:
        return txt(b)
    n, shift, i = 0, 0, 1
    while True:
        n |= (b[i] & 0x7F) << shift
        i += 1
        if not b[i - 1] & 0x80:
            break
        shift += 7
    return b[i:i + n].decode("utf-8", "replace").strip()


def pick(rows):
    """rows = [(jazyk, hodnota…)] – přednost čeština (20), jinak výchozí (0)."""
    rows = sorted(rows, key=lambda r: 0 if r[0] == 20 else 1)
    return rows[0] if rows else None


def load(path):
    # immutable=1: databáze je ve WAL režimu – jinak by SQLite vedle zálohy založil soubory -shm/-wal
    c = sqlite3.connect(pathlib.Path(path).resolve().as_uri() + "?mode=ro&immutable=1", uri=True)
    c.text_factory = bytes
    q = lambda s: c.execute(s).fetchall()
    D = {}
    places = defaultdict(list)
    for pid, lang, p in q("select place_id, data_language, place from places_lang_data"):
        places[pid].append((lang, txt(p)))
    D["place"] = {k: pick(v)[1] for k, v in places.items()}

    names = defaultdict(list)
    for iid, lang, fn, ln, ms, nick in q("""select d.individual_id, l.data_language, l.first_name, l.last_name,
            l.married_surname, l.nickname from individual_lang_data l
            join individual_data_set d using(individual_data_set_id) where d.delete_flag = 0"""):
        names[iid].append((lang, txt(fn), txt(ln), txt(ms), txt(nick)))
    D["ind"] = {}
    for iid, sex, alive in q("select individual_id, gender, is_alive from individual_main_data where delete_flag = 0"):
        n = pick(names.get(iid, [])) or (0, "", "", "", "")
        D["ind"][iid] = dict(first=n[1], last=n[2], married=n[3], nick=n[4], sex=txt(sex) or "U")
        # is_alive (1/2/3) v záloze neodpovídá skutečnosti – nepoužívá se

    flang = defaultdict(list)
    for fid, lang, head, cause in q("select individual_fact_id, data_language, header, cause_of_death from individual_fact_lang_data"):
        flang[fid].append((lang, txt(head), txt(cause)))
    D["facts"] = defaultdict(list)
    for fid, iid, tok, ftype, age, d, pid, cur in q("""select individual_fact_id, individual_id, token, fact_type, age, date,
            place_id, is_current from individual_fact_main_data where delete_flag = 0
            order by individual_id, is_current desc, sorted_date"""):
        l = pick(flang.get(fid, [])) or (0, "", "")
        if skip(txt(tok), txt(ftype), l[1]):
            continue
        D["facts"][iid].append(dict(id=fid, tag=txt(tok), type=txt(ftype), age=txt(age), date=date_text(d),
                                    place=D["place"].get(pid, ""), val=l[1], cause=l[2]))

    D["fam"] = defaultdict(lambda: {"h": None, "w": None, "c": []})
    for fid, iid, role in q("""select family_id, individual_id, individual_role_type from family_individual_connection
            where delete_flag = 0 order by family_id, child_order_in_family"""):
        if iid not in D["ind"]:   # osoba smazaná jen v hlavní tabulce – žádné odkazy do prázdna (Gramps, MyHeritage)
            continue
        f = D["fam"][fid]
        if role == 2:
            f["h"] = iid
        elif role == 3:
            f["w"] = iid
        elif role == 5:
            f["c"].append(iid)
    fflang = defaultdict(list)
    for ffid, lang, head in q("select family_fact_id, data_language, header from family_fact_lang_data"):
        fflang[ffid].append((lang, txt(head)))
    D["famfacts"] = defaultdict(list)
    for ffid, fid, tok, ftype, d, pid in q("""select family_fact_id, family_id, token, fact_type, date, place_id
            from family_fact_main_data where delete_flag = 0 order by family_id, sorted_date"""):
        l = pick(fflang.get(ffid, [])) or (0, "")
        if skip(txt(tok), txt(ftype), l[1]):
            continue
        D["famfacts"][fid].append(dict(tag=txt(tok), type=txt(ftype), date=date_text(d),
                                       place=D["place"].get(pid, ""), val=l[1]))

    tokens = {tid: (eid, it) for tid, eid, it in q("select token_on_item_id, entity_id, item_type from token_on_item")}
    nlang = defaultdict(list)
    for nid, lang, t in q("select note_id, data_language, note_text from note_lang_data"):
        nlang[nid].append((lang, txt(t)))
    fact_owner = {f["id"]: iid for iid, fs in D["facts"].items() for f in fs}
    D["notes"] = defaultdict(list)
    for nid, tid in q("select note_id, external_token_on_item_id from note_to_item_connection where delete_flag = 0"):
        eid, it = tokens.get(tid, (None, None))
        owner = eid if it == 1 else fact_owner.get(eid) if it == 3 else None
        t = (pick(nlang.get(nid, [])) or (0, ""))[1]
        if owner is not None and t:
            D["notes"][owner].append(t)

    slang = defaultdict(list)
    for sid, lang, title, author in q("select source_id, data_language, title, author from source_lang_data"):
        slang[sid].append((lang, txt(title), txt(author)))
    D["sources"] = defaultdict(set)
    for sid, page, tid in q("select source_id, page, external_token_on_item_id from citation_main_data where delete_flag = 0"):
        eid, it = tokens.get(tid, (None, None))
        owner = eid if it == 1 else fact_owner.get(eid) if it == 3 else None   # citace u osoby i u jejího faktu
        if owner is not None:
            s = pick(slang.get(sid, [])) or (0, "?", "")
            D["sources"][owner].add(s[1] + (f" ({s[2]})" if s[2] else ""))

    mlang = defaultdict(list)
    for mid, lang, title, desc in q("select media_item_id, data_language, title, description from media_item_lang_data"):
        mlang[mid].append((lang, txt(title), txt(desc)))
    D["media"] = defaultdict(list)
    for mid, eid, it, size in q("""select c.media_item_id, c.token_entity_id, c.token_item_type, m.file_size
            from media_item_to_item_connection c join media_item_main_data m using(media_item_id) where c.delete_flag = 0"""):
        if it == 1:
            m = pick(mlang.get(mid, [])) or (0, "", "")
            D["media"][eid].append((mid, m[1], m[2], int(txt(size) or 0)))
    return D


def full_name(p):
    return re.sub(r"\s+", " ", f"{p['first']} {p['last']}").strip() or "(beze jména)"


def chunks(s, n=240):
    """Dlouhý text na kusy pro CONC (GEDCOM 5.5.1 má řádek nejvýš 255 znaků); nedělí u mezery, aby se neztratila."""
    out = []
    while len(s) > n:
        i = n
        while i > n // 2 and (s[i - 1].isspace() or s[i].isspace()):
            i -= 1
        out.append(s[:i])
        s = s[i:]
    return out + [s]


def gtext(level, tag, value):
    out = []
    for k, line in enumerate((value or "").replace("\r", "").split("\n")):
        parts = chunks(line.rstrip())
        head = f"{level} {tag}" if k == 0 else f"{level + 1} CONT"
        out.append(f"{head} {parts[0]}" if parts[0] else head)
        out += [f"{level + 1} CONC {p}" for p in parts[1:]]
    return out


def write_ged(D, out):
    famc, fams = defaultdict(list), defaultdict(list)
    for fid, f in D["fam"].items():
        for p in (f["h"], f["w"]):
            if p:
                fams[p].append(fid)
        for ch in f["c"]:
            famc[ch].append(fid)
    L = ["0 HEAD", "1 SOUR ftb_export", "1 GEDC", "2 VERS 5.5.1", "1 CHAR UTF-8"]
    for iid, p in D["ind"].items():
        L.append(f"0 @I{iid}@ INDI")
        L.append(f"1 NAME {p['first']} /{p['last']}/".replace("  ", " "))
        if p["married"]:
            L.append(f"1 NAME {p['first']} /{p['married']}/")
            L.append("2 TYPE married")
        L.append(f"1 SEX {p['sex']}")
        for f in D["facts"].get(iid, []):
            tag = TAG_MAP.get(f["tag"], f["tag"])
            if tag == "EVEN":
                L += gtext(1, "EVEN", f["val"])
                L.append(f"2 TYPE {f['type']}")
            else:
                L += gtext(1, tag, f["val"])
            if f["date"]:
                L.append(f"2 DATE {f['date']}")
            if f["place"]:
                L.append(f"2 PLAC {f['place']}")
            if f["cause"]:
                L.append(f"2 CAUS {f['cause']}")
        for n in D["notes"].get(iid, []):
            L += gtext(1, "NOTE", n)
        L += [f"1 FAMC @F{x}@" for x in famc.get(iid, [])]
        L += [f"1 FAMS @F{x}@" for x in fams.get(iid, [])]
    for fid, f in D["fam"].items():
        L.append(f"0 @F{fid}@ FAM")
        if f["h"]:
            L.append(f"1 HUSB @I{f['h']}@")
        if f["w"]:
            L.append(f"1 WIFE @I{f['w']}@")
        L += [f"1 CHIL @I{c}@" for c in f["c"]]
        for e in D["famfacts"].get(fid, []):
            L += gtext(1, e["tag"], e["val"])
            if e["tag"] == "EVEN" and e["type"]:
                L.append(f"2 TYPE {e['type']}")
            if e["date"]:
                L.append(f"2 DATE {e['date']}")
            if e["place"]:
                L.append(f"2 PLAC {e['place']}")
    L.append("0 TRLR")
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L) + "\n")
    print("GEDCOM:", out, "|", len(D["ind"]), "osob,", len(D["fam"]), "rodin")


def birth_year(D, iid):
    for f in D["facts"].get(iid, []):
        if f["tag"] in ("BIRT", "CHR", "BAPM"):
            m = re.search(r"\d{4}", f["date"])
            if m:
                return int(m.group())
    return None


def write_line(D, root, out, photos):
    parents = {}
    for f in D["fam"].values():
        for ch in f["c"]:
            parents.setdefault(ch, (f["h"], f["w"]))
    files = defaultdict(list)   # soubory v Photos/ nesou jiné číslo než media_item_id – páruje se podle velikosti
    if photos and os.path.isdir(photos):
        for fn in os.listdir(photos):
            files[os.path.getsize(os.path.join(photos, fn))].append(fn)
    tree, todo, seen = {1: root}, [1], {root}
    while todo:
        k = todo.pop(0)
        if k >= 2 ** 24:
            continue
        h, w = parents.get(tree[k], (None, None))
        for kk, p in ((2 * k, h), (2 * k + 1, w)):
            if p and p in D["ind"]:
                if p in seen:   # smyčka nebo předek vícekrát (SAME)
                    tree[kk] = p
                    continue
                seen.add(p)
                tree[kk] = p
                todo.append(kk)
    L = ["# Přímá linie z MyHeritage (záloha Family Tree Builder)", "",
         "Pracovní výtah – údaje NEJSOU ověřené matrikou. „Původ“ = odkud údaj ve stromu přišel.", ""]
    for k in sorted(tree):
        iid = tree[k]
        p = D["ind"][iid]
        g = k.bit_length() - 1
        L.append(f"## {k}. {full_name(p)}  (generace {g}, id {iid})")
        if p["married"]:
            L.append(f"- příjmení po sňatku: {p['married']}")
        for f in D["facts"].get(iid, []):
            label = f["type"] if f["tag"] == "EVEN" else f["tag"]
            bits = [x for x in (f["val"], f["date"], f["place"], f"příčina: {f['cause']}" if f["cause"] else "",
                                f"věk {f['age']}" if f["age"] else "") if x]
            if bits:
                L.append(f"- {label}: {' | '.join(bits)}")
        for fid, f in D["fam"].items():
            if iid in (f["h"], f["w"]):
                sp = f["w"] if iid == f["h"] else f["h"]
                spn = full_name(D["ind"][sp]) if sp in D["ind"] else "?"
                ev = "; ".join(" | ".join(x for x in (e["tag"], e["date"], e["place"]) if x) for e in D["famfacts"].get(fid, []))
                kids = ", ".join(f"{full_name(D['ind'][c])} ({birth_year(D, c) or '?'})" for c in f["c"] if c in D["ind"])
                L.append(f"- rodina s: {spn} — {ev or 'bez údajů o sňatku'}; děti: {kids or '—'}")
        for n in D["notes"].get(iid, []):
            n = html.unescape(re.sub(r"<[^>]+>", " ", n))
            L.append("- poznámka: " + re.sub(r"\s+", " ", n).strip()[:2000])
        src = sorted(D["sources"].get(iid, []))
        L.append("- původ: " + ("; ".join(src) if src else "bez citace (zadáno ručně ve vlastním stromu)"))
        for mid, title, desc, size in D["media"].get(iid, []):
            fl = ", ".join(files.get(size, [])) or "(soubor nenalezen)"
            L.append(f"- foto/dokument: {fl} — {title}{' – ' + desc if desc else ''}")
        L.append("")
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(L))
    print("Přímá linie:", out, "|", len(tree), "předků, nejvzdálenější generace", max(k.bit_length() - 1 for k in tree))


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    D = load(sys.argv[1])
    write_ged(D, sys.argv[2])
    if len(sys.argv) >= 6:
        q, y = sys.argv[3].lower().split(), int(sys.argv[4])
        hits = [i for i, p in D["ind"].items() if all(w in full_name(p).lower() for w in q) and birth_year(D, i) == y]
        if len(hits) != 1:
            sys.exit(f"Výchozí osoba nenalezena jednoznačně: {hits}")
        write_line(D, hits[0], sys.argv[5], sys.argv[6] if len(sys.argv) > 6 else "")


if __name__ == "__main__":
    main()
