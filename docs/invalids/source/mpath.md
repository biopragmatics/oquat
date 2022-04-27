# mpath

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `mpath`. See the [GitHub repository](https://github.com/PaulNSchofield/mpath)


## `ICD-O`: International Classification of Diseases for Oncology

- Normalized prefix: `icdo`
- [https://bioregistry.io/icdo](https://bioregistry.io/icdo)
- Pattern:`^[8-9]\d{3}(/[0-3])?$`

| identifier       |   appearances | examples                                      |
|------------------|---------------|-----------------------------------------------|
| `ICD-O:M-8900/0` |             1 | [MPATH:722](https://bioregistry.io/MPATH:722) |

## `ICDO`: International Classification of Diseases for Oncology

- Normalized prefix: `icdo`
- [https://bioregistry.io/icdo](https://bioregistry.io/icdo)
- Pattern:`^[8-9]\d{3}(/[0-3])?$`

| identifier      |   appearances | examples                                      |
|-----------------|---------------|-----------------------------------------------|
| `ICDO:M-8822/1` |             1 | [MPATH:723](https://bioregistry.io/MPATH:723) |

## `ISBN`: International Standard Book Number

- Normalized prefix: `isbn`
- [https://bioregistry.io/isbn](https://bioregistry.io/isbn)
- Pattern:`^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`

| identifier             |   appearances | examples                                      |
|------------------------|---------------|-----------------------------------------------|
| `ISBN: 0-7216-2921-0.` |             1 | [MPATH:859](https://bioregistry.io/MPATH:859) |

## `MPATH`: Mouse pathology ontology

- Normalized prefix: `mpath`
- [https://bioregistry.io/mpath](https://bioregistry.io/mpath)
- Pattern:`^\d+$`

| identifier                  |   appearances | examples                                                                                                                                                                                                                                       |
|-----------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MPATH:curation`            |            53 | [MPATH:825](https://bioregistry.io/MPATH:825), [MPATH:832](https://bioregistry.io/MPATH:832), [MPATH:836](https://bioregistry.io/MPATH:836), [MPATH:850](https://bioregistry.io/MPATH:850), [MPATH:853](https://bioregistry.io/MPATH:853), ... |
| `MPATH:Sundberg`            |            51 | [MPATH:741](https://bioregistry.io/MPATH:741), [MPATH:753](https://bioregistry.io/MPATH:753), [MPATH:788](https://bioregistry.io/MPATH:788), [MPATH:794](https://bioregistry.io/MPATH:794), [MPATH:799](https://bioregistry.io/MPATH:799), ... |
| `MPATH:PNS`                 |            17 | [MPATH:776](https://bioregistry.io/MPATH:776), [MPATH:777](https://bioregistry.io/MPATH:777), [MPATH:779](https://bioregistry.io/MPATH:779), [MPATH:784](https://bioregistry.io/MPATH:784), [MPATH:798](https://bioregistry.io/MPATH:798), ... |
| `MPATH:Pathology Committee` |            11 | [MPATH:874](https://bioregistry.io/MPATH:874), [MPATH:875](https://bioregistry.io/MPATH:875), [MPATH:880](https://bioregistry.io/MPATH:880), [MPATH:885](https://bioregistry.io/MPATH:885), [MPATH:885](https://bioregistry.io/MPATH:885), ... |
| `MPATH:JPS`                 |             4 | [MPATH:882](https://bioregistry.io/MPATH:882), [MPATH:883](https://bioregistry.io/MPATH:883), [MPATH:884](https://bioregistry.io/MPATH:884), [MPATH:888](https://bioregistry.io/MPATH:888)                                                     |
| `MPATH:<new dbxref>`        |             3 | [MPATH:770](https://bioregistry.io/MPATH:770), [MPATH:771](https://bioregistry.io/MPATH:771), [MPATH:772](https://bioregistry.io/MPATH:772)                                                                                                    |
| `MPATH:Curation`            |             1 | [MPATH:656](https://bioregistry.io/MPATH:656)                                                                                                                                                                                                  |
| `MPATH::Sundberg`           |             1 | [MPATH:746](https://bioregistry.io/MPATH:746)                                                                                                                                                                                                  |
| `MPATH:Pathology committee` |             1 | [MPATH:809](https://bioregistry.io/MPATH:809)                                                                                                                                                                                                  |
| `MPATH:curationf>`          |             1 | [MPATH:865](https://bioregistry.io/MPATH:865)                                                                                                                                                                                                  |

## `mpath`: Mouse pathology ontology

- Normalized prefix: `mpath`
- [https://bioregistry.io/mpath](https://bioregistry.io/mpath)
- Pattern:`^\d+$`

| identifier           |   appearances | examples                                      |
|----------------------|---------------|-----------------------------------------------|
| `mpath:<new dbxref>` |             1 | [MPATH:775](https://bioregistry.io/MPATH:775) |
| `mpath:curation`     |             1 | [MPATH:833](https://bioregistry.io/MPATH:833) |

## `PMCID`: Pubmed Central

- Normalized prefix: `pmc`
- [https://bioregistry.io/pmc](https://bioregistry.io/pmc)
- Pattern:`^PMC\d+$`

| identifier       |   appearances | examples                                      |
|------------------|---------------|-----------------------------------------------|
| `PMCID: 1964945` |             1 | [MPATH:499](https://bioregistry.io/MPATH:499) |

## `PMID`: PubMed

- Normalized prefix: `pubmed`
- [https://bioregistry.io/pubmed](https://bioregistry.io/pubmed)
- Pattern:`^\d+$`

| identifier          |   appearances | examples                                      |
|---------------------|---------------|-----------------------------------------------|
| `PMID: 11794381`    |             1 | [MPATH:40](https://bioregistry.io/MPATH:40)   |
| `PMID:    21191096` |             1 | [MPATH:815](https://bioregistry.io/MPATH:815) |

