# bao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `bao`.


## `FBdv`: Drosophila development

Overall, there were 1 invalid
xrefs to external prefixed with `FBdv` (standardized to Bioregistry
prefix [`fbdv`](https://bioregistry.io/fbdv)) that
did not match the standard pattern `^\d{8}$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `FBdv:0005333`  |              1 | [EFO:0001323](http://www.ebi.ac.uk/efo/EFO_0001323) |

## `ICDO`: International Classification of Diseases for Oncology

Overall, there were 8 invalid
xrefs to external prefixed with `ICDO` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref   |   usages_count | usages                                                |
|-----------------|----------------|-------------------------------------------------------|
| `ICDO:M8000/3`  |              1 | [DOID:162](http://purl.obolibrary.org/obo/DOID_162)   |
| `ICDO:M8960/3`  |              1 | [DOID:2154](http://purl.obolibrary.org/obo/DOID_2154) |
| `ICDO:M9400/3`  |              1 | [DOID:3069](http://purl.obolibrary.org/obo/DOID_3069) |
| `ICDO:M9380/3`  |              1 | [DOID:3070](http://purl.obolibrary.org/obo/DOID_3070) |
| `ICDO:M9530/3`  |              1 | [DOID:3565](http://purl.obolibrary.org/obo/DOID_3565) |
| `ICDO:M8170/3`  |              1 | [DOID:684](http://purl.obolibrary.org/obo/DOID_684)   |
| `ICDO:M8970/3`  |              1 | [DOID:687](http://purl.obolibrary.org/obo/DOID_687)   |
| `ICDO:M9500/3`  |              1 | [DOID:769](http://purl.obolibrary.org/obo/DOID_769)   |

## `KEGG`: Kyoto Encyclopedia of Genes and Genomes

Overall, there were 34 invalid
xrefs to external prefixed with `KEGG` (standardized to Bioregistry
prefix [`kegg`](https://bioregistry.io/kegg)) that
did not match the standard pattern `^([CHDEGTMKR]\d+)|(\w+:[\w\d\.-]*)|([a-z]{3,5})|(\w{2,4}\d{5})$`.

| external_xref   |   usages_count | usages                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------|
| `KEGG:05321`    |              2 | [DOID:0050589](http://purl.obolibrary.org/obo/DOID_0050589), [DOID:9778](http://purl.obolibrary.org/obo/DOID_9778) |
| `KEGG:04950`    |              1 | [DOID:0050524](http://purl.obolibrary.org/obo/DOID_0050524)                                                        |
| `KEGG:05034`    |              1 | [DOID:0050741](http://purl.obolibrary.org/obo/DOID_0050741)                                                        |
| `KEGG:05143`    |              1 | [DOID:10112](http://purl.obolibrary.org/obo/DOID_10112)                                                            |
| `KEGG:05215`    |              1 | [DOID:10283](http://purl.obolibrary.org/obo/DOID_10283)                                                            |
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

## `MESH`: Medical Subject Headings

Overall, there were 6 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref              |   usages_count | usages                                                          |
|----------------------------|----------------|-----------------------------------------------------------------|
| `MESH:A03.492.411`         |              1 | [UBERON:0000160](http://purl.obolibrary.org/obo/UBERON_0000160) |
| `MESH:A03.492.766`         |              1 | [UBERON:0000945](http://purl.obolibrary.org/obo/UBERON_0000945) |
| `MESH:A03.365`             |              1 | [UBERON:0001043](http://purl.obolibrary.org/obo/UBERON_0001043) |
| `MESH:A05.810.161`         |              1 | [UBERON:0001255](http://purl.obolibrary.org/obo/UBERON_0001255) |
| `MESH:A03.492.411.620.270` |              1 | [UBERON:0002114](http://purl.obolibrary.org/obo/UBERON_0002114) |
| `MESH:A12.207.630`         |              1 | [UBERON:0002391](http://purl.obolibrary.org/obo/UBERON_0002391) |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `ncithesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                      |   usages_count | usages                                                          |
|------------------------------------|----------------|-----------------------------------------------------------------|
| `ncithesaurus:Developmental_Stage` |              1 | [UBERON:0000105](http://purl.obolibrary.org/obo/UBERON_0000105) |

## `OMIM`: Online Mendelian Inheritance in Man

Overall, there were 120 invalid
xrefs to external prefixed with `OMIM` (standardized to Bioregistry
prefix [`omim`](https://bioregistry.io/omim)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `OMIM:PS267700` |              1 | [DOID:0050120](http://purl.obolibrary.org/obo/DOID_0050120) |
| `OMIM:PS275200` |              1 | [DOID:0050328](http://purl.obolibrary.org/obo/DOID_0050328) |
| `OMIM:PS175100` |              1 | [DOID:0050424](http://purl.obolibrary.org/obo/DOID_0050424) |
| `OMIM:PS107970` |              1 | [DOID:0050431](http://purl.obolibrary.org/obo/DOID_0050431) |
| `OMIM:PS276900` |              1 | [DOID:0050439](http://purl.obolibrary.org/obo/DOID_0050439) |
| `OMIM:PS167200` |              1 | [DOID:0050449](http://purl.obolibrary.org/obo/DOID_0050449) |
| `OMIM:PS601144` |              1 | [DOID:0050451](http://purl.obolibrary.org/obo/DOID_0050451) |
| `OMIM:PS133200` |              1 | [DOID:0050467](http://purl.obolibrary.org/obo/DOID_0050467) |
| `OMIM:PS310500` |              1 | [DOID:0050534](http://purl.obolibrary.org/obo/DOID_0050534) |
| `OMIM:PS133780` |              1 | [DOID:0050535](http://purl.obolibrary.org/obo/DOID_0050535) |
| `OMIM:PS162400` |              1 | [DOID:0050548](http://purl.obolibrary.org/obo/DOID_0050548) |
| `OMIM:PS304500` |              1 | [DOID:0050566](http://purl.obolibrary.org/obo/DOID_0050566) |
| `OMIM:PS119530` |              1 | [DOID:0050567](http://purl.obolibrary.org/obo/DOID_0050567) |
| `OMIM:PS210600` |              1 | [DOID:0050569](http://purl.obolibrary.org/obo/DOID_0050569) |
| `OMIM:PS600721` |              1 | [DOID:0050575](http://purl.obolibrary.org/obo/DOID_0050575) |
| `OMIM:PS218330` |              1 | [DOID:0050577](http://purl.obolibrary.org/obo/DOID_0050577) |
| `OMIM:PS613155` |              1 | [DOID:0050588](http://purl.obolibrary.org/obo/DOID_0050588) |
| `OMIM:PS266600` |              1 | [DOID:0050589](http://purl.obolibrary.org/obo/DOID_0050589) |
| `OMIM:PS202700` |              1 | [DOID:0050590](http://purl.obolibrary.org/obo/DOID_0050590) |
| `OMIM:PS208500` |              1 | [DOID:0050592](http://purl.obolibrary.org/obo/DOID_0050592) |
| `OMIM:PS203100` |              1 | [DOID:0050632](http://purl.obolibrary.org/obo/DOID_0050632) |
| `OMIM:PS608583` |              1 | [DOID:0050650](http://purl.obolibrary.org/obo/DOID_0050650) |
| `OMIM:PS211530` |              1 | [DOID:0050694](http://purl.obolibrary.org/obo/DOID_0050694) |
| `OMIM:PS308350` |              1 | [DOID:0050709](http://purl.obolibrary.org/obo/DOID_0050709) |
| `OMIM:PS210200` |              1 | [DOID:0050710](http://purl.obolibrary.org/obo/DOID_0050710) |
| `OMIM:PS607426` |              1 | [DOID:0050730](http://purl.obolibrary.org/obo/DOID_0050730) |
| `OMIM:PS208085` |              1 | [DOID:0050763](http://purl.obolibrary.org/obo/DOID_0050763) |
| `OMIM:PS168000` |              1 | [DOID:0050773](http://purl.obolibrary.org/obo/DOID_0050773) |
| `OMIM:PS309530` |              1 | [DOID:0050776](http://purl.obolibrary.org/obo/DOID_0050776) |
| `OMIM:PS213200` |              1 | [DOID:0050950](http://purl.obolibrary.org/obo/DOID_0050950) |
| `OMIM:PS156200` |              1 | [DOID:0060307](http://purl.obolibrary.org/obo/DOID_0060307) |
| `OMIM:PS309510` |              1 | [DOID:0060309](http://purl.obolibrary.org/obo/DOID_0060309) |
| `OMIM:PS605552` |              1 | [DOID:0060611](http://purl.obolibrary.org/obo/DOID_0060611) |
| `OMIM:PS242300` |              1 | [DOID:0060655](http://purl.obolibrary.org/obo/DOID_0060655) |
| `OMIM:PS312080` |              1 | [DOID:0060786](http://purl.obolibrary.org/obo/DOID_0060786) |
| `OMIM:PS603041` |              1 | [DOID:0070329](http://purl.obolibrary.org/obo/DOID_0070329) |
| `OMIM:PS123000` |              1 | [DOID:0080033](http://purl.obolibrary.org/obo/DOID_0080033) |
| `OMIM:PS200600` |              1 | [DOID:0080043](http://purl.obolibrary.org/obo/DOID_0080043) |
| `OMIM:PS108300` |              1 | [DOID:0080046](http://purl.obolibrary.org/obo/DOID_0080046) |
| `OMIM:PS173900` |              1 | [DOID:0080322](http://purl.obolibrary.org/obo/DOID_0080322) |
| `OMIM:PS214100` |              1 | [DOID:0080377](http://purl.obolibrary.org/obo/DOID_0080377) |
| `OMIM:PS308230` |              1 | [DOID:0080544](http://purl.obolibrary.org/obo/DOID_0080544) |
| `OMIM:PS147060` |              1 | [DOID:0080545](http://purl.obolibrary.org/obo/DOID_0080545) |
| `OMIM:PS147950` |              1 | [DOID:0090070](http://purl.obolibrary.org/obo/DOID_0090070) |
| `OMIM:PS234200` |              1 | [DOID:0110734](http://purl.obolibrary.org/obo/DOID_0110734) |
| `OMIM:PS236670` |              1 | [DOID:0111229](http://purl.obolibrary.org/obo/DOID_0111229) |
| `OMIM:PS118100` |              1 | [DOID:10426](http://purl.obolibrary.org/obo/DOID_10426)     |
| `OMIM:PS268000` |              1 | [DOID:10584](http://purl.obolibrary.org/obo/DOID_10584)     |
| `OMIM:PS118220` |              1 | [DOID:10595](http://purl.obolibrary.org/obo/DOID_10595)     |
| `OMIM:PS134600` |              1 | [DOID:1062](http://purl.obolibrary.org/obo/DOID_1062)       |
| `OMIM:PS603075` |              1 | [DOID:10871](http://purl.obolibrary.org/obo/DOID_10871)     |
| `OMIM:PS122470` |              1 | [DOID:11725](http://purl.obolibrary.org/obo/DOID_11725)     |
| `OMIM:PS310300` |              1 | [DOID:11726](http://purl.obolibrary.org/obo/DOID_11726)     |
| `OMIM:PS166200` |              1 | [DOID:12347](http://purl.obolibrary.org/obo/DOID_12347)     |
| `OMIM:PS157640` |              1 | [DOID:12558](http://purl.obolibrary.org/obo/DOID_12558)     |
| `OMIM:PS256100` |              1 | [DOID:12712](http://purl.obolibrary.org/obo/DOID_12712)     |
| `OMIM:PS607014` |              1 | [DOID:12798](http://purl.obolibrary.org/obo/DOID_12798)     |
| `OMIM:PS115200` |              1 | [DOID:12930](http://purl.obolibrary.org/obo/DOID_12930)     |
| `OMIM:PS603278` |              1 | [DOID:1312](http://purl.obolibrary.org/obo/DOID_1312)       |
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
| `OMIM:PS215100` |              1 | [DOID:2580](http://purl.obolibrary.org/obo/DOID_2580)       |
| `OMIM:PS601495` |              1 | [DOID:2583](http://purl.obolibrary.org/obo/DOID_2583)       |
| `OMIM:PS127550` |              1 | [DOID:2729](http://purl.obolibrary.org/obo/DOID_2729)       |
| `OMIM:PS192500` |              1 | [DOID:2843](http://purl.obolibrary.org/obo/DOID_2843)       |
| `OMIM:PS154500` |              1 | [DOID:2908](http://purl.obolibrary.org/obo/DOID_2908)       |
| `OMIM:PS601675` |              1 | [DOID:2960](http://purl.obolibrary.org/obo/DOID_2960)       |
| `OMIM:PS259900` |              1 | [DOID:2977](http://purl.obolibrary.org/obo/DOID_2977)       |
| `OMIM:PS151623` |              1 | [DOID:3012](http://purl.obolibrary.org/obo/DOID_3012)       |
| `OMIM:PS137800` |              1 | [DOID:3070](http://purl.obolibrary.org/obo/DOID_3070)       |
| `OMIM:PS123700` |              1 | [DOID:3144](http://purl.obolibrary.org/obo/DOID_3144)       |
| `OMIM:PS161800` |              1 | [DOID:3191](http://purl.obolibrary.org/obo/DOID_3191)       |
| `OMIM:PS603165` |              1 | [DOID:3310](http://purl.obolibrary.org/obo/DOID_3310)       |
| `OMIM:PS105400` |              1 | [DOID:332](http://purl.obolibrary.org/obo/DOID_332)         |
| `OMIM:PS163950` |              1 | [DOID:3490](http://purl.obolibrary.org/obo/DOID_3490)       |
| `OMIM:PS601462` |              1 | [DOID:3635](http://purl.obolibrary.org/obo/DOID_3635)       |
| `OMIM:PS203300` |              1 | [DOID:3753](http://purl.obolibrary.org/obo/DOID_3753)       |
| `OMIM:PS102200` |              1 | [DOID:3829](http://purl.obolibrary.org/obo/DOID_3829)       |
| `OMIM:PS120435` |              1 | [DOID:3883](http://purl.obolibrary.org/obo/DOID_3883)       |
| `OMIM:PS115210` |              1 | [DOID:397](http://purl.obolibrary.org/obo/DOID_397)         |
| `OMIM:PS601678` |              1 | [DOID:445](http://purl.obolibrary.org/obo/DOID_445)         |
| `OMIM:PS605389` |              1 | [DOID:4535](http://purl.obolibrary.org/obo/DOID_4535)       |
| `OMIM:PS236100` |              1 | [DOID:4621](http://purl.obolibrary.org/obo/DOID_4621)       |
| `OMIM:PS190300` |              1 | [DOID:4990](http://purl.obolibrary.org/obo/DOID_4990)       |
| `OMIM:PS212065` |              1 | [DOID:5212](http://purl.obolibrary.org/obo/DOID_5212)       |
| `OMIM:PS128100` |              1 | [DOID:543](http://purl.obolibrary.org/obo/DOID_543)         |
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
| `OMIM:PS244400` |              1 | [DOID:9562](http://purl.obolibrary.org/obo/DOID_9562)       |
| `OMIM:PS211400` |              1 | [DOID:9563](http://purl.obolibrary.org/obo/DOID_9563)       |
| `OMIM:PS310700` |              1 | [DOID:9649](http://purl.obolibrary.org/obo/DOID_9649)       |
| `OMIM:PS203655` |              1 | [DOID:987](http://purl.obolibrary.org/obo/DOID_987)         |

## `ORDO`: Orphanet Rare Disease Ontology

Overall, there were 381 invalid
xrefs to external prefixed with `ORDO` (standardized to Bioregistry
prefix [`orphanet.ordo`](https://bioregistry.io/orphanet.ordo)) that
did not match the standard pattern `^Orphanet(_|:)C?\d+$`.

| external_xref   |   usages_count | usages                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------|
| `ORDO:768`      |              2 | [DOID:0060173](http://purl.obolibrary.org/obo/DOID_0060173), [DOID:2843](http://purl.obolibrary.org/obo/DOID_2843) |
| `ORDO:478`      |              2 | [DOID:0090070](http://purl.obolibrary.org/obo/DOID_0090070), [DOID:3614](http://purl.obolibrary.org/obo/DOID_3614) |
| `ORDO:540`      |              1 | [DOID:0050120](http://purl.obolibrary.org/obo/DOID_0050120)                                                        |
| `ORDO:733`      |              1 | [DOID:0050424](http://purl.obolibrary.org/obo/DOID_0050424)                                                        |
| `ORDO:910`      |              1 | [DOID:0050427](http://purl.obolibrary.org/obo/DOID_0050427)                                                        |
| `ORDO:2337`     |              1 | [DOID:0050428](http://purl.obolibrary.org/obo/DOID_0050428)                                                        |
| `ORDO:247698`   |              1 | [DOID:0050430](http://purl.obolibrary.org/obo/DOID_0050430)                                                        |
| `ORDO:217656`   |              1 | [DOID:0050431](http://purl.obolibrary.org/obo/DOID_0050431)                                                        |
| `ORDO:247`      |              1 | [DOID:0050431](http://purl.obolibrary.org/obo/DOID_0050431)                                                        |
| `ORDO:1162`     |              1 | [DOID:0050432](http://purl.obolibrary.org/obo/DOID_0050432)                                                        |
| `ORDO:2576`     |              1 | [DOID:0050436](http://purl.obolibrary.org/obo/DOID_0050436)                                                        |
| `ORDO:886`      |              1 | [DOID:0050439](http://purl.obolibrary.org/obo/DOID_0050439)                                                        |
| `ORDO:171723`   |              1 | [DOID:0050448](http://purl.obolibrary.org/obo/DOID_0050448)                                                        |
| `ORDO:2309`     |              1 | [DOID:0050449](http://purl.obolibrary.org/obo/DOID_0050449)                                                        |
| `ORDO:130`      |              1 | [DOID:0050451](http://purl.obolibrary.org/obo/DOID_0050451)                                                        |
| `ORDO:29`       |              1 | [DOID:0050452](http://purl.obolibrary.org/obo/DOID_0050452)                                                        |
| `ORDO:102009`   |              1 | [DOID:0050453](http://purl.obolibrary.org/obo/DOID_0050453)                                                        |
| `ORDO:98892`    |              1 | [DOID:0050454](http://purl.obolibrary.org/obo/DOID_0050454)                                                        |
| `ORDO:280`      |              1 | [DOID:0050460](http://purl.obolibrary.org/obo/DOID_0050460)                                                        |
| `ORDO:140`      |              1 | [DOID:0050463](http://purl.obolibrary.org/obo/DOID_0050463)                                                        |
| `ORDO:60030`    |              1 | [DOID:0050466](http://purl.obolibrary.org/obo/DOID_0050466)                                                        |
| `ORDO:317`      |              1 | [DOID:0050467](http://purl.obolibrary.org/obo/DOID_0050467)                                                        |
| `ORDO:508`      |              1 | [DOID:0050470](http://purl.obolibrary.org/obo/DOID_0050470)                                                        |
| `ORDO:1359`     |              1 | [DOID:0050471](http://purl.obolibrary.org/obo/DOID_0050471)                                                        |
| `ORDO:634`      |              1 | [DOID:0050474](http://purl.obolibrary.org/obo/DOID_0050474)                                                        |
| `ORDO:3449`     |              1 | [DOID:0050475](http://purl.obolibrary.org/obo/DOID_0050475)                                                        |
| `ORDO:552`      |              1 | [DOID:0050524](http://purl.obolibrary.org/obo/DOID_0050524)                                                        |
| `ORDO:83420`    |              1 | [DOID:0050529](http://purl.obolibrary.org/obo/DOID_0050529)                                                        |
| `ORDO:215`      |              1 | [DOID:0050534](http://purl.obolibrary.org/obo/DOID_0050534)                                                        |
| `ORDO:891`      |              1 | [DOID:0050535](http://purl.obolibrary.org/obo/DOID_0050535)                                                        |
| `ORDO:450`      |              1 | [DOID:0050545](http://purl.obolibrary.org/obo/DOID_0050545)                                                        |
| `ORDO:324999`   |              1 | [DOID:0050553](http://purl.obolibrary.org/obo/DOID_0050553)                                                        |
| `ORDO:97242`    |              1 | [DOID:0050557](http://purl.obolibrary.org/obo/DOID_0050557)                                                        |
| `ORDO:272`      |              1 | [DOID:0050559](http://purl.obolibrary.org/obo/DOID_0050559)                                                        |
| `ORDO:2382`     |              1 | [DOID:0050561](http://purl.obolibrary.org/obo/DOID_0050561)                                                        |
| `ORDO:90625`    |              1 | [DOID:0050566](http://purl.obolibrary.org/obo/DOID_0050566)                                                        |
| `ORDO:1797`     |              1 | [DOID:0050568](http://purl.obolibrary.org/obo/DOID_0050568)                                                        |
| `ORDO:2311`     |              1 | [DOID:0050568](http://purl.obolibrary.org/obo/DOID_0050568)                                                        |
| `ORDO:808`      |              1 | [DOID:0050569](http://purl.obolibrary.org/obo/DOID_0050569)                                                        |
| `ORDO:1872`     |              1 | [DOID:0050572](http://purl.obolibrary.org/obo/DOID_0050572)                                                        |
| `ORDO:79314`    |              1 | [DOID:0050574](http://purl.obolibrary.org/obo/DOID_0050574)                                                        |
| `ORDO:294937`   |              1 | [DOID:0050581](http://purl.obolibrary.org/obo/DOID_0050581)                                                        |
| `ORDO:370953`   |              1 | [DOID:0050588](http://purl.obolibrary.org/obo/DOID_0050588)                                                        |
| `ORDO:42738`    |              1 | [DOID:0050590](http://purl.obolibrary.org/obo/DOID_0050590)                                                        |
| `ORDO:2227`     |              1 | [DOID:0050591](http://purl.obolibrary.org/obo/DOID_0050591)                                                        |
| `ORDO:99798`    |              1 | [DOID:0050591](http://purl.obolibrary.org/obo/DOID_0050591)                                                        |
| `ORDO:474`      |              1 | [DOID:0050592](http://purl.obolibrary.org/obo/DOID_0050592)                                                        |
| `ORDO:1247`     |              1 | [DOID:0050597](http://purl.obolibrary.org/obo/DOID_0050597)                                                        |
| `ORDO:51`       |              1 | [DOID:0050629](http://purl.obolibrary.org/obo/DOID_0050629)                                                        |
| `ORDO:59`       |              1 | [DOID:0050631](http://purl.obolibrary.org/obo/DOID_0050631)                                                        |
| `ORDO:55`       |              1 | [DOID:0050632](http://purl.obolibrary.org/obo/DOID_0050632)                                                        |
| `ORDO:137807`   |              1 | [DOID:0050639](http://purl.obolibrary.org/obo/DOID_0050639)                                                        |
| `ORDO:51608`    |              1 | [DOID:0050644](http://purl.obolibrary.org/obo/DOID_0050644)                                                        |
| `ORDO:1147`     |              1 | [DOID:0050646](http://purl.obolibrary.org/obo/DOID_0050646)                                                        |
| `ORDO:97120`    |              1 | [DOID:0050646](http://purl.obolibrary.org/obo/DOID_0050646)                                                        |
| `ORDO:1187`     |              1 | [DOID:0050647](http://purl.obolibrary.org/obo/DOID_0050647)                                                        |
| `ORDO:1195`     |              1 | [DOID:0050649](http://purl.obolibrary.org/obo/DOID_0050649)                                                        |
| `ORDO:334`      |              1 | [DOID:0050650](http://purl.obolibrary.org/obo/DOID_0050650)                                                        |
| `ORDO:98722`    |              1 | [DOID:0050651](http://purl.obolibrary.org/obo/DOID_0050651)                                                        |
| `ORDO:1223`     |              1 | [DOID:0050654](http://purl.obolibrary.org/obo/DOID_0050654)                                                        |
| `ORDO:1229`     |              1 | [DOID:0050656](http://purl.obolibrary.org/obo/DOID_0050656)                                                        |
| `ORDO:109`      |              1 | [DOID:0050657](http://purl.obolibrary.org/obo/DOID_0050657)                                                        |
| `ORDO:1243`     |              1 | [DOID:0050661](http://purl.obolibrary.org/obo/DOID_0050661)                                                        |
| `ORDO:99000`    |              1 | [DOID:0050661](http://purl.obolibrary.org/obo/DOID_0050661)                                                        |
| `ORDO:127`      |              1 | [DOID:0050681](http://purl.obolibrary.org/obo/DOID_0050681)                                                        |
| `ORDO:1270`     |              1 | [DOID:0050684](http://purl.obolibrary.org/obo/DOID_0050684)                                                        |
| `ORDO:1293`     |              1 | [DOID:0050690](http://purl.obolibrary.org/obo/DOID_0050690)                                                        |
| `ORDO:79493`    |              1 | [DOID:0050693](http://purl.obolibrary.org/obo/DOID_0050693)                                                        |
| `ORDO:1934`     |              1 | [DOID:0050709](http://purl.obolibrary.org/obo/DOID_0050709)                                                        |
| `ORDO:6`        |              1 | [DOID:0050710](http://purl.obolibrary.org/obo/DOID_0050710)                                                        |
| `ORDO:3213`     |              1 | [DOID:0050757](http://purl.obolibrary.org/obo/DOID_0050757)                                                        |
| `ORDO:2697`     |              1 | [DOID:0050763](http://purl.obolibrary.org/obo/DOID_0050763)                                                        |
| `ORDO:263440`   |              1 | [DOID:0050765](http://purl.obolibrary.org/obo/DOID_0050765)                                                        |
| `ORDO:2388`     |              1 | [DOID:0050766](http://purl.obolibrary.org/obo/DOID_0050766)                                                        |
| `ORDO:2608`     |              1 | [DOID:0050769](http://purl.obolibrary.org/obo/DOID_0050769)                                                        |
| `ORDO:3021`     |              1 | [DOID:0050774](http://purl.obolibrary.org/obo/DOID_0050774)                                                        |
| `ORDO:777`      |              1 | [DOID:0050776](http://purl.obolibrary.org/obo/DOID_0050776)                                                        |
| `ORDO:1172`     |              1 | [DOID:0050950](http://purl.obolibrary.org/obo/DOID_0050950)                                                        |
| `ORDO:69127`    |              1 | [DOID:0060025](http://purl.obolibrary.org/obo/DOID_0060025)                                                        |
| `ORDO:547`      |              1 | [DOID:0060060](http://purl.obolibrary.org/obo/DOID_0060060)                                                        |
| `ORDO:209886`   |              1 | [DOID:0060062](http://purl.obolibrary.org/obo/DOID_0060062)                                                        |
| `ORDO:217330`   |              1 | [DOID:0060062](http://purl.obolibrary.org/obo/DOID_0060062)                                                        |
| `ORDO:70`       |              1 | [DOID:0060160](http://purl.obolibrary.org/obo/DOID_0060160)                                                        |
| `ORDO:306`      |              1 | [DOID:0060169](http://purl.obolibrary.org/obo/DOID_0060169)                                                        |
| `ORDO:65283`    |              1 | [DOID:0060173](http://purl.obolibrary.org/obo/DOID_0060173)                                                        |
| `ORDO:178469`   |              1 | [DOID:0060307](http://purl.obolibrary.org/obo/DOID_0060307)                                                        |
| `ORDO:281097`   |              1 | [DOID:0060655](http://purl.obolibrary.org/obo/DOID_0060655)                                                        |
| `ORDO:1048`     |              1 | [DOID:0060668](http://purl.obolibrary.org/obo/DOID_0060668)                                                        |
| `ORDO:163690`   |              1 | [DOID:0060858](http://purl.obolibrary.org/obo/DOID_0060858)                                                        |
| `ORDO:35698`    |              1 | [DOID:0070329](http://purl.obolibrary.org/obo/DOID_0070329)                                                        |
| `ORDO:1522`     |              1 | [DOID:0080033](http://purl.obolibrary.org/obo/DOID_0080033)                                                        |
| `ORDO:3152`     |              1 | [DOID:0080036](http://purl.obolibrary.org/obo/DOID_0080036)                                                        |
| `ORDO:763`      |              1 | [DOID:0080038](http://purl.obolibrary.org/obo/DOID_0080038)                                                        |
| `ORDO:429`      |              1 | [DOID:0080041](http://purl.obolibrary.org/obo/DOID_0080041)                                                        |
| `ORDO:828`      |              1 | [DOID:0080046](http://purl.obolibrary.org/obo/DOID_0080046)                                                        |
| `ORDO:93437`    |              1 | [DOID:0080049](http://purl.obolibrary.org/obo/DOID_0080049)                                                        |
| `ORDO:2978`     |              1 | [DOID:0080072](http://purl.obolibrary.org/obo/DOID_0080072)                                                        |
| `ORDO:726`      |              1 | [DOID:0080122](http://purl.obolibrary.org/obo/DOID_0080122)                                                        |
| `ORDO:33069`    |              1 | [DOID:0080422](http://purl.obolibrary.org/obo/DOID_0080422)                                                        |
| `ORDO:432`      |              1 | [DOID:0090070](http://purl.obolibrary.org/obo/DOID_0090070)                                                        |
| `ORDO:228346`   |              1 | [DOID:0110731](http://purl.obolibrary.org/obo/DOID_0110731)                                                        |
| `ORDO:385`      |              1 | [DOID:0110734](http://purl.obolibrary.org/obo/DOID_0110734)                                                        |
| `ORDO:352687`   |              1 | [DOID:0111229](http://purl.obolibrary.org/obo/DOID_0111229)                                                        |
| `ORDO:444490`   |              1 | [DOID:0111417](http://purl.obolibrary.org/obo/DOID_0111417)                                                        |
| `ORDO:915`      |              1 | [DOID:0111824](http://purl.obolibrary.org/obo/DOID_0111824)                                                        |
| `ORDO:33364`    |              1 | [DOID:0111866](http://purl.obolibrary.org/obo/DOID_0111866)                                                        |
| `ORDO:652`      |              1 | [DOID:10017](http://purl.obolibrary.org/obo/DOID_10017)                                                            |
| `ORDO:156071`   |              1 | [DOID:10126](http://purl.obolibrary.org/obo/DOID_10126)                                                            |
| `ORDO:548`      |              1 | [DOID:1024](http://purl.obolibrary.org/obo/DOID_1024)                                                              |
| `ORDO:1331`     |              1 | [DOID:10283](http://purl.obolibrary.org/obo/DOID_10283)                                                            |
| `ORDO:67038`    |              1 | [DOID:1040](http://purl.obolibrary.org/obo/DOID_1040)                                                              |
| `ORDO:2345`     |              1 | [DOID:10426](http://purl.obolibrary.org/obo/DOID_10426)                                                            |
| `ORDO:388`      |              1 | [DOID:10487](http://purl.obolibrary.org/obo/DOID_10487)                                                            |
| `ORDO:534`      |              1 | [DOID:1056](http://purl.obolibrary.org/obo/DOID_1056)                                                              |
| `ORDO:512`      |              1 | [DOID:10581](http://purl.obolibrary.org/obo/DOID_10581)                                                            |
| `ORDO:791`      |              1 | [DOID:10584](http://purl.obolibrary.org/obo/DOID_10584)                                                            |
| `ORDO:275555`   |              1 | [DOID:10591](http://purl.obolibrary.org/obo/DOID_10591)                                                            |
| `ORDO:555`      |              1 | [DOID:10608](http://purl.obolibrary.org/obo/DOID_10608)                                                            |
| `ORDO:289157`   |              1 | [DOID:10609](http://purl.obolibrary.org/obo/DOID_10609)                                                            |
| `ORDO:3337`     |              1 | [DOID:1062](http://purl.obolibrary.org/obo/DOID_1062)                                                              |
| `ORDO:3463`     |              1 | [DOID:10632](http://purl.obolibrary.org/obo/DOID_10632)                                                            |
| `ORDO:213`      |              1 | [DOID:1064](http://purl.obolibrary.org/obo/DOID_1064)                                                              |
| `ORDO:440`      |              1 | [DOID:10892](http://purl.obolibrary.org/obo/DOID_10892)                                                            |
| `ORDO:2182`     |              1 | [DOID:10908](http://purl.obolibrary.org/obo/DOID_10908)                                                            |
| `ORDO:2185`     |              1 | [DOID:10908](http://purl.obolibrary.org/obo/DOID_10908)                                                            |
| `ORDO:232`      |              1 | [DOID:10923](http://purl.obolibrary.org/obo/DOID_10923)                                                            |
| `ORDO:210141`   |              1 | [DOID:10970](http://purl.obolibrary.org/obo/DOID_10970)                                                            |
| `ORDO:63`       |              1 | [DOID:10983](http://purl.obolibrary.org/obo/DOID_10983)                                                            |
| `ORDO:295012`   |              1 | [DOID:11193](http://purl.obolibrary.org/obo/DOID_11193)                                                            |
| `ORDO:90025`    |              1 | [DOID:11193](http://purl.obolibrary.org/obo/DOID_11193)                                                            |
| `ORDO:93403`    |              1 | [DOID:11193](http://purl.obolibrary.org/obo/DOID_11193)                                                            |
| `ORDO:2238`     |              1 | [DOID:11199](http://purl.obolibrary.org/obo/DOID_11199)                                                            |
| `ORDO:797`      |              1 | [DOID:11335](http://purl.obolibrary.org/obo/DOID_11335)                                                            |
| `ORDO:98974`    |              1 | [DOID:11555](http://purl.obolibrary.org/obo/DOID_11555)                                                            |
| `ORDO:1416`     |              1 | [DOID:1156](http://purl.obolibrary.org/obo/DOID_1156)                                                              |
| `ORDO:399096`   |              1 | [DOID:11720](http://purl.obolibrary.org/obo/DOID_11720)                                                            |
| `ORDO:5448`     |              1 | [DOID:11720](http://purl.obolibrary.org/obo/DOID_11720)                                                            |
| `ORDO:59135`    |              1 | [DOID:11720](http://purl.obolibrary.org/obo/DOID_11720)                                                            |
| `ORDO:263`      |              1 | [DOID:11724](http://purl.obolibrary.org/obo/DOID_11724)                                                            |
| `ORDO:199`      |              1 | [DOID:11725](http://purl.obolibrary.org/obo/DOID_11725)                                                            |
| `ORDO:261`      |              1 | [DOID:11726](http://purl.obolibrary.org/obo/DOID_11726)                                                            |
| `ORDO:139436`   |              1 | [DOID:11824](http://purl.obolibrary.org/obo/DOID_11824)                                                            |
| `ORDO:739`      |              1 | [DOID:11983](http://purl.obolibrary.org/obo/DOID_11983)                                                            |
| `ORDO:217568`   |              1 | [DOID:11984](http://purl.obolibrary.org/obo/DOID_11984)                                                            |
| `ORDO:264675`   |              1 | [DOID:12120](http://purl.obolibrary.org/obo/DOID_12120)                                                            |
| `ORDO:98878`    |              1 | [DOID:12134](http://purl.obolibrary.org/obo/DOID_12134)                                                            |
| `ORDO:1572`     |              1 | [DOID:12177](http://purl.obolibrary.org/obo/DOID_12177)                                                            |
| `ORDO:2794`     |              1 | [DOID:12185](http://purl.obolibrary.org/obo/DOID_12185)                                                            |
| `ORDO:186`      |              1 | [DOID:12236](http://purl.obolibrary.org/obo/DOID_12236)                                                            |
| `ORDO:194`      |              1 | [DOID:12270](http://purl.obolibrary.org/obo/DOID_12270)                                                            |
| `ORDO:98945`    |              1 | [DOID:12270](http://purl.obolibrary.org/obo/DOID_12270)                                                            |
| `ORDO:666`      |              1 | [DOID:12347](http://purl.obolibrary.org/obo/DOID_12347)                                                            |
| `ORDO:223`      |              1 | [DOID:12387](http://purl.obolibrary.org/obo/DOID_12387)                                                            |
| `ORDO:2134`     |              1 | [DOID:12554](http://purl.obolibrary.org/obo/DOID_12554)                                                            |
| `ORDO:233`      |              1 | [DOID:12557](http://purl.obolibrary.org/obo/DOID_12557)                                                            |
| `ORDO:774`      |              1 | [DOID:1270](http://purl.obolibrary.org/obo/DOID_1270)                                                              |
| `ORDO:655`      |              1 | [DOID:12712](http://purl.obolibrary.org/obo/DOID_12712)                                                            |
| `ORDO:251`      |              1 | [DOID:12721](http://purl.obolibrary.org/obo/DOID_12721)                                                            |
| `ORDO:79213`    |              1 | [DOID:12798](http://purl.obolibrary.org/obo/DOID_12798)                                                            |
| `ORDO:581`      |              1 | [DOID:12801](http://purl.obolibrary.org/obo/DOID_12801)                                                            |
| `ORDO:106`      |              1 | [DOID:12849](http://purl.obolibrary.org/obo/DOID_12849)                                                            |
| `ORDO:217604`   |              1 | [DOID:12930](http://purl.obolibrary.org/obo/DOID_12930)                                                            |
| `ORDO:822`      |              1 | [DOID:12971](http://purl.obolibrary.org/obo/DOID_12971)                                                            |
| `ORDO:2573`     |              1 | [DOID:13099](http://purl.obolibrary.org/obo/DOID_13099)                                                            |
| `ORDO:280679`   |              1 | [DOID:13099](http://purl.obolibrary.org/obo/DOID_13099)                                                            |
| `ORDO:401945`   |              1 | [DOID:13099](http://purl.obolibrary.org/obo/DOID_13099)                                                            |
| `ORDO:79278`    |              1 | [DOID:13270](http://purl.obolibrary.org/obo/DOID_13270)                                                            |
| `ORDO:337`      |              1 | [DOID:13374](http://purl.obolibrary.org/obo/DOID_13374)                                                            |
| `ORDO:85`       |              1 | [DOID:1338](http://purl.obolibrary.org/obo/DOID_1338)                                                              |
| `ORDO:124`      |              1 | [DOID:1339](http://purl.obolibrary.org/obo/DOID_1339)                                                              |
| `ORDO:1860`     |              1 | [DOID:13481](http://purl.obolibrary.org/obo/DOID_13481)                                                            |
| `ORDO:2655`     |              1 | [DOID:13481](http://purl.obolibrary.org/obo/DOID_13481)                                                            |
| `ORDO:93274`    |              1 | [DOID:13481](http://purl.obolibrary.org/obo/DOID_13481)                                                            |
| `ORDO:93275`    |              1 | [DOID:13481](http://purl.obolibrary.org/obo/DOID_13481)                                                            |
| `ORDO:667`      |              1 | [DOID:13533](http://purl.obolibrary.org/obo/DOID_13533)                                                            |
| `ORDO:99879`    |              1 | [DOID:13543](http://purl.obolibrary.org/obo/DOID_13543)                                                            |
| `ORDO:30391`    |              1 | [DOID:13608](http://purl.obolibrary.org/obo/DOID_13608)                                                            |
| `ORDO:84`       |              1 | [DOID:13636](http://purl.obolibrary.org/obo/DOID_13636)                                                            |
| `ORDO:302`      |              1 | [DOID:13777](http://purl.obolibrary.org/obo/DOID_13777)                                                            |
| `ORDO:166282`   |              1 | [DOID:13884](http://purl.obolibrary.org/obo/DOID_13884)                                                            |
| `ORDO:49382`    |              1 | [DOID:13911](http://purl.obolibrary.org/obo/DOID_13911)                                                            |
| `ORDO:73247`    |              1 | [DOID:13922](http://purl.obolibrary.org/obo/DOID_13922)                                                            |
| `ORDO:136`      |              1 | [DOID:13945](http://purl.obolibrary.org/obo/DOID_13945)                                                            |
| `ORDO:1452`     |              1 | [DOID:13994](http://purl.obolibrary.org/obo/DOID_13994)                                                            |
| `ORDO:309015`   |              1 | [DOID:14118](http://purl.obolibrary.org/obo/DOID_14118)                                                            |
| `ORDO:47`       |              1 | [DOID:14179](http://purl.obolibrary.org/obo/DOID_14179)                                                            |
| `ORDO:436`      |              1 | [DOID:14213](http://purl.obolibrary.org/obo/DOID_14213)                                                            |
| `ORDO:217034`   |              1 | [DOID:14227](http://purl.obolibrary.org/obo/DOID_14227)                                                            |
| `ORDO:870`      |              1 | [DOID:14250](http://purl.obolibrary.org/obo/DOID_14250)                                                            |
| `ORDO:908`      |              1 | [DOID:14261](http://purl.obolibrary.org/obo/DOID_14261)                                                            |
| `ORDO:1949`     |              1 | [DOID:14264](http://purl.obolibrary.org/obo/DOID_14264)                                                            |
| `ORDO:500`      |              1 | [DOID:14291](http://purl.obolibrary.org/obo/DOID_14291)                                                            |
| `ORDO:2828`     |              1 | [DOID:14330](http://purl.obolibrary.org/obo/DOID_14330)                                                            |
| `ORDO:94`       |              1 | [DOID:1441](http://purl.obolibrary.org/obo/DOID_1441)                                                              |
| `ORDO:682`      |              1 | [DOID:14451](http://purl.obolibrary.org/obo/DOID_14451)                                                            |
| `ORDO:681`      |              1 | [DOID:14452](http://purl.obolibrary.org/obo/DOID_14452)                                                            |
| `ORDO:94093`    |              1 | [DOID:14464](http://purl.obolibrary.org/obo/DOID_14464)                                                            |
| `ORDO:216`      |              1 | [DOID:14503](http://purl.obolibrary.org/obo/DOID_14503)                                                            |
| `ORDO:79262`    |              1 | [DOID:14503](http://purl.obolibrary.org/obo/DOID_14503)                                                            |
| `ORDO:422`      |              1 | [DOID:14557](http://purl.obolibrary.org/obo/DOID_14557)                                                            |
| `ORDO:950`      |              1 | [DOID:14669](http://purl.obolibrary.org/obo/DOID_14669)                                                            |
| `ORDO:2300`     |              1 | [DOID:14671](http://purl.obolibrary.org/obo/DOID_14671)                                                            |
| `ORDO:782`      |              1 | [DOID:14686](http://purl.obolibrary.org/obo/DOID_14686)                                                            |
| `ORDO:2315`     |              1 | [DOID:14694](http://purl.obolibrary.org/obo/DOID_14694)                                                            |
| `ORDO:3320`     |              1 | [DOID:14699](http://purl.obolibrary.org/obo/DOID_14699)                                                            |
| `ORDO:323`      |              1 | [DOID:14711](http://purl.obolibrary.org/obo/DOID_14711)                                                            |
| `ORDO:93932`    |              1 | [DOID:14711](http://purl.obolibrary.org/obo/DOID_14711)                                                            |
| `ORDO:595`      |              1 | [DOID:14717](http://purl.obolibrary.org/obo/DOID_14717)                                                            |
| `ORDO:596`      |              1 | [DOID:14717](http://purl.obolibrary.org/obo/DOID_14717)                                                            |
| `ORDO:69186`    |              1 | [DOID:14717](http://purl.obolibrary.org/obo/DOID_14717)                                                            |
| `ORDO:69189`    |              1 | [DOID:14717](http://purl.obolibrary.org/obo/DOID_14717)                                                            |
| `ORDO:134`      |              1 | [DOID:14723](http://purl.obolibrary.org/obo/DOID_14723)                                                            |
| `ORDO:1520`     |              1 | [DOID:14737](http://purl.obolibrary.org/obo/DOID_14737)                                                            |
| `ORDO:94083`    |              1 | [DOID:14744](http://purl.obolibrary.org/obo/DOID_14744)                                                            |
| `ORDO:821`      |              1 | [DOID:14748](http://purl.obolibrary.org/obo/DOID_14748)                                                            |
| `ORDO:93108`    |              1 | [DOID:14766](http://purl.obolibrary.org/obo/DOID_14766)                                                            |
| `ORDO:2332`     |              1 | [DOID:14780](http://purl.obolibrary.org/obo/DOID_14780)                                                            |
| `ORDO:65`       |              1 | [DOID:14791](http://purl.obolibrary.org/obo/DOID_14791)                                                            |
| `ORDO:238468`   |              1 | [DOID:14793](http://purl.obolibrary.org/obo/DOID_14793)                                                            |
| `ORDO:586`      |              1 | [DOID:1485](http://purl.obolibrary.org/obo/DOID_1485)                                                              |
| `ORDO:852`      |              1 | [DOID:1588](http://purl.obolibrary.org/obo/DOID_1588)                                                              |
| `ORDO:1480`     |              1 | [DOID:1657](http://purl.obolibrary.org/obo/DOID_1657)                                                              |
| `ORDO:79354`    |              1 | [DOID:1697](http://purl.obolibrary.org/obo/DOID_1697)                                                              |
| `ORDO:1333`     |              1 | [DOID:1793](http://purl.obolibrary.org/obo/DOID_1793)                                                              |
| `ORDO:217074`   |              1 | [DOID:1793](http://purl.obolibrary.org/obo/DOID_1793)                                                              |
| `ORDO:284385`   |              1 | [DOID:1852](http://purl.obolibrary.org/obo/DOID_1852)                                                              |
| `ORDO:1478`     |              1 | [DOID:1882](http://purl.obolibrary.org/obo/DOID_1882)                                                              |
| `ORDO:1465`     |              1 | [DOID:1925](http://purl.obolibrary.org/obo/DOID_1925)                                                              |
| `ORDO:355`      |              1 | [DOID:1926](http://purl.obolibrary.org/obo/DOID_1926)                                                              |
| `ORDO:2377`     |              1 | [DOID:1930](http://purl.obolibrary.org/obo/DOID_1930)                                                              |
| `ORDO:783`      |              1 | [DOID:1933](http://purl.obolibrary.org/obo/DOID_1933)                                                              |
| `ORDO:110`      |              1 | [DOID:1935](http://purl.obolibrary.org/obo/DOID_1935)                                                              |
| `ORDO:83471`    |              1 | [DOID:2012](http://purl.obolibrary.org/obo/DOID_2012)                                                              |
| `ORDO:1334`     |              1 | [DOID:2058](http://purl.obolibrary.org/obo/DOID_2058)                                                              |
| `ORDO:614`      |              1 | [DOID:2106](http://purl.obolibrary.org/obo/DOID_2106)                                                              |
| `ORDO:2092`     |              1 | [DOID:2120](http://purl.obolibrary.org/obo/DOID_2120)                                                              |
| `ORDO:79373`    |              1 | [DOID:2121](http://purl.obolibrary.org/obo/DOID_2121)                                                              |
| `ORDO:99966`    |              1 | [DOID:2129](http://purl.obolibrary.org/obo/DOID_2129)                                                              |
| `ORDO:88661`    |              1 | [DOID:2187](http://purl.obolibrary.org/obo/DOID_2187)                                                              |
| `ORDO:274`      |              1 | [DOID:2217](http://purl.obolibrary.org/obo/DOID_2217)                                                              |
| `ORDO:849`      |              1 | [DOID:2219](http://purl.obolibrary.org/obo/DOID_2219)                                                              |
| `ORDO:3318`     |              1 | [DOID:2224](http://purl.obolibrary.org/obo/DOID_2224)                                                              |
| `ORDO:71493`    |              1 | [DOID:2224](http://purl.obolibrary.org/obo/DOID_2224)                                                              |
| `ORDO:330`      |              1 | [DOID:2231](http://purl.obolibrary.org/obo/DOID_2231)                                                              |
| `ORDO:35689`    |              1 | [DOID:230](http://purl.obolibrary.org/obo/DOID_230)                                                                |
| `ORDO:1531`     |              1 | [DOID:2340](http://purl.obolibrary.org/obo/DOID_2340)                                                              |
| `ORDO:139498`   |              1 | [DOID:2352](http://purl.obolibrary.org/obo/DOID_2352)                                                              |
| `ORDO:309144`   |              1 | [DOID:2368](http://purl.obolibrary.org/obo/DOID_2368)                                                              |
| `ORDO:288`      |              1 | [DOID:2373](http://purl.obolibrary.org/obo/DOID_2373)                                                              |
| `ORDO:213500`   |              1 | [DOID:2394](http://purl.obolibrary.org/obo/DOID_2394)                                                              |
| `ORDO:213517`   |              1 | [DOID:2394](http://purl.obolibrary.org/obo/DOID_2394)                                                              |
| `ORDO:377`      |              1 | [DOID:2512](http://purl.obolibrary.org/obo/DOID_2512)                                                              |
| `ORDO:98818`    |              1 | [DOID:2538](http://purl.obolibrary.org/obo/DOID_2538)                                                              |
| `ORDO:177`      |              1 | [DOID:2580](http://purl.obolibrary.org/obo/DOID_2580)                                                              |
| `ORDO:93442`    |              1 | [DOID:2581](http://purl.obolibrary.org/obo/DOID_2581)                                                              |
| `ORDO:125`      |              1 | [DOID:2717](http://purl.obolibrary.org/obo/DOID_2717)                                                              |
| `ORDO:1775`     |              1 | [DOID:2729](http://purl.obolibrary.org/obo/DOID_2729)                                                              |
| `ORDO:758`      |              1 | [DOID:2738](http://purl.obolibrary.org/obo/DOID_2738)                                                              |
| `ORDO:55881`    |              1 | [DOID:2776](http://purl.obolibrary.org/obo/DOID_2776)                                                              |
| `ORDO:101016`   |              1 | [DOID:2843](http://purl.obolibrary.org/obo/DOID_2843)                                                              |
| `ORDO:374`      |              1 | [DOID:2907](http://purl.obolibrary.org/obo/DOID_2907)                                                              |
| `ORDO:167`      |              1 | [DOID:2935](http://purl.obolibrary.org/obo/DOID_2935)                                                              |
| `ORDO:191`      |              1 | [DOID:2962](http://purl.obolibrary.org/obo/DOID_2962)                                                              |
| `ORDO:90321`    |              1 | [DOID:2962](http://purl.obolibrary.org/obo/DOID_2962)                                                              |
| `ORDO:90322`    |              1 | [DOID:2962](http://purl.obolibrary.org/obo/DOID_2962)                                                              |
| `ORDO:90324`    |              1 | [DOID:2962](http://purl.obolibrary.org/obo/DOID_2962)                                                              |
| `ORDO:416`      |              1 | [DOID:2977](http://purl.obolibrary.org/obo/DOID_2977)                                                              |
| `ORDO:342`      |              1 | [DOID:2987](http://purl.obolibrary.org/obo/DOID_2987)                                                              |
| `ORDO:524`      |              1 | [DOID:3012](http://purl.obolibrary.org/obo/DOID_3012)                                                              |
| `ORDO:182067`   |              1 | [DOID:3070](http://purl.obolibrary.org/obo/DOID_3070)                                                              |
| `ORDO:101330`   |              1 | [DOID:3132](http://purl.obolibrary.org/obo/DOID_3132)                                                              |
| `ORDO:100924`   |              1 | [DOID:3133](http://purl.obolibrary.org/obo/DOID_3133)                                                              |
| `ORDO:209`      |              1 | [DOID:3144](http://purl.obolibrary.org/obo/DOID_3144)                                                              |
| `ORDO:607`      |              1 | [DOID:3191](http://purl.obolibrary.org/obo/DOID_3191)                                                              |
| `ORDO:702`      |              1 | [DOID:3210](http://purl.obolibrary.org/obo/DOID_3210)                                                              |
| `ORDO:99757`    |              1 | [DOID:3246](http://purl.obolibrary.org/obo/DOID_3246)                                                              |
| `ORDO:2314`     |              1 | [DOID:3261](http://purl.obolibrary.org/obo/DOID_3261)                                                              |
| `ORDO:2884`     |              1 | [DOID:3263](http://purl.obolibrary.org/obo/DOID_3263)                                                              |
| `ORDO:379`      |              1 | [DOID:3265](http://purl.obolibrary.org/obo/DOID_3265)                                                              |
| `ORDO:3280`     |              1 | [DOID:327](http://purl.obolibrary.org/obo/DOID_327)                                                                |
| `ORDO:538`      |              1 | [DOID:3319](http://purl.obolibrary.org/obo/DOID_3319)                                                              |
| `ORDO:803`      |              1 | [DOID:332](http://purl.obolibrary.org/obo/DOID_332)                                                                |
| `ORDO:668`      |              1 | [DOID:3347](http://purl.obolibrary.org/obo/DOID_3347)                                                              |
| `ORDO:678`      |              1 | [DOID:3389](http://purl.obolibrary.org/obo/DOID_3389)                                                              |
| `ORDO:611`      |              1 | [DOID:3429](http://purl.obolibrary.org/obo/DOID_3429)                                                              |
| `ORDO:648`      |              1 | [DOID:3490](http://purl.obolibrary.org/obo/DOID_3490)                                                              |
| `ORDO:590`      |              1 | [DOID:3635](http://purl.obolibrary.org/obo/DOID_3635)                                                              |
| `ORDO:79243`    |              1 | [DOID:3649](http://purl.obolibrary.org/obo/DOID_3649)                                                              |
| `ORDO:506`      |              1 | [DOID:3652](http://purl.obolibrary.org/obo/DOID_3652)                                                              |
| `ORDO:231531`   |              1 | [DOID:3753](http://purl.obolibrary.org/obo/DOID_3753)                                                              |
| `ORDO:231537`   |              1 | [DOID:3753](http://purl.obolibrary.org/obo/DOID_3753)                                                              |
| `ORDO:280663`   |              1 | [DOID:3753](http://purl.obolibrary.org/obo/DOID_3753)                                                              |
| `ORDO:79430`    |              1 | [DOID:3753](http://purl.obolibrary.org/obo/DOID_3753)                                                              |
| `ORDO:745`      |              1 | [DOID:3756](http://purl.obolibrary.org/obo/DOID_3756)                                                              |
| `ORDO:2140`     |              1 | [DOID:3827](http://purl.obolibrary.org/obo/DOID_3827)                                                              |
| `ORDO:2869`     |              1 | [DOID:3852](http://purl.obolibrary.org/obo/DOID_3852)                                                              |
| `ORDO:144`      |              1 | [DOID:3883](http://purl.obolibrary.org/obo/DOID_3883)                                                              |
| `ORDO:740`      |              1 | [DOID:3911](http://purl.obolibrary.org/obo/DOID_3911)                                                              |
| `ORDO:75249`    |              1 | [DOID:397](http://purl.obolibrary.org/obo/DOID_397)                                                                |
| `ORDO:157850`   |              1 | [DOID:3981](http://purl.obolibrary.org/obo/DOID_3981)                                                              |
| `ORDO:95429`    |              1 | [DOID:4028](http://purl.obolibrary.org/obo/DOID_4028)                                                              |
| `ORDO:49042`    |              1 | [DOID:4154](http://purl.obolibrary.org/obo/DOID_4154)                                                              |
| `ORDO:79365`    |              1 | [DOID:420](http://purl.obolibrary.org/obo/DOID_420)                                                                |
| `ORDO:370334`   |              1 | [DOID:4232](http://purl.obolibrary.org/obo/DOID_4232)                                                              |
| `ORDO:163699`   |              1 | [DOID:4239](http://purl.obolibrary.org/obo/DOID_4239)                                                              |
| `ORDO:185`      |              1 | [DOID:4297](http://purl.obolibrary.org/obo/DOID_4297)                                                              |
| `ORDO:320`      |              1 | [DOID:4367](http://purl.obolibrary.org/obo/DOID_4367)                                                              |
| `ORDO:279`      |              1 | [DOID:4448](http://purl.obolibrary.org/obo/DOID_4448)                                                              |
| `ORDO:217071`   |              1 | [DOID:4450](http://purl.obolibrary.org/obo/DOID_4450)                                                              |
| `ORDO:235936`   |              1 | [DOID:446](http://purl.obolibrary.org/obo/DOID_446)                                                                |
| `ORDO:2108`     |              1 | [DOID:4534](http://purl.obolibrary.org/obo/DOID_4534)                                                              |
| `ORDO:55654`    |              1 | [DOID:4535](http://purl.obolibrary.org/obo/DOID_4535)                                                              |
| `ORDO:2162`     |              1 | [DOID:4621](http://purl.obolibrary.org/obo/DOID_4621)                                                              |
| `ORDO:296`      |              1 | [DOID:4624](http://purl.obolibrary.org/obo/DOID_4624)                                                              |
| `ORDO:304`      |              1 | [DOID:4644](http://purl.obolibrary.org/obo/DOID_4644)                                                              |
| `ORDO:754`      |              1 | [DOID:4674](http://purl.obolibrary.org/obo/DOID_4674)                                                              |
| `ORDO:862`      |              1 | [DOID:4990](http://purl.obolibrary.org/obo/DOID_4990)                                                              |
| `ORDO:137`      |              1 | [DOID:5212](http://purl.obolibrary.org/obo/DOID_5212)                                                              |
| `ORDO:95159`    |              1 | [DOID:5230](http://purl.obolibrary.org/obo/DOID_5230)                                                              |
| `ORDO:3103`     |              1 | [DOID:5325](http://purl.obolibrary.org/obo/DOID_5325)                                                              |
| `ORDO:99967`    |              1 | [DOID:5363](http://purl.obolibrary.org/obo/DOID_5363)                                                              |
| `ORDO:280110`   |              1 | [DOID:5408](http://purl.obolibrary.org/obo/DOID_5408)                                                              |
| `ORDO:619`      |              1 | [DOID:5426](http://purl.obolibrary.org/obo/DOID_5426)                                                              |
| `ORDO:116`      |              1 | [DOID:5572](http://purl.obolibrary.org/obo/DOID_5572)                                                              |
| `ORDO:902`      |              1 | [DOID:5688](http://purl.obolibrary.org/obo/DOID_5688)                                                              |
| `ORDO:98673`    |              1 | [DOID:5723](http://purl.obolibrary.org/obo/DOID_5723)                                                              |
| `ORDO:760`      |              1 | [DOID:5813](http://purl.obolibrary.org/obo/DOID_5813)                                                              |
| `ORDO:101972`   |              1 | [DOID:628](http://purl.obolibrary.org/obo/DOID_628)                                                                |
| `ORDO:3426`     |              1 | [DOID:6406](http://purl.obolibrary.org/obo/DOID_6406)                                                              |
| `ORDO:201`      |              1 | [DOID:6457](http://purl.obolibrary.org/obo/DOID_6457)                                                              |
| `ORDO:2968`     |              1 | [DOID:6612](http://purl.obolibrary.org/obo/DOID_6612)                                                              |
| `ORDO:3261`     |              1 | [DOID:6688](http://purl.obolibrary.org/obo/DOID_6688)                                                              |
| `ORDO:99772`    |              1 | [DOID:674](http://purl.obolibrary.org/obo/DOID_674)                                                                |
| `ORDO:92`       |              1 | [DOID:676](http://purl.obolibrary.org/obo/DOID_676)                                                                |
| `ORDO:683`      |              1 | [DOID:678](http://purl.obolibrary.org/obo/DOID_678)                                                                |
| `ORDO:88673`    |              1 | [DOID:684](http://purl.obolibrary.org/obo/DOID_684)                                                                |
| `ORDO:1635`     |              1 | [DOID:701](http://purl.obolibrary.org/obo/DOID_701)                                                                |
| `ORDO:825`      |              1 | [DOID:7147](http://purl.obolibrary.org/obo/DOID_7147)                                                              |
| `ORDO:647`      |              1 | [DOID:7400](http://purl.obolibrary.org/obo/DOID_7400)                                                              |
| `ORDO:635`      |              1 | [DOID:769](http://purl.obolibrary.org/obo/DOID_769)                                                                |
| `ORDO:99819`    |              1 | [DOID:7998](http://purl.obolibrary.org/obo/DOID_7998)                                                              |
| `ORDO:280133`   |              1 | [DOID:8354](http://purl.obolibrary.org/obo/DOID_8354)                                                              |
| `ORDO:50`       |              1 | [DOID:8461](http://purl.obolibrary.org/obo/DOID_8461)                                                              |
| `ORDO:423`      |              1 | [DOID:8545](http://purl.obolibrary.org/obo/DOID_8545)                                                              |
| `ORDO:521`      |              1 | [DOID:8552](http://purl.obolibrary.org/obo/DOID_8552)                                                              |
| `ORDO:98293`    |              1 | [DOID:8567](http://purl.obolibrary.org/obo/DOID_8567)                                                              |
| `ORDO:543`      |              1 | [DOID:8584](http://purl.obolibrary.org/obo/DOID_8584)                                                              |
| `ORDO:93921`    |              1 | [DOID:8712](http://purl.obolibrary.org/obo/DOID_8712)                                                              |
| `ORDO:730`      |              1 | [DOID:898](http://purl.obolibrary.org/obo/DOID_898)                                                                |
| `ORDO:912`      |              1 | [DOID:905](http://purl.obolibrary.org/obo/DOID_905)                                                                |
| `ORDO:536`      |              1 | [DOID:9074](http://purl.obolibrary.org/obo/DOID_9074)                                                              |
| `ORDO:507`      |              1 | [DOID:9146](http://purl.obolibrary.org/obo/DOID_9146)                                                              |
| `ORDO:52`       |              1 | [DOID:9245](http://purl.obolibrary.org/obo/DOID_9245)                                                              |
| `ORDO:85458`    |              1 | [DOID:9246](http://purl.obolibrary.org/obo/DOID_9246)                                                              |
| `ORDO:282`      |              1 | [DOID:9255](http://purl.obolibrary.org/obo/DOID_9255)                                                              |
| `ORDO:3440`     |              1 | [DOID:9258](http://purl.obolibrary.org/obo/DOID_9258)                                                              |
| `ORDO:895`      |              1 | [DOID:9258](http://purl.obolibrary.org/obo/DOID_9258)                                                              |
| `ORDO:150`      |              1 | [DOID:9261](http://purl.obolibrary.org/obo/DOID_9261)                                                              |
| `ORDO:394`      |              1 | [DOID:9263](http://purl.obolibrary.org/obo/DOID_9263)                                                              |
| `ORDO:214`      |              1 | [DOID:9266](http://purl.obolibrary.org/obo/DOID_9266)                                                              |
| `ORDO:511`      |              1 | [DOID:9269](http://purl.obolibrary.org/obo/DOID_9269)                                                              |
| `ORDO:56`       |              1 | [DOID:9270](http://purl.obolibrary.org/obo/DOID_9270)                                                              |
| `ORDO:2203`     |              1 | [DOID:9274](http://purl.obolibrary.org/obo/DOID_9274)                                                              |
| `ORDO:716`      |              1 | [DOID:9281](http://purl.obolibrary.org/obo/DOID_9281)                                                              |
| `ORDO:95494`    |              1 | [DOID:9406](http://purl.obolibrary.org/obo/DOID_9406)                                                              |
| `ORDO:2614`     |              1 | [DOID:9467](http://purl.obolibrary.org/obo/DOID_9467)                                                              |
| `ORDO:633`      |              1 | [DOID:9521](http://purl.obolibrary.org/obo/DOID_9521)                                                              |
| `ORDO:29073`    |              1 | [DOID:9538](http://purl.obolibrary.org/obo/DOID_9538)                                                              |
| `ORDO:244`      |              1 | [DOID:9562](http://purl.obolibrary.org/obo/DOID_9562)                                                              |
| `ORDO:60033`    |              1 | [DOID:9563](http://purl.obolibrary.org/obo/DOID_9563)                                                              |
| `ORDO:289365`   |              1 | [DOID:9620](http://purl.obolibrary.org/obo/DOID_9620)                                                              |
| `ORDO:211062`   |              1 | [DOID:963](http://purl.obolibrary.org/obo/DOID_963)                                                                |
| `ORDO:651`      |              1 | [DOID:9649](http://purl.obolibrary.org/obo/DOID_9649)                                                              |
| `ORDO:329211`   |              1 | [DOID:9719](http://purl.obolibrary.org/obo/DOID_9719)                                                              |
| `ORDO:180`      |              1 | [DOID:9821](http://purl.obolibrary.org/obo/DOID_9821)                                                              |
| `ORDO:98895`    |              1 | [DOID:9883](http://purl.obolibrary.org/obo/DOID_9883)                                                              |
| `ORDO:513`      |              1 | [DOID:9952](http://purl.obolibrary.org/obo/DOID_9952)                                                              |
| `ORDO:2248`     |              1 | [DOID:9955](http://purl.obolibrary.org/obo/DOID_9955)                                                              |
| `ORDO:168956`   |              1 | [DOID:999](http://purl.obolibrary.org/obo/DOID_999)                                                                |

## `Wikipedia`: Wikipedia

Overall, there were 7 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                        |   usages_count | usages                                                  |
|--------------------------------------|----------------|---------------------------------------------------------|
| `Wikipedia:Ligand_(biochemistry)`    |              1 | [GO:0005102](http://purl.obolibrary.org/obo/GO_0005102) |
| `Wikipedia:Binding_(molecular)`      |              1 | [GO:0005488](http://purl.obolibrary.org/obo/GO_0005488) |
| `Wikipedia:Transcription_(genetics)` |              1 | [GO:0006351](http://purl.obolibrary.org/obo/GO_0006351) |
| `Wikipedia:Translation_(genetics)`   |              1 | [GO:0006412](http://purl.obolibrary.org/obo/GO_0006412) |
| `Wikipedia:Autophagy_(cellular)`     |              1 | [GO:0006914](http://purl.obolibrary.org/obo/GO_0006914) |
| `Wikipedia:Regeneration_(biology)`   |              1 | [GO:0031099](http://purl.obolibrary.org/obo/GO_0031099) |
| `Wikipedia:Bleb_(cell_biology)`      |              1 | [GO:0032059](http://purl.obolibrary.org/obo/GO_0032059) |

