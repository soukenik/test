<!-- Metodická příručka (anglicky): rešeršní zpráva „Professional Genealogy in the Czech Lands & Central Europe —
Operating Playbook“, stav 2026-10-09. Autor ve zprávě není uveden. Podle stylu (štítky [FACT]/[INFERENCE], „this run“,
„via subagent“) jde nejspíš o výstup výzkumného nástroje s umělou inteligencí. Do skillu je zařazena jako pracovní
podklad, beze změn obsahu a bez nároku na autorství. Licence MIT repozitáře se na tento soubor nevztahuje.
Jste-li autor a nesouhlasíte se zařazením, ozvěte se prosím na sarsonj@gmail.com – soubor upravíme nebo odstraníme.
Pozor: jde o rešerši k datu 2026-10-09 – adresy, lhůty a ceny ověř, než se na ně spolehneš.
Čti po částech podle potřeby (obsah: §0 opravy, §1 hlavní zjištění, §2 prameny po zemích, §3 časová osa, §4 lhůty, §5 metoda a šablony, §6+ nástroje a ceny). -->

# Professional Genealogy in the Czech Lands & Central Europe — Operating Playbook, State of 2026-10-09


The strongest result for 2026 is that the bottleneck in Central European genealogy has moved. Finding images is no longer the hard part. The hard part is reading them and linking people across record classes, and none of the 2026 AI tools has published accuracy data for Czech, Latin or Kurrent parish entries, so they can't stand in for a professional reading every entry and building proof through land, military and residency records. [INFERENCE — my reading of the evidence below]


**TL;DR**
- Access thresholds really do differ across the six countries in 2026. In the current wording, CZ is 100/75/30 years, AT 100/75/30, DE 110/80/30, PL 100/80/80 and HU 110/86/30 (not the 130/86/30 in the brief). SK has one 100-year rule for transferring all three register types to the state archive. For Czech volumes the whole book stays closed until its last entry clears the threshold. [FACT]
- Online images now go far beyond parish registers: for example, SOA Plzeň finished publishing almost all seigniorial land books (2018–2025). But name search still mostly means 1850–1950 card indexes and volunteer indexes. FamilySearch Full-Text Search has no confirmed Czech, Latin, Slovak, Hungarian or Polish handwriting support, and German is not among its six top languages listed in 2026. [FACT/INFERENCE]
- Recommended operating model: build locality guides first. Read whole books, not indexes. Use house numbers, land transfers and domovská příslušnost (right of domicile) as linkage keys. Treat every HTR or LLM transcript as a finding aid that a human must check against the image. Transkribus publishes validation CERs of 4.5–6.9 % for German Kurrent models. An independent benchmark (Crosilla, Klic & Colavizza, arXiv 2503.15195) measured GPT-4o at 33.5–80.2 % zero-shot CER on non-English historical handwriting. [FACT]


---


## 0. Corrections to baseline


| # | Baseline statement | Correction / extension | Source (seen 2026-10-09) |
|---|---|---|---|
| 0.1 | Brief §5B: "HU 130/86/30" | **Wrong.** The current 2010. évi I. törvény 93/A. § (1) makes registers researchable by anyone after **30 years (deaths), 110 years (births) and 86 years (marriages)**, each counted from the year after the register was created. Several county pages of the Magyar Nemzeti Levéltár (Hungarian National Archives) still describe the 2014 wording: 30 years after death, or 100 years after birth, or 75 years after the entry. Treat those pages as outdated. [FACT] | Nemzeti Jogszabálytár (njt.hu), 2010. évi I. tv.; MNL BéML/ZML/NML pages |
| 0.2 | Brief: "SK (unknown — determine)" | Under zákon č. 154/1994 Z. z. § 5 ods. 3, registers stay at the matričný úrad (registry office) and pass to the state archive **100 years after the last entry for births, marriages and deaths alike**. I found no separate public-access period in that act. Access before transfer runs through the registry office, and its eligibility rules were not verified in this run. [FACT for the transfer rule; access rule not determinable here] | slov-lex.sk; nrsr.sk consolidated text effective 2025-01-01 |
| 0.3 | Baseline: WWI personnel files for cohorts 1887–1900 destroyed (single source, 🟡) | **Now corroborated.** The Kriegsarchiv (Austrian War Archive) director states that the Grundbuchblätter (basic service sheets) for cohorts 1865–1900 stayed in the successor states under Saint-Germain, and that "Der Großteil der in den Nachfolgestaaten verbliebenen Unterlagen ist inzwischen vernichtet worden" (most of what stayed in the successor states has since been destroyed). Familia Austria, citing the Kriegsarchiv, gives the Bohemia/Moravia/Silesia holdings as "Geburtsjahrgänge 1865–1886 (bis 1864 fragmentarisch, 1887–1898 großteils skartiert!)": cohorts 1865–1886 survive, earlier cohorts are fragmentary, and 1887–1898 were largely shredded. [FACT (ÖStA) / CLAIM (cohort split)] | ÖStA, Tepperberg, "Quellen zur genealogischen Forschung im Kriegsarchiv Wien" (PDF, opened); Familia Austria "Militär" |
| 0.4 | Transkribus: API only on paid tier; new API promised for summer 2026 (🟡) | The Transkribus API page now reads "Generally available". It says the API "comes with every plan from Scholar upwards" and that API jobs use credits "at half the rate". Older pricing and credits pages still restrict the API to the Organisation plan. That is a conflict between the vendor's own pages; the newer API page is probably current. [CLAIM — vendor self-report, conflicting] | transkribus.org/text-recognition-api; /pricing; /credits (via research subagent) |
| 0.5 | "No published accuracy measurements for LLM vision or Transkribus on Kurrent + Latin proper names" | **Partly outdated.** Transkribus publishes validation CERs for each model, for example German Kurrent (ID 36508) at 5.40 %. An independent test set for late-19th-century Kurrent (Journal of Open Humanities Data) measured 5.90 % mean CER for that generic model. A 2025 benchmark (Crosilla, Klic & Colavizza, Journal of Documentation 81/7) found GPT-4o zero-shot at 33.53 % CER on LAM (Italian, 18th c.) and up to 80.20 % on READ2016 (German, 15th–19th c.), a range of 33.5–80.2 % on non-English historical sets. **Still missing:** any measurement on Czech/Latin parish entries, or name-level accuracy. [FACT] | transkribus.org model pages; JOHD 10.5334/johd.46; arXiv 2503.15195 |
| 0.6 | FamilySearch "expanding full-text search to more languages" | FamilySearch's 2026 RootsTech handout gives the top languages by volume as English, Spanish, Italian, Portuguese, French and Dutch, with "Over 8,000 record collections" and "About 2.5 billion images". **German, Latin, Czech, Polish and Hungarian are not listed.** I could not confirm any Central European collection, because the collection list requires login. [FACT/not determinable] | FamilySearch handout (D. Ouimette, 2026), via subagent |
| 0.7 | AT 100/75/30 | Confirmed (PStG 2013 § 52 Abs. 5). The 100-year and 75-year periods apply only "sofern die Eintragung nicht eine lebende Person betrifft" (provided the entry does not concern a living person). **Conflict on the start of the count:** the statute counts from the entry ("seit der Eintragung"), while the Diözesanarchiv Wien counts from the last processing of the book ("nach der letzten Bearbeitung"). Church registers kept after 1938 are purely ecclesiastical books with no legal right of inspection (Salzburg archdiocesan archive). [FACT] | RIS BGBl. I 16/2013; eds.at; erzdioezese-wien.at |
| 0.8 | DE 110/80/30, PL 100/80/80 | Both confirmed. DE: PStG § 5 Abs. 5; death registers of the Sonderstandesamt Bad Arolsen have **80** years, not 30. PL: Prawo o aktach stanu cywilnego (2014), art. 28 and art. 128, counted from the closing of the book; transfer to the state archive within 2 years. [FACT] | buzer.de/dejure.org (PStG); MSWiA; archiwa.gov.pl |
| 0.9 | Vienna Meldezettel (registration slips) listed as a source | WStLA (Vienna City and State Archives) holds police registration records from about **1904–1975**, only where the person deregistered by 1975. Originals cannot be inspected. Answers come by written request **within 2 months** at **€35 per started half hour, charged even when nothing is found** (Gemeinderat resolution 2025-09-24). The 19th-century "A-Antiquariat" was destroyed by the Zentralmeldeamt, except for about 200 famous people. FamilySearch nonetheless shows a "Wiener Meldezettel 1850–1896" collection, which is a **conflict** (see §11). [FACT] | wien.gv.at; Wien Geschichte Wiki "Meldewesen"; oefr.at |
| 0.10 | Heimatortskartei (expellee home-locality card index) not covered | The Kirchlicher Suchdienst (church tracing service) closed on 2015-09-30. Its Heimatortskarteien are now Bundesarchiv holding B 530 KARTEIEN at Bayreuth (Lastenausgleichsarchiv), usable since January 2017. They register over 20 million people. All tracing-service card indexes together come to 33,300 boxes and nearly 40 million cards. A finding aid "Heimatortskartei Regensburg (Sudetendeutsche)" is published as XLSX. The OÖ Landesarchiv page still sends researchers to Passau and is outdated. [FACT] | bundesarchiv.de/Bayreuth; DDB/Archivportal-D; landesarchiv-ooe.at |


---


## 1. Executive summary — 12 highest-leverage findings


