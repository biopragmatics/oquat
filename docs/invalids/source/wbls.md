# wbls

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `wbls`. See the [GitHub repository](https://github.com/obophenotype/c-elegans-development-ontology)


## `PMC`: Pubmed Central

Overall, there were 2 invalid
xrefs to external prefixed with `PMC` (standardized to Bioregistry
entry [`pmc`]((https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `PMC:4492366`   |              1 | [WBls:0000801](https://bioregistry.io/WBls:0000801) |
| `PMC:3697962`   |              1 | [WBls:0000802](https://bioregistry.io/WBls:0000802) |

## `WB`: WormBase database of nematode biology

Overall, there were 751 invalid
xrefs to external prefixed with `WB` (standardized to Bioregistry
entry [`wormbase`]((https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                       |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `WB:dr`         |            612 | [WBls:0000158](https://bioregistry.io/WBls:0000158), [WBls:0000347](https://bioregistry.io/WBls:0000347), [WBls:0000625](https://bioregistry.io/WBls:0000625), [WBls:0000628](https://bioregistry.io/WBls:0000628), [WBls:0000659](https://bioregistry.io/WBls:0000659), ... |
| `WB:wjc`        |             69 | [WBls:0000008](https://bioregistry.io/WBls:0000008), [WBls:0000009](https://bioregistry.io/WBls:0000009), [WBls:0000015](https://bioregistry.io/WBls:0000015), [WBls:0000056](https://bioregistry.io/WBls:0000056), [WBls:0000069](https://bioregistry.io/WBls:0000069), ... |
| `WB:jl`         |             37 | [WBls:0000680](https://bioregistry.io/WBls:0000680), [WBls:0000682](https://bioregistry.io/WBls:0000682), [WBls:0000715](https://bioregistry.io/WBls:0000715), [WBls:0000724](https://bioregistry.io/WBls:0000724), [WBls:0000794](https://bioregistry.io/WBls:0000794), ... |
| `WB:fr`         |             18 | [WBls:0000723](https://bioregistry.io/WBls:0000723), [WBls:0000732](https://bioregistry.io/WBls:0000732), [WBls:0000732](https://bioregistry.io/WBls:0000732), [WBls:0000732](https://bioregistry.io/WBls:0000732), [WBls:0000736](https://bioregistry.io/WBls:0000736), ... |
| `WB:mb`         |             15 | [WBls:0000094](https://bioregistry.io/WBls:0000094), [WBls:0000096](https://bioregistry.io/WBls:0000096), [WBls:0000100](https://bioregistry.io/WBls:0000100), [WBls:0000100](https://bioregistry.io/WBls:0000100), [WBls:0000100](https://bioregistry.io/WBls:0000100), ... |

