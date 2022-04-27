# bs

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `bs`.


## `SO`: Sequence types and features ontology

Overall, there were 33 invalid
xrefs to external terms in `so` that did not match the standard
pattern `^\d{7}$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/so).

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                                                                       |
|----------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SO:cb`              |             19 | [SO:0001098](https://bioregistry.io/SO:0001098), [SO:0001098](https://bioregistry.io/SO:0001098), [SO:0001102](https://bioregistry.io/SO:0001102), [SO:0001150](https://bioregistry.io/SO:0001150), [SO:0001154](https://bioregistry.io/SO:0001154), ...                                     |
| `SO:ke`              |             12 | [SO:0000839](https://bioregistry.io/SO:0000839), [SO:0001146](https://bioregistry.io/SO:0001146), [SO:0100020](https://bioregistry.io/SO:0100020), [SO:0100020](https://bioregistry.io/SO:0100020), [so/subsets/biosapiens#gained](https://bioregistry.io/so/subsets/biosapiens#gained), ... |
| `SO:GAR`             |              1 | [SO:0000839](https://bioregistry.io/SO:0000839)                                                                                                                                                                                                                                              |
| `SO:immuno_workshop` |              1 | [so/subsets/biosapiens#variant:of](https://bioregistry.io/so/subsets/biosapiens#variant:of)                                                                                                                                                                                                  |

## `UniProt`: UniProt Protein

Overall, there were 21 invalid
xrefs to external terms in `uniprot` that did not match the standard
pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/uniprot).

| external_xref             |   usages_count | usages                                                                                                                                                                                                                                                   |
|---------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UniProt:curation_manual` |             19 | [SO:0001084](https://bioregistry.io/SO:0001084), [SO:0001086](https://bioregistry.io/SO:0001086), [SO:0001104](https://bioregistry.io/SO:0001104), [SO:0001112](https://bioregistry.io/SO:0001112), [SO:0001147](https://bioregistry.io/SO:0001147), ... |
| `UniProt:curator_manual`  |              1 | [SO:0001077](https://bioregistry.io/SO:0001077)                                                                                                                                                                                                          |
| `UniProt:Curation_manual` |              1 | [SO:0001093](https://bioregistry.io/SO:0001093)                                                                                                                                                                                                          |

## `uniprot`: UniProt Protein

Overall, there were 30 invalid
xrefs to external terms in `uniprot` that did not match the standard
pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/uniprot).

| external_xref          |   usages_count | usages                                                                                                                                                                                                                                                   |
|------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uniprot:feature_type` |             28 | [SO:0000417](https://bioregistry.io/SO:0000417), [SO:0000417](https://bioregistry.io/SO:0000417), [SO:0001064](https://bioregistry.io/SO:0001064), [SO:0001077](https://bioregistry.io/SO:0001077), [SO:0001128](https://bioregistry.io/SO:0001128), ... |
| `uniprot:curation`     |              1 | [SO:0001091](https://bioregistry.io/SO:0001091)                                                                                                                                                                                                          |
| `uniprot:feature`      |              1 | [SO:0100020](https://bioregistry.io/SO:0100020)                                                                                                                                                                                                          |

