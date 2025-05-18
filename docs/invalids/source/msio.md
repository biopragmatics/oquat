# msio

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `msio`. See the [GitHub repository](https://github.com/MSI-Metabolomics-Standards-Initiative/MSIO).


## `Gmelin`: Gmelins Handbuch der anorganischen Chemie

Overall, there were 2 invalid
xrefs to external prefixed with `Gmelin` (standardized to Bioregistry
prefix [`gmelin`](https://bioregistry.io/gmelin)) that
did not match the standard pattern `^[1-9][0-9]{2,6}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `Gmelin:79`     |              1 | [CHEBI:16134](http://purl.obolibrary.org/obo/CHEBI_16134) |
| `Gmelin:97`     |              1 | [CHEBI:41981](http://purl.obolibrary.org/obo/CHEBI_41981) |

## `LIPID_MAPS_class`: LIPID MAPS

Overall, there were 1 invalid
xrefs to external prefixed with `LIPID_MAPS_class` (standardized to Bioregistry
prefix [`lipidmaps`](https://bioregistry.io/lipidmaps)) that
did not match the standard pattern `^LM(FA|GL|GP|SP|ST|PR|SL|PK)[0-9]{4}([0-9a-zA-Z]{4,6})?$`.

| external_xref             |   usages_count | usages                                                    |
|---------------------------|----------------|-----------------------------------------------------------|
| `LIPID_MAPS_class:LMPR01` |              1 | [CHEBI:24913](http://purl.obolibrary.org/obo/CHEBI_24913) |

