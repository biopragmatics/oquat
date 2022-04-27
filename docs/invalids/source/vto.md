# vto

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vto`. See the [GitHub repository](https://github.com/phenoscape/vertebrate-taxonomy-ontology)


## `TTO`: Teleost taxonomy ontology

Overall, there were 43 invalid
xrefs to external prefixed with `TTO` (standardized to Bioregistry
entry [`tto`]((https://bioregistry.io/tto)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TTO:curator`   |             42 | [VTO:0034982](https://bioregistry.io/VTO:0034982), [VTO:0037000](https://bioregistry.io/VTO:0037000), [VTO:0059975](https://bioregistry.io/VTO:0059975), [VTO:0060915](https://bioregistry.io/VTO:0060915), [VTO:0061426](https://bioregistry.io/VTO:0061426), ... |
| `TTO:PEM`       |              1 | [VTO:0069215](https://bioregistry.io/VTO:0069215)                                                                                                                                                                                                                  |