1. In 2026 the whole Czech land-book layer has become an online, image-only source in some regions: SOA Plzeň has published "všechny pozemkové knihy z fondů velkostatků" (all land books from the estate fonds) apart from a few physically unfit volumes, after digitising them in 2018–2025. [FACT]
2. SOA Praha has put online land books and soupisy poddaných (lists of subjects) from 26 named estate fonds; its eBadatelna news page (2024-07-06) says "Celkem se jedná přibližně o 900 svazků" (about 900 volumes in total). That is a fraction of its estate holdings, so Central Bohemian land-book research is still mostly done in the reading room. [FACT/INFERENCE]
3. Hungary's current 110/86/30 rule is stricter for births than the 2014 version that county archive web pages still quote. Check njt.hu before ordering anything. [FACT]
4. Slovakia applies one 100-year transfer rule to all three civil register types. So marriages and deaths after about 1926 stay at the matričný úrad, unlike CZ, AT and DE where deaths open after 30 years. [FACT/INFERENCE]
5. Common-soldier Grundbuchblätter for Czech-domiciled men born 1887–1898 are largely lost. The Kriegsarchiv itself says most material left with the successor states has been destroyed. For WWI-generation soldiers, plan around Verlustlisten (casualty lists), the Vienna loss card indexes (AT-OeStA/KA VL: "ca. 40 Millionen Karteikarten", cohorts about 1865–1900, including the Kriegsgefangenenkarteien and the Totenkartei) and parish records. [FACT]
6. The Kriegsarchiv's military matriky (military parish registers: 1633–1938, about 8,000 volumes plus 322 boxes, closed series 1815–1920) are under a 100-year block and are searched by regiment. You need the regiment before you can search. [FACT]
7. Before 1820, a common soldier can be found only in the Musterlisten (muster rolls, 1740–1820, 12,613 boxes) by working through year by year with a known regiment. Wrede's recruitment-district table (Beilage VII) maps a locality to its regiment. [FACT]
8. Berní rula 1654 (the 1654 tax roll) lists only taxpayers with property, not podruzi (lodgers) or čeleď (servants). The 1651 Soupis poddaných podle víry (list of subjects by faith) lists whole families with ages but is incomplete and has no name index. Pre-1700 peasant links therefore rest on the 1651 list plus land books. [FACT]
9. The best-documented Kurrent HTR (Transkribus German Kurrent) has a 5.4 % validation CER and 5.9 % mean CER on an independent late-19th-century test set. That is good enough for search, not for unattended name extraction. [FACT/INFERENCE]
10. General-purpose LLM vision models are not a safe default for non-English historical handwriting. In Crosilla et al. (2025), GPT-4o measured 33.5–80.2 % CER there (80.20 % on the German READ2016 set), against 1.75 % on modern English (IAM). [FACT]
11. Indexes are partial by design. The FamilySearch Slovakia collection is explicitly "incomplete", with mainly baptisms indexed. In 2018 Geneteka (PTG) had 15,000 records for Lower Silesia, the third-weakest region after lubuskie (3.9k) and zachodniopomorskie (4k), against 6.7 million for Mazowieckie (More Maiorum, 2018-06-20, reporting the PTG president). The current Geneteka homepage (undated) states over 47 million indexes from over 4,500 parishes. A negative index result says little about whether a record exists. [FACT/CLAIM]
12. Czech professional pricing is published per record found: about 180–400 Kč per entry, more for the 17th–18th century. A 5–7-generation direct line costs about 6,000–22,600 Kč; a full 6–7-generation pedigree about 24,000–55,000 Kč. These are firm self-reports. [CLAIM]


---


## 2. Master inventory tables per territory


**Column key:** Search = none / img (image-only) / idx (name index) / ft (full-text). PL/img = permalink per image. Bulk = bulk download. Machine = machine-access policy. Pub = public-access rule. Verified = status in this run. "seen" means returned by web_search on 2026-10-09. "opened" means fetched. "not opened" means the URL is from baseline or general knowledge and was not checked. Where a cell is not determinable it says n.d.


### 2.1 Czech Republic (Bohemia, Moravia, Czech Silesia)


| Record class | Years | Holder (archive + fond) | Online | Search | PL/img | Bulk | Machine | Pub | Verified | Tag |
|---|---|---|---|---|---|---|---|---|---|---|
| Matriky (parish registers, Catholic, Protestant after 1781) | c. 1600s–1950 (state duty to 1949) | 8 regional archives (SOA/ZA/MZA/AHMP), fond "Sbírka matrik" | yes (baseline portals) | img | portal-dependent (n.d. this run) | Zámrsk zip (2020, unverified) | badatelský řád (reading-room rules) per archive, n.d. | 100/75/30 from last entry (zákon 301/2000 Sb.) | baseline; not re-opened | [FACT baseline] |
| Jewish registers (HBMa) | 1784–1949 | Národní archiv | yes (Digitální badatelna NA) | img | n.d. | n.d. | n.d. | as above | baseline | [FACT baseline] |
| Pozemkové / gruntovní knihy (seigniorial land books), urbáře (manorial registers), soupisy poddaných | 15th c.–1850 (estate books); 1871–1950/64 at cadastral offices | SOA, fonds "Velkostatek X" | SOA Plzeň Porta fontium (all estate land books, 2018–2025); SOA Praha eBadatelna (about 900 vols, 26 estates); ZA Opava Digitální badatelna (since 2012); SOA Třeboň digi (claimed complete); SOA HK digitising (Barchůvek, Bělohrad, 2025-11-20); MZA via ARON (claim, 2024) | img | n.d. | n.d. | n.d. | archive law; post-1871 books at katastrální úřad (cadastral office) | seen 2026-10-09 (soaplzen.gov.cz, ebadatelna.soapraha.cz, archives.cz, vychodoceskearchivy.cz) | [FACT] Plzeň/Praha/Opava/HK; [CLAIM] Třeboň, MZA |
| Soupis poddaných podle víry 1651 | 1651 | NA, Stará manipulace, sign. R 109/45 | edition PDFs by kraj (region) from NA (e.g. Berounsko 2007, e-book) | full text in edition PDF; no name index | n/a | PDF | n.d. | open | seen (nacr.cz) | [FACT] |
| Berní rula 1654 | 1654 | NA (originals); editions | general index: Červený, Libri 2003 (DNNT/Kramerius remote, claim) | idx (printed, by surname) | n/a | n/a | DNNT terms | open | seen (ptejteseknihovny.cz) | [CLAIM] |
| Lánové rejstříky (Moravian hide registers) 1669–79; Tereziánský katastr (Theresian cadastre) 1713–57; Josefský katastr (Josephine cadastre) 1785–89 | as named | NA (Bohemia); MZA (Moravia) | n.d. | n.d. | n.d. | n.d. | n.d. | open | not verified this run | [CLAIM] (Theresian cadastre: NA/MZA per secondary site) |
| Censuses 1857–1910, 1921, 1930 | as named | SOkA (district archives)/MZA/AMB (Brno City Archives) | partial (baseline) | img | n.d. | n.d. | n.d. | open (old) | baseline | [CLAIM] |
| Police registrations (Prague) | 1850–1914/18 | NA | yes | idx | n.d. | n.d. | n.d. | open | baseline | [FACT baseline] |
| Stabilní katastr (stable cadastre) indicative sketches | 1824–43 | ČÚZK | yes | img by cadastral area | n.d. | n.d. | n.d. | open | baseline | [FACT baseline] |
| Military kmenové listy (service sheets) | cohorts 1865–1910 (officers to 1905) | VÚA–VHA Praha | partial (card indexes, baseline) | idx (some) | n.d. | n.d. | VÚA refused machine fetch (baseline) | request | czecharchives.com (seen) | [CLAIM] |
| Pozůstalostní spisy (probate files), sirotčí knihy (orphan books), svatební smlouvy (marriage contracts) | 17th c.–1950 | SOkA (okresní soud = district-court fonds); estate fonds | mostly offline; some inside land-book series (Opava lists "knihy svatebních smluv, knihy testamentů a sirotčí registra" as land-book types) | img where online | n.d. | n.d. | n.d. | archive law | seen (archives.cz) | [FACT] Opava; rest [INFERENCE] |
| Kroniky (municipal/parish/school chronicles) | 19th–20th c. | SOkA | partly (ZA Opava "Kroniky" section; SOA Praha) | img | n.d. | n.d. | n.d. | open | seen | [FACT] |


### 2.2 Slovakia


| Record class | Years | Holder | Online | Search | Pub | Verified | Tag |
|---|---|---|---|---|---|---|---|
| Cirkevné matriky (church registers: RC, Lutheran, Reformed, Jewish) | 1592–1895 (state duplicates/church books to about 1910/1935 on FamilySearch) | Štátne archívy (state archives), "Zbierka cirkevných matrík" (books nationalised in the mid-20th c.) | FamilySearch "Slovakia, Church and Synagogue Books, 1592-1935" (CID 1554443; catalogue title 1592-1910) | img + partial idx (mainly baptisms; coverage table) | archive law | seen (FS Wiki, CGSI) | [FACT] |
| Image counts | — | — | CGSI: "over 1.6 million images" (undated); FS 2012: 1,098,483 indexed records + 15,823 images; Forebears: "around 14 million" entries | — | — | seen | [CLAIM] — figures conflict and are undated |
| Archive-side online matriky | — | ŠA | CGSI (undated): "the State Regional Archives in Slovakia do not have church books available online" | none | — | seen | [CLAIM] — possibly outdated; Slovakiana not checked this run |
| Štátne matriky (civil registers) | 1895-10-01 → | Matričný úrad → ŠA after 100 years | no | none | 100-year transfer, all classes (zákon 154/1994 § 5(3)) | seen | [FACT] |
| 1869 census | 1869 | ŠA; FamilySearch | images (FS) | img | open | seen (genealogyblog, FS) | [CLAIM] |


