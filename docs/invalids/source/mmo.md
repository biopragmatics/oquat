# mmo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `mmo`. See the [GitHub repository](https://github.com/rat-genome-database/MMO-Measurement-Method-Ontology).


## `efo`: Experimental Factor Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `efo` (standardized to Bioregistry
prefix [`efo`](https://bioregistry.io/efo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref     |   usages_count | usages                                                    |
|-------------------|----------------|-----------------------------------------------------------|
| `efo:EFO_0001458` |              1 | [MMO:0000642](http://purl.obolibrary.org/obo/MMO_0000642) |
| `efo:EFO_0002768` |              1 | [MMO:0000648](http://purl.obolibrary.org/obo/MMO_0000648) |
| `efo:EFO_0002943` |              1 | [MMO:0000655](http://purl.obolibrary.org/obo/MMO_0000655) |
| `efo:EFO_0002770` |              1 | [MMO:0000659](http://purl.obolibrary.org/obo/MMO_0000659) |
| `efo:EFO_0008896` |              1 | [MMO:0000659](http://purl.obolibrary.org/obo/MMO_0000659) |
| `efo:EFO_0002941` |              1 | [MMO:0000660](http://purl.obolibrary.org/obo/MMO_0000660) |
| `efo:EFO_0000561` |              1 | [MMO:0000672](http://purl.obolibrary.org/obo/MMO_0000672) |

## `RGD`: Rat Genome Database

Overall, there were 36 invalid
xrefs to external prefixed with `RGD` (standardized to Bioregistry
prefix [`rgd`](https://bioregistry.io/rgd)) that
did not match the standard pattern `^\d{4,}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RGD:JRS`       |             29 | [MMO:0000017](http://purl.obolibrary.org/obo/MMO_0000017), [MMO:0000088](http://purl.obolibrary.org/obo/MMO_0000088), [MMO:0000119](http://purl.obolibrary.org/obo/MMO_0000119), [MMO:0000218](http://purl.obolibrary.org/obo/MMO_0000218), [MMO:0000222](http://purl.obolibrary.org/obo/MMO_0000222), ... |
| `RGD:MS`        |              4 | [MMO:0000081](http://purl.obolibrary.org/obo/MMO_0000081), [MMO:0000097](http://purl.obolibrary.org/obo/MMO_0000097), [MMO:0000104](http://purl.obolibrary.org/obo/MMO_0000104), [MMO:0000160](http://purl.obolibrary.org/obo/MMO_0000160)                                                                 |
| `RGD:SL`        |              1 | [MMO:0000132](http://purl.obolibrary.org/obo/MMO_0000132)                                                                                                                                                                                                                                                  |
| `RGD:SJL`       |              1 | [MMO:0000448](http://purl.obolibrary.org/obo/MMO_0000448)                                                                                                                                                                                                                                                  |
| `RGD:GTH`       |              1 | [MMO:0000497](http://purl.obolibrary.org/obo/MMO_0000497)                                                                                                                                                                                                                                                  |

