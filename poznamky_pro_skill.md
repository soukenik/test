# Poznámky pro správce skillu „rodokmen“

Sem Claude průběžně zapisuje, co by se mělo ve skillu zlepšit: chyby nástrojů, nové archivy a postupy, nápady.
Jen technické věci, žádné údaje o rodině. Nic se neposílá automaticky – když budete chtít, Claude poznámky vypíše
a vy je zkopírujete do e-mailu na sarsonj@gmail.com. Klidně připište i vlastní zkušenosti – užitečné změny autor rád
zapracuje do skillu, aby je měli i ostatní. Děkujeme!


## Cloudové prostředí (claude.ai, Claude Code on the web)
- Výchozí síťová politika cloudové relace blokuje všechny archivní portály (proxy vrací 403 na CONNECT: www.mza.cz,
  actapublica.eu, aron.vychodoceskearchivy.cz, digi.archives.cz, kramerius5.nkp.cz, ndk.cz, data.matricula-online.eu,
  nominatim.openstreetmap.org). Funguje jen npm/PyPI a GitHub. Skill by mohl v Fázi 0 rovnou otestovat dostupnost
  portálů a poradit povolení domén (nastavení prostředí → Network access), nebo práci na vlastním počítači.
- Instalace skillu jako plugin (`/plugin marketplace add`) v cloudu nedává smysl; funguje zkopírovat
  `skills/rodokmen` do `.claude/skills/rodokmen` v repozitáři projektu – pak se načte v každé relaci nad repozitářem.
- `magick` (ImageMagick 7) v cloudovém kontejneru chybí, ImageMagick 6 (`convert`) nástroje použily bez problémů.
- Lhůta pro úmrtí: skill (SKILL.md i `ged_import.py`) počítá s 30 lety, podle zákona o matrikách (301/2000 Sb.) jsou to
  myslím 75 let od posledního zápisu (narození 100, manželství i úmrtí 75). Prosím ověřit – `ged_import.py` pak hlásí
  úmrtí z 80. let 20. století jako „matriky online“.
