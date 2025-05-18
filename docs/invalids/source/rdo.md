# rdo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `rdo`.


## `ClinVar`: ClinVar Variation

Overall, there were 2 invalid
xrefs to external prefixed with `ClinVar` (standardized to Bioregistry
prefix [`clinvar`](https://bioregistry.io/clinvar)) that
did not match the standard pattern `^\d+$`.

| external_xref            |   usages_count | usages                                                      |
|--------------------------|----------------|-------------------------------------------------------------|
| `ClinVar:VCV000983267`   |              1 | [DOID:9000729](http://purl.obolibrary.org/obo/DOID_9000729) |
| `ClinVar:VCV001077148.1` |              1 | [DOID:9000895](http://purl.obolibrary.org/obo/DOID_9000895) |

## `EFO`: Experimental Factor Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `EFO` (standardized to Bioregistry
prefix [`efo`](https://bioregistry.io/efo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref       |   usages_count | usages                                                      |
|---------------------|----------------|-------------------------------------------------------------|
| `EFO:MONDO:0018416` |              1 | [DOID:9009256](http://purl.obolibrary.org/obo/DOID_9009256) |

## `ICD-O`: International Classification of Diseases for Oncology

Overall, there were 47 invalid
xrefs to external prefixed with `ICD-O` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `ICD-O:M9861/3` |              1 | [DOID:0070323](http://purl.obolibrary.org/obo/DOID_0070323) |
| `ICD-O:M9724/3` |              1 | [DOID:0070324](http://purl.obolibrary.org/obo/DOID_0070324) |
| `ICD-O:M8700/3` |              1 | [DOID:0070325](http://purl.obolibrary.org/obo/DOID_0070325) |
| `ICD-O:M8761/3` |              1 | [DOID:0070327](http://purl.obolibrary.org/obo/DOID_0070327) |
| `ICD-O:M9835/3` |              1 | [DOID:0080144](http://purl.obolibrary.org/obo/DOID_0080144) |
| `ICD-O:M9831/3` |              1 | [DOID:0080145](http://purl.obolibrary.org/obo/DOID_0080145) |
| `ICD-O:M9837/3` |              1 | [DOID:0080145](http://purl.obolibrary.org/obo/DOID_0080145) |
| `ICD-O:M9836/3` |              1 | [DOID:0080146](http://purl.obolibrary.org/obo/DOID_0080146) |
| `ICD-O:M9729/3` |              1 | [DOID:0080148](http://purl.obolibrary.org/obo/DOID_0080148) |
| `ICD-O:M8960/3` |              1 | [DOID:2154](http://purl.obolibrary.org/obo/DOID_2154)       |
| `ICD-O:M9450/3` |              1 | [DOID:3183](http://purl.obolibrary.org/obo/DOID_3183)       |
| `ICD-O:M8810/3` |              1 | [DOID:3520](http://purl.obolibrary.org/obo/DOID_3520)       |
| `ICD-O:M9390/3` |              1 | [DOID:3545](http://purl.obolibrary.org/obo/DOID_3545)       |
| `ICD-O:M8000/3` |              1 | [DOID:3675](http://purl.obolibrary.org/obo/DOID_3675)       |
| `ICD-O:M9470/3` |              1 | [DOID:3869](http://purl.obolibrary.org/obo/DOID_3869)       |
| `ICD-O:M9473/3` |              1 | [DOID:3870](http://purl.obolibrary.org/obo/DOID_3870)       |
| `ICD-O:M8312/3` |              1 | [DOID:4454](http://purl.obolibrary.org/obo/DOID_4454)       |
| `ICD-O:M9240/3` |              1 | [DOID:4546](http://purl.obolibrary.org/obo/DOID_4546)       |
| `ICD-O:M9540/3` |              1 | [DOID:4690](http://purl.obolibrary.org/obo/DOID_4690)       |
| `ICD-O:M8850/3` |              1 | [DOID:5695](http://purl.obolibrary.org/obo/DOID_5695)       |
| `ICD-O:M9180/3` |              1 | [DOID:5809](http://purl.obolibrary.org/obo/DOID_5809)       |
| `ICD-O:M9590/3` |              1 | [DOID:5823](http://purl.obolibrary.org/obo/DOID_5823)       |
| `ICD-O:M8990/3` |              1 | [DOID:5893](http://purl.obolibrary.org/obo/DOID_5893)       |
| `ICD-O:M9064/3` |              1 | [DOID:6052](http://purl.obolibrary.org/obo/DOID_6052)       |
| `ICD-O:M9071/3` |              1 | [DOID:6083](http://purl.obolibrary.org/obo/DOID_6083)       |
| `ICD-O:M8720/3` |              1 | [DOID:6089](http://purl.obolibrary.org/obo/DOID_6089)       |
| `ICD-O:M9070/3` |              1 | [DOID:6162](http://purl.obolibrary.org/obo/DOID_6162)       |
| `ICD-O:M9081/3` |              1 | [DOID:6474](http://purl.obolibrary.org/obo/DOID_6474)       |
| `ICD-O:M9231/3` |              1 | [DOID:6494](http://purl.obolibrary.org/obo/DOID_6494)       |
| `ICD-O:M9380/3` |              1 | [DOID:6576](http://purl.obolibrary.org/obo/DOID_6576)       |
| `ICD-O:M9100/3` |              1 | [DOID:6639](http://purl.obolibrary.org/obo/DOID_6639)       |
| `ICD-O:M8910/3` |              1 | [DOID:6786](http://purl.obolibrary.org/obo/DOID_6786)       |
| `ICD-O:M9421/1` |              1 | [DOID:6812](http://purl.obolibrary.org/obo/DOID_6812)       |
| `ICD-O:M8170/3` |              1 | [DOID:684](http://purl.obolibrary.org/obo/DOID_684)         |
| `ICD-O:M9080/3` |              1 | [DOID:7037](http://purl.obolibrary.org/obo/DOID_7037)       |
| `ICD-O:M8804/3` |              1 | [DOID:7095](http://purl.obolibrary.org/obo/DOID_7095)       |
| `ICD-O:M9060/3` |              1 | [DOID:7340](http://purl.obolibrary.org/obo/DOID_7340)       |
| `ICD-O:M8901/3` |              1 | [DOID:7463](http://purl.obolibrary.org/obo/DOID_7463)       |
| `ICD-O:M9085/3` |              1 | [DOID:7516](http://purl.obolibrary.org/obo/DOID_7516)       |
| `ICD-O:M9195/3` |              1 | [DOID:7612](http://purl.obolibrary.org/obo/DOID_7612)       |
| `ICD-O:M9500/3` |              1 | [DOID:769](http://purl.obolibrary.org/obo/DOID_769)         |
| `ICD-O:M9150/3` |              1 | [DOID:7731](http://purl.obolibrary.org/obo/DOID_7731)       |
| `ICD-O:M9560/3` |              1 | [DOID:7732](http://purl.obolibrary.org/obo/DOID_7732)       |
| `ICD-O:M9510/3` |              1 | [DOID:7747](http://purl.obolibrary.org/obo/DOID_7747)       |
| `ICD-O:M9800/3` |              1 | [DOID:7757](http://purl.obolibrary.org/obo/DOID_7757)       |
| `ICD-O:M9392/3` |              1 | [DOID:7841](http://purl.obolibrary.org/obo/DOID_7841)       |
| `ICD-O:M8860/0` |              1 | [DOID:8410](http://purl.obolibrary.org/obo/DOID_8410)       |

## `ICD11`: International Classification of Diseases, 11th Revision (Foundation Component)

Overall, there were 4 invalid
xrefs to external prefixed with `ICD11` (standardized to Bioregistry
prefix [`icd11`](https://bioregistry.io/icd11)) that
did not match the standard pattern `^[1-9]\d*$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `ICD11:2A81.Z`  |              1 | [DOID:0050745](http://purl.obolibrary.org/obo/DOID_0050745) |
| `ICD11:4B24`    |              1 | [DOID:0081267](http://purl.obolibrary.org/obo/DOID_0081267) |
| `ICD11:2D10.0`  |              1 | [DOID:3962](http://purl.obolibrary.org/obo/DOID_3962)       |
| `ICD11:2D10.1`  |              1 | [DOID:3969](http://purl.obolibrary.org/obo/DOID_3969)       |

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

## `MESH`: Medical Subject Headings

Overall, there were 1 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D|M)\d{6,9}$`.

| external_xref   |   usages_count | usages                                          |
|-----------------|----------------|-------------------------------------------------|
| `MESH:C`        |              1 | [DOID:4](http://purl.obolibrary.org/obo/DOID_4) |

## `MIM`: Online Mendelian Inheritance in Man

Overall, there were 579 invalid
xrefs to external prefixed with `MIM` (standardized to Bioregistry
prefix [`omim`](https://bioregistry.io/omim)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------|
| `MIM:PS235400`  |              2 | [DOID:0080301](http://purl.obolibrary.org/obo/DOID_0080301), [DOID:12554](http://purl.obolibrary.org/obo/DOID_12554) |
| `MIM:PS600669`  |              2 | [DOID:1827](http://purl.obolibrary.org/obo/DOID_1827), [DOID:9009315](http://purl.obolibrary.org/obo/DOID_9009315)   |
| `MIM:PS128200`  |              2 | [DOID:543](http://purl.obolibrary.org/obo/DOID_543), [DOID:9009225](http://purl.obolibrary.org/obo/DOID_9009225)     |
| `MIM:PS614388`  |              2 | [DOID:9009111](http://purl.obolibrary.org/obo/DOID_9009111), [DOID:936](http://purl.obolibrary.org/obo/DOID_936)     |
| `MIM:232200#33` |              1 | [DOID:0081329](http://purl.obolibrary.org/obo/DOID_0081329)                                                          |
| `MIM:PS267700`  |              1 | [DOID:0050120](http://purl.obolibrary.org/obo/DOID_0050120)                                                          |
| `MIM:PS275200`  |              1 | [DOID:0050328](http://purl.obolibrary.org/obo/DOID_0050328)                                                          |
| `MIM:PS608415`  |              1 | [DOID:0050335](http://purl.obolibrary.org/obo/DOID_0050335)                                                          |
| `MIM:PS175100`  |              1 | [DOID:0050424](http://purl.obolibrary.org/obo/DOID_0050424)                                                          |
| `MIM:PS102300`  |              1 | [DOID:0050425](http://purl.obolibrary.org/obo/DOID_0050425)                                                          |
| `MIM:PS107970`  |              1 | [DOID:0050431](http://purl.obolibrary.org/obo/DOID_0050431)                                                          |
| `MIM:PS608638`  |              1 | [DOID:0050432](http://purl.obolibrary.org/obo/DOID_0050432)                                                          |
| `MIM:PS276900`  |              1 | [DOID:0050439](http://purl.obolibrary.org/obo/DOID_0050439)                                                          |
| `MIM:PS151660`  |              1 | [DOID:0050440](http://purl.obolibrary.org/obo/DOID_0050440)                                                          |
| `MIM:PS193900`  |              1 | [DOID:0050448](http://purl.obolibrary.org/obo/DOID_0050448)                                                          |
| `MIM:PS167200`  |              1 | [DOID:0050449](http://purl.obolibrary.org/obo/DOID_0050449)                                                          |
| `MIM:PS601144`  |              1 | [DOID:0050451](http://purl.obolibrary.org/obo/DOID_0050451)                                                          |
| `MIM:PS607432`  |              1 | [DOID:0050453](http://purl.obolibrary.org/obo/DOID_0050453)                                                          |
| `MIM:PS300049`  |              1 | [DOID:0050454](http://purl.obolibrary.org/obo/DOID_0050454)                                                          |
| `MIM:PS609192`  |              1 | [DOID:0050466](http://purl.obolibrary.org/obo/DOID_0050466)                                                          |
| `MIM:PS133200`  |              1 | [DOID:0050467](http://purl.obolibrary.org/obo/DOID_0050467)                                                          |
| `MIM:PS277600`  |              1 | [DOID:0050475](http://purl.obolibrary.org/obo/DOID_0050475)                                                          |
| `MIM:PS177200`  |              1 | [DOID:0050477](http://purl.obolibrary.org/obo/DOID_0050477)                                                          |
| `MIM:PS138800`  |              1 | [DOID:0050489](http://purl.obolibrary.org/obo/DOID_0050489)                                                          |
| `MIM:PS310500`  |              1 | [DOID:0050534](http://purl.obolibrary.org/obo/DOID_0050534)                                                          |
| `MIM:PS133780`  |              1 | [DOID:0050535](http://purl.obolibrary.org/obo/DOID_0050535)                                                          |
| `MIM:PS306955`  |              1 | [DOID:0050545](http://purl.obolibrary.org/obo/DOID_0050545)                                                          |
| `MIM:PS162400`  |              1 | [DOID:0050548](http://purl.obolibrary.org/obo/DOID_0050548)                                                          |
| `MIM:PS254090`  |              1 | [DOID:0050558](http://purl.obolibrary.org/obo/DOID_0050558)                                                          |
| `MIM:PS124900`  |              1 | [DOID:0050564](http://purl.obolibrary.org/obo/DOID_0050564)                                                          |
| `MIM:PS220290`  |              1 | [DOID:0050565](http://purl.obolibrary.org/obo/DOID_0050565)                                                          |
| `MIM:PS304500`  |              1 | [DOID:0050566](http://purl.obolibrary.org/obo/DOID_0050566)                                                          |
| `MIM:PS119530`  |              1 | [DOID:0050567](http://purl.obolibrary.org/obo/DOID_0050567)                                                          |
| `MIM:PS277300`  |              1 | [DOID:0050568](http://purl.obolibrary.org/obo/DOID_0050568)                                                          |
| `MIM:PS210600`  |              1 | [DOID:0050569](http://purl.obolibrary.org/obo/DOID_0050569)                                                          |
| `MIM:PS212065`  |              1 | [DOID:0050570](http://purl.obolibrary.org/obo/DOID_0050570)                                                          |
| `MIM:PS212066`  |              1 | [DOID:0050571](http://purl.obolibrary.org/obo/DOID_0050571)                                                          |
| `MIM:PS120970`  |              1 | [DOID:0050572](http://purl.obolibrary.org/obo/DOID_0050572)                                                          |
| `MIM:PS600721`  |              1 | [DOID:0050575](http://purl.obolibrary.org/obo/DOID_0050575)                                                          |
| `MIM:PS266900`  |              1 | [DOID:0050576](http://purl.obolibrary.org/obo/DOID_0050576)                                                          |
| `MIM:PS218330`  |              1 | [DOID:0050577](http://purl.obolibrary.org/obo/DOID_0050577)                                                          |
| `MIM:PS153100`  |              1 | [DOID:0050580](http://purl.obolibrary.org/obo/DOID_0050580)                                                          |
| `MIM:PS608594`  |              1 | [DOID:0050585](http://purl.obolibrary.org/obo/DOID_0050585)                                                          |
| `MIM:PS266600`  |              1 | [DOID:0050589](http://purl.obolibrary.org/obo/DOID_0050589)                                                          |
| `MIM:PS614328`  |              1 | [DOID:0050589](http://purl.obolibrary.org/obo/DOID_0050589)                                                          |
| `MIM:PS202700`  |              1 | [DOID:0050590](http://purl.obolibrary.org/obo/DOID_0050590)                                                          |
| `MIM:PS106600`  |              1 | [DOID:0050591](http://purl.obolibrary.org/obo/DOID_0050591)                                                          |
| `MIM:PS208500`  |              1 | [DOID:0050592](http://purl.obolibrary.org/obo/DOID_0050592)                                                          |
| `MIM:PS604348`  |              1 | [DOID:0050628](http://purl.obolibrary.org/obo/DOID_0050628)                                                          |
| `MIM:PS225750`  |              1 | [DOID:0050629](http://purl.obolibrary.org/obo/DOID_0050629)                                                          |
| `MIM:PS203100`  |              1 | [DOID:0050632](http://purl.obolibrary.org/obo/DOID_0050632)                                                          |
| `MIM:PS104290`  |              1 | [DOID:0050635](http://purl.obolibrary.org/obo/DOID_0050635)                                                          |
| `MIM:PS105250`  |              1 | [DOID:0050639](http://purl.obolibrary.org/obo/DOID_0050639)                                                          |
| `MIM:PS208000`  |              1 | [DOID:0050644](http://purl.obolibrary.org/obo/DOID_0050644)                                                          |
| `MIM:PS108120`  |              1 | [DOID:0050646](http://purl.obolibrary.org/obo/DOID_0050646)                                                          |
| `MIM:PS108720`  |              1 | [DOID:0050648](http://purl.obolibrary.org/obo/DOID_0050648)                                                          |
| `MIM:PS608583`  |              1 | [DOID:0050650](http://purl.obolibrary.org/obo/DOID_0050650)                                                          |
| `MIM:PS606215`  |              1 | [DOID:0050651](http://purl.obolibrary.org/obo/DOID_0050651)                                                          |
| `MIM:PS153840`  |              1 | [DOID:0050661](http://purl.obolibrary.org/obo/DOID_0050661)                                                          |
| `MIM:PS158810`  |              1 | [DOID:0050663](http://purl.obolibrary.org/obo/DOID_0050663)                                                          |
| `MIM:PS607765`  |              1 | [DOID:0050674](http://purl.obolibrary.org/obo/DOID_0050674)                                                          |
| `MIM:PS211530`  |              1 | [DOID:0050694](http://purl.obolibrary.org/obo/DOID_0050694)                                                          |
| `MIM:PS300009`  |              1 | [DOID:0050699](http://purl.obolibrary.org/obo/DOID_0050699)                                                          |
| `MIM:PS210200`  |              1 | [DOID:0050710](http://purl.obolibrary.org/obo/DOID_0050710)                                                          |
| `MIM:PS256520`  |              1 | [DOID:0050721](http://purl.obolibrary.org/obo/DOID_0050721)                                                          |
| `MIM:PS607426`  |              1 | [DOID:0050730](http://purl.obolibrary.org/obo/DOID_0050730)                                                          |
| `MIM:PS208085`  |              1 | [DOID:0050763](http://purl.obolibrary.org/obo/DOID_0050763)                                                          |
| `MIM:PS174050`  |              1 | [DOID:0050770](http://purl.obolibrary.org/obo/DOID_0050770)                                                          |
| `MIM:PS168000`  |              1 | [DOID:0050773](http://purl.obolibrary.org/obo/DOID_0050773)                                                          |
| `MIM:PS309530`  |              1 | [DOID:0050776](http://purl.obolibrary.org/obo/DOID_0050776)                                                          |
| `MIM:PS213300`  |              1 | [DOID:0050777](http://purl.obolibrary.org/obo/DOID_0050777)                                                          |
| `MIM:PS249000`  |              1 | [DOID:0050778](http://purl.obolibrary.org/obo/DOID_0050778)                                                          |
| `MIM:PS236680`  |              1 | [DOID:0050779](http://purl.obolibrary.org/obo/DOID_0050779)                                                          |
| `MIM:PS185800`  |              1 | [DOID:0050788](http://purl.obolibrary.org/obo/DOID_0050788)                                                          |
| `MIM:PS609620`  |              1 | [DOID:0050793](http://purl.obolibrary.org/obo/DOID_0050793)                                                          |
| `MIM:PS186500`  |              1 | [DOID:0050794](http://purl.obolibrary.org/obo/DOID_0050794)                                                          |
| `MIM:PS300352`  |              1 | [DOID:0050798](http://purl.obolibrary.org/obo/DOID_0050798)                                                          |
| `MIM:PS236730`  |              1 | [DOID:0050816](http://purl.obolibrary.org/obo/DOID_0050816)                                                          |
| `MIM:PS233400`  |              1 | [DOID:0050857](http://purl.obolibrary.org/obo/DOID_0050857)                                                          |
| `MIM:PS260370`  |              1 | [DOID:0050877](http://purl.obolibrary.org/obo/DOID_0050877)                                                          |
| `MIM:PS167320`  |              1 | [DOID:0050881](http://purl.obolibrary.org/obo/DOID_0050881)                                                          |
| `MIM:PS107480`  |              1 | [DOID:0050887](http://purl.obolibrary.org/obo/DOID_0050887)                                                          |
| `MIM:PS213200`  |              1 | [DOID:0050950](http://purl.obolibrary.org/obo/DOID_0050950)                                                          |
| `MIM:PS108600`  |              1 | [DOID:0050952](http://purl.obolibrary.org/obo/DOID_0050952)                                                          |
| `MIM:PS224050`  |              1 | [DOID:0050997](http://purl.obolibrary.org/obo/DOID_0050997)                                                          |
| `MIM:PS619720`  |              1 | [DOID:0051010](http://purl.obolibrary.org/obo/DOID_0051010)                                                          |
| `MIM:PS169500`  |              1 | [DOID:0051015](http://purl.obolibrary.org/obo/DOID_0051015)                                                          |
| `MIM:PS162000`  |              1 | [DOID:0060062](http://purl.obolibrary.org/obo/DOID_0060062)                                                          |
| `MIM:PS601764`  |              1 | [DOID:0060169](http://purl.obolibrary.org/obo/DOID_0060169)                                                          |
| `MIM:PS604233`  |              1 | [DOID:0060170](http://purl.obolibrary.org/obo/DOID_0060170)                                                          |
| `MIM:PS607631`  |              1 | [DOID:0060172](http://purl.obolibrary.org/obo/DOID_0060172)                                                          |
| `MIM:PS141500`  |              1 | [DOID:0060178](http://purl.obolibrary.org/obo/DOID_0060178)                                                          |
| `MIM:PS257920`  |              1 | [DOID:0060225](http://purl.obolibrary.org/obo/DOID_0060225)                                                          |
| `MIM:PS100300`  |              1 | [DOID:0060227](http://purl.obolibrary.org/obo/DOID_0060227)                                                          |
| `MIM:PS105800`  |              1 | [DOID:0060228](http://purl.obolibrary.org/obo/DOID_0060228)                                                          |
| `MIM:PS243310`  |              1 | [DOID:0060229](http://purl.obolibrary.org/obo/DOID_0060229)                                                          |
| `MIM:PS213600`  |              1 | [DOID:0060230](http://purl.obolibrary.org/obo/DOID_0060230)                                                          |
| `MIM:PS259450`  |              1 | [DOID:0060231](http://purl.obolibrary.org/obo/DOID_0060231)                                                          |
| `MIM:PS115150`  |              1 | [DOID:0060233](http://purl.obolibrary.org/obo/DOID_0060233)                                                          |
| `MIM:PS201000`  |              1 | [DOID:0060234](http://purl.obolibrary.org/obo/DOID_0060234)                                                          |
| `MIM:PS278300`  |              1 | [DOID:0060236](http://purl.obolibrary.org/obo/DOID_0060236)                                                          |
| `MIM:PS600118`  |              1 | [DOID:0060237](http://purl.obolibrary.org/obo/DOID_0060237)                                                          |
| `MIM:PS601390`  |              1 | [DOID:0060238](http://purl.obolibrary.org/obo/DOID_0060238)                                                          |
| `MIM:PS600630`  |              1 | [DOID:0060240](http://purl.obolibrary.org/obo/DOID_0060240)                                                          |
| `MIM:PS273750`  |              1 | [DOID:0060241](http://purl.obolibrary.org/obo/DOID_0060241)                                                          |
| `MIM:PS184450`  |              1 | [DOID:0060243](http://purl.obolibrary.org/obo/DOID_0060243)                                                          |
| `MIM:PS606711`  |              1 | [DOID:0060244](http://purl.obolibrary.org/obo/DOID_0060244)                                                          |
| `MIM:PS607326`  |              1 | [DOID:0060247](http://purl.obolibrary.org/obo/DOID_0060247)                                                          |
| `MIM:PS269500`  |              1 | [DOID:0060251](http://purl.obolibrary.org/obo/DOID_0060251)                                                          |
| `MIM:PS268310`  |              1 | [DOID:0060254](http://purl.obolibrary.org/obo/DOID_0060254)                                                          |
| `MIM:PS179850`  |              1 | [DOID:0060256](http://purl.obolibrary.org/obo/DOID_0060256)                                                          |
| `MIM:PS208540`  |              1 | [DOID:0060259](http://purl.obolibrary.org/obo/DOID_0060259)                                                          |
| `MIM:PS600803`  |              1 | [DOID:0060262](http://purl.obolibrary.org/obo/DOID_0060262)                                                          |
| `MIM:PS607596`  |              1 | [DOID:0060264](http://purl.obolibrary.org/obo/DOID_0060264)                                                          |
| `MIM:PS610489`  |              1 | [DOID:0060280](http://purl.obolibrary.org/obo/DOID_0060280)                                                          |
| `MIM:PS132100`  |              1 | [DOID:0060281](http://purl.obolibrary.org/obo/DOID_0060281)                                                          |
| `MIM:PS221900`  |              1 | [DOID:0060282](http://purl.obolibrary.org/obo/DOID_0060282)                                                          |
| `MIM:PS270300`  |              1 | [DOID:0060283](http://purl.obolibrary.org/obo/DOID_0060283)                                                          |
| `MIM:PS300818`  |              1 | [DOID:0060284](http://purl.obolibrary.org/obo/DOID_0060284)                                                          |
| `MIM:PS168500`  |              1 | [DOID:0060285](http://purl.obolibrary.org/obo/DOID_0060285)                                                          |
| `MIM:PS609060`  |              1 | [DOID:0060286](http://purl.obolibrary.org/obo/DOID_0060286)                                                          |
| `MIM:PS121400`  |              1 | [DOID:0060287](http://purl.obolibrary.org/obo/DOID_0060287)                                                          |
| `MIM:PS258315`  |              1 | [DOID:0060288](http://purl.obolibrary.org/obo/DOID_0060288)                                                          |
| `MIM:PS272430`  |              1 | [DOID:0060294](http://purl.obolibrary.org/obo/DOID_0060294)                                                          |
| `MIM:PS127500`  |              1 | [DOID:0060304](http://purl.obolibrary.org/obo/DOID_0060304)                                                          |
| `MIM:PS224690`  |              1 | [DOID:0060306](http://purl.obolibrary.org/obo/DOID_0060306)                                                          |
| `MIM:PS156200`  |              1 | [DOID:0060307](http://purl.obolibrary.org/obo/DOID_0060307)                                                          |
| `MIM:PS249500`  |              1 | [DOID:0060308](http://purl.obolibrary.org/obo/DOID_0060308)                                                          |
| `MIM:PS309510`  |              1 | [DOID:0060309](http://purl.obolibrary.org/obo/DOID_0060309)                                                          |
| `MIM:PS250950`  |              1 | [DOID:0060336](http://purl.obolibrary.org/obo/DOID_0060336)                                                          |
| `MIM:PS235510`  |              1 | [DOID:0060366](http://purl.obolibrary.org/obo/DOID_0060366)                                                          |
| `MIM:PS610448`  |              1 | [DOID:0060386](http://purl.obolibrary.org/obo/DOID_0060386)                                                          |
| `MIM:PS112240`  |              1 | [DOID:0060438](http://purl.obolibrary.org/obo/DOID_0060438)                                                          |
| `MIM:PS122100`  |              1 | [DOID:0060451](http://purl.obolibrary.org/obo/DOID_0060451)                                                          |
| `MIM:PS122000`  |              1 | [DOID:0060457](http://purl.obolibrary.org/obo/DOID_0060457)                                                          |
| `MIM:PS251450`  |              1 | [DOID:0060462](http://purl.obolibrary.org/obo/DOID_0060462)                                                          |
| `MIM:PS164280`  |              1 | [DOID:0060464](http://purl.obolibrary.org/obo/DOID_0060464)                                                          |
| `MIM:PS228520`  |              1 | [DOID:0060465](http://purl.obolibrary.org/obo/DOID_0060465)                                                          |
| `MIM:PS135300`  |              1 | [DOID:0060466](http://purl.obolibrary.org/obo/DOID_0060466)                                                          |
| `MIM:PS147920`  |              1 | [DOID:0060473](http://purl.obolibrary.org/obo/DOID_0060473)                                                          |
| `MIM:PS260400`  |              1 | [DOID:0060479](http://purl.obolibrary.org/obo/DOID_0060479)                                                          |
| `MIM:PS604169`  |              1 | [DOID:0060480](http://purl.obolibrary.org/obo/DOID_0060480)                                                          |
| `MIM:PS252011`  |              1 | [DOID:0060537](http://purl.obolibrary.org/obo/DOID_0060537)                                                          |
| `MIM:PS253310`  |              1 | [DOID:0060558](http://purl.obolibrary.org/obo/DOID_0060558)                                                          |
| `MIM:PS220210`  |              1 | [DOID:0060565](http://purl.obolibrary.org/obo/DOID_0060565)                                                          |
| `MIM:PS249210`  |              1 | [DOID:0060610](http://purl.obolibrary.org/obo/DOID_0060610)                                                          |
| `MIM:PS605552`  |              1 | [DOID:0060611](http://purl.obolibrary.org/obo/DOID_0060611)                                                          |
| `MIM:PS606176`  |              1 | [DOID:0060639](http://purl.obolibrary.org/obo/DOID_0060639)                                                          |
| `MIM:PS609628`  |              1 | [DOID:0060645](http://purl.obolibrary.org/obo/DOID_0060645)                                                          |
| `MIM:PS107250`  |              1 | [DOID:0060648](http://purl.obolibrary.org/obo/DOID_0060648)                                                          |
| `MIM:PS242300`  |              1 | [DOID:0060655](http://purl.obolibrary.org/obo/DOID_0060655)                                                          |
| `MIM:PS206500`  |              1 | [DOID:0060668](http://purl.obolibrary.org/obo/DOID_0060668)                                                          |
| `MIM:PS116860`  |              1 | [DOID:0060669](http://purl.obolibrary.org/obo/DOID_0060669)                                                          |
| `MIM:PS604772`  |              1 | [DOID:0060674](http://purl.obolibrary.org/obo/DOID_0060674)                                                          |
| `MIM:PS600513`  |              1 | [DOID:0060681](http://purl.obolibrary.org/obo/DOID_0060681)                                                          |
| `MIM:PS149400`  |              1 | [DOID:0060695](http://purl.obolibrary.org/obo/DOID_0060695)                                                          |
| `MIM:PS145980`  |              1 | [DOID:0060699](http://purl.obolibrary.org/obo/DOID_0060699)                                                          |
| `MIM:PS308240`  |              1 | [DOID:0060704](http://purl.obolibrary.org/obo/DOID_0060704)                                                          |
| `MIM:PS209880`  |              1 | [DOID:0060731](http://purl.obolibrary.org/obo/DOID_0060731)                                                          |
| `MIM:PS275210`  |              1 | [DOID:0060762](http://purl.obolibrary.org/obo/DOID_0060762)                                                          |
| `MIM:PS214700`  |              1 | [DOID:0060774](http://purl.obolibrary.org/obo/DOID_0060774)                                                          |
| `MIM:PS312080`  |              1 | [DOID:0060786](http://purl.obolibrary.org/obo/DOID_0060786)                                                          |
| `MIM:PS314580`  |              1 | [DOID:0060815](http://purl.obolibrary.org/obo/DOID_0060815)                                                          |
| `MIM:PS214450`  |              1 | [DOID:0060831](http://purl.obolibrary.org/obo/DOID_0060831)                                                          |
| `MIM:PS169150`  |              1 | [DOID:0060863](http://purl.obolibrary.org/obo/DOID_0060863)                                                          |
| `MIM:PS603896`  |              1 | [DOID:0060868](http://purl.obolibrary.org/obo/DOID_0060868)                                                          |
| `MIM:PS262400`  |              1 | [DOID:0060870](http://purl.obolibrary.org/obo/DOID_0060870)                                                          |
| `MIM:PS602014`  |              1 | [DOID:0060879](http://purl.obolibrary.org/obo/DOID_0060879)                                                          |
| `MIM:PS153600`  |              1 | [DOID:0060901](http://purl.obolibrary.org/obo/DOID_0060901)                                                          |
| `MIM:PS256040`  |              1 | [DOID:0060913](http://purl.obolibrary.org/obo/DOID_0060913)                                                          |
| `MIM:PS142700`  |              1 | [DOID:0060930](http://purl.obolibrary.org/obo/DOID_0060930)                                                          |
| `MIM:PS615273`  |              1 | [DOID:0060991](http://purl.obolibrary.org/obo/DOID_0060991)                                                          |
| `MIM:PS254130`  |              1 | [DOID:0070198](http://purl.obolibrary.org/obo/DOID_0070198)                                                          |
| `MIM:PS211600`  |              1 | [DOID:0070221](http://purl.obolibrary.org/obo/DOID_0070221)                                                          |
| `MIM:PS243300`  |              1 | [DOID:0070230](http://purl.obolibrary.org/obo/DOID_0070230)                                                          |
| `MIM:PS251200`  |              1 | [DOID:0070297](http://purl.obolibrary.org/obo/DOID_0070297)                                                          |
| `MIM:PS603041`  |              1 | [DOID:0070329](http://purl.obolibrary.org/obo/DOID_0070329)                                                          |
| `MIM:PS605711`  |              1 | [DOID:0070330](http://purl.obolibrary.org/obo/DOID_0070330)                                                          |
| `MIM:PS158600`  |              1 | [DOID:0070348](http://purl.obolibrary.org/obo/DOID_0070348)                                                          |
| `MIM:PS239300`  |              1 | [DOID:0070431](http://purl.obolibrary.org/obo/DOID_0070431)                                                          |
| `MIM:PS136550`  |              1 | [DOID:0070438](http://purl.obolibrary.org/obo/DOID_0070438)                                                          |
| `MIM:PS616901`  |              1 | [DOID:0070476](http://purl.obolibrary.org/obo/DOID_0070476)                                                          |
| `MIM:PS613135`  |              1 | [DOID:0070487](http://purl.obolibrary.org/obo/DOID_0070487)                                                          |
| `MIM:PS606777`  |              1 | [DOID:0070560](http://purl.obolibrary.org/obo/DOID_0070560)                                                          |
| `MIM:PS609322`  |              1 | [DOID:0070617](http://purl.obolibrary.org/obo/DOID_0070617)                                                          |
| `MIM:PS184840`  |              1 | [DOID:0080026](http://purl.obolibrary.org/obo/DOID_0080026)                                                          |
| `MIM:PS123000`  |              1 | [DOID:0080033](http://purl.obolibrary.org/obo/DOID_0080033)                                                          |
| `MIM:PS200600`  |              1 | [DOID:0080043](http://purl.obolibrary.org/obo/DOID_0080043)                                                          |
| `MIM:PS108300`  |              1 | [DOID:0080046](http://purl.obolibrary.org/obo/DOID_0080046)                                                          |
| `MIM:PS602875`  |              1 | [DOID:0080049](http://purl.obolibrary.org/obo/DOID_0080049)                                                          |
| `MIM:PS600462`  |              1 | [DOID:0080099](http://purl.obolibrary.org/obo/DOID_0080099)                                                          |
| `MIM:PS228550`  |              1 | [DOID:0080109](http://purl.obolibrary.org/obo/DOID_0080109)                                                          |
| `MIM:PS178110`  |              1 | [DOID:0080110](http://purl.obolibrary.org/obo/DOID_0080110)                                                          |
| `MIM:PS135700`  |              1 | [DOID:0080143](http://purl.obolibrary.org/obo/DOID_0080143)                                                          |
| `MIM:PS617099`  |              1 | [DOID:0080163](http://purl.obolibrary.org/obo/DOID_0080163)                                                          |
| `MIM:PS610460`  |              1 | [DOID:0080172](http://purl.obolibrary.org/obo/DOID_0080172)                                                          |
| `MIM:PS254940`  |              1 | [DOID:0080194](http://purl.obolibrary.org/obo/DOID_0080194)                                                          |
| `MIM:PS610805`  |              1 | [DOID:0080205](http://purl.obolibrary.org/obo/DOID_0080205)                                                          |
| `MIM:PS278000`  |              1 | [DOID:0080217](http://purl.obolibrary.org/obo/DOID_0080217)                                                          |
| `MIM:PS144200`  |              1 | [DOID:0080223](http://purl.obolibrary.org/obo/DOID_0080223)                                                          |
| `MIM:PS601419`  |              1 | [DOID:0080307](http://purl.obolibrary.org/obo/DOID_0080307)                                                          |
| `MIM:PS604004`  |              1 | [DOID:0080315](http://purl.obolibrary.org/obo/DOID_0080315)                                                          |
| `MIM:PS173900`  |              1 | [DOID:0080322](http://purl.obolibrary.org/obo/DOID_0080322)                                                          |
| `MIM:PS192600`  |              1 | [DOID:0080326](http://purl.obolibrary.org/obo/DOID_0080326)                                                          |
| `MIM:PS109730`  |              1 | [DOID:0080332](http://purl.obolibrary.org/obo/DOID_0080332)                                                          |
| `MIM:PS119580`  |              1 | [DOID:0080344](http://purl.obolibrary.org/obo/DOID_0080344)                                                          |
| `MIM:PS214100`  |              1 | [DOID:0080377](http://purl.obolibrary.org/obo/DOID_0080377)                                                          |
| `MIM:PS256550`  |              1 | [DOID:0080488](http://purl.obolibrary.org/obo/DOID_0080488)                                                          |
| `MIM:PS614080`  |              1 | [DOID:0080503](http://purl.obolibrary.org/obo/DOID_0080503)                                                          |
| `MIM:PS613280`  |              1 | [DOID:0080535](http://purl.obolibrary.org/obo/DOID_0080535)                                                          |
| `MIM:PS308230`  |              1 | [DOID:0080544](http://purl.obolibrary.org/obo/DOID_0080544)                                                          |
| `MIM:PS147060`  |              1 | [DOID:0080545](http://purl.obolibrary.org/obo/DOID_0080545)                                                          |
| `MIM:PS610253`  |              1 | [DOID:0080597](http://purl.obolibrary.org/obo/DOID_0080597)                                                          |
| `MIM:PS202200`  |              1 | [DOID:0080620](http://purl.obolibrary.org/obo/DOID_0080620)                                                          |
| `MIM:PS203650`  |              1 | [DOID:0080627](http://purl.obolibrary.org/obo/DOID_0080627)                                                          |
| `MIM:PS600165`  |              1 | [DOID:0080634](http://purl.obolibrary.org/obo/DOID_0080634)                                                          |
| `MIM:PS309800`  |              1 | [DOID:0080636](http://purl.obolibrary.org/obo/DOID_0080636)                                                          |
| `MIM:PS167030`  |              1 | [DOID:0080652](http://purl.obolibrary.org/obo/DOID_0080652)                                                          |
| `MIM:PS612286`  |              1 | [DOID:0080655](http://purl.obolibrary.org/obo/DOID_0080655)                                                          |
| `MIM:PS161050`  |              1 | [DOID:0080683](http://purl.obolibrary.org/obo/DOID_0080683)                                                          |
| `MIM:PS257300`  |              1 | [DOID:0080688](http://purl.obolibrary.org/obo/DOID_0080688)                                                          |
| `MIM:PS607721`  |              1 | [DOID:0080691](http://purl.obolibrary.org/obo/DOID_0080691)                                                          |
| `MIM:PS251300`  |              1 | [DOID:0080694](http://purl.obolibrary.org/obo/DOID_0080694)                                                          |
| `MIM:PS615438`  |              1 | [DOID:0080716](http://purl.obolibrary.org/obo/DOID_0080716)                                                          |
| `MIM:PS127000`  |              1 | [DOID:0080724](http://purl.obolibrary.org/obo/DOID_0080724)                                                          |
| `MIM:PS214150`  |              1 | [DOID:0080910](http://purl.obolibrary.org/obo/DOID_0080910)                                                          |
| `MIM:PS607095`  |              1 | [DOID:0080942](http://purl.obolibrary.org/obo/DOID_0080942)                                                          |
| `MIM:PS617468`  |              1 | [DOID:0080954](http://purl.obolibrary.org/obo/DOID_0080954)                                                          |
| `MIM:PS136760`  |              1 | [DOID:0081044](http://purl.obolibrary.org/obo/DOID_0081044)                                                          |
| `MIM:PS213980`  |              1 | [DOID:0081072](http://purl.obolibrary.org/obo/DOID_0081072)                                                          |
| `MIM:PS145420`  |              1 | [DOID:0081073](http://purl.obolibrary.org/obo/DOID_0081073)                                                          |
| `MIM:PS300291`  |              1 | [DOID:0081077](http://purl.obolibrary.org/obo/DOID_0081077)                                                          |
| `MIM:PS613339`  |              1 | [DOID:0081104](http://purl.obolibrary.org/obo/DOID_0081104)                                                          |
| `MIM:PS164310`  |              1 | [DOID:0081296](http://purl.obolibrary.org/obo/DOID_0081296)                                                          |
| `MIM:PS176670`  |              1 | [DOID:0081332](http://purl.obolibrary.org/obo/DOID_0081332)                                                          |
| `MIM:PS117000`  |              1 | [DOID:0081337](http://purl.obolibrary.org/obo/DOID_0081337)                                                          |
| `MIM:PS149730`  |              1 | [DOID:0081370](http://purl.obolibrary.org/obo/DOID_0081370)                                                          |
| `MIM:PS604364`  |              1 | [DOID:0081420](http://purl.obolibrary.org/obo/DOID_0081420)                                                          |
| `MIM:PS219000`  |              1 | [DOID:0090001](http://purl.obolibrary.org/obo/DOID_0090001)                                                          |
| `MIM:PS242860`  |              1 | [DOID:0090007](http://purl.obolibrary.org/obo/DOID_0090007)                                                          |
| `MIM:PS210250`  |              1 | [DOID:0090019](http://purl.obolibrary.org/obo/DOID_0090019)                                                          |
| `MIM:PS183600`  |              1 | [DOID:0090020](http://purl.obolibrary.org/obo/DOID_0090020)                                                          |
| `MIM:PS120100`  |              1 | [DOID:0090061](http://purl.obolibrary.org/obo/DOID_0090061)                                                          |
| `MIM:PS147950`  |              1 | [DOID:0090070](http://purl.obolibrary.org/obo/DOID_0090070)                                                          |
| `MIM:PS601198`  |              1 | [DOID:0090109](http://purl.obolibrary.org/obo/DOID_0090109)                                                          |
| `MIM:PS614039`  |              1 | [DOID:0090131](http://purl.obolibrary.org/obo/DOID_0090131)                                                          |
| `MIM:PS604931`  |              1 | [DOID:0090139](http://purl.obolibrary.org/obo/DOID_0090139)                                                          |
| `MIM:PS603511`  |              1 | [DOID:0110273](http://purl.obolibrary.org/obo/DOID_0110273)                                                          |
| `MIM:PS253600`  |              1 | [DOID:0110274](http://purl.obolibrary.org/obo/DOID_0110274)                                                          |
| `MIM:PS234200`  |              1 | [DOID:0110734](http://purl.obolibrary.org/obo/DOID_0110734)                                                          |
| `MIM:PS113900`  |              1 | [DOID:0111073](http://purl.obolibrary.org/obo/DOID_0111073)                                                          |
| `MIM:PS124000`  |              1 | [DOID:0111139](http://purl.obolibrary.org/obo/DOID_0111139)                                                          |
| `MIM:PS604273`  |              1 | [DOID:0111143](http://purl.obolibrary.org/obo/DOID_0111143)                                                          |
| `MIM:PS157600`  |              1 | [DOID:0111153](http://purl.obolibrary.org/obo/DOID_0111153)                                                          |
| `MIM:PS252150`  |              1 | [DOID:0111165](http://purl.obolibrary.org/obo/DOID_0111165)                                                          |
| `MIM:PS604320`  |              1 | [DOID:0111197](http://purl.obolibrary.org/obo/DOID_0111197)                                                          |
| `MIM:PS182960`  |              1 | [DOID:0111198](http://purl.obolibrary.org/obo/DOID_0111198)                                                          |
| `MIM:PS236670`  |              1 | [DOID:0111229](http://purl.obolibrary.org/obo/DOID_0111229)                                                          |
| `MIM:PS609015`  |              1 | [DOID:0111277](http://purl.obolibrary.org/obo/DOID_0111277)                                                          |
| `MIM:PS121210`  |              1 | [DOID:0111297](http://purl.obolibrary.org/obo/DOID_0111297)                                                          |
| `MIM:PS141200`  |              1 | [DOID:0111365](http://purl.obolibrary.org/obo/DOID_0111365)                                                          |
| `MIM:PS208150`  |              1 | [DOID:0111375](http://purl.obolibrary.org/obo/DOID_0111375)                                                          |
| `MIM:PS146200`  |              1 | [DOID:0111387](http://purl.obolibrary.org/obo/DOID_0111387)                                                          |
| `MIM:PS222470`  |              1 | [DOID:0111414](http://purl.obolibrary.org/obo/DOID_0111414)                                                          |
| `MIM:PS219080`  |              1 | [DOID:0111622](http://purl.obolibrary.org/obo/DOID_0111622)                                                          |
| `MIM:PS601228`  |              1 | [DOID:0111684](http://purl.obolibrary.org/obo/DOID_0111684)                                                          |
| `MIM:PS601068`  |              1 | [DOID:0111689](http://purl.obolibrary.org/obo/DOID_0111689)                                                          |
| `MIM:PS231050`  |              1 | [DOID:0111724](http://purl.obolibrary.org/obo/DOID_0111724)                                                          |
| `MIM:PS615040`  |              1 | [DOID:0111728](http://purl.obolibrary.org/obo/DOID_0111728)                                                          |
| `MIM:PS400043`  |              1 | [DOID:0111757](http://purl.obolibrary.org/obo/DOID_0111757)                                                          |
| `MIM:PS305620`  |              1 | [DOID:0111785](http://purl.obolibrary.org/obo/DOID_0111785)                                                          |
| `MIM:PS277180`  |              1 | [DOID:0111862](http://purl.obolibrary.org/obo/DOID_0111862)                                                          |
| `MIM:PS601675`  |              1 | [DOID:0111866](http://purl.obolibrary.org/obo/DOID_0111866)                                                          |
| `MIM:PS309801`  |              1 | [DOID:0111875](http://purl.obolibrary.org/obo/DOID_0111875)                                                          |
| `MIM:PS258150`  |              1 | [DOID:0111910](http://purl.obolibrary.org/obo/DOID_0111910)                                                          |
| `MIM:PS614594`  |              1 | [DOID:0112011](http://purl.obolibrary.org/obo/DOID_0112011)                                                          |
| `MIM:PS252010`  |              1 | [DOID:0112065](http://purl.obolibrary.org/obo/DOID_0112065)                                                          |
| `MIM:PS276300`  |              1 | [DOID:0112182](http://purl.obolibrary.org/obo/DOID_0112182)                                                          |
| `MIM:PS274400`  |              1 | [DOID:0112183](http://purl.obolibrary.org/obo/DOID_0112183)                                                          |
| `MIM:PS273395`  |              1 | [DOID:0112191](http://purl.obolibrary.org/obo/DOID_0112191)                                                          |
| `MIM:PS271640`  |              1 | [DOID:0112197](http://purl.obolibrary.org/obo/DOID_0112197)                                                          |
| `MIM:PS308350`  |              1 | [DOID:0112202](http://purl.obolibrary.org/obo/DOID_0112202)                                                          |
| `MIM:PS156610`  |              1 | [DOID:0112241](http://purl.obolibrary.org/obo/DOID_0112241)                                                          |
| `MIM:PS184255`  |              1 | [DOID:0112295](http://purl.obolibrary.org/obo/DOID_0112295)                                                          |
| `MIM:PS175780`  |              1 | [DOID:0112313](http://purl.obolibrary.org/obo/DOID_0112313)                                                          |
| `MIM:PS613155`  |              1 | [DOID:0112375](http://purl.obolibrary.org/obo/DOID_0112375)                                                          |
| `MIM:PS227220`  |              1 | [DOID:10123](http://purl.obolibrary.org/obo/DOID_10123)                                                              |
| `MIM:PS148300`  |              1 | [DOID:10126](http://purl.obolibrary.org/obo/DOID_10126)                                                              |
| `MIM:PS608805`  |              1 | [DOID:10159](http://purl.obolibrary.org/obo/DOID_10159)                                                              |
| `MIM:PS118100`  |              1 | [DOID:10426](http://purl.obolibrary.org/obo/DOID_10426)                                                              |
| `MIM:PS142623`  |              1 | [DOID:10487](http://purl.obolibrary.org/obo/DOID_10487)                                                              |
| `MIM:PS221820`  |              1 | [DOID:10579](http://purl.obolibrary.org/obo/DOID_10579)                                                              |
| `MIM:PS268000`  |              1 | [DOID:10584](http://purl.obolibrary.org/obo/DOID_10584)                                                              |
| `MIM:PS189800`  |              1 | [DOID:10591](http://purl.obolibrary.org/obo/DOID_10591)                                                              |
| `MIM:PS118220`  |              1 | [DOID:10595](http://purl.obolibrary.org/obo/DOID_10595)                                                              |
| `MIM:PS212750`  |              1 | [DOID:10608](http://purl.obolibrary.org/obo/DOID_10608)                                                              |
| `MIM:PS134600`  |              1 | [DOID:1062](http://purl.obolibrary.org/obo/DOID_1062)                                                                |
| `MIM:PS251600`  |              1 | [DOID:10629](http://purl.obolibrary.org/obo/DOID_10629)                                                              |
| `MIM:PS617068`  |              1 | [DOID:10762](http://purl.obolibrary.org/obo/DOID_10762)                                                              |
| `MIM:PS133100`  |              1 | [DOID:10780](http://purl.obolibrary.org/obo/DOID_10780)                                                              |
| `MIM:PS603075`  |              1 | [DOID:10871](http://purl.obolibrary.org/obo/DOID_10871)                                                              |
| `MIM:PS300633`  |              1 | [DOID:10892](http://purl.obolibrary.org/obo/DOID_10892)                                                              |
| `MIM:PS236600`  |              1 | [DOID:10908](http://purl.obolibrary.org/obo/DOID_10908)                                                              |
| `MIM:PS612900`  |              1 | [DOID:10970](http://purl.obolibrary.org/obo/DOID_10970)                                                              |
| `MIM:PS301050`  |              1 | [DOID:10983](http://purl.obolibrary.org/obo/DOID_10983)                                                              |
| `MIM:PS136800`  |              1 | [DOID:11555](http://purl.obolibrary.org/obo/DOID_11555)                                                              |
| `MIM:PS603933`  |              1 | [DOID:11713](http://purl.obolibrary.org/obo/DOID_11713)                                                              |
| `MIM:PS160500`  |              1 | [DOID:11720](http://purl.obolibrary.org/obo/DOID_11720)                                                              |
| `MIM:PS609308`  |              1 | [DOID:11724](http://purl.obolibrary.org/obo/DOID_11724)                                                              |
| `MIM:PS122470`  |              1 | [DOID:11725](http://purl.obolibrary.org/obo/DOID_11725)                                                              |
| `MIM:PS310300`  |              1 | [DOID:11726](http://purl.obolibrary.org/obo/DOID_11726)                                                              |
| `MIM:PS158900`  |              1 | [DOID:11727](http://purl.obolibrary.org/obo/DOID_11727)                                                              |
| `MIM:PS160700`  |              1 | [DOID:11830](http://purl.obolibrary.org/obo/DOID_11830)                                                              |
| `MIM:PS265120`  |              1 | [DOID:12120](http://purl.obolibrary.org/obo/DOID_12120)                                                              |
| `MIM:PS115430`  |              1 | [DOID:12169](http://purl.obolibrary.org/obo/DOID_12169)                                                              |
| `MIM:PS607594`  |              1 | [DOID:12177](http://purl.obolibrary.org/obo/DOID_12177)                                                              |
| `MIM:PS166800`  |              1 | [DOID:12185](http://purl.obolibrary.org/obo/DOID_12185)                                                              |
| `MIM:PS109720`  |              1 | [DOID:12236](http://purl.obolibrary.org/obo/DOID_12236)                                                              |
| `MIM:PS106210`  |              1 | [DOID:12271](http://purl.obolibrary.org/obo/DOID_12271)                                                              |
| `MIM:PS166200`  |              1 | [DOID:12347](http://purl.obolibrary.org/obo/DOID_12347)                                                              |
| `MIM:PS126800`  |              1 | [DOID:12557](http://purl.obolibrary.org/obo/DOID_12557)                                                              |
| `MIM:PS157640`  |              1 | [DOID:12558](http://purl.obolibrary.org/obo/DOID_12558)                                                              |
| `MIM:PS143880`  |              1 | [DOID:12678](http://purl.obolibrary.org/obo/DOID_12678)                                                              |
| `MIM:PS187300`  |              1 | [DOID:1270](http://purl.obolibrary.org/obo/DOID_1270)                                                                |
| `MIM:PS256100`  |              1 | [DOID:12712](http://purl.obolibrary.org/obo/DOID_12712)                                                              |
| `MIM:PS132400`  |              1 | [DOID:12721](http://purl.obolibrary.org/obo/DOID_12721)                                                              |
| `MIM:PS607014`  |              1 | [DOID:12798](http://purl.obolibrary.org/obo/DOID_12798)                                                              |
| `MIM:PS209850`  |              1 | [DOID:12849](http://purl.obolibrary.org/obo/DOID_12849)                                                              |
| `MIM:PS115200`  |              1 | [DOID:12930](http://purl.obolibrary.org/obo/DOID_12930)                                                              |
| `MIM:PS252350`  |              1 | [DOID:13099](http://purl.obolibrary.org/obo/DOID_13099)                                                              |
| `MIM:PS603278`  |              1 | [DOID:1312](http://purl.obolibrary.org/obo/DOID_1312)                                                                |
| `MIM:PS177000`  |              1 | [DOID:13270](http://purl.obolibrary.org/obo/DOID_13270)                                                              |
| `MIM:PS256450`  |              1 | [DOID:13317](http://purl.obolibrary.org/obo/DOID_13317)                                                              |
| `MIM:PS130000`  |              1 | [DOID:13359](http://purl.obolibrary.org/obo/DOID_13359)                                                              |
| `MIM:PS224120`  |              1 | [DOID:1338](http://purl.obolibrary.org/obo/DOID_1338)                                                                |
| `MIM:PS105650`  |              1 | [DOID:1339](http://purl.obolibrary.org/obo/DOID_1339)                                                                |
| `MIM:PS191100`  |              1 | [DOID:13515](http://purl.obolibrary.org/obo/DOID_13515)                                                              |
| `MIM:PS259700`  |              1 | [DOID:13533](http://purl.obolibrary.org/obo/DOID_13533)                                                              |
| `MIM:PS607634`  |              1 | [DOID:13533](http://purl.obolibrary.org/obo/DOID_13533)                                                              |
| `MIM:PS145000`  |              1 | [DOID:13543](http://purl.obolibrary.org/obo/DOID_13543)                                                              |
| `MIM:PS227650`  |              1 | [DOID:13636](http://purl.obolibrary.org/obo/DOID_13636)                                                              |
| `MIM:PS226400`  |              1 | [DOID:13777](http://purl.obolibrary.org/obo/DOID_13777)                                                              |
| `MIM:PS143890`  |              1 | [DOID:13810](http://purl.obolibrary.org/obo/DOID_13810)                                                              |
| `MIM:PS607411`  |              1 | [DOID:13832](http://purl.obolibrary.org/obo/DOID_13832)                                                              |
| `MIM:PS608567`  |              1 | [DOID:13884](http://purl.obolibrary.org/obo/DOID_13884)                                                              |
| `MIM:PS125310`  |              1 | [DOID:13945](http://purl.obolibrary.org/obo/DOID_13945)                                                              |
| `MIM:PS607086`  |              1 | [DOID:14004](http://purl.obolibrary.org/obo/DOID_14004)                                                              |
| `MIM:PS121200`  |              1 | [DOID:14264](http://purl.obolibrary.org/obo/DOID_14264)                                                              |
| `MIM:PS259100`  |              1 | [DOID:14283](http://purl.obolibrary.org/obo/DOID_14283)                                                              |
| `MIM:PS151100`  |              1 | [DOID:14291](http://purl.obolibrary.org/obo/DOID_14291)                                                              |
| `MIM:PS168600`  |              1 | [DOID:14330](http://purl.obolibrary.org/obo/DOID_14330)                                                              |
| `MIM:PS164400`  |              1 | [DOID:1441](http://purl.obolibrary.org/obo/DOID_1441)                                                                |
| `MIM:PS400044`  |              1 | [DOID:14448](http://purl.obolibrary.org/obo/DOID_14448)                                                              |
| `MIM:PS233300`  |              1 | [DOID:14450](http://purl.obolibrary.org/obo/DOID_14450)                                                              |
| `MIM:PS256730`  |              1 | [DOID:14503](http://purl.obolibrary.org/obo/DOID_14503)                                                              |
| `MIM:PS178600`  |              1 | [DOID:14557](http://purl.obolibrary.org/obo/DOID_14557)                                                              |
| `MIM:PS101800`  |              1 | [DOID:14669](http://purl.obolibrary.org/obo/DOID_14669)                                                              |
| `MIM:PS180860`  |              1 | [DOID:14681](http://purl.obolibrary.org/obo/DOID_14681)                                                              |
| `MIM:PS180500`  |              1 | [DOID:14686](http://purl.obolibrary.org/obo/DOID_14686)                                                              |
| `MIM:PS166780`  |              1 | [DOID:14702](http://purl.obolibrary.org/obo/DOID_14702)                                                              |
| `MIM:PS305450`  |              1 | [DOID:14711](http://purl.obolibrary.org/obo/DOID_14711)                                                              |
| `MIM:PS160150`  |              1 | [DOID:14717](http://purl.obolibrary.org/obo/DOID_14717)                                                              |
| `MIM:PS106100`  |              1 | [DOID:14735](http://purl.obolibrary.org/obo/DOID_14735)                                                              |
| `MIM:PS117550`  |              1 | [DOID:14748](http://purl.obolibrary.org/obo/DOID_14748)                                                              |
| `MIM:PS191830`  |              1 | [DOID:14766](http://purl.obolibrary.org/obo/DOID_14766)                                                              |
| `MIM:PS204000`  |              1 | [DOID:14791](http://purl.obolibrary.org/obo/DOID_14791)                                                              |
| `MIM:PS313900`  |              1 | [DOID:1588](http://purl.obolibrary.org/obo/DOID_1588)                                                                |
| `MIM:PS613112`  |              1 | [DOID:1588](http://purl.obolibrary.org/obo/DOID_1588)                                                                |
| `MIM:PS614429`  |              1 | [DOID:1657](http://purl.obolibrary.org/obo/DOID_1657)                                                                |
| `MIM:PS212093`  |              1 | [DOID:1682](http://purl.obolibrary.org/obo/DOID_1682)                                                                |
| `MIM:PS146590`  |              1 | [DOID:1697](http://purl.obolibrary.org/obo/DOID_1697)                                                                |
| `MIM:PS600131`  |              1 | [DOID:1825](http://purl.obolibrary.org/obo/DOID_1825)                                                                |
| `MIM:PS617290`  |              1 | [DOID:1826](http://purl.obolibrary.org/obo/DOID_1826)                                                                |
| `MIM:PS108800`  |              1 | [DOID:1882](http://purl.obolibrary.org/obo/DOID_1882)                                                                |
| `MIM:PS135900`  |              1 | [DOID:1925](http://purl.obolibrary.org/obo/DOID_1925)                                                                |
| `MIM:PS180849`  |              1 | [DOID:1933](http://purl.obolibrary.org/obo/DOID_1933)                                                                |
| `MIM:PS209900`  |              1 | [DOID:1935](http://purl.obolibrary.org/obo/DOID_1935)                                                                |
| `MIM:PS114580`  |              1 | [DOID:2058](http://purl.obolibrary.org/obo/DOID_2058)                                                                |
| `MIM:PS305100`  |              1 | [DOID:2121](http://purl.obolibrary.org/obo/DOID_2121)                                                                |
| `MIM:PS194070`  |              1 | [DOID:2154](http://purl.obolibrary.org/obo/DOID_2154)                                                                |
| `MIM:PS104500`  |              1 | [DOID:2187](http://purl.obolibrary.org/obo/DOID_2187)                                                                |
| `MIM:PS231200`  |              1 | [DOID:2218](http://purl.obolibrary.org/obo/DOID_2218)                                                                |
| `MIM:PS273800`  |              1 | [DOID:2219](http://purl.obolibrary.org/obo/DOID_2219)                                                                |
| `MIM:PS187950`  |              1 | [DOID:2228](http://purl.obolibrary.org/obo/DOID_2228)                                                                |
| `MIM:PS176400`  |              1 | [DOID:2277](http://purl.obolibrary.org/obo/DOID_2277)                                                                |
| `MIM:PS142690`  |              1 | [DOID:2280](http://purl.obolibrary.org/obo/DOID_2280)                                                                |
| `MIM:PS123100`  |              1 | [DOID:2340](http://purl.obolibrary.org/obo/DOID_2340)                                                                |
| `MIM:PS235200`  |              1 | [DOID:2352](http://purl.obolibrary.org/obo/DOID_2352)                                                                |
| `MIM:PS126200`  |              1 | [DOID:2377](http://purl.obolibrary.org/obo/DOID_2377)                                                                |
| `MIM:PS188050`  |              1 | [DOID:2452](http://purl.obolibrary.org/obo/DOID_2452)                                                                |
| `MIM:PS303350`  |              1 | [DOID:2476](http://purl.obolibrary.org/obo/DOID_2476)                                                                |
| `MIM:PS109400`  |              1 | [DOID:2512](http://purl.obolibrary.org/obo/DOID_2512)                                                                |
| `MIM:PS215100`  |              1 | [DOID:2580](http://purl.obolibrary.org/obo/DOID_2580)                                                                |
| `MIM:PS601495`  |              1 | [DOID:2583](http://purl.obolibrary.org/obo/DOID_2583)                                                                |
| `MIM:PS256300`  |              1 | [DOID:2590](http://purl.obolibrary.org/obo/DOID_2590)                                                                |
| `MIM:PS127550`  |              1 | [DOID:2729](http://purl.obolibrary.org/obo/DOID_2729)                                                                |
| `MIM:PS268400`  |              1 | [DOID:2732](http://purl.obolibrary.org/obo/DOID_2732)                                                                |
| `MIM:PS237450`  |              1 | [DOID:2741](http://purl.obolibrary.org/obo/DOID_2741)                                                                |
| `MIM:PS232200`  |              1 | [DOID:2747](http://purl.obolibrary.org/obo/DOID_2747)                                                                |
| `MIM:PS615895`  |              1 | [DOID:2747](http://purl.obolibrary.org/obo/DOID_2747)                                                                |
| `MIM:PS220400`  |              1 | [DOID:2842](http://purl.obolibrary.org/obo/DOID_2842)                                                                |
| `MIM:PS192500`  |              1 | [DOID:2843](http://purl.obolibrary.org/obo/DOID_2843)                                                                |
| `MIM:PS300908`  |              1 | [DOID:2861](http://purl.obolibrary.org/obo/DOID_2861)                                                                |
| `MIM:PS154500`  |              1 | [DOID:2908](http://purl.obolibrary.org/obo/DOID_2908)                                                                |
| `MIM:PS137950`  |              1 | [DOID:2920](http://purl.obolibrary.org/obo/DOID_2920)                                                                |
| `MIM:PS259900`  |              1 | [DOID:2977](http://purl.obolibrary.org/obo/DOID_2977)                                                                |
| `MIM:PS161950`  |              1 | [DOID:2986](http://purl.obolibrary.org/obo/DOID_2986)                                                                |
| `MIM:PS151623`  |              1 | [DOID:3012](http://purl.obolibrary.org/obo/DOID_3012)                                                                |
| `MIM:PS137800`  |              1 | [DOID:3070](http://purl.obolibrary.org/obo/DOID_3070)                                                                |
| `MIM:PS619611`  |              1 | [DOID:3082](http://purl.obolibrary.org/obo/DOID_3082)                                                                |
| `MIM:PS131100`  |              1 | [DOID:3125](http://purl.obolibrary.org/obo/DOID_3125)                                                                |
| `MIM:PS123700`  |              1 | [DOID:3144](http://purl.obolibrary.org/obo/DOID_3144)                                                                |
| `MIM:PS161800`  |              1 | [DOID:3191](http://purl.obolibrary.org/obo/DOID_3191)                                                                |
| `MIM:PS162091`  |              1 | [DOID:3204](http://purl.obolibrary.org/obo/DOID_3204)                                                                |
| `MIM:PS226650`  |              1 | [DOID:3209](http://purl.obolibrary.org/obo/DOID_3209)                                                                |
| `MIM:PS306400`  |              1 | [DOID:3265](http://purl.obolibrary.org/obo/DOID_3265)                                                                |
| `MIM:PS603165`  |              1 | [DOID:3310](http://purl.obolibrary.org/obo/DOID_3310)                                                                |
| `MIM:PS105400`  |              1 | [DOID:332](http://purl.obolibrary.org/obo/DOID_332)                                                                  |
| `MIM:PS600512`  |              1 | [DOID:3328](http://purl.obolibrary.org/obo/DOID_3328)                                                                |
| `MIM:PS163950`  |              1 | [DOID:3490](http://purl.obolibrary.org/obo/DOID_3490)                                                                |
| `MIM:PS254780`  |              1 | [DOID:3534](http://purl.obolibrary.org/obo/DOID_3534)                                                                |
| `MIM:PS231090`  |              1 | [DOID:3590](http://purl.obolibrary.org/obo/DOID_3590)                                                                |
| `MIM:PS601462`  |              1 | [DOID:3635](http://purl.obolibrary.org/obo/DOID_3635)                                                                |
| `MIM:PS610542`  |              1 | [DOID:3635](http://purl.obolibrary.org/obo/DOID_3635)                                                                |
| `MIM:PS312170`  |              1 | [DOID:3649](http://purl.obolibrary.org/obo/DOID_3649)                                                                |
| `MIM:PS203300`  |              1 | [DOID:3753](http://purl.obolibrary.org/obo/DOID_3753)                                                                |
| `MIM:PS220110`  |              1 | [DOID:3762](http://purl.obolibrary.org/obo/DOID_3762)                                                                |
| `MIM:PS175800`  |              1 | [DOID:3805](http://purl.obolibrary.org/obo/DOID_3805)                                                                |
| `MIM:PS142340`  |              1 | [DOID:3827](http://purl.obolibrary.org/obo/DOID_3827)                                                                |
| `MIM:PS102200`  |              1 | [DOID:3829](http://purl.obolibrary.org/obo/DOID_3829)                                                                |
| `MIM:PS120435`  |              1 | [DOID:3883](http://purl.obolibrary.org/obo/DOID_3883)                                                                |
| `MIM:PS188550`  |              1 | [DOID:3969](http://purl.obolibrary.org/obo/DOID_3969)                                                                |
| `MIM:PS115210`  |              1 | [DOID:397](http://purl.obolibrary.org/obo/DOID_397)                                                                  |
| `MIM:PS160565`  |              1 | [DOID:423](http://purl.obolibrary.org/obo/DOID_423)                                                                  |
| `MIM:PS601678`  |              1 | [DOID:445](http://purl.obolibrary.org/obo/DOID_445)                                                                  |
| `MIM:PS103900`  |              1 | [DOID:446](http://purl.obolibrary.org/obo/DOID_446)                                                                  |
| `MIM:PS145260`  |              1 | [DOID:4479](http://purl.obolibrary.org/obo/DOID_4479)                                                                |
| `MIM:PS177735`  |              1 | [DOID:4479](http://purl.obolibrary.org/obo/DOID_4479)                                                                |
| `MIM:PS160900`  |              1 | [DOID:450](http://purl.obolibrary.org/obo/DOID_450)                                                                  |
| `MIM:PS311200`  |              1 | [DOID:4501](http://purl.obolibrary.org/obo/DOID_4501)                                                                |
| `MIM:PS605389`  |              1 | [DOID:4535](http://purl.obolibrary.org/obo/DOID_4535)                                                                |
| `MIM:PS113800`  |              1 | [DOID:4603](http://purl.obolibrary.org/obo/DOID_4603)                                                                |
| `MIM:PS607602`  |              1 | [DOID:4603](http://purl.obolibrary.org/obo/DOID_4603)                                                                |
| `MIM:PS236100`  |              1 | [DOID:4621](http://purl.obolibrary.org/obo/DOID_4621)                                                                |
| `MIM:PS131760`  |              1 | [DOID:4644](http://purl.obolibrary.org/obo/DOID_4644)                                                                |
| `MIM:PS271930`  |              1 | [DOID:4751](http://purl.obolibrary.org/obo/DOID_4751)                                                                |
| `MIM:PS254770`  |              1 | [DOID:4890](http://purl.obolibrary.org/obo/DOID_4890)                                                                |
| `MIM:PS190300`  |              1 | [DOID:4990](http://purl.obolibrary.org/obo/DOID_4990)                                                                |
| `MIM:PS609698`  |              1 | [DOID:50](http://purl.obolibrary.org/obo/DOID_50)                                                                    |
| `MIM:PS616814`  |              1 | [DOID:5223](http://purl.obolibrary.org/obo/DOID_5223)                                                                |
| `MIM:PS167250`  |              1 | [DOID:5408](http://purl.obolibrary.org/obo/DOID_5408)                                                                |
| `MIM:PS311360`  |              1 | [DOID:5426](http://purl.obolibrary.org/obo/DOID_5426)                                                                |
| `MIM:PS128100`  |              1 | [DOID:543](http://purl.obolibrary.org/obo/DOID_543)                                                                  |
| `MIM:PS265450`  |              1 | [DOID:5453](http://purl.obolibrary.org/obo/DOID_5453)                                                                |
| `MIM:PS604370`  |              1 | [DOID:5683](http://purl.obolibrary.org/obo/DOID_5683)                                                                |
| `MIM:PS165500`  |              1 | [DOID:5723](http://purl.obolibrary.org/obo/DOID_5723)                                                                |
| `MIM:PS209920`  |              1 | [DOID:5812](http://purl.obolibrary.org/obo/DOID_5812)                                                                |
| `MIM:PS167870`  |              1 | [DOID:594](http://purl.obolibrary.org/obo/DOID_594)                                                                  |
| `MIM:PS300755`  |              1 | [DOID:612](http://purl.obolibrary.org/obo/DOID_612)                                                                  |
| `MIM:PS601457`  |              1 | [DOID:627](http://purl.obolibrary.org/obo/DOID_627)                                                                  |
| `MIM:PS157300`  |              1 | [DOID:6364](http://purl.obolibrary.org/obo/DOID_6364)                                                                |
| `MIM:PS158350`  |              1 | [DOID:6457](http://purl.obolibrary.org/obo/DOID_6457)                                                                |
| `MIM:PS249270`  |              1 | [DOID:655](http://purl.obolibrary.org/obo/DOID_655)                                                                  |
| `MIM:PS601104`  |              1 | [DOID:678](http://purl.obolibrary.org/obo/DOID_678)                                                                  |
| `MIM:PS155600`  |              1 | [DOID:6846](http://purl.obolibrary.org/obo/DOID_6846)                                                                |
| `MIM:PS106300`  |              1 | [DOID:7147](http://purl.obolibrary.org/obo/DOID_7147)                                                                |
| `MIM:PS100070`  |              1 | [DOID:7693](http://purl.obolibrary.org/obo/DOID_7693)                                                                |
| `MIM:PS116200`  |              1 | [DOID:83](http://purl.obolibrary.org/obo/DOID_83)                                                                    |
| `MIM:PS145600`  |              1 | [DOID:8545](http://purl.obolibrary.org/obo/DOID_8545)                                                                |
| `MIM:PS177900`  |              1 | [DOID:8893](http://purl.obolibrary.org/obo/DOID_8893)                                                                |
| `MIM:PS254800`  |              1 | [DOID:891](http://purl.obolibrary.org/obo/DOID_891)                                                                  |
| `MIM:PS300751`  |              1 | [DOID:8955](http://purl.obolibrary.org/obo/DOID_8955)                                                                |
| `MIM:PS161400`  |              1 | [DOID:8986](http://purl.obolibrary.org/obo/DOID_8986)                                                                |
| `MIM:PS602483`  |              1 | [DOID:9000208](http://purl.obolibrary.org/obo/DOID_9000208)                                                          |
| `MIM:PS613573`  |              1 | [DOID:9000244](http://purl.obolibrary.org/obo/DOID_9000244)                                                          |
| `MIM:PS619142`  |              1 | [DOID:9000250](http://purl.obolibrary.org/obo/DOID_9000250)                                                          |
| `MIM:PS245480`  |              1 | [DOID:9000265](http://purl.obolibrary.org/obo/DOID_9000265)                                                          |
| `MIM:PS245590`  |              1 | [DOID:9000309](http://purl.obolibrary.org/obo/DOID_9000309)                                                          |
| `MIM:PS256850`  |              1 | [DOID:9000462](http://purl.obolibrary.org/obo/DOID_9000462)                                                          |
| `MIM:PS243180`  |              1 | [DOID:9000473](http://purl.obolibrary.org/obo/DOID_9000473)                                                          |
| `MIM:PS607250`  |              1 | [DOID:9000588](http://purl.obolibrary.org/obo/DOID_9000588)                                                          |
| `MIM:PS617236`  |              1 | [DOID:9000732](http://purl.obolibrary.org/obo/DOID_9000732)                                                          |
| `MIM:PS136500`  |              1 | [DOID:9000745](http://purl.obolibrary.org/obo/DOID_9000745)                                                          |
| `MIM:PS113700`  |              1 | [DOID:9000865](http://purl.obolibrary.org/obo/DOID_9000865)                                                          |
| `MIM:PS618005`  |              1 | [DOID:9001022](http://purl.obolibrary.org/obo/DOID_9001022)                                                          |
| `MIM:PS605253`  |              1 | [DOID:9001527](http://purl.obolibrary.org/obo/DOID_9001527)                                                          |
| `MIM:PS206100`  |              1 | [DOID:9001631](http://purl.obolibrary.org/obo/DOID_9001631)                                                          |
| `MIM:PS601471`  |              1 | [DOID:9001799](http://purl.obolibrary.org/obo/DOID_9001799)                                                          |
| `MIM:PS609129`  |              1 | [DOID:9001890](http://purl.obolibrary.org/obo/DOID_9001890)                                                          |
| `MIM:PS136520`  |              1 | [DOID:9001923](http://purl.obolibrary.org/obo/DOID_9001923)                                                          |
| `MIM:PS613658`  |              1 | [DOID:9001942](http://purl.obolibrary.org/obo/DOID_9001942)                                                          |
| `MIM:PS267750`  |              1 | [DOID:9002033](http://purl.obolibrary.org/obo/DOID_9002033)                                                          |
| `MIM:PS251290`  |              1 | [DOID:9002061](http://purl.obolibrary.org/obo/DOID_9002061)                                                          |
| `MIM:PS614372`  |              1 | [DOID:9002118](http://purl.obolibrary.org/obo/DOID_9002118)                                                          |
| `MIM:PS308205`  |              1 | [DOID:9002152](http://purl.obolibrary.org/obo/DOID_9002152)                                                          |
| `MIM:PS251280`  |              1 | [DOID:9002171](http://purl.obolibrary.org/obo/DOID_9002171)                                                          |
| `MIM:PS603387`  |              1 | [DOID:9002403](http://purl.obolibrary.org/obo/DOID_9002403)                                                          |
| `MIM:PS615952`  |              1 | [DOID:9002419](http://purl.obolibrary.org/obo/DOID_9002419)                                                          |
| `MIM:PS605432`  |              1 | [DOID:9002496](http://purl.obolibrary.org/obo/DOID_9002496)                                                          |
| `MIM:PS277450`  |              1 | [DOID:9002557](http://purl.obolibrary.org/obo/DOID_9002557)                                                          |
| `MIM:PS300345`  |              1 | [DOID:9002642](http://purl.obolibrary.org/obo/DOID_9002642)                                                          |
| `MIM:PS614231`  |              1 | [DOID:9002791](http://purl.obolibrary.org/obo/DOID_9002791)                                                          |
| `MIM:PS616418`  |              1 | [DOID:9002857](http://purl.obolibrary.org/obo/DOID_9002857)                                                          |
| `MIM:PS612199`  |              1 | [DOID:9003025](http://purl.obolibrary.org/obo/DOID_9003025)                                                          |
| `MIM:PS174200`  |              1 | [DOID:9003071](http://purl.obolibrary.org/obo/DOID_9003071)                                                          |
| `MIM:PS105550`  |              1 | [DOID:9003713](http://purl.obolibrary.org/obo/DOID_9003713)                                                          |
| `MIM:PS184260`  |              1 | [DOID:9003789](http://purl.obolibrary.org/obo/DOID_9003789)                                                          |
| `MIM:PS616866`  |              1 | [DOID:9004171](http://purl.obolibrary.org/obo/DOID_9004171)                                                          |
| `MIM:PS135500`  |              1 | [DOID:9004260](http://purl.obolibrary.org/obo/DOID_9004260)                                                          |
| `MIM:PS601559`  |              1 | [DOID:9004577](http://purl.obolibrary.org/obo/DOID_9004577)                                                          |
| `MIM:PS604391`  |              1 | [DOID:9004583](http://purl.obolibrary.org/obo/DOID_9004583)                                                          |
| `MIM:PS617877`  |              1 | [DOID:9004675](http://purl.obolibrary.org/obo/DOID_9004675)                                                          |
| `MIM:PS193670`  |              1 | [DOID:9004715](http://purl.obolibrary.org/obo/DOID_9004715)                                                          |
| `MIM:PS607313`  |              1 | [DOID:9004787](http://purl.obolibrary.org/obo/DOID_9004787)                                                          |
| `MIM:PS174400`  |              1 | [DOID:9005329](http://purl.obolibrary.org/obo/DOID_9005329)                                                          |
| `MIM:PS229200`  |              1 | [DOID:9005468](http://purl.obolibrary.org/obo/DOID_9005468)                                                          |
| `MIM:PS608354`  |              1 | [DOID:9005469](http://purl.obolibrary.org/obo/DOID_9005469)                                                          |
| `MIM:PS251270`  |              1 | [DOID:9005482](http://purl.obolibrary.org/obo/DOID_9005482)                                                          |
| `MIM:PS190350`  |              1 | [DOID:9005517](http://purl.obolibrary.org/obo/DOID_9005517)                                                          |
| `MIM:PS277400`  |              1 | [DOID:9005614](http://purl.obolibrary.org/obo/DOID_9005614)                                                          |
| `MIM:PS148210`  |              1 | [DOID:9005709](http://purl.obolibrary.org/obo/DOID_9005709)                                                          |
| `MIM:PS223360`  |              1 | [DOID:9005950](http://purl.obolibrary.org/obo/DOID_9005950)                                                          |
| `MIM:PS616744`  |              1 | [DOID:9005986](http://purl.obolibrary.org/obo/DOID_9005986)                                                          |
| `MIM:PS614592`  |              1 | [DOID:9006314](http://purl.obolibrary.org/obo/DOID_9006314)                                                          |
| `MIM:PS616263`  |              1 | [DOID:9006461](http://purl.obolibrary.org/obo/DOID_9006461)                                                          |
| `MIM:PS615419`  |              1 | [DOID:9006603](http://purl.obolibrary.org/obo/DOID_9006603)                                                          |
| `MIM:PS261100`  |              1 | [DOID:9006825](http://purl.obolibrary.org/obo/DOID_9006825)                                                          |
| `MIM:PS609161`  |              1 | [DOID:9006845](http://purl.obolibrary.org/obo/DOID_9006845)                                                          |
| `MIM:PS617186`  |              1 | [DOID:9006901](http://purl.obolibrary.org/obo/DOID_9006901)                                                          |
| `MIM:PS612975`  |              1 | [DOID:9006913](http://purl.obolibrary.org/obo/DOID_9006913)                                                          |
| `MIM:PS188580`  |              1 | [DOID:9006927](http://purl.obolibrary.org/obo/DOID_9006927)                                                          |
| `MIM:PS212720`  |              1 | [DOID:9006949](http://purl.obolibrary.org/obo/DOID_9006949)                                                          |
| `MIM:PS607748`  |              1 | [DOID:9007118](http://purl.obolibrary.org/obo/DOID_9007118)                                                          |
| `MIM:PS614675`  |              1 | [DOID:9007222](http://purl.obolibrary.org/obo/DOID_9007222)                                                          |
| `MIM:PS190440`  |              1 | [DOID:9007261](http://purl.obolibrary.org/obo/DOID_9007261)                                                          |
| `MIM:PS301108`  |              1 | [DOID:9007299](http://purl.obolibrary.org/obo/DOID_9007299)                                                          |
| `MIM:PS182250`  |              1 | [DOID:9007304](http://purl.obolibrary.org/obo/DOID_9007304)                                                          |
| `MIM:PS179800`  |              1 | [DOID:9007406](http://purl.obolibrary.org/obo/DOID_9007406)                                                          |
| `MIM:PS615774`  |              1 | [DOID:9007456](http://purl.obolibrary.org/obo/DOID_9007456)                                                          |
| `MIM:PS193100`  |              1 | [DOID:9007505](http://purl.obolibrary.org/obo/DOID_9007505)                                                          |
| `MIM:PS613652`  |              1 | [DOID:9007516](http://purl.obolibrary.org/obo/DOID_9007516)                                                          |
| `MIM:PS220150`  |              1 | [DOID:9007605](http://purl.obolibrary.org/obo/DOID_9007605)                                                          |
| `MIM:PS614937`  |              1 | [DOID:9007722](http://purl.obolibrary.org/obo/DOID_9007722)                                                          |
| `MIM:PS606703`  |              1 | [DOID:9007924](http://purl.obolibrary.org/obo/DOID_9007924)                                                          |
| `MIM:PS617660`  |              1 | [DOID:9008119](http://purl.obolibrary.org/obo/DOID_9008119)                                                          |
| `MIM:PS619980`  |              1 | [DOID:9008270](http://purl.obolibrary.org/obo/DOID_9008270)                                                          |
| `MIM:PS614742`  |              1 | [DOID:9008357](http://purl.obolibrary.org/obo/DOID_9008357)                                                          |
| `MIM:PS619758`  |              1 | [DOID:9008554](http://purl.obolibrary.org/obo/DOID_9008554)                                                          |
| `MIM:PS618332`  |              1 | [DOID:9008706](http://purl.obolibrary.org/obo/DOID_9008706)                                                          |
| `MIM:PS619115`  |              1 | [DOID:9008741](http://purl.obolibrary.org/obo/DOID_9008741)                                                          |
| `MIM:PS210900`  |              1 | [DOID:9009080](http://purl.obolibrary.org/obo/DOID_9009080)                                                          |
| `MIM:PS221770`  |              1 | [DOID:9009089](http://purl.obolibrary.org/obo/DOID_9009089)                                                          |
| `MIM:PS236270`  |              1 | [DOID:9009103](http://purl.obolibrary.org/obo/DOID_9009103)                                                          |
| `MIM:PS243150`  |              1 | [DOID:9009203](http://purl.obolibrary.org/obo/DOID_9009203)                                                          |
| `MIM:PS252270`  |              1 | [DOID:9009254](http://purl.obolibrary.org/obo/DOID_9009254)                                                          |
| `MIM:PS616355`  |              1 | [DOID:9009276](http://purl.obolibrary.org/obo/DOID_9009276)                                                          |
| `MIM:PS619539`  |              1 | [DOID:9009291](http://purl.obolibrary.org/obo/DOID_9009291)                                                          |
| `MIM:PS608207`  |              1 | [DOID:9146](http://purl.obolibrary.org/obo/DOID_9146)                                                                |
| `MIM:PS118450`  |              1 | [DOID:9245](http://purl.obolibrary.org/obo/DOID_9245)                                                                |
| `MIM:PS193500`  |              1 | [DOID:9258](http://purl.obolibrary.org/obo/DOID_9258)                                                                |
| `MIM:PS605899`  |              1 | [DOID:9268](http://purl.obolibrary.org/obo/DOID_9268)                                                                |
| `MIM:PS248600`  |              1 | [DOID:9269](http://purl.obolibrary.org/obo/DOID_9269)                                                                |
| `MIM:PS276700`  |              1 | [DOID:9275](http://purl.obolibrary.org/obo/DOID_9275)                                                                |
| `MIM:PS610551`  |              1 | [DOID:936](http://purl.obolibrary.org/obo/DOID_936)                                                                  |
| `MIM:PS613038`  |              1 | [DOID:9410](http://purl.obolibrary.org/obo/DOID_9410)                                                                |
| `MIM:PS244400`  |              1 | [DOID:9562](http://purl.obolibrary.org/obo/DOID_9562)                                                                |
| `MIM:PS211400`  |              1 | [DOID:9563](http://purl.obolibrary.org/obo/DOID_9563)                                                                |
| `MIM:PS193000`  |              1 | [DOID:9620](http://purl.obolibrary.org/obo/DOID_9620)                                                                |
| `MIM:PS160120`  |              1 | [DOID:963](http://purl.obolibrary.org/obo/DOID_963)                                                                  |
| `MIM:PS310700`  |              1 | [DOID:9649](http://purl.obolibrary.org/obo/DOID_9649)                                                                |
| `MIM:PS215500`  |              1 | [DOID:980](http://purl.obolibrary.org/obo/DOID_980)                                                                  |
| `MIM:PS203655`  |              1 | [DOID:987](http://purl.obolibrary.org/obo/DOID_987)                                                                  |
| `MIM:PS230400`  |              1 | [DOID:9870](http://purl.obolibrary.org/obo/DOID_9870)                                                                |
| `MIM:PS157700`  |              1 | [DOID:988](http://purl.obolibrary.org/obo/DOID_988)                                                                  |
| `MIM:PS241550`  |              1 | [DOID:9955](http://purl.obolibrary.org/obo/DOID_9955)                                                                |

## `MONDO`: Mondo Disease Ontology

Overall, there were 10 invalid
xrefs to external prefixed with `MONDO` (standardized to Bioregistry
prefix [`mondo`](https://bioregistry.io/mondo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref    |   usages_count | usages                                                      |
|------------------|----------------|-------------------------------------------------------------|
| `MONDO:00030711` |              1 | [DOID:0051001](http://purl.obolibrary.org/obo/DOID_0051001) |
| `MONDO:009830`   |              1 | [DOID:0060372](http://purl.obolibrary.org/obo/DOID_0060372) |
| `MONDO:00958185` |              1 | [DOID:0060999](http://purl.obolibrary.org/obo/DOID_0060999) |
| `MONDO:00957208` |              1 | [DOID:0061018](http://purl.obolibrary.org/obo/DOID_0061018) |
| `MONDO:00018931` |              1 | [DOID:0080071](http://purl.obolibrary.org/obo/DOID_0080071) |
| `MONDO:08910`    |              1 | [DOID:0111583](http://purl.obolibrary.org/obo/DOID_0111583) |
| `MONDO:009404`   |              1 | [DOID:14670](http://purl.obolibrary.org/obo/DOID_14670)     |
| `MONDO:003092`   |              1 | [DOID:4685](http://purl.obolibrary.org/obo/DOID_4685)       |
| `MONDO:008206`   |              1 | [DOID:9006032](http://purl.obolibrary.org/obo/DOID_9006032) |
| `MONDO:14646`    |              1 | [DOID:9008174](http://purl.obolibrary.org/obo/DOID_9008174) |

