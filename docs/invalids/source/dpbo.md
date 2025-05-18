# dpbo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `dpbo`. See the [GitHub repository](https://github.com/nfdi4plants/nfdi4plants_ontology).


## `NCBITaxon`: NCBI Taxonomy

Overall, there were 1 invalid
xrefs to external prefixed with `NCBITaxon` (standardized to Bioregistry
prefix [`ncbitaxon`](https://bioregistry.io/ncbitaxon)) that
did not match the standard pattern `^\d+$`.

| external_xref       |   usages_count | usages                                                    |
|---------------------|----------------|-----------------------------------------------------------|
| `NCBITaxon:species` |              1 | [NCIT:C45293](http://purl.obolibrary.org/obo/NCIT_C45293) |

## `PRIDE`: Proteomics Identification Database Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `PRIDE` (standardized to Bioregistry
prefix [`pride`](https://bioregistry.io/pride)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                      |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PRIDE:PRIDE`   |              3 | [PRIDE:0000463](http://purl.obolibrary.org/obo/PRIDE_0000463), [PRIDE:0000513](http://purl.obolibrary.org/obo/PRIDE_0000513), [PRIDE:0000650](http://purl.obolibrary.org/obo/PRIDE_0000650) |

## `SO`: Sequence types and features ontology

Overall, there were 3 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                    |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SO:ke`         |              3 | [SO:0000323](http://purl.obolibrary.org/obo/SO_0000323), [SO:0000327](http://purl.obolibrary.org/obo/SO_0000327), [SO:0000568](http://purl.obolibrary.org/obo/SO_0000568) |

