# sdgio

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `sdgio`.


## `MA`: Mouse adult gross anatomy

Overall, there were 2 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
prefix [`ma`](https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref     |   usages_count | usages                                                                                                                                                                                     |
|-------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MA:('MA', 'ma')` |              2 | [http://purl.obolibrary.org/obo/ENVO_00000070](http://purl.obolibrary.org/obo/ENVO_00000070), [http://purl.obolibrary.org/obo/ENVO_00010483](http://purl.obolibrary.org/obo/ENVO_00010483) |

## `RO`: Relation Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `RO` (standardized to Bioregistry
prefix [`ro`](https://bioregistry.io/ro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref      |   usages_count | usages                                                                                 |
|--------------------|----------------|----------------------------------------------------------------------------------------|
| `RO:('RO', 'cjm')` |              1 | [http://purl.obolibrary.org/obo/RO_0009501](http://purl.obolibrary.org/obo/RO_0009501) |

