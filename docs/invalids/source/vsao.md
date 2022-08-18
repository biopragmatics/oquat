# vsao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vsao`.


## `CARO`: Common Anatomy Reference Ontology

Overall, there were 47 invalid
xrefs to external prefixed with `CARO` (standardized to Bioregistry
prefix [`caro`](https://bioregistry.io/caro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CARO:MAH`      |             44 | [CARO:0000000](http://purl.obolibrary.org/obo/CARO_0000000), [CARO:0000003](http://purl.obolibrary.org/obo/CARO_0000003), [CARO:0000004](http://purl.obolibrary.org/obo/CARO_0000004), [CARO:0000005](http://purl.obolibrary.org/obo/CARO_0000005), [CARO:0000006](http://purl.obolibrary.org/obo/CARO_0000006), ... |
| `CARO:mah`      |              3 | [CARO:0000062](http://purl.obolibrary.org/obo/CARO_0000062), [CARO:0000063](http://purl.obolibrary.org/obo/CARO_0000063), [CL:0000003](http://purl.obolibrary.org/obo/CL_0000003)                                                                                                                                    |

## `CL`: Cell Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `CL` (standardized to Bioregistry
prefix [`cl`](https://bioregistry.io/cl)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                           |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `CL:MAH`        |              2 | [CL:0007007](http://purl.obolibrary.org/obo/CL_0007007), [CL:0007008](http://purl.obolibrary.org/obo/CL_0007008) |

## `FB`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `FB` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `FB:ma`         |              1 | [CL:0000134](http://purl.obolibrary.org/obo/CL_0000134) |

## `GO`: Gene Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                         |   usages_count | usages                                                      |
|---------------------------------------|----------------|-------------------------------------------------------------|
| `GO:[GOC:mtg_sensu, ISBN:0198547684]` |              1 | [VSAO:0000021](http://purl.obolibrary.org/obo/VSAO_0000021) |
| `GO:curator`                          |              1 | [VSAO:0000092](http://purl.obolibrary.org/obo/VSAO_0000092) |

## `MESH`: Medical Subject Headings

Overall, there were 6 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref           |   usages_count | usages                                                  |
|-------------------------|----------------|---------------------------------------------------------|
| `MESH:A.11.436.107`     |              1 | [CL:0000059](http://purl.obolibrary.org/obo/CL_0000059) |
| `MESH:A.11.329.629`     |              1 | [CL:0000062](http://purl.obolibrary.org/obo/CL_0000062) |
| `MESH:A.11.329.629.500` |              1 | [CL:0000137](http://purl.obolibrary.org/obo/CL_0000137) |
| `MESH:A.11.329.171`     |              1 | [CL:0000138](http://purl.obolibrary.org/obo/CL_0000138) |
| `MESH:A.16.254.425.660` |              1 | [CL:0000222](http://purl.obolibrary.org/obo/CL_0000222) |
| `MESH:A.16.254.600`     |              1 | [CL:0000333](http://purl.obolibrary.org/obo/CL_0000333) |

## `PMID`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref    |   usages_count | usages                                                  |
|------------------|----------------|---------------------------------------------------------|
| `PMID:10102814j` |              1 | [CL:0000134](http://purl.obolibrary.org/obo/CL_0000134) |

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

## `Wikipedia`: Wikipedia

Overall, there were 1 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                          |   usages_count | usages                                                      |
|--------------------------------------------------------|----------------|-------------------------------------------------------------|
| `Wikipedia:http://en.wikipedia.org/wiki/Cartilaginous` |              1 | [PATO:0001449](http://purl.obolibrary.org/obo/PATO_0001449) |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 3 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:curator`  |              3 | [VSAO:0000001](http://purl.obolibrary.org/obo/VSAO_0000001), [VSAO:0000164](http://purl.obolibrary.org/obo/VSAO_0000164), [VSAO:0000178](http://purl.obolibrary.org/obo/VSAO_0000178) |

