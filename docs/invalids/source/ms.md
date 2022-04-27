# ms

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `ms`. See the [GitHub repository](https://github.com/HUPO-PSI/psi-ms-CV).


## `EDAM`: Bioinformatics operations, data types, formats, identifiers and topics

Overall, there were 2 invalid
xrefs to external prefixed with `EDAM` (standardized to Bioregistry
entry [`edam`](https://bioregistry.io/edam)) that
did not match the standard pattern `^(data|topic|operation|format)\_\d{4}$`.

| external_xref   |   usages_count | usages                                          |
|-----------------|----------------|-------------------------------------------------|
| `EDAM:0846`     |              1 | [MS:1000864](https://bioregistry.io/MS:1000864) |
| `EDAM:2301`     |              1 | [MS:1000868](https://bioregistry.io/MS:1000868) |

## `SWO`: Software ontology

Overall, there were 1 invalid
xrefs to external prefixed with `SWO` (standardized to Bioregistry
entry [`swo`](https://bioregistry.io/swo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                             |   usages_count | usages                                          |
|-------------------------------------------|----------------|-------------------------------------------------|
| `SWO:http://edamontology.org/format_2187` |              1 | [MS:1002659](https://bioregistry.io/MS:1002659) |

