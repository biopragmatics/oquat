# fbcv

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `fbcv`. See the [GitHub repository](https://github.com/FlyBase/flybase-controlled-vocabulary).


## `Reactome`: Reactome

Overall, there were 1 invalid
xrefs to external prefixed with `Reactome` (standardized to Bioregistry
prefix [`reactome`](https://bioregistry.io/reactome)) that
did not match the standard pattern `^R-[A-Z]{3}-\d+(-\d+)?(\.\d+)?$`.

| external_xref    |   usages_count | usages                                              |
|------------------|----------------|-----------------------------------------------------|
| `Reactome:69278` |              1 | [FBcv:0000432](https://bioregistry.io/FBcv:0000432) |

## `SO`: Sequence types and features ontology

Overall, there were 1 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `SO:ma`         |              1 | [FBcv:0003013](https://bioregistry.io/FBcv:0003013) |

## `WB_REF`: WormBase database of nematode biology

Overall, there were 1 invalid
xrefs to external prefixed with `WB_REF` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `WB_REF:cgc467` |              1 | [FBcv:0000002](https://bioregistry.io/FBcv:0000002) |

