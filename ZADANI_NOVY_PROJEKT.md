# Zadání pro nový, samostatný projekt: Rodokmen Vojtáskových z Rudimova

Toto zadání nezávisí na dosavadním repozitáři. Projekt se založí úplně od začátku (Fáze 0 skillu `rodokmen`)
a všechny známé údaje jsou přímo v textu níže.

## Příprava (jednou, ručně)

1. **Kde pracovat:** nejlépe v Claude Code **na vlastním počítači** (aplikace Claude → záložka Code), protože
   matriky Moravského zemského archivu se prohlížejí v prohlížeči. Připojte Claude in Chrome (`/chrome`),
   nebo nechte Clauda použít vlastní prohlížeč.
   Pokud chcete pracovat v cloudu (claude.ai), nejdřív v nastavení prostředí (menu prostředí → Edit → Network access)
   povolte domény: `www.mza.cz`, `actapublica.eu`, `www.actapublica.eu`, `kramerius5.nkp.cz`, `ndk.cz`,
   `www.digitalniknihovna.cz`, `nominatim.openstreetmap.org`.
2. **Skill:** nainstalujte skill `rodokmen` (https://github.com/sarsonj/rodokmen-skill), nebo zkopírujte jeho složku
   `skills/rodokmen` do `.claude/skills/rodokmen` v nové složce projektu.
3. **Rodinné fotky** (pokud je máte): fotografii Jana a Anastázie a fotku zadní strany rámu se zápisem si připravte,
   po založení projektu je dejte do složky `dokumenty/`.
4. Otevřete novou relaci v prázdné složce (navrženo `~/Rodokmen-Vojtaskovi-novy`) a vložte text níže.

## Text k vložení

```
/rodokmen

Založ nový, samostatný projekt rodokmenu Vojtáskových (Fáze 0) ve složce ~/Rodokmen-Vojtaskovi-novy
a pak rovnou pokračuj Fázemi 1–2. Komunikuj česky, stručně, pro člověka bez zkušeností s genealogií a programováním.

KROK 0 – PŘÍSTUP K ARCHIVŮM (udělej jako první, ještě před zakládáním projektu):
Ověř, že se dostaneš na www.mza.cz/actapublica a na Kramerius (kramerius5.nkp.cz nebo ndk.cz).
Pokud ne (síť je blokuje), hned skonči a řekni mi, které domény mám povolit – nic nehledej přes vyhledávače
a nic si nedomýšlej.

ZALOŽENÍ PROJEKTU:
- Zkontroluj nástroje (python3, node, ImageMagick, git), založ projekt nástrojem novy_projekt.py, git init, první uložení.
- Název webu „Rodokmen Vojtáskových“, v data/STAV.md vyplň „Pro koho“.
- Rodinné fotky z dokumenty/ (pokud tam jsou) přečti a vytěž do data/udaje_od_rodiny.md.

CO VÍME OD RODINY (zapiš do data/udaje_od_rodiny.md a do data/osoby.py se stavem „fam“):
- 1  Petr Vojtásek – výchozí osoba, žijící (jen jméno). Manželka Miriam roz. Kovářová, žijící (jen jméno, do SIDE).
- 2  Otto Vojtásek, otec – * 21. 9. 1931 (místo neznámé, nejspíš Rudimov), † 1984 Slavičín.
- 3  Jindřiška roz. Meislová, matka – * 24. 3. 1938 Slavičín (?), ve Slavičíně žila a zemřela (datum úmrtí neznámé).
- 4  Jan Vojtásek, dědeček – * 31. 7. 1908 Rudimov (?), † 26. 6. 1982. Podle rodiny velitel hasičů, hlavní kapelník,
     starosta a největší sedlák („kulak“) v obci. Na fotografii v hasičské uniformě s vyznamenáními (mezi nimi kříž).
- 5  Anastázie roz. Viceníková (?), babička – * 16. 4. 1904 Rudimov (?), † 2. 12. 1976 (?) (první číslice dne
     přepsaná, může být 7. 12.). Žena v domácnosti.
- Údaje u Jana a Anastázie jsou z tužkou psaného zápisu na zadní straně rámu fotografie. Rodné příjmení Anastázie
  je tam špatně čitelné (Viceníková / Vicaníková / Vicenáková?).
- Příjmení: rodina píše Vojtásek / Vojtásková bez háčku, na rámu je spíš „Vojtášek“ – hledej obě podoby.
- Rudimov u Luhačovic (okres Zlín) patří do farnosti Slavičín; do roku 1992 byl součástí Slavičína.
  Matriky: Moravský zemský archiv Brno, Acta Publica (www.mza.cz/actapublica), fond ŘKFÚ Slavičín.
  Známý svazek: matrika zemřelých pro Rudimov 1878–1949, inv. č. 4645. Index oddaných Slavičín 1942–1949, inv. č. 6624.
- Hasičský sbor v Rudimově založen 1907 (rudimov.cz → Historie).

OTEVŘENÉ OTÁZKY (do ISSUES): Vojtásek, nebo Vojtášek? Rodné příjmení Anastázie? Přesné datum jejího úmrtí?
Kde a kdy se Jan a Anastázie vzali? Byl Jan starostou a velitelem hasičů, kdy? Jak se mu vedlo jako „kulakovi“
po roce 1948? Kdy zemřela Jindřiška?

FÁZE 2 – MATRIKY, v tomto pořadí:
1. Na Acta Publica najdi všechny svazky ŘKFÚ Slavičín pro Rudimov (narození, oddaní, zemřelí, indexy)
   a zapiš je do data/svazky.json.
2. Najdi a přečti zápis o narození Jana (31. 7. 1908) a Anastázie (16. 4. 1904). Ověř rodné příjmení Anastázie
   a podobu příjmení. Zapiš je i jejich rodiče (osoby 8–11) se všemi 6 kroky ze skillu
   (svazek, zápis, výřez, rámeček, přepis s překladem, osoba). Čti i poznámky na okrajích (sňatek, úmrtí).
3. Hledej sňatek Jana a Anastázie (asi 1928–1931, nejdřív ve farnosti nevěsty), pokud je svazek online.
4. Pokračuj o generaci dál přes sňatky a úmrtí rodičů (matrika zemřelých Rudimov 1878–1949, inv. č. 4645),
   rod po rodu, dokud matriky dovolí.
5. Pokud zbude čas: noviny v Krameriu („Vojtásek Rudimov“, „Vojtášek Rudimov“ – starosta, hasiči, kapela).
6. Průběžně sbírej zajímavosti (data/zajimavosti.md) a po ~5 doložených generacích nabídni „Příběh Vojtáskových“.

PRAVIDLA:
- „doc“ jen to, co přečteš přímo na snímku; nejisté čtení s „(?)“, nečitelné „[…]“; rozpory do ISSUES.
- Každé hledání (i neúspěšné, s rozsahem snímků) do data/research_log.md.
- Po změnách spusť python3 -I tools/kontrola.py a oprav chyby.
- Žijící lidé (Petr, Miriam) jen jméno. Mladší zápisy (narození po roce 1926, sňatky po ~1951, úmrtí Otty,
  Jindřišky, Jana a Anastázie) dej do data/archivni_dotazy.md (matriční úřad Slavičín / Luhačovice).
- Než pustíš pomocníky, řekni mi plán a nech si ho schválit; pomocníci na levnějším modelu, jejich čtení ověř sám.
- Po každém kole mi stručně řekni, co jsi našel (kolik osob a zápisů, 2–4 zajímavé větve), ulož (git commit)
  a pokud je nastavený vzdálený repozitář, nahraj (git push).
```