### 2.3 Austria (incl. Vienna, Burgenland)


| Record class | Years | Holder | Online | Search | Pub | Verified | Tag |
|---|---|---|---|---|---|---|---|
| Catholic Matriken (Altmatriken = pre-1939 registers) | 16th c.–1938 | Diocesan archives | Matricula (data.matricula-online.eu). Parishes per fonds as listed: Erzdiözese Wien 567; Linz 427; St. Pölten 410; Graz-Seckau 358; Tirol (Landesarchiv) 353; Gurk 328; Salzburg 137; Vorarlberg 127; Burgenland Rk. 2 (Eisenstadt runs its own portal matriken.at, "not yet fully completed", updates to 2026-04-22) | img; no index | 100/75/30 (PStG 2013 § 52) | seen 2026-10-09 | [FACT] |
| Protestant registers A.B./H.B. (Lutheran/Reformed) | 1783– | Ev. Kirche | Matricula: Wien Ev. A.B. 16, H.B. 4; Kärnten 29; Steiermark 25; NÖ 17; OÖ 9; Burgenland 29; "Altösterreich (evangelisch)" 10 | img | same | seen | [FACT] |
| Old Catholic duplicates | after state recognition (1877) | WStLA ("Matriken-Zweitschriften der Altkatholiken") | n.d. | — | births/marriages restricted 100/75; deaths unrestricted | seen (WAIS) | [FACT] |
| Military matriky | 1633–1938 | ÖStA/KA Matr (about 8,000 vols + 322 boxes) | no | regiment list; WWI death matriky via card index | **100-year block** | opened | [FACT] |
| Grundbuchblätter | 1820–1918 (cohorts about 1790–1900), about 17,000 boxes | ÖStA/KA Pers GB | FamilySearch microfilm/digitised "Diverse" series for about 1820–1864 cohorts (662 rolls per czecharchives) | alphabetical (old series) | request | opened (ÖStA) | [FACT]; roll count [CLAIM] |
| Musterlisten & Standestabellen | 1740–1820 (cohorts about 1720–1800), 12,613 boxes | ÖStA/KA Pers MLST | partly filmed (n.d.) | by regiment/year | open | opened | [FACT] |
| WWI loss card indexes | 1914–18, about 40 million cards | ÖStA/KA VL | no | phonetic card index (written request) | — | opened | [FACT] |
| Meldeunterlagen Wien (registration records) | about 1904–1975 | WStLA (MA 8) | request only | archive staff search | €35 per started half hour; reply ≤2 months | seen | [FACT] |
| Meldezettel 1850–1896 | 1850–1896 | WStLA / FamilySearch | FS collection 1404451 (indexed) | idx | open | seen (oefr.at) | [CLAIM] — conflicts with "A-Antiquariat destroyed" |
| Totenbeschauprotokolle (Vienna death inspection records), Verlassenschaften (probate) | 17th–20th c. | WStLA | partly (n.d.) | n.d. | Wiener Archivgesetz | seen (wien.gv.at mentions) | [FACT] existence |


### 2.4 Poland (Cieszyn Silesia, Upper Silesia, Galicia)


| Record class | Years | Holder | Online | Search | Pub | Verified | Tag |
|---|---|---|---|---|---|---|---|
| Civil-status books (USC = civil registry office) | civil registration in the Prussian partition from 1874 (not re-verified); uniform secular registration from the decree of 1945-09-25 | USC → AP (state archives) after 100/80 years | szukajwarchiwach (not opened) | img | 100 births / 80 marriages & deaths from closing of book; transfer within 2 years | seen (MSWiA, archiwistyka.pl) | [FACT] |
| Parish metrical books (metryki) | 16th c.– | diocesan archives / AP | partly | Geneteka idx | diocesan rules (n.d.) | seen | [CLAIM] |
| Geneteka (PTG index) | — | Polskie Towarzystwo Genealogiczne | geneteka.genealodzy.pl | idx | — | seen | 25 M records (2018-06-18, PTG president, [FACT]); 57 M (undated, ZTG Pomerania); about 67 M, >4,500 parishes (undated, surname.pl) [CLAIM] |


### 2.5 Germany (Sudeten-German expellee material; border migration)


| Record class | Years | Holder | Online | Search | Pub | Verified | Tag |
|---|---|---|---|---|---|---|---|
| Standesamt registers (civil registers) | 1876-01-01 → (Prussia 1874, not re-verified) | Standesamt → municipal/Land archive | n.d. | none | 110/80/30 by register year (PStG § 5(5)); then archive law | seen | [FACT] |
| Heimatortskartei Sudetendeutsche (HOK Regensburg) | residence as of 1939-09-01 and postwar address | BArch Bayreuth, B 530 KARTEIEN | finding aid XLSX | written request | Bundesarchivgesetz; data protection for living people | seen | [FACT] |
| Lastenausgleich files (postwar compensation for expellees) | 1949– | BArch Bayreuth | no | request | BArchG | seen | [FACT] |
| Gemeindeseelenlisten / Gemeindevermisstenlisten (community population and missing-persons lists, incl. Sudetenland, Protectorate) | 1950s | BArch B 530 (2,885 units) | no | request | BArchG | seen | [FACT] |


### 2.6 Hungary (record-keeper for Slovakia before 1918)


| Record class | Years | Holder | Online | Search | Pub | Verified | Tag |
|---|---|---|---|---|---|---|---|
| State civil registers (állami anyakönyv, archive duplicates) | 1895-10-01 → (start date not re-verified) | MNL county archives (duplicates to 1980-12-31); anyakönyvi hivatal (registry office) | FamilySearch (n.d.) | n.d. | 110/86/30 after year of register (93/A § (1)); research requests at the archive for registers to 1980 (93/B); special-category data barred for 60 years after death | seen | [FACT] |
| Church registers held by church archives | — | e.g. Szeged-Csanád diocesan archive: "Az anyakönyvek csak a keletkezésüktől számított 90. év után kutathatók" (registers can be researched only after 90 years from creation); another church archive: baptisms to 1920, marriages to 1950, deaths to 1980 | — | — | church-specific | seen | [FACT] (archive rules) |


### 2.7 Search-mode map 1650–1950 (Czech lands; others in summary rows)


Grid legend: **N** name-searchable at scale; **I** image-only online; **O** mostly offline/reading room; **–** class does not exist. This is my reading of the inventory above, not a measured map. [INFERENCE]


| Class \ decade | 1650s | 1700s | 1750s | 1780s | 1800s | 1830s | 1850s | 1880s | 1900s | 1920s | 1940s |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Matriky | I | I | I | I | I | I | I | I | I | I/O (closure) | O (registry office) |
| Land books (estate) | I (Plzeň, Opava, Třeboň); O elsewhere | same | same | same | same | same | – (estates end 1850) | – | – | – | – |
| Land books (court, after 1871) | – | – | – | – | – | – | – | O (cadastral office/archive) | O | O | O |
| 1651 list / 1654 roll | N (printed index) | – | – | – | – | – | – | – | – | – | – |
| Censuses | – | – | – | – | – | – | I (partial) | I/O | I/O | O | – |
| Police/residence records | – | – | – | – | – | – | N (Prague) | N (Prague) | N (Prague) | O | O |
| Military personnel | – | – | O (Musterlisten) | O | O | O (GB, Vienna) | O | O (VHA) | lost (1887–98 cohorts) | O | O |
| Newspapers/printed | – | – | – | – | ft (Kramerius/ANNO, OCR quality varies) | ft | ft | ft | ft | ft | ft |
| **SK** church books | – | I (FS) | I | I | I/N partial | I/N | I/N | I/N | O (civil) | O | O |
| **AT** Matriken | I | I | I | I | I | I | I | I | I | I (to 1938) | O |
| **PL** metryki | I/N (Geneteka varies) | … | … | … | … | … | … | … | … | … | O (USC) |


---


## 3. Timeline of record-keeping milestones


