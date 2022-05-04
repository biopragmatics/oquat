# zfa

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `zfa`. See the [GitHub repository](https://github.com/cerivs/zebrafish-anatomical-ontology).


## `CL`: Cell Ontology

Overall, there were 172 invalid
xrefs to external prefixed with `CL` (standardized to Bioregistry
prefix [`cl`](https://bioregistry.io/cl)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CL:curator`    |            160 | [ZFA:0001691](http://purl.obolibrary.org/obo/ZFA_0001691), [ZFA:0001694](http://purl.obolibrary.org/obo/ZFA_0001694), [ZFA:0001725](http://purl.obolibrary.org/obo/ZFA_0001725), [ZFA:0005243](http://purl.obolibrary.org/obo/ZFA_0005243), [ZFA:0005244](http://purl.obolibrary.org/obo/ZFA_0005244), ... |
| `CL:CVS`        |              4 | [ZFA:0009375](http://purl.obolibrary.org/obo/ZFA_0009375), [ZFA:0009376](http://purl.obolibrary.org/obo/ZFA_0009376), [ZFA:0009393](http://purl.obolibrary.org/obo/ZFA_0009393), [ZFA:0009395](http://purl.obolibrary.org/obo/ZFA_0009395)                                                                 |
| `CL:Curator`    |              2 | [ZFA:0005242](http://purl.obolibrary.org/obo/ZFA_0005242), [ZFA:0005873](http://purl.obolibrary.org/obo/ZFA_0005873)                                                                                                                                                                                       |
| `CL:editor`     |              2 | [ZFA:0005769](http://purl.obolibrary.org/obo/ZFA_0005769), [ZFA:0009402](http://purl.obolibrary.org/obo/ZFA_0009402)                                                                                                                                                                                       |
| `CL:tfm`        |              1 | [ZFA:0005743](http://purl.obolibrary.org/obo/ZFA_0005743)                                                                                                                                                                                                                                                  |
| `CL:MAH`        |              1 | [ZFA:0005775](http://purl.obolibrary.org/obo/ZFA_0005775)                                                                                                                                                                                                                                                  |
| `CL:dhill`      |              1 | [ZFA:0009301](http://purl.obolibrary.org/obo/ZFA_0009301)                                                                                                                                                                                                                                                  |
| `CL:00000365`   |              1 | [ZFA:0005772](http://purl.obolibrary.org/obo/ZFA_0005772)                                                                                                                                                                                                                                                  |

## `FB`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `FB` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `FB:ma`         |              1 | [ZFA:0009387](http://purl.obolibrary.org/obo/ZFA_0009387) |

## `GO`: Gene Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `GO:CJM`        |              1 | [ZFA:0009307](http://purl.obolibrary.org/obo/ZFA_0009307) |

## `MESH`: Medical Subject Headings

Overall, there were 1 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `MESH:68018069` |              1 | [ZFA:0000678](http://purl.obolibrary.org/obo/ZFA_0000678) |

## `ORCiD`: Open Researcher and Contributor

Overall, there were 3 invalid
xrefs to external prefixed with `ORCiD` (standardized to Bioregistry
prefix [`orcid`](https://bioregistry.io/orcid)) that
did not match the standard pattern `^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$`.

| external_xref                |   usages_count | usages                                                    |
|------------------------------|----------------|-----------------------------------------------------------|
| `ORCiD:000-0002-9900-7880`   |              1 | [ZFA:0000833](http://purl.obolibrary.org/obo/ZFA_0000833) |
| `ORCiD:CVS`                  |              1 | [ZFA:0001679](http://purl.obolibrary.org/obo/ZFA_0001679) |
| `ORCiD:0000-0002-2244-7917,` |              1 | [ZFA:0005867](http://purl.obolibrary.org/obo/ZFA_0005867) |

## `ORCID`: Open Researcher and Contributor

Overall, there were 1 invalid
xrefs to external prefixed with `ORCID` (standardized to Bioregistry
prefix [`orcid`](https://bioregistry.io/orcid)) that
did not match the standard pattern `^\d{4}-\d{4}-\d{4}-\d{3}(\d|X)$`.

| external_xref              |   usages_count | usages                                                    |
|----------------------------|----------------|-----------------------------------------------------------|
| `ORCID:000-0002-2244-7917` |              1 | [ZFA:0005927](http://purl.obolibrary.org/obo/ZFA_0005927) |

## `UBERON`: Uber Anatomy Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `UBERON` (standardized to Bioregistry
prefix [`uberon`](https://bioregistry.io/uberon)) that
did not match the standard pattern `^\d+$`.

| external_xref    |   usages_count | usages                                                                                                               |
|------------------|----------------|----------------------------------------------------------------------------------------------------------------------|
| `UBERON:curator` |              2 | [ZFA:0000632](http://purl.obolibrary.org/obo/ZFA_0000632), [ZFA:0005658](http://purl.obolibrary.org/obo/ZFA_0005658) |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 12 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref              |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|----------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:<new dbxref>`        |              6 | [ZFA:0000259](http://purl.obolibrary.org/obo/ZFA_0000259), [ZFA:0000344](http://purl.obolibrary.org/obo/ZFA_0000344), [ZFA:0000400](http://purl.obolibrary.org/obo/ZFA_0000400), [ZFA:0000424](http://purl.obolibrary.org/obo/ZFA_0000424), [ZFA:0000464](http://purl.obolibrary.org/obo/ZFA_0000464), ... |
| `ZFIN:JCN 421-:189-198`    |              1 | [ZFA:0000443](http://purl.obolibrary.org/obo/ZFA_0000443)                                                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-171118-8v`   |              1 | [ZFA:0000704](http://purl.obolibrary.org/obo/ZFA_0000704)                                                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-120419-3.`   |              1 | [ZFA:0005877](http://purl.obolibrary.org/obo/ZFA_0005877)                                                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-050623-3.`   |              1 | [ZFA:0001249](http://purl.obolibrary.org/obo/ZFA_0001249)                                                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-961014-192.` |              1 | [ZFA:0001595](http://purl.obolibrary.org/obo/ZFA_0001595)                                                                                                                                                                                                                                                  |
| `ZFIN:ZDB-PUB-050120-6.`   |              1 | [ZFA:0005737](http://purl.obolibrary.org/obo/ZFA_0005737)                                                                                                                                                                                                                                                  |

