# plana

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `plana`.


## `ASIN`: Amazon Standard Identification Number

- Normalized prefix: `asin`
- Pattern:`^[0-9]{10}$`


| identifier                                                |   appearances | examples                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ASIN:B000M4NK9M](https://bioregistry.io/ASIN:B000M4NK9M) |            18 | [PLANA:0000224](https://bioregistry.io/PLANA:0000224), [PLANA:0000473](https://bioregistry.io/PLANA:0000473), [PLANA:0000475](https://bioregistry.io/PLANA:0000475), [PLANA:0007535](https://bioregistry.io/PLANA:0007535), [PLANA:0007535](https://bioregistry.io/PLANA:0007535), ... |

## `PMID`: PubMed

- Normalized prefix: `pubmed`
- Pattern:`^\d+$`


| identifier                                              |   appearances | examples                                                                                                     |
|---------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------|
| [PMID: 20967238](https://bioregistry.io/PMID: 20967238) |             2 | [PLANA:0003800](https://bioregistry.io/PLANA:0003800), [PLANA:0003801](https://bioregistry.io/PLANA:0003801) |
| [PMID: 23652002](https://bioregistry.io/PMID: 23652002) |             1 | [PLANA:0003504](https://bioregistry.io/PLANA:0003504)                                                        |
| [PMID: 29674431](https://bioregistry.io/PMID: 29674431) |             1 | [PLANA:0003802](https://bioregistry.io/PLANA:0003802)                                                        |
| [PMID: 29674432](https://bioregistry.io/PMID: 29674432) |             1 | [PLANA:0003803](https://bioregistry.io/PLANA:0003803)                                                        |
| [PMID: 29674433](https://bioregistry.io/PMID: 29674433) |             1 | [PLANA:0003804](https://bioregistry.io/PLANA:0003804)                                                        |
| [PMID: 22074376](https://bioregistry.io/PMID: 22074376) |             1 | [PLANA:0002042](https://bioregistry.io/PLANA:0002042)                                                        |

## `Wikipedia`: Wikipedia

- Normalized prefix: `wikipedia.en`
- Pattern:`^[A-Za-z-0-9_]+$`


| identifier                                                                                  |   appearances | examples                                              |
|---------------------------------------------------------------------------------------------|---------------|-------------------------------------------------------|
| [Wikipedia:Regeneration:(biology)](https://bioregistry.io/Wikipedia:Regeneration:(biology)) |             1 | [PLANA:0000137](https://bioregistry.io/PLANA:0000137) |

## `ncithesaurus`: NCI Thesaurus

- Normalized prefix: `ncit`
- Pattern:`^C\d+$`


| identifier                                                                        |   appearances | examples                                              |
|-----------------------------------------------------------------------------------|---------------|-------------------------------------------------------|
| [ncithesaurus:Blastemal_Cell](https://bioregistry.io/ncithesaurus:Blastemal_Cell) |             1 | [PLANA:0000495](https://bioregistry.io/PLANA:0000495) |

