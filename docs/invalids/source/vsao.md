# vsao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vsao`.


## `GO`: Gene Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
entry [`go`]((https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                         |   usages_count | usages                                              |
|---------------------------------------|----------------|-----------------------------------------------------|
| `GO:[GOC:mtg_sensu, ISBN:0198547684]` |              1 | [VSAO:0000021](https://bioregistry.io/VSAO:0000021) |
| `GO:curator`                          |              1 | [VSAO:0000092](https://bioregistry.io/VSAO:0000092) |

## `UBERON`: Uber Anatomy Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `UBERON` (standardized to Bioregistry
entry [`uberon`]((https://bioregistry.io/uberon)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                       |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UBERON:cjm`    |              7 | [VSAO:0000076](https://bioregistry.io/VSAO:0000076), [VSAO:0000155](https://bioregistry.io/VSAO:0000155), [VSAO:0000156](https://bioregistry.io/VSAO:0000156), [VSAO:0000303](https://bioregistry.io/VSAO:0000303), [VSAO:0000304](https://bioregistry.io/VSAO:0000304), ... |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 3 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
entry [`zfin`]((https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                        |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:curator`  |              3 | [VSAO:0000001](https://bioregistry.io/VSAO:0000001), [VSAO:0000164](https://bioregistry.io/VSAO:0000164), [VSAO:0000178](https://bioregistry.io/VSAO:0000178) |

