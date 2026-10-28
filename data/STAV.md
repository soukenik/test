# Stav rodokmenu a pravidla práce

Tento soubor je vstupní bod. Po každém restartu (nová konverzace, zkrácený kontext) ho Claude čte jako první,
pak konec `research_log.md` a sekci „Rozpracováno“.

## Pro koho
- Výchozí osoba: Petr Vojtásek (žijící). Rodiče Otto Vojtásek (1931–1984, Slavičín) a Jindřiška roz. Meislová (* 1938);
  prarodiče Jan Vojtásek (1908–1982) a Anastázie (1904–1976) z Rudimova u Luhačovic. Manželka Miriam roz. Kovářová.
- Kdo s Claudem pracuje a jak chce komunikovat: člen rodiny, česky. Pracuje se v cloudové relaci Claude Code (claude.ai), repozitář soukenik/test.

## Kde co je
| Soubor | Obsah |
|---|---|
| `data/osoby.py` | Přímí předci podle Kekulého čísla + rody, boční příbuzní, otevřené otázky, hypotézy. |
| `data/zaznamy.json` | Každý použitý zápis z matriky (klíč = název obrázku). |
| `data/svazky.json` | Matriční svazky (archiv, signatura, odkaz). |
| `data/prepisy.json` | Přepis originálu a český překlad každého zápisu. |
| `data/zvyrazneni.json` | Rámečky – které místo výřezu čteme. |
| `data/research_log.md` | Deník VŠECH hledání, i neúspěšných. |
| `data/udaje_od_rodiny.md` | Co řekla rodina, rodinné dokumenty. |
| `data/zajimavosti.md`, `data/pribeh.md` | Texty na web. |
| `data/archivni_dotazy.md` | Co by šlo zjistit jen v archivu. |
| `data/mista.json`, `data/dokumenty.json`, `data/web.json` | Mapa, rodinné fotky a dokumenty, nastavení webu. |
| `vyrezy/`, `zdroje/` | Výřezy zápisů pro web (1800 px) a v plném rozlišení. |
| `dokumenty/` | Rodinné dokumenty a fotky od uživatele (originály). |
| `pracovni/` | Pracovní soubory (stažené stránky, kontrolní obrázky) – nejdou na web. |
| `web/` | Rodinný web. `cd web && npm run data && npm run build`, náhled `npm run preview`. |

## Pravidla
1. Než něco ohlásím jako nové, prohledám `osoby.py`, `zaznamy.json` a `research_log.md` (jméno, místo, rok).
2. Údaj je „doloženo“ (doc) jen tehdy, když jsem ho přečetl přímo na snímku. Čtení od pomocníků ověřím sám.
3. Každé hledání (i neúspěšné) zapíšu do `research_log.md`.
4. Nejistá čtení označím (?) – nic nedomýšlím.
5. Ke každému novému zápisu: výřez (`tools/vyrez.py`), rámeček (`tools/ramecek.py`) a přepis s překladem.
6. Po změně dat spustím `python3 -I tools/kontrola.py`.

## Rozpracováno (aktualizovat průběžně)
- Fáze 1 (rozhovor s rodinou): vyjasněno – Jindřiška ze Slavičína (už nežije), Miri = manželka Miriam, Jan „největší kulak“.
  Zbývá: datum úmrtí Jindřišky, kde se narodil Otto, sňatek Jana a Anastázie, sňatek Otty a Jindřišky, čísla domů,
  rodiče Jindřišky (Meislovi), kdy byl Jan starostou.
- Čeká se na povolení domén archivů v nastavení cloudového prostředí (uživatel nastavuje z mobilu).
- Fáze 2 (matriky): Rudimov spadá pod **MZA Brno (Acta Publica)** – pro skill bez nástroje, jen přes prohlížeč.
  **Z cloudové relace jsou všechny archivní portály zablokované sítí** (proxy vrací 403 na www.mza.cz, actapublica.eu,
  kramerius5.nkp.cz, ndk.cz, nominatim.openstreetmap.org…). Potřeba povolit domény v nastavení prostředí,
  nebo pracovat v Claude Code na vlastním počítači.
  Pořadí: narození Jana 1908 a Anastázie 1904 v Rudimově (farnost zjistit na portálu) → rodiče = další generace;
  sňatek Jana a Anastázie asi 1928–1931 ve farnosti nevěsty (online, jen pokud je svazek uzavřen před ~1951).
  Narození Otty 1931 a mladší údaje jsou na matričním úřadě (viz `archivni_dotazy.md`).
- Noviny (Jan byl podle rodiny starosta, velitel hasičů a kapelník): Kramerius / NDK, hledat „Vojtásek Rudimov“, „Vojtášek Rudimov“.
- `dokumenty/rodokmen.ged`: GEDCOM se stejnými údaji jako `osoby.py` – při změnách osob ho aktualizovat (nebo smazat).
