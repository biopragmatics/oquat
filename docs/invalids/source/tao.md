# tao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `tao`.


## `CL`: Cell Ontology

Overall, there were 154 invalid
xrefs to external prefixed with `CL` (standardized to Bioregistry
entry [`cl`]((https://bioregistry.io/cl)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CL:curator`    |            153 | [TAO:0009017](https://bioregistry.io/TAO:0009017), [TAO:0009096](https://bioregistry.io/TAO:0009096), [TAO:0009124](https://bioregistry.io/TAO:0009124), [TAO:0009133](https://bioregistry.io/TAO:0009133), [TAO:0009204](https://bioregistry.io/TAO:0009204), ... |
| `CL:Curator`    |              1 | [TAO:0005242](https://bioregistry.io/TAO:0005242)                                                                                                                                                                                                                  |

## `ZFA`: Zebrafish anatomy and development ontology

Overall, there were 4 invalid
xrefs to external prefixed with `ZFA` (standardized to Bioregistry
entry [`zfa`]((https://bioregistry.io/zfa)) that
did not match the standard pattern `^\d{7}$`.

| external_xref           |   usages_count | usages                                                                                                                                                  |
|-------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFA:curator`           |              3 | [TAO:0002135](https://bioregistry.io/TAO:0002135), [TAO:0002136](https://bioregistry.io/TAO:0002136), [TAO:0002141](https://bioregistry.io/TAO:0002141) |
| `ZFA:ZDB-PUB-060323-12` |              1 | [TAO:0005245](https://bioregistry.io/TAO:0005245)                                                                                                       |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 811 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
entry [`zfin`]((https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref    |   usages_count | usages                                                                                                                                                                                                                                                             |
|------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:curator`   |            805 | [TAO:0000729](https://bioregistry.io/TAO:0000729), [TAO:0000875](https://bioregistry.io/TAO:0000875), [TAO:0000956](https://bioregistry.io/TAO:0000956), [TAO:0000974](https://bioregistry.io/TAO:0000974), [TAO:0001499](https://bioregistry.io/TAO:0001499), ... |
| `ZFIN:Curator`   |              4 | [TAO:0005153](https://bioregistry.io/TAO:0005153), [TAO:0005165](https://bioregistry.io/TAO:0005165), [TAO:0005166](https://bioregistry.io/TAO:0005166), [TAO:0005210](https://bioregistry.io/TAO:0005210)                                                         |
| `ZFIN:090511-18` |              1 | [TAO:0002145](https://bioregistry.io/TAO:0002145)                                                                                                                                                                                                                  |
| `ZFIN:CVS`       |              1 | [TAO:0005265](https://bioregistry.io/TAO:0005265)                                                                                                                                                                                                                  |

