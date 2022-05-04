# ddanat

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `ddanat`. See the [GitHub repository](https://github.com/dictyBase/migration-data).


## `CARO`: Common Anatomy Reference Ontology

Overall, there were 5 invalid
xrefs to external prefixed with `CARO` (standardized to Bioregistry
prefix [`caro`](https://bioregistry.io/caro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                              |
|-----------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CARO:MAH`      |              5 | [DDANAT:0000083](http://purl.obolibrary.org/obo/DDANAT_0000083), [DDANAT:0000401](http://purl.obolibrary.org/obo/DDANAT_0000401), [DDANAT:0010001](http://purl.obolibrary.org/obo/DDANAT_0010001), [DDANAT:0010081](http://purl.obolibrary.org/obo/DDANAT_0010081), [DDANAT:0010082](http://purl.obolibrary.org/obo/DDANAT_0010082) |

