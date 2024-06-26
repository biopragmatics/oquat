# tads

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `tads`. See the [GitHub repository](https://github.com/VEuPathDB-ontology/TADS).


## `ISBN`: International Standard Book Number

Overall, there were 3 invalid
xrefs to external prefixed with `ISBN` (standardized to Bioregistry
prefix [`isbn`](https://bioregistry.io/isbn)) that
did not match the standard pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`.

| external_xref         |   usages_count | usages                                                                                                                   |
|-----------------------|----------------|--------------------------------------------------------------------------------------------------------------------------|
| `ISBN:0-19-5505910-7` |              2 | [TADS:0000285](http://purl.obolibrary.org/obo/TADS_0000285), [TADS:0000286](http://purl.obolibrary.org/obo/TADS_0000286) |
| `ISBN:0-19-505910-7.` |              1 | [TADS:0000026](http://purl.obolibrary.org/obo/TADS_0000026)                                                              |

## `ISSN`: International Standard Serial Number

Overall, there were 6 invalid
xrefs to external prefixed with `ISSN` (standardized to Bioregistry
prefix [`issn`](https://bioregistry.io/issn)) that
did not match the standard pattern `^\d{4}-\d{3}[\dX]$`.

| external_xref                                   |   usages_count | usages                                                      |
|-------------------------------------------------|----------------|-------------------------------------------------------------|
| `ISSN:1516-635X.`                               |              1 | [TADS:0000244](http://purl.obolibrary.org/obo/TADS_0000244) |
| `ISSN:00168-8162`                               |              1 | [TADS:0000370](http://purl.obolibrary.org/obo/TADS_0000370) |
| `ISSN:0168-8162.`                               |              1 | [TADS:0000382](http://purl.obolibrary.org/obo/TADS_0000382) |
| `ISSN:0040-8166.`                               |              1 | [TADS:0000520](http://purl.obolibrary.org/obo/TADS_0000520) |
| `ISSN:0168-8162 Exp. Appl. Acarol. 17: 631-653` |              1 | [TADS:0000575](http://purl.obolibrary.org/obo/TADS_0000575) |
| `ISSN:0168-8162 Exp. Appl.Acarol. 17: 631-653`  |              1 | [TADS:0000581](http://purl.obolibrary.org/obo/TADS_0000581) |

