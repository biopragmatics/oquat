# mpath

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `mpath`.


## `PMID`: PubMed

- Normalized prefix: `pubmed`
- Pattern:`^\d+$`


| identifier                                                    |   appearances | examples                                      |
|---------------------------------------------------------------|---------------|-----------------------------------------------|
| [PMID: 11794381](https://bioregistry.io/PMID: 11794381)       |             1 | [MPATH:40](https://bioregistry.io/MPATH:40)   |
| [PMID:    21191096](https://bioregistry.io/PMID:    21191096) |             1 | [MPATH:815](https://bioregistry.io/MPATH:815) |

## `PMCID`: Pubmed Central

- Normalized prefix: `pmc`
- Pattern:`^PMC\d+$`


| identifier                                              |   appearances | examples                                      |
|---------------------------------------------------------|---------------|-----------------------------------------------|
| [PMCID: 1964945](https://bioregistry.io/PMCID: 1964945) |             1 | [MPATH:499](https://bioregistry.io/MPATH:499) |

## `MPATH`: Mouse pathology ontology

- Normalized prefix: `mpath`
- Pattern:`^\d+$`


| identifier                                                                    |   appearances | examples                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MPATH:curation](https://bioregistry.io/MPATH:curation)                       |            53 | [MPATH:817](https://bioregistry.io/MPATH:817), [MPATH:825](https://bioregistry.io/MPATH:825), [MPATH:857](https://bioregistry.io/MPATH:857), [MPATH:857](https://bioregistry.io/MPATH:857), [MPATH:863](https://bioregistry.io/MPATH:863), ... |
| [MPATH:Sundberg](https://bioregistry.io/MPATH:Sundberg)                       |            51 | [MPATH:751](https://bioregistry.io/MPATH:751), [MPATH:757](https://bioregistry.io/MPATH:757), [MPATH:763](https://bioregistry.io/MPATH:763), [MPATH:799](https://bioregistry.io/MPATH:799), [MPATH:801](https://bioregistry.io/MPATH:801), ... |
| [MPATH:PNS](https://bioregistry.io/MPATH:PNS)                                 |            17 | [MPATH:770](https://bioregistry.io/MPATH:770), [MPATH:773](https://bioregistry.io/MPATH:773), [MPATH:776](https://bioregistry.io/MPATH:776), [MPATH:780](https://bioregistry.io/MPATH:780), [MPATH:889](https://bioregistry.io/MPATH:889), ... |
| [MPATH:Pathology Committee](https://bioregistry.io/MPATH:Pathology Committee) |            11 | [MPATH:724](https://bioregistry.io/MPATH:724), [MPATH:874](https://bioregistry.io/MPATH:874), [MPATH:874](https://bioregistry.io/MPATH:874), [MPATH:879](https://bioregistry.io/MPATH:879), [MPATH:879](https://bioregistry.io/MPATH:879), ... |
| [MPATH:JPS](https://bioregistry.io/MPATH:JPS)                                 |             4 | [MPATH:882](https://bioregistry.io/MPATH:882), [MPATH:883](https://bioregistry.io/MPATH:883), [MPATH:884](https://bioregistry.io/MPATH:884), [MPATH:888](https://bioregistry.io/MPATH:888)                                                     |
| [MPATH:<new dbxref>](https://bioregistry.io/MPATH:<new dbxref>)               |             3 | [MPATH:770](https://bioregistry.io/MPATH:770), [MPATH:771](https://bioregistry.io/MPATH:771), [MPATH:772](https://bioregistry.io/MPATH:772)                                                                                                    |
| [MPATH:Curation](https://bioregistry.io/MPATH:Curation)                       |             1 | [MPATH:656](https://bioregistry.io/MPATH:656)                                                                                                                                                                                                  |
| [MPATH::Sundberg](https://bioregistry.io/MPATH::Sundberg)                     |             1 | [MPATH:746](https://bioregistry.io/MPATH:746)                                                                                                                                                                                                  |
| [MPATH:Pathology committee](https://bioregistry.io/MPATH:Pathology committee) |             1 | [MPATH:809](https://bioregistry.io/MPATH:809)                                                                                                                                                                                                  |
| [MPATH:curationf>](https://bioregistry.io/MPATH:curationf>)                   |             1 | [MPATH:865](https://bioregistry.io/MPATH:865)                                                                                                                                                                                                  |

## `ICD-O`: International Classification of Diseases for Oncology

- Normalized prefix: `icdo`
- Pattern:`^[8-9]\d{3}(/[0-3])?$`


| identifier                                              |   appearances | examples                                      |
|---------------------------------------------------------|---------------|-----------------------------------------------|
| [ICD-O:M-8900/0](https://bioregistry.io/ICD-O:M-8900/0) |             1 | [MPATH:722](https://bioregistry.io/MPATH:722) |

## `ICDO`: International Classification of Diseases for Oncology

- Normalized prefix: `icdo`
- Pattern:`^[8-9]\d{3}(/[0-3])?$`


| identifier                                            |   appearances | examples                                      |
|-------------------------------------------------------|---------------|-----------------------------------------------|
| [ICDO:M-8822/1](https://bioregistry.io/ICDO:M-8822/1) |             1 | [MPATH:723](https://bioregistry.io/MPATH:723) |

## `mpath`: Mouse pathology ontology

- Normalized prefix: `mpath`
- Pattern:`^\d+$`


| identifier                                                      |   appearances | examples                                      |
|-----------------------------------------------------------------|---------------|-----------------------------------------------|
| [mpath:<new dbxref>](https://bioregistry.io/mpath:<new dbxref>) |             1 | [MPATH:775](https://bioregistry.io/MPATH:775) |
| [mpath:curation](https://bioregistry.io/mpath:curation)         |             1 | [MPATH:833](https://bioregistry.io/MPATH:833) |

## `ISBN`: International Standard Book Number

- Normalized prefix: `isbn`
- Pattern:`^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`


| identifier                                                          |   appearances | examples                                      |
|---------------------------------------------------------------------|---------------|-----------------------------------------------|
| [ISBN: 0-7216-2921-0.](https://bioregistry.io/ISBN: 0-7216-2921-0.) |             1 | [MPATH:859](https://bioregistry.io/MPATH:859) |

