# lpt

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `lpt`.


## `MGI`: Mouse Genome Informatics

Overall, there were 6 invalid
xrefs to external prefixed with `MGI` (standardized to Bioregistry
entry [`mgi`]((https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MGI:MP`        |              4 | [LPT:0010269](https://bioregistry.io/LPT:0010269), [LPT:0010271](https://bioregistry.io/LPT:0010271), [LPT:0010275](https://bioregistry.io/LPT:0010275), [LPT:0010277](https://bioregistry.io/LPT:0010277) |
| `MGI:smb`       |              2 | [LPT:0004047](https://bioregistry.io/LPT:0004047), [LPT:0010451](https://bioregistry.io/LPT:0010451)                                                                                                       |

## `VT`: Vertebrate trait ontology

Overall, there were 1 invalid
xrefs to external prefixed with `VT` (standardized to Bioregistry
entry [`vt`]((https://bioregistry.io/vt)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                            |
|-----------------|----------------|---------------------------------------------------|
| `VT::0010808`   |              1 | [LPT:0000185](https://bioregistry.io/LPT:0000185) |

## `VTO`: Vertebrate Taxonomy Ontology

Overall, there were 540 invalid
xrefs to external prefixed with `VTO` (standardized to Bioregistry
entry [`vto`]((https://bioregistry.io/vto)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `VTO:CP`        |            357 | [LPT:0000145](https://bioregistry.io/LPT:0000145), [LPT:0010261](https://bioregistry.io/LPT:0010261), [LPT:0010373](https://bioregistry.io/LPT:0010373), [LPT:1000259](https://bioregistry.io/LPT:1000259), [LPT:1000260](https://bioregistry.io/LPT:1000260), ... |
| `VTO:INRA`      |            183 | [LPT:0010261](https://bioregistry.io/LPT:0010261), [LPT:0010310](https://bioregistry.io/LPT:0010310), [LPT:0010312](https://bioregistry.io/LPT:0010312), [LPT:0010392](https://bioregistry.io/LPT:0010392), [LPT:0010437](https://bioregistry.io/LPT:0010437), ... |

