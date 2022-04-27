# ro

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `ro`. See the [GitHub repository](https://github.com/oborel/obo-relations)


## `ECO`: Evidence ontology

- Normalized prefix: `eco`
- [https://bioregistry.io/eco](https://bioregistry.io/eco)
- Pattern:`^\d{7}$`

| identifier     |   appearances | examples                                              |
|----------------|---------------|-------------------------------------------------------|
| `ECO:00000060` |             1 | [RO:HOM0000017](https://bioregistry.io/RO:HOM0000017) |

## `MeSH`: Medical Subject Headings

- Normalized prefix: `mesh`
- [https://bioregistry.io/mesh](https://bioregistry.io/mesh)
- Pattern:`^(C|D)\d{6,9}$`

| identifier                          |   appearances | examples                                                                                                     |
|-------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------|
| `MeSH:Synteny`                      |             2 | [RO:HOM0000010](https://bioregistry.io/RO:HOM0000010), [RO:HOM0000010](https://bioregistry.io/RO:HOM0000010) |
| `MeSH:Structural_Homology,_Protein` |             1 | [RO:HOM0000015](https://bioregistry.io/RO:HOM0000015)                                                        |
| `MeSH:Chromosome_Pairing`           |             1 | [RO:HOM0000047](https://bioregistry.io/RO:HOM0000047)                                                        |

## `RO`: Relation Ontology

- Normalized prefix: `ro`
- [https://bioregistry.io/ro](https://bioregistry.io/ro)
- Pattern:`^\d{7}$`

| identifier   |   appearances | examples                                        |
|--------------|---------------|-------------------------------------------------|
| `RO:cjm`     |             1 | [RO:0009501](https://bioregistry.io/RO:0009501) |

## `RO_proposed_relation`: Relation Ontology

- Normalized prefix: `ro`
- [https://bioregistry.io/ro](https://bioregistry.io/ro)
- Pattern:`^\d{7}$`

| identifier                           |   appearances | examples                                              |
|--------------------------------------|---------------|-------------------------------------------------------|
| `RO_proposed_relation:homologous_to` |             1 | [RO:HOM0000007](https://bioregistry.io/RO:HOM0000007) |

## `SO`: Sequence types and features ontology

- Normalized prefix: `so`
- [https://bioregistry.io/so](https://bioregistry.io/so)
- Pattern:`^\d{7}$`

| identifier                     |   appearances | examples                                                                                                     |
|--------------------------------|---------------|--------------------------------------------------------------------------------------------------------------|
| `SO:non_functional_homolog_of` |             2 | [RO:HOM0000016](https://bioregistry.io/RO:HOM0000016), [RO:HOM0000016](https://bioregistry.io/RO:HOM0000016) |
| `SO:similar_to`                |             1 | [RO:HOM0000000](https://bioregistry.io/RO:HOM0000000)                                                        |
| `SO:homologous_to`             |             1 | [RO:HOM0000007](https://bioregistry.io/RO:HOM0000007)                                                        |
| `SO:paralogous_to`             |             1 | [RO:HOM0000011](https://bioregistry.io/RO:HOM0000011)                                                        |
| `SO:orthologous_to`            |             1 | [RO:HOM0000017](https://bioregistry.io/RO:HOM0000017)                                                        |

