# plana

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `plana`. See the [GitHub repository](https://github.com/obophenotype/planaria-ontology).


## `ASIN`: Amazon Standard Identification Number

Overall, there were 18 invalid
xrefs to external prefixed with `ASIN` (standardized to Bioregistry
prefix [`asin`](https://bioregistry.io/asin)) that
did not match the standard pattern `^[0-9]{10}$`.

| external_xref     |   usages_count | usages                                                                                                                                                                                                                                                                                                                         |
|-------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ASIN:B000M4NK9M` |             18 | [PLANA:0000224](http://purl.obolibrary.org/obo/PLANA_0000224), [PLANA:0000224](http://purl.obolibrary.org/obo/PLANA_0000224), [PLANA:0000241](http://purl.obolibrary.org/obo/PLANA_0000241), [PLANA:0000241](http://purl.obolibrary.org/obo/PLANA_0000241), [PLANA:0000472](http://purl.obolibrary.org/obo/PLANA_0000472), ... |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `ncithesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^[CRPA]\d+$`.

| external_xref                 |   usages_count | usages                                                        |
|-------------------------------|----------------|---------------------------------------------------------------|
| `ncithesaurus:Blastemal_Cell` |              1 | [PLANA:0000495](http://purl.obolibrary.org/obo/PLANA_0000495) |

## `NIF_Subcellular`: NIF Standard Ontology: Subcellular Entities

Overall, there were 1 invalid
xrefs to external prefixed with `NIF_Subcellular` (standardized to Bioregistry
prefix [`nlx.sub`](https://bioregistry.io/nlx.sub)) that
did not match the standard pattern `^\d+$`.

| external_xref                   |   usages_count | usages                                                        |
|---------------------------------|----------------|---------------------------------------------------------------|
| `NIF_Subcellular:sao1397492660` |              1 | [PLANA:0001005](http://purl.obolibrary.org/obo/PLANA_0001005) |

## `PMID`: PubMed

Overall, there were 7 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref    |   usages_count | usages                                                                                                                       |
|------------------|----------------|------------------------------------------------------------------------------------------------------------------------------|
| `PMID: 20967238` |              2 | [PLANA:0003800](http://purl.obolibrary.org/obo/PLANA_0003800), [PLANA:0003801](http://purl.obolibrary.org/obo/PLANA_0003801) |
| `PMID: 23652002` |              1 | [PLANA:0003504](http://purl.obolibrary.org/obo/PLANA_0003504)                                                                |
| `PMID: 29674431` |              1 | [PLANA:0003802](http://purl.obolibrary.org/obo/PLANA_0003802)                                                                |
| `PMID: 29674432` |              1 | [PLANA:0003803](http://purl.obolibrary.org/obo/PLANA_0003803)                                                                |
| `PMID: 29674433` |              1 | [PLANA:0003804](http://purl.obolibrary.org/obo/PLANA_0003804)                                                                |
| `PMID: 22074376` |              1 | [PLANA:0002042](http://purl.obolibrary.org/obo/PLANA_0002042)                                                                |

