# vsao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vsao`.


## `GO`: Gene Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                         |   usages_count | usages                                                      |
|---------------------------------------|----------------|-------------------------------------------------------------|
| `GO:[GOC:mtg_sensu, ISBN:0198547684]` |              1 | [VSAO:0000021](http://purl.obolibrary.org/obo/VSAO_0000021) |
| `GO:curator`                          |              1 | [VSAO:0000092](http://purl.obolibrary.org/obo/VSAO_0000092) |

## `TAO`: Teleost Anatomy Ontology

Overall, there were 27 invalid
xrefs to external prefixed with `TAO` (standardized to Bioregistry
prefix [`tao`](https://bioregistry.io/tao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TAO:curator`   |             26 | [VSAO:0000004](http://purl.obolibrary.org/obo/VSAO_0000004), [VSAO:0000007](http://purl.obolibrary.org/obo/VSAO_0000007), [VSAO:0000014](http://purl.obolibrary.org/obo/VSAO_0000014), [VSAO:0000024](http://purl.obolibrary.org/obo/VSAO_0000024), [VSAO:0000078](http://purl.obolibrary.org/obo/VSAO_0000078), ... |
| `TAO:GA_TG`     |              1 | [VSAO:0000154](http://purl.obolibrary.org/obo/VSAO_0000154)                                                                                                                                                                                                                                                          |

## `UBERON`: Uber Anatomy Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `UBERON` (standardized to Bioregistry
prefix [`uberon`](https://bioregistry.io/uberon)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UBERON:cjm`    |              7 | [VSAO:0000076](http://purl.obolibrary.org/obo/VSAO_0000076), [VSAO:0000155](http://purl.obolibrary.org/obo/VSAO_0000155), [VSAO:0000156](http://purl.obolibrary.org/obo/VSAO_0000156), [VSAO:0000303](http://purl.obolibrary.org/obo/VSAO_0000303), [VSAO:0000304](http://purl.obolibrary.org/obo/VSAO_0000304), ... |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 3 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:curator`  |              3 | [VSAO:0000001](http://purl.obolibrary.org/obo/VSAO_0000001), [VSAO:0000164](http://purl.obolibrary.org/obo/VSAO_0000164), [VSAO:0000178](http://purl.obolibrary.org/obo/VSAO_0000178) |

