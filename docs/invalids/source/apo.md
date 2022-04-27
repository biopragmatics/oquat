# apo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `apo`. See the [GitHub repository](https://github.com/obophenotype/ascomycete-phenotype-ontology).


## `BioGRID`: BioGRID

Overall, there were 3 invalid
xrefs to external prefixed with `BioGRID` (standardized to Bioregistry
prefix [`biogrid`](https://bioregistry.io/biogrid)) that
did not match the standard pattern `^\d+$`.

| external_xref                     |   usages_count | usages                                                                                                                                                                             |
|-----------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BioGRID:('BioGRID', 'curators')` |              2 | [http://purl.obolibrary.org/obo/APO_0000244](http://purl.obolibrary.org/obo/APO_0000244), [http://purl.obolibrary.org/obo/APO_0000272](http://purl.obolibrary.org/obo/APO_0000272) |
| `BioGRID:('BioGRID', 'mcc')`      |              1 | [http://purl.obolibrary.org/obo/APO_0000318](http://purl.obolibrary.org/obo/APO_0000318)                                                                                           |

## `CGD`: Candida Genome Database

Overall, there were 6 invalid
xrefs to external prefixed with `CGD` (standardized to Bioregistry
prefix [`cgd`](https://bioregistry.io/cgd)) that
did not match the standard pattern `^CAL\d{7}$`.

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CGD:('CGD', 'mcc')` |              6 | [http://purl.obolibrary.org/obo/APO_0000319](http://purl.obolibrary.org/obo/APO_0000319), [http://purl.obolibrary.org/obo/APO_0000320](http://purl.obolibrary.org/obo/APO_0000320), [http://purl.obolibrary.org/obo/APO_0000321](http://purl.obolibrary.org/obo/APO_0000321), [http://purl.obolibrary.org/obo/APO_0000324](http://purl.obolibrary.org/obo/APO_0000324), [http://purl.obolibrary.org/obo/APO_0000325](http://purl.obolibrary.org/obo/APO_0000325), ... |

## `SGD`: Saccharomyces Genome Database

Overall, there were 286 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
prefix [`sgd`](https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref             |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:('SGD', 'mcc')`      |            127 | [http://purl.obolibrary.org/obo/APO_0000023](http://purl.obolibrary.org/obo/APO_0000023), [http://purl.obolibrary.org/obo/APO_0000024](http://purl.obolibrary.org/obo/APO_0000024), [http://purl.obolibrary.org/obo/APO_0000027](http://purl.obolibrary.org/obo/APO_0000027), [http://purl.obolibrary.org/obo/APO_0000030](http://purl.obolibrary.org/obo/APO_0000030), [http://purl.obolibrary.org/obo/APO_0000031](http://purl.obolibrary.org/obo/APO_0000031), ... |
| `SGD:('SGD', 'RSN')`      |            110 | [http://purl.obolibrary.org/obo/APO_0000011](http://purl.obolibrary.org/obo/APO_0000011), [http://purl.obolibrary.org/obo/APO_0000011](http://purl.obolibrary.org/obo/APO_0000011), [http://purl.obolibrary.org/obo/APO_0000012](http://purl.obolibrary.org/obo/APO_0000012), [http://purl.obolibrary.org/obo/APO_0000012](http://purl.obolibrary.org/obo/APO_0000012), [http://purl.obolibrary.org/obo/APO_0000016](http://purl.obolibrary.org/obo/APO_0000016), ... |
| `SGD:('SGD', 'curators')` |             47 | [http://purl.obolibrary.org/obo/APO_0000001](http://purl.obolibrary.org/obo/APO_0000001), [http://purl.obolibrary.org/obo/APO_0000002](http://purl.obolibrary.org/obo/APO_0000002), [http://purl.obolibrary.org/obo/APO_0000003](http://purl.obolibrary.org/obo/APO_0000003), [http://purl.obolibrary.org/obo/APO_0000004](http://purl.obolibrary.org/obo/APO_0000004), [http://purl.obolibrary.org/obo/APO_0000005](http://purl.obolibrary.org/obo/APO_0000005), ... |
| `SGD:('SGD', 'rsn')`      |              1 | [http://purl.obolibrary.org/obo/APO_0000028](http://purl.obolibrary.org/obo/APO_0000028)                                                                                                                                                                                                                                                                                                                                                                              |
| `SGD:('SGD', 'krc')`      |              1 | [http://purl.obolibrary.org/obo/APO_0000029](http://purl.obolibrary.org/obo/APO_0000029)                                                                                                                                                                                                                                                                                                                                                                              |

