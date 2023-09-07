# fovt

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `fovt`. See the [GitHub repository](https://github.com/futres/fovt).


## `ISBN`: International Standard Book Number

Overall, there were 620 invalid
xrefs to external prefixed with `ISBN` (standardized to Bioregistry
prefix [`isbn`](https://bioregistry.io/isbn)) that
did not match the standard pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`.

| external_xref                     |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ISBN:9004086161, 9789004086166`  |            604 | [FOVT:0000006](http://purl.obolibrary.org/obo/FOVT_0000006), [FOVT:0000006](http://purl.obolibrary.org/obo/FOVT_0000006), [FOVT:0000008](http://purl.obolibrary.org/obo/FOVT_0000008), [FOVT:0000008](http://purl.obolibrary.org/obo/FOVT_0000008), [FOVT:0000009](http://purl.obolibrary.org/obo/FOVT_0000009), ... |
| `ISBN: 9004086161, 9789004086166` |             16 | [FOVT:2000009](http://purl.obolibrary.org/obo/FOVT_2000009), [FOVT:2000009](http://purl.obolibrary.org/obo/FOVT_2000009), [FOVT:2000011](http://purl.obolibrary.org/obo/FOVT_2000011), [FOVT:2000011](http://purl.obolibrary.org/obo/FOVT_2000011), [FOVT:2000012](http://purl.obolibrary.org/obo/FOVT_2000012), ... |

## `ORCID`: Open Researcher and Contributor

Overall, there were 1 invalid
xrefs to external prefixed with `ORCID` (standardized to Bioregistry
prefix [`orcid`](https://bioregistry.io/orcid)) that
did not match the standard pattern `^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$`.

| external_xref                |   usages_count | usages                                                      |
|------------------------------|----------------|-------------------------------------------------------------|
| `ORCID: 0000-0003-2699-3066` |              1 | [FOVT:0001158](http://purl.obolibrary.org/obo/FOVT_0001158) |

