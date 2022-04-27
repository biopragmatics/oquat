# vario

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vario`.


## `MI`: Molecular Interactions Controlled Vocabulary

Overall, there were 1 invalid
xrefs to external prefixed with `MI` (standardized to Bioregistry
prefix [`mi`](https://bioregistry.io/mi)) that
did not match the standard pattern `^\d{4}$`.

| external_xref          |   usages_count | usages                                                  |
|------------------------|----------------|---------------------------------------------------------|
| `MI:('MI', '0000704')` |              1 | [VariO:0272](http://purl.obolibrary.org/obo/VariO_0272) |

## `SGD`: Saccharomyces Genome Database

Overall, there were 2 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
prefix [`sgd`](https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref             |   usages_count | usages                                                                                                           |
|---------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `SGD:('SGD', 'curators')` |              2 | [VariO:0290](http://purl.obolibrary.org/obo/VariO_0290), [VariO:0291](http://purl.obolibrary.org/obo/VariO_0291) |

## `SO`: Sequence types and features ontology

Overall, there were 1 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref     |   usages_count | usages                                                  |
|-------------------|----------------|---------------------------------------------------------|
| `SO:('SO', 'ke')` |              1 | [VariO:0196](http://purl.obolibrary.org/obo/VariO_0196) |

## `UniProt`: UniProt Protein

Overall, there were 1 invalid
xrefs to external prefixed with `UniProt` (standardized to Bioregistry
prefix [`uniprot`](https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref                            |   usages_count | usages                                                  |
|------------------------------------------|----------------|---------------------------------------------------------|
| `UniProt:('UniProt', 'curation_manual')` |              1 | [VariO:0281](http://purl.obolibrary.org/obo/VariO_0281) |

## `VariO`: Variation Ontology

Overall, there were 410 invalid
xrefs to external prefixed with `VariO` (standardized to Bioregistry
prefix [`vario`](https://bioregistry.io/vario)) that
did not match the standard pattern `^\d+$`.

| external_xref           |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `VariO:('VariO', 'mv')` |            410 | [VariO:0001](http://purl.obolibrary.org/obo/VariO_0001), [VariO:0002](http://purl.obolibrary.org/obo/VariO_0002), [VariO:0003](http://purl.obolibrary.org/obo/VariO_0003), [VariO:0004](http://purl.obolibrary.org/obo/VariO_0004), [VariO:0005](http://purl.obolibrary.org/obo/VariO_0005), ... |

## `Vario`: Variation Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `Vario` (standardized to Bioregistry
prefix [`vario`](https://bioregistry.io/vario)) that
did not match the standard pattern `^\d+$`.

| external_xref           |   usages_count | usages                                                  |
|-------------------------|----------------|---------------------------------------------------------|
| `Vario:('Vario', 'mv')` |              1 | [VariO:0017](http://purl.obolibrary.org/obo/VariO_0017) |

