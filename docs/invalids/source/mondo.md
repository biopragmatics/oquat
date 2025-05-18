# mondo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `mondo`. See the [GitHub repository](https://github.com/monarch-initiative/mondo).


## `DO`: Human Disease Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `DO` (standardized to Bioregistry
prefix [`doid`](https://bioregistry.io/doid)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `DO:wk,ls`      |              1 | [MONDO:0000275](http://purl.obolibrary.org/obo/MONDO_0000275) |

## `GARD`: Genetic and Rare Diseases Information Center

Overall, there were 1 invalid
xrefs to external prefixed with `GARD` (standardized to Bioregistry
prefix [`gard`](https://bioregistry.io/gard)) that
did not match the standard pattern `^\d+$`.

| external_xref      |   usages_count | usages                                                        |
|--------------------|----------------|---------------------------------------------------------------|
| `GARD:0003995-def` |              1 | [MONDO:0044749](http://purl.obolibrary.org/obo/MONDO_0044749) |

## `ICD9`: International Classification of Diseases, 9th Revision

Overall, there were 31 invalid
xrefs to external prefixed with `ICD9` (standardized to Bioregistry
prefix [`icd9`](https://bioregistry.io/icd9)) that
did not match the standard pattern `^(\d\d\d|V\d\d|E[8-9]\d\d)(\.\d{1,2})?$`.

| external_xref     |   usages_count | usages                                                                                                                       |
|-------------------|----------------|------------------------------------------------------------------------------------------------------------------------------|
| `ICD9:520-579.99` |              2 | [MONDO:0004335](http://purl.obolibrary.org/obo/MONDO_0004335), [MONDO:0005020](http://purl.obolibrary.org/obo/MONDO_0005020) |
| `ICD9:001-009.99` |              1 | [MONDO:0000916](http://purl.obolibrary.org/obo/MONDO_0000916)                                                                |
| `ICD9:614-616.99` |              1 | [MONDO:0000922](http://purl.obolibrary.org/obo/MONDO_0000922)                                                                |
| `ICD9:110-118.99` |              1 | [MONDO:0002041](http://purl.obolibrary.org/obo/MONDO_0002041)                                                                |
| `ICD9:610-612.99` |              1 | [MONDO:0002657](http://purl.obolibrary.org/obo/MONDO_0002657)                                                                |
| `ICD9:600-608.99` |              1 | [MONDO:0003150](http://purl.obolibrary.org/obo/MONDO_0003150)                                                                |
| `ICD9:240-246.99` |              1 | [MONDO:0003240](http://purl.obolibrary.org/obo/MONDO_0003240)                                                                |
| `ICD9:350-359.99` |              1 | [MONDO:0003620](http://purl.obolibrary.org/obo/MONDO_0003620)                                                                |
| `ICD9:230-234.99` |              1 | [MONDO:0004647](http://purl.obolibrary.org/obo/MONDO_0004647)                                                                |
| `ICD9:120-129.99` |              1 | [MONDO:0004664](http://purl.obolibrary.org/obo/MONDO_0004664)                                                                |
| `ICD9:390-459.99` |              1 | [MONDO:0004995](http://purl.obolibrary.org/obo/MONDO_0004995)                                                                |
| `ICD9:420-429.99` |              1 | [MONDO:0004995](http://purl.obolibrary.org/obo/MONDO_0004995)                                                                |
| `ICD9:490-496.99` |              1 | [MONDO:0005002](http://purl.obolibrary.org/obo/MONDO_0005002)                                                                |
| `ICD9:410-414.99` |              1 | [MONDO:0005010](http://purl.obolibrary.org/obo/MONDO_0005010)                                                                |
| `ICD9:560-569.99` |              1 | [MONDO:0005020](http://purl.obolibrary.org/obo/MONDO_0005020)                                                                |
| `ICD9:570-579.99` |              1 | [MONDO:0005020](http://purl.obolibrary.org/obo/MONDO_0005020)                                                                |
| `ICD9:401-405.99` |              1 | [MONDO:0005044](http://purl.obolibrary.org/obo/MONDO_0005044)                                                                |
| `ICD9:140-239.99` |              1 | [MONDO:0005070](http://purl.obolibrary.org/obo/MONDO_0005070)                                                                |
| `ICD9:290-299.99` |              1 | [MONDO:0005084](http://purl.obolibrary.org/obo/MONDO_0005084)                                                                |
| `ICD9:460-519.99` |              1 | [MONDO:0005087](http://purl.obolibrary.org/obo/MONDO_0005087)                                                                |
| `ICD9:500-508.99` |              1 | [MONDO:0005087](http://purl.obolibrary.org/obo/MONDO_0005087)                                                                |
| `ICD9:510-519.99` |              1 | [MONDO:0005087](http://purl.obolibrary.org/obo/MONDO_0005087)                                                                |
| `ICD9:060-066.99` |              1 | [MONDO:0005108](http://purl.obolibrary.org/obo/MONDO_0005108)                                                                |
| `ICD9:042-042.99` |              1 | [MONDO:0005109](http://purl.obolibrary.org/obo/MONDO_0005109)                                                                |
| `ICD9:210-229.99` |              1 | [MONDO:0005165](http://purl.obolibrary.org/obo/MONDO_0005165)                                                                |
| `ICD9:280-289.99` |              1 | [MONDO:0005570](http://purl.obolibrary.org/obo/MONDO_0005570)                                                                |
| `ICD9:540-543.99` |              1 | [MONDO:0005649](http://purl.obolibrary.org/obo/MONDO_0005649)                                                                |
| `ICD9:430-438.99` |              1 | [MONDO:0011057](http://purl.obolibrary.org/obo/MONDO_0011057)                                                                |
| `ICD9:390-392.99` |              1 | [MONDO:0017767](http://purl.obolibrary.org/obo/MONDO_0017767)                                                                |
| `ICD9:209-209.99` |              1 | [MONDO:0019496](http://purl.obolibrary.org/obo/MONDO_0019496)                                                                |

## `ICD9CM`: International Classification of Diseases, 9th Revision, Clinical Modification

Overall, there were 2 invalid
xrefs to external prefixed with `ICD9CM` (standardized to Bioregistry
prefix [`icd9cm`](https://bioregistry.io/icd9cm)) that
did not match the standard pattern `^([\dA-Z]\d{2}(\.\d{1,3}|))|(\d{2}(\.\d{1,2}|))$`.

| external_xref       |   usages_count | usages                                                        |
|---------------------|----------------|---------------------------------------------------------------|
| `ICD9CM:280-289.99` |              1 | [MONDO:0005570](http://purl.obolibrary.org/obo/MONDO_0005570) |
| `ICD9CM:390-392.99` |              1 | [MONDO:0017767](http://purl.obolibrary.org/obo/MONDO_0017767) |

## `ICDO`: International Classification of Diseases for Oncology

Overall, there were 9 invalid
xrefs to external prefixed with `ICDO` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                      |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ICDO:0000/0`   |              3 | [MONDO:0003011](http://purl.obolibrary.org/obo/MONDO_0003011), [MONDO:0006131](http://purl.obolibrary.org/obo/MONDO_0006131), [MONDO:0006397](http://purl.obolibrary.org/obo/MONDO_0006397) |
| `ICDO:8800/9`   |              1 | [MONDO:0004309](http://purl.obolibrary.org/obo/MONDO_0004309)                                                                                                                               |
| `ICDO:M9861/3`  |              1 | [MONDO:0004996](http://purl.obolibrary.org/obo/MONDO_0004996)                                                                                                                               |
| `ICDO:981-983`  |              1 | [MONDO:0005402](http://purl.obolibrary.org/obo/MONDO_0005402)                                                                                                                               |
| `ICDO:8480/6`   |              1 | [MONDO:0017048](http://purl.obolibrary.org/obo/MONDO_0017048)                                                                                                                               |
| `ICDO:8010/6`   |              1 | [MONDO:0024879](http://purl.obolibrary.org/obo/MONDO_0024879)                                                                                                                               |
| `ICDO:8000/6`   |              1 | [MONDO:0024883](http://purl.obolibrary.org/obo/MONDO_0024883)                                                                                                                               |

## `MedDRA`: Medical Dictionary for Regulatory Activities Terminology

Overall, there were 1 invalid
xrefs to external prefixed with `MedDRA` (standardized to Bioregistry
prefix [`meddra`](https://bioregistry.io/meddra)) that
did not match the standard pattern `^\d+$`.

| external_xref     |   usages_count | usages                                                        |
|-------------------|----------------|---------------------------------------------------------------|
| `MedDRA:C1535926` |              1 | [MONDO:0700092](http://purl.obolibrary.org/obo/MONDO_0700092) |

## `MEDGEN`: Human Medical Genetics

Overall, there were 106 invalid
xrefs to external prefixed with `MEDGEN` (standardized to Bioregistry
prefix [`medgen`](https://bioregistry.io/medgen)) that
did not match the standard pattern `^[CN]*\d{4,7}$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `MEDGEN:610`    |              1 | [MONDO:0000009](http://purl.obolibrary.org/obo/MONDO_0000009) |
| `MEDGEN:849`    |              1 | [MONDO:0000437](http://purl.obolibrary.org/obo/MONDO_0000437) |
| `MEDGEN:194`    |              1 | [MONDO:0000661](http://purl.obolibrary.org/obo/MONDO_0000661) |
| `MEDGEN:966`    |              1 | [MONDO:0001122](http://purl.obolibrary.org/obo/MONDO_0001122) |
| `MEDGEN:604`    |              1 | [MONDO:0001531](http://purl.obolibrary.org/obo/MONDO_0001531) |
| `MEDGEN:571`    |              1 | [MONDO:0001564](http://purl.obolibrary.org/obo/MONDO_0001564) |
| `MEDGEN:785`    |              1 | [MONDO:0001612](http://purl.obolibrary.org/obo/MONDO_0001612) |
| `MEDGEN:925`    |              1 | [MONDO:0001751](http://purl.obolibrary.org/obo/MONDO_0001751) |
| `MEDGEN:872`    |              1 | [MONDO:0001797](http://purl.obolibrary.org/obo/MONDO_0001797) |
| `MEDGEN:491`    |              1 | [MONDO:0001882](http://purl.obolibrary.org/obo/MONDO_0001882) |
| `MEDGEN:90`     |              1 | [MONDO:0001909](http://purl.obolibrary.org/obo/MONDO_0001909) |
| `MEDGEN:297`    |              1 | [MONDO:0001939](http://purl.obolibrary.org/obo/MONDO_0001939) |
| `MEDGEN:709`    |              1 | [MONDO:0002123](http://purl.obolibrary.org/obo/MONDO_0002123) |
| `MEDGEN:920`    |              1 | [MONDO:0002155](http://purl.obolibrary.org/obo/MONDO_0002155) |
| `MEDGEN:525`    |              1 | [MONDO:0002278](http://purl.obolibrary.org/obo/MONDO_0002278) |
| `MEDGEN:676`    |              1 | [MONDO:0002443](http://purl.obolibrary.org/obo/MONDO_0002443) |
| `MEDGEN:691`    |              1 | [MONDO:0002471](http://purl.obolibrary.org/obo/MONDO_0002471) |
| `MEDGEN:358`    |              1 | [MONDO:0002476](http://purl.obolibrary.org/obo/MONDO_0002476) |
| `MEDGEN:123`    |              1 | [MONDO:0002512](http://purl.obolibrary.org/obo/MONDO_0002512) |
| `MEDGEN:359`    |              1 | [MONDO:0002519](http://purl.obolibrary.org/obo/MONDO_0002519) |
| `MEDGEN:652`    |              1 | [MONDO:0002657](http://purl.obolibrary.org/obo/MONDO_0002657) |
| `MEDGEN:154`    |              1 | [MONDO:0002816](http://purl.obolibrary.org/obo/MONDO_0002816) |
| `MEDGEN:609`    |              1 | [MONDO:0002901](http://purl.obolibrary.org/obo/MONDO_0002901) |
| `MEDGEN:312`    |              1 | [MONDO:0003039](http://purl.obolibrary.org/obo/MONDO_0003039) |
| `MEDGEN:264`    |              1 | [MONDO:0003040](http://purl.obolibrary.org/obo/MONDO_0003040) |
| `MEDGEN:360`    |              1 | [MONDO:0003046](http://purl.obolibrary.org/obo/MONDO_0003046) |
| `MEDGEN:175`    |              1 | [MONDO:0003709](http://purl.obolibrary.org/obo/MONDO_0003709) |
| `MEDGEN:930`    |              1 | [MONDO:0004575](http://purl.obolibrary.org/obo/MONDO_0004575) |
| `MEDGEN:116`    |              1 | [MONDO:0004613](http://purl.obolibrary.org/obo/MONDO_0004613) |
| `MEDGEN:763`    |              1 | [MONDO:0004647](http://purl.obolibrary.org/obo/MONDO_0004647) |
| `MEDGEN:484`    |              1 | [MONDO:0004652](http://purl.obolibrary.org/obo/MONDO_0004652) |
| `MEDGEN:942`    |              1 | [MONDO:0004674](http://purl.obolibrary.org/obo/MONDO_0004674) |
| `MEDGEN:598`    |              1 | [MONDO:0004785](http://purl.obolibrary.org/obo/MONDO_0004785) |
| `MEDGEN:49`     |              1 | [MONDO:0004846](http://purl.obolibrary.org/obo/MONDO_0004846) |
| `MEDGEN:122`    |              1 | [MONDO:0004970](http://purl.obolibrary.org/obo/MONDO_0004970) |
| `MEDGEN:125`    |              1 | [MONDO:0004972](http://purl.obolibrary.org/obo/MONDO_0004972) |
| `MEDGEN:274`    |              1 | [MONDO:0004976](http://purl.obolibrary.org/obo/MONDO_0004976) |
| `MEDGEN:445`    |              1 | [MONDO:0004981](http://purl.obolibrary.org/obo/MONDO_0004981) |
| `MEDGEN:594`    |              1 | [MONDO:0004987](http://purl.obolibrary.org/obo/MONDO_0004987) |
| `MEDGEN:765`    |              1 | [MONDO:0005023](http://purl.obolibrary.org/obo/MONDO_0005023) |
| `MEDGEN:764`    |              1 | [MONDO:0005082](http://purl.obolibrary.org/obo/MONDO_0005082) |
| `MEDGEN:766`    |              1 | [MONDO:0005086](http://purl.obolibrary.org/obo/MONDO_0005086) |
| `MEDGEN:362`    |              1 | [MONDO:0005160](http://purl.obolibrary.org/obo/MONDO_0005160) |
| `MEDGEN:482`    |              1 | [MONDO:0005229](http://purl.obolibrary.org/obo/MONDO_0005229) |
| `MEDGEN:853`    |              1 | [MONDO:0005264](http://purl.obolibrary.org/obo/MONDO_0005264) |
| `MEDGEN:213`    |              1 | [MONDO:0005340](http://purl.obolibrary.org/obo/MONDO_0005340) |
| `MEDGEN:316`    |              1 | [MONDO:0005351](http://purl.obolibrary.org/obo/MONDO_0005351) |
| `MEDGEN:868`    |              1 | [MONDO:0005491](http://purl.obolibrary.org/obo/MONDO_0005491) |
| `MEDGEN:714`    |              1 | [MONDO:0005557](http://purl.obolibrary.org/obo/MONDO_0005557) |
| `MEDGEN:361`    |              1 | [MONDO:0005618](http://purl.obolibrary.org/obo/MONDO_0005618) |
| `MEDGEN:126`    |              1 | [MONDO:0005636](http://purl.obolibrary.org/obo/MONDO_0005636) |
| `MEDGEN:174`    |              1 | [MONDO:0005638](http://purl.obolibrary.org/obo/MONDO_0005638) |
| `MEDGEN:504`    |              1 | [MONDO:0005664](http://purl.obolibrary.org/obo/MONDO_0005664) |
| `MEDGEN:586`    |              1 | [MONDO:0005668](http://purl.obolibrary.org/obo/MONDO_0005668) |
| `MEDGEN:597`    |              1 | [MONDO:0005672](http://purl.obolibrary.org/obo/MONDO_0005672) |
| `MEDGEN:600`    |              1 | [MONDO:0005673](http://purl.obolibrary.org/obo/MONDO_0005673) |
| `MEDGEN:674`    |              1 | [MONDO:0005683](http://purl.obolibrary.org/obo/MONDO_0005683) |
| `MEDGEN:743`    |              1 | [MONDO:0005690](http://purl.obolibrary.org/obo/MONDO_0005690) |
| `MEDGEN:869`    |              1 | [MONDO:0005844](http://purl.obolibrary.org/obo/MONDO_0005844) |
| `MEDGEN:295`    |              1 | [MONDO:0006021](http://purl.obolibrary.org/obo/MONDO_0006021) |
| `MEDGEN:918`    |              1 | [MONDO:0006108](http://purl.obolibrary.org/obo/MONDO_0006108) |
| `MEDGEN:124`    |              1 | [MONDO:0006493](http://purl.obolibrary.org/obo/MONDO_0006493) |
| `MEDGEN:854`    |              1 | [MONDO:0006497](http://purl.obolibrary.org/obo/MONDO_0006497) |
| `MEDGEN:284`    |              1 | [MONDO:0006506](http://purl.obolibrary.org/obo/MONDO_0006506) |
| `MEDGEN:229`    |              1 | [MONDO:0006625](http://purl.obolibrary.org/obo/MONDO_0006625) |
| `MEDGEN:161`    |              1 | [MONDO:0006641](http://purl.obolibrary.org/obo/MONDO_0006641) |
| `MEDGEN:543`    |              1 | [MONDO:0006676](http://purl.obolibrary.org/obo/MONDO_0006676) |
| `MEDGEN:296`    |              1 | [MONDO:0006805](http://purl.obolibrary.org/obo/MONDO_0006805) |
| `MEDGEN:254`    |              1 | [MONDO:0006944](http://purl.obolibrary.org/obo/MONDO_0006944) |
| `MEDGEN:364`    |              1 | [MONDO:0006992](http://purl.obolibrary.org/obo/MONDO_0006992) |
| `MEDGEN:54`     |              1 | [MONDO:0007035](http://purl.obolibrary.org/obo/MONDO_0007035) |
| `MEDGEN:651`    |              1 | [MONDO:0007254](http://purl.obolibrary.org/obo/MONDO_0007254) |
| `MEDGEN:495`    |              1 | [MONDO:0007416](http://purl.obolibrary.org/obo/MONDO_0007416) |
| `MEDGEN:939`    |              1 | [MONDO:0008207](http://purl.obolibrary.org/obo/MONDO_0008207) |
| `MEDGEN:969`    |              1 | [MONDO:0008829](http://purl.obolibrary.org/obo/MONDO_0008829) |
| `MEDGEN:439`    |              1 | [MONDO:0008840](http://purl.obolibrary.org/obo/MONDO_0008840) |
| `MEDGEN:891`    |              1 | [MONDO:0009280](http://purl.obolibrary.org/obo/MONDO_0009280) |
| `MEDGEN:944`    |              1 | [MONDO:0010557](http://purl.obolibrary.org/obo/MONDO_0010557) |
| `MEDGEN:945`    |              1 | [MONDO:0010604](http://purl.obolibrary.org/obo/MONDO_0010604) |
| `MEDGEN:858`    |              1 | [MONDO:0011057](http://purl.obolibrary.org/obo/MONDO_0011057) |
| `MEDGEN:287`    |              1 | [MONDO:0011382](http://purl.obolibrary.org/obo/MONDO_0011382) |
| `MEDGEN:99`     |              1 | [MONDO:0012268](http://purl.obolibrary.org/obo/MONDO_0012268) |
| `MEDGEN:665`    |              1 | [MONDO:0015265](http://purl.obolibrary.org/obo/MONDO_0015265) |
| `MEDGEN:168`    |              1 | [MONDO:0015977](http://purl.obolibrary.org/obo/MONDO_0015977) |
| `MEDGEN:498`    |              1 | [MONDO:0016430](http://purl.obolibrary.org/obo/MONDO_0016430) |
| `MEDGEN:283`    |              1 | [MONDO:0016486](http://purl.obolibrary.org/obo/MONDO_0016486) |
| `MEDGEN:668`    |              1 | [MONDO:0016523](http://purl.obolibrary.org/obo/MONDO_0016523) |
| `MEDGEN:138`    |              1 | [MONDO:0018690](http://purl.obolibrary.org/obo/MONDO_0018690) |
| `MEDGEN:272`    |              1 | [MONDO:0019065](http://purl.obolibrary.org/obo/MONDO_0019065) |
| `MEDGEN:240`    |              1 | [MONDO:0019507](http://purl.obolibrary.org/obo/MONDO_0019507) |
| `MEDGEN:84`     |              1 | [MONDO:0019648](http://purl.obolibrary.org/obo/MONDO_0019648) |
| `MEDGEN:438`    |              1 | [MONDO:0019781](http://purl.obolibrary.org/obo/MONDO_0019781) |
| `MEDGEN:98`     |              1 | [MONDO:0020599](http://purl.obolibrary.org/obo/MONDO_0020599) |
| `MEDGEN:114`    |              1 | [MONDO:0020600](http://purl.obolibrary.org/obo/MONDO_0020600) |
| `MEDGEN:113`    |              1 | [MONDO:0020680](http://purl.obolibrary.org/obo/MONDO_0020680) |
| `MEDGEN:177`    |              1 | [MONDO:0020689](http://purl.obolibrary.org/obo/MONDO_0020689) |
| `MEDGEN:389`    |              1 | [MONDO:0020731](http://purl.obolibrary.org/obo/MONDO_0020731) |
| `MEDGEN:935`    |              1 | [MONDO:0020779](http://purl.obolibrary.org/obo/MONDO_0020779) |
| `MEDGEN:965`    |              1 | [MONDO:0020782](http://purl.obolibrary.org/obo/MONDO_0020782) |
| `MEDGEN:365`    |              1 | [MONDO:0021902](http://purl.obolibrary.org/obo/MONDO_0021902) |
| `MEDGEN:585`    |              1 | [MONDO:0024613](http://purl.obolibrary.org/obo/MONDO_0024613) |
| `MEDGEN:637`    |              1 | [MONDO:0037872](http://purl.obolibrary.org/obo/MONDO_0037872) |
| `MEDGEN:182`    |              1 | [MONDO:0043209](http://purl.obolibrary.org/obo/MONDO_0043209) |
| `MEDGEN:103`    |              1 | [MONDO:0043472](http://purl.obolibrary.org/obo/MONDO_0043472) |
| `MEDGEN:762`    |              1 | [MONDO:0043529](http://purl.obolibrary.org/obo/MONDO_0043529) |
| `MEDGEN:294`    |              1 | [MONDO:0700064](http://purl.obolibrary.org/obo/MONDO_0700064) |

## `MESH`: Medical Subject Headings

Overall, there were 6 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D|M)\d{6,9}$`.

| external_xref           |   usages_count | usages                                                                                                                       |
|-------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------|
| `MESH:1622152`          |              2 | [MONDO:0000890](http://purl.obolibrary.org/obo/MONDO_0000890), [MONDO:0000890](http://purl.obolibrary.org/obo/MONDO_0000890) |
| `MESH:D018382-modified` |              1 | [MONDO:0001328](http://purl.obolibrary.org/obo/MONDO_0001328)                                                                |
| `MESH:D014077-modified` |              1 | [MONDO:0002325](http://purl.obolibrary.org/obo/MONDO_0002325)                                                                |
| `MESH:D014253-modified` |              1 | [MONDO:0005995](http://purl.obolibrary.org/obo/MONDO_0005995)                                                                |
| `MESH:D014323-modified` |              1 | [MONDO:0005998](http://purl.obolibrary.org/obo/MONDO_0005998)                                                                |

## `MONDO`: Mondo Disease Ontology

Overall, there were 19,733 invalid
xrefs to external prefixed with `MONDO` (standardized to Bioregistry
prefix [`mondo`](https://bioregistry.io/mondo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                                                  |   usages_count | usages                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MONDO:Lexical`                                                |           4556 | [MONDO:0000170](http://purl.obolibrary.org/obo/MONDO_0000170), [MONDO:0000200](http://purl.obolibrary.org/obo/MONDO_0000200), [MONDO:0000208](http://purl.obolibrary.org/obo/MONDO_0000208), [MONDO:0000902](http://purl.obolibrary.org/obo/MONDO_0000902), [MONDO:0000908](http://purl.obolibrary.org/obo/MONDO_0000908), ... |
| `MONDO:patterns/disease_series_by_gene`                        |           4003 | [MONDO:0000764](http://purl.obolibrary.org/obo/MONDO_0000764), [MONDO:0000908](http://purl.obolibrary.org/obo/MONDO_0000908), [MONDO:0000908](http://purl.obolibrary.org/obo/MONDO_0000908), [MONDO:0000911](http://purl.obolibrary.org/obo/MONDO_0000911), [MONDO:0000911](http://purl.obolibrary.org/obo/MONDO_0000911), ... |
| `MONDO:design_pattern`                                         |           2882 | [MONDO:0000212](http://purl.obolibrary.org/obo/MONDO_0000212), [MONDO:0000212](http://purl.obolibrary.org/obo/MONDO_0000212), [MONDO:0000257](http://purl.obolibrary.org/obo/MONDO_0000257), [MONDO:0000270](http://purl.obolibrary.org/obo/MONDO_0000270), [MONDO:0000414](http://purl.obolibrary.org/obo/MONDO_0000414), ... |
| `MONDO:patterns/location`                                      |           2827 | [MONDO:0000236](http://purl.obolibrary.org/obo/MONDO_0000236), [MONDO:0000236](http://purl.obolibrary.org/obo/MONDO_0000236), [MONDO:0000242](http://purl.obolibrary.org/obo/MONDO_0000242), [MONDO:0000242](http://purl.obolibrary.org/obo/MONDO_0000242), [MONDO:0000253](http://purl.obolibrary.org/obo/MONDO_0000253), ... |
| `MONDO:patterns/nonhuman_disease`                              |           1337 | [MONDO:0700049](http://purl.obolibrary.org/obo/MONDO_0700049), [MONDO:0700050](http://purl.obolibrary.org/obo/MONDO_0700050), [MONDO:0700053](http://purl.obolibrary.org/obo/MONDO_0700053), [MONDO:0700056](http://purl.obolibrary.org/obo/MONDO_0700056), [MONDO:0700059](http://purl.obolibrary.org/obo/MONDO_0700059), ... |
| `MONDO:ambiguous`                                              |            444 | [MONDO:0000063](http://purl.obolibrary.org/obo/MONDO_0000063), [MONDO:0000094](http://purl.obolibrary.org/obo/MONDO_0000094), [MONDO:0000106](http://purl.obolibrary.org/obo/MONDO_0000106), [MONDO:0000129](http://purl.obolibrary.org/obo/MONDO_0000129), [MONDO:0000138](http://purl.obolibrary.org/obo/MONDO_0000138), ... |
| `MONDO:patterns/specific_infectious_disease_by_agent`          |            349 | [MONDO:0000276](http://purl.obolibrary.org/obo/MONDO_0000276), [MONDO:0000292](http://purl.obolibrary.org/obo/MONDO_0000292), [MONDO:0000294](http://purl.obolibrary.org/obo/MONDO_0000294), [MONDO:0000294](http://purl.obolibrary.org/obo/MONDO_0000294), [MONDO:0000295](http://purl.obolibrary.org/obo/MONDO_0000295), ... |
| `MONDO:patterns/nonhuman_disease_series_by_gene`               |            314 | [MONDO:1010510](http://purl.obolibrary.org/obo/MONDO_1010510), [MONDO:1010511](http://purl.obolibrary.org/obo/MONDO_1010511), [MONDO:1010512](http://purl.obolibrary.org/obo/MONDO_1010512), [MONDO:1010616](http://purl.obolibrary.org/obo/MONDO_1010616), [MONDO:1010617](http://purl.obolibrary.org/obo/MONDO_1010617), ... |
| `MONDO:patterns/location_top`                                  |            243 | [MONDO:0000270](http://purl.obolibrary.org/obo/MONDO_0000270), [MONDO:0000462](http://purl.obolibrary.org/obo/MONDO_0000462), [MONDO:0000462](http://purl.obolibrary.org/obo/MONDO_0000462), [MONDO:0000469](http://purl.obolibrary.org/obo/MONDO_0000469), [MONDO:0000470](http://purl.obolibrary.org/obo/MONDO_0000470), ... |
| `MONDO:patterns/cancer`                                        |            242 | [MONDO:0000376](http://purl.obolibrary.org/obo/MONDO_0000376), [MONDO:0000377](http://purl.obolibrary.org/obo/MONDO_0000377), [MONDO:0000380](http://purl.obolibrary.org/obo/MONDO_0000380), [MONDO:0000405](http://purl.obolibrary.org/obo/MONDO_0000405), [MONDO:0000612](http://purl.obolibrary.org/obo/MONDO_0000612), ... |
| `MONDO:patterns/neoplasm`                                      |            234 | [MONDO:0000921](http://purl.obolibrary.org/obo/MONDO_0000921), [MONDO:0000933](http://purl.obolibrary.org/obo/MONDO_0000933), [MONDO:0001236](http://purl.obolibrary.org/obo/MONDO_0001236), [MONDO:0001406](http://purl.obolibrary.org/obo/MONDO_0001406), [MONDO:0001420](http://purl.obolibrary.org/obo/MONDO_0001420), ... |
| `MONDO:patterns/hereditary`                                    |            231 | [MONDO:0000044](http://purl.obolibrary.org/obo/MONDO_0000044), [MONDO:0000700](http://purl.obolibrary.org/obo/MONDO_0000700), [MONDO:0000995](http://purl.obolibrary.org/obo/MONDO_0000995), [MONDO:0001115](http://purl.obolibrary.org/obo/MONDO_0001115), [MONDO:0001336](http://purl.obolibrary.org/obo/MONDO_0001336), ... |
| `MONDO:patterns/rare`                                          |            154 | [MONDO:0015076](http://purl.obolibrary.org/obo/MONDO_0015076), [MONDO:0015076](http://purl.obolibrary.org/obo/MONDO_0015076), [MONDO:0015108](http://purl.obolibrary.org/obo/MONDO_0015108), [MONDO:0015112](http://purl.obolibrary.org/obo/MONDO_0015112), [MONDO:0015112](http://purl.obolibrary.org/obo/MONDO_0015112), ... |
| `MONDO:patterns/inflammatory_disease_by_site`                  |            130 | [MONDO:0000261](http://purl.obolibrary.org/obo/MONDO_0000261), [MONDO:0000261](http://purl.obolibrary.org/obo/MONDO_0000261), [MONDO:0000409](http://purl.obolibrary.org/obo/MONDO_0000409), [MONDO:0000497](http://purl.obolibrary.org/obo/MONDO_0000497), [MONDO:0000739](http://purl.obolibrary.org/obo/MONDO_0000739), ... |
| `MONDO:patterns/carcinoma`                                     |            114 | [MONDO:0000380](http://purl.obolibrary.org/obo/MONDO_0000380), [MONDO:0000521](http://purl.obolibrary.org/obo/MONDO_0000521), [MONDO:0000552](http://purl.obolibrary.org/obo/MONDO_0000552), [MONDO:0001502](http://purl.obolibrary.org/obo/MONDO_0001502), [MONDO:0001602](http://purl.obolibrary.org/obo/MONDO_0001602), ... |
| `MONDO:patterns/chronic`                                       |             99 | [MONDO:0000492](http://purl.obolibrary.org/obo/MONDO_0000492), [MONDO:0000492](http://purl.obolibrary.org/obo/MONDO_0000492), [MONDO:0001007](http://purl.obolibrary.org/obo/MONDO_0001007), [MONDO:0001007](http://purl.obolibrary.org/obo/MONDO_0001007), [MONDO:0001014](http://purl.obolibrary.org/obo/MONDO_0001014), ... |
| `MONDO:patterns/inborn_metabolic`                              |             98 | [MONDO:0000155](http://purl.obolibrary.org/obo/MONDO_0000155), [MONDO:0000155](http://purl.obolibrary.org/obo/MONDO_0000155), [MONDO:0000351](http://purl.obolibrary.org/obo/MONDO_0000351), [MONDO:0000351](http://purl.obolibrary.org/obo/MONDO_0000351), [MONDO:0000421](http://purl.obolibrary.org/obo/MONDO_0000421), ... |
| `MONDO:patterns/autosomal_dominant`                            |             93 | [MONDO:0000426](http://purl.obolibrary.org/obo/MONDO_0000426), [MONDO:0000426](http://purl.obolibrary.org/obo/MONDO_0000426), [MONDO:0004691](http://purl.obolibrary.org/obo/MONDO_0004691), [MONDO:0004691](http://purl.obolibrary.org/obo/MONDO_0004691), [MONDO:0007086](http://purl.obolibrary.org/obo/MONDO_0007086), ... |
| `MONDO:patterns/acquired`                                      |             91 | [MONDO:0001198](http://purl.obolibrary.org/obo/MONDO_0001198), [MONDO:0001198](http://purl.obolibrary.org/obo/MONDO_0001198), [MONDO:0001296](http://purl.obolibrary.org/obo/MONDO_0001296), [MONDO:0001296](http://purl.obolibrary.org/obo/MONDO_0001296), [MONDO:0001828](http://purl.obolibrary.org/obo/MONDO_0001828), ... |
| `MONDO:patterns/autosomal_recessive`                           |             83 | [MONDO:0000212](http://purl.obolibrary.org/obo/MONDO_0000212), [MONDO:0002014](http://purl.obolibrary.org/obo/MONDO_0002014), [MONDO:0006025](http://purl.obolibrary.org/obo/MONDO_0006025), [MONDO:0006025](http://purl.obolibrary.org/obo/MONDO_0006025), [MONDO:0008406](http://purl.obolibrary.org/obo/MONDO_0008406), ... |
| `MONDO:LexicalVariant`                                         |             83 | [MONDO:0000710](http://purl.obolibrary.org/obo/MONDO_0000710), [MONDO:0000906](http://purl.obolibrary.org/obo/MONDO_0000906), [MONDO:0001049](http://purl.obolibrary.org/obo/MONDO_0001049), [MONDO:0001224](http://purl.obolibrary.org/obo/MONDO_0001224), [MONDO:0001252](http://purl.obolibrary.org/obo/MONDO_0001252), ... |
| `MONDO:patterns/acute`                                         |             79 | [MONDO:0000222](http://purl.obolibrary.org/obo/MONDO_0000222), [MONDO:0000222](http://purl.obolibrary.org/obo/MONDO_0000222), [MONDO:0000257](http://purl.obolibrary.org/obo/MONDO_0000257), [MONDO:0000257](http://purl.obolibrary.org/obo/MONDO_0000257), [MONDO:0000990](http://purl.obolibrary.org/obo/MONDO_0000990), ... |
| `MONDO:patterns/basis_in_disruption_of_process`                |             79 | [MONDO:0002145](http://purl.obolibrary.org/obo/MONDO_0002145), [MONDO:0002459](http://purl.obolibrary.org/obo/MONDO_0002459), [MONDO:0002459](http://purl.obolibrary.org/obo/MONDO_0002459), [MONDO:0003832](http://purl.obolibrary.org/obo/MONDO_0003832), [MONDO:0005066](http://purl.obolibrary.org/obo/MONDO_0005066), ... |
| `MONDO:patterns/inherited_susceptibility`                      |             75 | [MONDO:0007454](http://purl.obolibrary.org/obo/MONDO_0007454), [MONDO:0007573](http://purl.obolibrary.org/obo/MONDO_0007573), [MONDO:0009100](http://purl.obolibrary.org/obo/MONDO_0009100), [MONDO:0010861](http://purl.obolibrary.org/obo/MONDO_0010861), [MONDO:0010862](http://purl.obolibrary.org/obo/MONDO_0010862), ... |
| `MONDO:patterns/infectious_disease_by_agent`                   |             73 | [MONDO:0000276](http://purl.obolibrary.org/obo/MONDO_0000276), [MONDO:0000290](http://purl.obolibrary.org/obo/MONDO_0000290), [MONDO:0000290](http://purl.obolibrary.org/obo/MONDO_0000290), [MONDO:0000292](http://purl.obolibrary.org/obo/MONDO_0000292), [MONDO:0000298](http://purl.obolibrary.org/obo/MONDO_0000298), ... |
| `MONDO:patterns/childhood`                                     |             72 | [MONDO:0000414](http://purl.obolibrary.org/obo/MONDO_0000414), [MONDO:0002505](http://purl.obolibrary.org/obo/MONDO_0002505), [MONDO:0002540](http://purl.obolibrary.org/obo/MONDO_0002540), [MONDO:0002623](http://purl.obolibrary.org/obo/MONDO_0002623), [MONDO:0002685](http://purl.obolibrary.org/obo/MONDO_0002685), ... |
| `MONDO:patterns/isolated`                                      |             69 | [MONDO:0000062](http://purl.obolibrary.org/obo/MONDO_0000062), [MONDO:0000062](http://purl.obolibrary.org/obo/MONDO_0000062), [MONDO:0000509](http://purl.obolibrary.org/obo/MONDO_0000509), [MONDO:0000509](http://purl.obolibrary.org/obo/MONDO_0000509), [MONDO:0000722](http://purl.obolibrary.org/obo/MONDO_0000722), ... |
| `MONDO:patterns/syndromic`                                     |             64 | [MONDO:0000508](http://purl.obolibrary.org/obo/MONDO_0000508), [MONDO:0000508](http://purl.obolibrary.org/obo/MONDO_0000508), [MONDO:0002254](http://purl.obolibrary.org/obo/MONDO_0002254), [MONDO:0009105](http://purl.obolibrary.org/obo/MONDO_0009105), [MONDO:0015150](http://purl.obolibrary.org/obo/MONDO_0015150), ... |
| `MONDO:patterns/allergy`                                       |             62 | [MONDO:0000606](http://purl.obolibrary.org/obo/MONDO_0000606), [MONDO:0000606](http://purl.obolibrary.org/obo/MONDO_0000606), [MONDO:0000772](http://purl.obolibrary.org/obo/MONDO_0000772), [MONDO:0000772](http://purl.obolibrary.org/obo/MONDO_0000772), [MONDO:0000773](http://purl.obolibrary.org/obo/MONDO_0000773), ... |
| `MONDO:patterns/genetic`                                       |             62 | [MONDO:0007781](http://purl.obolibrary.org/obo/MONDO_0007781), [MONDO:0007781](http://purl.obolibrary.org/obo/MONDO_0007781), [MONDO:0009970](http://purl.obolibrary.org/obo/MONDO_0009970), [MONDO:0009970](http://purl.obolibrary.org/obo/MONDO_0009970), [MONDO:0013099](http://purl.obolibrary.org/obo/MONDO_0013099), ... |
| `MONDO:patterns/adult`                                         |             58 | [MONDO:0000814](http://purl.obolibrary.org/obo/MONDO_0000814), [MONDO:0000875](http://purl.obolibrary.org/obo/MONDO_0000875), [MONDO:0001907](http://purl.obolibrary.org/obo/MONDO_0001907), [MONDO:0002543](http://purl.obolibrary.org/obo/MONDO_0002543), [MONDO:0002676](http://purl.obolibrary.org/obo/MONDO_0002676), ... |
| `MONDO:patterns/malignant`                                     |             55 | [MONDO:0000377](http://purl.obolibrary.org/obo/MONDO_0000377), [MONDO:0000378](http://purl.obolibrary.org/obo/MONDO_0000378), [MONDO:0000379](http://purl.obolibrary.org/obo/MONDO_0000379), [MONDO:0000379](http://purl.obolibrary.org/obo/MONDO_0000379), [MONDO:0000407](http://purl.obolibrary.org/obo/MONDO_0000407), ... |
| `MONDO:patterns/carcinoma_in_situ`                             |             53 | [MONDO:0000371](http://purl.obolibrary.org/obo/MONDO_0000371), [MONDO:0000372](http://purl.obolibrary.org/obo/MONDO_0000372), [MONDO:0000373](http://purl.obolibrary.org/obo/MONDO_0000373), [MONDO:0000373](http://purl.obolibrary.org/obo/MONDO_0000373), [MONDO:0000374](http://purl.obolibrary.org/obo/MONDO_0000374), ... |
| `MONDO:patterns/x_linked`                                      |             53 | [MONDO:0000425](http://purl.obolibrary.org/obo/MONDO_0000425), [MONDO:0000425](http://purl.obolibrary.org/obo/MONDO_0000425), [MONDO:0010222](http://purl.obolibrary.org/obo/MONDO_0010222), [MONDO:0010222](http://purl.obolibrary.org/obo/MONDO_0010222), [MONDO:0010248](http://purl.obolibrary.org/obo/MONDO_0010248), ... |
| `MONDO:patterns/sarcoma`                                       |             49 | [MONDO:0001204](http://purl.obolibrary.org/obo/MONDO_0001204), [MONDO:0001374](http://purl.obolibrary.org/obo/MONDO_0001374), [MONDO:0001387](http://purl.obolibrary.org/obo/MONDO_0001387), [MONDO:0001418](http://purl.obolibrary.org/obo/MONDO_0001418), [MONDO:0001501](http://purl.obolibrary.org/obo/MONDO_0001501), ... |
| `MONDO:patterns/benign`                                        |             34 | [MONDO:0000638](http://purl.obolibrary.org/obo/MONDO_0000638), [MONDO:0000638](http://purl.obolibrary.org/obo/MONDO_0000638), [MONDO:0000654](http://purl.obolibrary.org/obo/MONDO_0000654), [MONDO:0002065](http://purl.obolibrary.org/obo/MONDO_0002065), [MONDO:0002373](http://purl.obolibrary.org/obo/MONDO_0002373), ... |
| `MONDO:patterns/chromosome_type`                               |             24 | [MONDO:0020583](http://purl.obolibrary.org/obo/MONDO_0020583), [MONDO:0700008](http://purl.obolibrary.org/obo/MONDO_0700008), [MONDO:0700009](http://purl.obolibrary.org/obo/MONDO_0700009), [MONDO:0700010](http://purl.obolibrary.org/obo/MONDO_0700010), [MONDO:0700011](http://purl.obolibrary.org/obo/MONDO_0700011), ... |
| `MONDO:patterns/neuroendocrine_neoplasm`                       |             20 | [MONDO:0002477](http://purl.obolibrary.org/obo/MONDO_0002477), [MONDO:0002481](http://purl.obolibrary.org/obo/MONDO_0002481), [MONDO:0002485](http://purl.obolibrary.org/obo/MONDO_0002485), [MONDO:0002882](http://purl.obolibrary.org/obo/MONDO_0002882), [MONDO:0002883](http://purl.obolibrary.org/obo/MONDO_0002883), ... |
| `MONDO:patterns/allergic_form_of_disease`                      |             14 | [MONDO:0000771](http://purl.obolibrary.org/obo/MONDO_0000771), [MONDO:0000771](http://purl.obolibrary.org/obo/MONDO_0000771), [MONDO:0004784](http://purl.obolibrary.org/obo/MONDO_0004784), [MONDO:0004784](http://purl.obolibrary.org/obo/MONDO_0004784), [MONDO:0004980](http://purl.obolibrary.org/obo/MONDO_0004980), ... |
| `MONDO:patterns/specific_inflammatory_disease_by_site`         |             13 | [MONDO:0000252](http://purl.obolibrary.org/obo/MONDO_0000252), [MONDO:0000271](http://purl.obolibrary.org/obo/MONDO_0000271), [MONDO:0000709](http://purl.obolibrary.org/obo/MONDO_0000709), [MONDO:0000916](http://purl.obolibrary.org/obo/MONDO_0000916), [MONDO:0001537](http://purl.obolibrary.org/obo/MONDO_0001537), ... |
| `MONDO:patterns/autoimmune`                                    |             13 | [MONDO:0000587](http://purl.obolibrary.org/obo/MONDO_0000587), [MONDO:0000774](http://purl.obolibrary.org/obo/MONDO_0000774), [MONDO:0015939](http://purl.obolibrary.org/obo/MONDO_0015939), [MONDO:0018242](http://purl.obolibrary.org/obo/MONDO_0018242), [MONDO:0019098](http://purl.obolibrary.org/obo/MONDO_0019098), ... |
| `MONDO:patterns/congenital`                                    |             13 | [MONDO:0000577](http://purl.obolibrary.org/obo/MONDO_0000577), [MONDO:0001902](http://purl.obolibrary.org/obo/MONDO_0001902), [MONDO:0001902](http://purl.obolibrary.org/obo/MONDO_0001902), [MONDO:0005712](http://purl.obolibrary.org/obo/MONDO_0005712), [MONDO:0005714](http://purl.obolibrary.org/obo/MONDO_0005714), ... |
| `MONDO:patterns/neuroendocrine_neoplasm_grade1`                |             12 | [MONDO:0000540](http://purl.obolibrary.org/obo/MONDO_0000540), [MONDO:0006091](http://purl.obolibrary.org/obo/MONDO_0006091), [MONDO:0006093](http://purl.obolibrary.org/obo/MONDO_0006093), [MONDO:0006126](http://purl.obolibrary.org/obo/MONDO_0006126), [MONDO:0006155](http://purl.obolibrary.org/obo/MONDO_0006155), ... |
| `MONDO:patterns/OMIM_disease_series_by_gene`                   |             11 | [MONDO:0007617](http://purl.obolibrary.org/obo/MONDO_0007617), [MONDO:0014914](http://purl.obolibrary.org/obo/MONDO_0014914), [MONDO:0032702](http://purl.obolibrary.org/obo/MONDO_0032702), [MONDO:0032770](http://purl.obolibrary.org/obo/MONDO_0032770), [MONDO:0033492](http://purl.obolibrary.org/obo/MONDO_0033492), ... |
| `MONDO:patterns/patterns/poisoning`                            |              9 | [MONDO:0100331](http://purl.obolibrary.org/obo/MONDO_0100331), [MONDO:0100335](http://purl.obolibrary.org/obo/MONDO_0100335), [MONDO:0800373](http://purl.obolibrary.org/obo/MONDO_0800373), [MONDO:0800384](http://purl.obolibrary.org/obo/MONDO_0800384), [MONDO:0800385](http://purl.obolibrary.org/obo/MONDO_0800385), ... |
| `MONDO:patterns/environmental_stimulus`                        |              8 | [MONDO:0001000](http://purl.obolibrary.org/obo/MONDO_0001000), [MONDO:0001540](http://purl.obolibrary.org/obo/MONDO_0001540), [MONDO:0005425](http://purl.obolibrary.org/obo/MONDO_0005425), [MONDO:0006654](http://purl.obolibrary.org/obo/MONDO_0006654), [MONDO:0006688](http://purl.obolibrary.org/obo/MONDO_0006688), ... |
| `MONDO:patterns/infantile`                                     |              7 | [MONDO:0000212](http://purl.obolibrary.org/obo/MONDO_0000212), [MONDO:0015804](http://purl.obolibrary.org/obo/MONDO_0015804), [MONDO:0015804](http://purl.obolibrary.org/obo/MONDO_0015804), [MONDO:0017354](http://purl.obolibrary.org/obo/MONDO_0017354), [MONDO:0019190](http://purl.obolibrary.org/obo/MONDO_0019190), ... |
| `MONDO:patterns/disease_by_dysfunctional_structure`            |              6 | [MONDO:0001343](http://purl.obolibrary.org/obo/MONDO_0001343), [MONDO:0001343](http://purl.obolibrary.org/obo/MONDO_0001343), [MONDO:0004880](http://purl.obolibrary.org/obo/MONDO_0004880), [MONDO:0004880](http://purl.obolibrary.org/obo/MONDO_0004880), [MONDO:0100311](http://purl.obolibrary.org/obo/MONDO_0100311), ... |
| `MONDO:patterns/rare_genetic`                                  |              5 | [MONDO:0015107](http://purl.obolibrary.org/obo/MONDO_0015107), [MONDO:0015513](http://purl.obolibrary.org/obo/MONDO_0015513), [MONDO:0015955](http://purl.obolibrary.org/obo/MONDO_0015955), [MONDO:0015972](http://purl.obolibrary.org/obo/MONDO_0015972), [MONDO:0015972](http://purl.obolibrary.org/obo/MONDO_0015972)      |
| `MONDO:patterns/y_linked`                                      |              4 | [MONDO:0000428](http://purl.obolibrary.org/obo/MONDO_0000428), [MONDO:0000428](http://purl.obolibrary.org/obo/MONDO_0000428), [MONDO:0010761](http://purl.obolibrary.org/obo/MONDO_0010761), [MONDO:0010761](http://purl.obolibrary.org/obo/MONDO_0010761)                                                                     |
| `MONDO:patterns/susceptibility_by_gene`                        |              4 | [MONDO:0014680](http://purl.obolibrary.org/obo/MONDO_0014680), [MONDO:0100183](http://purl.obolibrary.org/obo/MONDO_0100183), [MONDO:0100231](http://purl.obolibrary.org/obo/MONDO_0100231), [MONDO:0100231](http://purl.obolibrary.org/obo/MONDO_0100231)                                                                     |
| `MONDO:patterns/disrupts_process`                              |              3 | [MONDO:0056803](http://purl.obolibrary.org/obo/MONDO_0056803), [MONDO:0100277](http://purl.obolibrary.org/obo/MONDO_0100277), [MONDO:0100306](http://purl.obolibrary.org/obo/MONDO_0100306)                                                                                                                                    |
| `MONDO:patterns/inborn_metabolic_disrupts`                     |              3 | [MONDO:0019688](http://purl.obolibrary.org/obo/MONDO_0019688), [MONDO:0100188](http://purl.obolibrary.org/obo/MONDO_0100188), [MONDO:0100304](http://purl.obolibrary.org/obo/MONDO_0100304)                                                                                                                                    |
| `MONDO:pr`                                                     |              2 | [MONDO:0002014](http://purl.obolibrary.org/obo/MONDO_0002014), [MONDO:0007524](http://purl.obolibrary.org/obo/MONDO_0007524)                                                                                                                                                                                                   |
| `MONDO:patterns/idiopathic`                                    |              2 | [MONDO:0600023](http://purl.obolibrary.org/obo/MONDO_0600023), [MONDO:0700007](http://purl.obolibrary.org/obo/MONDO_0700007)                                                                                                                                                                                                   |
| `MONDO:patterns/monosomy`                                      |              2 | [MONDO:0700035](http://purl.obolibrary.org/obo/MONDO_0700035), [MONDO:0700035](http://purl.obolibrary.org/obo/MONDO_0700035)                                                                                                                                                                                                   |
| `MONDO:patterns/post_infectious_disease`                       |              2 | [MONDO:0700280](http://purl.obolibrary.org/obo/MONDO_0700280), [MONDO:0700280](http://purl.obolibrary.org/obo/MONDO_0700280)                                                                                                                                                                                                   |
| `MONDO:patterns`                                               |              1 | [MONDO:0000263](http://purl.obolibrary.org/obo/MONDO_0000263)                                                                                                                                                                                                                                                                  |
| `MONDO:nv`                                                     |              1 | [MONDO:0003832](http://purl.obolibrary.org/obo/MONDO_0003832)                                                                                                                                                                                                                                                                  |
| `MONDO:patterns/juvenile`                                      |              1 | [MONDO:0100037](http://purl.obolibrary.org/obo/MONDO_0100037)                                                                                                                                                                                                                                                                  |
| `MONDO:patterns/disease-like`                                  |              1 | [MONDO:0100365](http://purl.obolibrary.org/obo/MONDO_0100365)                                                                                                                                                                                                                                                                  |
| `MONDO:patterns/realized_in_response_to_evironmental_exposure` |              1 | [MONDO:0100366](http://purl.obolibrary.org/obo/MONDO_0100366)                                                                                                                                                                                                                                                                  |
| `MONDO:patterns/specific_disease_by_disrupted_process`         |              1 | [MONDO:0100372](http://purl.obolibrary.org/obo/MONDO_0100372)                                                                                                                                                                                                                                                                  |
| `MONDO:pattterns/disease_series_by_gene`                       |              1 | [MONDO:0100436](http://purl.obolibrary.org/obo/MONDO_0100436)                                                                                                                                                                                                                                                                  |
| `MONDO:patterns/trisomy`                                       |              1 | [MONDO:0700126](http://purl.obolibrary.org/obo/MONDO_0700126)                                                                                                                                                                                                                                                                  |
| `MONDO:patterns/poisoning`                                     |              1 | [MONDO:0700296](http://purl.obolibrary.org/obo/MONDO_0700296)                                                                                                                                                                                                                                                                  |
| `MONDO:design_patterns`                                        |              1 | [MONDO:0007256](http://purl.obolibrary.org/obo/MONDO_0007256)                                                                                                                                                                                                                                                                  |
| `MONDO:LexicalPattern`                                         |              1 | [MONDO:0024325](http://purl.obolibrary.org/obo/MONDO_0024325)                                                                                                                                                                                                                                                                  |
| `MONDO:equivalentTo`                                           |              1 | [MONDO:0100087](http://purl.obolibrary.org/obo/MONDO_0100087)                                                                                                                                                                                                                                                                  |

## `NCIT`: NCI Thesaurus

Overall, there were 3 invalid
xrefs to external prefixed with `NCIT` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^[CRPA]\d+$`.

| external_xref           |   usages_count | usages                                                        |
|-------------------------|----------------|---------------------------------------------------------------|
| `NCIT:C128346-modified` |              1 | [MONDO:0005429](http://purl.obolibrary.org/obo/MONDO_0005429) |
| `NCIT:C3131-modified`   |              1 | [MONDO:0021094](http://purl.obolibrary.org/obo/MONDO_0021094) |
| `NCIT:C84543-modified`  |              1 | [MONDO:0043209](http://purl.obolibrary.org/obo/MONDO_0043209) |

## `NIFSTD`: NIF Standard Ontology

Overall, there were 18 invalid
xrefs to external prefixed with `NIFSTD` (standardized to Bioregistry
prefix [`nif.std`](https://bioregistry.io/nif.std)) that
did not match the standard pattern `^BAMSC\d+$`.

| external_xref             |   usages_count | usages                                                        |
|---------------------------|----------------|---------------------------------------------------------------|
| `NIFSTD:birnlex_2092`     |              1 | [MONDO:0004975](http://purl.obolibrary.org/obo/MONDO_0004975) |
| `NIFSTD:birnlex_12566`    |              1 | [MONDO:0004976](http://purl.obolibrary.org/obo/MONDO_0004976) |
| `NIFSTD:birnlex_12754`    |              1 | [MONDO:0004985](http://purl.obolibrary.org/obo/MONDO_0004985) |
| `NIFSTD:birnlex_406`      |              1 | [MONDO:0004992](http://purl.obolibrary.org/obo/MONDO_0004992) |
| `NIFSTD:birnlex_12718`    |              1 | [MONDO:0005027](http://purl.obolibrary.org/obo/MONDO_0005027) |
| `NIFSTD:birnlex_12617`    |              1 | [MONDO:0005033](http://purl.obolibrary.org/obo/MONDO_0005033) |
| `NIFSTD:birnlex_12633`    |              1 | [MONDO:0005035](http://purl.obolibrary.org/obo/MONDO_0005035) |
| `NIFSTD:birnlex_12631`    |              1 | [MONDO:0005072](http://purl.obolibrary.org/obo/MONDO_0005072) |
| `NIFSTD:birnlex_12669`    |              1 | [MONDO:0005084](http://purl.obolibrary.org/obo/MONDO_0005084) |
| `NIFSTD:birnlex_2104`     |              1 | [MONDO:0005090](http://purl.obolibrary.org/obo/MONDO_0005090) |
| `NIFSTD:birnlex_12783`    |              1 | [MONDO:0005098](http://purl.obolibrary.org/obo/MONDO_0005098) |
| `NIFSTD:birnlex_12733`    |              1 | [MONDO:0005115](http://purl.obolibrary.org/obo/MONDO_0005115) |
| `NIFSTD:nlx_dys_20090303` |              1 | [MONDO:0005139](http://purl.obolibrary.org/obo/MONDO_0005139) |
| `NIFSTD:birnlex_12679`    |              1 | [MONDO:0005146](http://purl.obolibrary.org/obo/MONDO_0005146) |
| `NIFSTD:birnlex_12812`    |              1 | [MONDO:0005150](http://purl.obolibrary.org/obo/MONDO_0005150) |
| `NIFSTD:birnlex_2098`     |              1 | [MONDO:0005180](http://purl.obolibrary.org/obo/MONDO_0005180) |
| `NIFSTD:nlx_dys_20090502` |              1 | [MONDO:0008608](http://purl.obolibrary.org/obo/MONDO_0008608) |
| `NIFSTD:nlx_dys_20090302` |              1 | [MONDO:0011122](http://purl.obolibrary.org/obo/MONDO_0011122) |

## `PMID`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref           |   usages_count | usages                                                        |
|-------------------------|----------------|---------------------------------------------------------------|
| `PMID:PMID%3A+19243607` |              1 | [MONDO:0008644](http://purl.obolibrary.org/obo/MONDO_0008644) |

