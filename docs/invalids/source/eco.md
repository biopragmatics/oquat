# eco

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `eco`. See the [GitHub repository](https://github.com/evidenceontology/evidenceontology).


## `DisProt`: DisProt

Overall, there were 7 invalid
xrefs to external prefixed with `DisProt` (standardized to Bioregistry
prefix [`disprot`](https://bioregistry.io/disprot)) that
did not match the standard pattern `^DP\d{5}$`.

| external_xref            |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|--------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DisProt:BalintMeszaros` |              7 | [ECO:0006183](http://purl.obolibrary.org/obo/ECO_0006183), [ECO:0006185](http://purl.obolibrary.org/obo/ECO_0006185), [ECO:0006187](http://purl.obolibrary.org/obo/ECO_0006187), [ECO:0006188](http://purl.obolibrary.org/obo/ECO_0006188), [ECO:0006189](http://purl.obolibrary.org/obo/ECO_0006189), ... |

## `ECO`: Evidence ontology

Overall, there were 1,411 invalid
xrefs to external prefixed with `ECO` (standardized to Bioregistry
prefix [`eco`](https://bioregistry.io/eco)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ECO:RCT`       |            718 | [ECO:0000009](http://purl.obolibrary.org/obo/ECO_0000009), [ECO:0000011](http://purl.obolibrary.org/obo/ECO_0000011), [ECO:0000033](http://purl.obolibrary.org/obo/ECO_0000033), [ECO:0000053](http://purl.obolibrary.org/obo/ECO_0000053), [ECO:0000054](http://purl.obolibrary.org/obo/ECO_0000054), ... |
| `ECO:SN`        |            328 | [ECO:0000001](http://purl.obolibrary.org/obo/ECO_0000001), [ECO:0000002](http://purl.obolibrary.org/obo/ECO_0000002), [ECO:0000018](http://purl.obolibrary.org/obo/ECO_0000018), [ECO:0000021](http://purl.obolibrary.org/obo/ECO_0000021), [ECO:0000028](http://purl.obolibrary.org/obo/ECO_0000028), ... |
| `ECO:MCC`       |            297 | [ECO:0000000](http://purl.obolibrary.org/obo/ECO_0000000), [ECO:0000007](http://purl.obolibrary.org/obo/ECO_0000007), [ECO:0000008](http://purl.obolibrary.org/obo/ECO_0000008), [ECO:0000019](http://purl.obolibrary.org/obo/ECO_0000019), [ECO:0000020](http://purl.obolibrary.org/obo/ECO_0000020), ... |
| `ECO:SW`        |             58 | [ECO:0000085](http://purl.obolibrary.org/obo/ECO_0000085), [ECO:0000095](http://purl.obolibrary.org/obo/ECO_0000095), [ECO:0000096](http://purl.obolibrary.org/obo/ECO_0000096), [ECO:0000106](http://purl.obolibrary.org/obo/ECO_0000106), [ECO:0000109](http://purl.obolibrary.org/obo/ECO_0000109), ... |
| `ECO:KAV`       |              3 | [ECO:0000003](http://purl.obolibrary.org/obo/ECO_0000003), [ECO:0000154](http://purl.obolibrary.org/obo/ECO_0000154), [ECO:0000164](http://purl.obolibrary.org/obo/ECO_0000164)                                                                                                                            |
| `ECO:KIM`       |              2 | [ECO:0000004](http://purl.obolibrary.org/obo/ECO_0000004), [ECO:0000096](http://purl.obolibrary.org/obo/ECO_0000096)                                                                                                                                                                                       |
| `ECO:RCJ`       |              2 | [ECO:0001828](http://purl.obolibrary.org/obo/ECO_0001828), [ECO:0007850](http://purl.obolibrary.org/obo/ECO_0007850)                                                                                                                                                                                       |
| `ECO:MG`        |              2 | [ECO:0006186](http://purl.obolibrary.org/obo/ECO_0006186), [ECO:0006252](http://purl.obolibrary.org/obo/ECO_0006252)                                                                                                                                                                                       |
| `ECO:cjm`       |              1 | [ECO:0000501](http://purl.obolibrary.org/obo/ECO_0000501)                                                                                                                                                                                                                                                  |

## `ERO`: eagle-i resource ontology

Overall, there were 1 invalid
xrefs to external prefixed with `ERO` (standardized to Bioregistry
prefix [`ero`](https://bioregistry.io/ero)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                                                           |   usages_count | usages                                                    |
|-------------------------------------------------------------------------|----------------|-----------------------------------------------------------|
| `ERO:0000329|URL:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3907272/` |              1 | [ECO:0007043](http://purl.obolibrary.org/obo/ECO_0007043) |

## `GO`: Gene Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                          |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:IEP`        |              3 | [ECO:0000008](http://purl.obolibrary.org/obo/ECO_0000008), [ECO:0007006](http://purl.obolibrary.org/obo/ECO_0007006), [ECO:0007007](http://purl.obolibrary.org/obo/ECO_0007007) |
| `GO:IMP`        |              3 | [ECO:0000015](http://purl.obolibrary.org/obo/ECO_0000015), [ECO:0007000](http://purl.obolibrary.org/obo/ECO_0007000), [ECO:0007001](http://purl.obolibrary.org/obo/ECO_0007001) |
| `GO:TAS`        |              1 | [ECO:0000033](http://purl.obolibrary.org/obo/ECO_0000033)                                                                                                                       |

## `HPO`: Human Phenotype Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `HPO` (standardized to Bioregistry
prefix [`hp`](https://bioregistry.io/hp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `HPO:PCS`       |              1 | [ECO:0006017](http://purl.obolibrary.org/obo/ECO_0006017) |
| `HPO:ICE`       |              1 | [ECO:0006019](http://purl.obolibrary.org/obo/ECO_0006019) |

## `PomBase`: PomBase

Overall, there were 1 invalid
xrefs to external prefixed with `PomBase` (standardized to Bioregistry
prefix [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `PomBase:MAH`   |              1 | [ECO:0000095](http://purl.obolibrary.org/obo/ECO_0000095) |

