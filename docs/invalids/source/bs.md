# bs

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `bs`. See the [GitHub repository](https://github.com/The-Sequence-Ontology/SO-Ontologies).


## `SO`: Sequence types and features ontology

Overall, there were 33 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                                                                                                                         |
|----------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SO:cb`              |             19 | [SO:0000419](http://purl.obolibrary.org/obo/SO_0000419), [SO:0001070](http://purl.obolibrary.org/obo/SO_0001070), [SO:0001072](http://purl.obolibrary.org/obo/SO_0001072), [SO:0001073](http://purl.obolibrary.org/obo/SO_0001073), [SO:0001074](http://purl.obolibrary.org/obo/SO_0001074), ...                                               |
| `SO:ke`              |             12 | [SO:0000409](http://purl.obolibrary.org/obo/SO_0000409), [SO:0000839](http://purl.obolibrary.org/obo/SO_0000839), [SO:0001146](http://purl.obolibrary.org/obo/SO_0001146), [SO:0100020](http://purl.obolibrary.org/obo/SO_0100020), [so/subsets/biosapiens#adjacent:to](http://purl.obolibrary.org/obo/so/subsets/biosapiens#adjacent_to), ... |
| `SO:GAR`             |              1 | [SO:0000839](http://purl.obolibrary.org/obo/SO_0000839)                                                                                                                                                                                                                                                                                        |
| `SO:immuno_workshop` |              1 | [so/subsets/biosapiens#variant:of](http://purl.obolibrary.org/obo/so/subsets/biosapiens#variant_of)                                                                                                                                                                                                                                            |

## `UniProt`: UniProt Protein

Overall, there were 21 invalid
xrefs to external prefixed with `UniProt` (standardized to Bioregistry
prefix [`uniprot`](https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref             |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|---------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UniProt:curation_manual` |             19 | [SO:0001064](http://purl.obolibrary.org/obo/SO_0001064), [SO:0001066](http://purl.obolibrary.org/obo/SO_0001066), [SO:0001067](http://purl.obolibrary.org/obo/SO_0001067), [SO:0001080](http://purl.obolibrary.org/obo/SO_0001080), [SO:0001083](http://purl.obolibrary.org/obo/SO_0001083), ... |
| `UniProt:curator_manual`  |              1 | [SO:0001077](http://purl.obolibrary.org/obo/SO_0001077)                                                                                                                                                                                                                                          |
| `UniProt:Curation_manual` |              1 | [SO:0001093](http://purl.obolibrary.org/obo/SO_0001093)                                                                                                                                                                                                                                          |

## `uniprot`: UniProt Protein

Overall, there were 30 invalid
xrefs to external prefixed with `uniprot` (standardized to Bioregistry
prefix [`uniprot`](https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref          |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uniprot:feature_type` |             28 | [SO:0000417](http://purl.obolibrary.org/obo/SO_0000417), [SO:0000418](http://purl.obolibrary.org/obo/SO_0000418), [SO:0000419](http://purl.obolibrary.org/obo/SO_0000419), [SO:0000691](http://purl.obolibrary.org/obo/SO_0000691), [SO:0000725](http://purl.obolibrary.org/obo/SO_0000725), ... |
| `uniprot:curation`     |              1 | [SO:0001091](http://purl.obolibrary.org/obo/SO_0001091)                                                                                                                                                                                                                                          |
| `uniprot:feature`      |              1 | [SO:0100020](http://purl.obolibrary.org/obo/SO_0100020)                                                                                                                                                                                                                                          |

