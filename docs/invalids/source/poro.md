# poro

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `poro`. See the [GitHub repository](https://github.com/obophenotype/porifera-ontology).


## `UBERON`: Uber Anatomy Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `UBERON` (standardized to Bioregistry
prefix [`uberon`](https://bioregistry.io/uberon)) that
did not match the standard pattern `^\d+$`.

| external_xref              |   usages_count | usages                                                                                                                                                                                 |
|----------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UBERON:('UBERON', 'cjm')` |              2 | [http://purl.obolibrary.org/obo/PORO_0000044](http://purl.obolibrary.org/obo/PORO_0000044), [http://purl.obolibrary.org/obo/PORO_0000101](http://purl.obolibrary.org/obo/PORO_0000101) |