| Date | Jurisdiction | Milestone | What changes for the researcher | Tag |
|---|---|---|---|---|
| 1563 | Catholic Church | Council of Trent orders baptism and marriage registers | Earliest Catholic registers in theory. In Bohemia very few survive before about 1620–1650. | [CLAIM] general knowledge |
| 1587 | Upper Hungary | Earliest Slovak church book (Košice baptisms) | SK coverage can start before CZ, but Ottoman and rebellion-era losses are heavy | [FACT] FS Wiki |
| 1633 | k. k. army | Earliest surviving military matriky | Soldiers' families may appear outside the home parish | [FACT] ÖStA |
| 1650-11-16 → 1651 | Bohemia | Patent ordering the Soupis poddaných podle víry (list of subjects by faith) | Family-level list with ages; incomplete, because some regions listed only non-Catholics | [FACT] |
| 1654 | Bohemia | Berní rula (tax roll) | Holders of taxable land only; the anchor for house/grunt (holding) continuity | [FACT] |
| 1669–79 | Moravia | Lánové rejstříky (hide registers) | Moravian counterpart to the Berní rula | [CLAIM] |
| 1740 | Habsburg army | Musterlisten series begins (to 1820) | Soldier's age, origin, religion, family; you need the regiment | [FACT] |
| 1770/71 | Bohemia/Moravia | Conscription and house numbering | Čísla popisná (house numbers) become a linkage key; watch for later renumbering | [CLAIM] |
| 1781 | Monarchy | Toleranzpatent (Patent of Toleration) | Lutheran/Reformed congregations form; non-Catholics still often entered by the Catholic priest | [CLAIM] |
| 1784-02-20 | Cisleithania | Josephine register patent: separate N/O/Z books (births/marriages/deaths) with prescribed columns | Columnar forms (good for extraction, but the worst case for full-text HTR) | [FACT] baseline/Stellner |
| 1820 | k. k. army | Grundbuchblätter replace Musterlisten | An individual service sheet with civilian occupation, marriage and children | [FACT] |
| 1850 | Cisleithania | Okresní hejtmanství (district administration) and soudní okresy (court districts) replace estates | Land and orphan records move from estate fonds to court fonds | [CLAIM] |
| 1868 | k. k. army | Grundbuchblätter decentralised to replacement units | Post-1868 sheets were not sent to Vienna, hence the losses after 1918 | [FACT] |
| 1871 | Cisleithania | Modern court land books (pozemkové knihy) | Kept at cadastral offices to 1950/64; reading room only | [CLAIM] |
| 1876-01-01 | German Empire | Standesamt registration | Civil registers for Saxony/Bavaria border migrants | [FACT] (Bayreuth series starts 1876) |
| 1895-10-01 | Hungary (incl. SK) | State civil registration | Second, state series; church books continue | [CLAIM] not re-verified |
| 1904 | Vienna | Start of the surviving police registration series (WStLA) | Earlier Meldezettel largely destroyed (see conflict in §11) | [FACT] |
| 1914–18 | Monarchy | Verlustlisten (casualty lists), loss card indexes (about 40 M cards), hospital sheets (about 6,300 boxes) | Main substitute for lost personnel sheets | [FACT] |
| 1919 | Saint-Germain | GB cohorts 1865–1900 of non-Austrian domicile stay in successor states | Czech soldiers' sheets in VHA Prague; most later destroyed | [FACT] |
| 1939-01-01 | Austria | Standesämter (civil registration) introduced | Church books after 1938 are purely ecclesiastical, with no legal right of inspection | [FACT] |
| 1945-09-25 | Poland | Decree on uniform secular civil registration | USC books from 1945/46 on | [FACT] |
| 1945–47 | CZ/DE | Expulsion; Kirchlicher Suchdienst founded 1945-08-01 | HOK cards record pre-1939 residence and postwar address | [FACT] |
| 1950-01-01 | Czechoslovakia | State matriky (zákon 268/1949 Sb.) | Parish books stop being state records | [CLAIM] not re-verified |
| 2009-01-01 | Germany | PStG reform: retention periods 110/80/30 | Older registers move to archives | [FACT] |
| 2013 | Austria | PStG 2013 | Codifies 100/75/30 | [FACT] |
| 2014-07-01 | Hungary | Archive research regime for state duplicates | Later amended to 110/86/30 | [FACT] |
| 2015-09-30 | Germany | Kirchlicher Suchdienst closes; HOK to BArch (2016/2017) | Requests now go to BArch Bayreuth | [FACT] |


---


## 4. Access law matrix 2026


| Country | Statute & section | Births | Marriages | Deaths | Count from | Latest open in 2026 (my computation) | Earlier access | Office | Fees/turnaround | Tag |
|---|---|---|---|---|---|---|---|---|---|---|
| CZ | zákon 301/2000 Sb. (matriky law) | 100 | 75 | 30 | **last entry in the volume** | birth volumes with last entry ≤ 1926-10-09; marriages ≤ 1951-10-09; deaths ≤ 1996-10-09 (death books 1951–96 are still at the matriční úřad, the registry office) | the person, spouse/partner, parents, children, siblings, with proof | matriční úřad | n.d. this run | [FACT baseline] / [INFERENCE] dates |
| SK | zákon 154/1994 Z. z. § 5(3) | 100 (transfer) | 100 | 100 | last entry | books with last entry ≤ 1926 at the archive; everything later at the registry office | not verified this run | Matričný úrad | n.d. | [FACT]/n.d. |
| AT | PStG 2013 § 52(5), § 62–63, § 72 | 100 | 75 | 30 | entry (statute) vs last processing (Diözesanarchiv Wien), **conflict** | births ≤ 1926; marriages ≤ 1951 if no living person is affected; deaths ≤ 1996 | person concerned, anyone whose civil status is affected, legal interest | church archives (Altmatriken, pre-1939); Standesamt 1939+ | n.d. | [FACT] |
| DE | PStG § 5(5), § 7(3), § 55(3), § 61 | 110 | 80 | 30 (Bad Arolsen 80) | register year | births ≤ 1915; marriages ≤ 1945; deaths ≤ 1995 (handed over at the start of the following year; Bayreuth 2025: births 1876–1914, marriages to 1944, deaths to 1994) | direct relatives (parents, grandparents, children, grandchildren, siblings) or legal interest; a further archive-law period may apply (Bavaria municipal archive: 10 years after death / 80 after birth) | Standesamt → archive | n.d. | [FACT] |
| PL | Prawo o aktach stanu cywilnego 2014, art. 28, 128 | 100 | 80 | 80 | closing of the book | births ≤ 1925; marriages/deaths ≤ 1945; transfer within 2 years, so archive availability lags | before expiry: USC under civil-status law; after expiry but before transfer: archive-law rules (NSA ruling) | USC → AP | n.d. | [FACT] |
| HU | 2010. évi I. tv. 93/A–93/B | 110 | 86 | 30 | year after the register's creation | births ≤ 1915; marriages ≤ 1939; deaths ≤ 1995 | descendants and others listed in (3) (wording not verified); scientific research after 30 years with a research plan | anyakönyvi hivatal; MNL for duplicates to 1980-12-31 | archive preparation 21 days, extendable once by 21 days (2014 regime, MNL pages) | [FACT] |


**Practical consequences** [INFERENCE — my reading]:
- **Czech volume closure.** A Czech birth book running 1890–1935 stays closed until 2035, even for its 1890 entries. Order an extract through the matriční úřad, or check whether a duplicate or index volume closes earlier.
- **Slovakia** is the outlier for deaths. A 1960 death is public in CZ, AT, DE and HU but stays at the registry office in SK.
- **DE and PL** count from the register year or the closing of the book, not from the individual entry. Their threshold years therefore jump once a year.
- **Austria:** after 1938 the church books carry no right of inspection, so for 1939+ events use the Standesamt.
- **GDPR.** It does not protect the dead, but the Hungarian 60-year bar on special-category data (religion, illegitimacy, cause of death) shows that national law can add protection. When you publish a shared tree, strip those fields for anyone who died within the last 60 years.


---


## 5. Professional method


### 5.1 Workflow (operational)


1. **Question and hypothesis.** One person, one event, one stated hypothesis.
2. **Locality analysis.** Build a locality guide before searching (template 5.2.4). Chain: obec (municipality) → fara/lokálie (parish/local chaplaincy, before and after 1784–90) → panství/Herrschaft (estate; before 1850) → kraj (region) → after 1850 okresní hejtmanství + soudní okres (court district, for land/orphan/probate) → archive and fond → book with years.
3. **Inventory.** List every record class that exists for that locality and period, its search mode and its access status. This is the §2 table filtered to one place.
4. **Extraction.** Use one template per record type and transcribe every field, including witnesses, godparents, house number and the midwife.
5. **Whole-book reading.** Read every entry for the surname and the house number across the full book, not just index hits. Extract whole households.
6. **Correlation.** Build a timeline with house number × person × event × status term. Test conflicts explicitly.
7. **Proof argument.** Write one for any conclusion that rests on indirect evidence (template 5.2.5).
8. **Research log.** Record every search, including negative results with their scope (template 5.2.3).
9. **Write to tree.** Only with a citation down to image level. Record conflicts as notes; set the living-person flag where needed.


### 5.2 Templates


#### 5.2.1 Extraction schemas (YAML; one per record type)


