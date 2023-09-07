# sdgio

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `sdgio`. See the [GitHub repository](https://github.com/SDG-InterfaceOntology/sdgio).


## `MA`: Mouse adult gross anatomy

Overall, there were 2 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
prefix [`ma`](https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                       |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------|
| `MA:ma`         |              2 | [ENVO:00000070](http://purl.obolibrary.org/obo/ENVO_00000070), [ENVO:00010483](http://purl.obolibrary.org/obo/ENVO_00010483) |

## `RO`: Relation Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `RO` (standardized to Bioregistry
prefix [`ro`](https://bioregistry.io/ro)) that
did not match the standard pattern `^(HOM)?\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `RO:cjm`        |              1 | [RO:0009501](http://purl.obolibrary.org/obo/RO_0009501) |

