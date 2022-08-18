# ms

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `ms`. See the [GitHub repository](https://github.com/HUPO-PSI/psi-ms-CV).


## `EDAM`: Bioinformatics operations, data types, formats, identifiers and topics

Overall, there were 2 invalid
xrefs to external prefixed with `EDAM` (standardized to Bioregistry
prefix [`edam`](https://bioregistry.io/edam)) that
did not match the standard pattern `^(data|topic|operation|format)\_\d{4}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `EDAM:0846`     |              1 | [MS:1000864](http://purl.obolibrary.org/obo/MS_1000864) |
| `EDAM:2301`     |              1 | [MS:1000868](http://purl.obolibrary.org/obo/MS_1000868) |

