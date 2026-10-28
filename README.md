# Rodokmen Vojtáskových z Rudimova

Rodokmen Petra Vojtáska a jeho předků z Rudimova u Luhačovic (okres Zlín). Příjmení se píše
Vojtásek / Vojtásková, s „s“ bez háčku.

| # | Osoba | Vztah k Petrovi | Narození | Úmrtí | Poznámka |
|---|---|---|---|---|---|
| 1 | **Petr Vojtásek** | výchozí osoba | | | žijící |
| – | **Miriam**, roz. Kovářová | manželka | | | žijící |
| 2 | **Otto Vojtásek** | otec | 21. 9. 1931 | 1984, Slavičín | |
| 3 | **Jindřiška**, roz. Meislová | matka | 24. 3. 1938 | | Slavičín – upřesnit |
| 4 | **Jan Vojtásek** | dědeček | 31. 7. 1908, Rudimov (?) | 26. 6. 1982 | velitel hasičů, kapelník a starosta |
| 5 | **Anastázie**, roz. Viceníková (?) | babička | 16. 4. 1904, Rudimov (?) | 2. 12. 1976 | žena v domácnosti |

## Jak je projekt uspořádaný

Projekt vede skill [rodokmen](https://github.com/sarsonj/rodokmen-skill) (verze 0.5.0, kopie v `.claude/skills/rodokmen/`).
V každé relaci Claude Code nad tímto repozitářem se načte sám (nebo `/rodokmen`).

- `data/` – osoby (`data/osoby.py`), stav práce (`data/STAV.md`), údaje od rodiny, deník hledání, dotazy na archiv
- `web/` – rodinný web (`cd web && npm install && npm run data && npm run build`)
- `dokumenty/` – rodinné fotografie, zápis z rámu a `rodokmen.ged` (GEDCOM pro MyHeritage, FamilySearch, Geni)
- `vyrezy/`, `zdroje/` – výřezy fotografií a matričních zápisů pro web
- `tools/` – nástroje skillu (stahování z archivů, kontrola dat, výřezy)

## Hledání v matrikách

Rudimov patří pod Moravský zemský archiv v Brně (Acta Publica). Cloudová relace Claude Code na claude.ai má archivní
portály ve výchozím nastavení sítě zablokované. Hledat v matrikách jde buď po povolení domén v nastavení prostředí,
nebo v Claude Code na vlastním počítači.
