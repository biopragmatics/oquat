# apo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `apo`. See the [GitHub repository](https://github.com/obophenotype/ascomycete-phenotype-ontology)


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
| `CGD:mcc`       |              6 | [APO:0000319](https://bioregistry.io/APO:0000319), [APO:0000319](https://bioregistry.io/APO:0000319), [APO:0000320](https://bioregistry.io/APO:0000320), [APO:0000320](https://bioregistry.io/APO:0000320), [APO:0000320](https://bioregistry.io/APO:0000320), ... |

## `SGD`: Saccharomyces Genome Database

Overall, there were 286 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
entry [`sgd`]((https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:mcc`       |            127 | [APO:0000091](https://bioregistry.io/APO:0000091), [APO:0000093](https://bioregistry.io/APO:0000093), [APO:0000124](https://bioregistry.io/APO:0000124), [APO:0000197](https://bioregistry.io/APO:0000197), [APO:0000199](https://bioregistry.io/APO:0000199), ... |
| `SGD:RSN`       |            110 | [APO:0000026](https://bioregistry.io/APO:0000026), [APO:0000136](https://bioregistry.io/APO:0000136), [APO:0000265](https://bioregistry.io/APO:0000265), [APO:0000268](https://bioregistry.io/APO:0000268), [APO:0000276](https://bioregistry.io/APO:0000276), ... |
| `SGD:curators`  |             47 | [APO:0000004](https://bioregistry.io/APO:0000004), [APO:0000020](https://bioregistry.io/APO:0000020), [APO:0000098](https://bioregistry.io/APO:0000098), [APO:0000110](https://bioregistry.io/APO:0000110), [APO:0000211](https://bioregistry.io/APO:0000211), ... |
| `SGD:rsn`       |              1 | [APO:0000028](https://bioregistry.io/APO:0000028)                                                                                                                                                                                                                  |
| `SGD:krc`       |              1 | [APO:0000029](https://bioregistry.io/APO:0000029)                                                                                                                                                                                                                  |

