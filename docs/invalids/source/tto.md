# tto

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `tto`. See the [GitHub repository](https://github.com/phenoscape/teleost-taxonomy-ontology).


## `NCBITaxon`: NCBI Taxonomy

Overall, there were 6 invalid
xrefs to external prefixed with `NCBITaxon` (standardized to Bioregistry
prefix [`ncbitaxon`](https://bioregistry.io/ncbitaxon)) that
did not match the standard pattern `^\d+$`.

| external_xref       |   usages_count | usages                                                    |
|---------------------|----------------|-----------------------------------------------------------|
| `NCBITaxon:class`   |              1 | [TTO:class](http://purl.obolibrary.org/obo/TTO_class)     |
| `NCBITaxon:family`  |              1 | [TTO:family](http://purl.obolibrary.org/obo/TTO_family)   |
| `NCBITaxon:genus`   |              1 | [TTO:genus](http://purl.obolibrary.org/obo/TTO_genus)     |
| `NCBITaxon:order`   |              1 | [TTO:order](http://purl.obolibrary.org/obo/TTO_order)     |
| `NCBITaxon:phylum`  |              1 | [TTO:phylum](http://purl.obolibrary.org/obo/TTO_phylum)   |
| `NCBITaxon:species` |              1 | [TTO:species](http://purl.obolibrary.org/obo/TTO_species) |

## `TTO`: Teleost taxonomy ontology

Overall, there were 43 invalid
xrefs to external prefixed with `TTO` (standardized to Bioregistry
prefix [`tto`](https://bioregistry.io/tto)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                         |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TTO:curator`   |             42 | [TTO:10000676](http://purl.obolibrary.org/obo/TTO_10000676), [TTO:10000677](http://purl.obolibrary.org/obo/TTO_10000677), [TTO:1001317](http://purl.obolibrary.org/obo/TTO_1001317), [TTO:1002747](http://purl.obolibrary.org/obo/TTO_1002747), [TTO:1003391](http://purl.obolibrary.org/obo/TTO_1003391), ... |
| `TTO:PEM`       |              1 | [TTO:1007547](http://purl.obolibrary.org/obo/TTO_1007547)                                                                                                                                                                                                                                                      |

