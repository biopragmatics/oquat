# zfa

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `zfa`. See the [GitHub repository](https://github.com/cerivs/zebrafish-anatomical-ontology)


## `CL`: Cell Ontology

Overall, there were 172 invalid
xrefs to external terms in `cl` that did not match the standard
pattern `^\d{7}$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/cl).

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CL:curator`    |            160 | [ZFA:0009043](https://bioregistry.io/ZFA:0009043), [ZFA:0009111](https://bioregistry.io/ZFA:0009111), [ZFA:0009311](https://bioregistry.io/ZFA:0009311), [ZFA:0009314](https://bioregistry.io/ZFA:0009314), [ZFA:0009324](https://bioregistry.io/ZFA:0009324), ... |
| `CL:CVS`        |              4 | [ZFA:0009375](https://bioregistry.io/ZFA:0009375), [ZFA:0009376](https://bioregistry.io/ZFA:0009376), [ZFA:0009393](https://bioregistry.io/ZFA:0009393), [ZFA:0009395](https://bioregistry.io/ZFA:0009395)                                                         |
| `CL:Curator`    |              2 | [ZFA:0005242](https://bioregistry.io/ZFA:0005242), [ZFA:0005873](https://bioregistry.io/ZFA:0005873)                                                                                                                                                               |
| `CL:editor`     |              2 | [ZFA:0005769](https://bioregistry.io/ZFA:0005769), [ZFA:0009402](https://bioregistry.io/ZFA:0009402)                                                                                                                                                               |
| `CL:tfm`        |              1 | [ZFA:0005743](https://bioregistry.io/ZFA:0005743)                                                                                                                                                                                                                  |
| `CL:MAH`        |              1 | [ZFA:0005775](https://bioregistry.io/ZFA:0005775)                                                                                                                                                                                                                  |
| `CL:dhill`      |              1 | [ZFA:0009301](https://bioregistry.io/ZFA:0009301)                                                                                                                                                                                                                  |
| `CL:00000365`   |              1 | [ZFA:0005772](https://bioregistry.io/ZFA:0005772)                                                                                                                                                                                                                  |

## `FB`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external terms in `flybase` that did not match the standard
pattern `^FB\w{2}\d{7}$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/flybase).

| external_xref   |   usages_count | usages                                            |
|-----------------|----------------|---------------------------------------------------|
| `FB:ma`         |              1 | [ZFA:0009387](https://bioregistry.io/ZFA:0009387) |

## `GO`: Gene Ontology

Overall, there were 1 invalid
xrefs to external terms in `go` that did not match the standard
pattern `^\d{7}$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/go).

| external_xref   |   usages_count | usages                                            |
|-----------------|----------------|---------------------------------------------------|
| `GO:CJM`        |              1 | [ZFA:0009307](https://bioregistry.io/ZFA:0009307) |

## `MESH`: Medical Subject Headings

Overall, there were 1 invalid
xrefs to external terms in `mesh` that did not match the standard
pattern `^(C|D)\d{6,9}$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/mesh).

| external_xref   |   usages_count | usages                                            |
|-----------------|----------------|---------------------------------------------------|
| `MESH:68018069` |              1 | [ZFA:0000678](https://bioregistry.io/ZFA:0000678) |

## `ORCiD`: Open Researcher and Contributor

Overall, there were 3 invalid
xrefs to external terms in `orcid` that did not match the standard
pattern `^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/orcid).

| external_xref                |   usages_count | usages                                            |
|------------------------------|----------------|---------------------------------------------------|
| `ORCiD:000-0002-9900-7880`   |              1 | [ZFA:0000833](https://bioregistry.io/ZFA:0000833) |
| `ORCiD:CVS`                  |              1 | [ZFA:0001679](https://bioregistry.io/ZFA:0001679) |
| `ORCiD:0000-0002-2244-7917,` |              1 | [ZFA:0005867](https://bioregistry.io/ZFA:0005867) |

## `ORCID`: Open Researcher and Contributor

Overall, there were 1 invalid
xrefs to external terms in `orcid` that did not match the standard
pattern `^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/orcid).

| external_xref              |   usages_count | usages                                            |
|----------------------------|----------------|---------------------------------------------------|
| `ORCID:000-0002-2244-7917` |              1 | [ZFA:0005927](https://bioregistry.io/ZFA:0005927) |

## `UBERON`: Uber Anatomy Ontology

Overall, there were 2 invalid
xrefs to external terms in `uberon` that did not match the standard
pattern `^\d+$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/uberon).

| external_xref    |   usages_count | usages                                                                                               |
|------------------|----------------|------------------------------------------------------------------------------------------------------|
| `UBERON:curator` |              2 | [ZFA:0000632](https://bioregistry.io/ZFA:0000632), [ZFA:0005658](https://bioregistry.io/ZFA:0005658) |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 12 invalid
xrefs to external terms in `zfin` that did not match the standard
pattern `^ZDB\-\w+\-\d+\-\d+$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/zfin).

| external_xref              |   usages_count | usages                                                                                                                                                                                                                                                             |
|----------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:<new dbxref>`        |              6 | [ZFA:0000259](https://bioregistry.io/ZFA:0000259), [ZFA:0000424](https://bioregistry.io/ZFA:0000424), [ZFA:0000424](https://bioregistry.io/ZFA:0000424), [ZFA:0000464](https://bioregistry.io/ZFA:0000464), [ZFA:0000524](https://bioregistry.io/ZFA:0000524), ... |
| `ZFIN:JCN 421-:189-198`    |              1 | [ZFA:0000443](https://bioregistry.io/ZFA:0000443)                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-171118-8v`   |              1 | [ZFA:0000704](https://bioregistry.io/ZFA:0000704)                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-120419-3.`   |              1 | [ZFA:0005877](https://bioregistry.io/ZFA:0005877)                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-050623-3.`   |              1 | [ZFA:0001249](https://bioregistry.io/ZFA:0001249)                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-961014-192.` |              1 | [ZFA:0001595](https://bioregistry.io/ZFA:0001595)                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-050120-6.`   |              1 | [ZFA:0005737](https://bioregistry.io/ZFA:0005737)                                                                                                                                                                                                                  |

