# apo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `apo`. See the [GitHub repository](https://github.com/obophenotype/ascomycete-phenotype-ontology).


## `BioGRID`: BioGRID

Overall, there were 3 invalid
xrefs to external prefixed with `BioGRID` (standardized to Bioregistry
entry [`biogrid`]((https://bioregistry.io/biogrid)) that
did not match the standard pattern `^\d+$`.

| external_xref      |   usages_count | usages                                                                                               |
|--------------------|----------------|------------------------------------------------------------------------------------------------------|
| `BioGRID:curators` |              2 | [APO:0000244](https://bioregistry.io/APO:0000244), [APO:0000272](https://bioregistry.io/APO:0000272) |
| `BioGRID:mcc`      |              1 | [APO:0000318](https://bioregistry.io/APO:0000318)                                                    |

## `CGD`: Candida Genome Database

Overall, there were 6 invalid
xrefs to external prefixed with `CGD` (standardized to Bioregistry
entry [`cgd`]((https://bioregistry.io/cgd)) that
did not match the standard pattern `^CAL\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CGD:mcc`       |              6 | [APO:0000319](https://bioregistry.io/APO:0000319), [APO:0000320](https://bioregistry.io/APO:0000320), [APO:0000321](https://bioregistry.io/APO:0000321), [APO:0000324](https://bioregistry.io/APO:0000324), [APO:0000325](https://bioregistry.io/APO:0000325), ... |

## `SGD`: Saccharomyces Genome Database

Overall, there were 286 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
entry [`sgd`]((https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:mcc`       |            127 | [APO:0000023](https://bioregistry.io/APO:0000023), [APO:0000024](https://bioregistry.io/APO:0000024), [APO:0000027](https://bioregistry.io/APO:0000027), [APO:0000030](https://bioregistry.io/APO:0000030), [APO:0000031](https://bioregistry.io/APO:0000031), ... |
| `SGD:RSN`       |            110 | [APO:0000011](https://bioregistry.io/APO:0000011), [APO:0000011](https://bioregistry.io/APO:0000011), [APO:0000012](https://bioregistry.io/APO:0000012), [APO:0000012](https://bioregistry.io/APO:0000012), [APO:0000016](https://bioregistry.io/APO:0000016), ... |
| `SGD:curators`  |             47 | [APO:0000001](https://bioregistry.io/APO:0000001), [APO:0000002](https://bioregistry.io/APO:0000002), [APO:0000003](https://bioregistry.io/APO:0000003), [APO:0000004](https://bioregistry.io/APO:0000004), [APO:0000005](https://bioregistry.io/APO:0000005), ... |
| `SGD:rsn`       |              1 | [APO:0000028](https://bioregistry.io/APO:0000028)                                                                                                                                                                                                                  |
| `SGD:krc`       |              1 | [APO:0000029](https://bioregistry.io/APO:0000029)                                                                                                                                                                                                                  |

