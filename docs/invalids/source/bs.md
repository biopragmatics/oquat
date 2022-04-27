# bs

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `bs`.


## `SO`: Sequence types and features ontology

- Normalized prefix: `so`
- [https://bioregistry.io/so](https://bioregistry.io/so)
- Pattern:`^\d{7}$`

| identifier           |   appearances | examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SO:cb`              |            19 | [SO:0001070](https://bioregistry.io/SO:0001070), [SO:0001095](https://bioregistry.io/SO:0001095), [SO:0001098](https://bioregistry.io/SO:0001098), [SO:0001103](https://bioregistry.io/SO:0001103), [SO:0001103](https://bioregistry.io/SO:0001103), ...                                                                                                                                                                                                                                           |
| `SO:ke`              |            12 | [so/subsets/biosapiens#adjacent:to](https://bioregistry.io/so/subsets/biosapiens#adjacent:to), [so/subsets/biosapiens#evidence:for:feature](https://bioregistry.io/so/subsets/biosapiens#evidence:for:feature), [so/subsets/biosapiens#exemplar:of](https://bioregistry.io/so/subsets/biosapiens#exemplar:of), [so/subsets/biosapiens#exemplar:of](https://bioregistry.io/so/subsets/biosapiens#exemplar:of), [so/subsets/biosapiens#lost](https://bioregistry.io/so/subsets/biosapiens#lost), ... |
| `SO:GAR`             |             1 | [SO:0000839](https://bioregistry.io/SO:0000839)                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `SO:immuno_workshop` |             1 | [so/subsets/biosapiens#variant:of](https://bioregistry.io/so/subsets/biosapiens#variant:of)                                                                                                                                                                                                                                                                                                                                                                                                        |

## `UniProt`: UniProt Protein

- Normalized prefix: `uniprot`
- [https://bioregistry.io/uniprot](https://bioregistry.io/uniprot)
- Pattern:`^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`

| identifier                |   appearances | examples                                                                                                                                                                                                                                                 |
|---------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UniProt:curation_manual` |            19 | [SO:0001083](https://bioregistry.io/SO:0001083), [SO:0001087](https://bioregistry.io/SO:0001087), [SO:0001089](https://bioregistry.io/SO:0001089), [SO:0001113](https://bioregistry.io/SO:0001113), [SO:0001148](https://bioregistry.io/SO:0001148), ... |
| `UniProt:curator_manual`  |             1 | [SO:0001077](https://bioregistry.io/SO:0001077)                                                                                                                                                                                                          |
| `UniProt:Curation_manual` |             1 | [SO:0001093](https://bioregistry.io/SO:0001093)                                                                                                                                                                                                          |

## `uniprot`: UniProt Protein

- Normalized prefix: `uniprot`
- [https://bioregistry.io/uniprot](https://bioregistry.io/uniprot)
- Pattern:`^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`

| identifier             |   appearances | examples                                                                                                                                                                                                                                                 |
|------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uniprot:feature_type` |            28 | [SO:0000839](https://bioregistry.io/SO:0000839), [SO:0001064](https://bioregistry.io/SO:0001064), [SO:0001067](https://bioregistry.io/SO:0001067), [SO:0001072](https://bioregistry.io/SO:0001072), [SO:0001128](https://bioregistry.io/SO:0001128), ... |
| `uniprot:curation`     |             1 | [SO:0001091](https://bioregistry.io/SO:0001091)                                                                                                                                                                                                          |
| `uniprot:feature`      |             1 | [SO:0100020](https://bioregistry.io/SO:0100020)                                                                                                                                                                                                          |

