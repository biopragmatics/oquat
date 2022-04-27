# miro

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `miro`. See the [GitHub repository](https://github.com/VEuPathDB-ontology/MIRO).


## `CAS`: CAS Chemical Registry

Overall, there were 1 invalid
xrefs to external prefixed with `CAS` (standardized to Bioregistry
prefix [`cas`](https://bioregistry.io/cas)) that
did not match the standard pattern `^\d{1,7}\-\d{2}\-\d$`.

| external_xref                                                                           |   usages_count | usages                                                |
|-----------------------------------------------------------------------------------------|----------------|-------------------------------------------------------|
| `CAS:7-(2-chlorophenyl)-4-ethoxy-3,5-dioxa-6-aza-4-phosphaoct-6-ene-8-nitrile4-sulfide` |              1 | [MIRO:10000108](https://bioregistry.io/MIRO:10000108) |

