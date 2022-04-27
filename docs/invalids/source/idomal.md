# idomal

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `idomal`.


## `BFO`: Basic Formal Ontology

- Normalized prefix: `bfo`
- Pattern:`^\d{7}$`


| identifier                                  |   appearances | examples                                                |
|---------------------------------------------|---------------|---------------------------------------------------------|
| [BFO:SNAP](https://bioregistry.io/BFO:SNAP) |             1 | [IDOMAL:0000002](https://bioregistry.io/IDOMAL:0000002) |

## `Wikipedia`: Wikipedia

- Normalized prefix: `wikipedia.en`
- Pattern:`^[A-Za-z-0-9_]+$`


| identifier                                                              |   appearances | examples                                                |
|-------------------------------------------------------------------------|---------------|---------------------------------------------------------|
| [Wikipedia:Field'sstain](https://bioregistry.io/Wikipedia:Field'sstain) |             1 | [IDOMAL:0000553](https://bioregistry.io/IDOMAL:0000553) |

## `ISBN`: International Standard Book Number

- Normalized prefix: `isbn`
- Pattern:`^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`


| identifier                                                        |   appearances | examples                                                |
|-------------------------------------------------------------------|---------------|---------------------------------------------------------|
| [ISBN:0-8493-15-67-0](https://bioregistry.io/ISBN:0-8493-15-67-0) |             1 | [IDOMAL:0000783](https://bioregistry.io/IDOMAL:0000783) |
| [ISBN:0-412-40180-0:](https://bioregistry.io/ISBN:0-412-40180-0:) |             1 | [IDOMAL:0002188](https://bioregistry.io/IDOMAL:0002188) |

## `NCI`: NCI Thesaurus

- Normalized prefix: `ncit`
- Pattern:`^C\d+$`


| identifier                                            |   appearances | examples                                                  |
|-------------------------------------------------------|---------------|-----------------------------------------------------------|
| [NCI:Thesaurus](https://bioregistry.io/NCI:Thesaurus) |             1 | [IDOMAL:50000048](https://bioregistry.io/IDOMAL:50000048) |

