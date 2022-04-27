# tgma

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `tgma`. See the [GitHub repository](https://github.com/VEuPathDB-ontology/TGMA)


## `ISBN`: International Standard Book Number

- Normalized prefix: `isbn`
- [https://bioregistry.io/isbn](https://bioregistry.io/isbn)
- Pattern:`^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`

| identifier                        |   appearances | examples                                                                                                 |
|-----------------------------------|---------------|----------------------------------------------------------------------------------------------------------|
| `ISBN:0-937548-00-60-937548-00-6` |             2 | [TGMA:0000316](https://bioregistry.io/TGMA:0000316), [TGMA:0000457](https://bioregistry.io/TGMA:0000457) |
| `ISBN:0-937548-00-6.`             |             2 | [TGMA:0001282](https://bioregistry.io/TGMA:0001282), [TGMA:0001282](https://bioregistry.io/TGMA:0001282) |
| `ISBN:0--937548-00-6`             |             1 | [TGMA:0001491](https://bioregistry.io/TGMA:0001491)                                                      |
| `ISBN:0-412-40-1800`              |             1 | [TGMA:0001814](https://bioregistry.io/TGMA:0001814)                                                      |

## `ISSN`: International Standard Serial Number

- Normalized prefix: `issn`
- [https://bioregistry.io/issn](https://bioregistry.io/issn)
- Pattern:`^\d{4}-\d{3}[\dX]$`

| identifier        |   appearances | examples                                            |
|-------------------|---------------|-----------------------------------------------------|
| `ISSN:00931-3669` |             1 | [TGMA:0001124](https://bioregistry.io/TGMA:0001124) |

## `PubMed`: PubMed

- Normalized prefix: `pubmed`
- [https://bioregistry.io/pubmed](https://bioregistry.io/pubmed)
- Pattern:`^\d+$`

| identifier             |   appearances | examples                                                                                                                                                                                                                                                                     |
|------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PubMed:PMID:15857775` |             9 | [TGMA:0000001](https://bioregistry.io/TGMA:0000001), [TGMA:0001818](https://bioregistry.io/TGMA:0001818), [TGMA:0001849](https://bioregistry.io/TGMA:0001849), [TGMA:0001851](https://bioregistry.io/TGMA:0001851), [TGMA:0001851](https://bioregistry.io/TGMA:0001851), ... |

