# ms

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `ms`. See the [GitHub repository](https://github.com/HUPO-PSI/psi-ms-CV).


## `EDAM`: Bioinformatics operations, data types, formats, identifiers and topics

Overall, there were 2 invalid
xrefs to external prefixed with `EDAM` (standardized to Bioregistry
prefix [`edam`](https://bioregistry.io/edam)) that
did not match the standard pattern `^(data|topic|operation|format)\_\d{4}$`.

| external_xref           |   usages_count | usages                                                                                 |
|-------------------------|----------------|----------------------------------------------------------------------------------------|
| `EDAM:('EDAM', '0846')` |              1 | [http://purl.obolibrary.org/obo/MS_1000864](http://purl.obolibrary.org/obo/MS_1000864) |
| `EDAM:('EDAM', '2301')` |              1 | [http://purl.obolibrary.org/obo/MS_1000868](http://purl.obolibrary.org/obo/MS_1000868) |

## `SWO`: Software ontology

Overall, there were 1 invalid
xrefs to external prefixed with `SWO` (standardized to Bioregistry
prefix [`swo`](https://bioregistry.io/swo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                                        |   usages_count | usages                                                                                 |
|------------------------------------------------------|----------------|----------------------------------------------------------------------------------------|
| `SWO:('SWO', 'http://edamontology.org/format_2187')` |              1 | [http://purl.obolibrary.org/obo/MS_1002659](http://purl.obolibrary.org/obo/MS_1002659) |