```yaml
baptism_1784plus:        # Josephine columnar form
  citation: {archive, fond, inv_c, sign, book_type: N, years, folio, image_no, permalink}
  entry_no:
  date_birth:            # as written + ISO
  date_baptism:
  house_no:              # čp. as written; flag renumbering era
  locality:              # village as written + normalized + gazetteer ID
  child: {given_as_written, given_normalized, sex}
  legitimacy:            # ehelich/unehelich/legitimus/illegitimus + marginal legitimation text
  father: {name, status_term, occupation, residence, religion, parents_if_given}
  mother: {name, maiden, father_of_mother, status_term_of_her_father, residence}
  godparents: [{name, status, residence, relation_hint}]
  midwife: {name, trained: y/n}
  officiant:
  marginal_notes: [{text, date, authority}]   # name change, legitimation, death, marriage
  transcriber_confidence: {names: 0-1, dates: 0-1}
  read_by: {human|htr_model_id|llm_model}, verified_by_human: bool


marriage_1784plus:
  citation: {...}
  date:
  groom: {name, age, house_no, locality, status, occupation, religion, marital_state(ledig/Witwer), parents:{father, mother_with_maiden}}
  bride: {..., widow_of: }
  witnesses: [{name, status, residence}]
  banns/dispensations: {consanguinity_degree, dispensation_ref}
  consent: {Ehekonsens/povolení vrchnosti, guardian_name}


burial_1784plus:
  citation: {...}
  date_death, date_burial, house_no, locality
  deceased: {name, status_term, occupation, religion, sex, age_years, age_months, age_days}
  spouse_or_parents_named:
  cause_of_death:
  examiner/Totenbeschauer:
  computed_birth_window: {from: , to: }   # age ± tolerance (see 5.3.7)


land_transfer (gruntovní/pozemková kniha):
  citation: {archive, fond: "Velkostatek X", inv_c, book_title, folio, image_no, permalink}
  holding: {grunt_name, house_no, category: lán/chalupa/domek, area}
  seller/previous_holder: {name, relation_to_buyer}
  buyer: {name, relation_to_seller}
  price, payment_schedule (vejrunky = instalments)
  heirs_paid_out: [{name, relation, share, date_paid}]    # siblings = filiation proof
  vymínek/výměnek (retirement allowance): {beneficiaries, rights}
  date, witnesses, estate_officer


orphan_book_entry: {citation, deceased_parent, date, orphans:[{name, age, guardian, inheritance_share, later_receipt_date}]}
soupis_1651: {citation, kraj, panství, village, household_head, status, occupation, age, religion, members:[{name, relation, age, religion}], conversion_hope}
grundbuchblatt: {citation, name, birth_year, birth_place, Heimatrecht_place, religion, marital_state, civilian_occupation, regiment, assentiert_date, wife/children}
```


#### 5.2.2 Citation templates and permalink handling


| Portal | Citation pattern | Permalink pattern | Tag |
|---|---|---|---|
| Czech regional archive (any) | `[Archiv], fond [Sbírka matrik / Velkostatek X], inv. č. [n], sign. [n], kniha [N/O/Z, roky], fol. [n], snímek [n], trvalý odkaz [URL], přístup [YYYY-MM-DD].` (archive, fond, inventory no., shelf mark, book, folio, image, permalink, accessed) | not opened this run, so record the portal's own "trvalý odkaz" (permalink) button value per image | [INFERENCE] |
| Matricula | `[Diocese], [Pfarre], [Buchtyp] [Signatur], [years], p./image [n], URL, accessed.` | parish/book/image URL path (not verified this run) | [INFERENCE] |
| FamilySearch | `"[Collection title]," images, FamilySearch, DGS [no.], image [n], accessed [date]; citing [archive], [fond].` DGS number = image-group number, which FTS also exposes as a filter | ark: URL per image | [CLAIM] |
| ÖStA/KA | `ÖStA, KA, Pers GB [Reihe], [Karton], [name], accessed.` (signatures as in archive information system, e.g. AT-OeStA/KA Pers GB) | archivinformationssystem.at | [FACT] signature format |
| BArch | `BArch, B 530 KARTEIEN, HOK Regensburg, [Ort], [card].` | invenio (not opened) | [INFERENCE] |


#### 5.2.3 Research log (one row per search)


| log_id | date | researcher/agent | question_id | source (archive/fond/book/years) | search scope (all entries / index only / years x–y) | names & variants searched | result (positive/negative/ambiguous) | images cited | next action |
|---|---|---|---|---|---|---|---|---|---|


Rule: a negative result is valid only with its scope stated. "Not found in Z book 1784–1820, every entry read" is evidence. "Not in index" is not.


#### 5.2.4 Locality guide (fill once per village)


```yaml
locality: {name_cz, name_de, name_hu/pl, gazetteer_ids, cadastral_area}
parish_history: [{years, parish/lokálie, diocese, archive, notes: "lokálie 1786; before: fara X"}]
protestant_jewish: [{years, congregation/rabbinate}]
estate (panství/Herrschaft) to 1850: {name, fond, archive, land_books:[{inv_c, years, online_url}]}
post-1850: {okresní hejtmanství, soudní okres, SOkA}
house_numbering: [{year: 1770/71, scheme}, {renumbering_year, concordance_source}]
censuses: [{year, holder, online}]
military: {recruitment_regiment (Wrede table), years}
losses: [{class, years, cause}]
gazetteers_checked: [Retrospektivní lexikon obcí, Historický lexikon obcí, GenTeam/oefr gazetteer, Helységnévtár]
```


#### 5.2.5 Proof-argument skeleton


1. **Question:** identity or relationship, stated precisely.
2. **Answer:** conclusion with confidence level.
3. **Sources searched:** pointer to the log rows, including negative searches.
4. **Direct evidence:** each item cited to the image.
5. **Indirect evidence:** each item with the inference it supports.
6. **Conflicts and their resolution:** the evidence for each side, which source is more reliable and why (original vs derivative, informant, time from the event).
7. **Exclusion of alternatives:** list every other same-name candidate in the parish and the reason each is rejected.
8. **Conclusion:** restate it, and say what new evidence would overturn it.


### 5.3 Linkage techniques (worked examples are constructed illustrations [INFERENCE])


| # | Technique | Worked example | Pitfall |
|---|---|---|---|
| 1 | House-number continuity | Jan Novák at čp. 12 in Z 1820 (age 60) and a Jan Novák at čp. 12 in the 1788 marriage book: same holding. Check renumbering against the indicative sketch (1824–43). | Renumbering after fire or new building splits a village; one house can have two numbers over time |
| 2 | House names (jména po chalupě, vulgo) | "Wenzel Schmid vulgo Bauer" — the grunt name survives a change of holder; the land book explains it | A grunt name can pass to a son-in-law, so it is not a surname |
| 3 | FAN (friends, associates, neighbours) clusters | The same 3 godparent couples across 8 baptisms in 1790–1810 mark one family; a godparent change can mark a remarriage | Godparents often came from fixed "kmotrovské" (godparent) families, not relatives |
| 4 | Status terms | sedlák (farmer) → výměnkář (retired holder on a výměnek allowance) in the same house = the old farmer retired; domkář (cottager) ≠ sedlák of the same name | A status can be upgraded by marriage into a grunt |
| 5 | Land transfer as filiation | "Václav prodává synu Janovi … dědické díly bratru Matějovi, sestře Anně" (Václav sells to his son Jan … inheritance shares to brother Matěj, sister Anna): one entry names parent, child and siblings, which is direct evidence of filiation. The archive staff quoted by Czech Radio say land books were more careful than registers "tam šlo o peníze" (because money was involved) [CLAIM] | Payment receipts were often entered decades later; date each payment |
| 6 | Orphan books | Orphans' ages in an orphan inventory → birth windows → match baptisms | Ages rounded |
| 7 | Marriage contracts (svatební smlouvy) | Bride's dowry from "otec Jiří, sedlák v X" (father Jiří, farmer in X) points to her parish of origin | Often in town books, not estate books |
| 8 | Probate | Post-1850 probate at the soudní okres names heirs in other districts and in Vienna | Fonds may be sampled/shredded |
| 9 | Age-at-death back-calculation | "70 let" (aged 70) in 1830 → search baptisms 1755–1765; tolerance ±5 years for ages ≥60, ±2 for children | Old people's ages are inflated; ages in years/months/days are more exact |
| 10 | Naming patterns | First son often named after a grandfather; a reused name means a sibling with that name died | Weak evidence on its own |
| 11 | Feminine surnames and orthography | Nováková = Novak (de) = Novakowa; Latinised Joannes/Ioannes; Hungarian order surname-first | Indexers split or merge forms |
| 12 | Magyarisation/Germanisation | Slovak Kováč → Kovács; Czech Šimek → Schimek; place names: Bytča = Nagybiccse | Search all language forms of person and place |
| 13 | Gazetteers | Retrospektivní lexikon obcí, Historický lexikon obcí; oefr gazetteer (72,000 localities with parish affiliation, per oefr.at); Helységnévtár 1877/1913; Słownik geograficzny | Use the parish as of the event year |
| 14 | Feast-day dating | "feria 2da post Dominicam Laetare" = Monday after the 4th Sunday of Lent; compute with a perpetual calendar | Pre-1584 Julian dates rarely matter in Bohemia |
| 15 | Marginal legitimations | Birth entry "illegitimus" plus later marginal note "legitimiert durch nachfolgende Ehe am …" (legitimated by subsequent marriage on …) identifies the father | The note may sit in a different book |
| 16 | Domovská příslušnost / Heimatrecht | A Vienna Meldezettel or Grundbuchblatt records the Heimatrecht place (place of legal domicile), which leads to the home parish; the Kriegsarchiv keeps sheets by Heimatrecht | Heimatrecht ≠ birthplace (acquired by residence or marriage) |


### 5.4 Disambiguation rule set


Default rule: merge two same-name persons only on **two independent identifiers**, drawn from house number, both parents, spouse, a godparent cluster or an exact birth date. Each identifier must come from a different record, created by a different informant. [INFERENCE — my reading of standard practice; no Central European society publishes a numeric threshold that I found]


Tests:
- **Same-name cousins in one village:** the house number alone fails, because cousins can live in neighbouring houses or share one. Require parents plus spouse.
- **Remarried widows:** a woman appears under two married surnames, so link by maiden name plus the father's name in both marriage entries.
- **Step-families:** a výměnek (retirement allowance) beneficiary may be a stepparent; the land book states the relationship.
- **Foundlings:** no parents, so link through the foundling-hospital number (Vienna Findelhaus) and the wet-nurse's place.
- **Soldiers:** the regiment and Heimatrecht place on the GB are the two identifiers, not the birthplace alone.


