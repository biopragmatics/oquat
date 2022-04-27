# bao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `bao`.


## `FBdv`: Drosophila development

Overall, there were 1 invalid
xrefs to external prefixed with `FBdv` (standardized to Bioregistry
prefix [`fbdv`](https://bioregistry.io/fbdv)) that
did not match the standard pattern `^\d{8}$`.

| external_xref              |   usages_count | usages                                                                       |
|----------------------------|----------------|------------------------------------------------------------------------------|
| `FBdv:('FBdv', '0005333')` |              1 | [http://www.ebi.ac.uk/efo/EFO_0001323](http://www.ebi.ac.uk/efo/EFO_0001323) |

## `ICDO`: International Classification of Diseases for Oncology

Overall, there were 8 invalid
xrefs to external prefixed with `ICDO` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref              |   usages_count | usages                                                                               |
|----------------------------|----------------|--------------------------------------------------------------------------------------|
| `ICDO:('ICDO', 'M8000/3')` |              1 | [http://purl.obolibrary.org/obo/DOID_162](http://purl.obolibrary.org/obo/DOID_162)   |
| `ICDO:('ICDO', 'M8960/3')` |              1 | [http://purl.obolibrary.org/obo/DOID_2154](http://purl.obolibrary.org/obo/DOID_2154) |
| `ICDO:('ICDO', 'M9400/3')` |              1 | [http://purl.obolibrary.org/obo/DOID_3069](http://purl.obolibrary.org/obo/DOID_3069) |
| `ICDO:('ICDO', 'M9380/3')` |              1 | [http://purl.obolibrary.org/obo/DOID_3070](http://purl.obolibrary.org/obo/DOID_3070) |
| `ICDO:('ICDO', 'M9530/3')` |              1 | [http://purl.obolibrary.org/obo/DOID_3565](http://purl.obolibrary.org/obo/DOID_3565) |
| `ICDO:('ICDO', 'M8170/3')` |              1 | [http://purl.obolibrary.org/obo/DOID_684](http://purl.obolibrary.org/obo/DOID_684)   |
| `ICDO:('ICDO', 'M8970/3')` |              1 | [http://purl.obolibrary.org/obo/DOID_687](http://purl.obolibrary.org/obo/DOID_687)   |
| `ICDO:('ICDO', 'M9500/3')` |              1 | [http://purl.obolibrary.org/obo/DOID_769](http://purl.obolibrary.org/obo/DOID_769)   |

## `KEGG`: Kyoto Encyclopedia of Genes and Genomes

Overall, there were 34 invalid
xrefs to external prefixed with `KEGG` (standardized to Bioregistry
prefix [`kegg`](https://bioregistry.io/kegg)) that
did not match the standard pattern `^([CHDEGTMKR]\d+)|(\w+:[\w\d\.-]*)|([a-z]{3,5})|(\w{2,4}\d{5})$`.

| external_xref            |   usages_count | usages                                                                                                                                                                           |
|--------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `KEGG:('KEGG', '05321')` |              2 | [http://purl.obolibrary.org/obo/DOID_0050589](http://purl.obolibrary.org/obo/DOID_0050589), [http://purl.obolibrary.org/obo/DOID_9778](http://purl.obolibrary.org/obo/DOID_9778) |
| `KEGG:('KEGG', '04950')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050524](http://purl.obolibrary.org/obo/DOID_0050524)                                                                                       |
| `KEGG:('KEGG', '05034')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050741](http://purl.obolibrary.org/obo/DOID_0050741)                                                                                       |
| `KEGG:('KEGG', '05143')` |              1 | [http://purl.obolibrary.org/obo/DOID_10112](http://purl.obolibrary.org/obo/DOID_10112)                                                                                           |
| `KEGG:('KEGG', '05215')` |              1 | [http://purl.obolibrary.org/obo/DOID_10283](http://purl.obolibrary.org/obo/DOID_10283)                                                                                           |
| `KEGG:('KEGG', '05010')` |              1 | [http://purl.obolibrary.org/obo/DOID_10652](http://purl.obolibrary.org/obo/DOID_10652)                                                                                           |
| `KEGG:('KEGG', '05219')` |              1 | [http://purl.obolibrary.org/obo/DOID_11054](http://purl.obolibrary.org/obo/DOID_11054)                                                                                           |
| `KEGG:('KEGG', '05133')` |              1 | [http://purl.obolibrary.org/obo/DOID_1116](http://purl.obolibrary.org/obo/DOID_1116)                                                                                             |
| `KEGG:('KEGG', '05410')` |              1 | [http://purl.obolibrary.org/obo/DOID_11984](http://purl.obolibrary.org/obo/DOID_11984)                                                                                           |
| `KEGG:('KEGG', '05142')` |              1 | [http://purl.obolibrary.org/obo/DOID_12140](http://purl.obolibrary.org/obo/DOID_12140)                                                                                           |
| `KEGG:('KEGG', '05131')` |              1 | [http://purl.obolibrary.org/obo/DOID_12385](http://purl.obolibrary.org/obo/DOID_12385)                                                                                           |
| `KEGG:('KEGG', '05016')` |              1 | [http://purl.obolibrary.org/obo/DOID_12858](http://purl.obolibrary.org/obo/DOID_12858)                                                                                           |
| `KEGG:('KEGG', '05414')` |              1 | [http://purl.obolibrary.org/obo/DOID_12930](http://purl.obolibrary.org/obo/DOID_12930)                                                                                           |
| `KEGG:('KEGG', '05213')` |              1 | [http://purl.obolibrary.org/obo/DOID_1380](http://purl.obolibrary.org/obo/DOID_1380)                                                                                             |
| `KEGG:('KEGG', '05012')` |              1 | [http://purl.obolibrary.org/obo/DOID_14330](http://purl.obolibrary.org/obo/DOID_14330)                                                                                           |
| `KEGG:('KEGG', '05216')` |              1 | [http://purl.obolibrary.org/obo/DOID_1781](http://purl.obolibrary.org/obo/DOID_1781)                                                                                             |
| `KEGG:('KEGG', '05212')` |              1 | [http://purl.obolibrary.org/obo/DOID_1793](http://purl.obolibrary.org/obo/DOID_1793)                                                                                             |
| `KEGG:('KEGG', '05218')` |              1 | [http://purl.obolibrary.org/obo/DOID_1909](http://purl.obolibrary.org/obo/DOID_1909)                                                                                             |
| `KEGG:('KEGG', '05217')` |              1 | [http://purl.obolibrary.org/obo/DOID_2513](http://purl.obolibrary.org/obo/DOID_2513)                                                                                             |
| `KEGG:('KEGG', '05310')` |              1 | [http://purl.obolibrary.org/obo/DOID_2841](http://purl.obolibrary.org/obo/DOID_2841)                                                                                             |
| `KEGG:('KEGG', '05214')` |              1 | [http://purl.obolibrary.org/obo/DOID_3070](http://purl.obolibrary.org/obo/DOID_3070)                                                                                             |
| `KEGG:('KEGG', '05014')` |              1 | [http://purl.obolibrary.org/obo/DOID_332](http://purl.obolibrary.org/obo/DOID_332)                                                                                               |
| `KEGG:('KEGG', '05223')` |              1 | [http://purl.obolibrary.org/obo/DOID_3908](http://purl.obolibrary.org/obo/DOID_3908)                                                                                             |
| `KEGG:('KEGG', '05222')` |              1 | [http://purl.obolibrary.org/obo/DOID_5409](http://purl.obolibrary.org/obo/DOID_5409)                                                                                             |
| `KEGG:('KEGG', '05340')` |              1 | [http://purl.obolibrary.org/obo/DOID_612](http://purl.obolibrary.org/obo/DOID_612)                                                                                               |
| `KEGG:('KEGG', '05020')` |              1 | [http://purl.obolibrary.org/obo/DOID_649](http://purl.obolibrary.org/obo/DOID_649)                                                                                               |
| `KEGG:('KEGG', '05323')` |              1 | [http://purl.obolibrary.org/obo/DOID_7148](http://purl.obolibrary.org/obo/DOID_7148)                                                                                             |
| `KEGG:('KEGG', '05416')` |              1 | [http://purl.obolibrary.org/obo/DOID_820](http://purl.obolibrary.org/obo/DOID_820)                                                                                               |
| `KEGG:('KEGG', '05220')` |              1 | [http://purl.obolibrary.org/obo/DOID_8552](http://purl.obolibrary.org/obo/DOID_8552)                                                                                             |
| `KEGG:('KEGG', '05322')` |              1 | [http://purl.obolibrary.org/obo/DOID_9074](http://purl.obolibrary.org/obo/DOID_9074)                                                                                             |
| `KEGG:('KEGG', '05221')` |              1 | [http://purl.obolibrary.org/obo/DOID_9119](http://purl.obolibrary.org/obo/DOID_9119)                                                                                             |
| `KEGG:('KEGG', '05210')` |              1 | [http://purl.obolibrary.org/obo/DOID_9256](http://purl.obolibrary.org/obo/DOID_9256)                                                                                             |
| `KEGG:('KEGG', '04930')` |              1 | [http://purl.obolibrary.org/obo/DOID_9352](http://purl.obolibrary.org/obo/DOID_9352)                                                                                             |

## `MESH`: Medical Subject Headings

Overall, there were 6 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                          |   usages_count | usages                                                                                         |
|----------------------------------------|----------------|------------------------------------------------------------------------------------------------|
| `MESH:('MESH', 'A03.492.411')`         |              1 | [http://purl.obolibrary.org/obo/UBERON_0000160](http://purl.obolibrary.org/obo/UBERON_0000160) |
| `MESH:('MESH', 'A03.492.766')`         |              1 | [http://purl.obolibrary.org/obo/UBERON_0000945](http://purl.obolibrary.org/obo/UBERON_0000945) |
| `MESH:('MESH', 'A03.365')`             |              1 | [http://purl.obolibrary.org/obo/UBERON_0001043](http://purl.obolibrary.org/obo/UBERON_0001043) |
| `MESH:('MESH', 'A05.810.161')`         |              1 | [http://purl.obolibrary.org/obo/UBERON_0001255](http://purl.obolibrary.org/obo/UBERON_0001255) |
| `MESH:('MESH', 'A03.492.411.620.270')` |              1 | [http://purl.obolibrary.org/obo/UBERON_0002114](http://purl.obolibrary.org/obo/UBERON_0002114) |
| `MESH:('MESH', 'A12.207.630')`         |              1 | [http://purl.obolibrary.org/obo/UBERON_0002391](http://purl.obolibrary.org/obo/UBERON_0002391) |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `ncithesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                                          |   usages_count | usages                                                                                         |
|--------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------|
| `ncithesaurus:('ncithesaurus', 'Developmental_Stage')` |              1 | [http://purl.obolibrary.org/obo/UBERON_0000105](http://purl.obolibrary.org/obo/UBERON_0000105) |

## `OMIM`: Online Mendelian Inheritance in Man

Overall, there were 120 invalid
xrefs to external prefixed with `OMIM` (standardized to Bioregistry
prefix [`omim`](https://bioregistry.io/omim)) that
did not match the standard pattern `^\d+$`.

| external_xref               |   usages_count | usages                                                                                     |
|-----------------------------|----------------|--------------------------------------------------------------------------------------------|
| `OMIM:('OMIM', 'PS267700')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050120](http://purl.obolibrary.org/obo/DOID_0050120) |
| `OMIM:('OMIM', 'PS275200')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050328](http://purl.obolibrary.org/obo/DOID_0050328) |
| `OMIM:('OMIM', 'PS175100')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050424](http://purl.obolibrary.org/obo/DOID_0050424) |
| `OMIM:('OMIM', 'PS107970')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050431](http://purl.obolibrary.org/obo/DOID_0050431) |
| `OMIM:('OMIM', 'PS276900')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050439](http://purl.obolibrary.org/obo/DOID_0050439) |
| `OMIM:('OMIM', 'PS167200')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050449](http://purl.obolibrary.org/obo/DOID_0050449) |
| `OMIM:('OMIM', 'PS601144')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050451](http://purl.obolibrary.org/obo/DOID_0050451) |
| `OMIM:('OMIM', 'PS133200')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050467](http://purl.obolibrary.org/obo/DOID_0050467) |
| `OMIM:('OMIM', 'PS310500')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050534](http://purl.obolibrary.org/obo/DOID_0050534) |
| `OMIM:('OMIM', 'PS133780')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050535](http://purl.obolibrary.org/obo/DOID_0050535) |
| `OMIM:('OMIM', 'PS162400')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050548](http://purl.obolibrary.org/obo/DOID_0050548) |
| `OMIM:('OMIM', 'PS304500')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050566](http://purl.obolibrary.org/obo/DOID_0050566) |
| `OMIM:('OMIM', 'PS119530')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050567](http://purl.obolibrary.org/obo/DOID_0050567) |
| `OMIM:('OMIM', 'PS210600')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050569](http://purl.obolibrary.org/obo/DOID_0050569) |
| `OMIM:('OMIM', 'PS600721')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050575](http://purl.obolibrary.org/obo/DOID_0050575) |
| `OMIM:('OMIM', 'PS218330')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050577](http://purl.obolibrary.org/obo/DOID_0050577) |
| `OMIM:('OMIM', 'PS613155')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050588](http://purl.obolibrary.org/obo/DOID_0050588) |
| `OMIM:('OMIM', 'PS266600')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050589](http://purl.obolibrary.org/obo/DOID_0050589) |
| `OMIM:('OMIM', 'PS202700')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050590](http://purl.obolibrary.org/obo/DOID_0050590) |
| `OMIM:('OMIM', 'PS208500')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050592](http://purl.obolibrary.org/obo/DOID_0050592) |
| `OMIM:('OMIM', 'PS203100')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050632](http://purl.obolibrary.org/obo/DOID_0050632) |
| `OMIM:('OMIM', 'PS608583')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050650](http://purl.obolibrary.org/obo/DOID_0050650) |
| `OMIM:('OMIM', 'PS211530')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050694](http://purl.obolibrary.org/obo/DOID_0050694) |
| `OMIM:('OMIM', 'PS308350')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050709](http://purl.obolibrary.org/obo/DOID_0050709) |
| `OMIM:('OMIM', 'PS210200')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050710](http://purl.obolibrary.org/obo/DOID_0050710) |
| `OMIM:('OMIM', 'PS607426')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050730](http://purl.obolibrary.org/obo/DOID_0050730) |
| `OMIM:('OMIM', 'PS208085')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050763](http://purl.obolibrary.org/obo/DOID_0050763) |
| `OMIM:('OMIM', 'PS168000')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050773](http://purl.obolibrary.org/obo/DOID_0050773) |
| `OMIM:('OMIM', 'PS309530')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050776](http://purl.obolibrary.org/obo/DOID_0050776) |
| `OMIM:('OMIM', 'PS213200')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050950](http://purl.obolibrary.org/obo/DOID_0050950) |
| `OMIM:('OMIM', 'PS156200')` |              1 | [http://purl.obolibrary.org/obo/DOID_0060307](http://purl.obolibrary.org/obo/DOID_0060307) |
| `OMIM:('OMIM', 'PS309510')` |              1 | [http://purl.obolibrary.org/obo/DOID_0060309](http://purl.obolibrary.org/obo/DOID_0060309) |
| `OMIM:('OMIM', 'PS605552')` |              1 | [http://purl.obolibrary.org/obo/DOID_0060611](http://purl.obolibrary.org/obo/DOID_0060611) |
| `OMIM:('OMIM', 'PS242300')` |              1 | [http://purl.obolibrary.org/obo/DOID_0060655](http://purl.obolibrary.org/obo/DOID_0060655) |
| `OMIM:('OMIM', 'PS312080')` |              1 | [http://purl.obolibrary.org/obo/DOID_0060786](http://purl.obolibrary.org/obo/DOID_0060786) |
| `OMIM:('OMIM', 'PS603041')` |              1 | [http://purl.obolibrary.org/obo/DOID_0070329](http://purl.obolibrary.org/obo/DOID_0070329) |
| `OMIM:('OMIM', 'PS123000')` |              1 | [http://purl.obolibrary.org/obo/DOID_0080033](http://purl.obolibrary.org/obo/DOID_0080033) |
| `OMIM:('OMIM', 'PS200600')` |              1 | [http://purl.obolibrary.org/obo/DOID_0080043](http://purl.obolibrary.org/obo/DOID_0080043) |
| `OMIM:('OMIM', 'PS108300')` |              1 | [http://purl.obolibrary.org/obo/DOID_0080046](http://purl.obolibrary.org/obo/DOID_0080046) |
| `OMIM:('OMIM', 'PS173900')` |              1 | [http://purl.obolibrary.org/obo/DOID_0080322](http://purl.obolibrary.org/obo/DOID_0080322) |
| `OMIM:('OMIM', 'PS214100')` |              1 | [http://purl.obolibrary.org/obo/DOID_0080377](http://purl.obolibrary.org/obo/DOID_0080377) |
| `OMIM:('OMIM', 'PS308230')` |              1 | [http://purl.obolibrary.org/obo/DOID_0080544](http://purl.obolibrary.org/obo/DOID_0080544) |
| `OMIM:('OMIM', 'PS147060')` |              1 | [http://purl.obolibrary.org/obo/DOID_0080545](http://purl.obolibrary.org/obo/DOID_0080545) |
| `OMIM:('OMIM', 'PS147950')` |              1 | [http://purl.obolibrary.org/obo/DOID_0090070](http://purl.obolibrary.org/obo/DOID_0090070) |
| `OMIM:('OMIM', 'PS234200')` |              1 | [http://purl.obolibrary.org/obo/DOID_0110734](http://purl.obolibrary.org/obo/DOID_0110734) |
| `OMIM:('OMIM', 'PS236670')` |              1 | [http://purl.obolibrary.org/obo/DOID_0111229](http://purl.obolibrary.org/obo/DOID_0111229) |
| `OMIM:('OMIM', 'PS118100')` |              1 | [http://purl.obolibrary.org/obo/DOID_10426](http://purl.obolibrary.org/obo/DOID_10426)     |
| `OMIM:('OMIM', 'PS268000')` |              1 | [http://purl.obolibrary.org/obo/DOID_10584](http://purl.obolibrary.org/obo/DOID_10584)     |
| `OMIM:('OMIM', 'PS118220')` |              1 | [http://purl.obolibrary.org/obo/DOID_10595](http://purl.obolibrary.org/obo/DOID_10595)     |
| `OMIM:('OMIM', 'PS134600')` |              1 | [http://purl.obolibrary.org/obo/DOID_1062](http://purl.obolibrary.org/obo/DOID_1062)       |
| `OMIM:('OMIM', 'PS603075')` |              1 | [http://purl.obolibrary.org/obo/DOID_10871](http://purl.obolibrary.org/obo/DOID_10871)     |
| `OMIM:('OMIM', 'PS122470')` |              1 | [http://purl.obolibrary.org/obo/DOID_11725](http://purl.obolibrary.org/obo/DOID_11725)     |
| `OMIM:('OMIM', 'PS310300')` |              1 | [http://purl.obolibrary.org/obo/DOID_11726](http://purl.obolibrary.org/obo/DOID_11726)     |
| `OMIM:('OMIM', 'PS166200')` |              1 | [http://purl.obolibrary.org/obo/DOID_12347](http://purl.obolibrary.org/obo/DOID_12347)     |
| `OMIM:('OMIM', 'PS157640')` |              1 | [http://purl.obolibrary.org/obo/DOID_12558](http://purl.obolibrary.org/obo/DOID_12558)     |
| `OMIM:('OMIM', 'PS256100')` |              1 | [http://purl.obolibrary.org/obo/DOID_12712](http://purl.obolibrary.org/obo/DOID_12712)     |
| `OMIM:('OMIM', 'PS607014')` |              1 | [http://purl.obolibrary.org/obo/DOID_12798](http://purl.obolibrary.org/obo/DOID_12798)     |
| `OMIM:('OMIM', 'PS115200')` |              1 | [http://purl.obolibrary.org/obo/DOID_12930](http://purl.obolibrary.org/obo/DOID_12930)     |
| `OMIM:('OMIM', 'PS603278')` |              1 | [http://purl.obolibrary.org/obo/DOID_1312](http://purl.obolibrary.org/obo/DOID_1312)       |
| `OMIM:('OMIM', 'PS130000')` |              1 | [http://purl.obolibrary.org/obo/DOID_13359](http://purl.obolibrary.org/obo/DOID_13359)     |
| `OMIM:('OMIM', 'PS224120')` |              1 | [http://purl.obolibrary.org/obo/DOID_1338](http://purl.obolibrary.org/obo/DOID_1338)       |
| `OMIM:('OMIM', 'PS105650')` |              1 | [http://purl.obolibrary.org/obo/DOID_1339](http://purl.obolibrary.org/obo/DOID_1339)       |
| `OMIM:('OMIM', 'PS191100')` |              1 | [http://purl.obolibrary.org/obo/DOID_13515](http://purl.obolibrary.org/obo/DOID_13515)     |
| `OMIM:('OMIM', 'PS259700')` |              1 | [http://purl.obolibrary.org/obo/DOID_13533](http://purl.obolibrary.org/obo/DOID_13533)     |
| `OMIM:('OMIM', 'PS607634')` |              1 | [http://purl.obolibrary.org/obo/DOID_13533](http://purl.obolibrary.org/obo/DOID_13533)     |
| `OMIM:('OMIM', 'PS227650')` |              1 | [http://purl.obolibrary.org/obo/DOID_13636](http://purl.obolibrary.org/obo/DOID_13636)     |
| `OMIM:('OMIM', 'PS226400')` |              1 | [http://purl.obolibrary.org/obo/DOID_13777](http://purl.obolibrary.org/obo/DOID_13777)     |
| `OMIM:('OMIM', 'PS125310')` |              1 | [http://purl.obolibrary.org/obo/DOID_13945](http://purl.obolibrary.org/obo/DOID_13945)     |
| `OMIM:('OMIM', 'PS151100')` |              1 | [http://purl.obolibrary.org/obo/DOID_14291](http://purl.obolibrary.org/obo/DOID_14291)     |
| `OMIM:('OMIM', 'PS168600')` |              1 | [http://purl.obolibrary.org/obo/DOID_14330](http://purl.obolibrary.org/obo/DOID_14330)     |
| `OMIM:('OMIM', 'PS164400')` |              1 | [http://purl.obolibrary.org/obo/DOID_1441](http://purl.obolibrary.org/obo/DOID_1441)       |
| `OMIM:('OMIM', 'PS256730')` |              1 | [http://purl.obolibrary.org/obo/DOID_14503](http://purl.obolibrary.org/obo/DOID_14503)     |
| `OMIM:('OMIM', 'PS117550')` |              1 | [http://purl.obolibrary.org/obo/DOID_14748](http://purl.obolibrary.org/obo/DOID_14748)     |
| `OMIM:('OMIM', 'PS204000')` |              1 | [http://purl.obolibrary.org/obo/DOID_14791](http://purl.obolibrary.org/obo/DOID_14791)     |
| `OMIM:('OMIM', 'PS108800')` |              1 | [http://purl.obolibrary.org/obo/DOID_1882](http://purl.obolibrary.org/obo/DOID_1882)       |
| `OMIM:('OMIM', 'PS135900')` |              1 | [http://purl.obolibrary.org/obo/DOID_1925](http://purl.obolibrary.org/obo/DOID_1925)       |
| `OMIM:('OMIM', 'PS209900')` |              1 | [http://purl.obolibrary.org/obo/DOID_1935](http://purl.obolibrary.org/obo/DOID_1935)       |
| `OMIM:('OMIM', 'PS305100')` |              1 | [http://purl.obolibrary.org/obo/DOID_2121](http://purl.obolibrary.org/obo/DOID_2121)       |
| `OMIM:('OMIM', 'PS104500')` |              1 | [http://purl.obolibrary.org/obo/DOID_2187](http://purl.obolibrary.org/obo/DOID_2187)       |
| `OMIM:('OMIM', 'PS235200')` |              1 | [http://purl.obolibrary.org/obo/DOID_2352](http://purl.obolibrary.org/obo/DOID_2352)       |
| `OMIM:('OMIM', 'PS188050')` |              1 | [http://purl.obolibrary.org/obo/DOID_2452](http://purl.obolibrary.org/obo/DOID_2452)       |
| `OMIM:('OMIM', 'PS215100')` |              1 | [http://purl.obolibrary.org/obo/DOID_2580](http://purl.obolibrary.org/obo/DOID_2580)       |
| `OMIM:('OMIM', 'PS601495')` |              1 | [http://purl.obolibrary.org/obo/DOID_2583](http://purl.obolibrary.org/obo/DOID_2583)       |
| `OMIM:('OMIM', 'PS127550')` |              1 | [http://purl.obolibrary.org/obo/DOID_2729](http://purl.obolibrary.org/obo/DOID_2729)       |
| `OMIM:('OMIM', 'PS192500')` |              1 | [http://purl.obolibrary.org/obo/DOID_2843](http://purl.obolibrary.org/obo/DOID_2843)       |
| `OMIM:('OMIM', 'PS154500')` |              1 | [http://purl.obolibrary.org/obo/DOID_2908](http://purl.obolibrary.org/obo/DOID_2908)       |
| `OMIM:('OMIM', 'PS601675')` |              1 | [http://purl.obolibrary.org/obo/DOID_2960](http://purl.obolibrary.org/obo/DOID_2960)       |
| `OMIM:('OMIM', 'PS259900')` |              1 | [http://purl.obolibrary.org/obo/DOID_2977](http://purl.obolibrary.org/obo/DOID_2977)       |
| `OMIM:('OMIM', 'PS151623')` |              1 | [http://purl.obolibrary.org/obo/DOID_3012](http://purl.obolibrary.org/obo/DOID_3012)       |
| `OMIM:('OMIM', 'PS137800')` |              1 | [http://purl.obolibrary.org/obo/DOID_3070](http://purl.obolibrary.org/obo/DOID_3070)       |
| `OMIM:('OMIM', 'PS123700')` |              1 | [http://purl.obolibrary.org/obo/DOID_3144](http://purl.obolibrary.org/obo/DOID_3144)       |
| `OMIM:('OMIM', 'PS161800')` |              1 | [http://purl.obolibrary.org/obo/DOID_3191](http://purl.obolibrary.org/obo/DOID_3191)       |
| `OMIM:('OMIM', 'PS603165')` |              1 | [http://purl.obolibrary.org/obo/DOID_3310](http://purl.obolibrary.org/obo/DOID_3310)       |
| `OMIM:('OMIM', 'PS105400')` |              1 | [http://purl.obolibrary.org/obo/DOID_332](http://purl.obolibrary.org/obo/DOID_332)         |
| `OMIM:('OMIM', 'PS163950')` |              1 | [http://purl.obolibrary.org/obo/DOID_3490](http://purl.obolibrary.org/obo/DOID_3490)       |
| `OMIM:('OMIM', 'PS601462')` |              1 | [http://purl.obolibrary.org/obo/DOID_3635](http://purl.obolibrary.org/obo/DOID_3635)       |
| `OMIM:('OMIM', 'PS203300')` |              1 | [http://purl.obolibrary.org/obo/DOID_3753](http://purl.obolibrary.org/obo/DOID_3753)       |
| `OMIM:('OMIM', 'PS102200')` |              1 | [http://purl.obolibrary.org/obo/DOID_3829](http://purl.obolibrary.org/obo/DOID_3829)       |
| `OMIM:('OMIM', 'PS120435')` |              1 | [http://purl.obolibrary.org/obo/DOID_3883](http://purl.obolibrary.org/obo/DOID_3883)       |
| `OMIM:('OMIM', 'PS115210')` |              1 | [http://purl.obolibrary.org/obo/DOID_397](http://purl.obolibrary.org/obo/DOID_397)         |
| `OMIM:('OMIM', 'PS601678')` |              1 | [http://purl.obolibrary.org/obo/DOID_445](http://purl.obolibrary.org/obo/DOID_445)         |
| `OMIM:('OMIM', 'PS605389')` |              1 | [http://purl.obolibrary.org/obo/DOID_4535](http://purl.obolibrary.org/obo/DOID_4535)       |
| `OMIM:('OMIM', 'PS236100')` |              1 | [http://purl.obolibrary.org/obo/DOID_4621](http://purl.obolibrary.org/obo/DOID_4621)       |
| `OMIM:('OMIM', 'PS190300')` |              1 | [http://purl.obolibrary.org/obo/DOID_4990](http://purl.obolibrary.org/obo/DOID_4990)       |
| `OMIM:('OMIM', 'PS212065')` |              1 | [http://purl.obolibrary.org/obo/DOID_5212](http://purl.obolibrary.org/obo/DOID_5212)       |
| `OMIM:('OMIM', 'PS128100')` |              1 | [http://purl.obolibrary.org/obo/DOID_543](http://purl.obolibrary.org/obo/DOID_543)         |
| `OMIM:('OMIM', 'PS165500')` |              1 | [http://purl.obolibrary.org/obo/DOID_5723](http://purl.obolibrary.org/obo/DOID_5723)       |
| `OMIM:('OMIM', 'PS300755')` |              1 | [http://purl.obolibrary.org/obo/DOID_612](http://purl.obolibrary.org/obo/DOID_612)         |
| `OMIM:('OMIM', 'PS158350')` |              1 | [http://purl.obolibrary.org/obo/DOID_6457](http://purl.obolibrary.org/obo/DOID_6457)       |
| `OMIM:('OMIM', 'PS106300')` |              1 | [http://purl.obolibrary.org/obo/DOID_7147](http://purl.obolibrary.org/obo/DOID_7147)       |
| `OMIM:('OMIM', 'PS116200')` |              1 | [http://purl.obolibrary.org/obo/DOID_83](http://purl.obolibrary.org/obo/DOID_83)           |
| `OMIM:('OMIM', 'PS145600')` |              1 | [http://purl.obolibrary.org/obo/DOID_8545](http://purl.obolibrary.org/obo/DOID_8545)       |
| `OMIM:('OMIM', 'PS177900')` |              1 | [http://purl.obolibrary.org/obo/DOID_8893](http://purl.obolibrary.org/obo/DOID_8893)       |
| `OMIM:('OMIM', 'PS254800')` |              1 | [http://purl.obolibrary.org/obo/DOID_891](http://purl.obolibrary.org/obo/DOID_891)         |
| `OMIM:('OMIM', 'PS300751')` |              1 | [http://purl.obolibrary.org/obo/DOID_8955](http://purl.obolibrary.org/obo/DOID_8955)       |
| `OMIM:('OMIM', 'PS193500')` |              1 | [http://purl.obolibrary.org/obo/DOID_9258](http://purl.obolibrary.org/obo/DOID_9258)       |
| `OMIM:('OMIM', 'PS244400')` |              1 | [http://purl.obolibrary.org/obo/DOID_9562](http://purl.obolibrary.org/obo/DOID_9562)       |
| `OMIM:('OMIM', 'PS211400')` |              1 | [http://purl.obolibrary.org/obo/DOID_9563](http://purl.obolibrary.org/obo/DOID_9563)       |
| `OMIM:('OMIM', 'PS310700')` |              1 | [http://purl.obolibrary.org/obo/DOID_9649](http://purl.obolibrary.org/obo/DOID_9649)       |
| `OMIM:('OMIM', 'PS203655')` |              1 | [http://purl.obolibrary.org/obo/DOID_987](http://purl.obolibrary.org/obo/DOID_987)         |

## `ORDO`: Orphanet Rare Disease Ontology

Overall, there were 381 invalid
xrefs to external prefixed with `ORDO` (standardized to Bioregistry
prefix [`orphanet.ordo`](https://bioregistry.io/orphanet.ordo)) that
did not match the standard pattern `^Orphanet(_|:)C?\d+$`.

| external_xref             |   usages_count | usages                                                                                                                                                                           |
|---------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ORDO:('ORDO', '768')`    |              2 | [http://purl.obolibrary.org/obo/DOID_0060173](http://purl.obolibrary.org/obo/DOID_0060173), [http://purl.obolibrary.org/obo/DOID_2843](http://purl.obolibrary.org/obo/DOID_2843) |
| `ORDO:('ORDO', '478')`    |              2 | [http://purl.obolibrary.org/obo/DOID_0090070](http://purl.obolibrary.org/obo/DOID_0090070), [http://purl.obolibrary.org/obo/DOID_3614](http://purl.obolibrary.org/obo/DOID_3614) |
| `ORDO:('ORDO', '540')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050120](http://purl.obolibrary.org/obo/DOID_0050120)                                                                                       |
| `ORDO:('ORDO', '733')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050424](http://purl.obolibrary.org/obo/DOID_0050424)                                                                                       |
| `ORDO:('ORDO', '910')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050427](http://purl.obolibrary.org/obo/DOID_0050427)                                                                                       |
| `ORDO:('ORDO', '2337')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050428](http://purl.obolibrary.org/obo/DOID_0050428)                                                                                       |
| `ORDO:('ORDO', '247698')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050430](http://purl.obolibrary.org/obo/DOID_0050430)                                                                                       |
| `ORDO:('ORDO', '217656')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050431](http://purl.obolibrary.org/obo/DOID_0050431)                                                                                       |
| `ORDO:('ORDO', '247')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050431](http://purl.obolibrary.org/obo/DOID_0050431)                                                                                       |
| `ORDO:('ORDO', '1162')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050432](http://purl.obolibrary.org/obo/DOID_0050432)                                                                                       |
| `ORDO:('ORDO', '2576')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050436](http://purl.obolibrary.org/obo/DOID_0050436)                                                                                       |
| `ORDO:('ORDO', '886')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050439](http://purl.obolibrary.org/obo/DOID_0050439)                                                                                       |
| `ORDO:('ORDO', '171723')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050448](http://purl.obolibrary.org/obo/DOID_0050448)                                                                                       |
| `ORDO:('ORDO', '2309')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050449](http://purl.obolibrary.org/obo/DOID_0050449)                                                                                       |
| `ORDO:('ORDO', '130')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050451](http://purl.obolibrary.org/obo/DOID_0050451)                                                                                       |
| `ORDO:('ORDO', '29')`     |              1 | [http://purl.obolibrary.org/obo/DOID_0050452](http://purl.obolibrary.org/obo/DOID_0050452)                                                                                       |
| `ORDO:('ORDO', '102009')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050453](http://purl.obolibrary.org/obo/DOID_0050453)                                                                                       |
| `ORDO:('ORDO', '98892')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0050454](http://purl.obolibrary.org/obo/DOID_0050454)                                                                                       |
| `ORDO:('ORDO', '280')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050460](http://purl.obolibrary.org/obo/DOID_0050460)                                                                                       |
| `ORDO:('ORDO', '140')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050463](http://purl.obolibrary.org/obo/DOID_0050463)                                                                                       |
| `ORDO:('ORDO', '60030')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0050466](http://purl.obolibrary.org/obo/DOID_0050466)                                                                                       |
| `ORDO:('ORDO', '317')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050467](http://purl.obolibrary.org/obo/DOID_0050467)                                                                                       |
| `ORDO:('ORDO', '508')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050470](http://purl.obolibrary.org/obo/DOID_0050470)                                                                                       |
| `ORDO:('ORDO', '1359')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050471](http://purl.obolibrary.org/obo/DOID_0050471)                                                                                       |
| `ORDO:('ORDO', '634')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050474](http://purl.obolibrary.org/obo/DOID_0050474)                                                                                       |
| `ORDO:('ORDO', '3449')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050475](http://purl.obolibrary.org/obo/DOID_0050475)                                                                                       |
| `ORDO:('ORDO', '552')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050524](http://purl.obolibrary.org/obo/DOID_0050524)                                                                                       |
| `ORDO:('ORDO', '83420')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0050529](http://purl.obolibrary.org/obo/DOID_0050529)                                                                                       |
| `ORDO:('ORDO', '215')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050534](http://purl.obolibrary.org/obo/DOID_0050534)                                                                                       |
| `ORDO:('ORDO', '891')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050535](http://purl.obolibrary.org/obo/DOID_0050535)                                                                                       |
| `ORDO:('ORDO', '450')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050545](http://purl.obolibrary.org/obo/DOID_0050545)                                                                                       |
| `ORDO:('ORDO', '324999')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050553](http://purl.obolibrary.org/obo/DOID_0050553)                                                                                       |
| `ORDO:('ORDO', '97242')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0050557](http://purl.obolibrary.org/obo/DOID_0050557)                                                                                       |
| `ORDO:('ORDO', '272')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050559](http://purl.obolibrary.org/obo/DOID_0050559)                                                                                       |
| `ORDO:('ORDO', '2382')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050561](http://purl.obolibrary.org/obo/DOID_0050561)                                                                                       |
| `ORDO:('ORDO', '90625')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0050566](http://purl.obolibrary.org/obo/DOID_0050566)                                                                                       |
| `ORDO:('ORDO', '1797')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050568](http://purl.obolibrary.org/obo/DOID_0050568)                                                                                       |
| `ORDO:('ORDO', '2311')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050568](http://purl.obolibrary.org/obo/DOID_0050568)                                                                                       |
| `ORDO:('ORDO', '808')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050569](http://purl.obolibrary.org/obo/DOID_0050569)                                                                                       |
| `ORDO:('ORDO', '1872')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050572](http://purl.obolibrary.org/obo/DOID_0050572)                                                                                       |
| `ORDO:('ORDO', '79314')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0050574](http://purl.obolibrary.org/obo/DOID_0050574)                                                                                       |
| `ORDO:('ORDO', '294937')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050581](http://purl.obolibrary.org/obo/DOID_0050581)                                                                                       |
| `ORDO:('ORDO', '370953')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050588](http://purl.obolibrary.org/obo/DOID_0050588)                                                                                       |
| `ORDO:('ORDO', '42738')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0050590](http://purl.obolibrary.org/obo/DOID_0050590)                                                                                       |
| `ORDO:('ORDO', '2227')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050591](http://purl.obolibrary.org/obo/DOID_0050591)                                                                                       |
| `ORDO:('ORDO', '99798')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0050591](http://purl.obolibrary.org/obo/DOID_0050591)                                                                                       |
| `ORDO:('ORDO', '474')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050592](http://purl.obolibrary.org/obo/DOID_0050592)                                                                                       |
| `ORDO:('ORDO', '1247')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050597](http://purl.obolibrary.org/obo/DOID_0050597)                                                                                       |
| `ORDO:('ORDO', '51')`     |              1 | [http://purl.obolibrary.org/obo/DOID_0050629](http://purl.obolibrary.org/obo/DOID_0050629)                                                                                       |
| `ORDO:('ORDO', '59')`     |              1 | [http://purl.obolibrary.org/obo/DOID_0050631](http://purl.obolibrary.org/obo/DOID_0050631)                                                                                       |
| `ORDO:('ORDO', '55')`     |              1 | [http://purl.obolibrary.org/obo/DOID_0050632](http://purl.obolibrary.org/obo/DOID_0050632)                                                                                       |
| `ORDO:('ORDO', '137807')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050639](http://purl.obolibrary.org/obo/DOID_0050639)                                                                                       |
| `ORDO:('ORDO', '51608')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0050644](http://purl.obolibrary.org/obo/DOID_0050644)                                                                                       |
| `ORDO:('ORDO', '1147')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050646](http://purl.obolibrary.org/obo/DOID_0050646)                                                                                       |
| `ORDO:('ORDO', '97120')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0050646](http://purl.obolibrary.org/obo/DOID_0050646)                                                                                       |
| `ORDO:('ORDO', '1187')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050647](http://purl.obolibrary.org/obo/DOID_0050647)                                                                                       |
| `ORDO:('ORDO', '1195')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050649](http://purl.obolibrary.org/obo/DOID_0050649)                                                                                       |
| `ORDO:('ORDO', '334')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050650](http://purl.obolibrary.org/obo/DOID_0050650)                                                                                       |
| `ORDO:('ORDO', '98722')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0050651](http://purl.obolibrary.org/obo/DOID_0050651)                                                                                       |
| `ORDO:('ORDO', '1223')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050654](http://purl.obolibrary.org/obo/DOID_0050654)                                                                                       |
| `ORDO:('ORDO', '1229')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050656](http://purl.obolibrary.org/obo/DOID_0050656)                                                                                       |
| `ORDO:('ORDO', '109')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050657](http://purl.obolibrary.org/obo/DOID_0050657)                                                                                       |
| `ORDO:('ORDO', '1243')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050661](http://purl.obolibrary.org/obo/DOID_0050661)                                                                                       |
| `ORDO:('ORDO', '99000')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0050661](http://purl.obolibrary.org/obo/DOID_0050661)                                                                                       |
| `ORDO:('ORDO', '127')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050681](http://purl.obolibrary.org/obo/DOID_0050681)                                                                                       |
| `ORDO:('ORDO', '1270')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050684](http://purl.obolibrary.org/obo/DOID_0050684)                                                                                       |
| `ORDO:('ORDO', '1293')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050690](http://purl.obolibrary.org/obo/DOID_0050690)                                                                                       |
| `ORDO:('ORDO', '79493')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0050693](http://purl.obolibrary.org/obo/DOID_0050693)                                                                                       |
| `ORDO:('ORDO', '1934')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050709](http://purl.obolibrary.org/obo/DOID_0050709)                                                                                       |
| `ORDO:('ORDO', '6')`      |              1 | [http://purl.obolibrary.org/obo/DOID_0050710](http://purl.obolibrary.org/obo/DOID_0050710)                                                                                       |
| `ORDO:('ORDO', '3213')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050757](http://purl.obolibrary.org/obo/DOID_0050757)                                                                                       |
| `ORDO:('ORDO', '2697')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050763](http://purl.obolibrary.org/obo/DOID_0050763)                                                                                       |
| `ORDO:('ORDO', '263440')` |              1 | [http://purl.obolibrary.org/obo/DOID_0050765](http://purl.obolibrary.org/obo/DOID_0050765)                                                                                       |
| `ORDO:('ORDO', '2388')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050766](http://purl.obolibrary.org/obo/DOID_0050766)                                                                                       |
| `ORDO:('ORDO', '2608')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050769](http://purl.obolibrary.org/obo/DOID_0050769)                                                                                       |
| `ORDO:('ORDO', '3021')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050774](http://purl.obolibrary.org/obo/DOID_0050774)                                                                                       |
| `ORDO:('ORDO', '777')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0050776](http://purl.obolibrary.org/obo/DOID_0050776)                                                                                       |
| `ORDO:('ORDO', '1172')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0050950](http://purl.obolibrary.org/obo/DOID_0050950)                                                                                       |
| `ORDO:('ORDO', '69127')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0060025](http://purl.obolibrary.org/obo/DOID_0060025)                                                                                       |
| `ORDO:('ORDO', '547')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0060060](http://purl.obolibrary.org/obo/DOID_0060060)                                                                                       |
| `ORDO:('ORDO', '209886')` |              1 | [http://purl.obolibrary.org/obo/DOID_0060062](http://purl.obolibrary.org/obo/DOID_0060062)                                                                                       |
| `ORDO:('ORDO', '217330')` |              1 | [http://purl.obolibrary.org/obo/DOID_0060062](http://purl.obolibrary.org/obo/DOID_0060062)                                                                                       |
| `ORDO:('ORDO', '70')`     |              1 | [http://purl.obolibrary.org/obo/DOID_0060160](http://purl.obolibrary.org/obo/DOID_0060160)                                                                                       |
| `ORDO:('ORDO', '306')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0060169](http://purl.obolibrary.org/obo/DOID_0060169)                                                                                       |
| `ORDO:('ORDO', '65283')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0060173](http://purl.obolibrary.org/obo/DOID_0060173)                                                                                       |
| `ORDO:('ORDO', '178469')` |              1 | [http://purl.obolibrary.org/obo/DOID_0060307](http://purl.obolibrary.org/obo/DOID_0060307)                                                                                       |
| `ORDO:('ORDO', '281097')` |              1 | [http://purl.obolibrary.org/obo/DOID_0060655](http://purl.obolibrary.org/obo/DOID_0060655)                                                                                       |
| `ORDO:('ORDO', '1048')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0060668](http://purl.obolibrary.org/obo/DOID_0060668)                                                                                       |
| `ORDO:('ORDO', '163690')` |              1 | [http://purl.obolibrary.org/obo/DOID_0060858](http://purl.obolibrary.org/obo/DOID_0060858)                                                                                       |
| `ORDO:('ORDO', '35698')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0070329](http://purl.obolibrary.org/obo/DOID_0070329)                                                                                       |
| `ORDO:('ORDO', '1522')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0080033](http://purl.obolibrary.org/obo/DOID_0080033)                                                                                       |
| `ORDO:('ORDO', '3152')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0080036](http://purl.obolibrary.org/obo/DOID_0080036)                                                                                       |
| `ORDO:('ORDO', '763')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0080038](http://purl.obolibrary.org/obo/DOID_0080038)                                                                                       |
| `ORDO:('ORDO', '429')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0080041](http://purl.obolibrary.org/obo/DOID_0080041)                                                                                       |
| `ORDO:('ORDO', '828')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0080046](http://purl.obolibrary.org/obo/DOID_0080046)                                                                                       |
| `ORDO:('ORDO', '93437')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0080049](http://purl.obolibrary.org/obo/DOID_0080049)                                                                                       |
| `ORDO:('ORDO', '2978')`   |              1 | [http://purl.obolibrary.org/obo/DOID_0080072](http://purl.obolibrary.org/obo/DOID_0080072)                                                                                       |
| `ORDO:('ORDO', '726')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0080122](http://purl.obolibrary.org/obo/DOID_0080122)                                                                                       |
| `ORDO:('ORDO', '33069')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0080422](http://purl.obolibrary.org/obo/DOID_0080422)                                                                                       |
| `ORDO:('ORDO', '432')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0090070](http://purl.obolibrary.org/obo/DOID_0090070)                                                                                       |
| `ORDO:('ORDO', '228346')` |              1 | [http://purl.obolibrary.org/obo/DOID_0110731](http://purl.obolibrary.org/obo/DOID_0110731)                                                                                       |
| `ORDO:('ORDO', '385')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0110734](http://purl.obolibrary.org/obo/DOID_0110734)                                                                                       |
| `ORDO:('ORDO', '352687')` |              1 | [http://purl.obolibrary.org/obo/DOID_0111229](http://purl.obolibrary.org/obo/DOID_0111229)                                                                                       |
| `ORDO:('ORDO', '444490')` |              1 | [http://purl.obolibrary.org/obo/DOID_0111417](http://purl.obolibrary.org/obo/DOID_0111417)                                                                                       |
| `ORDO:('ORDO', '915')`    |              1 | [http://purl.obolibrary.org/obo/DOID_0111824](http://purl.obolibrary.org/obo/DOID_0111824)                                                                                       |
| `ORDO:('ORDO', '33364')`  |              1 | [http://purl.obolibrary.org/obo/DOID_0111866](http://purl.obolibrary.org/obo/DOID_0111866)                                                                                       |
| `ORDO:('ORDO', '652')`    |              1 | [http://purl.obolibrary.org/obo/DOID_10017](http://purl.obolibrary.org/obo/DOID_10017)                                                                                           |
| `ORDO:('ORDO', '156071')` |              1 | [http://purl.obolibrary.org/obo/DOID_10126](http://purl.obolibrary.org/obo/DOID_10126)                                                                                           |
| `ORDO:('ORDO', '548')`    |              1 | [http://purl.obolibrary.org/obo/DOID_1024](http://purl.obolibrary.org/obo/DOID_1024)                                                                                             |
| `ORDO:('ORDO', '1331')`   |              1 | [http://purl.obolibrary.org/obo/DOID_10283](http://purl.obolibrary.org/obo/DOID_10283)                                                                                           |
| `ORDO:('ORDO', '67038')`  |              1 | [http://purl.obolibrary.org/obo/DOID_1040](http://purl.obolibrary.org/obo/DOID_1040)                                                                                             |
| `ORDO:('ORDO', '2345')`   |              1 | [http://purl.obolibrary.org/obo/DOID_10426](http://purl.obolibrary.org/obo/DOID_10426)                                                                                           |
| `ORDO:('ORDO', '388')`    |              1 | [http://purl.obolibrary.org/obo/DOID_10487](http://purl.obolibrary.org/obo/DOID_10487)                                                                                           |
| `ORDO:('ORDO', '534')`    |              1 | [http://purl.obolibrary.org/obo/DOID_1056](http://purl.obolibrary.org/obo/DOID_1056)                                                                                             |
| `ORDO:('ORDO', '512')`    |              1 | [http://purl.obolibrary.org/obo/DOID_10581](http://purl.obolibrary.org/obo/DOID_10581)                                                                                           |
| `ORDO:('ORDO', '791')`    |              1 | [http://purl.obolibrary.org/obo/DOID_10584](http://purl.obolibrary.org/obo/DOID_10584)                                                                                           |
| `ORDO:('ORDO', '275555')` |              1 | [http://purl.obolibrary.org/obo/DOID_10591](http://purl.obolibrary.org/obo/DOID_10591)                                                                                           |
| `ORDO:('ORDO', '555')`    |              1 | [http://purl.obolibrary.org/obo/DOID_10608](http://purl.obolibrary.org/obo/DOID_10608)                                                                                           |
| `ORDO:('ORDO', '289157')` |              1 | [http://purl.obolibrary.org/obo/DOID_10609](http://purl.obolibrary.org/obo/DOID_10609)                                                                                           |
| `ORDO:('ORDO', '3337')`   |              1 | [http://purl.obolibrary.org/obo/DOID_1062](http://purl.obolibrary.org/obo/DOID_1062)                                                                                             |
| `ORDO:('ORDO', '3463')`   |              1 | [http://purl.obolibrary.org/obo/DOID_10632](http://purl.obolibrary.org/obo/DOID_10632)                                                                                           |
| `ORDO:('ORDO', '213')`    |              1 | [http://purl.obolibrary.org/obo/DOID_1064](http://purl.obolibrary.org/obo/DOID_1064)                                                                                             |
| `ORDO:('ORDO', '440')`    |              1 | [http://purl.obolibrary.org/obo/DOID_10892](http://purl.obolibrary.org/obo/DOID_10892)                                                                                           |
| `ORDO:('ORDO', '2182')`   |              1 | [http://purl.obolibrary.org/obo/DOID_10908](http://purl.obolibrary.org/obo/DOID_10908)                                                                                           |
| `ORDO:('ORDO', '2185')`   |              1 | [http://purl.obolibrary.org/obo/DOID_10908](http://purl.obolibrary.org/obo/DOID_10908)                                                                                           |
| `ORDO:('ORDO', '232')`    |              1 | [http://purl.obolibrary.org/obo/DOID_10923](http://purl.obolibrary.org/obo/DOID_10923)                                                                                           |
| `ORDO:('ORDO', '210141')` |              1 | [http://purl.obolibrary.org/obo/DOID_10970](http://purl.obolibrary.org/obo/DOID_10970)                                                                                           |
| `ORDO:('ORDO', '63')`     |              1 | [http://purl.obolibrary.org/obo/DOID_10983](http://purl.obolibrary.org/obo/DOID_10983)                                                                                           |
| `ORDO:('ORDO', '295012')` |              1 | [http://purl.obolibrary.org/obo/DOID_11193](http://purl.obolibrary.org/obo/DOID_11193)                                                                                           |
| `ORDO:('ORDO', '90025')`  |              1 | [http://purl.obolibrary.org/obo/DOID_11193](http://purl.obolibrary.org/obo/DOID_11193)                                                                                           |
| `ORDO:('ORDO', '93403')`  |              1 | [http://purl.obolibrary.org/obo/DOID_11193](http://purl.obolibrary.org/obo/DOID_11193)                                                                                           |
| `ORDO:('ORDO', '2238')`   |              1 | [http://purl.obolibrary.org/obo/DOID_11199](http://purl.obolibrary.org/obo/DOID_11199)                                                                                           |
| `ORDO:('ORDO', '797')`    |              1 | [http://purl.obolibrary.org/obo/DOID_11335](http://purl.obolibrary.org/obo/DOID_11335)                                                                                           |
| `ORDO:('ORDO', '98974')`  |              1 | [http://purl.obolibrary.org/obo/DOID_11555](http://purl.obolibrary.org/obo/DOID_11555)                                                                                           |
| `ORDO:('ORDO', '1416')`   |              1 | [http://purl.obolibrary.org/obo/DOID_1156](http://purl.obolibrary.org/obo/DOID_1156)                                                                                             |
| `ORDO:('ORDO', '399096')` |              1 | [http://purl.obolibrary.org/obo/DOID_11720](http://purl.obolibrary.org/obo/DOID_11720)                                                                                           |
| `ORDO:('ORDO', '5448')`   |              1 | [http://purl.obolibrary.org/obo/DOID_11720](http://purl.obolibrary.org/obo/DOID_11720)                                                                                           |
| `ORDO:('ORDO', '59135')`  |              1 | [http://purl.obolibrary.org/obo/DOID_11720](http://purl.obolibrary.org/obo/DOID_11720)                                                                                           |
| `ORDO:('ORDO', '263')`    |              1 | [http://purl.obolibrary.org/obo/DOID_11724](http://purl.obolibrary.org/obo/DOID_11724)                                                                                           |
| `ORDO:('ORDO', '199')`    |              1 | [http://purl.obolibrary.org/obo/DOID_11725](http://purl.obolibrary.org/obo/DOID_11725)                                                                                           |
| `ORDO:('ORDO', '261')`    |              1 | [http://purl.obolibrary.org/obo/DOID_11726](http://purl.obolibrary.org/obo/DOID_11726)                                                                                           |
| `ORDO:('ORDO', '139436')` |              1 | [http://purl.obolibrary.org/obo/DOID_11824](http://purl.obolibrary.org/obo/DOID_11824)                                                                                           |
| `ORDO:('ORDO', '739')`    |              1 | [http://purl.obolibrary.org/obo/DOID_11983](http://purl.obolibrary.org/obo/DOID_11983)                                                                                           |
| `ORDO:('ORDO', '217568')` |              1 | [http://purl.obolibrary.org/obo/DOID_11984](http://purl.obolibrary.org/obo/DOID_11984)                                                                                           |
| `ORDO:('ORDO', '264675')` |              1 | [http://purl.obolibrary.org/obo/DOID_12120](http://purl.obolibrary.org/obo/DOID_12120)                                                                                           |
| `ORDO:('ORDO', '98878')`  |              1 | [http://purl.obolibrary.org/obo/DOID_12134](http://purl.obolibrary.org/obo/DOID_12134)                                                                                           |
| `ORDO:('ORDO', '1572')`   |              1 | [http://purl.obolibrary.org/obo/DOID_12177](http://purl.obolibrary.org/obo/DOID_12177)                                                                                           |
| `ORDO:('ORDO', '2794')`   |              1 | [http://purl.obolibrary.org/obo/DOID_12185](http://purl.obolibrary.org/obo/DOID_12185)                                                                                           |
| `ORDO:('ORDO', '186')`    |              1 | [http://purl.obolibrary.org/obo/DOID_12236](http://purl.obolibrary.org/obo/DOID_12236)                                                                                           |
| `ORDO:('ORDO', '194')`    |              1 | [http://purl.obolibrary.org/obo/DOID_12270](http://purl.obolibrary.org/obo/DOID_12270)                                                                                           |
| `ORDO:('ORDO', '98945')`  |              1 | [http://purl.obolibrary.org/obo/DOID_12270](http://purl.obolibrary.org/obo/DOID_12270)                                                                                           |
| `ORDO:('ORDO', '666')`    |              1 | [http://purl.obolibrary.org/obo/DOID_12347](http://purl.obolibrary.org/obo/DOID_12347)                                                                                           |
| `ORDO:('ORDO', '223')`    |              1 | [http://purl.obolibrary.org/obo/DOID_12387](http://purl.obolibrary.org/obo/DOID_12387)                                                                                           |
| `ORDO:('ORDO', '2134')`   |              1 | [http://purl.obolibrary.org/obo/DOID_12554](http://purl.obolibrary.org/obo/DOID_12554)                                                                                           |
| `ORDO:('ORDO', '233')`    |              1 | [http://purl.obolibrary.org/obo/DOID_12557](http://purl.obolibrary.org/obo/DOID_12557)                                                                                           |
| `ORDO:('ORDO', '774')`    |              1 | [http://purl.obolibrary.org/obo/DOID_1270](http://purl.obolibrary.org/obo/DOID_1270)                                                                                             |
| `ORDO:('ORDO', '655')`    |              1 | [http://purl.obolibrary.org/obo/DOID_12712](http://purl.obolibrary.org/obo/DOID_12712)                                                                                           |
| `ORDO:('ORDO', '251')`    |              1 | [http://purl.obolibrary.org/obo/DOID_12721](http://purl.obolibrary.org/obo/DOID_12721)                                                                                           |
| `ORDO:('ORDO', '79213')`  |              1 | [http://purl.obolibrary.org/obo/DOID_12798](http://purl.obolibrary.org/obo/DOID_12798)                                                                                           |
| `ORDO:('ORDO', '581')`    |              1 | [http://purl.obolibrary.org/obo/DOID_12801](http://purl.obolibrary.org/obo/DOID_12801)                                                                                           |
| `ORDO:('ORDO', '106')`    |              1 | [http://purl.obolibrary.org/obo/DOID_12849](http://purl.obolibrary.org/obo/DOID_12849)                                                                                           |
| `ORDO:('ORDO', '217604')` |              1 | [http://purl.obolibrary.org/obo/DOID_12930](http://purl.obolibrary.org/obo/DOID_12930)                                                                                           |
| `ORDO:('ORDO', '822')`    |              1 | [http://purl.obolibrary.org/obo/DOID_12971](http://purl.obolibrary.org/obo/DOID_12971)                                                                                           |
| `ORDO:('ORDO', '2573')`   |              1 | [http://purl.obolibrary.org/obo/DOID_13099](http://purl.obolibrary.org/obo/DOID_13099)                                                                                           |
| `ORDO:('ORDO', '280679')` |              1 | [http://purl.obolibrary.org/obo/DOID_13099](http://purl.obolibrary.org/obo/DOID_13099)                                                                                           |
| `ORDO:('ORDO', '401945')` |              1 | [http://purl.obolibrary.org/obo/DOID_13099](http://purl.obolibrary.org/obo/DOID_13099)                                                                                           |
| `ORDO:('ORDO', '79278')`  |              1 | [http://purl.obolibrary.org/obo/DOID_13270](http://purl.obolibrary.org/obo/DOID_13270)                                                                                           |
| `ORDO:('ORDO', '337')`    |              1 | [http://purl.obolibrary.org/obo/DOID_13374](http://purl.obolibrary.org/obo/DOID_13374)                                                                                           |
| `ORDO:('ORDO', '85')`     |              1 | [http://purl.obolibrary.org/obo/DOID_1338](http://purl.obolibrary.org/obo/DOID_1338)                                                                                             |
| `ORDO:('ORDO', '124')`    |              1 | [http://purl.obolibrary.org/obo/DOID_1339](http://purl.obolibrary.org/obo/DOID_1339)                                                                                             |
| `ORDO:('ORDO', '1860')`   |              1 | [http://purl.obolibrary.org/obo/DOID_13481](http://purl.obolibrary.org/obo/DOID_13481)                                                                                           |
| `ORDO:('ORDO', '2655')`   |              1 | [http://purl.obolibrary.org/obo/DOID_13481](http://purl.obolibrary.org/obo/DOID_13481)                                                                                           |
| `ORDO:('ORDO', '93274')`  |              1 | [http://purl.obolibrary.org/obo/DOID_13481](http://purl.obolibrary.org/obo/DOID_13481)                                                                                           |
| `ORDO:('ORDO', '93275')`  |              1 | [http://purl.obolibrary.org/obo/DOID_13481](http://purl.obolibrary.org/obo/DOID_13481)                                                                                           |
| `ORDO:('ORDO', '667')`    |              1 | [http://purl.obolibrary.org/obo/DOID_13533](http://purl.obolibrary.org/obo/DOID_13533)                                                                                           |
| `ORDO:('ORDO', '99879')`  |              1 | [http://purl.obolibrary.org/obo/DOID_13543](http://purl.obolibrary.org/obo/DOID_13543)                                                                                           |
| `ORDO:('ORDO', '30391')`  |              1 | [http://purl.obolibrary.org/obo/DOID_13608](http://purl.obolibrary.org/obo/DOID_13608)                                                                                           |
| `ORDO:('ORDO', '84')`     |              1 | [http://purl.obolibrary.org/obo/DOID_13636](http://purl.obolibrary.org/obo/DOID_13636)                                                                                           |
| `ORDO:('ORDO', '302')`    |              1 | [http://purl.obolibrary.org/obo/DOID_13777](http://purl.obolibrary.org/obo/DOID_13777)                                                                                           |
| `ORDO:('ORDO', '166282')` |              1 | [http://purl.obolibrary.org/obo/DOID_13884](http://purl.obolibrary.org/obo/DOID_13884)                                                                                           |
| `ORDO:('ORDO', '49382')`  |              1 | [http://purl.obolibrary.org/obo/DOID_13911](http://purl.obolibrary.org/obo/DOID_13911)                                                                                           |
| `ORDO:('ORDO', '73247')`  |              1 | [http://purl.obolibrary.org/obo/DOID_13922](http://purl.obolibrary.org/obo/DOID_13922)                                                                                           |
| `ORDO:('ORDO', '136')`    |              1 | [http://purl.obolibrary.org/obo/DOID_13945](http://purl.obolibrary.org/obo/DOID_13945)                                                                                           |
| `ORDO:('ORDO', '1452')`   |              1 | [http://purl.obolibrary.org/obo/DOID_13994](http://purl.obolibrary.org/obo/DOID_13994)                                                                                           |
| `ORDO:('ORDO', '309015')` |              1 | [http://purl.obolibrary.org/obo/DOID_14118](http://purl.obolibrary.org/obo/DOID_14118)                                                                                           |
| `ORDO:('ORDO', '47')`     |              1 | [http://purl.obolibrary.org/obo/DOID_14179](http://purl.obolibrary.org/obo/DOID_14179)                                                                                           |
| `ORDO:('ORDO', '436')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14213](http://purl.obolibrary.org/obo/DOID_14213)                                                                                           |
| `ORDO:('ORDO', '217034')` |              1 | [http://purl.obolibrary.org/obo/DOID_14227](http://purl.obolibrary.org/obo/DOID_14227)                                                                                           |
| `ORDO:('ORDO', '870')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14250](http://purl.obolibrary.org/obo/DOID_14250)                                                                                           |
| `ORDO:('ORDO', '908')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14261](http://purl.obolibrary.org/obo/DOID_14261)                                                                                           |
| `ORDO:('ORDO', '1949')`   |              1 | [http://purl.obolibrary.org/obo/DOID_14264](http://purl.obolibrary.org/obo/DOID_14264)                                                                                           |
| `ORDO:('ORDO', '500')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14291](http://purl.obolibrary.org/obo/DOID_14291)                                                                                           |
| `ORDO:('ORDO', '2828')`   |              1 | [http://purl.obolibrary.org/obo/DOID_14330](http://purl.obolibrary.org/obo/DOID_14330)                                                                                           |
| `ORDO:('ORDO', '94')`     |              1 | [http://purl.obolibrary.org/obo/DOID_1441](http://purl.obolibrary.org/obo/DOID_1441)                                                                                             |
| `ORDO:('ORDO', '682')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14451](http://purl.obolibrary.org/obo/DOID_14451)                                                                                           |
| `ORDO:('ORDO', '681')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14452](http://purl.obolibrary.org/obo/DOID_14452)                                                                                           |
| `ORDO:('ORDO', '94093')`  |              1 | [http://purl.obolibrary.org/obo/DOID_14464](http://purl.obolibrary.org/obo/DOID_14464)                                                                                           |
| `ORDO:('ORDO', '216')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14503](http://purl.obolibrary.org/obo/DOID_14503)                                                                                           |
| `ORDO:('ORDO', '79262')`  |              1 | [http://purl.obolibrary.org/obo/DOID_14503](http://purl.obolibrary.org/obo/DOID_14503)                                                                                           |
| `ORDO:('ORDO', '422')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14557](http://purl.obolibrary.org/obo/DOID_14557)                                                                                           |
| `ORDO:('ORDO', '950')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14669](http://purl.obolibrary.org/obo/DOID_14669)                                                                                           |
| `ORDO:('ORDO', '2300')`   |              1 | [http://purl.obolibrary.org/obo/DOID_14671](http://purl.obolibrary.org/obo/DOID_14671)                                                                                           |
| `ORDO:('ORDO', '782')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14686](http://purl.obolibrary.org/obo/DOID_14686)                                                                                           |
| `ORDO:('ORDO', '2315')`   |              1 | [http://purl.obolibrary.org/obo/DOID_14694](http://purl.obolibrary.org/obo/DOID_14694)                                                                                           |
| `ORDO:('ORDO', '3320')`   |              1 | [http://purl.obolibrary.org/obo/DOID_14699](http://purl.obolibrary.org/obo/DOID_14699)                                                                                           |
| `ORDO:('ORDO', '323')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14711](http://purl.obolibrary.org/obo/DOID_14711)                                                                                           |
| `ORDO:('ORDO', '93932')`  |              1 | [http://purl.obolibrary.org/obo/DOID_14711](http://purl.obolibrary.org/obo/DOID_14711)                                                                                           |
| `ORDO:('ORDO', '595')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14717](http://purl.obolibrary.org/obo/DOID_14717)                                                                                           |
| `ORDO:('ORDO', '596')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14717](http://purl.obolibrary.org/obo/DOID_14717)                                                                                           |
| `ORDO:('ORDO', '69186')`  |              1 | [http://purl.obolibrary.org/obo/DOID_14717](http://purl.obolibrary.org/obo/DOID_14717)                                                                                           |
| `ORDO:('ORDO', '69189')`  |              1 | [http://purl.obolibrary.org/obo/DOID_14717](http://purl.obolibrary.org/obo/DOID_14717)                                                                                           |
| `ORDO:('ORDO', '134')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14723](http://purl.obolibrary.org/obo/DOID_14723)                                                                                           |
| `ORDO:('ORDO', '1520')`   |              1 | [http://purl.obolibrary.org/obo/DOID_14737](http://purl.obolibrary.org/obo/DOID_14737)                                                                                           |
| `ORDO:('ORDO', '94083')`  |              1 | [http://purl.obolibrary.org/obo/DOID_14744](http://purl.obolibrary.org/obo/DOID_14744)                                                                                           |
| `ORDO:('ORDO', '821')`    |              1 | [http://purl.obolibrary.org/obo/DOID_14748](http://purl.obolibrary.org/obo/DOID_14748)                                                                                           |
| `ORDO:('ORDO', '93108')`  |              1 | [http://purl.obolibrary.org/obo/DOID_14766](http://purl.obolibrary.org/obo/DOID_14766)                                                                                           |
| `ORDO:('ORDO', '2332')`   |              1 | [http://purl.obolibrary.org/obo/DOID_14780](http://purl.obolibrary.org/obo/DOID_14780)                                                                                           |
| `ORDO:('ORDO', '65')`     |              1 | [http://purl.obolibrary.org/obo/DOID_14791](http://purl.obolibrary.org/obo/DOID_14791)                                                                                           |
| `ORDO:('ORDO', '238468')` |              1 | [http://purl.obolibrary.org/obo/DOID_14793](http://purl.obolibrary.org/obo/DOID_14793)                                                                                           |
| `ORDO:('ORDO', '586')`    |              1 | [http://purl.obolibrary.org/obo/DOID_1485](http://purl.obolibrary.org/obo/DOID_1485)                                                                                             |
| `ORDO:('ORDO', '852')`    |              1 | [http://purl.obolibrary.org/obo/DOID_1588](http://purl.obolibrary.org/obo/DOID_1588)                                                                                             |
| `ORDO:('ORDO', '1480')`   |              1 | [http://purl.obolibrary.org/obo/DOID_1657](http://purl.obolibrary.org/obo/DOID_1657)                                                                                             |
| `ORDO:('ORDO', '79354')`  |              1 | [http://purl.obolibrary.org/obo/DOID_1697](http://purl.obolibrary.org/obo/DOID_1697)                                                                                             |
| `ORDO:('ORDO', '1333')`   |              1 | [http://purl.obolibrary.org/obo/DOID_1793](http://purl.obolibrary.org/obo/DOID_1793)                                                                                             |
| `ORDO:('ORDO', '217074')` |              1 | [http://purl.obolibrary.org/obo/DOID_1793](http://purl.obolibrary.org/obo/DOID_1793)                                                                                             |
| `ORDO:('ORDO', '284385')` |              1 | [http://purl.obolibrary.org/obo/DOID_1852](http://purl.obolibrary.org/obo/DOID_1852)                                                                                             |
| `ORDO:('ORDO', '1478')`   |              1 | [http://purl.obolibrary.org/obo/DOID_1882](http://purl.obolibrary.org/obo/DOID_1882)                                                                                             |
| `ORDO:('ORDO', '1465')`   |              1 | [http://purl.obolibrary.org/obo/DOID_1925](http://purl.obolibrary.org/obo/DOID_1925)                                                                                             |
| `ORDO:('ORDO', '355')`    |              1 | [http://purl.obolibrary.org/obo/DOID_1926](http://purl.obolibrary.org/obo/DOID_1926)                                                                                             |
| `ORDO:('ORDO', '2377')`   |              1 | [http://purl.obolibrary.org/obo/DOID_1930](http://purl.obolibrary.org/obo/DOID_1930)                                                                                             |
| `ORDO:('ORDO', '783')`    |              1 | [http://purl.obolibrary.org/obo/DOID_1933](http://purl.obolibrary.org/obo/DOID_1933)                                                                                             |
| `ORDO:('ORDO', '110')`    |              1 | [http://purl.obolibrary.org/obo/DOID_1935](http://purl.obolibrary.org/obo/DOID_1935)                                                                                             |
| `ORDO:('ORDO', '83471')`  |              1 | [http://purl.obolibrary.org/obo/DOID_2012](http://purl.obolibrary.org/obo/DOID_2012)                                                                                             |
| `ORDO:('ORDO', '1334')`   |              1 | [http://purl.obolibrary.org/obo/DOID_2058](http://purl.obolibrary.org/obo/DOID_2058)                                                                                             |
| `ORDO:('ORDO', '614')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2106](http://purl.obolibrary.org/obo/DOID_2106)                                                                                             |
| `ORDO:('ORDO', '2092')`   |              1 | [http://purl.obolibrary.org/obo/DOID_2120](http://purl.obolibrary.org/obo/DOID_2120)                                                                                             |
| `ORDO:('ORDO', '79373')`  |              1 | [http://purl.obolibrary.org/obo/DOID_2121](http://purl.obolibrary.org/obo/DOID_2121)                                                                                             |
| `ORDO:('ORDO', '99966')`  |              1 | [http://purl.obolibrary.org/obo/DOID_2129](http://purl.obolibrary.org/obo/DOID_2129)                                                                                             |
| `ORDO:('ORDO', '88661')`  |              1 | [http://purl.obolibrary.org/obo/DOID_2187](http://purl.obolibrary.org/obo/DOID_2187)                                                                                             |
| `ORDO:('ORDO', '274')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2217](http://purl.obolibrary.org/obo/DOID_2217)                                                                                             |
| `ORDO:('ORDO', '849')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2219](http://purl.obolibrary.org/obo/DOID_2219)                                                                                             |
| `ORDO:('ORDO', '3318')`   |              1 | [http://purl.obolibrary.org/obo/DOID_2224](http://purl.obolibrary.org/obo/DOID_2224)                                                                                             |
| `ORDO:('ORDO', '71493')`  |              1 | [http://purl.obolibrary.org/obo/DOID_2224](http://purl.obolibrary.org/obo/DOID_2224)                                                                                             |
| `ORDO:('ORDO', '330')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2231](http://purl.obolibrary.org/obo/DOID_2231)                                                                                             |
| `ORDO:('ORDO', '35689')`  |              1 | [http://purl.obolibrary.org/obo/DOID_230](http://purl.obolibrary.org/obo/DOID_230)                                                                                               |
| `ORDO:('ORDO', '1531')`   |              1 | [http://purl.obolibrary.org/obo/DOID_2340](http://purl.obolibrary.org/obo/DOID_2340)                                                                                             |
| `ORDO:('ORDO', '139498')` |              1 | [http://purl.obolibrary.org/obo/DOID_2352](http://purl.obolibrary.org/obo/DOID_2352)                                                                                             |
| `ORDO:('ORDO', '309144')` |              1 | [http://purl.obolibrary.org/obo/DOID_2368](http://purl.obolibrary.org/obo/DOID_2368)                                                                                             |
| `ORDO:('ORDO', '288')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2373](http://purl.obolibrary.org/obo/DOID_2373)                                                                                             |
| `ORDO:('ORDO', '213500')` |              1 | [http://purl.obolibrary.org/obo/DOID_2394](http://purl.obolibrary.org/obo/DOID_2394)                                                                                             |
| `ORDO:('ORDO', '213517')` |              1 | [http://purl.obolibrary.org/obo/DOID_2394](http://purl.obolibrary.org/obo/DOID_2394)                                                                                             |
| `ORDO:('ORDO', '377')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2512](http://purl.obolibrary.org/obo/DOID_2512)                                                                                             |
| `ORDO:('ORDO', '98818')`  |              1 | [http://purl.obolibrary.org/obo/DOID_2538](http://purl.obolibrary.org/obo/DOID_2538)                                                                                             |
| `ORDO:('ORDO', '177')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2580](http://purl.obolibrary.org/obo/DOID_2580)                                                                                             |
| `ORDO:('ORDO', '93442')`  |              1 | [http://purl.obolibrary.org/obo/DOID_2581](http://purl.obolibrary.org/obo/DOID_2581)                                                                                             |
| `ORDO:('ORDO', '125')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2717](http://purl.obolibrary.org/obo/DOID_2717)                                                                                             |
| `ORDO:('ORDO', '1775')`   |              1 | [http://purl.obolibrary.org/obo/DOID_2729](http://purl.obolibrary.org/obo/DOID_2729)                                                                                             |
| `ORDO:('ORDO', '758')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2738](http://purl.obolibrary.org/obo/DOID_2738)                                                                                             |
| `ORDO:('ORDO', '55881')`  |              1 | [http://purl.obolibrary.org/obo/DOID_2776](http://purl.obolibrary.org/obo/DOID_2776)                                                                                             |
| `ORDO:('ORDO', '101016')` |              1 | [http://purl.obolibrary.org/obo/DOID_2843](http://purl.obolibrary.org/obo/DOID_2843)                                                                                             |
| `ORDO:('ORDO', '374')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2907](http://purl.obolibrary.org/obo/DOID_2907)                                                                                             |
| `ORDO:('ORDO', '167')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2935](http://purl.obolibrary.org/obo/DOID_2935)                                                                                             |
| `ORDO:('ORDO', '191')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2962](http://purl.obolibrary.org/obo/DOID_2962)                                                                                             |
| `ORDO:('ORDO', '90321')`  |              1 | [http://purl.obolibrary.org/obo/DOID_2962](http://purl.obolibrary.org/obo/DOID_2962)                                                                                             |
| `ORDO:('ORDO', '90322')`  |              1 | [http://purl.obolibrary.org/obo/DOID_2962](http://purl.obolibrary.org/obo/DOID_2962)                                                                                             |
| `ORDO:('ORDO', '90324')`  |              1 | [http://purl.obolibrary.org/obo/DOID_2962](http://purl.obolibrary.org/obo/DOID_2962)                                                                                             |
| `ORDO:('ORDO', '416')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2977](http://purl.obolibrary.org/obo/DOID_2977)                                                                                             |
| `ORDO:('ORDO', '342')`    |              1 | [http://purl.obolibrary.org/obo/DOID_2987](http://purl.obolibrary.org/obo/DOID_2987)                                                                                             |
| `ORDO:('ORDO', '524')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3012](http://purl.obolibrary.org/obo/DOID_3012)                                                                                             |
| `ORDO:('ORDO', '182067')` |              1 | [http://purl.obolibrary.org/obo/DOID_3070](http://purl.obolibrary.org/obo/DOID_3070)                                                                                             |
| `ORDO:('ORDO', '101330')` |              1 | [http://purl.obolibrary.org/obo/DOID_3132](http://purl.obolibrary.org/obo/DOID_3132)                                                                                             |
| `ORDO:('ORDO', '100924')` |              1 | [http://purl.obolibrary.org/obo/DOID_3133](http://purl.obolibrary.org/obo/DOID_3133)                                                                                             |
| `ORDO:('ORDO', '209')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3144](http://purl.obolibrary.org/obo/DOID_3144)                                                                                             |
| `ORDO:('ORDO', '607')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3191](http://purl.obolibrary.org/obo/DOID_3191)                                                                                             |
| `ORDO:('ORDO', '702')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3210](http://purl.obolibrary.org/obo/DOID_3210)                                                                                             |
| `ORDO:('ORDO', '99757')`  |              1 | [http://purl.obolibrary.org/obo/DOID_3246](http://purl.obolibrary.org/obo/DOID_3246)                                                                                             |
| `ORDO:('ORDO', '2314')`   |              1 | [http://purl.obolibrary.org/obo/DOID_3261](http://purl.obolibrary.org/obo/DOID_3261)                                                                                             |
| `ORDO:('ORDO', '2884')`   |              1 | [http://purl.obolibrary.org/obo/DOID_3263](http://purl.obolibrary.org/obo/DOID_3263)                                                                                             |
| `ORDO:('ORDO', '379')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3265](http://purl.obolibrary.org/obo/DOID_3265)                                                                                             |
| `ORDO:('ORDO', '3280')`   |              1 | [http://purl.obolibrary.org/obo/DOID_327](http://purl.obolibrary.org/obo/DOID_327)                                                                                               |
| `ORDO:('ORDO', '538')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3319](http://purl.obolibrary.org/obo/DOID_3319)                                                                                             |
| `ORDO:('ORDO', '803')`    |              1 | [http://purl.obolibrary.org/obo/DOID_332](http://purl.obolibrary.org/obo/DOID_332)                                                                                               |
| `ORDO:('ORDO', '668')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3347](http://purl.obolibrary.org/obo/DOID_3347)                                                                                             |
| `ORDO:('ORDO', '678')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3389](http://purl.obolibrary.org/obo/DOID_3389)                                                                                             |
| `ORDO:('ORDO', '611')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3429](http://purl.obolibrary.org/obo/DOID_3429)                                                                                             |
| `ORDO:('ORDO', '648')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3490](http://purl.obolibrary.org/obo/DOID_3490)                                                                                             |
| `ORDO:('ORDO', '590')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3635](http://purl.obolibrary.org/obo/DOID_3635)                                                                                             |
| `ORDO:('ORDO', '79243')`  |              1 | [http://purl.obolibrary.org/obo/DOID_3649](http://purl.obolibrary.org/obo/DOID_3649)                                                                                             |
| `ORDO:('ORDO', '506')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3652](http://purl.obolibrary.org/obo/DOID_3652)                                                                                             |
| `ORDO:('ORDO', '231531')` |              1 | [http://purl.obolibrary.org/obo/DOID_3753](http://purl.obolibrary.org/obo/DOID_3753)                                                                                             |
| `ORDO:('ORDO', '231537')` |              1 | [http://purl.obolibrary.org/obo/DOID_3753](http://purl.obolibrary.org/obo/DOID_3753)                                                                                             |
| `ORDO:('ORDO', '280663')` |              1 | [http://purl.obolibrary.org/obo/DOID_3753](http://purl.obolibrary.org/obo/DOID_3753)                                                                                             |
| `ORDO:('ORDO', '79430')`  |              1 | [http://purl.obolibrary.org/obo/DOID_3753](http://purl.obolibrary.org/obo/DOID_3753)                                                                                             |
| `ORDO:('ORDO', '745')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3756](http://purl.obolibrary.org/obo/DOID_3756)                                                                                             |
| `ORDO:('ORDO', '2140')`   |              1 | [http://purl.obolibrary.org/obo/DOID_3827](http://purl.obolibrary.org/obo/DOID_3827)                                                                                             |
| `ORDO:('ORDO', '2869')`   |              1 | [http://purl.obolibrary.org/obo/DOID_3852](http://purl.obolibrary.org/obo/DOID_3852)                                                                                             |
| `ORDO:('ORDO', '144')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3883](http://purl.obolibrary.org/obo/DOID_3883)                                                                                             |
| `ORDO:('ORDO', '740')`    |              1 | [http://purl.obolibrary.org/obo/DOID_3911](http://purl.obolibrary.org/obo/DOID_3911)                                                                                             |
| `ORDO:('ORDO', '75249')`  |              1 | [http://purl.obolibrary.org/obo/DOID_397](http://purl.obolibrary.org/obo/DOID_397)                                                                                               |
| `ORDO:('ORDO', '157850')` |              1 | [http://purl.obolibrary.org/obo/DOID_3981](http://purl.obolibrary.org/obo/DOID_3981)                                                                                             |
| `ORDO:('ORDO', '95429')`  |              1 | [http://purl.obolibrary.org/obo/DOID_4028](http://purl.obolibrary.org/obo/DOID_4028)                                                                                             |
| `ORDO:('ORDO', '49042')`  |              1 | [http://purl.obolibrary.org/obo/DOID_4154](http://purl.obolibrary.org/obo/DOID_4154)                                                                                             |
| `ORDO:('ORDO', '79365')`  |              1 | [http://purl.obolibrary.org/obo/DOID_420](http://purl.obolibrary.org/obo/DOID_420)                                                                                               |
| `ORDO:('ORDO', '370334')` |              1 | [http://purl.obolibrary.org/obo/DOID_4232](http://purl.obolibrary.org/obo/DOID_4232)                                                                                             |
| `ORDO:('ORDO', '163699')` |              1 | [http://purl.obolibrary.org/obo/DOID_4239](http://purl.obolibrary.org/obo/DOID_4239)                                                                                             |
| `ORDO:('ORDO', '185')`    |              1 | [http://purl.obolibrary.org/obo/DOID_4297](http://purl.obolibrary.org/obo/DOID_4297)                                                                                             |
| `ORDO:('ORDO', '320')`    |              1 | [http://purl.obolibrary.org/obo/DOID_4367](http://purl.obolibrary.org/obo/DOID_4367)                                                                                             |
| `ORDO:('ORDO', '279')`    |              1 | [http://purl.obolibrary.org/obo/DOID_4448](http://purl.obolibrary.org/obo/DOID_4448)                                                                                             |
| `ORDO:('ORDO', '217071')` |              1 | [http://purl.obolibrary.org/obo/DOID_4450](http://purl.obolibrary.org/obo/DOID_4450)                                                                                             |
| `ORDO:('ORDO', '235936')` |              1 | [http://purl.obolibrary.org/obo/DOID_446](http://purl.obolibrary.org/obo/DOID_446)                                                                                               |
| `ORDO:('ORDO', '2108')`   |              1 | [http://purl.obolibrary.org/obo/DOID_4534](http://purl.obolibrary.org/obo/DOID_4534)                                                                                             |
| `ORDO:('ORDO', '55654')`  |              1 | [http://purl.obolibrary.org/obo/DOID_4535](http://purl.obolibrary.org/obo/DOID_4535)                                                                                             |
| `ORDO:('ORDO', '2162')`   |              1 | [http://purl.obolibrary.org/obo/DOID_4621](http://purl.obolibrary.org/obo/DOID_4621)                                                                                             |
| `ORDO:('ORDO', '296')`    |              1 | [http://purl.obolibrary.org/obo/DOID_4624](http://purl.obolibrary.org/obo/DOID_4624)                                                                                             |
| `ORDO:('ORDO', '304')`    |              1 | [http://purl.obolibrary.org/obo/DOID_4644](http://purl.obolibrary.org/obo/DOID_4644)                                                                                             |
| `ORDO:('ORDO', '754')`    |              1 | [http://purl.obolibrary.org/obo/DOID_4674](http://purl.obolibrary.org/obo/DOID_4674)                                                                                             |
| `ORDO:('ORDO', '862')`    |              1 | [http://purl.obolibrary.org/obo/DOID_4990](http://purl.obolibrary.org/obo/DOID_4990)                                                                                             |
| `ORDO:('ORDO', '137')`    |              1 | [http://purl.obolibrary.org/obo/DOID_5212](http://purl.obolibrary.org/obo/DOID_5212)                                                                                             |
| `ORDO:('ORDO', '95159')`  |              1 | [http://purl.obolibrary.org/obo/DOID_5230](http://purl.obolibrary.org/obo/DOID_5230)                                                                                             |
| `ORDO:('ORDO', '3103')`   |              1 | [http://purl.obolibrary.org/obo/DOID_5325](http://purl.obolibrary.org/obo/DOID_5325)                                                                                             |
| `ORDO:('ORDO', '99967')`  |              1 | [http://purl.obolibrary.org/obo/DOID_5363](http://purl.obolibrary.org/obo/DOID_5363)                                                                                             |
| `ORDO:('ORDO', '280110')` |              1 | [http://purl.obolibrary.org/obo/DOID_5408](http://purl.obolibrary.org/obo/DOID_5408)                                                                                             |
| `ORDO:('ORDO', '619')`    |              1 | [http://purl.obolibrary.org/obo/DOID_5426](http://purl.obolibrary.org/obo/DOID_5426)                                                                                             |
| `ORDO:('ORDO', '116')`    |              1 | [http://purl.obolibrary.org/obo/DOID_5572](http://purl.obolibrary.org/obo/DOID_5572)                                                                                             |
| `ORDO:('ORDO', '902')`    |              1 | [http://purl.obolibrary.org/obo/DOID_5688](http://purl.obolibrary.org/obo/DOID_5688)                                                                                             |
| `ORDO:('ORDO', '98673')`  |              1 | [http://purl.obolibrary.org/obo/DOID_5723](http://purl.obolibrary.org/obo/DOID_5723)                                                                                             |
| `ORDO:('ORDO', '760')`    |              1 | [http://purl.obolibrary.org/obo/DOID_5813](http://purl.obolibrary.org/obo/DOID_5813)                                                                                             |
| `ORDO:('ORDO', '101972')` |              1 | [http://purl.obolibrary.org/obo/DOID_628](http://purl.obolibrary.org/obo/DOID_628)                                                                                               |
| `ORDO:('ORDO', '3426')`   |              1 | [http://purl.obolibrary.org/obo/DOID_6406](http://purl.obolibrary.org/obo/DOID_6406)                                                                                             |
| `ORDO:('ORDO', '201')`    |              1 | [http://purl.obolibrary.org/obo/DOID_6457](http://purl.obolibrary.org/obo/DOID_6457)                                                                                             |
| `ORDO:('ORDO', '2968')`   |              1 | [http://purl.obolibrary.org/obo/DOID_6612](http://purl.obolibrary.org/obo/DOID_6612)                                                                                             |
| `ORDO:('ORDO', '3261')`   |              1 | [http://purl.obolibrary.org/obo/DOID_6688](http://purl.obolibrary.org/obo/DOID_6688)                                                                                             |
| `ORDO:('ORDO', '99772')`  |              1 | [http://purl.obolibrary.org/obo/DOID_674](http://purl.obolibrary.org/obo/DOID_674)                                                                                               |
| `ORDO:('ORDO', '92')`     |              1 | [http://purl.obolibrary.org/obo/DOID_676](http://purl.obolibrary.org/obo/DOID_676)                                                                                               |
| `ORDO:('ORDO', '683')`    |              1 | [http://purl.obolibrary.org/obo/DOID_678](http://purl.obolibrary.org/obo/DOID_678)                                                                                               |
| `ORDO:('ORDO', '88673')`  |              1 | [http://purl.obolibrary.org/obo/DOID_684](http://purl.obolibrary.org/obo/DOID_684)                                                                                               |
| `ORDO:('ORDO', '1635')`   |              1 | [http://purl.obolibrary.org/obo/DOID_701](http://purl.obolibrary.org/obo/DOID_701)                                                                                               |
| `ORDO:('ORDO', '825')`    |              1 | [http://purl.obolibrary.org/obo/DOID_7147](http://purl.obolibrary.org/obo/DOID_7147)                                                                                             |
| `ORDO:('ORDO', '647')`    |              1 | [http://purl.obolibrary.org/obo/DOID_7400](http://purl.obolibrary.org/obo/DOID_7400)                                                                                             |
| `ORDO:('ORDO', '635')`    |              1 | [http://purl.obolibrary.org/obo/DOID_769](http://purl.obolibrary.org/obo/DOID_769)                                                                                               |
| `ORDO:('ORDO', '99819')`  |              1 | [http://purl.obolibrary.org/obo/DOID_7998](http://purl.obolibrary.org/obo/DOID_7998)                                                                                             |
| `ORDO:('ORDO', '280133')` |              1 | [http://purl.obolibrary.org/obo/DOID_8354](http://purl.obolibrary.org/obo/DOID_8354)                                                                                             |
| `ORDO:('ORDO', '50')`     |              1 | [http://purl.obolibrary.org/obo/DOID_8461](http://purl.obolibrary.org/obo/DOID_8461)                                                                                             |
| `ORDO:('ORDO', '423')`    |              1 | [http://purl.obolibrary.org/obo/DOID_8545](http://purl.obolibrary.org/obo/DOID_8545)                                                                                             |
| `ORDO:('ORDO', '521')`    |              1 | [http://purl.obolibrary.org/obo/DOID_8552](http://purl.obolibrary.org/obo/DOID_8552)                                                                                             |
| `ORDO:('ORDO', '98293')`  |              1 | [http://purl.obolibrary.org/obo/DOID_8567](http://purl.obolibrary.org/obo/DOID_8567)                                                                                             |
| `ORDO:('ORDO', '543')`    |              1 | [http://purl.obolibrary.org/obo/DOID_8584](http://purl.obolibrary.org/obo/DOID_8584)                                                                                             |
| `ORDO:('ORDO', '93921')`  |              1 | [http://purl.obolibrary.org/obo/DOID_8712](http://purl.obolibrary.org/obo/DOID_8712)                                                                                             |
| `ORDO:('ORDO', '730')`    |              1 | [http://purl.obolibrary.org/obo/DOID_898](http://purl.obolibrary.org/obo/DOID_898)                                                                                               |
| `ORDO:('ORDO', '912')`    |              1 | [http://purl.obolibrary.org/obo/DOID_905](http://purl.obolibrary.org/obo/DOID_905)                                                                                               |
| `ORDO:('ORDO', '536')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9074](http://purl.obolibrary.org/obo/DOID_9074)                                                                                             |
| `ORDO:('ORDO', '507')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9146](http://purl.obolibrary.org/obo/DOID_9146)                                                                                             |
| `ORDO:('ORDO', '52')`     |              1 | [http://purl.obolibrary.org/obo/DOID_9245](http://purl.obolibrary.org/obo/DOID_9245)                                                                                             |
| `ORDO:('ORDO', '85458')`  |              1 | [http://purl.obolibrary.org/obo/DOID_9246](http://purl.obolibrary.org/obo/DOID_9246)                                                                                             |
| `ORDO:('ORDO', '282')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9255](http://purl.obolibrary.org/obo/DOID_9255)                                                                                             |
| `ORDO:('ORDO', '3440')`   |              1 | [http://purl.obolibrary.org/obo/DOID_9258](http://purl.obolibrary.org/obo/DOID_9258)                                                                                             |
| `ORDO:('ORDO', '895')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9258](http://purl.obolibrary.org/obo/DOID_9258)                                                                                             |
| `ORDO:('ORDO', '150')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9261](http://purl.obolibrary.org/obo/DOID_9261)                                                                                             |
| `ORDO:('ORDO', '394')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9263](http://purl.obolibrary.org/obo/DOID_9263)                                                                                             |
| `ORDO:('ORDO', '214')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9266](http://purl.obolibrary.org/obo/DOID_9266)                                                                                             |
| `ORDO:('ORDO', '511')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9269](http://purl.obolibrary.org/obo/DOID_9269)                                                                                             |
| `ORDO:('ORDO', '56')`     |              1 | [http://purl.obolibrary.org/obo/DOID_9270](http://purl.obolibrary.org/obo/DOID_9270)                                                                                             |
| `ORDO:('ORDO', '2203')`   |              1 | [http://purl.obolibrary.org/obo/DOID_9274](http://purl.obolibrary.org/obo/DOID_9274)                                                                                             |
| `ORDO:('ORDO', '716')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9281](http://purl.obolibrary.org/obo/DOID_9281)                                                                                             |
| `ORDO:('ORDO', '95494')`  |              1 | [http://purl.obolibrary.org/obo/DOID_9406](http://purl.obolibrary.org/obo/DOID_9406)                                                                                             |
| `ORDO:('ORDO', '2614')`   |              1 | [http://purl.obolibrary.org/obo/DOID_9467](http://purl.obolibrary.org/obo/DOID_9467)                                                                                             |
| `ORDO:('ORDO', '633')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9521](http://purl.obolibrary.org/obo/DOID_9521)                                                                                             |
| `ORDO:('ORDO', '29073')`  |              1 | [http://purl.obolibrary.org/obo/DOID_9538](http://purl.obolibrary.org/obo/DOID_9538)                                                                                             |
| `ORDO:('ORDO', '244')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9562](http://purl.obolibrary.org/obo/DOID_9562)                                                                                             |
| `ORDO:('ORDO', '60033')`  |              1 | [http://purl.obolibrary.org/obo/DOID_9563](http://purl.obolibrary.org/obo/DOID_9563)                                                                                             |
| `ORDO:('ORDO', '289365')` |              1 | [http://purl.obolibrary.org/obo/DOID_9620](http://purl.obolibrary.org/obo/DOID_9620)                                                                                             |
| `ORDO:('ORDO', '211062')` |              1 | [http://purl.obolibrary.org/obo/DOID_963](http://purl.obolibrary.org/obo/DOID_963)                                                                                               |
| `ORDO:('ORDO', '651')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9649](http://purl.obolibrary.org/obo/DOID_9649)                                                                                             |
| `ORDO:('ORDO', '329211')` |              1 | [http://purl.obolibrary.org/obo/DOID_9719](http://purl.obolibrary.org/obo/DOID_9719)                                                                                             |
| `ORDO:('ORDO', '180')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9821](http://purl.obolibrary.org/obo/DOID_9821)                                                                                             |
| `ORDO:('ORDO', '98895')`  |              1 | [http://purl.obolibrary.org/obo/DOID_9883](http://purl.obolibrary.org/obo/DOID_9883)                                                                                             |
| `ORDO:('ORDO', '513')`    |              1 | [http://purl.obolibrary.org/obo/DOID_9952](http://purl.obolibrary.org/obo/DOID_9952)                                                                                             |
| `ORDO:('ORDO', '2248')`   |              1 | [http://purl.obolibrary.org/obo/DOID_9955](http://purl.obolibrary.org/obo/DOID_9955)                                                                                             |
| `ORDO:('ORDO', '168956')` |              1 | [http://purl.obolibrary.org/obo/DOID_999](http://purl.obolibrary.org/obo/DOID_999)                                                                                               |

## `Wikipedia`: Wikipedia

Overall, there were 7 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                         |   usages_count | usages                                                                                 |
|-------------------------------------------------------|----------------|----------------------------------------------------------------------------------------|
| `Wikipedia:('Wikipedia', 'Ligand_(biochemistry)')`    |              1 | [http://purl.obolibrary.org/obo/GO_0005102](http://purl.obolibrary.org/obo/GO_0005102) |
| `Wikipedia:('Wikipedia', 'Binding_(molecular)')`      |              1 | [http://purl.obolibrary.org/obo/GO_0005488](http://purl.obolibrary.org/obo/GO_0005488) |
| `Wikipedia:('Wikipedia', 'Transcription_(genetics)')` |              1 | [http://purl.obolibrary.org/obo/GO_0006351](http://purl.obolibrary.org/obo/GO_0006351) |
| `Wikipedia:('Wikipedia', 'Translation_(genetics)')`   |              1 | [http://purl.obolibrary.org/obo/GO_0006412](http://purl.obolibrary.org/obo/GO_0006412) |
| `Wikipedia:('Wikipedia', 'Autophagy_(cellular)')`     |              1 | [http://purl.obolibrary.org/obo/GO_0006914](http://purl.obolibrary.org/obo/GO_0006914) |
| `Wikipedia:('Wikipedia', 'Regeneration_(biology)')`   |              1 | [http://purl.obolibrary.org/obo/GO_0031099](http://purl.obolibrary.org/obo/GO_0031099) |
| `Wikipedia:('Wikipedia', 'Bleb_(cell_biology)')`      |              1 | [http://purl.obolibrary.org/obo/GO_0032059](http://purl.obolibrary.org/obo/GO_0032059) |

