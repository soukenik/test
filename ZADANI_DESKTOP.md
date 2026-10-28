# Zadání pro nové vlákno v Claude Code na počítači

## Příprava (jednou)

1. Stáhněte si projekt do počítače. V Terminálu (Mac) nebo Git Bash (Windows) spusťte:
   ```
   git clone -b claude/vitaskovi-rudimov-genealogy-0zly2z https://github.com/soukenik/test.git ~/Rodokmen-Vojtaskovi
   ```
2. V aplikaci Claude (záložka Code) otevřete novou relaci **ve složce `~/Rodokmen-Vojtaskovi`**.
   Skill `rodokmen` je přímo v projektu (`.claude/skills/rodokmen`), načte se sám.
3. Matriky Moravského zemského archivu se prohlížejí v prohlížeči. Připojte proto Claude in Chrome
   (příkaz `/chrome` v relaci), nebo nechte Clauda použít vlastní prohlížeč.
4. Do relace vložte text níže.

## Text k vložení

```
/rodokmen

Pokračuj v rodokmenu Vojtáskových v této složce. Nejdřív si přečti data/STAV.md, konec data/research_log.md,
data/udaje_od_rodiny.md a data/osoby.py. Projekt byl založený v cloudové relaci, kde byly archivy zablokované,
takže zatím nemáme žádný matriční zápis.

Co víme od rodiny (výchozí osoba Petr Vojtásek, žijící):
- rodiče: Otto Vojtásek (* 21. 9. 1931, † 1984 Slavičín) a Jindřiška roz. Meislová (* 24. 3. 1938 Slavičín (?), † Slavičín)
- prarodiče: Jan Vojtásek (* 31. 7. 1908, † 26. 6. 1982) a Anastázie roz. Viceníková (?) (* 16. 4. 1904, † 2. 12. 1976 (?)),
  oba nejspíš narození v Rudimově u Luhačovic. Jan byl podle rodiny velitel hasičů, kapelník, starosta a největší sedlák
  („kulak“) v obci. Příjmení rodina píše Vojtásek bez háčku, na rámu fotky je spíš „Vojtášek“ – hledej obě podoby.
- Rudimov patří do farnosti Slavičín (Moravský zemský archiv Brno, Acta Publica – www.mza.cz/actapublica).
  Do roku 1992 byl Rudimov součástí Slavičína.

Úkol – Fáze 2 (matriky), v tomto pořadí:
1. Ověř, že se dostaneš na www.mza.cz/actapublica. Najdi svazky ŘKFÚ Slavičín pro Rudimov (narození, oddaní, zemřelí)
   a zapiš je do data/svazky.json.
2. Najdi a přečti zápis o narození Jana Vojtáska (31. 7. 1908) a Anastázie (16. 4. 1904). Ověř rodné příjmení Anastázie
   a podobu příjmení Vojtásek/Vojtášek. Zapiš jejich rodiče (další generaci) se všemi 6 kroky ze skillu
   (svazek, zápis, výřez, rámeček, přepis s překladem, osoba).
3. Hledej sňatek Jana a Anastázie (asi 1928–1931, nejdřív ve farnosti nevěsty), pokud je svazek online.
4. Pokračuj o generaci dál přes sňatky a úmrtí rodičů (matrika zemřelých pro Rudimov 1878–1949, inv. č. 4645).
5. Pokud zbude čas: noviny v Krameriu (Jan Vojtásek / Vojtášek, Rudimov – starosta, hasiči, kapela).

Pravidla: „doc“ jen to, co přečteš přímo na snímku; nejisté čtení s „(?)“; každé hledání (i neúspěšné) do deníku;
po změnách spusť python3 -I tools/kontrola.py. Žijící lidé (Petr, manželka Miriam roz. Kovářová) jen jméno.
Mladší zápisy (narození po roce 1926, sňatky po ~1951) dej do data/archivni_dotazy.md.
Než pustíš pomocníky, řekni mi plán. Po každém kole mi stručně řekni, co jsi našel, a průběžně ukládej
(git commit) a nahrávej do větve claude/vitaskovi-rudimov-genealogy-0zly2z (git push).
```
