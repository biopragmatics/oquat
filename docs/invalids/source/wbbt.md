# wbbt

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `wbbt`. See the [GitHub repository](https://github.com/obophenotype/c-elegans-gross-anatomy-ontology).


## `WB`: WormBase database of nematode biology

Overall, there were 5,448 invalid
xrefs to external prefixed with `WB` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref                |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `WB:('WB', 'rynl')`          |           5259 | [WBbt:0000102](http://purl.obolibrary.org/obo/WBbt_0000102), [WBbt:0001001](http://purl.obolibrary.org/obo/WBbt_0001001), [WBbt:0001002](http://purl.obolibrary.org/obo/WBbt_0001002), [WBbt:0001003](http://purl.obolibrary.org/obo/WBbt_0001003), [WBbt:0001004](http://purl.obolibrary.org/obo/WBbt_0001004), ... |
| `WB:('WB', 'Paper00000938')` |             81 | [WBbt:0003938](http://purl.obolibrary.org/obo/WBbt_0003938), [WBbt:0005118](http://purl.obolibrary.org/obo/WBbt_0005118), [WBbt:0005119](http://purl.obolibrary.org/obo/WBbt_0005119), [WBbt:0005270](http://purl.obolibrary.org/obo/WBbt_0005270), [WBbt:0005274](http://purl.obolibrary.org/obo/WBbt_0005274), ... |
| `WB:('WB', 'Paper00002608')` |             24 | [WBbt:0003378](http://purl.obolibrary.org/obo/WBbt_0003378), [WBbt:0003383](http://purl.obolibrary.org/obo/WBbt_0003383), [WBbt:0004113](http://purl.obolibrary.org/obo/WBbt_0004113), [WBbt:0005065](http://purl.obolibrary.org/obo/WBbt_0005065), [WBbt:0005067](http://purl.obolibrary.org/obo/WBbt_0005067), ... |
| `WB:('WB', 'Paper00000462')` |             22 | [WBbt:0002684](http://purl.obolibrary.org/obo/WBbt_0002684), [WBbt:0004008](http://purl.obolibrary.org/obo/WBbt_0004008), [WBbt:0004010](http://purl.obolibrary.org/obo/WBbt_0004010), [WBbt:0004012](http://purl.obolibrary.org/obo/WBbt_0004012), [WBbt:0004014](http://purl.obolibrary.org/obo/WBbt_0004014), ... |
| `WB:('WB', 'wjc')`           |             12 | [WBbt:0006757](http://purl.obolibrary.org/obo/WBbt_0006757), [WBbt:0006758](http://purl.obolibrary.org/obo/WBbt_0006758), [WBbt:0006763](http://purl.obolibrary.org/obo/WBbt_0006763), [WBbt:0006765](http://purl.obolibrary.org/obo/WBbt_0006765), [WBbt:0006766](http://purl.obolibrary.org/obo/WBbt_0006766), ... |
| `WB:('WB', 'Paper00038216')` |              9 | [WBbt:0008411](http://purl.obolibrary.org/obo/WBbt_0008411), [WBbt:0008424](http://purl.obolibrary.org/obo/WBbt_0008424), [WBbt:0008425](http://purl.obolibrary.org/obo/WBbt_0008425), [WBbt:0008426](http://purl.obolibrary.org/obo/WBbt_0008426), [WBbt:0008427](http://purl.obolibrary.org/obo/WBbt_0008427), ... |
| `WB:('WB', 'sdm')`           |              6 | [WBbt:0005244](http://purl.obolibrary.org/obo/WBbt_0005244), [WBbt:0005261](http://purl.obolibrary.org/obo/WBbt_0005261), [WBbt:0005310](http://purl.obolibrary.org/obo/WBbt_0005310), [WBbt:0005373](http://purl.obolibrary.org/obo/WBbt_0005373), [WBbt:0005415](http://purl.obolibrary.org/obo/WBbt_0005415), ... |
| `WB:('WB', 'pws')`           |              5 | [WBbt:0005732](http://purl.obolibrary.org/obo/WBbt_0005732), [WBbt:0005733](http://purl.obolibrary.org/obo/WBbt_0005733), [WBbt:0005733](http://purl.obolibrary.org/obo/WBbt_0005733), [WBbt:0005734](http://purl.obolibrary.org/obo/WBbt_0005734), [WBbt:0005734](http://purl.obolibrary.org/obo/WBbt_0005734)      |
| `WB:('WB', 'Paper00000009')` |              4 | [WBbt:0003638](http://purl.obolibrary.org/obo/WBbt_0003638), [WBbt:0003645](http://purl.obolibrary.org/obo/WBbt_0003645), [WBbt:0003649](http://purl.obolibrary.org/obo/WBbt_0003649), [WBbt:0003666](http://purl.obolibrary.org/obo/WBbt_0003666)                                                                   |
| `WB:('WB', 'cgc938')`        |              3 | [WBbt:0005334](http://purl.obolibrary.org/obo/WBbt_0005334), [WBbt:0005413](http://purl.obolibrary.org/obo/WBbt_0005413), [WBbt:0005660](http://purl.obolibrary.org/obo/WBbt_0005660)                                                                                                                                |
| `WB:('WB', 'Paper00001807')` |              3 | [WBbt:0005779](http://purl.obolibrary.org/obo/WBbt_0005779), [WBbt:0005780](http://purl.obolibrary.org/obo/WBbt_0005780), [WBbt:0007810](http://purl.obolibrary.org/obo/WBbt_0007810)                                                                                                                                |
| `WB:('WB', 'cgc3760')`       |              3 | [WBbt:0005832](http://purl.obolibrary.org/obo/WBbt_0005832), [WBbt:0005832](http://purl.obolibrary.org/obo/WBbt_0005832), [WBbt:0005833](http://purl.obolibrary.org/obo/WBbt_0005833)                                                                                                                                |
| `WB:('WB', 'Paper00005027')` |              3 | [WBbt:0006859](http://purl.obolibrary.org/obo/WBbt_0006859), [WBbt:0006860](http://purl.obolibrary.org/obo/WBbt_0006860), [WBbt:0006861](http://purl.obolibrary.org/obo/WBbt_0006861)                                                                                                                                |
| `WB:('WB', 'RYNL')`          |              2 | [WBbt:0000101](http://purl.obolibrary.org/obo/WBbt_0000101), [WBbt:0000101](http://purl.obolibrary.org/obo/WBbt_0000101)                                                                                                                                                                                             |
| `WB:('WB', 'Paper00004052')` |              2 | [WBbt:0005154](http://purl.obolibrary.org/obo/WBbt_0005154), [WBbt:0005171](http://purl.obolibrary.org/obo/WBbt_0005171)                                                                                                                                                                                             |
| `WB:('WB', 'Paper00000193')` |              2 | [WBbt:0006870](http://purl.obolibrary.org/obo/WBbt_0006870), [WBbt:0008321](http://purl.obolibrary.org/obo/WBbt_0008321)                                                                                                                                                                                             |
| `WB:('WB', 'Paper00003633')` |              2 | [WBbt:0008447](http://purl.obolibrary.org/obo/WBbt_0008447), [WBbt:0008448](http://purl.obolibrary.org/obo/WBbt_0008448)                                                                                                                                                                                             |
| `WB:('WB', 'Paper00000596')` |              1 | [WBbt:0004535](http://purl.obolibrary.org/obo/WBbt_0004535)                                                                                                                                                                                                                                                          |
| `WB:('WB', 'Paper00000978')` |              1 | [WBbt:0005742](http://purl.obolibrary.org/obo/WBbt_0005742)                                                                                                                                                                                                                                                          |
| `WB:('WB', 'Paper00000653')` |              1 | [WBbt:0005796](http://purl.obolibrary.org/obo/WBbt_0005796)                                                                                                                                                                                                                                                          |
| `WB:('WB', 'Paper00001594')` |              1 | [WBbt:0006761](http://purl.obolibrary.org/obo/WBbt_0006761)                                                                                                                                                                                                                                                          |
| `WB:('WB', 'Paper00000536')` |              1 | [WBbt:0006850](http://purl.obolibrary.org/obo/WBbt_0006850)                                                                                                                                                                                                                                                          |
| `WB:('WB', 'Paper00006002')` |              1 | [WBbt:0007854](http://purl.obolibrary.org/obo/WBbt_0007854)                                                                                                                                                                                                                                                          |

## `Wb`: WormBase database of nematode biology

Overall, there were 3 invalid
xrefs to external prefixed with `Wb` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref       |   usages_count | usages                                                                                                                   |
|---------------------|----------------|--------------------------------------------------------------------------------------------------------------------------|
| `Wb:('Wb', 'rynl')` |              2 | [WBbt:0005370](http://purl.obolibrary.org/obo/WBbt_0005370), [WBbt:0005839](http://purl.obolibrary.org/obo/WBbt_0005839) |
| `Wb:('Wb', 'wjc')`  |              1 | [WBbt:0006762](http://purl.obolibrary.org/obo/WBbt_0006762)                                                              |

## `wB`: WormBase database of nematode biology

Overall, there were 1 invalid
xrefs to external prefixed with `wB` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref       |   usages_count | usages                                                      |
|---------------------|----------------|-------------------------------------------------------------|
| `wB:('wB', 'rynl')` |              1 | [WBbt:0008445](http://purl.obolibrary.org/obo/WBbt_0008445) |

