# vario

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vario`.


## `MI`: Molecular Interactions Controlled Vocabulary

- Normalized prefix: `mi`
- [https://bioregistry.io/mi](https://bioregistry.io/mi)
- Pattern:`^\d{4}$`

| identifier   |   appearances | examples                                        |
|--------------|---------------|-------------------------------------------------|
| `MI:0000704` |             1 | [VariO:0272](https://bioregistry.io/VariO:0272) |

## `SGD`: Saccharomyces Genome Database

- Normalized prefix: `sgd`
- [https://bioregistry.io/sgd](https://bioregistry.io/sgd)
- Pattern:`^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`

| identifier     |   appearances | examples                                                                                         |
|----------------|---------------|--------------------------------------------------------------------------------------------------|
| `SGD:curators` |             2 | [VariO:0290](https://bioregistry.io/VariO:0290), [VariO:0291](https://bioregistry.io/VariO:0291) |

## `SO`: Sequence types and features ontology

- Normalized prefix: `so`
- [https://bioregistry.io/so](https://bioregistry.io/so)
- Pattern:`^\d{7}$`

| identifier   |   appearances | examples                                        |
|--------------|---------------|-------------------------------------------------|
| `SO:ke`      |             1 | [VariO:0196](https://bioregistry.io/VariO:0196) |

## `UniProt`: UniProt Protein

- Normalized prefix: `uniprot`
- [https://bioregistry.io/uniprot](https://bioregistry.io/uniprot)
- Pattern:`^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`

| identifier                |   appearances | examples                                        |
|---------------------------|---------------|-------------------------------------------------|
| `UniProt:curation_manual` |             1 | [VariO:0281](https://bioregistry.io/VariO:0281) |

## `VariO`: Variation Ontology

- Normalized prefix: `vario`
- [https://bioregistry.io/vario](https://bioregistry.io/vario)
- Pattern:`^\d+$`

| identifier   |   appearances | examples                                                                                                                                                                                                                                                 |
|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `VariO:mv`   |           410 | [VariO:0005](https://bioregistry.io/VariO:0005), [VariO:0041](https://bioregistry.io/VariO:0041), [VariO:0074](https://bioregistry.io/VariO:0074), [VariO:0079](https://bioregistry.io/VariO:0079), [VariO:0420](https://bioregistry.io/VariO:0420), ... |

## `Vario`: Variation Ontology

- Normalized prefix: `vario`
- [https://bioregistry.io/vario](https://bioregistry.io/vario)
- Pattern:`^\d+$`

| identifier   |   appearances | examples                                        |
|--------------|---------------|-------------------------------------------------|
| `Vario:mv`   |             1 | [VariO:0017](https://bioregistry.io/VariO:0017) |

