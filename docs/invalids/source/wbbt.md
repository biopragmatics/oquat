# wbbt

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `wbbt`. See the [GitHub repository](https://github.com/obophenotype/c-elegans-gross-anatomy-ontology).


## `WB`: WormBase database of nematode biology

Overall, there were 5,448 invalid
xrefs to external prefixed with `WB` (standardized to Bioregistry
entry [`wormbase`]((https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref      |   usages_count | usages                                                                                                                                                                                                                                                                       |
|--------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `WB:rynl`          |           5259 | [WBbt:0000102](https://bioregistry.io/WBbt:0000102), [WBbt:0001001](https://bioregistry.io/WBbt:0001001), [WBbt:0001002](https://bioregistry.io/WBbt:0001002), [WBbt:0001003](https://bioregistry.io/WBbt:0001003), [WBbt:0001004](https://bioregistry.io/WBbt:0001004), ... |
| `WB:Paper00000938` |             81 | [WBbt:0003938](https://bioregistry.io/WBbt:0003938), [WBbt:0005118](https://bioregistry.io/WBbt:0005118), [WBbt:0005119](https://bioregistry.io/WBbt:0005119), [WBbt:0005270](https://bioregistry.io/WBbt:0005270), [WBbt:0005274](https://bioregistry.io/WBbt:0005274), ... |
| `WB:Paper00002608` |             24 | [WBbt:0003378](https://bioregistry.io/WBbt:0003378), [WBbt:0003383](https://bioregistry.io/WBbt:0003383), [WBbt:0004113](https://bioregistry.io/WBbt:0004113), [WBbt:0005065](https://bioregistry.io/WBbt:0005065), [WBbt:0005067](https://bioregistry.io/WBbt:0005067), ... |
| `WB:Paper00000462` |             22 | [WBbt:0002684](https://bioregistry.io/WBbt:0002684), [WBbt:0004008](https://bioregistry.io/WBbt:0004008), [WBbt:0004010](https://bioregistry.io/WBbt:0004010), [WBbt:0004012](https://bioregistry.io/WBbt:0004012), [WBbt:0004014](https://bioregistry.io/WBbt:0004014), ... |
| `WB:wjc`           |             12 | [WBbt:0006757](https://bioregistry.io/WBbt:0006757), [WBbt:0006758](https://bioregistry.io/WBbt:0006758), [WBbt:0006763](https://bioregistry.io/WBbt:0006763), [WBbt:0006765](https://bioregistry.io/WBbt:0006765), [WBbt:0006766](https://bioregistry.io/WBbt:0006766), ... |
| `WB:Paper00038216` |              9 | [WBbt:0008411](https://bioregistry.io/WBbt:0008411), [WBbt:0008424](https://bioregistry.io/WBbt:0008424), [WBbt:0008425](https://bioregistry.io/WBbt:0008425), [WBbt:0008426](https://bioregistry.io/WBbt:0008426), [WBbt:0008427](https://bioregistry.io/WBbt:0008427), ... |
| `WB:sdm`           |              6 | [WBbt:0005244](https://bioregistry.io/WBbt:0005244), [WBbt:0005261](https://bioregistry.io/WBbt:0005261), [WBbt:0005310](https://bioregistry.io/WBbt:0005310), [WBbt:0005373](https://bioregistry.io/WBbt:0005373), [WBbt:0005415](https://bioregistry.io/WBbt:0005415), ... |
| `WB:pws`           |              5 | [WBbt:0005732](https://bioregistry.io/WBbt:0005732), [WBbt:0005733](https://bioregistry.io/WBbt:0005733), [WBbt:0005733](https://bioregistry.io/WBbt:0005733), [WBbt:0005734](https://bioregistry.io/WBbt:0005734), [WBbt:0005734](https://bioregistry.io/WBbt:0005734)      |
| `WB:Paper00000009` |              4 | [WBbt:0003638](https://bioregistry.io/WBbt:0003638), [WBbt:0003645](https://bioregistry.io/WBbt:0003645), [WBbt:0003649](https://bioregistry.io/WBbt:0003649), [WBbt:0003666](https://bioregistry.io/WBbt:0003666)                                                           |
| `WB:cgc938`        |              3 | [WBbt:0005334](https://bioregistry.io/WBbt:0005334), [WBbt:0005413](https://bioregistry.io/WBbt:0005413), [WBbt:0005660](https://bioregistry.io/WBbt:0005660)                                                                                                                |
| `WB:Paper00001807` |              3 | [WBbt:0005779](https://bioregistry.io/WBbt:0005779), [WBbt:0005780](https://bioregistry.io/WBbt:0005780), [WBbt:0007810](https://bioregistry.io/WBbt:0007810)                                                                                                                |
| `WB:cgc3760`       |              3 | [WBbt:0005832](https://bioregistry.io/WBbt:0005832), [WBbt:0005832](https://bioregistry.io/WBbt:0005832), [WBbt:0005833](https://bioregistry.io/WBbt:0005833)                                                                                                                |
| `WB:Paper00005027` |              3 | [WBbt:0006859](https://bioregistry.io/WBbt:0006859), [WBbt:0006860](https://bioregistry.io/WBbt:0006860), [WBbt:0006861](https://bioregistry.io/WBbt:0006861)                                                                                                                |
| `WB:RYNL`          |              2 | [WBbt:0000101](https://bioregistry.io/WBbt:0000101), [WBbt:0000101](https://bioregistry.io/WBbt:0000101)                                                                                                                                                                     |
| `WB:Paper00004052` |              2 | [WBbt:0005154](https://bioregistry.io/WBbt:0005154), [WBbt:0005171](https://bioregistry.io/WBbt:0005171)                                                                                                                                                                     |
| `WB:Paper00000193` |              2 | [WBbt:0006870](https://bioregistry.io/WBbt:0006870), [WBbt:0008321](https://bioregistry.io/WBbt:0008321)                                                                                                                                                                     |
| `WB:Paper00003633` |              2 | [WBbt:0008447](https://bioregistry.io/WBbt:0008447), [WBbt:0008448](https://bioregistry.io/WBbt:0008448)                                                                                                                                                                     |
| `WB:Paper00000596` |              1 | [WBbt:0004535](https://bioregistry.io/WBbt:0004535)                                                                                                                                                                                                                          |
| `WB:Paper00000978` |              1 | [WBbt:0005742](https://bioregistry.io/WBbt:0005742)                                                                                                                                                                                                                          |
| `WB:Paper00000653` |              1 | [WBbt:0005796](https://bioregistry.io/WBbt:0005796)                                                                                                                                                                                                                          |
| `WB:Paper00001594` |              1 | [WBbt:0006761](https://bioregistry.io/WBbt:0006761)                                                                                                                                                                                                                          |
| `WB:Paper00000536` |              1 | [WBbt:0006850](https://bioregistry.io/WBbt:0006850)                                                                                                                                                                                                                          |
| `WB:Paper00006002` |              1 | [WBbt:0007854](https://bioregistry.io/WBbt:0007854)                                                                                                                                                                                                                          |

## `Wb`: WormBase database of nematode biology

Overall, there were 3 invalid
xrefs to external prefixed with `Wb` (standardized to Bioregistry
entry [`wormbase`]((https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref   |   usages_count | usages                                                                                                   |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------|
| `Wb:rynl`       |              2 | [WBbt:0005370](https://bioregistry.io/WBbt:0005370), [WBbt:0005839](https://bioregistry.io/WBbt:0005839) |
| `Wb:wjc`        |              1 | [WBbt:0006762](https://bioregistry.io/WBbt:0006762)                                                      |

## `wB`: WormBase database of nematode biology

Overall, there were 1 invalid
xrefs to external prefixed with `wB` (standardized to Bioregistry
entry [`wormbase`]((https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `wB:rynl`       |              1 | [WBbt:0008445](https://bioregistry.io/WBbt:0008445) |

