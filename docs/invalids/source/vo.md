# vo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vo`. See the [GitHub repository](https://github.com/vaccineontology/VO).


## `MeSH`: Medical Subject Headings

Overall, there were 23 invalid
xrefs to external prefixed with `MeSH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D|M)\d{6,9}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `MeSH: D014612` |              1 | [VO:0000001](http://purl.obolibrary.org/obo/VO_0000001) |
| `MeSH: D022122` |              1 | [VO:0000013](http://purl.obolibrary.org/obo/VO_0000013) |
| `MeSH: D002004` |              1 | [VO:0000025](http://purl.obolibrary.org/obo/VO_0000025) |
| `MeSH: D022361` |              1 | [VO:0000041](http://purl.obolibrary.org/obo/VO_0000041) |
| `MeSH: D022401` |              1 | [VO:0000053](http://purl.obolibrary.org/obo/VO_0000053) |
| `MeSH: D001428` |              1 | [VO:0000165](http://purl.obolibrary.org/obo/VO_0000165) |
| `MeSH: D005657` |              1 | [VO:0000267](http://purl.obolibrary.org/obo/VO_0000267) |
| `MeSH: D016052` |              1 | [VO:0000417](http://purl.obolibrary.org/obo/VO_0000417) |
| `MeSH: D014765` |              1 | [VO:0000609](http://purl.obolibrary.org/obo/VO_0000609) |
| `MeSH: D017778` |              1 | [VO:0000641](http://purl.obolibrary.org/obo/VO_0000641) |
| `MeSH: D018073` |              1 | [VO:0000661](http://purl.obolibrary.org/obo/VO_0000661) |
| `MeSH: D022581` |              1 | [VO:0000754](http://purl.obolibrary.org/obo/VO_0000754) |
| `MeSH: D022462` |              1 | [VO:0000755](http://purl.obolibrary.org/obo/VO_0000755) |
| `MeSH: D022642` |              1 | [VO:0000759](http://purl.obolibrary.org/obo/VO_0000759) |
| `MeSH: D023582` |              1 | [VO:0000760](http://purl.obolibrary.org/obo/VO_0000760) |
| `MeSH: D022123` |              1 | [VO:0000764](http://purl.obolibrary.org/obo/VO_0000764) |
| `MeSH: D054406` |              1 | [VO:0000766](http://purl.obolibrary.org/obo/VO_0000766) |
| `MeSH: D012290` |              1 | [VO:0000767](http://purl.obolibrary.org/obo/VO_0000767) |
| `MeSH: D022562` |              1 | [VO:0000768](http://purl.obolibrary.org/obo/VO_0000768) |
| `MeSH: D022281` |              1 | [VO:0000769](http://purl.obolibrary.org/obo/VO_0000769) |
| `MeSH: D013209` |              1 | [VO:0000770](http://purl.obolibrary.org/obo/VO_0000770) |
| `MeSH: D022541` |              1 | [VO:0000772](http://purl.obolibrary.org/obo/VO_0000772) |
| `MeSH: D053918` |              1 | [VO:0003538](http://purl.obolibrary.org/obo/VO_0003538) |

## `SNOMEDCT`: SNOMED CT (International Edition)

Overall, there were 6 invalid
xrefs to external prefixed with `SNOMEDCT` (standardized to Bioregistry
prefix [`snomedct`](https://bioregistry.io/snomedct)) that
did not match the standard pattern `^(\w+)?\d+$`.

| external_xref         |   usages_count | usages                                                  |
|-----------------------|----------------|---------------------------------------------------------|
| `SNOMEDCT: 442561000` |              1 | [VO:0000096](http://purl.obolibrary.org/obo/VO_0000096) |
| `SNOMEDCT: 416532007` |              1 | [VO:0000418](http://purl.obolibrary.org/obo/VO_0000418) |
| `SNOMEDCT: 52974007`  |              1 | [VO:0000465](http://purl.obolibrary.org/obo/VO_0000465) |
| `SNOMEDCT: 34679007`  |              1 | [VO:0000467](http://purl.obolibrary.org/obo/VO_0000467) |
| `SNOMEDCT: 424519000` |              1 | [VO:0000667](http://purl.obolibrary.org/obo/VO_0000667) |
| `SNOMEDCT: 55262006`  |              1 | [VO:0002452](http://purl.obolibrary.org/obo/VO_0002452) |

## `UMLS_CUI`: Unified Medical Language System Concept Unique Identifier

Overall, there were 4 invalid
xrefs to external prefixed with `UMLS_CUI` (standardized to Bioregistry
prefix [`umls`](https://bioregistry.io/umls)) that
did not match the standard pattern `^C\d+$`.

| external_xref        |   usages_count | usages                                                  |
|----------------------|----------------|---------------------------------------------------------|
| `UMLS_CUI: C0695130` |              1 | [VO:0000096](http://purl.obolibrary.org/obo/VO_0000096) |
| `UMLS_CUI: C0310856` |              1 | [VO:0000465](http://purl.obolibrary.org/obo/VO_0000465) |
| `UMLS_CUI: C0311044` |              1 | [VO:0000467](http://purl.obolibrary.org/obo/VO_0000467) |
| `UMLS_CUI: C1512511` |              1 | [VO:0000667](http://purl.obolibrary.org/obo/VO_0000667) |

