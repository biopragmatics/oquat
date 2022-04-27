# wbls

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `wbls`. See the [GitHub repository](https://github.com/obophenotype/c-elegans-development-ontology).


## `PMC`: Pubmed Central

Overall, there were 2 invalid
xrefs to external prefixed with `PMC` (standardized to Bioregistry
prefix [`pmc`](https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref            |   usages_count | usages                                                                                     |
|--------------------------|----------------|--------------------------------------------------------------------------------------------|
| `PMC:('PMC', '4492366')` |              1 | [http://purl.obolibrary.org/obo/WBls_0000801](http://purl.obolibrary.org/obo/WBls_0000801) |
| `PMC:('PMC', '3697962')` |              1 | [http://purl.obolibrary.org/obo/WBls_0000802](http://purl.obolibrary.org/obo/WBls_0000802) |

## `WB`: WormBase database of nematode biology

Overall, there were 751 invalid
xrefs to external prefixed with `WB` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref      |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `WB:('WB', 'dr')`  |            612 | [http://purl.obolibrary.org/obo/WBls_0000006](http://purl.obolibrary.org/obo/WBls_0000006), [http://purl.obolibrary.org/obo/WBls_0000074](http://purl.obolibrary.org/obo/WBls_0000074), [http://purl.obolibrary.org/obo/WBls_0000077](http://purl.obolibrary.org/obo/WBls_0000077), [http://purl.obolibrary.org/obo/WBls_0000079](http://purl.obolibrary.org/obo/WBls_0000079), [http://purl.obolibrary.org/obo/WBls_0000080](http://purl.obolibrary.org/obo/WBls_0000080), ... |
| `WB:('WB', 'wjc')` |             69 | [http://purl.obolibrary.org/obo/WBls_0000002](http://purl.obolibrary.org/obo/WBls_0000002), [http://purl.obolibrary.org/obo/WBls_0000003](http://purl.obolibrary.org/obo/WBls_0000003), [http://purl.obolibrary.org/obo/WBls_0000004](http://purl.obolibrary.org/obo/WBls_0000004), [http://purl.obolibrary.org/obo/WBls_0000005](http://purl.obolibrary.org/obo/WBls_0000005), [http://purl.obolibrary.org/obo/WBls_0000006](http://purl.obolibrary.org/obo/WBls_0000006), ... |
| `WB:('WB', 'jl')`  |             37 | [http://purl.obolibrary.org/obo/WBls_0000001](http://purl.obolibrary.org/obo/WBls_0000001), [http://purl.obolibrary.org/obo/WBls_0000059](http://purl.obolibrary.org/obo/WBls_0000059), [http://purl.obolibrary.org/obo/WBls_0000076](http://purl.obolibrary.org/obo/WBls_0000076), [http://purl.obolibrary.org/obo/WBls_0000091](http://purl.obolibrary.org/obo/WBls_0000091), [http://purl.obolibrary.org/obo/WBls_0000101](http://purl.obolibrary.org/obo/WBls_0000101), ... |
| `WB:('WB', 'fr')`  |             18 | [http://purl.obolibrary.org/obo/WBls_0000723](http://purl.obolibrary.org/obo/WBls_0000723), [http://purl.obolibrary.org/obo/WBls_0000726](http://purl.obolibrary.org/obo/WBls_0000726), [http://purl.obolibrary.org/obo/WBls_0000727](http://purl.obolibrary.org/obo/WBls_0000727), [http://purl.obolibrary.org/obo/WBls_0000728](http://purl.obolibrary.org/obo/WBls_0000728), [http://purl.obolibrary.org/obo/WBls_0000729](http://purl.obolibrary.org/obo/WBls_0000729), ... |
| `WB:('WB', 'mb')`  |             15 | [http://purl.obolibrary.org/obo/WBls_0000077](http://purl.obolibrary.org/obo/WBls_0000077), [http://purl.obolibrary.org/obo/WBls_0000079](http://purl.obolibrary.org/obo/WBls_0000079), [http://purl.obolibrary.org/obo/WBls_0000080](http://purl.obolibrary.org/obo/WBls_0000080), [http://purl.obolibrary.org/obo/WBls_0000081](http://purl.obolibrary.org/obo/WBls_0000081), [http://purl.obolibrary.org/obo/WBls_0000082](http://purl.obolibrary.org/obo/WBls_0000082), ... |

