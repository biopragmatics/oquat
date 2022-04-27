# zfa

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `zfa`.


## `ZFIN`: Zebrafish Information Network Gene

- Normalized prefix: `zfin`
- Pattern:`^ZDB\-\w+\-\d+\-\d+$`


| identifier                                                                  |   appearances | examples                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ZFIN:<new dbxref>](https://bioregistry.io/ZFIN:<new dbxref>)               |             6 | [ZFA:0000259](https://bioregistry.io/ZFA:0000259), [ZFA:0000400](https://bioregistry.io/ZFA:0000400), [ZFA:0000400](https://bioregistry.io/ZFA:0000400), [ZFA:0000464](https://bioregistry.io/ZFA:0000464), [ZFA:0000464](https://bioregistry.io/ZFA:0000464), ... |
| [ZFIN:JCN 421-:189-198](https://bioregistry.io/ZFIN:JCN 421-:189-198)       |             1 | [ZFA:0000443](https://bioregistry.io/ZFA:0000443)                                                                                                                                                                                                                  |
| [ZFIN:ZDB-PUB-171118-8v](https://bioregistry.io/ZFIN:ZDB-PUB-171118-8v)     |             1 | [ZFA:0000704](https://bioregistry.io/ZFA:0000704)                                                                                                                                                                                                                  |
| [ZFIN:ZDB-PUB-120419-3.](https://bioregistry.io/ZFIN:ZDB-PUB-120419-3.)     |             1 | [ZFA:0005877](https://bioregistry.io/ZFA:0005877)                                                                                                                                                                                                                  |
| [ZFIN:ZDB-PUB-050623-3.](https://bioregistry.io/ZFIN:ZDB-PUB-050623-3.)     |             1 | [ZFA:0001249](https://bioregistry.io/ZFA:0001249)                                                                                                                                                                                                                  |
| [ZFIN:ZDB-PUB-961014-192.](https://bioregistry.io/ZFIN:ZDB-PUB-961014-192.) |             1 | [ZFA:0001595](https://bioregistry.io/ZFA:0001595)                                                                                                                                                                                                                  |
| [ZFIN:ZDB-PUB-050120-6.](https://bioregistry.io/ZFIN:ZDB-PUB-050120-6.)     |             1 | [ZFA:0005737](https://bioregistry.io/ZFA:0005737)                                                                                                                                                                                                                  |

## `UBERON`: Uber Anatomy Ontology

- Normalized prefix: `uberon`
- Pattern:`^\d+$`


| identifier                                              |   appearances | examples                                                                                             |
|---------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------|
| [UBERON:curator](https://bioregistry.io/UBERON:curator) |             2 | [ZFA:0000632](https://bioregistry.io/ZFA:0000632), [ZFA:0005658](https://bioregistry.io/ZFA:0005658) |

## `MESH`: Medical Subject Headings

- Normalized prefix: `mesh`
- Pattern:`^(C|D)\d{6,9}$`


| identifier                                            |   appearances | examples                                          |
|-------------------------------------------------------|---------------|---------------------------------------------------|
| [MESH:68018069](https://bioregistry.io/MESH:68018069) |             1 | [ZFA:0000678](https://bioregistry.io/ZFA:0000678) |

## `ORCiD`: Open Researcher and Contributor

- Normalized prefix: `orcid`
- Pattern:`^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$`


| identifier                                                                      |   appearances | examples                                          |
|---------------------------------------------------------------------------------|---------------|---------------------------------------------------|
| [ORCiD:000-0002-9900-7880](https://bioregistry.io/ORCiD:000-0002-9900-7880)     |             1 | [ZFA:0000833](https://bioregistry.io/ZFA:0000833) |
| [ORCiD:CVS](https://bioregistry.io/ORCiD:CVS)                                   |             1 | [ZFA:0001679](https://bioregistry.io/ZFA:0001679) |
| [ORCiD:0000-0002-2244-7917,](https://bioregistry.io/ORCiD:0000-0002-2244-7917,) |             1 | [ZFA:0005867](https://bioregistry.io/ZFA:0005867) |

## `CL`: Cell Ontology

- Normalized prefix: `cl`
- Pattern:`^\d{7}$`


| identifier                                        |   appearances | examples                                                                                                                                                                                                                                                           |
|---------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CL:curator](https://bioregistry.io/CL:curator)   |           160 | [ZFA:0005830](https://bioregistry.io/ZFA:0005830), [ZFA:0009005](https://bioregistry.io/ZFA:0009005), [ZFA:0009007](https://bioregistry.io/ZFA:0009007), [ZFA:0009094](https://bioregistry.io/ZFA:0009094), [ZFA:0009351](https://bioregistry.io/ZFA:0009351), ... |
| [CL:CVS](https://bioregistry.io/CL:CVS)           |             4 | [ZFA:0009375](https://bioregistry.io/ZFA:0009375), [ZFA:0009376](https://bioregistry.io/ZFA:0009376), [ZFA:0009393](https://bioregistry.io/ZFA:0009393), [ZFA:0009395](https://bioregistry.io/ZFA:0009395)                                                         |
| [CL:Curator](https://bioregistry.io/CL:Curator)   |             2 | [ZFA:0005242](https://bioregistry.io/ZFA:0005242), [ZFA:0005873](https://bioregistry.io/ZFA:0005873)                                                                                                                                                               |
| [CL:editor](https://bioregistry.io/CL:editor)     |             2 | [ZFA:0005769](https://bioregistry.io/ZFA:0005769), [ZFA:0009402](https://bioregistry.io/ZFA:0009402)                                                                                                                                                               |
| [CL:tfm](https://bioregistry.io/CL:tfm)           |             1 | [ZFA:0005743](https://bioregistry.io/ZFA:0005743)                                                                                                                                                                                                                  |
| [CL:MAH](https://bioregistry.io/CL:MAH)           |             1 | [ZFA:0005775](https://bioregistry.io/ZFA:0005775)                                                                                                                                                                                                                  |
| [CL:dhill](https://bioregistry.io/CL:dhill)       |             1 | [ZFA:0009301](https://bioregistry.io/ZFA:0009301)                                                                                                                                                                                                                  |
| [CL:00000365](https://bioregistry.io/CL:00000365) |             1 | [ZFA:0005772](https://bioregistry.io/ZFA:0005772)                                                                                                                                                                                                                  |

## `ORCID`: Open Researcher and Contributor

- Normalized prefix: `orcid`
- Pattern:`^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$`


| identifier                                                                  |   appearances | examples                                          |
|-----------------------------------------------------------------------------|---------------|---------------------------------------------------|
| [ORCID:000-0002-2244-7917](https://bioregistry.io/ORCID:000-0002-2244-7917) |             1 | [ZFA:0005927](https://bioregistry.io/ZFA:0005927) |

## `GO`: Gene Ontology

- Normalized prefix: `go`
- Pattern:`^\d{7}$`


| identifier                              |   appearances | examples                                          |
|-----------------------------------------|---------------|---------------------------------------------------|
| [GO:CJM](https://bioregistry.io/GO:CJM) |             1 | [ZFA:0009307](https://bioregistry.io/ZFA:0009307) |

## `FB`: FlyBase Gene

- Normalized prefix: `flybase`
- Pattern:`^FB\w{2}\d{7}$`


| identifier                            |   appearances | examples                                          |
|---------------------------------------|---------------|---------------------------------------------------|
| [FB:ma](https://bioregistry.io/FB:ma) |             1 | [ZFA:0009387](https://bioregistry.io/ZFA:0009387) |

