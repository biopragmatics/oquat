# tto

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `tto`. See the [GitHub repository](https://github.com/phenoscape/teleost-taxonomy-ontology).


## `NCBITaxon`: NCBI organismal classification

Overall, there were 6 invalid
xrefs to external prefixed with `NCBITaxon` (standardized to Bioregistry
prefix [`ncbitaxon`](https://bioregistry.io/ncbitaxon)) that
did not match the standard pattern `^\d+$`.

| external_xref                        |   usages_count | usages                                                                                   |
|--------------------------------------|----------------|------------------------------------------------------------------------------------------|
| `NCBITaxon:('NCBITaxon', 'class')`   |              1 | [http://purl.obolibrary.org/obo/TTO_class](http://purl.obolibrary.org/obo/TTO_class)     |
| `NCBITaxon:('NCBITaxon', 'family')`  |              1 | [http://purl.obolibrary.org/obo/TTO_family](http://purl.obolibrary.org/obo/TTO_family)   |
| `NCBITaxon:('NCBITaxon', 'genus')`   |              1 | [http://purl.obolibrary.org/obo/TTO_genus](http://purl.obolibrary.org/obo/TTO_genus)     |
| `NCBITaxon:('NCBITaxon', 'order')`   |              1 | [http://purl.obolibrary.org/obo/TTO_order](http://purl.obolibrary.org/obo/TTO_order)     |
| `NCBITaxon:('NCBITaxon', 'phylum')`  |              1 | [http://purl.obolibrary.org/obo/TTO_phylum](http://purl.obolibrary.org/obo/TTO_phylum)   |
| `NCBITaxon:('NCBITaxon', 'species')` |              1 | [http://purl.obolibrary.org/obo/TTO_species](http://purl.obolibrary.org/obo/TTO_species) |

## `TTO`: Teleost taxonomy ontology

Overall, there were 43 invalid
xrefs to external prefixed with `TTO` (standardized to Bioregistry
prefix [`tto`](https://bioregistry.io/tto)) that
did not match the standard pattern `^\d+$`.

| external_xref            |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TTO:('TTO', 'curator')` |             42 | [http://purl.obolibrary.org/obo/TTO_10000676](http://purl.obolibrary.org/obo/TTO_10000676), [http://purl.obolibrary.org/obo/TTO_10000677](http://purl.obolibrary.org/obo/TTO_10000677), [http://purl.obolibrary.org/obo/TTO_1001317](http://purl.obolibrary.org/obo/TTO_1001317), [http://purl.obolibrary.org/obo/TTO_1002747](http://purl.obolibrary.org/obo/TTO_1002747), [http://purl.obolibrary.org/obo/TTO_1003391](http://purl.obolibrary.org/obo/TTO_1003391), ... |
| `TTO:('TTO', 'PEM')`     |              1 | [http://purl.obolibrary.org/obo/TTO_1007547](http://purl.obolibrary.org/obo/TTO_1007547)                                                                                                                                                                                                                                                                                                                                                                                  |

