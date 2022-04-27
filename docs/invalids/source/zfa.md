# zfa

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `zfa`. See the [GitHub repository](https://github.com/cerivs/zebrafish-anatomical-ontology)


## `CL`: Cell Ontology

- Normalized prefix: `cl`
- [https://bioregistry.io/cl](https://bioregistry.io/cl)
- Pattern:`^\d{7}$`

| identifier    |   appearances | examples                                                                                                                                                                                                                                                           |
|---------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CL:curator`  |           160 | [ZFA:0005329](https://bioregistry.io/ZFA:0005329), [ZFA:0009006](https://bioregistry.io/ZFA:0009006), [ZFA:0009084](https://bioregistry.io/ZFA:0009084), [ZFA:0009121](https://bioregistry.io/ZFA:0009121), [ZFA:0009227](https://bioregistry.io/ZFA:0009227), ... |
| `CL:CVS`      |             4 | [ZFA:0009375](https://bioregistry.io/ZFA:0009375), [ZFA:0009376](https://bioregistry.io/ZFA:0009376), [ZFA:0009393](https://bioregistry.io/ZFA:0009393), [ZFA:0009395](https://bioregistry.io/ZFA:0009395)                                                         |
| `CL:Curator`  |             2 | [ZFA:0005242](https://bioregistry.io/ZFA:0005242), [ZFA:0005873](https://bioregistry.io/ZFA:0005873)                                                                                                                                                               |
| `CL:editor`   |             2 | [ZFA:0005769](https://bioregistry.io/ZFA:0005769), [ZFA:0009402](https://bioregistry.io/ZFA:0009402)                                                                                                                                                               |
| `CL:tfm`      |             1 | [ZFA:0005743](https://bioregistry.io/ZFA:0005743)                                                                                                                                                                                                                  |
| `CL:MAH`      |             1 | [ZFA:0005775](https://bioregistry.io/ZFA:0005775)                                                                                                                                                                                                                  |
| `CL:dhill`    |             1 | [ZFA:0009301](https://bioregistry.io/ZFA:0009301)                                                                                                                                                                                                                  |
| `CL:00000365` |             1 | [ZFA:0005772](https://bioregistry.io/ZFA:0005772)                                                                                                                                                                                                                  |

## `FB`: FlyBase Gene

- Normalized prefix: `flybase`
- [https://bioregistry.io/flybase](https://bioregistry.io/flybase)
- Pattern:`^FB\w{2}\d{7}$`

| identifier   |   appearances | examples                                          |
|--------------|---------------|---------------------------------------------------|
| `FB:ma`      |             1 | [ZFA:0009387](https://bioregistry.io/ZFA:0009387) |

## `GO`: Gene Ontology

- Normalized prefix: `go`
- [https://bioregistry.io/go](https://bioregistry.io/go)
- Pattern:`^\d{7}$`

| identifier   |   appearances | examples                                          |
|--------------|---------------|---------------------------------------------------|
| `GO:CJM`     |             1 | [ZFA:0009307](https://bioregistry.io/ZFA:0009307) |

## `MESH`: Medical Subject Headings

- Normalized prefix: `mesh`
- [https://bioregistry.io/mesh](https://bioregistry.io/mesh)
- Pattern:`^(C|D)\d{6,9}$`

| identifier      |   appearances | examples                                          |
|-----------------|---------------|---------------------------------------------------|
| `MESH:68018069` |             1 | [ZFA:0000678](https://bioregistry.io/ZFA:0000678) |

## `ORCiD`: Open Researcher and Contributor

- Normalized prefix: `orcid`
- [https://bioregistry.io/orcid](https://bioregistry.io/orcid)
- Pattern:`^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$`

| identifier                   |   appearances | examples                                          |
|------------------------------|---------------|---------------------------------------------------|
| `ORCiD:000-0002-9900-7880`   |             1 | [ZFA:0000833](https://bioregistry.io/ZFA:0000833) |
| `ORCiD:CVS`                  |             1 | [ZFA:0001679](https://bioregistry.io/ZFA:0001679) |
| `ORCiD:0000-0002-2244-7917,` |             1 | [ZFA:0005867](https://bioregistry.io/ZFA:0005867) |

## `ORCID`: Open Researcher and Contributor

- Normalized prefix: `orcid`
- [https://bioregistry.io/orcid](https://bioregistry.io/orcid)
- Pattern:`^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$`

| identifier                 |   appearances | examples                                          |
|----------------------------|---------------|---------------------------------------------------|
| `ORCID:000-0002-2244-7917` |             1 | [ZFA:0005927](https://bioregistry.io/ZFA:0005927) |

## `UBERON`: Uber Anatomy Ontology

- Normalized prefix: `uberon`
- [https://bioregistry.io/uberon](https://bioregistry.io/uberon)
- Pattern:`^\d+$`

| identifier       |   appearances | examples                                                                                             |
|------------------|---------------|------------------------------------------------------------------------------------------------------|
| `UBERON:curator` |             2 | [ZFA:0000632](https://bioregistry.io/ZFA:0000632), [ZFA:0005658](https://bioregistry.io/ZFA:0005658) |

## `ZFIN`: Zebrafish Information Network Gene

- Normalized prefix: `zfin`
- [https://bioregistry.io/zfin](https://bioregistry.io/zfin)
- Pattern:`^ZDB\-\w+\-\d+\-\d+$`

| identifier                 |   appearances | examples                                                                                                                                                                                                                                                           |
|----------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:<new dbxref>`        |             6 | [ZFA:0000259](https://bioregistry.io/ZFA:0000259), [ZFA:0000259](https://bioregistry.io/ZFA:0000259), [ZFA:0000259](https://bioregistry.io/ZFA:0000259), [ZFA:0000259](https://bioregistry.io/ZFA:0000259), [ZFA:0000464](https://bioregistry.io/ZFA:0000464), ... |
| `ZFIN:JCN 421-:189-198`    |             1 | [ZFA:0000443](https://bioregistry.io/ZFA:0000443)                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-171118-8v`   |             1 | [ZFA:0000704](https://bioregistry.io/ZFA:0000704)                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-120419-3.`   |             1 | [ZFA:0005877](https://bioregistry.io/ZFA:0005877)                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-050623-3.`   |             1 | [ZFA:0001249](https://bioregistry.io/ZFA:0001249)                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-961014-192.` |             1 | [ZFA:0001595](https://bioregistry.io/ZFA:0001595)                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-050120-6.`   |             1 | [ZFA:0005737](https://bioregistry.io/ZFA:0005737)                                                                                                                                                                                                                  |

