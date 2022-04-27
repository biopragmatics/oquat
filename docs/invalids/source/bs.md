# bs

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `bs`.


## `SO`: Sequence types and features ontology

Overall, there were 33 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
entry [`so`]((https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SO:cb`              |             19 | [SO:0000419](https://bioregistry.io/SO:0000419), [SO:0000419](https://bioregistry.io/SO:0000419), [SO:0001098](https://bioregistry.io/SO:0001098), [SO:0001100](https://bioregistry.io/SO:0001100), [SO:0001103](https://bioregistry.io/SO:0001103), ...                                                                                                                                 |
| `SO:ke`              |             12 | [SO:0000839](https://bioregistry.io/SO:0000839), [SO:0100020](https://bioregistry.io/SO:0100020), [so/subsets/biosapiens#evidence:for:feature](https://bioregistry.io/so/subsets/biosapiens#evidence:for:feature), [so/subsets/biosapiens#lost](https://bioregistry.io/so/subsets/biosapiens#lost), [so/subsets/biosapiens#lost](https://bioregistry.io/so/subsets/biosapiens#lost), ... |
| `SO:GAR`             |              1 | [SO:0000839](https://bioregistry.io/SO:0000839)                                                                                                                                                                                                                                                                                                                                          |
| `SO:immuno_workshop` |              1 | [so/subsets/biosapiens#variant:of](https://bioregistry.io/so/subsets/biosapiens#variant:of)                                                                                                                                                                                                                                                                                              |

## `UniProt`: UniProt Protein

Overall, there were 21 invalid
xrefs to external prefixed with `UniProt` (standardized to Bioregistry
entry [`uniprot`]((https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref             |   usages_count | usages                                                                                                                                                                                                                                                   |
|---------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UniProt:curation_manual` |             19 | [SO:0001084](https://bioregistry.io/SO:0001084), [SO:0001084](https://bioregistry.io/SO:0001084), [SO:0001084](https://bioregistry.io/SO:0001084), [SO:0001088](https://bioregistry.io/SO:0001088), [SO:0001148](https://bioregistry.io/SO:0001148), ... |
| `UniProt:curator_manual`  |              1 | [SO:0001077](https://bioregistry.io/SO:0001077)                                                                                                                                                                                                          |
| `UniProt:Curation_manual` |              1 | [SO:0001093](https://bioregistry.io/SO:0001093)                                                                                                                                                                                                          |

## `uniprot`: UniProt Protein

Overall, there were 30 invalid
xrefs to external prefixed with `uniprot` (standardized to Bioregistry
entry [`uniprot`]((https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref          |   usages_count | usages                                                                                                                                                                                                                                                   |
|------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uniprot:feature_type` |             28 | [SO:0000417](https://bioregistry.io/SO:0000417), [SO:0000691](https://bioregistry.io/SO:0000691), [SO:0000725](https://bioregistry.io/SO:0000725), [SO:0001062](https://bioregistry.io/SO:0001062), [SO:0001128](https://bioregistry.io/SO:0001128), ... |
| `uniprot:curation`     |              1 | [SO:0001091](https://bioregistry.io/SO:0001091)                                                                                                                                                                                                          |
| `uniprot:feature`      |              1 | [SO:0100020](https://bioregistry.io/SO:0100020)                                                                                                                                                                                                          |

