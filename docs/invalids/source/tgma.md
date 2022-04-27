# tgma

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `tgma`. See the [GitHub repository](https://github.com/VEuPathDB-ontology/TGMA)


## `ISBN`: International Standard Book Number

Overall, there were 6 invalid
xrefs to external terms in `isbn` that did not match the standard
pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/isbn).

| external_xref                     |   usages_count | usages                                                                                                   |
|-----------------------------------|----------------|----------------------------------------------------------------------------------------------------------|
| `ISBN:0-937548-00-60-937548-00-6` |              2 | [TGMA:0000316](https://bioregistry.io/TGMA:0000316), [TGMA:0000457](https://bioregistry.io/TGMA:0000457) |
| `ISBN:0-937548-00-6.`             |              2 | [TGMA:0001282](https://bioregistry.io/TGMA:0001282), [TGMA:0001282](https://bioregistry.io/TGMA:0001282) |
| `ISBN:0--937548-00-6`             |              1 | [TGMA:0001491](https://bioregistry.io/TGMA:0001491)                                                      |
| `ISBN:0-412-40-1800`              |              1 | [TGMA:0001814](https://bioregistry.io/TGMA:0001814)                                                      |

## `ISSN`: International Standard Serial Number

Overall, there were 1 invalid
xrefs to external terms in `issn` that did not match the standard
pattern `^\d{4}-\d{3}[\dX]$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/issn).

| external_xref     |   usages_count | usages                                              |
|-------------------|----------------|-----------------------------------------------------|
| `ISSN:00931-3669` |              1 | [TGMA:0001124](https://bioregistry.io/TGMA:0001124) |

## `PubMed`: PubMed

Overall, there were 9 invalid
xrefs to external terms in `pubmed` that did not match the standard
pattern `^\d+$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/pubmed).

| external_xref          |   usages_count | usages                                                                                                                                                                                                                                                                       |
|------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PubMed:PMID:15857775` |              9 | [TGMA:0000001](https://bioregistry.io/TGMA:0000001), [TGMA:0000001](https://bioregistry.io/TGMA:0000001), [TGMA:0001849](https://bioregistry.io/TGMA:0001849), [TGMA:0001851](https://bioregistry.io/TGMA:0001851), [TGMA:0001852](https://bioregistry.io/TGMA:0001852), ... |

