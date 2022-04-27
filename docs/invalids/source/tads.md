# tads

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `tads`. See the [GitHub repository](https://github.com/VEuPathDB-ontology/TADS)


## `ISBN`: International Standard Book Number

- Normalized prefix: `isbn`
- [https://bioregistry.io/isbn](https://bioregistry.io/isbn)
- Pattern:`^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`

| identifier            |   appearances | examples                                                                                                 |
|-----------------------|---------------|----------------------------------------------------------------------------------------------------------|
| `ISBN:0-19-5505910-7` |             2 | [TADS:0000285](https://bioregistry.io/TADS:0000285), [TADS:0000286](https://bioregistry.io/TADS:0000286) |
| `ISBN:0-19-505910-7.` |             1 | [TADS:0000026](https://bioregistry.io/TADS:0000026)                                                      |

## `ISSN`: International Standard Serial Number

- Normalized prefix: `issn`
- [https://bioregistry.io/issn](https://bioregistry.io/issn)
- Pattern:`^\d{4}-\d{3}[\dX]$`

| identifier                                      |   appearances | examples                                            |
|-------------------------------------------------|---------------|-----------------------------------------------------|
| `ISSN:1516-635X.`                               |             1 | [TADS:0000244](https://bioregistry.io/TADS:0000244) |
| `ISSN:00168-8162`                               |             1 | [TADS:0000370](https://bioregistry.io/TADS:0000370) |
| `ISSN:0168-8162.`                               |             1 | [TADS:0000382](https://bioregistry.io/TADS:0000382) |
| `ISSN:0040-8166.`                               |             1 | [TADS:0000520](https://bioregistry.io/TADS:0000520) |
| `ISSN:0168-8162 Exp. Appl. Acarol. 17: 631-653` |             1 | [TADS:0000575](https://bioregistry.io/TADS:0000575) |
| `ISSN:0168-8162 Exp. Appl.Acarol. 17: 631-653`  |             1 | [TADS:0000581](https://bioregistry.io/TADS:0000581) |

## `Wikipedia`: Wikipedia

- Normalized prefix: `wikipedia.en`
- [https://bioregistry.io/wikipedia.en](https://bioregistry.io/wikipedia.en)
- Pattern:`^[A-Za-z-0-9_]+$`

| identifier                    |   appearances | examples                                            |
|-------------------------------|---------------|-----------------------------------------------------|
| `Wikipedia:www.wikipedia.org` |             1 | [TADS:0000224](https://bioregistry.io/TADS:0000224) |

