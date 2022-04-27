# tto

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `tto`. See the [GitHub repository](https://github.com/phenoscape/teleost-taxonomy-ontology)


## `NCBITaxon`: NCBI organismal classification

Overall, there were 6 invalid
xrefs to external prefixed with `NCBITaxon` (standardized to Bioregistry
entry [`ncbitaxon`]((https://bioregistry.io/ncbitaxon)) that
did not match the standard pattern `^\d+$`.

| external_xref       |   usages_count | usages                                            |
|---------------------|----------------|---------------------------------------------------|
| `NCBITaxon:class`   |              1 | [TTO:class](https://bioregistry.io/TTO:class)     |
| `NCBITaxon:family`  |              1 | [TTO:family](https://bioregistry.io/TTO:family)   |
| `NCBITaxon:genus`   |              1 | [TTO:genus](https://bioregistry.io/TTO:genus)     |
| `NCBITaxon:order`   |              1 | [TTO:order](https://bioregistry.io/TTO:order)     |
| `NCBITaxon:phylum`  |              1 | [TTO:phylum](https://bioregistry.io/TTO:phylum)   |
| `NCBITaxon:species` |              1 | [TTO:species](https://bioregistry.io/TTO:species) |

## `TTO`: Teleost taxonomy ontology

Overall, there were 43 invalid
xrefs to external prefixed with `TTO` (standardized to Bioregistry
entry [`tto`]((https://bioregistry.io/tto)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TTO:curator`   |             42 | [TTO:1005387](https://bioregistry.io/TTO:1005387), [TTO:1005871](https://bioregistry.io/TTO:1005871), [TTO:1048281](https://bioregistry.io/TTO:1048281), [TTO:1053567](https://bioregistry.io/TTO:1053567), [TTO:1054251](https://bioregistry.io/TTO:1054251), ... |
| `TTO:PEM`       |              1 | [TTO:1007547](https://bioregistry.io/TTO:1007547)                                                                                                                                                                                                                  |

