# vsao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vsao`.


## `GO`: Gene Ontology

Overall, there were 2 invalid
xrefs to external terms in `go` that did not match the standard
pattern `^\d{7}$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/go).

| external_xref                         |   usages_count | usages                                              |
|---------------------------------------|----------------|-----------------------------------------------------|
| `GO:[GOC:mtg_sensu, ISBN:0198547684]` |              1 | [VSAO:0000021](https://bioregistry.io/VSAO:0000021) |
| `GO:curator`                          |              1 | [VSAO:0000092](https://bioregistry.io/VSAO:0000092) |

## `UBERON`: Uber Anatomy Ontology

Overall, there were 7 invalid
xrefs to external terms in `uberon` that did not match the standard
pattern `^\d+$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/uberon).

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                       |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UBERON:cjm`    |              7 | [VSAO:0000076](https://bioregistry.io/VSAO:0000076), [VSAO:0000076](https://bioregistry.io/VSAO:0000076), [VSAO:0000155](https://bioregistry.io/VSAO:0000155), [VSAO:0000303](https://bioregistry.io/VSAO:0000303), [VSAO:0000305](https://bioregistry.io/VSAO:0000305), ... |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 3 invalid
xrefs to external terms in `zfin` that did not match the standard
pattern `^ZDB\-\w+\-\d+\-\d+$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/zfin).

| external_xref   |   usages_count | usages                                                                                                                                                        |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:curator`  |              3 | [VSAO:0000001](https://bioregistry.io/VSAO:0000001), [VSAO:0000164](https://bioregistry.io/VSAO:0000164), [VSAO:0000178](https://bioregistry.io/VSAO:0000178) |

