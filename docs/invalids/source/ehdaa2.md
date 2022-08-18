# ehdaa2

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `ehdaa2`. See the [GitHub repository](https://github.com/obophenotype/human-developmental-anatomy-ontology).


## `AEO`: Anatomical Entity Ontology

Overall, there were 111 invalid
xrefs to external prefixed with `AEO` (standardized to Bioregistry
prefix [`aeo`](https://bioregistry.io/aeo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AEO:JB`        |            111 | [AEO:0000078](http://purl.obolibrary.org/obo/AEO_0000078), [AEO:0000079](http://purl.obolibrary.org/obo/AEO_0000079), [AEO:0000080](http://purl.obolibrary.org/obo/AEO_0000080), [AEO:0000081](http://purl.obolibrary.org/obo/AEO_0000081), [AEO:0000082](http://purl.obolibrary.org/obo/AEO_0000082), ... |

## `AEO.`: Anatomical Entity Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `AEO.` (standardized to Bioregistry
prefix [`aeo`](https://bioregistry.io/aeo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `AEO.:JB`       |              1 | [AEO:0000203](http://purl.obolibrary.org/obo/AEO_0000203) |

## `CARO`: Common Anatomy Reference Ontology

Overall, there were 49 invalid
xrefs to external prefixed with `CARO` (standardized to Bioregistry
prefix [`caro`](https://bioregistry.io/caro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                       |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CARO:MAH`      |             47 | [AEO:0000013](http://purl.obolibrary.org/obo/AEO_0000013), [AEO:0000192](http://purl.obolibrary.org/obo/AEO_0000192), [AEO:0000193](http://purl.obolibrary.org/obo/AEO_0000193), [AEO:0000198](http://purl.obolibrary.org/obo/AEO_0000198), [CARO:0000000](http://purl.obolibrary.org/obo/CARO_0000000), ... |
| `CARO:mah`      |              2 | [CARO:0000062](http://purl.obolibrary.org/obo/CARO_0000062), [CL:0000000](http://purl.obolibrary.org/obo/CL_0000000)                                                                                                                                                                                         |

## `FB`: FlyBase Gene

Overall, there were 9 invalid
xrefs to external prefixed with `FB` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FB:ma`         |              9 | [CL:0000063](http://purl.obolibrary.org/obo/CL_0000063), [CL:0000066](http://purl.obolibrary.org/obo/CL_0000066), [CL:0000134](http://purl.obolibrary.org/obo/CL_0000134), [CL:0000144](http://purl.obolibrary.org/obo/CL_0000144), [CL:0000211](http://purl.obolibrary.org/obo/CL_0000211), ... |

## `FBbt`: Drosophila gross anatomy

Overall, there were 1 invalid
xrefs to external prefixed with `FBbt` (standardized to Bioregistry
prefix [`fbbt`](https://bioregistry.io/fbbt)) that
did not match the standard pattern `^\d{8}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `FBbt:DOS`      |              1 | [AEO:0000211](http://purl.obolibrary.org/obo/AEO_0000211) |

## `GO`: Gene Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `GO:curator`    |              1 | [AEO:0000147](http://purl.obolibrary.org/obo/AEO_0000147) |

## `MESH`: Medical Subject Headings

Overall, there were 19 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref       |   usages_count | usages                                                                                                           |
|---------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `MESH:A.08.637`     |              2 | [CL:0000125](http://purl.obolibrary.org/obo/CL_0000125), [CL:0000243](http://purl.obolibrary.org/obo/CL_0000243) |
| `MESH:A.11.872`     |              1 | [CL:0000034](http://purl.obolibrary.org/obo/CL_0000034)                                                          |
| `MESH:A.11.329.228` |              1 | [CL:0000057](http://purl.obolibrary.org/obo/CL_0000057)                                                          |
| `MESH:A.11.329.629` |              1 | [CL:0000062](http://purl.obolibrary.org/obo/CL_0000062)                                                          |
| `MESH:A.11.436`     |              1 | [CL:0000066](http://purl.obolibrary.org/obo/CL_0000066)                                                          |
| `MESH:A.08.663.358` |              1 | [CL:0000099](http://purl.obolibrary.org/obo/CL_0000099)                                                          |
| `MESH:A.08.637.200` |              1 | [CL:0000127](http://purl.obolibrary.org/obo/CL_0000127)                                                          |
| `MESH:A.08.637.600` |              1 | [CL:0000128](http://purl.obolibrary.org/obo/CL_0000128)                                                          |
| `MESH:A.11.329.114` |              1 | [CL:0000136](http://purl.obolibrary.org/obo/CL_0000136)                                                          |
| `MESH:A.11.329.171` |              1 | [CL:0000138](http://purl.obolibrary.org/obo/CL_0000138)                                                          |
| `MESH:A.06.688`     |              1 | [CL:0000165](http://purl.obolibrary.org/obo/CL_0000165)                                                          |
| `MESH:A.11.620`     |              1 | [CL:0000187](http://purl.obolibrary.org/obo/CL_0000187)                                                          |
| `MESH:A.11.620.520` |              1 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192)                                                          |
| `MESH:A.11.329.830` |              1 | [CL:0000499](http://purl.obolibrary.org/obo/CL_0000499)                                                          |
| `MESH:A.08.663.650` |              1 | [CL:0000526](http://purl.obolibrary.org/obo/CL_0000526)                                                          |
| `MESH:A.08.663.655` |              1 | [CL:0000527](http://purl.obolibrary.org/obo/CL_0000527)                                                          |
| `MESH:A.08.663`     |              1 | [CL:0000540](http://purl.obolibrary.org/obo/CL_0000540)                                                          |
| `MESH:A.05.360.490` |              1 | [CL:0000586](http://purl.obolibrary.org/obo/CL_0000586)                                                          |

## `PMID`: PubMed

Overall, there were 3 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref    |   usages_count | usages                                                  |
|------------------|----------------|---------------------------------------------------------|
| `PMID:10102814j` |              1 | [CL:0000134](http://purl.obolibrary.org/obo/CL_0000134) |
| `PMID:_17986482` |              1 | [CL:0000134](http://purl.obolibrary.org/obo/CL_0000134) |
| `PMID:_19960544` |              1 | [CL:0000134](http://purl.obolibrary.org/obo/CL_0000134) |

