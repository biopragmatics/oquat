# mfomd

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `mfomd`. See the [GitHub repository](https://github.com/jannahastings/mental-functioning-ontology).


## `ICD9CM`: International Classification of Diseases, 9th Revision, Clinical Modification

Overall, there were 1 invalid
xrefs to external prefixed with `ICD9CM` (standardized to Bioregistry
prefix [`icd9cm`](https://bioregistry.io/icd9cm)) that
did not match the standard pattern `^([\dA-Z]\d{2}(\.\d{1,3}|))|(\d{2}(\.\d{1,2}|))$`.

| external_xref       |   usages_count | usages                                                        |
|---------------------|----------------|---------------------------------------------------------------|
| `ICD9CM:290-319.99` |              1 | [MFOMD:0000004](http://purl.obolibrary.org/obo/MFOMD_0000004) |

