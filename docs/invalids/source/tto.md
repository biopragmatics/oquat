# tto

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `tto`. See the [GitHub repository](https://github.com/phenoscape/teleost-taxonomy-ontology)


## `NCBITaxon`: NCBI organismal classification

Overall, there were 6 invalid
xrefs to external terms in `ncbitaxon` that did not match the standard
pattern `^\d+$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/ncbitaxon).

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
xrefs to external terms in `tto` that did not match the standard
pattern `^\d+$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/tto).

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TTO:curator`   |             42 | [TTO:1005528](https://bioregistry.io/TTO:1005528), [TTO:1005567](https://bioregistry.io/TTO:1005567), [TTO:1005871](https://bioregistry.io/TTO:1005871), [TTO:1005889](https://bioregistry.io/TTO:1005889), [TTO:1056844](https://bioregistry.io/TTO:1056844), ... |
| `TTO:PEM`       |              1 | [TTO:1007547](https://bioregistry.io/TTO:1007547)                                                                                                                                                                                                                  |

