# hp

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `hp`. See the [GitHub repository](https://github.com/obophenotype/human-phenotype-ontology).


## `ICD-10`: International Classification of Diseases, 10th Revision

Overall, there were 1 invalid
xrefs to external prefixed with `ICD-10` (standardized to Bioregistry
prefix [`icd10`](https://bioregistry.io/icd10)) that
did not match the standard pattern `^(([XVI]+)|([A-Z][0-9]+((-[A-Z][0-9]+)|(\.[0-9]))?))$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `ICD-10:26.8`   |              1 | [HP:0011671](http://purl.obolibrary.org/obo/HP_0011671) |

## `ICD-O`: International Classification of Diseases for Oncology

Overall, there were 2 invalid
xrefs to external prefixed with `ICD-O` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `ICD-O:M8272/0` |              1 | [HP:0002893](http://purl.obolibrary.org/obo/HP_0002893) |
| `ICD-O:M9982/3` |              1 | [HP:0004828](http://purl.obolibrary.org/obo/HP_0004828) |

## `ISBN`: International Standard Book Number

Overall, there were 1 invalid
xrefs to external prefixed with `ISBN` (standardized to Bioregistry
prefix [`isbn`](https://bioregistry.io/isbn)) that
did not match the standard pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`.

| external_xref      |   usages_count | usages                                                  |
|--------------------|----------------|---------------------------------------------------------|
| `ISBN:0412792702.` |              1 | [HP:0032984](http://purl.obolibrary.org/obo/HP_0032984) |

## `NCIT`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCIT` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `NCIT:CL017969` |              1 | [HP:0031018](http://purl.obolibrary.org/obo/HP_0031018) |

## `OMIM`: Online Mendelian Inheritance in Man

Overall, there were 1 invalid
xrefs to external prefixed with `OMIM` (standardized to Bioregistry
prefix [`omim`](https://bioregistry.io/omim)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `OMIM:ahamosh`  |              1 | [HP:0033628](http://purl.obolibrary.org/obo/HP_0033628) |

## `PMID`: PubMed

Overall, there were 3 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref               |   usages_count | usages                                                                                                           |
|-----------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `PMID:probinson`            |              2 | [HP:0009659](http://purl.obolibrary.org/obo/HP_0009659), [HP:0030789](http://purl.obolibrary.org/obo/HP_0030789) |
| `PMID:30085516rdfs:comment` |              1 | [HP:0033585](http://purl.obolibrary.org/obo/HP_0033585)                                                          |

## `UMLS`: Unified Medical Language System Concept Unique Identifier

Overall, there were 1 invalid
xrefs to external prefixed with `UMLS` (standardized to Bioregistry
prefix [`umls`](https://bioregistry.io/umls)) that
did not match the standard pattern `^C\d+$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `UMLS:0189573`  |              1 | [HP:0034420](http://purl.obolibrary.org/obo/HP_0034420) |

