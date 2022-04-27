# ro

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `ro`.


## `MeSH`: Medical Subject Headings

- Normalized prefix: `mesh`
- Pattern:`^(C|D)\d{6,9}$`


| identifier                                                                                    |   appearances | examples                                                                                                     |
|-----------------------------------------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------|
| [MeSH:Synteny](https://bioregistry.io/MeSH:Synteny)                                           |             2 | [RO:HOM0000010](https://bioregistry.io/RO:HOM0000010), [RO:HOM0000010](https://bioregistry.io/RO:HOM0000010) |
| [MeSH:Structural_Homology,_Protein](https://bioregistry.io/MeSH:Structural_Homology,_Protein) |             1 | [RO:HOM0000015](https://bioregistry.io/RO:HOM0000015)                                                        |
| [MeSH:Chromosome_Pairing](https://bioregistry.io/MeSH:Chromosome_Pairing)                     |             1 | [RO:HOM0000047](https://bioregistry.io/RO:HOM0000047)                                                        |

## `SO`: Sequence types and features ontology

- Normalized prefix: `so`
- Pattern:`^\d{7}$`


| identifier                                                                          |   appearances | examples                                                                                                     |
|-------------------------------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------|
| [SO:non_functional_homolog_of](https://bioregistry.io/SO:non_functional_homolog_of) |             2 | [RO:HOM0000016](https://bioregistry.io/RO:HOM0000016), [RO:HOM0000016](https://bioregistry.io/RO:HOM0000016) |
| [SO:similar_to](https://bioregistry.io/SO:similar_to)                               |             1 | [RO:HOM0000000](https://bioregistry.io/RO:HOM0000000)                                                        |
| [SO:homologous_to](https://bioregistry.io/SO:homologous_to)                         |             1 | [RO:HOM0000007](https://bioregistry.io/RO:HOM0000007)                                                        |
| [SO:paralogous_to](https://bioregistry.io/SO:paralogous_to)                         |             1 | [RO:HOM0000011](https://bioregistry.io/RO:HOM0000011)                                                        |
| [SO:orthologous_to](https://bioregistry.io/SO:orthologous_to)                       |             1 | [RO:HOM0000017](https://bioregistry.io/RO:HOM0000017)                                                        |

## `RO`: Relation Ontology

- Normalized prefix: `ro`
- Pattern:`^\d{7}$`


| identifier                              |   appearances | examples                                        |
|-----------------------------------------|---------------|-------------------------------------------------|
| [RO:cjm](https://bioregistry.io/RO:cjm) |             1 | [RO:0009501](https://bioregistry.io/RO:0009501) |

## `RO_proposed_relation`: Relation Ontology

- Normalized prefix: `ro`
- Pattern:`^\d{7}$`


| identifier                                                                                      |   appearances | examples                                              |
|-------------------------------------------------------------------------------------------------|---------------|-------------------------------------------------------|
| [RO_proposed_relation:homologous_to](https://bioregistry.io/RO_proposed_relation:homologous_to) |             1 | [RO:HOM0000007](https://bioregistry.io/RO:HOM0000007) |

## `ECO`: Evidence ontology

- Normalized prefix: `eco`
- Pattern:`^\d{7}$`


| identifier                                          |   appearances | examples                                              |
|-----------------------------------------------------|---------------|-------------------------------------------------------|
| [ECO:00000060](https://bioregistry.io/ECO:00000060) |             1 | [RO:HOM0000017](https://bioregistry.io/RO:HOM0000017) |

