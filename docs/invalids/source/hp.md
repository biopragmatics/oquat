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

Overall, there were 20 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                               |   usages_count | usages                                                                                                           |
|---------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `PMID:probinson`                            |              2 | [HP:0009659](http://purl.obolibrary.org/obo/HP_0009659), [HP:0030789](http://purl.obolibrary.org/obo/HP_0030789) |
| `PMID:31910377|PMID:32179430`               |              1 | [HP:0002494](http://purl.obolibrary.org/obo/HP_0002494)                                                          |
| `PMID:36115370|PMID:30725708|PMID:36872502` |              1 | [HP:0006979](http://purl.obolibrary.org/obo/HP_0006979)                                                          |
| `PMID:34557672|PMID:32374025`               |              1 | [HP:0007159](http://purl.obolibrary.org/obo/HP_0007159)                                                          |
| `PMID:35551411|PMID:36031317`               |              1 | [HP:0010536](http://purl.obolibrary.org/obo/HP_0010536)                                                          |
| `PMID:35808955|PMID:28613628|PMID:34732752` |              1 | [HP:0012452](http://purl.obolibrary.org/obo/HP_0012452)                                                          |
| `PMID:32644427|PMID:30458142`               |              1 | [HP:0025236](http://purl.obolibrary.org/obo/HP_0025236)                                                          |
| `PMID:30228690|PMID:35624073`               |              1 | [HP:0030050](http://purl.obolibrary.org/obo/HP_0030050)                                                          |
| `PMID:30085516rdfs:comment`                 |              1 | [HP:0033585](http://purl.obolibrary.org/obo/HP_0033585)                                                          |
| `PMID:27862615|PMID:18622776`               |              1 | [HP:5200212](http://purl.obolibrary.org/obo/HP_5200212)                                                          |
| `PMID:20636189|PMID:34541953`               |              1 | [HP:5200220](http://purl.obolibrary.org/obo/HP_5200220)                                                          |
| `PMID:30416391;PMID:31582814`               |              1 | [HP:5200235](http://purl.obolibrary.org/obo/HP_5200235)                                                          |
| `PMID:29779616|PMID:34191224`               |              1 | [HP:5200283](http://purl.obolibrary.org/obo/HP_5200283)                                                          |
| `PMID:33205754|PMID:31553690`               |              1 | [HP:5200289](http://purl.obolibrary.org/obo/HP_5200289)                                                          |
| `PMID:23997705|PMID:22560828`               |              1 | [HP:5200292](http://purl.obolibrary.org/obo/HP_5200292)                                                          |
| `PMID:35388549|PMID:36866491`               |              1 | [HP:5200294](http://purl.obolibrary.org/obo/HP_5200294)                                                          |
| `PMID:32809562|PMID:36507891`               |              1 | [HP:5200295](http://purl.obolibrary.org/obo/HP_5200295)                                                          |
| `PMID:31997686;PMID:17391357`               |              1 | [HP:5200310](http://purl.obolibrary.org/obo/HP_5200310)                                                          |
| `PMID:24001164|PMID:26851616`               |              1 | [HP:5200321](http://purl.obolibrary.org/obo/HP_5200321)                                                          |

## `UMLS`: Unified Medical Language System Concept Unique Identifier

Overall, there were 1 invalid
xrefs to external prefixed with `UMLS` (standardized to Bioregistry
prefix [`umls`](https://bioregistry.io/umls)) that
did not match the standard pattern `^C\d+$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `UMLS:0189573`  |              1 | [HP:0034420](http://purl.obolibrary.org/obo/HP_0034420) |