### 5.5 Failure-mode catalogue (25)


| # | Failure mode | Detection cue | Resolving record |
|---|---|---|---|
| 1 | Two same-name men merged | Children born 10 months apart to "the same" couple | Marriage entries for both; house numbers |
| 2 | Father of an illegitimate child assumed | No legitimation note | Marginal note; later marriage entry; court paternity file |
| 3 | Index treated as the record | Citation points to an index only | Image of the original |
| 4 | Wrong parish because of post-1784 reorganisation | Village missing from the expected book | Locality guide; lokálie founding date |
| 5 | Renumbered house | Same family, different čp. | Indicative sketch; renumbering concordance |
| 6 | Grunt name mistaken for a surname | Surname "changes" on succession | Land book |
| 7 | Age-at-death used without tolerance | Baptism "not found" | Widen window; orphan book |
| 8 | Bride's place of origin = place of marriage assumed | Marriage in the bride's parish is the norm, but not always | Banns notes; land book |
| 9 | Latin given name mis-normalised | Joannes ≠ Joachim | Paleography table |
| 10 | Feminine surname treated as a different family | -ová / -owa / -in | Orthography rule |
| 11 | Hungarian-form place name not mapped | Village "not found" in SK | Helységnévtár |
| 12 | Volume-closure rule ignored | Archive says the book is "not yet transferred" | Registry office request |
| 13 | HTR transcript copied as fact | Name spelled oddly in one source only | Image check |
| 14 | Godparent read as a relative | Same godparents for unrelated families | FAN analysis |
| 15 | Výměnkář read as father | Retired holder ≠ parent | Land transfer entry |
| 16 | Soldier's birthplace confused with Heimatrecht | GB vs baptism mismatch | Heimatschein (domicile certificate) / municipal domicile register |
| 17 | Jewish surname adoption (1787) missed | Pre-1787 patronymics | Familiantenbücher (Jewish family registers), 1793 list |
| 18 | Convert's earlier identity lost | Adult baptism entry | Conversion note; Jewish register |
| 19 | Protestant entry sought only in the Lutheran book | Pre-1849 Catholic priest recorded it | Catholic register |
| 20 | Old Catholic event sought in an RC book after recognition | Gap after 1877 | Old Catholic duplicates (WStLA) |
| 21 | Vienna death sought in the home parish | No entry | Vienna parish / Totenbeschauprotokoll |
| 22 | US-anglicised name | Name not found in Czech books | Passenger list, naturalisation, CGSI/fraternal records |
| 23 | Military matriky missed | Soldier's child "missing" | ÖStA military matriky by regiment |
| 24 | Double-counting duplicate registers | Two "sources" agree because one was copied from the other | Identify duplicate vs original |
| 25 | Calendar/feast-day misread | Date off by days or weeks | Perpetual calendar |


---


## 6. Paleography and glossary


**Scripts by period** [CLAIM — standard knowledge, not sourced this run]:
- Czech books: Czech Bastarda/humanist cursive in the 16th–17th c.; Latin humanist cursive for Latin entries throughout.
- German Kurrent dominates in the 18th–19th c. Names and Latin terms are often written in Latin script inside Kurrent text, so use mixed-script models (Transkribus "German handwriting M1", 4.7 % validation CER, is intended for "Kurrent/Sütterlin and Latin script mixed").
- Czech-language entries return in many Bohemian parishes in the later 19th c.
- The Kriegsarchiv notes that over 90 % of its files are in German, and that reading Kurrent is a prerequisite. [FACT]


**Numerals and dates:**
- Roman numerals in folio numbers.
- Months abbreviated as 7bris/8bris/9bris/Xbris (September–December) — the Latin numeric month trap.
- "anno currente" (in the current year); "eodem" (the same day).
- Ages given as "annorum 40" (40 years old) or "alt 40 J.".


**Glossary (120 terms).** Compiled from working knowledge; verify spellings against FamilySearch word lists and Czech archive aids before relying on them. [CLAIM — collective tag]


