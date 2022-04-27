# plana

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `plana`. See the [GitHub repository](https://github.com/obophenotype/planaria-ontology).


## `ASIN`: Amazon Standard Identification Number

Overall, there were 18 invalid
xrefs to external prefixed with `ASIN` (standardized to Bioregistry
prefix [`asin`](https://bioregistry.io/asin)) that
did not match the standard pattern `^[0-9]{10}$`.

| external_xref     |   usages_count | usages                                                                                                                                                                                                                                                                                 |
|-------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ASIN:B000M4NK9M` |             18 | [PLANA:0000224](https://bioregistry.io/PLANA:0000224), [PLANA:0000224](https://bioregistry.io/PLANA:0000224), [PLANA:0000241](https://bioregistry.io/PLANA:0000241), [PLANA:0000241](https://bioregistry.io/PLANA:0000241), [PLANA:0000472](https://bioregistry.io/PLANA:0000472), ... |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `ncithesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                 |   usages_count | usages                                                |
|-------------------------------|----------------|-------------------------------------------------------|
| `ncithesaurus:Blastemal_Cell` |              1 | [PLANA:0000495](https://bioregistry.io/PLANA:0000495) |

## `PMID`: PubMed

Overall, there were 7 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref    |   usages_count | usages                                                                                                       |
|------------------|----------------|--------------------------------------------------------------------------------------------------------------|
| `PMID: 20967238` |              2 | [PLANA:0003800](https://bioregistry.io/PLANA:0003800), [PLANA:0003801](https://bioregistry.io/PLANA:0003801) |
| `PMID: 23652002` |              1 | [PLANA:0003504](https://bioregistry.io/PLANA:0003504)                                                        |
| `PMID: 29674431` |              1 | [PLANA:0003802](https://bioregistry.io/PLANA:0003802)                                                        |
| `PMID: 29674432` |              1 | [PLANA:0003803](https://bioregistry.io/PLANA:0003803)                                                        |
| `PMID: 29674433` |              1 | [PLANA:0003804](https://bioregistry.io/PLANA:0003804)                                                        |
| `PMID: 22074376` |              1 | [PLANA:0002042](https://bioregistry.io/PLANA:0002042)                                                        |

## `Wikipedia`: Wikipedia

Overall, there were 1 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                      |   usages_count | usages                                                |
|------------------------------------|----------------|-------------------------------------------------------|
| `Wikipedia:Regeneration:(biology)` |              1 | [PLANA:0000137](https://bioregistry.io/PLANA:0000137) |

