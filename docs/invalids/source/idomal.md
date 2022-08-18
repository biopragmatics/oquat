# idomal

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `idomal`. See the [GitHub repository](https://github.com/VEuPathDB-ontology/IDOMAL).


## `BFO`: Basic Formal Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `BFO` (standardized to Bioregistry
prefix [`bfo`](https://bioregistry.io/bfo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                              |
|-----------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BFO:SNAP`      |              5 | [IDOMAL:0000002](http://purl.obolibrary.org/obo/IDOMAL_0000002), [snap:Disposition](http://purl.obolibrary.org/obo/snap_Disposition), [snap:Object](http://purl.obolibrary.org/obo/snap_Object), [snap:ObjectAggregate](http://purl.obolibrary.org/obo/snap_ObjectAggregate), [snap:Role](http://purl.obolibrary.org/obo/snap_Role) |
| `BFO:BFO`       |              1 | [snap:GenericallyDependentContinuant](http://purl.obolibrary.org/obo/snap_GenericallyDependentContinuant)                                                                                                                                                                                                                           |
| `BFO:SPAN`      |              1 | [span:Process](http://purl.obolibrary.org/obo/span_Process)                                                                                                                                                                                                                                                                         |

## `CARO`: Common Anatomy Reference Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `CARO` (standardized to Bioregistry
prefix [`caro`](https://bioregistry.io/caro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `CARO:mah`      |              1 | [CL:0000000](http://purl.obolibrary.org/obo/CL_0000000)         |
| `CARO:00000041` |              1 | [IDOMAL:0002461](http://purl.obolibrary.org/obo/IDOMAL_0002461) |

## `CAS`: CAS Chemical Registry

Overall, there were 1 invalid
xrefs to external prefixed with `CAS` (standardized to Bioregistry
prefix [`cas`](https://bioregistry.io/cas)) that
did not match the standard pattern `^\d{1,7}\-\d{2}\-\d$`.

| external_xref                                                                           |   usages_count | usages                                                        |
|-----------------------------------------------------------------------------------------|----------------|---------------------------------------------------------------|
| `CAS:7-(2-chlorophenyl)-4-ethoxy-3,5-dioxa-6-aza-4-phosphaoct-6-ene-8-nitrile4-sulfide` |              1 | [MIRO:10000108](http://purl.obolibrary.org/obo/MIRO_10000108) |

## `CL`: Cell Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `CL` (standardized to Bioregistry
prefix [`cl`](https://bioregistry.io/cl)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `CL:00000081`   |              1 | [CL:0000081](http://purl.obolibrary.org/obo/CL_0000081) |

## `EnvO`: Environment Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `EnvO` (standardized to Bioregistry
prefix [`envo`](https://bioregistry.io/envo)) that
did not match the standard pattern `^\d{7,8}$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `EnvO:EnvO`     |              1 | [ENVO:00002036](http://purl.obolibrary.org/obo/ENVO_00002036) |

## `Geomames`: GeoNames

Overall, there were 1 invalid
xrefs to external prefixed with `Geomames` (standardized to Bioregistry
prefix [`geonames`](https://bioregistry.io/geonames)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `Geomames:DTCH` |              1 | [ENVO:00000037](http://purl.obolibrary.org/obo/ENVO_00000037) |

## `Geonames`: GeoNames

Overall, there were 59 invalid
xrefs to external prefixed with `Geonames` (standardized to Bioregistry
prefix [`geonames`](https://bioregistry.io/geonames)) that
did not match the standard pattern `^\d+$`.

| external_xref      |   usages_count | usages                                                                                                                                                                                                                                                                                                                         |
|--------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Geonames:feature` |             25 | [ENVO:00000014](http://purl.obolibrary.org/obo/ENVO_00000014), [ENVO:00000019](http://purl.obolibrary.org/obo/ENVO_00000019), [ENVO:00000020](http://purl.obolibrary.org/obo/ENVO_00000020), [ENVO:00000023](http://purl.obolibrary.org/obo/ENVO_00000023), [ENVO:00000026](http://purl.obolibrary.org/obo/ENVO_00000026), ... |
| `Geonames:CNL`     |              1 | [ENVO:00000014](http://purl.obolibrary.org/obo/ENVO_00000014)                                                                                                                                                                                                                                                                  |
| `Geonames:LKN`     |              1 | [ENVO:00000019](http://purl.obolibrary.org/obo/ENVO_00000019)                                                                                                                                                                                                                                                                  |
| `Geonames:LKSN`    |              1 | [ENVO:00000019](http://purl.obolibrary.org/obo/ENVO_00000019)                                                                                                                                                                                                                                                                  |
| `Geonames:LK`      |              1 | [ENVO:00000020](http://purl.obolibrary.org/obo/ENVO_00000020)                                                                                                                                                                                                                                                                  |
| `Geonames:LKS`     |              1 | [ENVO:00000020](http://purl.obolibrary.org/obo/ENVO_00000020)                                                                                                                                                                                                                                                                  |
| `Geonames:STM`     |              1 | [ENVO:00000023](http://purl.obolibrary.org/obo/ENVO_00000023)                                                                                                                                                                                                                                                                  |
| `Geonames:STMS`    |              1 | [ENVO:00000023](http://purl.obolibrary.org/obo/ENVO_00000023)                                                                                                                                                                                                                                                                  |
| `Geonames:WLL`     |              1 | [ENVO:00000026](http://purl.obolibrary.org/obo/ENVO_00000026)                                                                                                                                                                                                                                                                  |
| `Geonames:WLLS`    |              1 | [ENVO:00000026](http://purl.obolibrary.org/obo/ENVO_00000026)                                                                                                                                                                                                                                                                  |
| `Geonames:SPNG`    |              1 | [ENVO:00000027](http://purl.obolibrary.org/obo/ENVO_00000027)                                                                                                                                                                                                                                                                  |
| `Geonames:NRWS`    |              1 | [ENVO:00000029](http://purl.obolibrary.org/obo/ENVO_00000029)                                                                                                                                                                                                                                                                  |
| `Geonames:RCH`     |              1 | [ENVO:00000029](http://purl.obolibrary.org/obo/ENVO_00000029)                                                                                                                                                                                                                                                                  |
| `Geonames:SPLY`    |              1 | [ENVO:00000029](http://purl.obolibrary.org/obo/ENVO_00000029)                                                                                                                                                                                                                                                                  |
| `Geonames:WTRC`    |              1 | [ENVO:00000029](http://purl.obolibrary.org/obo/ENVO_00000029)                                                                                                                                                                                                                                                                  |
| `Geonames:PND`     |              1 | [ENVO:00000033](http://purl.obolibrary.org/obo/ENVO_00000033)                                                                                                                                                                                                                                                                  |
| `Geonames:PNDS`    |              1 | [ENVO:00000033](http://purl.obolibrary.org/obo/ENVO_00000033)                                                                                                                                                                                                                                                                  |
| `Geonames:POOL`    |              1 | [ENVO:00000033](http://purl.obolibrary.org/obo/ENVO_00000033)                                                                                                                                                                                                                                                                  |
| `Geonames:LGN`     |              1 | [ENVO:00000038](http://purl.obolibrary.org/obo/ENVO_00000038)                                                                                                                                                                                                                                                                  |
| `Geonames:LGNS`    |              1 | [ENVO:00000038](http://purl.obolibrary.org/obo/ENVO_00000038)                                                                                                                                                                                                                                                                  |
| `Geonames:CRKT`    |              1 | [ENVO:00000041](http://purl.obolibrary.org/obo/ENVO_00000041)                                                                                                                                                                                                                                                                  |
| `Geonames:WTLD`    |              1 | [ENVO:00000043](http://purl.obolibrary.org/obo/ENVO_00000043)                                                                                                                                                                                                                                                                  |
| `Geonames:ESTY`    |              1 | [ENVO:00000045](http://purl.obolibrary.org/obo/ENVO_00000045)                                                                                                                                                                                                                                                                  |
| `Geonames:MGV`     |              1 | [ENVO:00000057](http://purl.obolibrary.org/obo/ENVO_00000057)                                                                                                                                                                                                                                                                  |
| `Geonames:ISLM`    |              1 | [ENVO:00000103](http://purl.obolibrary.org/obo/ENVO_00000103)                                                                                                                                                                                                                                                                  |
| `Geonames:CULT`    |              1 | [ENVO:00000113](http://purl.obolibrary.org/obo/ENVO_00000113)                                                                                                                                                                                                                                                                  |
| `Geonames:DTCHI`   |              1 | [ENVO:00000139](http://purl.obolibrary.org/obo/ENVO_00000139)                                                                                                                                                                                                                                                                  |
| `Geonames:DTCHD`   |              1 | [ENVO:00000140](http://purl.obolibrary.org/obo/ENVO_00000140)                                                                                                                                                                                                                                                                  |
| `Geonames:MOOR`    |              1 | [ENVO:00000231](http://purl.obolibrary.org/obo/ENVO_00000231)                                                                                                                                                                                                                                                                  |
| `Geonames:SWMP`    |              1 | [ENVO:00000233](http://purl.obolibrary.org/obo/ENVO_00000233)                                                                                                                                                                                                                                                                  |
| `Geonames:FLTT`    |              1 | [ENVO:00000241](http://purl.obolibrary.org/obo/ENVO_00000241)                                                                                                                                                                                                                                                                  |
| `Geonames:CHN`     |              1 | [ENVO:00000395](http://purl.obolibrary.org/obo/ENVO_00000395)                                                                                                                                                                                                                                                                  |
| `Geonames:SCNU`    |              1 | [ENVO:00000395](http://purl.obolibrary.org/obo/ENVO_00000395)                                                                                                                                                                                                                                                                  |
| `Geonames:SCSU`    |              1 | [ENVO:00000395](http://purl.obolibrary.org/obo/ENVO_00000395)                                                                                                                                                                                                                                                                  |
| `Geonames:WTRH`    |              1 | [ENVO:00000547](http://purl.obolibrary.org/obo/ENVO_00000547)                                                                                                                                                                                                                                                                  |

## `GO`: Gene Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `GO:00304321`   |              1 | [GO:00304321](http://purl.obolibrary.org/obo/GO_00304321) |

## `ISBN`: International Standard Book Number

Overall, there were 2 invalid
xrefs to external prefixed with `ISBN` (standardized to Bioregistry
prefix [`isbn`](https://bioregistry.io/isbn)) that
did not match the standard pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`.

| external_xref         |   usages_count | usages                                                          |
|-----------------------|----------------|-----------------------------------------------------------------|
| `ISBN:0-8493-15-67-0` |              1 | [IDOMAL:0000783](http://purl.obolibrary.org/obo/IDOMAL_0000783) |
| `ISBN:0-412-40180-0:` |              1 | [IDOMAL:0002188](http://purl.obolibrary.org/obo/IDOMAL_0002188) |

## `MA`: Mouse adult gross anatomy

Overall, there were 13 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
prefix [`ma`](https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                         |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MA:ma`         |             13 | [ENVO:00000014](http://purl.obolibrary.org/obo/ENVO_00000014), [ENVO:00000019](http://purl.obolibrary.org/obo/ENVO_00000019), [ENVO:00000033](http://purl.obolibrary.org/obo/ENVO_00000033), [ENVO:00000053](http://purl.obolibrary.org/obo/ENVO_00000053), [ENVO:00000057](http://purl.obolibrary.org/obo/ENVO_00000057), ... |

## `MESH`: Medical Subject Headings

Overall, there were 2 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                            |   usages_count | usages                                                  |
|------------------------------------------|----------------|---------------------------------------------------------|
| `MESH:A.11.118.290`                      |              1 | [CL:0000232](http://purl.obolibrary.org/obo/CL_0000232) |
| `MESH:A.11.118.637.555.567.569.200.400.` |              1 | [CL:0000492](http://purl.obolibrary.org/obo/CL_0000492) |

## `NCI`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCI` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref   |   usages_count | usages                                                            |
|-----------------|----------------|-------------------------------------------------------------------|
| `NCI:Thesaurus` |              1 | [IDOMAL:50000048](http://purl.obolibrary.org/obo/IDOMAL_50000048) |

## `OBOREL`: Relation Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `OBOREL` (standardized to Bioregistry
prefix [`ro`](https://bioregistry.io/ro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref            |   usages_count | usages                                                                      |
|--------------------------|----------------|-----------------------------------------------------------------------------|
| `OBOREL:happens_during`  |              1 | [TEMP#happens:during](http://purl.obolibrary.org/obo/TEMP#happens_during)   |
| `OBOREL:participates_in` |              1 | [TEMP#participates:in](http://purl.obolibrary.org/obo/TEMP#participates_in) |
| `OBOREL:preceded_by`     |              1 | [TEMP#preceded:by](http://purl.obolibrary.org/obo/TEMP#preceded_by)         |

## `SO`: Sequence types and features ontology

Overall, there were 1 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `SO:ls`         |              1 | [SYMP:0000462](http://purl.obolibrary.org/obo/SYMP_0000462) |

## `Wikipedia`: Wikipedia

Overall, there were 3 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                       |   usages_count | usages                                                          |
|-----------------------------------------------------|----------------|-----------------------------------------------------------------|
| `Wikipedia:Spring_%28hydrosphere%29#Classification` |              1 | [ENVO:00000027](http://purl.obolibrary.org/obo/ENVO_00000027)   |
| `Wikipedia:Channel_%28geography%29`                 |              1 | [ENVO:00000395](http://purl.obolibrary.org/obo/ENVO_00000395)   |
| `Wikipedia:Field'sstain`                            |              1 | [IDOMAL:0000553](http://purl.obolibrary.org/obo/IDOMAL_0000553) |