| # | Latin | German | Czech | SK / HU / PL | English |
|---|---|---|---|---|---|
| 1 | pater | Vater | otec | otec / apa / ojciec | father |
| 2 | mater | Mutter | matka | matka / anya / matka | mother |
| 3 | filius | Sohn | syn | syn / fia / syn | son |
| 4 | filia | Tochter | dcera | dcéra / lánya / córka | daughter |
| 5 | frater | Bruder | bratr | brat / fivér / brat | brother |
| 6 | soror | Schwester | sestra | sestra / nővér / siostra | sister |
| 7 | avus | Großvater | děd | starý otec / nagyapa / dziadek | grandfather |
| 8 | avia | Großmutter | babička | stará matka / nagyanya / babka | grandmother |
| 9 | nepos | Enkel / Neffe | vnuk / synovec | vnuk / unoka / wnuk | grandson / nephew |
| 10 | maritus | Ehemann | manžel | manžel / férj / mąż | husband |
| 11 | uxor | Ehefrau | manželka | manželka / feleség / żona | wife |
| 12 | vidua | Witwe | vdova | vdova / özvegy / wdowa | widow |
| 13 | viduus | Witwer | vdovec | vdovec / özvegy / wdowiec | widower |
| 14 | sponsus | Bräutigam | ženich | ženích / vőlegény / pan młody | groom |
| 15 | sponsa | Braut | nevěsta | nevesta / menyasszony / panna młoda | bride |
| 16 | levans / patrinus | Pate | kmotr | krstný otec / keresztapa / ojciec chrzestny | godfather |
| 17 | matrina | Patin | kmotra | krstná matka / keresztanya / matka chrzestna | godmother |
| 18 | testis | Zeuge | svědek | svedok / tanú / świadek | witness |
| 19 | obstetrix | Hebamme | porodní bába | pôrodná baba / bába / akuszerka | midwife |
| 20 | legitimus | ehelich | manželský | manželský / törvényes / ślubny | legitimate |
| 21 | illegitimus | unehelich | nemanželský | nemanželský / törvénytelen / nieślubny | illegitimate |
| 22 | spurius | Bastard | levoboček | – / – / – | bastard (pejorative) |
| 23 | legitimatus per subsequens matrimonium | legitimiert durch nachfolgende Ehe | legitimován následným sňatkem | – | legitimated by subsequent marriage |
| 24 | gemelli | Zwillinge | dvojčata | dvojčatá / ikrek / bliźnięta | twins |
| 25 | infans | Kind | dítě | dieťa / gyermek / dziecko | child |
| 26 | parvulus | Kleinkind | nemluvně | – | infant |
| 27 | posthumus | nachgeboren | pohrobek | pohrobok / – / pogrobowiec | posthumous child |
| 28 | expositus / inventus | Findelkind | nalezenec | nájdenec / lelenc / podrzutek | foundling |
| 29 | privignus | Stiefsohn | nevlastní syn | – | stepson |
| 30 | vitricus | Stiefvater | otčím | otčim / mostohaapa / ojczym | stepfather |
| 31 | noverca | Stiefmutter | macecha | macocha / mostohaanya / macocha | stepmother |
| 32 | gener | Schwiegersohn | zeť | zať / vő / zięć | son-in-law |
| 33 | nurus | Schwiegertochter | snacha | nevesta / meny / synowa | daughter-in-law |
| 34 | socer | Schwiegervater | tchán | svokor / após / teść | father-in-law |
| 35 | tutor / curator | Vormund | poručník | poručník / gyám / opiekun | guardian |
| 36 | orphanus | Waise | sirotek | sirota / árva / sierota | orphan |
| 37 | consanguinitas | Blutsverwandtschaft | pokrevní příbuzenství | – | consanguinity |
| 38 | dispensatio | Dispens | dispens | – | dispensation |
| 39 | baptizatus | getauft | pokřtěn | pokrstený / megkeresztelt / ochrzczony | baptised |
| 40 | natus | geboren | narozen | narodený / született / urodzony | born |
| 41 | copulati | getraut | oddáni | sobášení / esketett / zaślubieni | married |
| 42 | denatus / obiit | gestorben | zemřel | zomrel / meghalt / zmarł | died |
| 43 | sepultus | begraben | pohřben | pochovaný / eltemetve / pochowany | buried |
| 44 | proclamationes / banna | Aufgebot | ohlášky | ohlášky / kihirdetés / zapowiedzi | banns |
| 45 | confirmatus | gefirmt | biřmován | birmovaný / bérmált / bierzmowany | confirmed |
| 46 | provisus sacramentis | versehen | zaopatřen | zaopatrený / – / opatrzony | given last rites |
| 47 | in periculo mortis baptizatus | nottgetauft | pokřtěn z nouze | – | emergency baptism |
| 48 | mortuus natus | totgeboren | mrtvě narozený | mŕtvo narodený / halva született / martwo urodzony | stillborn |
| 49 | ritus catholicus | katholisch | katolický | – / róm. kat. / katolicki | Catholic |
| 50 | Augustanae confessionis (A.C.) | evangelisch A.B. | evangelík a. v. | ev. a. v. / evangélikus / ewangelicki | Lutheran |
| 51 | Helveticae confessionis (H.C.) | reformiert H.B. | evangelík h. v. | reformovaný / református / reformowany | Reformed |
| 52 | Judaeus | Jude / israelitisch | žid / izraelita | žid / zsidó / żyd | Jewish |
| 53 | acatholicus | Akatholik | nekatolík | – | non-Catholic |
| 54 | conversus | Konvertit | konvertita | – | convert |
| 55 | colonus | Bauer | sedlák | sedliak / jobbágy (gazda) / kmieć | farmer (full holder) |
| 56 | casarius / casae possessor | Häusler / Chalupner | chalupník | – / zsellér házas / zagrodnik | cottager with land |
| 57 | domunculus | Häusler | domkář | domkár / házas zsellér / chałupnik | cottager (house only) |
| 58 | inquilinus | Inwohner / Inmann | podruh | podruh / hazátlan zsellér / komornik | lodger, landless |
| 59 | – | Ausgedinger / Auszügler | výměnkář | výmenkár / – / wycużnik | retired holder (on allowance) |
| 60 | servus / famulus | Knecht | čeledín | sluha / szolga / parobek | farmhand |
| 61 | ancilla | Magd | děvečka | slúžka / szolgáló / dziewka | maid |
| 62 | molitor | Müller | mlynář | mlynár / molnár / młynarz | miller |
| 63 | faber ferrarius | Schmied | kovář | kováč / kovács / kowal | smith |
| 64 | sartor | Schneider | krejčí | krajčír / szabó / krawiec | tailor |
| 65 | sutor | Schuster | švec | obuvník / varga / szewc | shoemaker |
| 66 | textor | Weber | tkadlec | tkáč / takács / tkacz | weaver |
| 67 | lanio | Fleischhauer | řezník | mäsiar / mészáros / rzeźnik | butcher |
| 68 | pistor | Bäcker | pekař | pekár / pék / piekarz | baker |
| 69 | braxator | Brauer | sládek | sládok / sörfőző / piwowar | brewer |
| 70 | caupo | Wirt | hostinský | krčmár / kocsmáros / karczmarz | innkeeper |
| 71 | figulus | Töpfer | hrnčíř | hrnčiar / fazekas / garncarz | potter |
| 72 | faber lignarius | Zimmermann | tesař | tesár / ács / cieśla | carpenter |
| 73 | murarius | Maurer | zedník | murár / kőműves / murarz | mason |
| 74 | pastor | Hirt | pastýř | pastier / pásztor / pasterz | herdsman |
| 75 | opilio | Schäfer | ovčák | ovčiar / juhász / owczarz | shepherd |
| 76 | venator | Jäger | myslivec | poľovník / vadász / myśliwy | gamekeeper |
| 77 | ludimagister | Schullehrer | učitel | učiteľ / tanító / nauczyciel | schoolmaster |
| 78 | aedituus | Mesner | kostelník | kostolník / sekrestyés / zakrystian | sexton |
| 79 | civis | Bürger | měšťan | mešťan / polgár / mieszczanin | burgher |
| 80 | judex | Richter | rychtář | richtár / bíró / sołtys | village headman |
| 81 | miles | Soldat | voják | vojak / katona / żołnierz | soldier |
| 82 | miles emeritus | Invalide / Abschied | vysloužilec | vyslúžilec / – / weteran | discharged soldier |
| 83 | mendicus | Bettler | žebrák | žobrák / koldus / żebrak | beggar |
| 84 | subditus | Untertan | poddaný | poddaný / jobbágy / poddany | subject (serf) |
| 85 | dominium | Herrschaft | panství | panstvo / uradalom / dobra | estate |
| 86 | – | Grund / Bauerngut | grunt / usedlost | gazdovstvo / telek / gospodarstwo | farm holding |
| 87 | – | Kaufbrief | trhová smlouva | kúpna zmluva / adásvételi / umowa kupna | purchase contract |
| 88 | – | Waisenbuch | sirotčí kniha | sirotská kniha / árvakönyv / księga sierocińska | orphan book |
| 89 | – | Heiratsvertrag | svatební smlouva | svadobná zmluva / házassági szerződés / intercyza | marriage contract |
| 90 | – | Verlassenschaft | pozůstalost | pozostalosť / hagyaték / spadek | estate of the deceased |
| 91 | testamentum | Testament | poslední vůle | závet / végrendelet / testament | will |
| 92 | – | Heimatrecht / Heimatschein | domovské právo / domovský list | domovské právo / illetőség / prawo przynależności | right of domicile / certificate |
| 93 | – | Entlassungsschein | výhostní list (propuštění z poddanství) | – | release from serfdom |
| 94 | – | Konsens | povolení k sňatku | – | marriage permission |
| 95 | – | Hausnummer | číslo popisné (čp.) | súpisné číslo / házszám / numer domu | house number |
| 96 | vulgo | genannt | řečený | – | alias |
| 97 | olim | ehemals | dříve | – | formerly |
| 98 | quondam (q.) | weiland / verstorben | nebožtík | – / néhai / nieboszczyk | late (deceased) |
| 99 | hujas | hiesig | zdejší | – | of this place |
| 100 | ex | aus | z / ze | – | from |
| 101 | annorum | Jahre alt | let | rokov / éves / lat | aged (years) |
| 102 | febris | Fieber | horečka | horúčka / láz / gorączka | fever |
| 103 | phthisis / tabes | Lungensucht / Auszehrung | souchotiny | suchoty / tüdővész / suchoty | consumption (TB) |
| 104 | variolae | Blattern | neštovice | kiahne / himlő / ospa | smallpox |
| 105 | cholera | Cholera | cholera | cholera / kolera / cholera | cholera |
| 106 | dysenteria | Ruhr | úplavice | červienka / vérhas / czerwonka | dysentery |
| 107 | hydrops | Wassersucht | vodnatelnost | vodnateľnosť / vízkór / puchlina | dropsy |
| 108 | apoplexia | Schlagfluss | mrtvice | porážka / gutaütés / apopleksja | stroke |
| 109 | convulsiones | Fraisen | psotník | – / görcs / konwulsje | convulsions (infant) |
| 110 | marasmus senilis | Altersschwäche | sešlost věkem | starecká slabosť / végelgyengülés / starość | old age |
| 111 | angina / diphtheria | Halsbräune | záškrt | záškrt / torokgyík / błonica | diphtheria |
| 112 | typhus | Typhus / Nervenfieber | tyfus | týfus / tífusz / tyfus | typhus |
| 113 | partus | Kindbett | šestinedělí | – / gyermekágy / połóg | childbed |
| 114 | submersus | ertrunken | utonul | utopil sa / vízbe fúlt / utonął | drowned |
| 115 | morbilli | Masern | spalničky | osýpky / kanyaró / odra | measles |
| 116 | pertussis | Keuchhusten | černý kašel | čierny kašeľ / szamárköhögés / koklusz | whooping cough |
| 117 | dies | Tag | den | deň / nap / dzień | day |
| 118 | mane / vespere | früh / abends | ráno / večer | – | morning / evening |
| 119 | eodem | desselben | téhož | – | the same (day) |
| 120 | ut supra (u. s.) | wie oben | jako výše | – | as above |


---


## 7. Pro profiles funnel → 3 picks


