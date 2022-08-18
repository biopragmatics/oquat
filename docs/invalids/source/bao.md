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

## `NIF_Subcellular`: NIF Standard Ontology: Subcellular Entities

Overall, there were 13 invalid
xrefs to external prefixed with `NIF_Subcellular` (standardized to Bioregistry
prefix [`nlx.sub`](https://bioregistry.io/nlx.sub)) that
did not match the standard pattern `^\d+$`.

| external_xref                   |   usages_count | usages                                                  |
|---------------------------------|----------------|---------------------------------------------------------|
| `NIF_Subcellular:sao1702920020` |              1 | [GO:0005634](http://purl.obolibrary.org/obo/GO_0005634) |
| `NIF_Subcellular:sao1860313010` |              1 | [GO:0005739](http://purl.obolibrary.org/obo/GO_0005739) |
| `NIF_Subcellular:sao585356902`  |              1 | [GO:0005764](http://purl.obolibrary.org/obo/GO_0005764) |
| `NIF_Subcellular:sao8663416959` |              1 | [GO:0005776](http://purl.obolibrary.org/obo/GO_0005776) |
| `NIF_Subcellular:sao1036339110` |              1 | [GO:0005783](http://purl.obolibrary.org/obo/GO_0005783) |
| `NIF_Subcellular:sao451912436`  |              1 | [GO:0005794](http://purl.obolibrary.org/obo/GO_0005794) |
| `NIF_Subcellular:sao101633890`  |              1 | [GO:0005829](http://purl.obolibrary.org/obo/GO_0005829) |
| `NIF_Subcellular:sao1663586795` |              1 | [GO:0005886](http://purl.obolibrary.org/obo/GO_0005886) |
| `NIF_Subcellular:sao1770195789` |              1 | [GO:0030424](http://purl.obolibrary.org/obo/GO_0030424) |
| `NIF_Subcellular:sao867568886`  |              1 | [GO:0043005](http://purl.obolibrary.org/obo/GO_0043005) |
| `NIF_Subcellular:sao1470140754` |              1 | [GO:0044303](http://purl.obolibrary.org/obo/GO_0044303) |
| `NIF_Subcellular:sao884265541`  |              1 | [GO:0044307](http://purl.obolibrary.org/obo/GO_0044307) |
| `NIF_Subcellular:sao707332678`  |              1 | [GO:1901589](http://purl.obolibrary.org/obo/GO_1901589) |

## `NIFSTD`: NIF Standard Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `NIFSTD` (standardized to Bioregistry
prefix [`nif.std`](https://bioregistry.io/nif.std)) that
did not match the standard pattern `^BAMSC\d+$`.

| external_xref        |   usages_count | usages                                              |
|----------------------|----------------|-----------------------------------------------------|
| `NIFSTD:birnlex_228` |              1 | [EFO:0001272](http://www.ebi.ac.uk/efo/EFO_0001272) |
| `NIFSTD:birnlex_681` |              1 | [EFO:0001272](http://www.ebi.ac.uk/efo/EFO_0001272) |

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

