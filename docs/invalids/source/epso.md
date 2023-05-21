# epso

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `epso`.


## `ICD10`: International Classification of Diseases, 10th Revision

Overall, there were 6 invalid
xrefs to external prefixed with `ICD10` (standardized to Bioregistry
prefix [`icd10`](https://bioregistry.io/icd10)) that
did not match the standard pattern `^(([XVI]+)|([A-Z][0-9]+((-[A-Z][0-9]+)|(\.[0-9]))?))$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `ICD10:Q00.Q99` |              1 | [MONDO:0000839](http://purl.obolibrary.org/obo/MONDO_0000839) |
| `ICD10:C00.D48` |              1 | [MONDO:0005070](http://purl.obolibrary.org/obo/MONDO_0005070) |
| `ICD10:F00.F99` |              1 | [MONDO:0005084](http://purl.obolibrary.org/obo/MONDO_0005084) |
| `ICD10:G47.41`  |              1 | [MONDO:0016158](http://purl.obolibrary.org/obo/MONDO_0016158) |
| `ICD10:G47.419` |              1 | [MONDO:0016158](http://purl.obolibrary.org/obo/MONDO_0016158) |
| `ICD10:G47.24`  |              1 | [MONDO:0019137](http://purl.obolibrary.org/obo/MONDO_0019137) |

## `ICD9`: International Classification of Diseases, 9th Revision

Overall, there were 2 invalid
xrefs to external prefixed with `ICD9` (standardized to Bioregistry
prefix [`icd9`](https://bioregistry.io/icd9)) that
did not match the standard pattern `^(\d\d\d|V\d\d|E[8-9]\d\d)(\.\d{1,2})?$`.

| external_xref     |   usages_count | usages                                                        |
|-------------------|----------------|---------------------------------------------------------------|
| `ICD9:140-239.99` |              1 | [MONDO:0005070](http://purl.obolibrary.org/obo/MONDO_0005070) |
| `ICD9:290-299.99` |              1 | [MONDO:0005084](http://purl.obolibrary.org/obo/MONDO_0005084) |

## `ICD9CM`: International Classification of Diseases, 9th Revision, Clinical Modification

Overall, there were 10 invalid
xrefs to external prefixed with `ICD9CM` (standardized to Bioregistry
prefix [`icd9cm`](https://bioregistry.io/icd9cm)) that
did not match the standard pattern `^([\dA-Z]\d{2}(\.\d{1,3}|))|(\d{2}(\.\d{1,2}|))$`.

| external_xref       |   usages_count | usages                                                  |
|---------------------|----------------|---------------------------------------------------------|
| `ICD9CM:401-405.99` |              1 | [DOID:10763](http://purl.obolibrary.org/obo/DOID_10763) |
| `ICD9CM:110-118.99` |              1 | [DOID:1564](http://purl.obolibrary.org/obo/DOID_1564)   |
| `ICD9CM:510-519.99` |              1 | [DOID:1579](http://purl.obolibrary.org/obo/DOID_1579)   |
| `ICD9CM:410-414.99` |              1 | [DOID:3393](http://purl.obolibrary.org/obo/DOID_3393)   |
| `ICD9CM:240-246.99` |              1 | [DOID:50](http://purl.obolibrary.org/obo/DOID_50)       |
| `ICD9CM:042-042.99` |              1 | [DOID:526](http://purl.obolibrary.org/obo/DOID_526)     |
| `ICD9CM:350-359.99` |              1 | [DOID:574](http://purl.obolibrary.org/obo/DOID_574)     |
| `ICD9CM:430-438.99` |              1 | [DOID:6713](http://purl.obolibrary.org/obo/DOID_6713)   |
| `ICD9CM:520-579.99` |              1 | [DOID:77](http://purl.obolibrary.org/obo/DOID_77)       |
| `ICD9CM:060-066.99` |              1 | [DOID:934](http://purl.obolibrary.org/obo/DOID_934)     |

## `ICDO`: International Classification of Diseases for Oncology

Overall, there were 3 invalid
xrefs to external prefixed with `ICDO` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `ICDO:M9400/3`  |              1 | [DOID:3069](http://purl.obolibrary.org/obo/DOID_3069)         |
| `ICDO:M9530/3`  |              1 | [DOID:3565](http://purl.obolibrary.org/obo/DOID_3565)         |
| `ICDO:8000/6`   |              1 | [MONDO:0024883](http://purl.obolibrary.org/obo/MONDO_0024883) |

## `KEGG`: Kyoto Encyclopedia of Genes and Genomes

Overall, there were 9 invalid
xrefs to external prefixed with `KEGG` (standardized to Bioregistry
prefix [`kegg`](https://bioregistry.io/kegg)) that
did not match the standard pattern `^([CHDEGTMKR]\d+)|(\w+:[\w\d\.-]*)|([a-z]{3,5})|(\w{2,4}\d{5})$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `KEGG:05321`    |              1 | [DOID:0050589](http://purl.obolibrary.org/obo/DOID_0050589)   |
| `KEGG:05034`    |              1 | [DOID:0050741](http://purl.obolibrary.org/obo/DOID_0050741)   |
| `KEGG:05143`    |              1 | [DOID:10112](http://purl.obolibrary.org/obo/DOID_10112)       |
| `KEGG:05010`    |              1 | [DOID:10652](http://purl.obolibrary.org/obo/DOID_10652)       |
| `KEGG:05310`    |              1 | [DOID:2841](http://purl.obolibrary.org/obo/DOID_2841)         |
| `KEGG:05323`    |              1 | [DOID:7148](http://purl.obolibrary.org/obo/DOID_7148)         |
| `KEGG:05322`    |              1 | [DOID:9074](http://purl.obolibrary.org/obo/DOID_9074)         |
| `KEGG:04940`    |              1 | [DOID:9744](http://purl.obolibrary.org/obo/DOID_9744)         |
| `KEGG:05214`    |              1 | [MONDO:0015917](http://purl.obolibrary.org/obo/MONDO_0015917) |

## `MESH`: Medical Subject Headings

Overall, there were 18 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                          |   usages_count | usages                                                          |
|----------------------------------------|----------------|-----------------------------------------------------------------|
| `MESH:A08.186.211.577.750`             |              1 | [UBERON:0000446](http://purl.obolibrary.org/obo/UBERON_0000446) |
| `MESH:A08.186.211.730.885.213.270.700` |              1 | [UBERON:0000451](http://purl.obolibrary.org/obo/UBERON_0000451) |
| `MESH:A08.186.211.730.885.213`         |              1 | [UBERON:0000956](http://purl.obolibrary.org/obo/UBERON_0000956) |
| `MESH:A08.186.211.730.885.213.270.548` |              1 | [UBERON:0001384](http://purl.obolibrary.org/obo/UBERON_0001384) |
| `MESH:A08.186.211.730.885.213.863`     |              1 | [UBERON:0001871](http://purl.obolibrary.org/obo/UBERON_0001871) |
| `MESH:A08.186.211.730.885.213.670`     |              1 | [UBERON:0001872](http://purl.obolibrary.org/obo/UBERON_0001872) |
| `MESH:A08.186.211.577.090`             |              1 | [UBERON:0001876](http://purl.obolibrary.org/obo/UBERON_0001876) |
| `MESH:A08.186.211.730.385`             |              1 | [UBERON:0001894](http://purl.obolibrary.org/obo/UBERON_0001894) |
| `MESH:A08.186.211.730.385.826`         |              1 | [UBERON:0001897](http://purl.obolibrary.org/obo/UBERON_0001897) |
| `MESH:A08.186.211.577.482`             |              1 | [UBERON:0001898](http://purl.obolibrary.org/obo/UBERON_0001898) |
| `MESH:A08.186.211.132.659.237.816`     |              1 | [UBERON:0001945](http://purl.obolibrary.org/obo/UBERON_0001945) |
| `MESH:A08.186.211.132.659.237.364`     |              1 | [UBERON:0001946](http://purl.obolibrary.org/obo/UBERON_0001946) |
| `MESH:A08.186.211.730.885.213.571`     |              1 | [UBERON:0002021](http://purl.obolibrary.org/obo/UBERON_0002021) |
| `MESH:A08.186.211.577.699.573`         |              1 | [UBERON:0002264](http://purl.obolibrary.org/obo/UBERON_0002264) |
| `MESH:A08.186.211.730.885.362`         |              1 | [UBERON:0002336](http://purl.obolibrary.org/obo/UBERON_0002336) |
| `MESH:A08.186.211.577.710.225`         |              1 | [UBERON:0002728](http://purl.obolibrary.org/obo/UBERON_0002728) |
| `MESH:A08.186.211.730.885.213.670.675` |              1 | [UBERON:0008930](http://purl.obolibrary.org/obo/UBERON_0008930) |
| `MESH:A08.186.211.730.885.213.270`     |              1 | [UBERON:0016525](http://purl.obolibrary.org/obo/UBERON_0016525) |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 5 invalid
xrefs to external prefixed with `ncithesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                           |   usages_count | usages                                                          |
|-----------------------------------------|----------------|-----------------------------------------------------------------|
| `ncithesaurus:Parieto-occipital_Sulcus` |              1 | [UBERON:0002695](http://purl.obolibrary.org/obo/UBERON_0002695) |
| `ncithesaurus:Middle_Frontal_Gyrus`     |              1 | [UBERON:0002702](http://purl.obolibrary.org/obo/UBERON_0002702) |
| `ncithesaurus:Inferior_Temporal_Gyrus`  |              1 | [UBERON:0002751](http://purl.obolibrary.org/obo/UBERON_0002751) |
| `ncithesaurus:Superior_Temporal_Gyrus`  |              1 | [UBERON:0002769](http://purl.obolibrary.org/obo/UBERON_0002769) |
| `ncithesaurus:Middle_Temporal_Gyrus`    |              1 | [UBERON:0002771](http://purl.obolibrary.org/obo/UBERON_0002771) |

## `NIFSTD`: NIF Standard Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `NIFSTD` (standardized to Bioregistry
prefix [`nif.std`](https://bioregistry.io/nif.std)) that
did not match the standard pattern `^BAMSC\d+$`.

| external_xref          |   usages_count | usages                                                        |
|------------------------|----------------|---------------------------------------------------------------|
| `NIFSTD:birnlex_12669` |              1 | [MONDO:0005084](http://purl.obolibrary.org/obo/MONDO_0005084) |

## `OMIM`: Online Mendelian Inheritance in Man

Overall, there were 11 invalid
xrefs to external prefixed with `OMIM` (standardized to Bioregistry
prefix [`omim`](https://bioregistry.io/omim)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `OMIM:PS102300` |              1 | [DOID:0050425](http://purl.obolibrary.org/obo/DOID_0050425) |
| `OMIM:PS601144` |              1 | [DOID:0050451](http://purl.obolibrary.org/obo/DOID_0050451) |
| `OMIM:PS266600` |              1 | [DOID:0050589](http://purl.obolibrary.org/obo/DOID_0050589) |
| `OMIM:PS604348` |              1 | [DOID:0050628](http://purl.obolibrary.org/obo/DOID_0050628) |
| `OMIM:PS308350` |              1 | [DOID:0050709](http://purl.obolibrary.org/obo/DOID_0050709) |
| `OMIM:PS600513` |              1 | [DOID:0060681](http://purl.obolibrary.org/obo/DOID_0060681) |
| `OMIM:PS191100` |              1 | [DOID:13515](http://purl.obolibrary.org/obo/DOID_13515)     |
| `OMIM:PS256730` |              1 | [DOID:14503](http://purl.obolibrary.org/obo/DOID_14503)     |
| `OMIM:PS192500` |              1 | [DOID:2843](http://purl.obolibrary.org/obo/DOID_2843)       |
| `OMIM:PS177900` |              1 | [DOID:8893](http://purl.obolibrary.org/obo/DOID_8893)       |
| `OMIM:PS254800` |              1 | [DOID:891](http://purl.obolibrary.org/obo/DOID_891)         |

## `UMLS`: Unified Medical Language System Concept Unique Identifier

Overall, there were 24 invalid
xrefs to external prefixed with `UMLS` (standardized to Bioregistry
prefix [`umls`](https://bioregistry.io/umls)) that
did not match the standard pattern `^C\d+$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `UMLS:CN227588` |              1 | [MONDO:0000456](http://purl.obolibrary.org/obo/MONDO_0000456) |
| `UMLS:CN232116` |              1 | [MONDO:0000839](http://purl.obolibrary.org/obo/MONDO_0000839) |
| `UMLS:CN236628` |              1 | [MONDO:0005070](http://purl.obolibrary.org/obo/MONDO_0005070) |
| `UMLS:CN240636` |              1 | [MONDO:0005084](http://purl.obolibrary.org/obo/MONDO_0005084) |
| `UMLS:CN200685` |              1 | [MONDO:0007295](http://purl.obolibrary.org/obo/MONDO_0007295) |
| `UMLS:CN203406` |              1 | [MONDO:0009945](http://purl.obolibrary.org/obo/MONDO_0009945) |
| `UMLS:CN233170` |              1 | [MONDO:0014708](http://purl.obolibrary.org/obo/MONDO_0014708) |
| `UMLS:CN199399` |              1 | [MONDO:0015346](http://purl.obolibrary.org/obo/MONDO_0015346) |
| `UMLS:CN199955` |              1 | [MONDO:0015584](http://purl.obolibrary.org/obo/MONDO_0015584) |
| `UMLS:CN200058` |              1 | [MONDO:0015648](http://purl.obolibrary.org/obo/MONDO_0015648) |
| `UMLS:CN200064` |              1 | [MONDO:0015654](http://purl.obolibrary.org/obo/MONDO_0015654) |
| `UMLS:CN200066` |              1 | [MONDO:0015657](http://purl.obolibrary.org/obo/MONDO_0015657) |
| `UMLS:CN200068` |              1 | [MONDO:0015659](http://purl.obolibrary.org/obo/MONDO_0015659) |
| `UMLS:CN200514` |              1 | [MONDO:0015916](http://purl.obolibrary.org/obo/MONDO_0015916) |
| `UMLS:CN201945` |              1 | [MONDO:0016701](http://purl.obolibrary.org/obo/MONDO_0016701) |
| `UMLS:CN227171` |              1 | [MONDO:0017657](http://purl.obolibrary.org/obo/MONDO_0017657) |
| `UMLS:CN205631` |              1 | [MONDO:0019113](http://purl.obolibrary.org/obo/MONDO_0019113) |
| `UMLS:CN205780` |              1 | [MONDO:0019197](http://purl.obolibrary.org/obo/MONDO_0019197) |
| `UMLS:CN206266` |              1 | [MONDO:0019486](http://purl.obolibrary.org/obo/MONDO_0019486) |
| `UMLS:CN206974` |              1 | [MONDO:0020070](http://purl.obolibrary.org/obo/MONDO_0020070) |
| `UMLS:CN206975` |              1 | [MONDO:0020071](http://purl.obolibrary.org/obo/MONDO_0020071) |
| `UMLS:CN206976` |              1 | [MONDO:0020072](http://purl.obolibrary.org/obo/MONDO_0020072) |
| `UMLS:CN207128` |              1 | [MONDO:0020308](http://purl.obolibrary.org/obo/MONDO_0020308) |
| `UMLS:CN207131` |              1 | [MONDO:0020310](http://purl.obolibrary.org/obo/MONDO_0020310) |

