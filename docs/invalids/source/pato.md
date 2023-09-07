# pato

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `pato`. See the [GitHub repository](https://github.com/pato-ontology/pato).


## `ENVO`: Environment Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `ENVO` (standardized to Bioregistry
prefix [`envo`](https://bioregistry.io/envo)) that
did not match the standard pattern `^\d{7,8}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ENVO:pb`       |              3 | [PATO:0015017](http://purl.obolibrary.org/obo/PATO_0015017), [PATO:0015018](http://purl.obolibrary.org/obo/PATO_0015018), [PATO:0015029](http://purl.obolibrary.org/obo/PATO_0015029) |

## `GO`: Gene Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:GO`         |              3 | [PATO:0001440](http://purl.obolibrary.org/obo/PATO_0001440), [PATO:0001441](http://purl.obolibrary.org/obo/PATO_0001441), [PATO:0001720](http://purl.obolibrary.org/obo/PATO_0001720) |

## `ISSN`: International Standard Serial Number

Overall, there were 1 invalid
xrefs to external prefixed with `ISSN` (standardized to Bioregistry
prefix [`issn`](https://bioregistry.io/issn)) that
did not match the standard pattern `^\d{4}-\d{3}[\dX]$`.

| external_xref        |   usages_count | usages                                                      |
|----------------------|----------------|-------------------------------------------------------------|
| `ISSN:9781496335418` |              1 | [PATO:0001744](http://purl.obolibrary.org/obo/PATO_0001744) |

## `Medline`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `Medline` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                                |   usages_count | usages                                                      |
|----------------------------------------------|----------------|-------------------------------------------------------------|
| `Medline:http://www.nlm.nih.gov/medlineplus` |              1 | [PATO:0002048](http://purl.obolibrary.org/obo/PATO_0002048) |

## `neurolex`: NIF Standard Ontology: Neurolex

Overall, there were 2 invalid
xrefs to external prefixed with `neurolex` (standardized to Bioregistry
prefix [`neurolex`](https://bioregistry.io/neurolex)) that
did not match the standard pattern `^\d+$`.

| external_xref                                                           |   usages_count | usages                                                      |
|-------------------------------------------------------------------------|----------------|-------------------------------------------------------------|
| `neurolex:http://neurolex.org/`                                         |              1 | [PATO:0002216](http://purl.obolibrary.org/obo/PATO_0002216) |
| `neurolex:http://neurolex.org/wiki/Category:Nitrated_Molecular_Quality` |              1 | [PATO:0002217](http://purl.obolibrary.org/obo/PATO_0002217) |

## `OBI`: Ontology for Biomedical Investigations

Overall, there were 1 invalid
xrefs to external prefixed with `OBI` (standardized to Bioregistry
prefix [`obi`](https://bioregistry.io/obi)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `OBI:OBI`       |              1 | [PATO:0001985](http://purl.obolibrary.org/obo/PATO_0001985) |

## `OBO_REL`: Relation Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `OBO_REL` (standardized to Bioregistry
prefix [`ro`](https://bioregistry.io/ro)) that
did not match the standard pattern `^(HOM)?\d{7}$`.

| external_xref        |   usages_count | usages                                                      |
|----------------------|----------------|-------------------------------------------------------------|
| `OBO_REL:has_part`   |              1 | [PATO:0001555](http://purl.obolibrary.org/obo/PATO_0001555) |
| `OBO_REL:lacks_part` |              1 | [PATO:0002000](http://purl.obolibrary.org/obo/PATO_0002000) |

## `PATO`: Phenotype And Trait Ontology

Overall, there were 69 invalid
xrefs to external prefixed with `PATO` (standardized to Bioregistry
prefix [`pato`](https://bioregistry.io/pato)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PATO:GVG`      |             54 | [PATO:0000911](http://purl.obolibrary.org/obo/PATO_0000911), [PATO:0000912](http://purl.obolibrary.org/obo/PATO_0000912), [PATO:0001153](http://purl.obolibrary.org/obo/PATO_0001153), [PATO:0001304](http://purl.obolibrary.org/obo/PATO_0001304), [PATO:0001313](http://purl.obolibrary.org/obo/PATO_0001313), ... |
| `PATO:MAH`      |              8 | [PATO:0000428](http://purl.obolibrary.org/obo/PATO_0000428), [PATO:0001559](http://purl.obolibrary.org/obo/PATO_0001559), [PATO:0001624](http://purl.obolibrary.org/obo/PATO_0001624), [PATO:0001625](http://purl.obolibrary.org/obo/PATO_0001625), [PATO:0002629](http://purl.obolibrary.org/obo/PATO_0002629), ... |
| `PATO:LC`       |              2 | [PATO:0000694](http://purl.obolibrary.org/obo/PATO_0000694), [PATO:0002363](http://purl.obolibrary.org/obo/PATO_0002363)                                                                                                                                                                                             |
| `PATO:WS`       |              1 | [PATO:0002311](http://purl.obolibrary.org/obo/PATO_0002311)                                                                                                                                                                                                                                                          |
| `PATO:WC`       |              1 | [PATO:0002320](http://purl.obolibrary.org/obo/PATO_0002320)                                                                                                                                                                                                                                                          |
| `PATO:PG`       |              1 | [PATO:0002389](http://purl.obolibrary.org/obo/PATO_0002389)                                                                                                                                                                                                                                                          |
| `PATO:DS`       |              1 | [PATO:0002390](http://purl.obolibrary.org/obo/PATO_0002390)                                                                                                                                                                                                                                                          |
| `PATO:JL`       |              1 | [PATO:0002454](http://purl.obolibrary.org/obo/PATO_0002454)                                                                                                                                                                                                                                                          |

## `TO`: Plant Trait Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `TO` (standardized to Bioregistry
prefix [`to`](https://bioregistry.io/to)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                   |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------|
| `TO:TO`         |              2 | [PATO:0001540](http://purl.obolibrary.org/obo/PATO_0001540), [PATO:0001541](http://purl.obolibrary.org/obo/PATO_0001541) |

