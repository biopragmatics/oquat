# lpt

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `lpt`.


## `MGI`: Mouse Genome Informatics

Overall, there were 6 invalid
xrefs to external prefixed with `MGI` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                     |
|----------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MGI:('MGI', 'MP')`  |              4 | [LPT:0010269](http://purl.obolibrary.org/obo/LPT_0010269), [LPT:0010271](http://purl.obolibrary.org/obo/LPT_0010271), [LPT:0010275](http://purl.obolibrary.org/obo/LPT_0010275), [LPT:0010277](http://purl.obolibrary.org/obo/LPT_0010277) |
| `MGI:('MGI', 'smb')` |              2 | [LPT:0004047](http://purl.obolibrary.org/obo/LPT_0004047), [LPT:0010451](http://purl.obolibrary.org/obo/LPT_0010451)                                                                                                                       |

## `VT`: Vertebrate trait ontology

Overall, there were 1 invalid
xrefs to external prefixed with `VT` (standardized to Bioregistry
prefix [`vt`](https://bioregistry.io/vt)) that
did not match the standard pattern `^\d{7}$`.

| external_xref           |   usages_count | usages                                                    |
|-------------------------|----------------|-----------------------------------------------------------|
| `VT:('VT', ':0010808')` |              1 | [LPT:0000185](http://purl.obolibrary.org/obo/LPT_0000185) |

## `VTO`: Vertebrate Taxonomy Ontology

Overall, there were 540 invalid
xrefs to external prefixed with `VTO` (standardized to Bioregistry
prefix [`vto`](https://bioregistry.io/vto)) that
did not match the standard pattern `^\d{7}$`.

| external_xref         |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `VTO:('VTO', 'CP')`   |            357 | [LPT:0000001](http://purl.obolibrary.org/obo/LPT_0000001), [LPT:0000002](http://purl.obolibrary.org/obo/LPT_0000002), [LPT:0000003](http://purl.obolibrary.org/obo/LPT_0000003), [LPT:0000004](http://purl.obolibrary.org/obo/LPT_0000004), [LPT:0000005](http://purl.obolibrary.org/obo/LPT_0000005), ... |
| `VTO:('VTO', 'INRA')` |            183 | [LPT:0000038](http://purl.obolibrary.org/obo/LPT_0000038), [LPT:0010003](http://purl.obolibrary.org/obo/LPT_0010003), [LPT:0010007](http://purl.obolibrary.org/obo/LPT_0010007), [LPT:0010008](http://purl.obolibrary.org/obo/LPT_0010008), [LPT:0010009](http://purl.obolibrary.org/obo/LPT_0010009), ... |

