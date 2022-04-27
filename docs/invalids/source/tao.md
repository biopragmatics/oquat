# tao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `tao`.


## `CL`: Cell Ontology

Overall, there were 154 invalid
xrefs to external prefixed with `CL` (standardized to Bioregistry
prefix [`cl`](https://bioregistry.io/cl)) that
did not match the standard pattern `^\d{7}$`.

| external_xref          |   usages_count | usages                                                                                                                                                                                                                                                             |
|------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CL:('CL', 'curator')` |            153 | [TAO:0002148](https://bioregistry.io/TAO:0002148), [TAO:0002182](https://bioregistry.io/TAO:0002182), [TAO:0002211](https://bioregistry.io/TAO:0002211), [TAO:0005243](https://bioregistry.io/TAO:0005243), [TAO:0005322](https://bioregistry.io/TAO:0005322), ... |
| `CL:('CL', 'Curator')` |              1 | [TAO:0005242](https://bioregistry.io/TAO:0005242)                                                                                                                                                                                                                  |

## `ZFA`: Zebrafish anatomy and development ontology

Overall, there were 4 invalid
xrefs to external prefixed with `ZFA` (standardized to Bioregistry
prefix [`zfa`](https://bioregistry.io/zfa)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                      |   usages_count | usages                                                                                                                                                  |
|------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFA:('ZFA', 'curator')`           |              3 | [TAO:0002135](https://bioregistry.io/TAO:0002135), [TAO:0002136](https://bioregistry.io/TAO:0002136), [TAO:0002141](https://bioregistry.io/TAO:0002141) |
| `ZFA:('ZFA', 'ZDB-PUB-060323-12')` |              1 | [TAO:0005245](https://bioregistry.io/TAO:0005245)                                                                                                       |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 811 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref                |   usages_count | usages                                                                                                                                                                                                                                                             |
|------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:('ZFIN', 'curator')`   |            805 | [TAO:0000000](https://bioregistry.io/TAO:0000000), [TAO:0000001](https://bioregistry.io/TAO:0000001), [TAO:0000006](https://bioregistry.io/TAO:0000006), [TAO:0000007](https://bioregistry.io/TAO:0000007), [TAO:0000008](https://bioregistry.io/TAO:0000008), ... |
| `ZFIN:('ZFIN', 'Curator')`   |              4 | [TAO:0005153](https://bioregistry.io/TAO:0005153), [TAO:0005165](https://bioregistry.io/TAO:0005165), [TAO:0005166](https://bioregistry.io/TAO:0005166), [TAO:0005210](https://bioregistry.io/TAO:0005210)                                                         |
| `ZFIN:('ZFIN', '090511-18')` |              1 | [TAO:0002145](https://bioregistry.io/TAO:0002145)                                                                                                                                                                                                                  |
| `ZFIN:('ZFIN', 'CVS')`       |              1 | [TAO:0005265](https://bioregistry.io/TAO:0005265)                                                                                                                                                                                                                  |

