# vto

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vto`. See the [GitHub repository](https://github.com/phenoscape/vertebrate-taxonomy-ontology).


## `TTO`: Teleost taxonomy ontology

Overall, there were 43 invalid
xrefs to external prefixed with `TTO` (standardized to Bioregistry
prefix [`tto`](https://bioregistry.io/tto)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TTO:curator`   |             42 | [VTO:0034982](http://purl.obolibrary.org/obo/VTO_0034982), [VTO:0035024](http://purl.obolibrary.org/obo/VTO_0035024), [VTO:0035052](http://purl.obolibrary.org/obo/VTO_0035052), [VTO:0035054](http://purl.obolibrary.org/obo/VTO_0035054), [VTO:0035058](http://purl.obolibrary.org/obo/VTO_0035058), ... |
| `TTO:PEM`       |              1 | [VTO:0069215](http://purl.obolibrary.org/obo/VTO_0069215)                                                                                                                                                                                                                                                  |

