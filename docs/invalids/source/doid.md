# doid

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `doid`. See the [GitHub repository](https://github.com/DiseaseOntology/HumanDiseaseOntology).


## `DO`: Human Disease Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `DO` (standardized to Bioregistry
prefix [`doid`](https://bioregistry.io/doid)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `DO:wk`         |              1 | [DOID:0050178](http://purl.obolibrary.org/obo/DOID_0050178) |
| `DO:lh`         |              1 | [DOID:462](http://purl.obolibrary.org/obo/DOID_462)         |

## `ICD10CM`: International Classification of Diseases, 10th Revision, Clinical Modification

Overall, there were 2 invalid
xrefs to external prefixed with `ICD10CM` (standardized to Bioregistry
prefix [`icd10cm`](https://bioregistry.io/icd10cm)) that
did not match the standard pattern `^([A-Z][0-9][0-9AB]((-[A-Z][0-9][0-9AB])|(\.[0-9A-KXZ]([0-9A-EXYZ]([0-9A-HX][0-59A-HJKMNP-S]?)?)?)?))$`.

| external_xref    |   usages_count | usages                                                      |
|------------------|----------------|-------------------------------------------------------------|
| `ICD10CM:E74.0+` |              1 | [DOID:0090101](http://purl.obolibrary.org/obo/DOID_0090101) |
| `ICD10CM:G73.6*` |              1 | [DOID:0090101](http://purl.obolibrary.org/obo/DOID_0090101) |

## `ICD11`: International Classification of Diseases, 11th Revision (Foundation Component)

Overall, there were 1 invalid
xrefs to external prefixed with `ICD11` (standardized to Bioregistry
prefix [`icd11`](https://bioregistry.io/icd11)) that
did not match the standard pattern `^[1-9]\d*$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `ICD11:4B24`    |              1 | [DOID:0081267](http://purl.obolibrary.org/obo/DOID_0081267) |

## `ICD9CM`: International Classification of Diseases, 9th Revision, Clinical Modification

Overall, there were 13 invalid
xrefs to external prefixed with `ICD9CM` (standardized to Bioregistry
prefix [`icd9cm`](https://bioregistry.io/icd9cm)) that
did not match the standard pattern `^([\dA-Z]\d{2}(\.\d{1,3}|))|(\d{2}(\.\d{1,2}|))$`.

| external_xref       |   usages_count | usages                                                  |
|---------------------|----------------|---------------------------------------------------------|
| `ICD9CM:001-009.99` |              1 | [DOID:100](http://purl.obolibrary.org/obo/DOID_100)     |
| `ICD9CM:401-405.99` |              1 | [DOID:10763](http://purl.obolibrary.org/obo/DOID_10763) |
| `ICD9CM:110-118.99` |              1 | [DOID:1564](http://purl.obolibrary.org/obo/DOID_1564)   |
| `ICD9CM:390-392.99` |              1 | [DOID:1586](http://purl.obolibrary.org/obo/DOID_1586)   |
| `ICD9CM:209-209.99` |              1 | [DOID:169](http://purl.obolibrary.org/obo/DOID_169)     |
| `ICD9CM:410-414.99` |              1 | [DOID:3393](http://purl.obolibrary.org/obo/DOID_3393)   |
| `ICD9CM:610-612.99` |              1 | [DOID:3463](http://purl.obolibrary.org/obo/DOID_3463)   |
| `ICD9CM:042-042.99` |              1 | [DOID:526](http://purl.obolibrary.org/obo/DOID_526)     |
| `ICD9CM:520-579.99` |              1 | [DOID:77](http://purl.obolibrary.org/obo/DOID_77)       |
| `ICD9CM:540-543.99` |              1 | [DOID:8337](http://purl.obolibrary.org/obo/DOID_8337)   |
| `ICD9CM:230-234.99` |              1 | [DOID:8719](http://purl.obolibrary.org/obo/DOID_8719)   |
| `ICD9CM:120-129.99` |              1 | [DOID:883](http://purl.obolibrary.org/obo/DOID_883)     |
| `ICD9CM:060-066.99` |              1 | [DOID:934](http://purl.obolibrary.org/obo/DOID_934)     |

## `ICDO`: International Classification of Diseases for Oncology

Overall, there were 2 invalid
xrefs to external prefixed with `ICDO` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref   |   usages_count | usages                                                |
|-----------------|----------------|-------------------------------------------------------|
| `ICDO:8480/6`   |              1 | [DOID:3559](http://purl.obolibrary.org/obo/DOID_3559) |
| `ICDO:8800/9`   |              1 | [DOID:7615](http://purl.obolibrary.org/obo/DOID_7615) |

## `KEGG`: Kyoto Encyclopedia of Genes and Genomes

Overall, there were 36 invalid
xrefs to external prefixed with `KEGG` (standardized to Bioregistry
prefix [`kegg`](https://bioregistry.io/kegg)) that
did not match the standard pattern `^([CHDEGTMKR]\d+)|(\w+:[\w\d\.-]*)|([a-z]{3,5})|(\w{2,4}\d{5})$`.

| external_xref   |   usages_count | usages                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------|
| `KEGG:05321`    |              2 | [DOID:0050589](http://purl.obolibrary.org/obo/DOID_0050589), [DOID:9778](http://purl.obolibrary.org/obo/DOID_9778) |
| `KEGG:05215`    |              2 | [DOID:10283](http://purl.obolibrary.org/obo/DOID_10283), [DOID:10286](http://purl.obolibrary.org/obo/DOID_10286)   |
| `KEGG:04950`    |              1 | [DOID:0050524](http://purl.obolibrary.org/obo/DOID_0050524)                                                        |
| `KEGG:05034`    |              1 | [DOID:0050741](http://purl.obolibrary.org/obo/DOID_0050741)                                                        |
| `KEGG:05143`    |              1 | [DOID:10112](http://purl.obolibrary.org/obo/DOID_10112)                                                            |
| `KEGG:05010`    |              1 | [DOID:10652](http://purl.obolibrary.org/obo/DOID_10652)                                                            |
| `KEGG:05219`    |              1 | [DOID:11054](http://purl.obolibrary.org/obo/DOID_11054)                                                            |
| `KEGG:05133`    |              1 | [DOID:1116](http://purl.obolibrary.org/obo/DOID_1116)                                                              |
| `KEGG:05410`    |              1 | [DOID:11984](http://purl.obolibrary.org/obo/DOID_11984)                                                            |
| `KEGG:05142`    |              1 | [DOID:12140](http://purl.obolibrary.org/obo/DOID_12140)                                                            |
| `KEGG:05131`    |              1 | [DOID:12385](http://purl.obolibrary.org/obo/DOID_12385)                                                            |
| `KEGG:05016`    |              1 | [DOID:12858](http://purl.obolibrary.org/obo/DOID_12858)                                                            |
| `KEGG:05414`    |              1 | [DOID:12930](http://purl.obolibrary.org/obo/DOID_12930)                                                            |
| `KEGG:05213`    |              1 | [DOID:1380](http://purl.obolibrary.org/obo/DOID_1380)                                                              |
| `KEGG:05012`    |              1 | [DOID:14330](http://purl.obolibrary.org/obo/DOID_14330)                                                            |
| `KEGG:05216`    |              1 | [DOID:1781](http://purl.obolibrary.org/obo/DOID_1781)                                                              |
| `KEGG:05212`    |              1 | [DOID:1793](http://purl.obolibrary.org/obo/DOID_1793)                                                              |
| `KEGG:05218`    |              1 | [DOID:1909](http://purl.obolibrary.org/obo/DOID_1909)                                                              |
| `KEGG:05217`    |              1 | [DOID:2513](http://purl.obolibrary.org/obo/DOID_2513)                                                              |
| `KEGG:05310`    |              1 | [DOID:2841](http://purl.obolibrary.org/obo/DOID_2841)                                                              |
| `KEGG:05214`    |              1 | [DOID:3070](http://purl.obolibrary.org/obo/DOID_3070)                                                              |
| `KEGG:05014`    |              1 | [DOID:332](http://purl.obolibrary.org/obo/DOID_332)                                                                |
| `KEGG:05223`    |              1 | [DOID:3908](http://purl.obolibrary.org/obo/DOID_3908)                                                              |
| `KEGG:05222`    |              1 | [DOID:5409](http://purl.obolibrary.org/obo/DOID_5409)                                                              |
| `KEGG:05340`    |              1 | [DOID:612](http://purl.obolibrary.org/obo/DOID_612)                                                                |
| `KEGG:05020`    |              1 | [DOID:649](http://purl.obolibrary.org/obo/DOID_649)                                                                |
| `KEGG:05323`    |              1 | [DOID:7148](http://purl.obolibrary.org/obo/DOID_7148)                                                              |
| `KEGG:05416`    |              1 | [DOID:820](http://purl.obolibrary.org/obo/DOID_820)                                                                |
| `KEGG:05220`    |              1 | [DOID:8552](http://purl.obolibrary.org/obo/DOID_8552)                                                              |
| `KEGG:05322`    |              1 | [DOID:9074](http://purl.obolibrary.org/obo/DOID_9074)                                                              |
| `KEGG:05221`    |              1 | [DOID:9119](http://purl.obolibrary.org/obo/DOID_9119)                                                              |
| `KEGG:05210`    |              1 | [DOID:9256](http://purl.obolibrary.org/obo/DOID_9256)                                                              |
| `KEGG:04930`    |              1 | [DOID:9352](http://purl.obolibrary.org/obo/DOID_9352)                                                              |
| `KEGG:04940`    |              1 | [DOID:9744](http://purl.obolibrary.org/obo/DOID_9744)                                                              |

## `OMIM`: Online Mendelian Inheritance in Man

Overall, there were 276 invalid
xrefs to external prefixed with `OMIM` (standardized to Bioregistry
prefix [`omim`](https://bioregistry.io/omim)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `OMIM:PS267700` |              1 | [DOID:0050120](http://purl.obolibrary.org/obo/DOID_0050120) |
| `OMIM:PS275200` |              1 | [DOID:0050328](http://purl.obolibrary.org/obo/DOID_0050328) |
| `OMIM:PS608415` |              1 | [DOID:0050335](http://purl.obolibrary.org/obo/DOID_0050335) |
| `OMIM:PS175100` |              1 | [DOID:0050424](http://purl.obolibrary.org/obo/DOID_0050424) |
| `OMIM:PS102300` |              1 | [DOID:0050425](http://purl.obolibrary.org/obo/DOID_0050425) |
| `OMIM:PS107970` |              1 | [DOID:0050431](http://purl.obolibrary.org/obo/DOID_0050431) |
| `OMIM:PS608638` |              1 | [DOID:0050432](http://purl.obolibrary.org/obo/DOID_0050432) |
| `OMIM:PS276900` |              1 | [DOID:0050439](http://purl.obolibrary.org/obo/DOID_0050439) |
| `OMIM:PS151660` |              1 | [DOID:0050440](http://purl.obolibrary.org/obo/DOID_0050440) |
| `OMIM:PS193900` |              1 | [DOID:0050448](http://purl.obolibrary.org/obo/DOID_0050448) |
| `OMIM:PS167200` |              1 | [DOID:0050449](http://purl.obolibrary.org/obo/DOID_0050449) |
| `OMIM:PS601144` |              1 | [DOID:0050451](http://purl.obolibrary.org/obo/DOID_0050451) |
| `OMIM:PS607432` |              1 | [DOID:0050453](http://purl.obolibrary.org/obo/DOID_0050453) |
| `OMIM:PS133200` |              1 | [DOID:0050467](http://purl.obolibrary.org/obo/DOID_0050467) |
| `OMIM:PS277600` |              1 | [DOID:0050475](http://purl.obolibrary.org/obo/DOID_0050475) |
| `OMIM:PS138800` |              1 | [DOID:0050489](http://purl.obolibrary.org/obo/DOID_0050489) |
| `OMIM:PS310500` |              1 | [DOID:0050534](http://purl.obolibrary.org/obo/DOID_0050534) |
| `OMIM:PS133780` |              1 | [DOID:0050535](http://purl.obolibrary.org/obo/DOID_0050535) |
| `OMIM:PS306955` |              1 | [DOID:0050545](http://purl.obolibrary.org/obo/DOID_0050545) |
| `OMIM:PS162400` |              1 | [DOID:0050548](http://purl.obolibrary.org/obo/DOID_0050548) |
| `OMIM:PS124900` |              1 | [DOID:0050564](http://purl.obolibrary.org/obo/DOID_0050564) |
| `OMIM:PS220290` |              1 | [DOID:0050565](http://purl.obolibrary.org/obo/DOID_0050565) |
| `OMIM:PS304500` |              1 | [DOID:0050566](http://purl.obolibrary.org/obo/DOID_0050566) |
| `OMIM:PS119530` |              1 | [DOID:0050567](http://purl.obolibrary.org/obo/DOID_0050567) |
| `OMIM:PS277300` |              1 | [DOID:0050568](http://purl.obolibrary.org/obo/DOID_0050568) |
| `OMIM:PS210600` |              1 | [DOID:0050569](http://purl.obolibrary.org/obo/DOID_0050569) |
| `OMIM:PS212065` |              1 | [DOID:0050570](http://purl.obolibrary.org/obo/DOID_0050570) |
| `OMIM:PS212066` |              1 | [DOID:0050571](http://purl.obolibrary.org/obo/DOID_0050571) |
| `OMIM:PS600721` |              1 | [DOID:0050575](http://purl.obolibrary.org/obo/DOID_0050575) |
| `OMIM:PS266900` |              1 | [DOID:0050576](http://purl.obolibrary.org/obo/DOID_0050576) |
| `OMIM:PS218330` |              1 | [DOID:0050577](http://purl.obolibrary.org/obo/DOID_0050577) |
| `OMIM:PS153100` |              1 | [DOID:0050580](http://purl.obolibrary.org/obo/DOID_0050580) |
| `OMIM:PS608594` |              1 | [DOID:0050585](http://purl.obolibrary.org/obo/DOID_0050585) |
| `OMIM:PS266600` |              1 | [DOID:0050589](http://purl.obolibrary.org/obo/DOID_0050589) |
| `OMIM:PS202700` |              1 | [DOID:0050590](http://purl.obolibrary.org/obo/DOID_0050590) |
| `OMIM:PS106600` |              1 | [DOID:0050591](http://purl.obolibrary.org/obo/DOID_0050591) |
| `OMIM:PS208500` |              1 | [DOID:0050592](http://purl.obolibrary.org/obo/DOID_0050592) |
| `OMIM:PS604348` |              1 | [DOID:0050628](http://purl.obolibrary.org/obo/DOID_0050628) |
| `OMIM:PS225750` |              1 | [DOID:0050629](http://purl.obolibrary.org/obo/DOID_0050629) |
| `OMIM:PS203100` |              1 | [DOID:0050632](http://purl.obolibrary.org/obo/DOID_0050632) |
| `OMIM:PS104290` |              1 | [DOID:0050635](http://purl.obolibrary.org/obo/DOID_0050635) |
| `OMIM:PS105250` |              1 | [DOID:0050639](http://purl.obolibrary.org/obo/DOID_0050639) |
| `OMIM:PS108120` |              1 | [DOID:0050646](http://purl.obolibrary.org/obo/DOID_0050646) |
| `OMIM:PS608583` |              1 | [DOID:0050650](http://purl.obolibrary.org/obo/DOID_0050650) |
| `OMIM:PS211530` |              1 | [DOID:0050694](http://purl.obolibrary.org/obo/DOID_0050694) |
| `OMIM:PS210200` |              1 | [DOID:0050710](http://purl.obolibrary.org/obo/DOID_0050710) |
| `OMIM:PS607426` |              1 | [DOID:0050730](http://purl.obolibrary.org/obo/DOID_0050730) |
| `OMIM:PS208085` |              1 | [DOID:0050763](http://purl.obolibrary.org/obo/DOID_0050763) |
| `OMIM:PS168000` |              1 | [DOID:0050773](http://purl.obolibrary.org/obo/DOID_0050773) |
| `OMIM:PS309530` |              1 | [DOID:0050776](http://purl.obolibrary.org/obo/DOID_0050776) |
| `OMIM:PS213300` |              1 | [DOID:0050777](http://purl.obolibrary.org/obo/DOID_0050777) |
| `OMIM:PS249000` |              1 | [DOID:0050778](http://purl.obolibrary.org/obo/DOID_0050778) |
| `OMIM:PS236680` |              1 | [DOID:0050779](http://purl.obolibrary.org/obo/DOID_0050779) |
| `OMIM:PS185800` |              1 | [DOID:0050788](http://purl.obolibrary.org/obo/DOID_0050788) |
| `OMIM:PS186500` |              1 | [DOID:0050794](http://purl.obolibrary.org/obo/DOID_0050794) |
| `OMIM:PS300352` |              1 | [DOID:0050798](http://purl.obolibrary.org/obo/DOID_0050798) |
| `OMIM:PS236730` |              1 | [DOID:0050816](http://purl.obolibrary.org/obo/DOID_0050816) |
| `OMIM:PS233400` |              1 | [DOID:0050857](http://purl.obolibrary.org/obo/DOID_0050857) |
| `OMIM:PS167320` |              1 | [DOID:0050881](http://purl.obolibrary.org/obo/DOID_0050881) |
| `OMIM:PS213200` |              1 | [DOID:0050950](http://purl.obolibrary.org/obo/DOID_0050950) |
| `OMIM:PS601764` |              1 | [DOID:0060169](http://purl.obolibrary.org/obo/DOID_0060169) |
| `OMIM:PS257920` |              1 | [DOID:0060225](http://purl.obolibrary.org/obo/DOID_0060225) |
| `OMIM:PS100300` |              1 | [DOID:0060227](http://purl.obolibrary.org/obo/DOID_0060227) |
| `OMIM:PS105800` |              1 | [DOID:0060228](http://purl.obolibrary.org/obo/DOID_0060228) |
| `OMIM:PS243310` |              1 | [DOID:0060229](http://purl.obolibrary.org/obo/DOID_0060229) |
| `OMIM:PS115150` |              1 | [DOID:0060233](http://purl.obolibrary.org/obo/DOID_0060233) |
| `OMIM:PS278300` |              1 | [DOID:0060236](http://purl.obolibrary.org/obo/DOID_0060236) |
| `OMIM:PS600118` |              1 | [DOID:0060237](http://purl.obolibrary.org/obo/DOID_0060237) |
| `OMIM:PS601390` |              1 | [DOID:0060238](http://purl.obolibrary.org/obo/DOID_0060238) |
| `OMIM:PS600630` |              1 | [DOID:0060240](http://purl.obolibrary.org/obo/DOID_0060240) |
| `OMIM:PS607326` |              1 | [DOID:0060247](http://purl.obolibrary.org/obo/DOID_0060247) |
| `OMIM:PS269500` |              1 | [DOID:0060251](http://purl.obolibrary.org/obo/DOID_0060251) |
| `OMIM:PS268310` |              1 | [DOID:0060254](http://purl.obolibrary.org/obo/DOID_0060254) |
| `OMIM:PS607596` |              1 | [DOID:0060264](http://purl.obolibrary.org/obo/DOID_0060264) |
| `OMIM:PS609060` |              1 | [DOID:0060286](http://purl.obolibrary.org/obo/DOID_0060286) |
| `OMIM:PS258315` |              1 | [DOID:0060288](http://purl.obolibrary.org/obo/DOID_0060288) |
| `OMIM:PS272430` |              1 | [DOID:0060294](http://purl.obolibrary.org/obo/DOID_0060294) |
| `OMIM:PS224690` |              1 | [DOID:0060306](http://purl.obolibrary.org/obo/DOID_0060306) |
| `OMIM:PS156200` |              1 | [DOID:0060307](http://purl.obolibrary.org/obo/DOID_0060307) |
| `OMIM:PS249500` |              1 | [DOID:0060308](http://purl.obolibrary.org/obo/DOID_0060308) |
| `OMIM:PS309510` |              1 | [DOID:0060309](http://purl.obolibrary.org/obo/DOID_0060309) |
| `OMIM:PS250950` |              1 | [DOID:0060336](http://purl.obolibrary.org/obo/DOID_0060336) |
| `OMIM:PS122100` |              1 | [DOID:0060451](http://purl.obolibrary.org/obo/DOID_0060451) |
| `OMIM:PS122000` |              1 | [DOID:0060457](http://purl.obolibrary.org/obo/DOID_0060457) |
| `OMIM:PS228520` |              1 | [DOID:0060465](http://purl.obolibrary.org/obo/DOID_0060465) |
| `OMIM:PS253310` |              1 | [DOID:0060558](http://purl.obolibrary.org/obo/DOID_0060558) |
| `OMIM:PS220210` |              1 | [DOID:0060565](http://purl.obolibrary.org/obo/DOID_0060565) |
| `OMIM:PS605552` |              1 | [DOID:0060611](http://purl.obolibrary.org/obo/DOID_0060611) |
| `OMIM:PS107250` |              1 | [DOID:0060648](http://purl.obolibrary.org/obo/DOID_0060648) |
| `OMIM:PS242300` |              1 | [DOID:0060655](http://purl.obolibrary.org/obo/DOID_0060655) |
| `OMIM:PS604772` |              1 | [DOID:0060674](http://purl.obolibrary.org/obo/DOID_0060674) |
| `OMIM:PS600513` |              1 | [DOID:0060681](http://purl.obolibrary.org/obo/DOID_0060681) |
| `OMIM:PS149400` |              1 | [DOID:0060695](http://purl.obolibrary.org/obo/DOID_0060695) |
| `OMIM:PS145980` |              1 | [DOID:0060699](http://purl.obolibrary.org/obo/DOID_0060699) |
| `OMIM:PS308240` |              1 | [DOID:0060704](http://purl.obolibrary.org/obo/DOID_0060704) |
| `OMIM:PS275210` |              1 | [DOID:0060762](http://purl.obolibrary.org/obo/DOID_0060762) |
| `OMIM:PS214700` |              1 | [DOID:0060774](http://purl.obolibrary.org/obo/DOID_0060774) |
| `OMIM:PS312080` |              1 | [DOID:0060786](http://purl.obolibrary.org/obo/DOID_0060786) |
| `OMIM:PS214450` |              1 | [DOID:0060831](http://purl.obolibrary.org/obo/DOID_0060831) |
| `OMIM:PS169150` |              1 | [DOID:0060863](http://purl.obolibrary.org/obo/DOID_0060863) |
| `OMIM:PS603896` |              1 | [DOID:0060868](http://purl.obolibrary.org/obo/DOID_0060868) |
| `OMIM:PS602014` |              1 | [DOID:0060879](http://purl.obolibrary.org/obo/DOID_0060879) |
| `OMIM:PS256040` |              1 | [DOID:0060913](http://purl.obolibrary.org/obo/DOID_0060913) |
| `OMIM:PS254130` |              1 | [DOID:0070198](http://purl.obolibrary.org/obo/DOID_0070198) |
| `OMIM:PS211600` |              1 | [DOID:0070221](http://purl.obolibrary.org/obo/DOID_0070221) |
| `OMIM:PS243300` |              1 | [DOID:0070230](http://purl.obolibrary.org/obo/DOID_0070230) |
| `OMIM:PS251200` |              1 | [DOID:0070296](http://purl.obolibrary.org/obo/DOID_0070296) |
| `OMIM:PS603041` |              1 | [DOID:0070329](http://purl.obolibrary.org/obo/DOID_0070329) |
| `OMIM:PS605711` |              1 | [DOID:0070330](http://purl.obolibrary.org/obo/DOID_0070330) |
| `OMIM:PS158600` |              1 | [DOID:0070348](http://purl.obolibrary.org/obo/DOID_0070348) |
| `OMIM:PS239300` |              1 | [DOID:0070431](http://purl.obolibrary.org/obo/DOID_0070431) |
| `OMIM:PS136550` |              1 | [DOID:0070438](http://purl.obolibrary.org/obo/DOID_0070438) |
| `OMIM:PS616901` |              1 | [DOID:0070476](http://purl.obolibrary.org/obo/DOID_0070476) |
| `OMIM:PS123000` |              1 | [DOID:0080033](http://purl.obolibrary.org/obo/DOID_0080033) |
| `OMIM:PS200600` |              1 | [DOID:0080043](http://purl.obolibrary.org/obo/DOID_0080043) |
| `OMIM:PS108300` |              1 | [DOID:0080046](http://purl.obolibrary.org/obo/DOID_0080046) |
| `OMIM:PS178110` |              1 | [DOID:0080110](http://purl.obolibrary.org/obo/DOID_0080110) |
| `OMIM:PS135700` |              1 | [DOID:0080143](http://purl.obolibrary.org/obo/DOID_0080143) |
| `OMIM:PS610805` |              1 | [DOID:0080205](http://purl.obolibrary.org/obo/DOID_0080205) |
| `OMIM:PS601419` |              1 | [DOID:0080307](http://purl.obolibrary.org/obo/DOID_0080307) |
| `OMIM:PS604004` |              1 | [DOID:0080315](http://purl.obolibrary.org/obo/DOID_0080315) |
| `OMIM:PS173900` |              1 | [DOID:0080322](http://purl.obolibrary.org/obo/DOID_0080322) |
| `OMIM:PS192600` |              1 | [DOID:0080326](http://purl.obolibrary.org/obo/DOID_0080326) |
| `OMIM:PS109730` |              1 | [DOID:0080332](http://purl.obolibrary.org/obo/DOID_0080332) |
| `OMIM:PS119580` |              1 | [DOID:0080344](http://purl.obolibrary.org/obo/DOID_0080344) |
| `OMIM:PS214100` |              1 | [DOID:0080377](http://purl.obolibrary.org/obo/DOID_0080377) |
| `OMIM:PS614080` |              1 | [DOID:0080503](http://purl.obolibrary.org/obo/DOID_0080503) |
| `OMIM:PS613280` |              1 | [DOID:0080535](http://purl.obolibrary.org/obo/DOID_0080535) |
| `OMIM:PS308230` |              1 | [DOID:0080544](http://purl.obolibrary.org/obo/DOID_0080544) |
| `OMIM:PS147060` |              1 | [DOID:0080545](http://purl.obolibrary.org/obo/DOID_0080545) |
| `OMIM:PS610253` |              1 | [DOID:0080597](http://purl.obolibrary.org/obo/DOID_0080597) |
| `OMIM:PS202200` |              1 | [DOID:0080620](http://purl.obolibrary.org/obo/DOID_0080620) |
| `OMIM:PS203650` |              1 | [DOID:0080627](http://purl.obolibrary.org/obo/DOID_0080627) |
| `OMIM:PS600165` |              1 | [DOID:0080634](http://purl.obolibrary.org/obo/DOID_0080634) |
| `OMIM:PS309800` |              1 | [DOID:0080636](http://purl.obolibrary.org/obo/DOID_0080636) |
| `OMIM:PS612286` |              1 | [DOID:0080655](http://purl.obolibrary.org/obo/DOID_0080655) |
| `OMIM:PS161050` |              1 | [DOID:0080683](http://purl.obolibrary.org/obo/DOID_0080683) |
| `OMIM:PS257300` |              1 | [DOID:0080688](http://purl.obolibrary.org/obo/DOID_0080688) |
| `OMIM:PS251300` |              1 | [DOID:0080694](http://purl.obolibrary.org/obo/DOID_0080694) |
| `OMIM:PS615438` |              1 | [DOID:0080716](http://purl.obolibrary.org/obo/DOID_0080716) |
| `OMIM:PS127000` |              1 | [DOID:0080724](http://purl.obolibrary.org/obo/DOID_0080724) |
| `OMIM:PS214150` |              1 | [DOID:0080910](http://purl.obolibrary.org/obo/DOID_0080910) |
| `OMIM:PS607095` |              1 | [DOID:0080942](http://purl.obolibrary.org/obo/DOID_0080942) |
| `OMIM:PS617468` |              1 | [DOID:0080954](http://purl.obolibrary.org/obo/DOID_0080954) |
| `OMIM:PS136760` |              1 | [DOID:0081044](http://purl.obolibrary.org/obo/DOID_0081044) |
| `OMIM:PS213980` |              1 | [DOID:0081072](http://purl.obolibrary.org/obo/DOID_0081072) |
| `OMIM:PS145420` |              1 | [DOID:0081073](http://purl.obolibrary.org/obo/DOID_0081073) |
| `OMIM:PS300291` |              1 | [DOID:0081077](http://purl.obolibrary.org/obo/DOID_0081077) |
| `OMIM:PS613339` |              1 | [DOID:0081104](http://purl.obolibrary.org/obo/DOID_0081104) |
| `OMIM:PS248370` |              1 | [DOID:0081127](http://purl.obolibrary.org/obo/DOID_0081127) |
| `OMIM:PS164310` |              1 | [DOID:0081296](http://purl.obolibrary.org/obo/DOID_0081296) |
| `OMIM:PS149730` |              1 | [DOID:0081370](http://purl.obolibrary.org/obo/DOID_0081370) |
| `OMIM:PS219000` |              1 | [DOID:0090001](http://purl.obolibrary.org/obo/DOID_0090001) |
| `OMIM:PS242860` |              1 | [DOID:0090007](http://purl.obolibrary.org/obo/DOID_0090007) |
| `OMIM:PS183600` |              1 | [DOID:0090020](http://purl.obolibrary.org/obo/DOID_0090020) |
| `OMIM:PS120100` |              1 | [DOID:0090061](http://purl.obolibrary.org/obo/DOID_0090061) |
| `OMIM:PS147950` |              1 | [DOID:0090070](http://purl.obolibrary.org/obo/DOID_0090070) |
| `OMIM:PS601198` |              1 | [DOID:0090109](http://purl.obolibrary.org/obo/DOID_0090109) |
| `OMIM:PS614039` |              1 | [DOID:0090131](http://purl.obolibrary.org/obo/DOID_0090131) |
| `OMIM:PS604931` |              1 | [DOID:0090139](http://purl.obolibrary.org/obo/DOID_0090139) |
| `OMIM:PS603511` |              1 | [DOID:0110273](http://purl.obolibrary.org/obo/DOID_0110273) |
| `OMIM:PS253600` |              1 | [DOID:0110274](http://purl.obolibrary.org/obo/DOID_0110274) |
| `OMIM:PS234200` |              1 | [DOID:0110734](http://purl.obolibrary.org/obo/DOID_0110734) |
| `OMIM:PS113900` |              1 | [DOID:0111073](http://purl.obolibrary.org/obo/DOID_0111073) |
| `OMIM:PS252150` |              1 | [DOID:0111165](http://purl.obolibrary.org/obo/DOID_0111165) |
| `OMIM:PS236670` |              1 | [DOID:0111229](http://purl.obolibrary.org/obo/DOID_0111229) |
| `OMIM:PS121210` |              1 | [DOID:0111297](http://purl.obolibrary.org/obo/DOID_0111297) |
| `OMIM:PS208150` |              1 | [DOID:0111375](http://purl.obolibrary.org/obo/DOID_0111375) |
| `OMIM:PS222470` |              1 | [DOID:0111414](http://purl.obolibrary.org/obo/DOID_0111414) |
| `OMIM:PS601068` |              1 | [DOID:0111689](http://purl.obolibrary.org/obo/DOID_0111689) |
| `OMIM:PS231050` |              1 | [DOID:0111724](http://purl.obolibrary.org/obo/DOID_0111724) |
| `OMIM:PS615040` |              1 | [DOID:0111728](http://purl.obolibrary.org/obo/DOID_0111728) |
| `OMIM:PS400043` |              1 | [DOID:0111757](http://purl.obolibrary.org/obo/DOID_0111757) |
| `OMIM:PS305620` |              1 | [DOID:0111785](http://purl.obolibrary.org/obo/DOID_0111785) |
| `OMIM:PS601675` |              1 | [DOID:0111866](http://purl.obolibrary.org/obo/DOID_0111866) |
| `OMIM:PS309801` |              1 | [DOID:0111875](http://purl.obolibrary.org/obo/DOID_0111875) |
| `OMIM:PS258150` |              1 | [DOID:0111910](http://purl.obolibrary.org/obo/DOID_0111910) |
| `OMIM:PS252010` |              1 | [DOID:0112065](http://purl.obolibrary.org/obo/DOID_0112065) |
| `OMIM:PS271640` |              1 | [DOID:0112197](http://purl.obolibrary.org/obo/DOID_0112197) |
| `OMIM:PS308350` |              1 | [DOID:0112202](http://purl.obolibrary.org/obo/DOID_0112202) |
| `OMIM:PS175780` |              1 | [DOID:0112313](http://purl.obolibrary.org/obo/DOID_0112313) |
| `OMIM:PS613155` |              1 | [DOID:0112375](http://purl.obolibrary.org/obo/DOID_0112375) |
| `OMIM:PS118100` |              1 | [DOID:10426](http://purl.obolibrary.org/obo/DOID_10426)     |
| `OMIM:PS268000` |              1 | [DOID:10584](http://purl.obolibrary.org/obo/DOID_10584)     |
| `OMIM:PS118220` |              1 | [DOID:10595](http://purl.obolibrary.org/obo/DOID_10595)     |
| `OMIM:PS134600` |              1 | [DOID:1062](http://purl.obolibrary.org/obo/DOID_1062)       |
| `OMIM:PS133100` |              1 | [DOID:10780](http://purl.obolibrary.org/obo/DOID_10780)     |
| `OMIM:PS603075` |              1 | [DOID:10871](http://purl.obolibrary.org/obo/DOID_10871)     |
| `OMIM:PS612900` |              1 | [DOID:10970](http://purl.obolibrary.org/obo/DOID_10970)     |
| `OMIM:PS160500` |              1 | [DOID:11720](http://purl.obolibrary.org/obo/DOID_11720)     |
| `OMIM:PS122470` |              1 | [DOID:11725](http://purl.obolibrary.org/obo/DOID_11725)     |
| `OMIM:PS310300` |              1 | [DOID:11726](http://purl.obolibrary.org/obo/DOID_11726)     |
| `OMIM:PS115430` |              1 | [DOID:12169](http://purl.obolibrary.org/obo/DOID_12169)     |
| `OMIM:PS607594` |              1 | [DOID:12177](http://purl.obolibrary.org/obo/DOID_12177)     |
| `OMIM:PS166800` |              1 | [DOID:12185](http://purl.obolibrary.org/obo/DOID_12185)     |
| `OMIM:PS109720` |              1 | [DOID:12236](http://purl.obolibrary.org/obo/DOID_12236)     |
| `OMIM:PS166200` |              1 | [DOID:12347](http://purl.obolibrary.org/obo/DOID_12347)     |
| `OMIM:PS157640` |              1 | [DOID:12558](http://purl.obolibrary.org/obo/DOID_12558)     |
| `OMIM:PS256100` |              1 | [DOID:12712](http://purl.obolibrary.org/obo/DOID_12712)     |
| `OMIM:PS607014` |              1 | [DOID:12798](http://purl.obolibrary.org/obo/DOID_12798)     |
| `OMIM:PS115200` |              1 | [DOID:12930](http://purl.obolibrary.org/obo/DOID_12930)     |
| `OMIM:PS603278` |              1 | [DOID:1312](http://purl.obolibrary.org/obo/DOID_1312)       |
| `OMIM:PS256450` |              1 | [DOID:13317](http://purl.obolibrary.org/obo/DOID_13317)     |
| `OMIM:PS130000` |              1 | [DOID:13359](http://purl.obolibrary.org/obo/DOID_13359)     |
| `OMIM:PS224120` |              1 | [DOID:1338](http://purl.obolibrary.org/obo/DOID_1338)       |
| `OMIM:PS105650` |              1 | [DOID:1339](http://purl.obolibrary.org/obo/DOID_1339)       |
| `OMIM:PS191100` |              1 | [DOID:13515](http://purl.obolibrary.org/obo/DOID_13515)     |
| `OMIM:PS259700` |              1 | [DOID:13533](http://purl.obolibrary.org/obo/DOID_13533)     |
| `OMIM:PS607634` |              1 | [DOID:13533](http://purl.obolibrary.org/obo/DOID_13533)     |
| `OMIM:PS227650` |              1 | [DOID:13636](http://purl.obolibrary.org/obo/DOID_13636)     |
| `OMIM:PS226400` |              1 | [DOID:13777](http://purl.obolibrary.org/obo/DOID_13777)     |
| `OMIM:PS125310` |              1 | [DOID:13945](http://purl.obolibrary.org/obo/DOID_13945)     |
| `OMIM:PS151100` |              1 | [DOID:14291](http://purl.obolibrary.org/obo/DOID_14291)     |
| `OMIM:PS168600` |              1 | [DOID:14330](http://purl.obolibrary.org/obo/DOID_14330)     |
| `OMIM:PS164400` |              1 | [DOID:1441](http://purl.obolibrary.org/obo/DOID_1441)       |
| `OMIM:PS400044` |              1 | [DOID:14448](http://purl.obolibrary.org/obo/DOID_14448)     |
| `OMIM:PS233300` |              1 | [DOID:14450](http://purl.obolibrary.org/obo/DOID_14450)     |
| `OMIM:PS256730` |              1 | [DOID:14503](http://purl.obolibrary.org/obo/DOID_14503)     |
| `OMIM:PS117550` |              1 | [DOID:14748](http://purl.obolibrary.org/obo/DOID_14748)     |
| `OMIM:PS204000` |              1 | [DOID:14791](http://purl.obolibrary.org/obo/DOID_14791)     |
| `OMIM:PS108800` |              1 | [DOID:1882](http://purl.obolibrary.org/obo/DOID_1882)       |
| `OMIM:PS135900` |              1 | [DOID:1925](http://purl.obolibrary.org/obo/DOID_1925)       |
| `OMIM:PS209900` |              1 | [DOID:1935](http://purl.obolibrary.org/obo/DOID_1935)       |
| `OMIM:PS305100` |              1 | [DOID:2121](http://purl.obolibrary.org/obo/DOID_2121)       |
| `OMIM:PS104500` |              1 | [DOID:2187](http://purl.obolibrary.org/obo/DOID_2187)       |
| `OMIM:PS235200` |              1 | [DOID:2352](http://purl.obolibrary.org/obo/DOID_2352)       |
| `OMIM:PS188050` |              1 | [DOID:2452](http://purl.obolibrary.org/obo/DOID_2452)       |
| `OMIM:PS303350` |              1 | [DOID:2476](http://purl.obolibrary.org/obo/DOID_2476)       |
| `OMIM:PS109400` |              1 | [DOID:2512](http://purl.obolibrary.org/obo/DOID_2512)       |
| `OMIM:PS215100` |              1 | [DOID:2580](http://purl.obolibrary.org/obo/DOID_2580)       |
| `OMIM:PS601495` |              1 | [DOID:2583](http://purl.obolibrary.org/obo/DOID_2583)       |
| `OMIM:PS256300` |              1 | [DOID:2590](http://purl.obolibrary.org/obo/DOID_2590)       |
| `OMIM:PS127550` |              1 | [DOID:2729](http://purl.obolibrary.org/obo/DOID_2729)       |
| `OMIM:PS192500` |              1 | [DOID:2843](http://purl.obolibrary.org/obo/DOID_2843)       |
| `OMIM:PS154500` |              1 | [DOID:2908](http://purl.obolibrary.org/obo/DOID_2908)       |
| `OMIM:PS259900` |              1 | [DOID:2977](http://purl.obolibrary.org/obo/DOID_2977)       |
| `OMIM:PS151623` |              1 | [DOID:3012](http://purl.obolibrary.org/obo/DOID_3012)       |
| `OMIM:PS137800` |              1 | [DOID:3070](http://purl.obolibrary.org/obo/DOID_3070)       |
| `OMIM:PS123700` |              1 | [DOID:3144](http://purl.obolibrary.org/obo/DOID_3144)       |
| `OMIM:PS161800` |              1 | [DOID:3191](http://purl.obolibrary.org/obo/DOID_3191)       |
| `OMIM:PS162091` |              1 | [DOID:3204](http://purl.obolibrary.org/obo/DOID_3204)       |
| `OMIM:PS306400` |              1 | [DOID:3265](http://purl.obolibrary.org/obo/DOID_3265)       |
| `OMIM:PS603165` |              1 | [DOID:3310](http://purl.obolibrary.org/obo/DOID_3310)       |
| `OMIM:PS105400` |              1 | [DOID:332](http://purl.obolibrary.org/obo/DOID_332)         |
| `OMIM:PS600512` |              1 | [DOID:3328](http://purl.obolibrary.org/obo/DOID_3328)       |
| `OMIM:PS163950` |              1 | [DOID:3490](http://purl.obolibrary.org/obo/DOID_3490)       |
| `OMIM:PS601462` |              1 | [DOID:3635](http://purl.obolibrary.org/obo/DOID_3635)       |
| `OMIM:PS203300` |              1 | [DOID:3753](http://purl.obolibrary.org/obo/DOID_3753)       |
| `OMIM:PS220110` |              1 | [DOID:3762](http://purl.obolibrary.org/obo/DOID_3762)       |
| `OMIM:PS102200` |              1 | [DOID:3829](http://purl.obolibrary.org/obo/DOID_3829)       |
| `OMIM:PS120435` |              1 | [DOID:3883](http://purl.obolibrary.org/obo/DOID_3883)       |
| `OMIM:PS115210` |              1 | [DOID:397](http://purl.obolibrary.org/obo/DOID_397)         |
| `OMIM:PS601678` |              1 | [DOID:445](http://purl.obolibrary.org/obo/DOID_445)         |
| `OMIM:PS605389` |              1 | [DOID:4535](http://purl.obolibrary.org/obo/DOID_4535)       |
| `OMIM:PS113800` |              1 | [DOID:4603](http://purl.obolibrary.org/obo/DOID_4603)       |
| `OMIM:PS236100` |              1 | [DOID:4621](http://purl.obolibrary.org/obo/DOID_4621)       |
| `OMIM:PS190300` |              1 | [DOID:4990](http://purl.obolibrary.org/obo/DOID_4990)       |
| `OMIM:PS167250` |              1 | [DOID:5408](http://purl.obolibrary.org/obo/DOID_5408)       |
| `OMIM:PS311360` |              1 | [DOID:5426](http://purl.obolibrary.org/obo/DOID_5426)       |
| `OMIM:PS128100` |              1 | [DOID:543](http://purl.obolibrary.org/obo/DOID_543)         |
| `OMIM:PS265450` |              1 | [DOID:5453](http://purl.obolibrary.org/obo/DOID_5453)       |
| `OMIM:PS165500` |              1 | [DOID:5723](http://purl.obolibrary.org/obo/DOID_5723)       |
| `OMIM:PS300755` |              1 | [DOID:612](http://purl.obolibrary.org/obo/DOID_612)         |
| `OMIM:PS158350` |              1 | [DOID:6457](http://purl.obolibrary.org/obo/DOID_6457)       |
| `OMIM:PS106300` |              1 | [DOID:7147](http://purl.obolibrary.org/obo/DOID_7147)       |
| `OMIM:PS116200` |              1 | [DOID:83](http://purl.obolibrary.org/obo/DOID_83)           |
| `OMIM:PS145600` |              1 | [DOID:8545](http://purl.obolibrary.org/obo/DOID_8545)       |
| `OMIM:PS177900` |              1 | [DOID:8893](http://purl.obolibrary.org/obo/DOID_8893)       |
| `OMIM:PS254800` |              1 | [DOID:891](http://purl.obolibrary.org/obo/DOID_891)         |
| `OMIM:PS300751` |              1 | [DOID:8955](http://purl.obolibrary.org/obo/DOID_8955)       |
| `OMIM:PS193500` |              1 | [DOID:9258](http://purl.obolibrary.org/obo/DOID_9258)       |
| `OMIM:PS613038` |              1 | [DOID:9410](http://purl.obolibrary.org/obo/DOID_9410)       |
| `OMIM:PS244400` |              1 | [DOID:9562](http://purl.obolibrary.org/obo/DOID_9562)       |
| `OMIM:PS211400` |              1 | [DOID:9563](http://purl.obolibrary.org/obo/DOID_9563)       |
| `OMIM:PS310700` |              1 | [DOID:9649](http://purl.obolibrary.org/obo/DOID_9649)       |
| `OMIM:PS203655` |              1 | [DOID:987](http://purl.obolibrary.org/obo/DOID_987)         |

