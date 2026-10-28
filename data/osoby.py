# Přímí předci podle Kekulého čísel: 1 = výchozí osoba (ten, pro koho rodokmen děláme),
# otec osoby n má číslo 2n, matka 2n+1. Tedy 2 = otec, 3 = matka, 4–7 prarodiče, 8–15 pradědečci a prababičky…
#
# Každá osoba:  číslo: dict(n="Jméno Příjmení", y="1850–1910", st="doc", f=[...], r=[...], note="...")
#   n    jméno; ženy rodným příjmením („Anna Dvořáková“), u nejistého čtení otazník („Marie Špalková (?)“)
#   y    roky života pro přehledy: "* 1931" (žije / úmrtí neznámé), "1850–1910", "asi 1720–1785", "1680 – před 1740"
#   st   stav doložení:  doc  = doloženo matrikou (čteno přímo ze snímku)
#                        prob = pravděpodobné (shoda údajů, ale ne přímý doklad)
#                        fam  = údaj od rodiny / z rodinného dokumentu
#                        mh   = jen z cizího rodokmenu na internetu (MyHeritage, Geni…) – neověřeno
#                        unk  = neznámé (jen místo v rodokmenu)
#   f    fakta jako krátké věty: "* 12. 3. 1873 Hořice čp. 477", "kovář", "× 28. 1. 1897 Anna Stejskalová", "† 14. 5. 1902"
#        (* narození, × sňatek, † úmrtí – podle těchto značek web pozná sňatky a místa pro mapu)
#   r    klíče zápisů z data/zaznamy.json, které osobu dokládají
#   note poznámka: proč je údaj nejistý, rozpory, odkud se vzal
#   sex  jen u osoby 1: "M" nebo "F" (u ostatních plyne z čísla)
# Žijící lidé: jen jméno a rok narození (soukromí), note="Žijící – údaje jen základní."
# Neznámý otec nemanželského dítěte: dict(n="otec neuveden", st="unk", f=[], note="…")

P = {
 1: dict(n="Petr Vojtásek", y="", st="fam", sex="M", f=[],
         note="Žijící – údaje jen základní. Vnuk Jana a Anastázie Vojtáskových."),
 2: dict(n="Otto Vojtásek", y="1931–1984", st="fam",
         f=["* 21. 9. 1931", "† 1984 Slavičín"],
         note="Údaje od rodiny (Petr je jeho syn). Místo narození zatím neznámé – nejspíš Rudimov."),
 3: dict(n="Jindřiška Meislová", y="1938 – ?", st="fam",
         f=["* 24. 3. 1938 Slavičín (?)", "bydlela ve Slavičíně", "† Slavičín (datum doplnit)"],
         note="Provdaná Vojtásková. Podle rodiny ve Slavičíně žila a zemřela; narodit se tam „měla“ – místo narození proto s otazníkem. "
              "Datum úmrtí zatím neznámé."),
 4: dict(n="Jan Vojtásek", y="1908–1982", st="fam",
         f=["* 31. 7. 1908 Rudimov (?)", "velitel hasičů, kapelník a starosta – podle rodiny",
            "největší sedlák („kulak“) v obci – podle rodiny", "bydlel v Rudimově u Luhačovic", "† 26. 6. 1982"],
         note="Data z tužkou psaného zápisu na zadní straně rámu rodinné fotografie; na fotografii v hasičské uniformě "
              "s vyznamenáními. Podle rodiny byl velitelem hasičů, hlavním kapelníkem a starostou (obce Rudimov – ověřit) "
              "a největším „kulakem“, tedy nejbohatším sedlákem – tak komunistický režim po roce 1948 označoval velké hospodáře. "
              "Místo narození Rudimov jen podle rodiny („nejspíše“). Na rámu psáno „Vojtášek“, rodina píše Vojtásek bez háčku."),
 5: dict(n="Anastázie Viceníková (?)", y="1904–1976", st="fam",
         f=["* 16. 4. 1904 Rudimov (?)", "žena v domácnosti", "bydlela v Rudimově u Luhačovic", "† 2. 12. 1976 (?)"],
         note="Provdaná Vojtásková. Rodné příjmení na rámu špatně čitelné (Viceníková / Vicaníková / Vicenáková?). "
              "V datu úmrtí je první číslice přepsaná – 2. 12., nebo 7. 12. 1976. Místo narození Rudimov jen podle rodiny („nejspíše“)."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
 8: ("Vojtáskové", "Rod z Rudimova u Luhačovic na Zlínsku – Jan Vojtásek, hasič, kapelník a starosta."),
 10: ("Viceníkovi (?)", "Rod Anastázie Vojtáskové; rodné příjmení zatím nejisté."),
 12: ("Meislovi", "Rod Jindřišky Vojtáskové, roz. Meislové."),
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
 dict(k=1, n="Miriam Vojtásková, roz. Kovářová", t="Manželka Petra Vojtáska. Žijící – údaje jen základní."),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
 ("Píše se příjmení Vojtásek, nebo Vojtášek?",
  "Otevřené: rodina píše Vojtásek, na rámu fotografie je spíš Vojtášek. Rozhodne matrika."),
 ("Jaké bylo rodné příjmení Anastázie?",
  "Otevřené: na rámu nejspíš Viceníková, možná Vicaníková nebo Vicenáková. Hledat v matrice narozených 1904."),
 ("Kdy přesně zemřela Anastázie?",
  "Otevřené: 2. 12. nebo 7. 12. 1976 (číslice na rámu přepsaná)."),
 ("Kde se Jan a Anastázie narodili a vzali?",
  "Otevřené: rodina myslí, že oba v Rudimově. Sňatek (asi 1928–1931, před narozením Otty) zatím neznámý."),
 ("Byl Jan Vojtásek starostou Rudimova a velitelem tamních hasičů?",
  "Otevřené: tak to říká rodina. Ověřit v kronice obce, v historii hasičského sboru a v novinách."),
 ("Jak se vedlo Janovi jako „kulakovi“ po roce 1948?",
  "Otevřené: podle rodiny byl největším sedlákem v obci. Hledat v archivu MNV Rudimov a JZD (SOkA Zlín)."),
 ("Kdy zemřela Jindřiška Vojtásková, roz. Meislová?",
  "Otevřené: zemřela ve Slavičíně, datum zatím neznámé."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
