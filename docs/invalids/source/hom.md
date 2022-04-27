# hom

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `hom`. See the [GitHub repository](https://github.com/BgeeDB/homology-ontology).


## `ECO`: Evidence ontology

Overall, there were 1 invalid
xrefs to external prefixed with `ECO` (standardized to Bioregistry
prefix [`eco`](https://bioregistry.io/eco)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                            |
|-----------------|----------------|---------------------------------------------------|
| `ECO:00000060`  |              1 | [HOM:0000017](https://bioregistry.io/HOM:0000017) |

## `MeSH`: Medical Subject Headings

Overall, there were 4 invalid
xrefs to external prefixed with `MeSH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                       |   usages_count | usages                                                                                               |
|-------------------------------------|----------------|------------------------------------------------------------------------------------------------------|
| `MeSH:Synteny`                      |              2 | [HOM:0000010](https://bioregistry.io/HOM:0000010), [HOM:0000010](https://bioregistry.io/HOM:0000010) |
| `MeSH:Structural Homology, Protein` |              1 | [HOM:0000015](https://bioregistry.io/HOM:0000015)                                                    |
| `MeSH:Chromosome Pairing`           |              1 | [HOM:0000047](https://bioregistry.io/HOM:0000047)                                                    |

## `RO_proposed_relation`: Relation Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `RO_proposed_relation` (standardized to Bioregistry
prefix [`ro`](https://bioregistry.io/ro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                        |   usages_count | usages                                            |
|--------------------------------------|----------------|---------------------------------------------------|
| `RO_proposed_relation:homologous_to` |              1 | [HOM:0000007](https://bioregistry.io/HOM:0000007) |

## `SO`: Sequence types and features ontology

Overall, there were 6 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                  |   usages_count | usages                                                                                               |
|--------------------------------|----------------|------------------------------------------------------------------------------------------------------|
| `SO:non_functional_homolog_of` |              2 | [HOM:0000016](https://bioregistry.io/HOM:0000016), [HOM:0000016](https://bioregistry.io/HOM:0000016) |
| `SO:similar_to`                |              1 | [HOM:0000000](https://bioregistry.io/HOM:0000000)                                                    |
| `SO:homologous_to`             |              1 | [HOM:0000007](https://bioregistry.io/HOM:0000007)                                                    |
| `SO:paralogous_to`             |              1 | [HOM:0000011](https://bioregistry.io/HOM:0000011)                                                    |
| `SO:orthologous_to`            |              1 | [HOM:0000017](https://bioregistry.io/HOM:0000017)                                                    |

