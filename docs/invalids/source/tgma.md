# tgma

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `tgma`. See the [GitHub repository](https://github.com/VEuPathDB-ontology/TGMA).


## `ISBN`: International Standard Book Number

Overall, there were 6 invalid
xrefs to external prefixed with `ISBN` (standardized to Bioregistry
prefix [`isbn`](https://bioregistry.io/isbn)) that
did not match the standard pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`.

| external_xref                     |   usages_count | usages                                                                                                                   |
|-----------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------|
| `ISBN:0-937548-00-60-937548-00-6` |              2 | [TGMA:0000316](http://purl.obolibrary.org/obo/TGMA_0000316), [TGMA:0000457](http://purl.obolibrary.org/obo/TGMA_0000457) |
| `ISBN:0-937548-00-6.`             |              2 | [TGMA:0001282](http://purl.obolibrary.org/obo/TGMA_0001282), [TGMA:0001282](http://purl.obolibrary.org/obo/TGMA_0001282) |
| `ISBN:0--937548-00-6`             |              1 | [TGMA:0001491](http://purl.obolibrary.org/obo/TGMA_0001491)                                                              |
| `ISBN:0-412-40-1800`              |              1 | [TGMA:0001814](http://purl.obolibrary.org/obo/TGMA_0001814)                                                              |

## `ISSN`: International Standard Serial Number

Overall, there were 1 invalid
xrefs to external prefixed with `ISSN` (standardized to Bioregistry
prefix [`issn`](https://bioregistry.io/issn)) that
did not match the standard pattern `^\d{4}-\d{3}[\dX]$`.

| external_xref     |   usages_count | usages                                                      |
|-------------------|----------------|-------------------------------------------------------------|
| `ISSN:00931-3669` |              1 | [TGMA:0001124](http://purl.obolibrary.org/obo/TGMA_0001124) |

## `PubMed`: PubMed ID

Overall, there were 9 invalid
xrefs to external prefixed with `PubMed` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref          |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PubMed:PMID:15857775` |              9 | [TGMA:0000001](http://purl.obolibrary.org/obo/TGMA_0000001), [TGMA:0000710](http://purl.obolibrary.org/obo/TGMA_0000710), [TGMA:0000910](http://purl.obolibrary.org/obo/TGMA_0000910), [TGMA:0001818](http://purl.obolibrary.org/obo/TGMA_0001818), [TGMA:0001849](http://purl.obolibrary.org/obo/TGMA_0001849), ... |

