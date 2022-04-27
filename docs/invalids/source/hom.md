# hom

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `hom`. See the [GitHub repository](https://github.com/BgeeDB/homology-ontology)


## `ECO`: Evidence ontology

- Normalized prefix: `eco`
- [https://bioregistry.io/eco](https://bioregistry.io/eco)
- Pattern:`^\d{7}$`

| identifier     |   appearances | examples                                          |
|----------------|---------------|---------------------------------------------------|
| `ECO:00000060` |             1 | [HOM:0000017](https://bioregistry.io/HOM:0000017) |

## `MeSH`: Medical Subject Headings

- Normalized prefix: `mesh`
- [https://bioregistry.io/mesh](https://bioregistry.io/mesh)
- Pattern:`^(C|D)\d{6,9}$`

| identifier                          |   appearances | examples                                                                                             |
|-------------------------------------|---------------|------------------------------------------------------------------------------------------------------|
| `MeSH:Synteny`                      |             2 | [HOM:0000010](https://bioregistry.io/HOM:0000010), [HOM:0000010](https://bioregistry.io/HOM:0000010) |
| `MeSH:Structural Homology, Protein` |             1 | [HOM:0000015](https://bioregistry.io/HOM:0000015)                                                    |
| `MeSH:Chromosome Pairing`           |             1 | [HOM:0000047](https://bioregistry.io/HOM:0000047)                                                    |

## `RO_proposed_relation`: Relation Ontology

- Normalized prefix: `ro`
- [https://bioregistry.io/ro](https://bioregistry.io/ro)
- Pattern:`^\d{7}$`

| identifier                           |   appearances | examples                                          |
|--------------------------------------|---------------|---------------------------------------------------|
| `RO_proposed_relation:homologous_to` |             1 | [HOM:0000007](https://bioregistry.io/HOM:0000007) |

## `SO`: Sequence types and features ontology

- Normalized prefix: `so`
- [https://bioregistry.io/so](https://bioregistry.io/so)
- Pattern:`^\d{7}$`

| identifier                     |   appearances | examples                                                                                             |
|--------------------------------|---------------|------------------------------------------------------------------------------------------------------|
| `SO:non_functional_homolog_of` |             2 | [HOM:0000016](https://bioregistry.io/HOM:0000016), [HOM:0000016](https://bioregistry.io/HOM:0000016) |
| `SO:similar_to`                |             1 | [HOM:0000000](https://bioregistry.io/HOM:0000000)                                                    |
| `SO:homologous_to`             |             1 | [HOM:0000007](https://bioregistry.io/HOM:0000007)                                                    |
| `SO:paralogous_to`             |             1 | [HOM:0000011](https://bioregistry.io/HOM:0000011)                                                    |
| `SO:orthologous_to`            |             1 | [HOM:0000017](https://bioregistry.io/HOM:0000017)                                                    |

