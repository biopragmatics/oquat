# xlmod

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `xlmod`. See the [GitHub repository](https://github.com/HUPO-PSI/xlmod-CV).


## `CAS`: CAS Chemical Registry

Overall, there were 1 invalid
xrefs to external prefixed with `CAS` (standardized to Bioregistry
prefix [`cas`](https://bioregistry.io/cas)) that
did not match the standard pattern `^\d{1,7}\-\d{2}\-\d$`.

| external_xref                                          |   usages_count | usages                                                                                   |
|--------------------------------------------------------|----------------|------------------------------------------------------------------------------------------|
| `CAS:('CAS', '139609-20-4,PubChem_Compound:90469951')` |              1 | [http://purl.obolibrary.org/obo/XLMOD_02152](http://purl.obolibrary.org/obo/XLMOD_02152) |

