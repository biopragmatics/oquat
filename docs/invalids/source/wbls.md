# wbls

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `wbls`. See the [GitHub repository](https://github.com/obophenotype/c-elegans-development-ontology).


## `PMC`: Pubmed Central

Overall, there were 2 invalid
xrefs to external prefixed with `PMC` (standardized to Bioregistry
entry [`pmc`](https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `PMC:4492366`   |              1 | [WBls:0000801](https://bioregistry.io/WBls:0000801) |
| `PMC:3697962`   |              1 | [WBls:0000802](https://bioregistry.io/WBls:0000802) |

## `WB`: WormBase database of nematode biology

Overall, there were 751 invalid
xrefs to external prefixed with `WB` (standardized to Bioregistry
entry [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                       |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `WB:dr`         |            612 | [WBls:0000006](https://bioregistry.io/WBls:0000006), [WBls:0000074](https://bioregistry.io/WBls:0000074), [WBls:0000077](https://bioregistry.io/WBls:0000077), [WBls:0000079](https://bioregistry.io/WBls:0000079), [WBls:0000080](https://bioregistry.io/WBls:0000080), ... |
| `WB:wjc`        |             69 | [WBls:0000002](https://bioregistry.io/WBls:0000002), [WBls:0000003](https://bioregistry.io/WBls:0000003), [WBls:0000004](https://bioregistry.io/WBls:0000004), [WBls:0000005](https://bioregistry.io/WBls:0000005), [WBls:0000006](https://bioregistry.io/WBls:0000006), ... |
| `WB:jl`         |             37 | [WBls:0000001](https://bioregistry.io/WBls:0000001), [WBls:0000059](https://bioregistry.io/WBls:0000059), [WBls:0000076](https://bioregistry.io/WBls:0000076), [WBls:0000091](https://bioregistry.io/WBls:0000091), [WBls:0000101](https://bioregistry.io/WBls:0000101), ... |
| `WB:fr`         |             18 | [WBls:0000723](https://bioregistry.io/WBls:0000723), [WBls:0000726](https://bioregistry.io/WBls:0000726), [WBls:0000727](https://bioregistry.io/WBls:0000727), [WBls:0000728](https://bioregistry.io/WBls:0000728), [WBls:0000729](https://bioregistry.io/WBls:0000729), ... |
| `WB:mb`         |             15 | [WBls:0000077](https://bioregistry.io/WBls:0000077), [WBls:0000079](https://bioregistry.io/WBls:0000079), [WBls:0000080](https://bioregistry.io/WBls:0000080), [WBls:0000081](https://bioregistry.io/WBls:0000081), [WBls:0000082](https://bioregistry.io/WBls:0000082), ... |

