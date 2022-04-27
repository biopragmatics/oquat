# symp

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `symp`. See the [GitHub repository](https://github.com/DiseaseOntology/SymptomOntology).


## `ICD9CM_2005`: International Classification of Diseases, 9th Revision, Clinical Modification

Overall, there were 1 invalid
xrefs to external prefixed with `ICD9CM_2005` (standardized to Bioregistry
prefix [`icd9cm`](https://bioregistry.io/icd9cm)) that
did not match the standard pattern `^([\dA-Z]\d{2}(\.\d{1,3}|))|(\d{2}(\.\d{1,2}|))$`.

| external_xref                                 |   usages_count | usages                                              |
|-----------------------------------------------|----------------|-----------------------------------------------------|
| `ICD9CM_2005:('ICD9CM_2005', '<new dbxref>')` |              1 | [SYMP:0000821](https://bioregistry.io/SYMP:0000821) |

