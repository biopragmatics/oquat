# vsao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vsao`.


## `GO`: Gene Ontology

- Normalized prefix: `go`
- [https://bioregistry.io/go](https://bioregistry.io/go)
- Pattern:`^\d{7}$`

| identifier                            |   appearances | examples                                            |
|---------------------------------------|---------------|-----------------------------------------------------|
| `GO:[GOC:mtg_sensu, ISBN:0198547684]` |             1 | [VSAO:0000021](https://bioregistry.io/VSAO:0000021) |
| `GO:curator`                          |             1 | [VSAO:0000092](https://bioregistry.io/VSAO:0000092) |

## `UBERON`: Uber Anatomy Ontology

- Normalized prefix: `uberon`
- [https://bioregistry.io/uberon](https://bioregistry.io/uberon)
- Pattern:`^\d+$`

| identifier   |   appearances | examples                                                                                                                                                                                                                                                                     |
|--------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UBERON:cjm` |             7 | [VSAO:0000076](https://bioregistry.io/VSAO:0000076), [VSAO:0000076](https://bioregistry.io/VSAO:0000076), [VSAO:0000303](https://bioregistry.io/VSAO:0000303), [VSAO:0000304](https://bioregistry.io/VSAO:0000304), [VSAO:0000305](https://bioregistry.io/VSAO:0000305), ... |

## `ZFIN`: Zebrafish Information Network Gene

- Normalized prefix: `zfin`
- [https://bioregistry.io/zfin](https://bioregistry.io/zfin)
- Pattern:`^ZDB\-\w+\-\d+\-\d+$`

| identifier     |   appearances | examples                                                                                                                                                      |
|----------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:curator` |             3 | [VSAO:0000001](https://bioregistry.io/VSAO:0000001), [VSAO:0000164](https://bioregistry.io/VSAO:0000164), [VSAO:0000178](https://bioregistry.io/VSAO:0000178) |

