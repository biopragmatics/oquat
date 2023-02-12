# msio

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `msio`. See the [GitHub repository](https://github.com/MSI-Metabolomics-Standards-Initiative/MSIO).


## `Gmelin`: Gmelins Handbuch der anorganischen Chemie

Overall, there were 4 invalid
xrefs to external prefixed with `Gmelin` (standardized to Bioregistry
prefix [`gmelin`](https://bioregistry.io/gmelin)) that
did not match the standard pattern `^[1-9][0-9]{3,6}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `Gmelin:117`    |              1 | [CHEBI:15377](http://purl.obolibrary.org/obo/CHEBI_15377) |
| `Gmelin:79`     |              1 | [CHEBI:16134](http://purl.obolibrary.org/obo/CHEBI_16134) |
| `Gmelin:895`    |              1 | [CHEBI:38472](http://purl.obolibrary.org/obo/CHEBI_38472) |
| `Gmelin:97`     |              1 | [CHEBI:41981](http://purl.obolibrary.org/obo/CHEBI_41981) |

## `LIPID_MAPS_class`: LIPID MAPS ID

Overall, there were 1 invalid
xrefs to external prefixed with `LIPID_MAPS_class` (standardized to Bioregistry
prefix [`lipidmaps`](https://bioregistry.io/lipidmaps)) that
did not match the standard pattern `^LM(FA|GL|GP|SP|ST|PR|SL|PK)[0-9]{4}([0-9a-zA-Z]{4,6})?$`.

| external_xref             |   usages_count | usages                                                    |
|---------------------------|----------------|-----------------------------------------------------------|
| `LIPID_MAPS_class:LMPR01` |              1 | [CHEBI:24913](http://purl.obolibrary.org/obo/CHEBI_24913) |

## `Wikipedia`: Wikipedia

Overall, there were 1 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref           |   usages_count | usages                                                    |
|-------------------------|----------------|-----------------------------------------------------------|
| `Wikipedia:1,4-Dioxane` |              1 | [CHEBI:47032](http://purl.obolibrary.org/obo/CHEBI_47032) |

