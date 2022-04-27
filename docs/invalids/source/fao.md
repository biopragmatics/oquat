# fao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `fao`. See the [GitHub repository](https://github.com/obophenotype/fungal-anatomy-ontology).


## `CGD`: Candida Genome Database

Overall, there were 10 invalid
xrefs to external prefixed with `CGD` (standardized to Bioregistry
entry [`cgd`]((https://bioregistry.io/cgd)) that
did not match the standard pattern `^CAL\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CGD:doi`       |             10 | [FAO:0000042](https://bioregistry.io/FAO:0000042), [FAO:0000059](https://bioregistry.io/FAO:0000059), [FAO:0000060](https://bioregistry.io/FAO:0000060), [FAO:0000061](https://bioregistry.io/FAO:0000061), [FAO:0000062](https://bioregistry.io/FAO:0000062), ... |

## `FAO`: Fungal gross anatomy

Overall, there were 88 invalid
xrefs to external prefixed with `FAO` (standardized to Bioregistry
entry [`fao`]((https://bioregistry.io/fao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FAO:mah`       |             32 | [FAO:0000001](https://bioregistry.io/FAO:0000001), [FAO:0000002](https://bioregistry.io/FAO:0000002), [FAO:0000006](https://bioregistry.io/FAO:0000006), [FAO:0000013](https://bioregistry.io/FAO:0000013), [FAO:0000016](https://bioregistry.io/FAO:0000016), ... |
| `FAO:mcc`       |             23 | [FAO:0001001](https://bioregistry.io/FAO:0001001), [FAO:0001002](https://bioregistry.io/FAO:0001002), [FAO:0001003](https://bioregistry.io/FAO:0001003), [FAO:0001004](https://bioregistry.io/FAO:0001004), [FAO:0001007](https://bioregistry.io/FAO:0001007), ... |
| `FAO:curators`  |             17 | [FAO:0000002](https://bioregistry.io/FAO:0000002), [FAO:0000003](https://bioregistry.io/FAO:0000003), [FAO:0000004](https://bioregistry.io/FAO:0000004), [FAO:0000005](https://bioregistry.io/FAO:0000005), [FAO:0000007](https://bioregistry.io/FAO:0000007), ... |
| `FAO:doi`       |             14 | [FAO:0000010](https://bioregistry.io/FAO:0000010), [FAO:0001030](https://bioregistry.io/FAO:0001030), [FAO:0001031](https://bioregistry.io/FAO:0001031), [FAO:0002003](https://bioregistry.io/FAO:0002003), [FAO:0002003](https://bioregistry.io/FAO:0002003), ... |
| `FAO:clt`       |              2 | [FAO:0001005](https://bioregistry.io/FAO:0001005), [FAO:0001006](https://bioregistry.io/FAO:0001006)                                                                                                                                                               |

## `SGD`: Saccharomyces Genome Database

Overall, there were 33 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
entry [`sgd`]((https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:clt`       |             33 | [FAO:0000002](https://bioregistry.io/FAO:0000002), [FAO:0000006](https://bioregistry.io/FAO:0000006), [FAO:0000007](https://bioregistry.io/FAO:0000007), [FAO:0000014](https://bioregistry.io/FAO:0000014), [FAO:0000017](https://bioregistry.io/FAO:0000017), ... |

