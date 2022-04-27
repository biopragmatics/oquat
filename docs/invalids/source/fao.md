# fao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `fao`. See the [GitHub repository](https://github.com/obophenotype/fungal-anatomy-ontology).


## `CGD`: Candida Genome Database

Overall, there were 10 invalid
xrefs to external prefixed with `CGD` (standardized to Bioregistry
prefix [`cgd`](https://bioregistry.io/cgd)) that
did not match the standard pattern `^CAL\d{7}$`.

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|----------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CGD:('CGD', 'doi')` |             10 | [FAO:0000042](http://purl.obolibrary.org/obo/FAO_0000042), [FAO:0000059](http://purl.obolibrary.org/obo/FAO_0000059), [FAO:0000060](http://purl.obolibrary.org/obo/FAO_0000060), [FAO:0000061](http://purl.obolibrary.org/obo/FAO_0000061), [FAO:0000062](http://purl.obolibrary.org/obo/FAO_0000062), ... |

## `FAO`: Fungal gross anatomy

Overall, there were 88 invalid
xrefs to external prefixed with `FAO` (standardized to Bioregistry
prefix [`fao`](https://bioregistry.io/fao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref             |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|---------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FAO:('FAO', 'mah')`      |             32 | [FAO:0000001](http://purl.obolibrary.org/obo/FAO_0000001), [FAO:0000002](http://purl.obolibrary.org/obo/FAO_0000002), [FAO:0000006](http://purl.obolibrary.org/obo/FAO_0000006), [FAO:0000013](http://purl.obolibrary.org/obo/FAO_0000013), [FAO:0000016](http://purl.obolibrary.org/obo/FAO_0000016), ... |
| `FAO:('FAO', 'mcc')`      |             23 | [FAO:0001001](http://purl.obolibrary.org/obo/FAO_0001001), [FAO:0001002](http://purl.obolibrary.org/obo/FAO_0001002), [FAO:0001003](http://purl.obolibrary.org/obo/FAO_0001003), [FAO:0001004](http://purl.obolibrary.org/obo/FAO_0001004), [FAO:0001007](http://purl.obolibrary.org/obo/FAO_0001007), ... |
| `FAO:('FAO', 'curators')` |             17 | [FAO:0000002](http://purl.obolibrary.org/obo/FAO_0000002), [FAO:0000003](http://purl.obolibrary.org/obo/FAO_0000003), [FAO:0000004](http://purl.obolibrary.org/obo/FAO_0000004), [FAO:0000005](http://purl.obolibrary.org/obo/FAO_0000005), [FAO:0000007](http://purl.obolibrary.org/obo/FAO_0000007), ... |
| `FAO:('FAO', 'doi')`      |             14 | [FAO:0000010](http://purl.obolibrary.org/obo/FAO_0000010), [FAO:0001030](http://purl.obolibrary.org/obo/FAO_0001030), [FAO:0001031](http://purl.obolibrary.org/obo/FAO_0001031), [FAO:0002003](http://purl.obolibrary.org/obo/FAO_0002003), [FAO:0002003](http://purl.obolibrary.org/obo/FAO_0002003), ... |
| `FAO:('FAO', 'clt')`      |              2 | [FAO:0001005](http://purl.obolibrary.org/obo/FAO_0001005), [FAO:0001006](http://purl.obolibrary.org/obo/FAO_0001006)                                                                                                                                                                                       |

## `SGD`: Saccharomyces Genome Database

Overall, there were 33 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
prefix [`sgd`](https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|----------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:('SGD', 'clt')` |             33 | [FAO:0000002](http://purl.obolibrary.org/obo/FAO_0000002), [FAO:0000006](http://purl.obolibrary.org/obo/FAO_0000006), [FAO:0000007](http://purl.obolibrary.org/obo/FAO_0000007), [FAO:0000014](http://purl.obolibrary.org/obo/FAO_0000014), [FAO:0000017](http://purl.obolibrary.org/obo/FAO_0000017), ... |

