# tads

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `tads`. See the [GitHub repository](https://github.com/VEuPathDB-ontology/TADS)


## `ISBN`: International Standard Book Number

Overall, there were 3 invalid
xrefs to external prefixed with `ISBN` (standardized to Bioregistry
entry [`isbn`]((https://bioregistry.io/isbn)) that
did not match the standard pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`.

| external_xref         |   usages_count | usages                                                                                                   |
|-----------------------|----------------|----------------------------------------------------------------------------------------------------------|
| `ISBN:0-19-5505910-7` |              2 | [TADS:0000285](https://bioregistry.io/TADS:0000285), [TADS:0000286](https://bioregistry.io/TADS:0000286) |
| `ISBN:0-19-505910-7.` |              1 | [TADS:0000026](https://bioregistry.io/TADS:0000026)                                                      |

## `ISSN`: International Standard Serial Number

Overall, there were 6 invalid
xrefs to external prefixed with `ISSN` (standardized to Bioregistry
entry [`issn`]((https://bioregistry.io/issn)) that
did not match the standard pattern `^\d{4}-\d{3}[\dX]$`.

| external_xref                                   |   usages_count | usages                                              |
|-------------------------------------------------|----------------|-----------------------------------------------------|
| `ISSN:1516-635X.`                               |              1 | [TADS:0000244](https://bioregistry.io/TADS:0000244) |
| `ISSN:00168-8162`                               |              1 | [TADS:0000370](https://bioregistry.io/TADS:0000370) |
| `ISSN:0168-8162.`                               |              1 | [TADS:0000382](https://bioregistry.io/TADS:0000382) |
| `ISSN:0040-8166.`                               |              1 | [TADS:0000520](https://bioregistry.io/TADS:0000520) |
| `ISSN:0168-8162 Exp. Appl. Acarol. 17: 631-653` |              1 | [TADS:0000575](https://bioregistry.io/TADS:0000575) |
| `ISSN:0168-8162 Exp. Appl.Acarol. 17: 631-653`  |              1 | [TADS:0000581](https://bioregistry.io/TADS:0000581) |

## `Wikipedia`: Wikipedia

Overall, there were 1 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
entry [`wikipedia.en`]((https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                 |   usages_count | usages                                              |
|-------------------------------|----------------|-----------------------------------------------------|
| `Wikipedia:www.wikipedia.org` |              1 | [TADS:0000224](https://bioregistry.io/TADS:0000224) |

