# wbls

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `wbls`. See the [GitHub repository](https://github.com/obophenotype/c-elegans-development-ontology).


## `PMC`: PubMed Central

Overall, there were 2 invalid
xrefs to external prefixed with `PMC` (standardized to Bioregistry
prefix [`pmc`](https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `PMC:4492366`   |              1 | [WBls:0000801](http://purl.obolibrary.org/obo/WBls_0000801) |
| `PMC:3697962`   |              1 | [WBls:0000802](http://purl.obolibrary.org/obo/WBls_0000802) |

## `WB`: Wormbase Gene ID

Overall, there were 751 invalid
xrefs to external prefixed with `WB` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `WB:dr`         |            612 | [WBls:0000006](http://purl.obolibrary.org/obo/WBls_0000006), [WBls:0000074](http://purl.obolibrary.org/obo/WBls_0000074), [WBls:0000077](http://purl.obolibrary.org/obo/WBls_0000077), [WBls:0000079](http://purl.obolibrary.org/obo/WBls_0000079), [WBls:0000080](http://purl.obolibrary.org/obo/WBls_0000080), ... |
| `WB:wjc`        |             69 | [WBls:0000002](http://purl.obolibrary.org/obo/WBls_0000002), [WBls:0000003](http://purl.obolibrary.org/obo/WBls_0000003), [WBls:0000004](http://purl.obolibrary.org/obo/WBls_0000004), [WBls:0000005](http://purl.obolibrary.org/obo/WBls_0000005), [WBls:0000006](http://purl.obolibrary.org/obo/WBls_0000006), ... |
| `WB:jl`         |             37 | [WBls:0000001](http://purl.obolibrary.org/obo/WBls_0000001), [WBls:0000059](http://purl.obolibrary.org/obo/WBls_0000059), [WBls:0000076](http://purl.obolibrary.org/obo/WBls_0000076), [WBls:0000091](http://purl.obolibrary.org/obo/WBls_0000091), [WBls:0000101](http://purl.obolibrary.org/obo/WBls_0000101), ... |
| `WB:fr`         |             18 | [WBls:0000723](http://purl.obolibrary.org/obo/WBls_0000723), [WBls:0000726](http://purl.obolibrary.org/obo/WBls_0000726), [WBls:0000727](http://purl.obolibrary.org/obo/WBls_0000727), [WBls:0000728](http://purl.obolibrary.org/obo/WBls_0000728), [WBls:0000729](http://purl.obolibrary.org/obo/WBls_0000729), ... |
| `WB:mb`         |             15 | [WBls:0000077](http://purl.obolibrary.org/obo/WBls_0000077), [WBls:0000079](http://purl.obolibrary.org/obo/WBls_0000079), [WBls:0000080](http://purl.obolibrary.org/obo/WBls_0000080), [WBls:0000081](http://purl.obolibrary.org/obo/WBls_0000081), [WBls:0000082](http://purl.obolibrary.org/obo/WBls_0000082), ... |

