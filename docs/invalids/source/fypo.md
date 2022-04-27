# fypo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `fypo`.


## `PomBase`: PomBase

- Normalized prefix: `pombase`
- Pattern:`^S\w+(\.)?\w+(\.)?$`


| identifier                                            |   appearances | examples                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PomBase:mah](https://bioregistry.io/PomBase:mah)     |         14849 | [FYPO:0002174](https://bioregistry.io/FYPO:0002174), [FYPO:0002622](https://bioregistry.io/FYPO:0002622), [FYPO:0004286](https://bioregistry.io/FYPO:0004286), [FYPO:0006286](https://bioregistry.io/FYPO:0006286), [FYPO:0006934](https://bioregistry.io/FYPO:0006934), ... |
| [PomBase:vw](https://bioregistry.io/PomBase:vw)       |          1969 | [FYPO:0000947](https://bioregistry.io/FYPO:0000947), [FYPO:0002638](https://bioregistry.io/FYPO:0002638), [FYPO:0003305](https://bioregistry.io/FYPO:0003305), [FYPO:0007139](https://bioregistry.io/FYPO:0007139), [FYPO:0007873](https://bioregistry.io/FYPO:0007873), ... |
| [PomBase:al](https://bioregistry.io/PomBase:al)       |          1076 | [FYPO:0001285](https://bioregistry.io/FYPO:0001285), [FYPO:0001483](https://bioregistry.io/FYPO:0001483), [FYPO:0002161](https://bioregistry.io/FYPO:0002161), [FYPO:0003676](https://bioregistry.io/FYPO:0003676), [FYPO:0005639](https://bioregistry.io/FYPO:0005639), ... |
| [PomBase:jh](https://bioregistry.io/PomBase:jh)       |            93 | [FYPO:0000284](https://bioregistry.io/FYPO:0000284), [FYPO:0000318](https://bioregistry.io/FYPO:0000318), [FYPO:0002280](https://bioregistry.io/FYPO:0002280), [FYPO:0002296](https://bioregistry.io/FYPO:0002296), [FYPO:0007659](https://bioregistry.io/FYPO:0007659), ... |
| [PomBase:val](https://bioregistry.io/PomBase:val)     |            16 | [FYPO:0007906](https://bioregistry.io/FYPO:0007906), [FYPO:0007943](https://bioregistry.io/FYPO:0007943), [FYPO:0007944](https://bioregistry.io/FYPO:0007944), [FYPO:0007952](https://bioregistry.io/FYPO:0007952), [FYPO:0007953](https://bioregistry.io/FYPO:0007953), ... |
| [PomBase:amc](https://bioregistry.io/PomBase:amc)     |             3 | [FYPO:0004251](https://bioregistry.io/FYPO:0004251), [FYPO:0006087](https://bioregistry.io/FYPO:0006087), [FYPO:0006318](https://bioregistry.io/FYPO:0006318)                                                                                                                |
| [PomBase:mp](https://bioregistry.io/PomBase:mp)       |             2 | [FYPO:0001404](https://bioregistry.io/FYPO:0001404), [FYPO:0001405](https://bioregistry.io/FYPO:0001405)                                                                                                                                                                     |
| [PomBase:gs](https://bioregistry.io/PomBase:gs)       |             2 | [FYPO:0002484](https://bioregistry.io/FYPO:0002484), [FYPO:0002485](https://bioregistry.io/FYPO:0002485)                                                                                                                                                                     |
| [PomBase:ch](https://bioregistry.io/PomBase:ch)       |             1 | [FYPO:0000153](https://bioregistry.io/FYPO:0000153)                                                                                                                                                                                                                          |
| [PomBase:pr](https://bioregistry.io/PomBase:pr)       |             1 | [FYPO:0005334](https://bioregistry.io/FYPO:0005334)                                                                                                                                                                                                                          |
| [PomBase:mahle](https://bioregistry.io/PomBase:mahle) |             1 | [FYPO:0007633](https://bioregistry.io/FYPO:0007633)                                                                                                                                                                                                                          |
| [PomBase:sm](https://bioregistry.io/PomBase:sm)       |             1 | [FYPO:0007683](https://bioregistry.io/FYPO:0007683)                                                                                                                                                                                                                          |

## `GO`: Gene Ontology

- Normalized prefix: `go`
- Pattern:`^\d{7}$`


| identifier                                                              |   appearances | examples                                                                                                                                                      |
|-------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GO:0036124,PomBase:mah](https://bioregistry.io/GO:0036124,PomBase:mah) |             3 | [FYPO:0007507](https://bioregistry.io/FYPO:0007507), [FYPO:0007508](https://bioregistry.io/FYPO:0007508), [FYPO:0007509](https://bioregistry.io/FYPO:0007509) |
| [GO:006355](https://bioregistry.io/GO:006355)                           |             2 | [FYPO:0004526](https://bioregistry.io/FYPO:0004526), [FYPO:0004527](https://bioregistry.io/FYPO:0004527)                                                      |
| [GO:001322](https://bioregistry.io/GO:001322)                           |             1 | [FYPO:0003561](https://bioregistry.io/FYPO:0003561)                                                                                                           |
| [GO:030995](https://bioregistry.io/GO:030995)                           |             1 | [FYPO:0004270](https://bioregistry.io/FYPO:0004270)                                                                                                           |
| [GO:003118](https://bioregistry.io/GO:003118)                           |             1 | [FYPO:0007501](https://bioregistry.io/FYPO:0007501)                                                                                                           |

## `PMID`: PubMed

- Normalized prefix: `pubmed`
- Pattern:`^\d+$`


| identifier                                            |   appearances | examples                                            |
|-------------------------------------------------------|---------------|-----------------------------------------------------|
| [PMID:34805795
PomBase:val](https://bioregistry.io/PMID:34805795
PomBase:val)                                                       |             1 | [FYPO:0007907](https://bioregistry.io/FYPO:0007907) |
| [PMID::8247131](https://bioregistry.io/PMID::8247131) |             1 | [FYPO:0001686](https://bioregistry.io/FYPO:0001686) |

## `SGD`: Saccharomyces Genome Database

- Normalized prefix: `sgd`
- Pattern:`^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`


| identifier                                                                  |   appearances | examples                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SGD:phenotype_annotation](https://bioregistry.io/SGD:phenotype_annotation) |           293 | [FYPO:0000360](https://bioregistry.io/FYPO:0000360), [FYPO:0000426](https://bioregistry.io/FYPO:0000426), [FYPO:0000467](https://bioregistry.io/FYPO:0000467), [FYPO:0000536](https://bioregistry.io/FYPO:0000536), [FYPO:0000582](https://bioregistry.io/FYPO:0000582), ... |

## `Pombase`: PomBase

- Normalized prefix: `pombase`
- Pattern:`^S\w+(\.)?\w+(\.)?$`


| identifier                                        |   appearances | examples                                                                                                                                                                                                                                                                     |
|---------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Pombase:vw](https://bioregistry.io/Pombase:vw)   |            29 | [FYPO:0004749](https://bioregistry.io/FYPO:0004749), [FYPO:0005363](https://bioregistry.io/FYPO:0005363), [FYPO:0007051](https://bioregistry.io/FYPO:0007051), [FYPO:0007067](https://bioregistry.io/FYPO:0007067), [FYPO:0007491](https://bioregistry.io/FYPO:0007491), ... |
| [Pombase:al](https://bioregistry.io/Pombase:al)   |             6 | [FYPO:0005527](https://bioregistry.io/FYPO:0005527), [FYPO:0005528](https://bioregistry.io/FYPO:0005528), [FYPO:0006260](https://bioregistry.io/FYPO:0006260), [FYPO:0007084](https://bioregistry.io/FYPO:0007084), [FYPO:0007144](https://bioregistry.io/FYPO:0007144), ... |
| [Pombase:mah](https://bioregistry.io/Pombase:mah) |             4 | [FYPO:0005385](https://bioregistry.io/FYPO:0005385), [FYPO:0005396](https://bioregistry.io/FYPO:0005396), [FYPO:0006770](https://bioregistry.io/FYPO:0006770), [FYPO:0007288](https://bioregistry.io/FYPO:0007288)                                                           |

## `SO`: Sequence types and features ontology

- Normalized prefix: `so`
- Pattern:`^\d{7}$`


| identifier                                |   appearances | examples                                            |
|-------------------------------------------|---------------|-----------------------------------------------------|
| [SO:1861](https://bioregistry.io/SO:1861) |             1 | [FYPO:0003251](https://bioregistry.io/FYPO:0003251) |

