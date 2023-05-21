# cl

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `cl`. See the [GitHub repository](https://github.com/obophenotype/cell-ontology).


## `BTO`: BRENDA Tissue Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `BTO` (standardized to Bioregistry
prefix [`bto`](https://bioregistry.io/bto)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `BTO:000125`    |              1 | [CL:1000398](http://purl.obolibrary.org/obo/CL_1000398) |

## `CARO`: Common Anatomy Reference Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `CARO` (standardized to Bioregistry
prefix [`caro`](https://bioregistry.io/caro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                           |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `CARO:mah`      |              2 | [CL:0000000](http://purl.obolibrary.org/obo/CL_0000000), [CL:0000003](http://purl.obolibrary.org/obo/CL_0000003) |

## `CL`: Cell Ontology

Overall, there were 22 invalid
xrefs to external prefixed with `CL` (standardized to Bioregistry
prefix [`cl`](https://bioregistry.io/cl)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                            |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CL:CVS`                                 |             16 | [CL:0000212](http://purl.obolibrary.org/obo/CL_0000212), [CL:0005000](http://purl.obolibrary.org/obo/CL_0005000), [CL:0005001](http://purl.obolibrary.org/obo/CL_0005001), [CL:0005002](http://purl.obolibrary.org/obo/CL_0005002), [CL:0005003](http://purl.obolibrary.org/obo/CL_0005003), ... |
| `CL:MAH`                                 |              3 | [CL:0007007](http://purl.obolibrary.org/obo/CL_0007007), [CL:0007008](http://purl.obolibrary.org/obo/CL_0007008), [CL:0007011](http://purl.obolibrary.org/obo/CL_0007011)                                                                                                                        |
| `CL:curator`                             |              1 | [CL:0005018](http://purl.obolibrary.org/obo/CL_0005018)                                                                                                                                                                                                                                          |
| `CL:patterns/cellPartOfAnatomicalEntity` |              1 | [CL:0011030](http://purl.obolibrary.org/obo/CL_0011030)                                                                                                                                                                                                                                          |
| `CL:cjm`                                 |              1 | [CL:1000742](http://purl.obolibrary.org/obo/CL_1000742)                                                                                                                                                                                                                                          |

## `DOI`: Digital Object Identifier

Overall, there were 1 invalid
xrefs to external prefixed with `DOI` (standardized to Bioregistry
prefix [`doi`](https://bioregistry.io/doi)) that
did not match the standard pattern `^10.\d{2,9}/.*$`.

| external_xref                               |   usages_count | usages                                                  |
|---------------------------------------------|----------------|---------------------------------------------------------|
| `DOI:https://doi.org/10.1378/chest.12-2762` |              1 | [CL:0000158](http://purl.obolibrary.org/obo/CL_0000158) |

## `FB`: FlyBase Gene

Overall, there were 25 invalid
xrefs to external prefixed with `FB` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FB:ma`         |             25 | [CL:0000004](http://purl.obolibrary.org/obo/CL_0000004), [CL:0000063](http://purl.obolibrary.org/obo/CL_0000063), [CL:0000066](http://purl.obolibrary.org/obo/CL_0000066), [CL:0000134](http://purl.obolibrary.org/obo/CL_0000134), [CL:0000144](http://purl.obolibrary.org/obo/CL_0000144), ... |

## `Flybase`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `Flybase` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `Flybase:dsj`   |              1 | [CL:0000362](http://purl.obolibrary.org/obo/CL_0000362) |

## `FlyBase`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `FlyBase` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `FlyBase:ds`    |              1 | [CL:0000463](http://purl.obolibrary.org/obo/CL_0000463) |

## `GC`: Genetic Code

Overall, there were 1 invalid
xrefs to external prefixed with `GC` (standardized to Bioregistry
prefix [`gc`](https://bioregistry.io/gc)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `GC:tfm`        |              1 | [CL:0002597](http://purl.obolibrary.org/obo/CL_0002597) |

## `GO`: Gene Ontology

Overall, there were 17 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:tfm`        |             16 | [CL:0000478](http://purl.obolibrary.org/obo/CL_0000478), [CL:0000479](http://purl.obolibrary.org/obo/CL_0000479), [CL:0000480](http://purl.obolibrary.org/obo/CL_0000480), [CL:0000481](http://purl.obolibrary.org/obo/CL_0000481), [CL:0000482](http://purl.obolibrary.org/obo/CL_0000482), ... |
| `GO:cvs`        |              1 | [CL:0005008](http://purl.obolibrary.org/obo/CL_0005008)                                                                                                                                                                                                                                          |

## `HPA`: Human Protein Atlas tissue profile information

Overall, there were 7 invalid
xrefs to external prefixed with `HPA` (standardized to Bioregistry
prefix [`hpa`](https://bioregistry.io/hpa)) that
did not match the standard pattern `^ENSG\d{11}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HPA:HPA`       |              6 | [CL:1001586](http://purl.obolibrary.org/obo/CL_1001586), [CL:1001591](http://purl.obolibrary.org/obo/CL_1001591), [CL:1001593](http://purl.obolibrary.org/obo/CL_1001593), [CL:1001596](http://purl.obolibrary.org/obo/CL_1001596), [CL:1001599](http://purl.obolibrary.org/obo/CL_1001599), ... |
| `HPA:Breast`    |              1 | [CL:1001583](http://purl.obolibrary.org/obo/CL_1001583)                                                                                                                                                                                                                                          |

## `KUPO`: Kidney and Urinary Pathway Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `KUPO` (standardized to Bioregistry
prefix [`kupo`](https://bioregistry.io/kupo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `KUPO:SJ`       |              1 | [CL:0002518](http://purl.obolibrary.org/obo/CL_0002518) |

## `MA`: Mouse adult gross anatomy

Overall, there were 4 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
prefix [`ma`](https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                             |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MA:ma`         |              4 | [CL:0000362](http://purl.obolibrary.org/obo/CL_0000362), [CL:0000724](http://purl.obolibrary.org/obo/CL_0000724), [CL:0000730](http://purl.obolibrary.org/obo/CL_0000730), [CL:0000731](http://purl.obolibrary.org/obo/CL_0000731) |

## `MESH`: Medical Subject Headings

Overall, there were 6 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref              |   usages_count | usages                                                  |
|----------------------------|----------------|---------------------------------------------------------|
| `MESH:A09.371.060.067.31`  |              1 | [CL:0000132](http://purl.obolibrary.org/obo/CL_0000132) |
| `MESH:A16.254.600`         |              1 | [CL:0000333](http://purl.obolibrary.org/obo/CL_0000333) |
| `MESH:A11.118.290.350.200` |              1 | [CL:0000547](http://purl.obolibrary.org/obo/CL_0000547) |
| `MESH:A11.070`             |              1 | [CL:0000568](http://purl.obolibrary.org/obo/CL_0000568) |
| `MESH:A03.492.766.440.250` |              1 | [CL:0000577](http://purl.obolibrary.org/obo/CL_0000577) |
| `MESH:A11.329.679`         |              1 | [CL:0000588](http://purl.obolibrary.org/obo/CL_0000588) |

## `MP`: Mammalian Phenotype Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `MP` (standardized to Bioregistry
prefix [`mp`](https://bioregistry.io/mp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `MP:19876834`   |              1 | [CL:0002488](http://purl.obolibrary.org/obo/CL_0002488) |

## `NCI_Thesaurus`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCI_Thesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                                   |   usages_count | usages                                                  |
|-------------------------------------------------|----------------|---------------------------------------------------------|
| `NCI_Thesaurus:Small_Intestinal_Glandular_Cell` |              1 | [CL:1001598](http://purl.obolibrary.org/obo/CL_1001598) |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 4 invalid
xrefs to external prefixed with `ncithesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                     |   usages_count | usages                                                  |
|-----------------------------------|----------------|---------------------------------------------------------|
| `ncithesaurus:Spermatogenic_Cell` |              1 | [CL:0000015](http://purl.obolibrary.org/obo/CL_0000015) |
| `ncithesaurus:Egg`                |              1 | [CL:0000021](http://purl.obolibrary.org/obo/CL_0000021) |
| `ncithesaurus:Beta_Cell`          |              1 | [CL:0000169](http://purl.obolibrary.org/obo/CL_0000169) |
| `ncithesaurus:Blastemal_Cell`     |              1 | [CL:0000354](http://purl.obolibrary.org/obo/CL_0000354) |

## `NIFSTD`: NIF Standard Ontology

Overall, there were 4 invalid
xrefs to external prefixed with `NIFSTD` (standardized to Bioregistry
prefix [`nif.std`](https://bioregistry.io/nif.std)) that
did not match the standard pattern `^BAMSC\d+$`.

| external_xref          |   usages_count | usages                                                                                                           |
|------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `NIFSTD:sao131261273`  |              2 | [CL:1001571](http://purl.obolibrary.org/obo/CL_1001571), [CL:1001571](http://purl.obolibrary.org/obo/CL_1001571) |
| `NIFSTD:sao1415726815` |              1 | [CL:0000119](http://purl.obolibrary.org/obo/CL_0000119)                                                          |
| `NIFSTD:sao862606388`  |              1 | [CL:0000598](http://purl.obolibrary.org/obo/CL_0000598)                                                          |

## `ReO`: Reagent Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `ReO` (standardized to Bioregistry
prefix [`reo`](https://bioregistry.io/reo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ReO:mhb`       |              7 | [CL:0000001](http://purl.obolibrary.org/obo/CL_0000001), [CL:0000002](http://purl.obolibrary.org/obo/CL_0000002), [CL:0000010](http://purl.obolibrary.org/obo/CL_0000010), [CL:0000578](http://purl.obolibrary.org/obo/CL_0000578), [CL:0001034](http://purl.obolibrary.org/obo/CL_0001034), ... |

## `SAO`: Subcellular Anatomy Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `SAO` (standardized to Bioregistry
prefix [`sao`](https://bioregistry.io/sao)) that
did not match the standard pattern `^\d+$`.

| external_xref      |   usages_count | usages                                                  |
|--------------------|----------------|---------------------------------------------------------|
| `SAO:sao131261273` |              1 | [CL:1001571](http://purl.obolibrary.org/obo/CL_1001571) |

## `SGD`: Saccharomyces Genome Database

Overall, there were 19 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
prefix [`sgd`](https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:clt`       |             19 | [CL:0000596](http://purl.obolibrary.org/obo/CL_0000596), [CL:0000597](http://purl.obolibrary.org/obo/CL_0000597), [CL:0000599](http://purl.obolibrary.org/obo/CL_0000599), [CL:0000605](http://purl.obolibrary.org/obo/CL_0000605), [CL:0000606](http://purl.obolibrary.org/obo/CL_0000606), ... |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 6 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                      |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:CVS`      |              5 | [CL:0005023](http://purl.obolibrary.org/obo/CL_0005023), [CL:0005024](http://purl.obolibrary.org/obo/CL_0005024), [CL:0005025](http://purl.obolibrary.org/obo/CL_0005025), [CL:0011100](http://purl.obolibrary.org/obo/CL_0011100), [CL:0015000](http://purl.obolibrary.org/obo/CL_0015000) |
| `ZFIN:YB`       |              1 | [CL:0011100](http://purl.obolibrary.org/obo/CL_0011100)                                                                                                                                                                                                                                     |

