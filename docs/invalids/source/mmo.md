# mmo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `mmo`. See the [GitHub repository](https://github.com/rat-genome-database/MMO-Measurement-Method-Ontology).


## `ECO`: Evidence ontology

Overall, there were 9 invalid
xrefs to external prefixed with `ECO` (standardized to Bioregistry
prefix [`eco`](https://bioregistry.io/eco)) that
did not match the standard pattern `^\d{7}$`.

| external_xref     |   usages_count | usages                                                    |
|-------------------|----------------|-----------------------------------------------------------|
| `ECO:ECO:0001010` |              1 | [MMO:0000678](http://purl.obolibrary.org/obo/MMO_0000678) |
| `ECO:ECO:0000004` |              1 | [MMO:0000679](http://purl.obolibrary.org/obo/MMO_0000679) |
| `ECO:ECO:0000230` |              1 | [MMO:0000680](http://purl.obolibrary.org/obo/MMO_0000680) |
| `ECO:ECO:0000102` |              1 | [MMO:0000681](http://purl.obolibrary.org/obo/MMO_0000681) |
| `ECO:ECO:0000085` |              1 | [MMO:0000682](http://purl.obolibrary.org/obo/MMO_0000682) |
| `ECO:ECO:0000070` |              1 | [MMO:0000683](http://purl.obolibrary.org/obo/MMO_0000683) |
| `ECO:ECO:0001049` |              1 | [MMO:0000684](http://purl.obolibrary.org/obo/MMO_0000684) |
| `ECO:ECO:0005587` |              1 | [MMO:0000685](http://purl.obolibrary.org/obo/MMO_0000685) |
| `ECO:ECO:0005600` |              1 | [MMO:0000686](http://purl.obolibrary.org/obo/MMO_0000686) |

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

## `MESH`: Medical Subject Headings

Overall, there were 1 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                                         |   usages_count | usages                                                    |
|-------------------------------------------------------|----------------|-----------------------------------------------------------|
| `MESH:https://meshb.nlm.nih.gov/record/ui?ui=D009543` |              1 | [MMO:0000697](http://purl.obolibrary.org/obo/MMO_0000697) |

## `PMID`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref       |   usages_count | usages                                                    |
|---------------------|----------------|-----------------------------------------------------------|
| `PMID:PMID:3411196` |              1 | [MMO:0000695](http://purl.obolibrary.org/obo/MMO_0000695) |

## `RGD`: Rat Genome Database

Overall, there were 37 invalid
xrefs to external prefixed with `RGD` (standardized to Bioregistry
prefix [`rgd`](https://bioregistry.io/rgd)) that
did not match the standard pattern `^\d{4,}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RGD:JRS`       |             29 | [MMO:0000017](http://purl.obolibrary.org/obo/MMO_0000017), [MMO:0000088](http://purl.obolibrary.org/obo/MMO_0000088), [MMO:0000119](http://purl.obolibrary.org/obo/MMO_0000119), [MMO:0000218](http://purl.obolibrary.org/obo/MMO_0000218), [MMO:0000222](http://purl.obolibrary.org/obo/MMO_0000222), ... |
| `RGD:MS`        |              5 | [MMO:0000081](http://purl.obolibrary.org/obo/MMO_0000081), [MMO:0000097](http://purl.obolibrary.org/obo/MMO_0000097), [MMO:0000104](http://purl.obolibrary.org/obo/MMO_0000104), [MMO:0000137](http://purl.obolibrary.org/obo/MMO_0000137), [MMO:0000160](http://purl.obolibrary.org/obo/MMO_0000160)      |
| `RGD:SL`        |              1 | [MMO:0000132](http://purl.obolibrary.org/obo/MMO_0000132)                                                                                                                                                                                                                                                  |
| `RGD:SJL`       |              1 | [MMO:0000448](http://purl.obolibrary.org/obo/MMO_0000448)                                                                                                                                                                                                                                                  |
| `RGD:GTH`       |              1 | [MMO:0000497](http://purl.obolibrary.org/obo/MMO_0000497)                                                                                                                                                                                                                                                  |