**Funnel (8 candidates seen; methodology visibility rated)** [CLAIM — firms' self-reports]


| # | Practitioner / firm | Territory | Visible methodology | Pricing model (published) |
|---|---|---|---|---|
| 1 | hledanipredku.cz | CZ | combines registers with "majetkové, vojenské a další záznamy" (property, military and other records); publishes land-book guide | per-package: paternal line 3 gens 6,499 Kč; 5 gens incl. land/military + book 22,556 Kč; ancestry chart 4 gens 54,301 Kč |
| 2 | rodokmeny-rodin.cz | CZ | period-differentiated reading fees | 180–220 Kč/record; 300 Kč per 18th-c. entry; 400 Kč per 17th-c. entry |
| 3 | vasegeny.cz | CZ | link catalogue (848 links, baseline); land-book study listed as a service | 350 Kč/record (5–10), 250 Kč (>10), +250 Kč transcript (2026 list) |
| 4 | rodokmeny-priborsky.cz | CZ | results-based per-record price | 300–360 Kč/record |
| 5 | Rediens | CZ | individual quotes; DNA testing offered | 20,000 Kč to 7th generation (combined lines) |
| 6 | korenypredku.cz | CZ | 200 Kč/record | packages 7,000–55,000 Kč |
| 7 | oefr.at | AT | publishes source guides (Vienna registration enquiries, link lists, 72,000-locality gazetteer) | n.d. |
| 8 | Familia Austria (society, not a firm) | AT | archive-by-archive military holdings summaries citing the Kriegsarchiv | membership |


**Credentials:** I could not determine from this run's sources whether any of these holds BCG or ICAPGen credentials, or any member list of a Central European professional body. None of the Czech price pages shows a sample report, a proof argument or a QC step. The ÖStA guide has a section "3.4 Berufsgenealogen" (professional genealogists), but its contents were truncated in the fetch. [FACT/not determinable]


**3 picks to emulate and the exact practice to copy** [INFERENCE — my reading]:
1. **hledanipredku.cz.** Copy its default of correlating parish entries with land, military and subject-list records rather than registers alone. Copy the rule its interviewed peers state: land books record "kdo na gruntě seděl" (who sat on the holding).
2. **rodokmeny-rodin.cz.** Copy its period-weighted cost model: budget 1.5–2× effort for 18th-century and 2× for 17th-century entries. Use that model for agent cost estimates and to decide when to call in a human reader.
3. **oefr.at / Familia Austria.** Copy their source-guide habit: a written, dated note per holding (who holds what, which cohorts, cost, turnaround) before any request. That is your locality guide extended to institutions.


**What none of them shows publicly**, and you should do anyway: whole-book reading logs, image-level citations, negative-evidence logs and written proof arguments. [INFERENCE]


---


## 8. Tooling and AI matrix


| Tool | 2026 status | Central European coverage | Measured accuracy | Machine access | Tag |
|---|---|---|---|---|---|
| FamilySearch Full-Text Search | out of Labs; launched Aug 2025; >8,000 collections, about 2.5 bn images | top languages EN, ES, IT, PT, FR, NL; German 23 collections (CompGen 2025-06); CZ/SK/AT/HU/PL **not determinable** (list behind login) | FamilySearch retrains models below "90%-word accuracy"; user tests: about 85 % name recall on clean prose, 45 % faded, 25 % overwritten, "a complete failure" on columnar inventories | API partner-only (baseline) | [FACT]/[CLAIM] |
| Transkribus | API "Generally available" (Scholar+ per API page; Organisation-only per pricing page, **conflict**); free 50 credits/month; Scholar €99/yr 900 credits (third-party) | public German Kurrent models; Czech-specific model **not verified this run** | German Kurrent 5.4 % validation CER; German Genius 4.5 %; handwriting M1 4.7 %; 17th–18th c. 5.5 %; Early Kurrent 6.3 %; Kurrent XIX 6.9 %; independent test 5.9 % mean / 10.2 % worst | API, half-rate credits | [FACT] model pages; [CLAIM] pricing |
| LLM vision (GPT-4o class) | general-purpose | — | modern EN 1.75 % CER (IAM); non-English historical 33.5–80.2 % CER (Crosilla et al. 2025; READ2016 German 80.20 %) | per vendor ToS | [FACT] |
| Matricula | free, no account | AT dioceses (counts §2.3), DE, PL, SI | no index | not checked | [FACT] |
| Geneteka | free | PL; weak in Lower Silesia (2018) | volunteer index; error rate n.d. | PTG claims database rights (surname.pl: "linkujemy, nie pobieramy danych" — we link, we don't download the data) | [CLAIM] |
| Kramerius / ANNO | full text | CZ / AT newspapers | Fraktur OCR quality n.d. | documented API (baseline) | [CLAIM] |


**H4 verdict, measured:** a 5 % CER means roughly one wrong character every 20. Proper names concentrate those errors, because they lack the language-model context that common words get. So at validation CER, a material share of surnames will be misread. [INFERENCE] **Unsupervised extraction is not justified.** Run a 20–30 entry pilot and measure name-level error yourself.


**Recommended stack (default → runner-up, with the deciding reason)** [INFERENCE]:


| Function | Default | Runner-up | Deciding reason |
|---|---|---|---|
| Tree database | Gramps Web (self-hosted) + MCP | Gramps desktop | Self-hosting keeps living-person data off third-party clouds |
| Transcription | Transkribus German Kurrent / German handwriting M1 + human check | LLM vision for Czech/Latin columnar entries with mandatory image check | Only Transkribus publishes per-model CER |
| Index aggregator | FamilySearch (indexes + FTS) | Geneteka (PL), Matricula (browse) | Largest CE image base |
| Gazetteer | Retrospektivní/Historický lexikon obcí + oefr gazetteer | Helységnévtár (HU/SK) | Parish affiliation per period |
| Citation | Own template 5.2.2, image-level permalink | Evidence Explained style for US records | Archive structure (fond/inv. č.) is native to CZ/AT |


---


## 9. Brick-wall decision trees


| Dead end | Substitutes in priority order | Linking field | Expected success |
|---|---|---|---|
| Pre-1784 gap | 1. Combined pre-1784 registers (whole-book read) → 2. Estate land books → 3. Orphan books / marriage contracts → 4. Theresian cadastre → 5. 1651 Soupis / 1654 Berní rula | grunt / house + holder succession | Not determinable as a rate; **realistic depth for Bohemian peasant lines with surviving land books is about 1650**, because the 1651 list and 1654 roll are the floor and few registers survive from before the Thirty Years' War [INFERENCE] |
| Register lost | Duplicate/index volumes, land books, conscription lists, military Musterlisten | house no. | n.d. |
| Illegitimate birth | Marginal legitimation → later marriage of the mother → godparent → paternity/court file → land book | mother + child's house | n.d. |
| Migrant to Vienna | Vienna parish → Meldeunterlagen (1904–75, €35/half hour) → Verlassenschaft → Heimatrecht place | Heimatrecht | Good after 1904; weak 1850–1904 (conflict on Meldezettel) |
| Migrant to USA | Passenger lists → naturalisation → church/fraternal (CGSI) → home-parish marginal notes | village name in original spelling | n.d. |
| Soldier | Regiment (Wrede table) → Musterlisten (pre-1820) / GB (1820–1864 cohorts in Vienna; 1865–1886 VHA; 1887–98 largely lost) → military matriky (100-year block) → Verlustlisten / loss card index | regiment + Heimatrecht | High for 1820–1886 cohorts, low for 1887–98 [FACT/INFERENCE] |
| Foundling | Foundling-hospital records → wet-nurse parish | foundling number | n.d. |
| Sealed 20th-century register | Registry office with proof of kinship (CZ/SK); Standesamt (DE/AT); HOK (Sudeten Germans); police registrations | — | depends on kinship |
| Sudeten German line after 1945 | HOK Regensburg (BArch Bayreuth) → Lastenausgleich → Gemeindeseelenlisten | 1939 residence | n.d. |
| Name change / language variant | All forms (see §5.3 #11–12) | — | — |


---


## 10. Community, costs, DNA (concise)


- **Costs, CZ professionals** (self-published, 2026): 180–400 Kč per record; 5-generation paternal line with land/military records and a book, 22,556 Kč; 7-generation combined, 20,000 Kč; full 7-generation pedigree, 55,000 Kč. [CLAIM]
- **Archive fees:** WStLA Meldeauskunft (Vienna registration enquiry) €35 per started half hour, charged on negative results too. [FACT] HU archive preparation time 21 days, extendable once by 21 (MNL pages, 2014 regime). [FACT]
- **Societies** mentioned in sources: Familia Austria, CompGen, PTG (Geneteka), CGSI. Journal details were not checked this run. [FACT existence]
- **DNA:** pool composition for Central Europe and Czech/Slovak Y-DNA projects not determinable in this run. Hungarian law already treats religion and illegitimacy as special data; DNA is special-category data under GDPR art. 9. [INFERENCE]


---


## 11. Open questions and "Not determinable from public sources"


- Whether FamilySearch Full-Text Search includes any Czech, Slovak, Austrian, Hungarian or Polish collection (collection list requires login).
- Name-level accuracy of any HTR or LLM on Czech/Latin parish entries: no measurement found.
- **Conflict:** WStLA says the 19th-century Meldezettel ("A-Antiquariat") were destroyed except about 200, while FamilySearch hosts "Wiener Meldezettel 1850–1896" (indexed). Possibly a different series; not resolved.
- **Conflict:** the Kriegsarchiv says GB cohorts from 1865 left Vienna; one German site says "nach 1886".
- **Conflict:** the FamilySearch Grundbuchblätter "Diverse" roll count (662 total vs 454 + 211 = 665).
- **Conflict:** the Transkribus API plan scope (Scholar+ vs Organisation).
- **Conflict:** Austrian period start (entry vs last processing).
- Slovak access rules before the 100-year transfer, beyond § 5(3).
- Civil-registration start dates for HU (1895-10-01), CZ (1950-01-01) and Prussia (1874-10-01): not re-verified in this run.
- Share of Czech parish books digitised per archive, SOkA holdings online, and FamilySearch Slovakia image totals (CGSI 1.6 M images vs Forebears "14 million" entries).


**Falsification pass (§6)**


| H | Verdict | Most decisive source | What would change it |
|---|---|---|---|
| H1 Everything useful is online | **False** | SOA Praha: about 900 land-book volumes online, from a minority of its estates; post-1871 land books and most probate/orphan files offline | Archive-published digitisation percentages |
| H2 Name indexes cover most 19th-c. Czech records | **False** | Baseline: Czech matriky image-only; FamilySearch indexes partial | A Czech crowd-index with published coverage |
| H3 FS FTS makes Czech parish research trivial | **False / not determinable** | FS 2026 handout language list omits Czech, Latin, German | FS announcing Czech/Latin plus measured accuracy |
| H4 AI reads Kurrent for unsupervised extraction | **False** | Transkribus 5–7 % CER; GPT-4o 33.5–80.2 % CER (non-English historical, Crosilla et al. 2025) | Name-level CER below about 1 % on parish entries |
| H5 Pre-1784 research impossible for peasants | **False** | SOA Plzeň/Opava/Třeboň land books online; 1651 list editions | — |
| H6 Access rules are the same | **False** | njt.hu (HU 110/86/30) vs slov-lex (SK 100 transfer) vs PStG (DE 110/80/30) | — |
| H7 Verified index = verified fact | **False** | FS FTS user tests: 85 % → 25 % name recall; FS: "Handwriting recognition errors are common" | — |


---


## 12. Sources


Each source is named inline next to the claim it supports, with this run's status ("seen"/"opened" 2026-10-09) in §0, §2 and §8. Per house formatting rules there is no separate bibliography. Portal URLs carried over from the baseline (AHMP, SOA portals, Acta Publica, digi.archives.cz, Digitální badatelna NA, Kramerius, VÚA) were **not re-opened in this run** and keep their baseline status.