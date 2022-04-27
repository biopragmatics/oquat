# uberon

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `uberon`. See the [GitHub repository](https://github.com/obophenotype/uberon).


## `AEO`: Anatomical Entity Ontology

Overall, there were 31 invalid
xrefs to external prefixed with `AEO` (standardized to Bioregistry
prefix [`aeo`](https://bioregistry.io/aeo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref           |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AEO:('AEO', 'JB')`     |             30 | [UBERON:0001637](https://bioregistry.io/UBERON:0001637), [UBERON:0004016](https://bioregistry.io/UBERON:0004016), [UBERON:0005866](https://bioregistry.io/UBERON:0005866), [UBERON:0006846](https://bioregistry.io/UBERON:0006846), [UBERON:0007473](https://bioregistry.io/UBERON:0007473), ... |
| `AEO:('AEO', '000020')` |              1 | [UBERON:0001013](https://bioregistry.io/UBERON:0001013)                                                                                                                                                                                                                                          |

## `CALOHA`: CALIPHO Group Ontology of Human Anatomy

Overall, there were 3 invalid
xrefs to external prefixed with `CALOHA` (standardized to Bioregistry
prefix [`caloha`](https://bioregistry.io/caloha)) that
did not match the standard pattern `^TS-\d+$`.

| external_xref                |   usages_count | usages                                                                                                                                                                    |
|------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CALOHA:('CALOHA', 'paula')` |              3 | [UBERON:0007808](https://bioregistry.io/UBERON:0007808), [UBERON:0014454](https://bioregistry.io/UBERON:0014454), [UBERON:0014455](https://bioregistry.io/UBERON:0014455) |

## `CL`: Cell Ontology

Overall, there were 19 invalid
xrefs to external prefixed with `CL` (standardized to Bioregistry
prefix [`cl`](https://bioregistry.io/cl)) that
did not match the standard pattern `^\d{7}$`.

| external_xref     |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CL:('CL', 'tm')` |             19 | [UBERON:0001249](https://bioregistry.io/UBERON:0001249), [UBERON:0001249](https://bioregistry.io/UBERON:0001249), [UBERON:0001745](https://bioregistry.io/UBERON:0001745), [UBERON:0004041](https://bioregistry.io/UBERON:0004041), [UBERON:0004042](https://bioregistry.io/UBERON:0004042), ... |

## `DHBA`: Developing Human Brain Atlas

Overall, there were 17 invalid
xrefs to external prefixed with `DHBA` (standardized to Bioregistry
prefix [`dhba`](https://bioregistry.io/dhba)) that
did not match the standard pattern `^\d+$`.

| external_xref              |   usages_count | usages                                                  |
|----------------------------|----------------|---------------------------------------------------------|
| `DHBA:('DHBA', 'HNM')`     |              1 | [UBERON:0001892](https://bioregistry.io/UBERON:0001892) |
| `DHBA:('DHBA', 'GiRt')`    |              1 | [UBERON:0002155](https://bioregistry.io/UBERON:0002155) |
| `DHBA:('DHBA', 'ILN')`     |              1 | [UBERON:0002733](https://bioregistry.io/UBERON:0002733) |
| `DHBA:('DHBA', '10N')`     |              1 | [UBERON:0002870](https://bioregistry.io/UBERON:0002870) |
| `DHBA:('DHBA', 'AILN')`    |              1 | [UBERON:0002965](https://bioregistry.io/UBERON:0002965) |
| `DHBA:('DHBA', 'SZ')`      |              1 | [UBERON:0004023](https://bioregistry.io/UBERON:0004023) |
| `DHBA:('DHBA', 'CbV')`     |              1 | [UBERON:0004079](https://bioregistry.io/UBERON:0004079) |
| `DHBA:('DHBA', 'CbVI')`    |              1 | [UBERON:0004080](https://bioregistry.io/UBERON:0004080) |
| `DHBA:('DHBA', 'CbVIIb')`  |              1 | [UBERON:0005346](https://bioregistry.io/UBERON:0005346) |
| `DHBA:('DHBA', 'CbVIIIb')` |              1 | [UBERON:0005349](https://bioregistry.io/UBERON:0005349) |
| `DHBA:('DHBA', 'HN')`      |              1 | [UBERON:0008993](https://bioregistry.io/UBERON:0008993) |
| `DHBA:('DHBA', 'HGM')`     |              1 | [UBERON:0019263](https://bioregistry.io/UBERON:0019263) |
| `DHBA:('DHBA', 'PILN')`    |              1 | [UBERON:0019295](https://bioregistry.io/UBERON:0019295) |
| `DHBA:('DHBA', 'SHy')`     |              1 | [UBERON:0019308](https://bioregistry.io/UBERON:0019308) |
| `DHBA:('DHBA', 'FIFT')`    |              1 | [UBERON:0022247](https://bioregistry.io/UBERON:0022247) |
| `DHBA:('DHBA', 'cpn')`     |              1 | [UBERON:0022271](https://bioregistry.io/UBERON:0022271) |
| `DHBA:('DHBA', 'cbu-h')`   |              1 | [UBERON:0022272](https://bioregistry.io/UBERON:0022272) |

## `DMBA`: Developing Mouse Brain Atlas

Overall, there were 16 invalid
xrefs to external prefixed with `DMBA` (standardized to Bioregistry
prefix [`dmba`](https://bioregistry.io/dmba)) that
did not match the standard pattern `^\d+$`.

| external_xref             |   usages_count | usages                                                  |
|---------------------------|----------------|---------------------------------------------------------|
| `DMBA:('DMBA', 'CbHCx')`  |              1 | [UBERON:0002129](https://bioregistry.io/UBERON:0002129) |
| `DMBA:('DMBA', 'Mam')`    |              1 | [UBERON:0002206](https://bioregistry.io/UBERON:0002206) |
| `DMBA:('DMBA', 'dpy')`    |              1 | [UBERON:0002755](https://bioregistry.io/UBERON:0002755) |
| `DMBA:('DMBA', 'OB')`     |              1 | [UBERON:0004186](https://bioregistry.io/UBERON:0004186) |
| `DMBA:('DMBA', 'DTTh')`   |              1 | [UBERON:0004703](https://bioregistry.io/UBERON:0004703) |
| `DMBA:('DMBA', 'OB-Opl')` |              1 | [UBERON:0005376](https://bioregistry.io/UBERON:0005376) |
| `DMBA:('DMBA', 'AGlom')`  |              1 | [UBERON:0007631](https://bioregistry.io/UBERON:0007631) |
| `DMBA:('DMBA', 'Bar')`    |              1 | [UBERON:0007632](https://bioregistry.io/UBERON:0007632) |
| `DMBA:('DMBA', 'tracts')` |              1 | [UBERON:0007702](https://bioregistry.io/UBERON:0007702) |
| `DMBA:('DMBA', 'AGr')`    |              1 | [UBERON:0015244](https://bioregistry.io/UBERON:0015244) |
| `DMBA:('DMBA', 'm2')`     |              1 | [UBERON:0019274](https://bioregistry.io/UBERON:0019274) |
| `DMBA:('DMBA', 'r9')`     |              1 | [UBERON:0019284](https://bioregistry.io/UBERON:0019284) |
| `DMBA:('DMBA', 'r10')`    |              1 | [UBERON:0019285](https://bioregistry.io/UBERON:0019285) |
| `DMBA:('DMBA', 'r11')`    |              1 | [UBERON:0019286](https://bioregistry.io/UBERON:0019286) |
| `DMBA:('DMBA', 'AOPl')`   |              1 | [UBERON:0019289](https://bioregistry.io/UBERON:0019289) |
| `DMBA:('DMBA', 'AIPl')`   |              1 | [UBERON:0019290](https://bioregistry.io/UBERON:0019290) |

## `EMAPA`: Mouse Developmental Anatomy Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `EMAPA` (standardized to Bioregistry
prefix [`emapa`](https://bioregistry.io/emapa)) that
did not match the standard pattern `^\d+$`.

| external_xref           |   usages_count | usages                                                  |
|-------------------------|----------------|---------------------------------------------------------|
| `EMAPA:('EMAPA', 'th')` |              1 | [UBERON:0001638](https://bioregistry.io/UBERON:0001638) |

## `FB`: FlyBase Gene

Overall, there were 8 invalid
xrefs to external prefixed with `FB` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref      |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|--------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FB:('FB', 'gg')`  |              7 | [UBERON:0000018](https://bioregistry.io/UBERON:0000018), [UBERON:0000914](https://bioregistry.io/UBERON:0000914), [UBERON:0000918](https://bioregistry.io/UBERON:0000918), [UBERON:0000972](https://bioregistry.io/UBERON:0000972), [UBERON:0000984](https://bioregistry.io/UBERON:0000984), ... |
| `FB:('FB', 'DJS')` |              1 | [UBERON:0001048](https://bioregistry.io/UBERON:0001048)                                                                                                                                                                                                                                          |

## `FlyBase`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `FlyBase` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref                             |   usages_count | usages                                                  |
|-------------------------------------------|----------------|---------------------------------------------------------|
| `FlyBase:('FlyBase', 'FBim0000836.html')` |              1 | [UBERON:6004646](https://bioregistry.io/UBERON:6004646) |

## `FMA`: Foundational Model of Anatomy

Overall, there were 1,056 invalid
xrefs to external prefixed with `FMA` (standardized to Bioregistry
prefix [`fma`](https://bioregistry.io/fma)) that
did not match the standard pattern `^\d+$`.

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|----------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FMA:('FMA', 'TA')`  |           1023 | [UBERON:0000002](https://bioregistry.io/UBERON:0000002), [UBERON:0000010](https://bioregistry.io/UBERON:0000010), [UBERON:0000011](https://bioregistry.io/UBERON:0000011), [UBERON:0000013](https://bioregistry.io/UBERON:0000013), [UBERON:0000019](https://bioregistry.io/UBERON:0000019), ... |
| `FMA:('FMA', 'FMA')` |             27 | [UBERON:0000485](https://bioregistry.io/UBERON:0000485), [UBERON:0000486](https://bioregistry.io/UBERON:0000486), [UBERON:0001845](https://bioregistry.io/UBERON:0001845), [UBERON:0001943](https://bioregistry.io/UBERON:0001943), [UBERON:0002137](https://bioregistry.io/UBERON:0002137), ... |
| `FMA:('FMA', 'CMA')` |              6 | [UBERON:0002022](https://bioregistry.io/UBERON:0002022), [UBERON:0002657](https://bioregistry.io/UBERON:0002657), [UBERON:0002740](https://bioregistry.io/UBERON:0002740), [UBERON:0002756](https://bioregistry.io/UBERON:0002756), [UBERON:0016636](https://bioregistry.io/UBERON:0016636), ... |

## `GO`: Gene Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref          |   usages_count | usages                                                                                                           |
|------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `GO:('GO', 'GO')`      |              2 | [UBERON:0000016](https://bioregistry.io/UBERON:0000016), [UBERON:0006003](https://bioregistry.io/UBERON:0006003) |
| `GO:('GO', 'curator')` |              1 | [UBERON:0005863](https://bioregistry.io/UBERON:0005863)                                                          |

## `HBA`: Human Brain Atlas

Overall, there were 17 invalid
xrefs to external prefixed with `HBA` (standardized to Bioregistry
prefix [`hba`](https://bioregistry.io/hba)) that
did not match the standard pattern `^\d+$`.

| external_xref           |   usages_count | usages                                                  |
|-------------------------|----------------|---------------------------------------------------------|
| `HBA:('HBA', 'GiRt')`   |              1 | [UBERON:0002155](https://bioregistry.io/UBERON:0002155) |
| `HBA:('HBA', 'DTL')`    |              1 | [UBERON:0002736](https://bioregistry.io/UBERON:0002736) |
| `HBA:('HBA', 'ILr')`    |              1 | [UBERON:0002965](https://bioregistry.io/UBERON:0002965) |
| `HBA:('HBA', 'DTLd')`   |              1 | [UBERON:0002984](https://bioregistry.io/UBERON:0002984) |
| `HBA:('HBA', 'TELWM')`  |              1 | [UBERON:0011299](https://bioregistry.io/UBERON:0011299) |
| `HBA:('HBA', 'FLs')`    |              1 | [UBERON:0014639](https://bioregistry.io/UBERON:0014639) |
| `HBA:('HBA', 'TLs')`    |              1 | [UBERON:0014687](https://bioregistry.io/UBERON:0014687) |
| `HBA:('HBA', 'MESWM')`  |              1 | [UBERON:0016554](https://bioregistry.io/UBERON:0016554) |
| `HBA:('HBA', 'MYWM')`   |              1 | [UBERON:0019262](https://bioregistry.io/UBERON:0019262) |
| `HBA:('HBA', 'PoWM')`   |              1 | [UBERON:0019293](https://bioregistry.io/UBERON:0019293) |
| `HBA:('HBA', 'TELCom')` |              1 | [UBERON:0019294](https://bioregistry.io/UBERON:0019294) |
| `HBA:('HBA', 'ILc')`    |              1 | [UBERON:0019295](https://bioregistry.io/UBERON:0019295) |
| `HBA:('HBA', 'SolVL')`  |              1 | [UBERON:0019312](https://bioregistry.io/UBERON:0019312) |
| `HBA:('HBA', 'AOrG')`   |              1 | [UBERON:0022244](https://bioregistry.io/UBERON:0022244) |
| `HBA:('HBA', 'EL')`     |              1 | [UBERON:0022258](https://bioregistry.io/UBERON:0022258) |
| `HBA:('HBA', 'PLT')`    |              1 | [UBERON:0022268](https://bioregistry.io/UBERON:0022268) |
| `HBA:('HBA', 'cpn')`    |              1 | [UBERON:0022271](https://bioregistry.io/UBERON:0022271) |

## `HPO`: Human Phenotype Ontology

Overall, there were 5 invalid
xrefs to external prefixed with `HPO` (standardized to Bioregistry
prefix [`hp`](https://bioregistry.io/hp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref              |   usages_count | usages                                                                                                           |
|----------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `HPO:('HPO', 'curators')`  |              2 | [UBERON:0014386](https://bioregistry.io/UBERON:0014386), [UBERON:0034908](https://bioregistry.io/UBERON:0034908) |
| `HPO:('HPO', 'pr')`        |              2 | [UBERON:0001750](https://bioregistry.io/UBERON:0001750), [UBERON:0035639](https://bioregistry.io/UBERON:0035639) |
| `HPO:('HPO', 'probinson')` |              1 | [UBERON:0017732](https://bioregistry.io/UBERON:0017732)                                                          |

## `MA`: Mouse adult gross anatomy

Overall, there were 16 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
prefix [`ma`](https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref     |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MA:('MA', 'th')` |             16 | [UBERON:0000983](https://bioregistry.io/UBERON:0000983), [UBERON:0002470](https://bioregistry.io/UBERON:0002470), [UBERON:0002471](https://bioregistry.io/UBERON:0002471), [UBERON:0002472](https://bioregistry.io/UBERON:0002472), [UBERON:0003282](https://bioregistry.io/UBERON:0003282), ... |

## `MESH`: Medical Subject Headings

Overall, there were 452 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                                          |   usages_count | usages                                                                                                                                                                    |
|--------------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MESH:('MESH', 'A02.835.232.500.247.343')`             |              3 | [UBERON:0006767](https://bioregistry.io/UBERON:0006767), [UBERON:0006767](https://bioregistry.io/UBERON:0006767), [UBERON:0006767](https://bioregistry.io/UBERON:0006767) |
| `MESH:('MESH', 'D24.185.926.580.590')`                 |              3 | [UBERON:0008274](https://bioregistry.io/UBERON:0008274), [UBERON:0008274](https://bioregistry.io/UBERON:0008274), [UBERON:0008274](https://bioregistry.io/UBERON:0008274) |
| `MESH:('MESH', 'D24.185.926.580.230')`                 |              3 | [UBERON:0008280](https://bioregistry.io/UBERON:0008280), [UBERON:0008280](https://bioregistry.io/UBERON:0008280), [UBERON:0008280](https://bioregistry.io/UBERON:0008280) |
| `MESH:('MESH', 'D24.185.965.850.325')`                 |              3 | [UBERON:0013106](https://bioregistry.io/UBERON:0013106), [UBERON:0013106](https://bioregistry.io/UBERON:0013106), [UBERON:0013106](https://bioregistry.io/UBERON:0013106) |
| `MESH:('MESH', 'D24.185.965.850.480')`                 |              3 | [UBERON:0013110](https://bioregistry.io/UBERON:0013110), [UBERON:0013110](https://bioregistry.io/UBERON:0013110), [UBERON:0013110](https://bioregistry.io/UBERON:0013110) |
| `MESH:('MESH', 'D24.185.965.850.960')`                 |              3 | [UBERON:0013112](https://bioregistry.io/UBERON:0013112), [UBERON:0013112](https://bioregistry.io/UBERON:0013112), [UBERON:0013112](https://bioregistry.io/UBERON:0013112) |
| `MESH:('MESH', 'A08.186.211.577.699')`                 |              3 | [UBERON:0013201](https://bioregistry.io/UBERON:0013201), [UBERON:0013201](https://bioregistry.io/UBERON:0013201), [UBERON:0013201](https://bioregistry.io/UBERON:0013201) |
| `MESH:('MESH', 'A10.165.265.507')`                     |              3 | [UBERON:0014730](https://bioregistry.io/UBERON:0014730), [UBERON:0014730](https://bioregistry.io/UBERON:0014730), [UBERON:0014731](https://bioregistry.io/UBERON:0014731) |
| `MESH:('MESH', 'G06.535.805')`                         |              3 | [UBERON:0018229](https://bioregistry.io/UBERON:0018229), [UBERON:0018229](https://bioregistry.io/UBERON:0018229), [UBERON:0018229](https://bioregistry.io/UBERON:0018229) |
| `MESH:('MESH', 'A08.800.550.700.650')`                 |              3 | [UBERON:0035017](https://bioregistry.io/UBERON:0035017), [UBERON:0035017](https://bioregistry.io/UBERON:0035017), [UBERON:0035017](https://bioregistry.io/UBERON:0035017) |
| `MESH:('MESH', 'A08.800.550.700.840')`                 |              3 | [UBERON:0035018](https://bioregistry.io/UBERON:0035018), [UBERON:0035018](https://bioregistry.io/UBERON:0035018), [UBERON:0035018](https://bioregistry.io/UBERON:0035018) |
| `MESH:('MESH', 'A09.246.631.909.625.125')`             |              2 | [UBERON:0000054](https://bioregistry.io/UBERON:0000054), [UBERON:0000054](https://bioregistry.io/UBERON:0000054)                                                          |
| `MESH:('MESH', 'A08.186.211.730.385.800.240')`         |              2 | [UBERON:0000432](https://bioregistry.io/UBERON:0000432), [UBERON:0000432](https://bioregistry.io/UBERON:0000432)                                                          |
| `MESH:('MESH', 'A04.531.621.578')`                     |              2 | [UBERON:0001764](https://bioregistry.io/UBERON:0001764), [UBERON:0001764](https://bioregistry.io/UBERON:0001764)                                                          |
| `MESH:('MESH', 'A07.231.432.952')`                     |              2 | [UBERON:0001979](https://bioregistry.io/UBERON:0001979), [UBERON:0001979](https://bioregistry.io/UBERON:0001979)                                                          |
| `MESH:('MESH', 'A08.186.854.610.800')`                 |              2 | [UBERON:0002181](https://bioregistry.io/UBERON:0002181), [UBERON:0002181](https://bioregistry.io/UBERON:0002181)                                                          |
| `MESH:('MESH', 'A05.810.453.736.520.380')`             |              2 | [UBERON:0002320](https://bioregistry.io/UBERON:0002320), [UBERON:0002320](https://bioregistry.io/UBERON:0002320)                                                          |
| `MESH:('MESH', 'A08.186.211.730.385.357.362')`         |              2 | [UBERON:0002770](https://bioregistry.io/UBERON:0002770), [UBERON:0002770](https://bioregistry.io/UBERON:0002770)                                                          |
| `MESH:('MESH', 'A01.047.412')`                         |              2 | [UBERON:0003702](https://bioregistry.io/UBERON:0003702), [UBERON:0003702](https://bioregistry.io/UBERON:0003702)                                                          |
| `MESH:('MESH', 'A12.200.946')`                         |              2 | [UBERON:0007108](https://bioregistry.io/UBERON:0007108), [UBERON:0007108](https://bioregistry.io/UBERON:0007108)                                                          |
| `MESH:('MESH', 'A14.254.245')`                         |              2 | [UBERON:0007116](https://bioregistry.io/UBERON:0007116), [UBERON:0007116](https://bioregistry.io/UBERON:0007116)                                                          |
| `MESH:('MESH', 'A01.047.849')`                         |              2 | [UBERON:0007118](https://bioregistry.io/UBERON:0007118), [UBERON:0007118](https://bioregistry.io/UBERON:0007118)                                                          |
| `MESH:('MESH', 'A13.869.524')`                         |              2 | [UBERON:0007362](https://bioregistry.io/UBERON:0007362), [UBERON:0007362](https://bioregistry.io/UBERON:0007362)                                                          |
| `MESH:('MESH', 'A14.254.237')`                         |              2 | [UBERON:0007774](https://bioregistry.io/UBERON:0007774), [UBERON:0007774](https://bioregistry.io/UBERON:0007774)                                                          |
| `MESH:('MESH', 'A14.254.860.715')`                     |              2 | [UBERON:0007776](https://bioregistry.io/UBERON:0007776), [UBERON:0007776](https://bioregistry.io/UBERON:0007776)                                                          |
| `MESH:('MESH', 'A14.254.229')`                         |              2 | [UBERON:0007799](https://bioregistry.io/UBERON:0007799), [UBERON:0007799](https://bioregistry.io/UBERON:0007799)                                                          |
| `MESH:('MESH', 'A01.047.365')`                         |              2 | [UBERON:0008337](https://bioregistry.io/UBERON:0008337), [UBERON:0008337](https://bioregistry.io/UBERON:0008337)                                                          |
| `MESH:('MESH', 'A08.186.211.730.885.213.670.675')`     |              2 | [UBERON:0008930](https://bioregistry.io/UBERON:0008930), [UBERON:0008930](https://bioregistry.io/UBERON:0008930)                                                          |
| `MESH:('MESH', 'A14.254.860.700.500')`                 |              2 | [UBERON:0009977](https://bioregistry.io/UBERON:0009977), [UBERON:0009977](https://bioregistry.io/UBERON:0009977)                                                          |
| `MESH:('MESH', 'A13.660')`                             |              2 | [UBERON:0010207](https://bioregistry.io/UBERON:0010207), [UBERON:0010207](https://bioregistry.io/UBERON:0010207)                                                          |
| `MESH:('MESH', 'A07.231.432')`                         |              2 | [UBERON:0010523](https://bioregistry.io/UBERON:0010523), [UBERON:0010523](https://bioregistry.io/UBERON:0010523)                                                          |
| `MESH:('MESH', 'A09.246.631.246.280')`                 |              2 | [UBERON:0011060](https://bioregistry.io/UBERON:0011060), [UBERON:0011060](https://bioregistry.io/UBERON:0011060)                                                          |
| `MESH:('MESH', 'A08.663.542.100')`                     |              2 | [UBERON:0011924](https://bioregistry.io/UBERON:0011924), [UBERON:0011924](https://bioregistry.io/UBERON:0011924)                                                          |
| `MESH:('MESH', 'A08.663.542.122')`                     |              2 | [UBERON:0011925](https://bioregistry.io/UBERON:0011925), [UBERON:0011925](https://bioregistry.io/UBERON:0011925)                                                          |
| `MESH:('MESH', 'A06.224.736')`                         |              2 | [UBERON:0012279](https://bioregistry.io/UBERON:0012279), [UBERON:0012279](https://bioregistry.io/UBERON:0012279)                                                          |
| `MESH:('MESH', 'A02.513.170')`                         |              2 | [UBERON:0012332](https://bioregistry.io/UBERON:0012332), [UBERON:0012332](https://bioregistry.io/UBERON:0012332)                                                          |
| `MESH:('MESH', 'A08.800.550')`                         |              2 | [UBERON:0012453](https://bioregistry.io/UBERON:0012453), [UBERON:0012453](https://bioregistry.io/UBERON:0012453)                                                          |
| `MESH:('MESH', 'D24.185.965.850')`                     |              2 | [UBERON:0013076](https://bioregistry.io/UBERON:0013076), [UBERON:0013076](https://bioregistry.io/UBERON:0013076)                                                          |
| `MESH:('MESH', 'A08.186.211.132.810.428.200.462')`     |              2 | [UBERON:0014908](https://bioregistry.io/UBERON:0014908), [UBERON:0014908](https://bioregistry.io/UBERON:0014908)                                                          |
| `MESH:('MESH', 'A08.612.600')`                         |              2 | [UBERON:0034931](https://bioregistry.io/UBERON:0034931), [UBERON:0034931](https://bioregistry.io/UBERON:0034931)                                                          |
| `MESH:('MESH', 'A08.800.550.700.120.600.350')`         |              2 | [UBERON:0034972](https://bioregistry.io/UBERON:0034972), [UBERON:0034972](https://bioregistry.io/UBERON:0034972)                                                          |
| `MESH:('MESH', 'A08.800.550.700.120.600')`             |              2 | [UBERON:0034979](https://bioregistry.io/UBERON:0034979), [UBERON:0034979](https://bioregistry.io/UBERON:0034979)                                                          |
| `MESH:('MESH', 'A01.378.800')`                         |              2 | [UBERON:0001460](https://bioregistry.io/UBERON:0001460), [UBERON:0001460](https://bioregistry.io/UBERON:0001460)                                                          |
| `MESH:('MESH', 'A14.254.646')`                         |              2 | [UBERON:0001758](https://bioregistry.io/UBERON:0001758), [UBERON:0001758](https://bioregistry.io/UBERON:0001758)                                                          |
| `MESH:('MESH', 'A08.186.211.730.385.357.352')`         |              2 | [UBERON:0002555](https://bioregistry.io/UBERON:0002555), [UBERON:0002555](https://bioregistry.io/UBERON:0002555)                                                          |
| `MESH:('MESH', 'A08.800.050.800.900.700')`             |              2 | [UBERON:0004019](https://bioregistry.io/UBERON:0004019), [UBERON:0018392](https://bioregistry.io/UBERON:0018392)                                                          |
| `MESH:('MESH', 'A12.207.571')`                         |              2 | [UBERON:0006586](https://bioregistry.io/UBERON:0006586), [UBERON:0006586](https://bioregistry.io/UBERON:0006586)                                                          |
| `MESH:('MESH', 'A16.254.891')`                         |              2 | [UBERON:0007105](https://bioregistry.io/UBERON:0007105), [UBERON:0007105](https://bioregistry.io/UBERON:0007105)                                                          |
| `MESH:('MESH', 'A16.254.403.473.200')`                 |              2 | [UBERON:0007106](https://bioregistry.io/UBERON:0007106), [UBERON:0007106](https://bioregistry.io/UBERON:0007106)                                                          |
| `MESH:('MESH', 'A01.047.025.600.225')`                 |              2 | [UBERON:0007111](https://bioregistry.io/UBERON:0007111), [UBERON:0007111](https://bioregistry.io/UBERON:0007111)                                                          |
| `MESH:('MESH', 'A03.365.414')`                         |              2 | [UBERON:0007650](https://bioregistry.io/UBERON:0007650), [UBERON:0007650](https://bioregistry.io/UBERON:0007650)                                                          |
| `MESH:('MESH', 'A06.407.747.357')`                     |              2 | [UBERON:0009976](https://bioregistry.io/UBERON:0009976), [UBERON:0009976](https://bioregistry.io/UBERON:0009976)                                                          |
| `MESH:('MESH', 'A08.663.542.075.800')`                 |              2 | [UBERON:0011926](https://bioregistry.io/UBERON:0011926), [UBERON:0011926](https://bioregistry.io/UBERON:0011926)                                                          |
| `MESH:('MESH', 'A08.800.550.700')`                     |              2 | [UBERON:0012451](https://bioregistry.io/UBERON:0012451), [UBERON:0012451](https://bioregistry.io/UBERON:0012451)                                                          |
| `MESH:('MESH', 'A06.407.850')`                         |              2 | [UBERON:0002370](https://bioregistry.io/UBERON:0002370), [UBERON:0003483](https://bioregistry.io/UBERON:0003483)                                                          |
| `MESH:('MESH', 'A03.734.414')`                         |              1 | [UBERON:0000006](https://bioregistry.io/UBERON:0000006)                                                                                                                   |
| `MESH:('MESH', 'A09.371.729.522')`                     |              1 | [UBERON:0000053](https://bioregistry.io/UBERON:0000053)                                                                                                                   |
| `MESH:('MESH', 'A01.456.810')`                         |              1 | [UBERON:0000403](https://bioregistry.io/UBERON:0000403)                                                                                                                   |
| `MESH:('MESH', 'A07.541.510')`                         |              1 | [UBERON:0000946](https://bioregistry.io/UBERON:0000946)                                                                                                                   |
| `MESH:('MESH', 'A07.231.114.056')`                     |              1 | [UBERON:0000947](https://bioregistry.io/UBERON:0000947)                                                                                                                   |
| `MESH:('MESH', 'A09.371.060.217')`                     |              1 | [UBERON:0000964](https://bioregistry.io/UBERON:0000964)                                                                                                                   |
| `MESH:('MESH', 'A10.165.114')`                         |              1 | [UBERON:0001013](https://bioregistry.io/UBERON:0001013)                                                                                                                   |
| `MESH:('MESH', 'A13.641')`                             |              1 | [UBERON:0001058](https://bioregistry.io/UBERON:0001058)                                                                                                                   |
| `MESH:('MESH', 'A02.633.567.900.500')`                 |              1 | [UBERON:0001111](https://bioregistry.io/UBERON:0001111)                                                                                                                   |
| `MESH:('MESH', 'A07.231.114.565.755')`                 |              1 | [UBERON:0001182](https://bioregistry.io/UBERON:0001182)                                                                                                                   |
| `MESH:('MESH', 'A10.549.600')`                         |              1 | [UBERON:0001211](https://bioregistry.io/UBERON:0001211)                                                                                                                   |
| `MESH:('MESH', 'A06.407.071.265')`                     |              1 | [UBERON:0001236](https://bioregistry.io/UBERON:0001236)                                                                                                                   |
| `MESH:('MESH', 'A05.360.319.679.490')`                 |              1 | [UBERON:0001295](https://bioregistry.io/UBERON:0001295)                                                                                                                   |
| `MESH:('MESH', 'A02.633.570.500')`                     |              1 | [UBERON:0001296](https://bioregistry.io/UBERON:0001296)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.251')`                     |              1 | [UBERON:0001437](https://bioregistry.io/UBERON:0001437)                                                                                                                   |
| `MESH:('MESH', 'A02.835.583.378.062')`                 |              1 | [UBERON:0001488](https://bioregistry.io/UBERON:0001488)                                                                                                                   |
| `MESH:('MESH', 'A04.531.621.827')`                     |              1 | [UBERON:0001724](https://bioregistry.io/UBERON:0001724)                                                                                                                   |
| `MESH:('MESH', 'A09.371.060.067')`                     |              1 | [UBERON:0001766](https://bioregistry.io/UBERON:0001766)                                                                                                                   |
| `MESH:('MESH', 'A09.371.060.217.325')`                 |              1 | [UBERON:0001772](https://bioregistry.io/UBERON:0001772)                                                                                                                   |
| `MESH:('MESH', 'A09.371.060.217.228')`                 |              1 | [UBERON:0001777](https://bioregistry.io/UBERON:0001777)                                                                                                                   |
| `MESH:('MESH', 'A08.800.800.720')`                     |              1 | [UBERON:0001780](https://bioregistry.io/UBERON:0001780)                                                                                                                   |
| `MESH:('MESH', 'A09.371.060')`                         |              1 | [UBERON:0001801](https://bioregistry.io/UBERON:0001801)                                                                                                                   |
| `MESH:('MESH', 'A09.371.060.200')`                     |              1 | [UBERON:0001811](https://bioregistry.io/UBERON:0001811)                                                                                                                   |
| `MESH:('MESH', 'A12.200.194')`                         |              1 | [UBERON:0001914](https://bioregistry.io/UBERON:0001914)                                                                                                                   |
| `MESH:('MESH', 'A10.272.491')`                         |              1 | [UBERON:0001986](https://bioregistry.io/UBERON:0001986)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.132.810.428.200')`         |              1 | [UBERON:0002037](https://bioregistry.io/UBERON:0002037)                                                                                                                   |
| `MESH:('MESH', 'A06.407.071.140.960')`                 |              1 | [UBERON:0002053](https://bioregistry.io/UBERON:0002053)                                                                                                                   |
| `MESH:('MESH', 'A06.407.071.140.950')`                 |              1 | [UBERON:0002054](https://bioregistry.io/UBERON:0002054)                                                                                                                   |
| `MESH:('MESH', 'A06.407.071.140.970')`                 |              1 | [UBERON:0002055](https://bioregistry.io/UBERON:0002055)                                                                                                                   |
| `MESH:('MESH', 'A07.541.459')`                         |              1 | [UBERON:0002099](https://bioregistry.io/UBERON:0002099)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.132.810.406.286')`         |              1 | [UBERON:0002162](https://bioregistry.io/UBERON:0002162)                                                                                                                   |
| `MESH:('MESH', 'A04.411.125')`                         |              1 | [UBERON:0002185](https://bioregistry.io/UBERON:0002185)                                                                                                                   |
| `MESH:('MESH', 'A07.231.114.681')`                     |              1 | [UBERON:0002250](https://bioregistry.io/UBERON:0002250)                                                                                                                   |
| `MESH:('MESH', 'A12.200.147')`                         |              1 | [UBERON:0002297](https://bioregistry.io/UBERON:0002297)                                                                                                                   |
| `MESH:('MESH', 'A08.340.315.350.800')`                 |              1 | [UBERON:0002441](https://bioregistry.io/UBERON:0002441)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.317.357.342.063')`     |              1 | [UBERON:0002634](https://bioregistry.io/UBERON:0002634)                                                                                                                   |
| `MESH:('MESH', 'A10.615.284.473')`                     |              1 | [UBERON:0003124](https://bioregistry.io/UBERON:0003124)                                                                                                                   |
| `MESH:('MESH', 'A02.513.514.475')`                     |              1 | [UBERON:0003676](https://bioregistry.io/UBERON:0003676)                                                                                                                   |
| `MESH:('MESH', 'A02.633.567.600')`                     |              1 | [UBERON:0003681](https://bioregistry.io/UBERON:0003681)                                                                                                                   |
| `MESH:('MESH', 'A02.633.567.750')`                     |              1 | [UBERON:0003682](https://bioregistry.io/UBERON:0003682)                                                                                                                   |
| `MESH:('MESH', 'A03.159.183.079')`                     |              1 | [UBERON:0003703](https://bioregistry.io/UBERON:0003703)                                                                                                                   |
| `MESH:('MESH', 'A03.159.183.158')`                     |              1 | [UBERON:0003704](https://bioregistry.io/UBERON:0003704)                                                                                                                   |
| `MESH:('MESH', 'A07.231.836')`                         |              1 | [UBERON:0003710](https://bioregistry.io/UBERON:0003710)                                                                                                                   |
| `MESH:('MESH', 'A01.456.830.165')`                     |              1 | [UBERON:0003722](https://bioregistry.io/UBERON:0003722)                                                                                                                   |
| `MESH:('MESH', 'A08.800.800.720.800')`                 |              1 | [UBERON:0003726](https://bioregistry.io/UBERON:0003726)                                                                                                                   |
| `MESH:('MESH', 'A04.760')`                             |              1 | [UBERON:0004785](https://bioregistry.io/UBERON:0004785)                                                                                                                   |
| `MESH:('MESH', 'A05.360.444.849')`                     |              1 | [UBERON:0005212](https://bioregistry.io/UBERON:0005212)                                                                                                                   |
| `MESH:('MESH', 'A04.531.520.573')`                     |              1 | [UBERON:0005386](https://bioregistry.io/UBERON:0005386)                                                                                                                   |
| `MESH:('MESH', 'A07.541.278.395')`                     |              1 | [UBERON:0005440](https://bioregistry.io/UBERON:0005440)                                                                                                                   |
| `MESH:('MESH', 'A07.231.114.565')`                     |              1 | [UBERON:0005616](https://bioregistry.io/UBERON:0005616)                                                                                                                   |
| `MESH:('MESH', 'A07.231.908.670.385')`                 |              1 | [UBERON:0005617](https://bioregistry.io/UBERON:0005617)                                                                                                                   |
| `MESH:('MESH', 'A12.207')`                             |              1 | [UBERON:0006314](https://bioregistry.io/UBERON:0006314)                                                                                                                   |
| `MESH:('MESH', 'A05.810.453.537.503')`                 |              1 | [UBERON:0006517](https://bioregistry.io/UBERON:0006517)                                                                                                                   |
| `MESH:('MESH', 'A02.633.567.700')`                     |              1 | [UBERON:0006531](https://bioregistry.io/UBERON:0006531)                                                                                                                   |
| `MESH:('MESH', 'A02.513.803')`                         |              1 | [UBERON:0006589](https://bioregistry.io/UBERON:0006589)                                                                                                                   |
| `MESH:('MESH', 'A12.200.935')`                         |              1 | [UBERON:0007113](https://bioregistry.io/UBERON:0007113)                                                                                                                   |
| `MESH:('MESH', 'A13.869.106')`                         |              1 | [UBERON:0007358](https://bioregistry.io/UBERON:0007358)                                                                                                                   |
| `MESH:('MESH', 'A13.869.697')`                         |              1 | [UBERON:0007361](https://bioregistry.io/UBERON:0007361)                                                                                                                   |
| `MESH:('MESH', 'A13.869.804')`                         |              1 | [UBERON:0007365](https://bioregistry.io/UBERON:0007365)                                                                                                                   |
| `MESH:('MESH', 'A07.231.114.895')`                     |              1 | [UBERON:0007610](https://bioregistry.io/UBERON:0007610)                                                                                                                   |
| `MESH:('MESH', 'A12.383')`                             |              1 | [UBERON:0007780](https://bioregistry.io/UBERON:0007780)                                                                                                                   |
| `MESH:('MESH', 'A12.207.119')`                         |              1 | [UBERON:0007795](https://bioregistry.io/UBERON:0007795)                                                                                                                   |
| `MESH:('MESH', 'A09.246.631.663')`                     |              1 | [UBERON:0007833](https://bioregistry.io/UBERON:0007833)                                                                                                                   |
| `MESH:('MESH', 'A01.456.505.580')`                     |              1 | [UBERON:0008200](https://bioregistry.io/UBERON:0008200)                                                                                                                   |
| `MESH:('MESH', 'A02.633.567.825')`                     |              1 | [UBERON:0008450](https://bioregistry.io/UBERON:0008450)                                                                                                                   |
| `MESH:('MESH', 'A01.456.830.200')`                     |              1 | [UBERON:0008788](https://bioregistry.io/UBERON:0008788)                                                                                                                   |
| `MESH:('MESH', 'A08.800.800.720.725')`                 |              1 | [UBERON:0009623](https://bioregistry.io/UBERON:0009623)                                                                                                                   |
| `MESH:('MESH', 'A16.254.500')`                         |              1 | [UBERON:0000080](https://bioregistry.io/UBERON:0000080)                                                                                                                   |
| `MESH:('MESH', 'A01.378.610')`                         |              1 | [UBERON:0000978](https://bioregistry.io/UBERON:0000978)                                                                                                                   |
| `MESH:('MESH', 'A03.734.667')`                         |              1 | [UBERON:0001064](https://bioregistry.io/UBERON:0001064)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.834')`                     |              1 | [UBERON:0001130](https://bioregistry.io/UBERON:0001130)                                                                                                                   |
| `MESH:('MESH', 'A05.360.319.779.479')`                 |              1 | [UBERON:0001346](https://bioregistry.io/UBERON:0001346)                                                                                                                   |
| `MESH:('MESH', 'A08.800.800.120.680.660')`             |              1 | [UBERON:0001783](https://bioregistry.io/UBERON:0001783)                                                                                                                   |
| `MESH:('MESH', 'A08.800.050.050.150')`                 |              1 | [UBERON:0002010](https://bioregistry.io/UBERON:0002010)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232')`                         |              1 | [UBERON:0002481](https://bioregistry.io/UBERON:0002481)                                                                                                                   |
| `MESH:('MESH', 'A09.246.631.909.625')`                 |              1 | [UBERON:0002518](https://bioregistry.io/UBERON:0002518)                                                                                                                   |
| `MESH:('MESH', 'A07.231.114.891')`                     |              1 | [UBERON:0003473](https://bioregistry.io/UBERON:0003473)                                                                                                                   |
| `MESH:('MESH', 'A04.329.364.737')`                     |              1 | [UBERON:0003706](https://bioregistry.io/UBERON:0003706)                                                                                                                   |
| `MESH:('MESH', 'A01.378.610.500')`                     |              1 | [UBERON:0003823](https://bioregistry.io/UBERON:0003823)                                                                                                                   |
| `MESH:('MESH', 'A09.371.894.223.250')`                 |              1 | [UBERON:0003957](https://bioregistry.io/UBERON:0003957)                                                                                                                   |
| `MESH:('MESH', 'A05.810.453.736.560.570')`             |              1 | [UBERON:0004134](https://bioregistry.io/UBERON:0004134)                                                                                                                   |
| `MESH:('MESH', 'A09.246.631.246.930')`                 |              1 | [UBERON:0006724](https://bioregistry.io/UBERON:0006724)                                                                                                                   |
| `MESH:('MESH', 'A09.371.670')`                         |              1 | [UBERON:0007625](https://bioregistry.io/UBERON:0007625)                                                                                                                   |
| `MESH:('MESH', 'A02.835.583.378.900')`                 |              1 | [UBERON:0007721](https://bioregistry.io/UBERON:0007721)                                                                                                                   |
| `MESH:('MESH', 'A02.835.583.378.831')`                 |              1 | [UBERON:0008447](https://bioregistry.io/UBERON:0008447)                                                                                                                   |
| `MESH:('MESH', 'A06.224')`                             |              1 | [UBERON:0010074](https://bioregistry.io/UBERON:0010074)                                                                                                                   |
| `MESH:('MESH', 'A12.207.152.200')`                     |              1 | [UBERON:0012168](https://bioregistry.io/UBERON:0012168)                                                                                                                   |
| `MESH:('MESH', 'A13.734')`                             |              1 | [UBERON:0012281](https://bioregistry.io/UBERON:0012281)                                                                                                                   |
| `MESH:('MESH', 'A08.800.800.720.725.150')`             |              1 | [UBERON:0012337](https://bioregistry.io/UBERON:0012337)                                                                                                                   |
| `MESH:('MESH', 'A11.284.180.565')`                     |              1 | [UBERON:0012423](https://bioregistry.io/UBERON:0012423)                                                                                                                   |
| `MESH:('MESH', 'A13.970')`                             |              1 | [UBERON:0013196](https://bioregistry.io/UBERON:0013196)                                                                                                                   |
| `MESH:('MESH', 'E05.256')`                             |              1 | [UBERON:0013487](https://bioregistry.io/UBERON:0013487)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.495')`                     |              1 | [UBERON:0000059](https://bioregistry.io/UBERON:0000059)                                                                                                                   |
| `MESH:('MESH', 'A16.254.270.550')`                     |              1 | [UBERON:0000085](https://bioregistry.io/UBERON:0000085)                                                                                                                   |
| `MESH:('MESH', 'A11.936')`                             |              1 | [UBERON:0000088](https://bioregistry.io/UBERON:0000088)                                                                                                                   |
| `MESH:('MESH', 'A16.254.270')`                         |              1 | [UBERON:0000107](https://bioregistry.io/UBERON:0000107)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411')`                         |              1 | [UBERON:0000160](https://bioregistry.io/UBERON:0000160)                                                                                                                   |
| `MESH:('MESH', 'A16.254.403.277')`                     |              1 | [UBERON:0000305](https://bioregistry.io/UBERON:0000305)                                                                                                                   |
| `MESH:('MESH', 'A16.254.270.274')`                     |              1 | [UBERON:0000307](https://bioregistry.io/UBERON:0000307)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577')`                     |              1 | [UBERON:0000349](https://bioregistry.io/UBERON:0000349)                                                                                                                   |
| `MESH:('MESH', 'A16.254.085')`                         |              1 | [UBERON:0000358](https://bioregistry.io/UBERON:0000358)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.105.487')`         |              1 | [UBERON:0000369](https://bioregistry.io/UBERON:0000369)                                                                                                                   |
| `MESH:('MESH', 'A02.165.507.411')`                     |              1 | [UBERON:0000388](https://bioregistry.io/UBERON:0000388)                                                                                                                   |
| `MESH:('MESH', 'A09.371.509.225')`                     |              1 | [UBERON:0000389](https://bioregistry.io/UBERON:0000389)                                                                                                                   |
| `MESH:('MESH', 'A09.371.509.670')`                     |              1 | [UBERON:0000390](https://bioregistry.io/UBERON:0000390)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.213.571.735')`     |              1 | [UBERON:0000411](https://bioregistry.io/UBERON:0000411)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.750')`                 |              1 | [UBERON:0000446](https://bioregistry.io/UBERON:0000446)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.213.270.700')`     |              1 | [UBERON:0000451](https://bioregistry.io/UBERON:0000451)                                                                                                                   |
| `MESH:('MESH', 'A12.207.630.350')`                     |              1 | [UBERON:0000911](https://bioregistry.io/UBERON:0000911)                                                                                                                   |
| `MESH:('MESH', 'A01.047')`                             |              1 | [UBERON:0000916](https://bioregistry.io/UBERON:0000916)                                                                                                                   |
| `MESH:('MESH', 'A16.254.425')`                         |              1 | [UBERON:0000923](https://bioregistry.io/UBERON:0000923)                                                                                                                   |
| `MESH:('MESH', 'A16.254.425.273')`                     |              1 | [UBERON:0000924](https://bioregistry.io/UBERON:0000924)                                                                                                                   |
| `MESH:('MESH', 'A16.254.425.407')`                     |              1 | [UBERON:0000925](https://bioregistry.io/UBERON:0000925)                                                                                                                   |
| `MESH:('MESH', 'A16.254.425.660')`                     |              1 | [UBERON:0000926](https://bioregistry.io/UBERON:0000926)                                                                                                                   |
| `MESH:('MESH', 'A03.492.766')`                         |              1 | [UBERON:0000945](https://bioregistry.io/UBERON:0000945)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.213')`             |              1 | [UBERON:0000956](https://bioregistry.io/UBERON:0000956)                                                                                                                   |
| `MESH:('MESH', 'A09.371.509')`                         |              1 | [UBERON:0000965](https://bioregistry.io/UBERON:0000965)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.087.412')`                 |              1 | [UBERON:0000976](https://bioregistry.io/UBERON:0000976)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.500.883')`                 |              1 | [UBERON:0000979](https://bioregistry.io/UBERON:0000979)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.500.247')`                 |              1 | [UBERON:0000981](https://bioregistry.io/UBERON:0000981)                                                                                                                   |
| `MESH:('MESH', 'A16.254.403.981')`                     |              1 | [UBERON:0001040](https://bioregistry.io/UBERON:0001040)                                                                                                                   |
| `MESH:('MESH', 'A03.867')`                             |              1 | [UBERON:0001042](https://bioregistry.io/UBERON:0001042)                                                                                                                   |
| `MESH:('MESH', 'A03.365')`                             |              1 | [UBERON:0001043](https://bioregistry.io/UBERON:0001043)                                                                                                                   |
| `MESH:('MESH', 'A03.867.490')`                         |              1 | [UBERON:0001051](https://bioregistry.io/UBERON:0001051)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.495.767')`                 |              1 | [UBERON:0001052](https://bioregistry.io/UBERON:0001052)                                                                                                                   |
| `MESH:('MESH', 'A02.165.410')`                         |              1 | [UBERON:0001066](https://bioregistry.io/UBERON:0001066)                                                                                                                   |
| `MESH:('MESH', 'A14.254.860')`                         |              1 | [UBERON:0001091](https://bioregistry.io/UBERON:0001091)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.834.151.213')`             |              1 | [UBERON:0001092](https://bioregistry.io/UBERON:0001092)                                                                                                                   |
| `MESH:('MESH', 'A14.254.860.425')`                     |              1 | [UBERON:0001098](https://bioregistry.io/UBERON:0001098)                                                                                                                   |
| `MESH:('MESH', 'A01.176')`                             |              1 | [UBERON:0001137](https://bioregistry.io/UBERON:0001137)                                                                                                                   |
| `MESH:('MESH', 'A03.159.183.419')`                     |              1 | [UBERON:0001152](https://bioregistry.io/UBERON:0001152)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.495.209')`                 |              1 | [UBERON:0001153](https://bioregistry.io/UBERON:0001153)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.495.209.290')`             |              1 | [UBERON:0001154](https://bioregistry.io/UBERON:0001154)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.495.356')`                 |              1 | [UBERON:0001155](https://bioregistry.io/UBERON:0001155)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.495.356.668')`             |              1 | [UBERON:0001159](https://bioregistry.io/UBERON:0001159)                                                                                                                   |
| `MESH:('MESH', 'A03.492.766.419')`                     |              1 | [UBERON:0001160](https://bioregistry.io/UBERON:0001160)                                                                                                                   |
| `MESH:('MESH', 'A03.492.766.163')`                     |              1 | [UBERON:0001162](https://bioregistry.io/UBERON:0001162)                                                                                                                   |
| `MESH:('MESH', 'A03.492.766.716')`                     |              1 | [UBERON:0001165](https://bioregistry.io/UBERON:0001165)                                                                                                                   |
| `MESH:('MESH', 'A03.492.766.799')`                     |              1 | [UBERON:0001166](https://bioregistry.io/UBERON:0001166)                                                                                                                   |
| `MESH:('MESH', 'A01.047.025.600.678')`                 |              1 | [UBERON:0001179](https://bioregistry.io/UBERON:0001179)                                                                                                                   |
| `MESH:('MESH', 'A03.492.766.440')`                     |              1 | [UBERON:0001199](https://bioregistry.io/UBERON:0001199)                                                                                                                   |
| `MESH:('MESH', 'A10.549.598')`                         |              1 | [UBERON:0001211](https://bioregistry.io/UBERON:0001211)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.620.270.322')`             |              1 | [UBERON:0001212](https://bioregistry.io/UBERON:0001212)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.369')`                     |              1 | [UBERON:0001242](https://bioregistry.io/UBERON:0001242)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.495.767.288')`             |              1 | [UBERON:0001245](https://bioregistry.io/UBERON:0001245)                                                                                                                   |
| `MESH:('MESH', 'A05.810.161')`                         |              1 | [UBERON:0001255](https://bioregistry.io/UBERON:0001255)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.611.108')`                 |              1 | [UBERON:0001269](https://bioregistry.io/UBERON:0001269)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.611')`                     |              1 | [UBERON:0001272](https://bioregistry.io/UBERON:0001272)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.611.434')`                 |              1 | [UBERON:0001273](https://bioregistry.io/UBERON:0001273)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.611.548')`                 |              1 | [UBERON:0001274](https://bioregistry.io/UBERON:0001274)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.611.781')`                 |              1 | [UBERON:0001275](https://bioregistry.io/UBERON:0001275)                                                                                                                   |
| `MESH:('MESH', 'A05.360.444.849.286')`                 |              1 | [UBERON:0001301](https://bioregistry.io/UBERON:0001301)                                                                                                                   |
| `MESH:('MESH', 'A12.207.268')`                         |              1 | [UBERON:0001359](https://bioregistry.io/UBERON:0001359)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.213.270.548')`     |              1 | [UBERON:0001384](https://bioregistry.io/UBERON:0001384)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.213.863.297')`     |              1 | [UBERON:0001393](https://bioregistry.io/UBERON:0001393)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.087.702')`                 |              1 | [UBERON:0001423](https://bioregistry.io/UBERON:0001423)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.087.911')`                 |              1 | [UBERON:0001424](https://bioregistry.io/UBERON:0001424)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.087.144.650')`             |              1 | [UBERON:0001427](https://bioregistry.io/UBERON:0001427)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.087.144.663')`             |              1 | [UBERON:0001428](https://bioregistry.io/UBERON:0001428)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.087.144')`                 |              1 | [UBERON:0001435](https://bioregistry.io/UBERON:0001435)                                                                                                                   |
| `MESH:('MESH', 'A01.911')`                             |              1 | [UBERON:0001443](https://bioregistry.io/UBERON:0001443)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.500.321')`                 |              1 | [UBERON:0001446](https://bioregistry.io/UBERON:0001446)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.300.710')`                 |              1 | [UBERON:0001447](https://bioregistry.io/UBERON:0001447)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.300.492')`                 |              1 | [UBERON:0001448](https://bioregistry.io/UBERON:0001448)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.300.710.300')`             |              1 | [UBERON:0001450](https://bioregistry.io/UBERON:0001450)                                                                                                                   |
| `MESH:('MESH', 'A02.835.583.959')`                     |              1 | [UBERON:0001491](https://bioregistry.io/UBERON:0001491)                                                                                                                   |
| `MESH:('MESH', 'A08.800.550.700.120.600.150')`         |              1 | [UBERON:0001629](https://bioregistry.io/UBERON:0001629)                                                                                                                   |
| `MESH:('MESH', 'A15.382.520.869')`                     |              1 | [UBERON:0001631](https://bioregistry.io/UBERON:0001631)                                                                                                                   |
| `MESH:('MESH', 'A02.165.639')`                         |              1 | [UBERON:0001706](https://bioregistry.io/UBERON:0001706)                                                                                                                   |
| `MESH:('MESH', 'A08.800.550.700.120.800')`             |              1 | [UBERON:0001727](https://bioregistry.io/UBERON:0001727)                                                                                                                   |
| `MESH:('MESH', 'A03.867.557')`                         |              1 | [UBERON:0001728](https://bioregistry.io/UBERON:0001728)                                                                                                                   |
| `MESH:('MESH', 'A03.867.603')`                         |              1 | [UBERON:0001729](https://bioregistry.io/UBERON:0001729)                                                                                                                   |
| `MESH:('MESH', 'A15.382.520.604.084')`                 |              1 | [UBERON:0001732](https://bioregistry.io/UBERON:0001732)                                                                                                                   |
| `MESH:('MESH', 'A02.165.507.870')`                     |              1 | [UBERON:0001738](https://bioregistry.io/UBERON:0001738)                                                                                                                   |
| `MESH:('MESH', 'A02.165.507')`                         |              1 | [UBERON:0001739](https://bioregistry.io/UBERON:0001739)                                                                                                                   |
| `MESH:('MESH', 'A02.165.507.083')`                     |              1 | [UBERON:0001740](https://bioregistry.io/UBERON:0001740)                                                                                                                   |
| `MESH:('MESH', 'A14.254.900.280')`                     |              1 | [UBERON:0001751](https://bioregistry.io/UBERON:0001751)                                                                                                                   |
| `MESH:('MESH', 'A14.254.900.255')`                     |              1 | [UBERON:0001752](https://bioregistry.io/UBERON:0001752)                                                                                                                   |
| `MESH:('MESH', 'A14.254.646.267')`                     |              1 | [UBERON:0001753](https://bioregistry.io/UBERON:0001753)                                                                                                                   |
| `MESH:('MESH', 'A14.254.900.260')`                     |              1 | [UBERON:0001754](https://bioregistry.io/UBERON:0001754)                                                                                                                   |
| `MESH:('MESH', 'A14.254.900.720.250')`                 |              1 | [UBERON:0001763](https://bioregistry.io/UBERON:0001763)                                                                                                                   |
| `MESH:('MESH', 'A09.371.943')`                         |              1 | [UBERON:0001798](https://bioregistry.io/UBERON:0001798)                                                                                                                   |
| `MESH:('MESH', 'A09.371.192')`                         |              1 | [UBERON:0001811](https://bioregistry.io/UBERON:0001811)                                                                                                                   |
| `MESH:('MESH', 'A14.254.646.480')`                     |              1 | [UBERON:0001828](https://bioregistry.io/UBERON:0001828)                                                                                                                   |
| `MESH:('MESH', 'A12.207.571.678')`                     |              1 | [UBERON:0001845](https://bioregistry.io/UBERON:0001845)                                                                                                                   |
| `MESH:('MESH', 'A12.207.571.324')`                     |              1 | [UBERON:0001852](https://bioregistry.io/UBERON:0001852)                                                                                                                   |
| `MESH:('MESH', 'A02.165.207')`                         |              1 | [UBERON:0001867](https://bioregistry.io/UBERON:0001867)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.213.863')`         |              1 | [UBERON:0001871](https://bioregistry.io/UBERON:0001871)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.213.670')`         |              1 | [UBERON:0001872](https://bioregistry.io/UBERON:0001872)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.105.487.550.184')` |              1 | [UBERON:0001873](https://bioregistry.io/UBERON:0001873)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.105.487.550.784')` |              1 | [UBERON:0001874](https://bioregistry.io/UBERON:0001874)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.105.487.397')`     |              1 | [UBERON:0001875](https://bioregistry.io/UBERON:0001875)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.090')`                 |              1 | [UBERON:0001876](https://bioregistry.io/UBERON:0001876)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.699.400')`             |              1 | [UBERON:0001881](https://bioregistry.io/UBERON:0001881)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.105.683')`         |              1 | [UBERON:0001882](https://bioregistry.io/UBERON:0001882)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.405.200')`             |              1 | [UBERON:0001885](https://bioregistry.io/UBERON:0001885)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385')`                 |              1 | [UBERON:0001894](https://bioregistry.io/UBERON:0001894)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.826')`             |              1 | [UBERON:0001897](https://bioregistry.io/UBERON:0001897)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.482')`                 |              1 | [UBERON:0001898](https://bioregistry.io/UBERON:0001898)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.200')`                 |              1 | [UBERON:0001899](https://bioregistry.io/UBERON:0001899)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.800')`             |              1 | [UBERON:0001900](https://bioregistry.io/UBERON:0001900)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.200.360')`             |              1 | [UBERON:0001904](https://bioregistry.io/UBERON:0001904)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.800.800')`         |              1 | [UBERON:0001906](https://bioregistry.io/UBERON:0001906)                                                                                                                   |
| `MESH:('MESH', 'A13.622')`                             |              1 | [UBERON:0001913](https://bioregistry.io/UBERON:0001913)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.357.342.450')`     |              1 | [UBERON:0001928](https://bioregistry.io/UBERON:0001928)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.357.342.650')`     |              1 | [UBERON:0001929](https://bioregistry.io/UBERON:0001929)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.357.342.400')`     |              1 | [UBERON:0001930](https://bioregistry.io/UBERON:0001930)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.357.352.081')`     |              1 | [UBERON:0001932](https://bioregistry.io/UBERON:0001932)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.357.352.270')`     |              1 | [UBERON:0001934](https://bioregistry.io/UBERON:0001934)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.357.352.953')`     |              1 | [UBERON:0001935](https://bioregistry.io/UBERON:0001935)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.132.659.237.816')`         |              1 | [UBERON:0001945](https://bioregistry.io/UBERON:0001945)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.132.659.237.364')`         |              1 | [UBERON:0001946](https://bioregistry.io/UBERON:0001946)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.132.659.822.642')`         |              1 | [UBERON:0001947](https://bioregistry.io/UBERON:0001947)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.213.420')`         |              1 | [UBERON:0001950](https://bioregistry.io/UBERON:0001950)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.405')`                 |              1 | [UBERON:0001954](https://bioregistry.io/UBERON:0001954)                                                                                                                   |
| `MESH:('MESH', 'A07.231.432.410')`                     |              1 | [UBERON:0001982](https://bioregistry.io/UBERON:0001982)                                                                                                                   |
| `MESH:('MESH', 'A16.759')`                             |              1 | [UBERON:0001987](https://bioregistry.io/UBERON:0001987)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.213.571')`         |              1 | [UBERON:0002021](https://bioregistry.io/UBERON:0002021)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.357.342.625')`     |              1 | [UBERON:0002034](https://bioregistry.io/UBERON:0002034)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.132.659.687')`             |              1 | [UBERON:0002038](https://bioregistry.io/UBERON:0002038)                                                                                                                   |
| `MESH:('MESH', 'A16.254.835')`                         |              1 | [UBERON:0002068](https://bioregistry.io/UBERON:0002068)                                                                                                                   |
| `MESH:('MESH', 'A01.047.025.600.451')`                 |              1 | [UBERON:0002095](https://bioregistry.io/UBERON:0002095)                                                                                                                   |
| `MESH:('MESH', 'A15.382.520.604.713')`                 |              1 | [UBERON:0002106](https://bioregistry.io/UBERON:0002106)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.620')`                     |              1 | [UBERON:0002108](https://bioregistry.io/UBERON:0002108)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.620.270')`                 |              1 | [UBERON:0002114](https://bioregistry.io/UBERON:0002114)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.620.625')`                 |              1 | [UBERON:0002115](https://bioregistry.io/UBERON:0002115)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.620.484')`                 |              1 | [UBERON:0002116](https://bioregistry.io/UBERON:0002116)                                                                                                                   |
| `MESH:('MESH', 'A08.713.810')`                         |              1 | [UBERON:0002139](https://bioregistry.io/UBERON:0002139)                                                                                                                   |
| `MESH:('MESH', 'A06.407.747.608')`                     |              1 | [UBERON:0002196](https://bioregistry.io/UBERON:0002196)                                                                                                                   |
| `MESH:('MESH', 'A06.407.747.734.500')`                 |              1 | [UBERON:0002197](https://bioregistry.io/UBERON:0002197)                                                                                                                   |
| `MESH:('MESH', 'A06.407.747.734')`                     |              1 | [UBERON:0002198](https://bioregistry.io/UBERON:0002198)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.357.362.500')`     |              1 | [UBERON:0002206](https://bioregistry.io/UBERON:0002206)                                                                                                                   |
| `MESH:('MESH', 'A08.713.840')`                         |              1 | [UBERON:0002219](https://bioregistry.io/UBERON:0002219)                                                                                                                   |
| `MESH:('MESH', 'A01.911.800')`                         |              1 | [UBERON:0002224](https://bioregistry.io/UBERON:0002224)                                                                                                                   |
| `MESH:('MESH', 'A09.246.631.246.292.906')`             |              1 | [UBERON:0002233](https://bioregistry.io/UBERON:0002233)                                                                                                                   |
| `MESH:('MESH', 'A04.531.591.940')`                     |              1 | [UBERON:0002255](https://bioregistry.io/UBERON:0002255)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.132.659.237')`             |              1 | [UBERON:0002259](https://bioregistry.io/UBERON:0002259)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.699.573')`             |              1 | [UBERON:0002264](https://bioregistry.io/UBERON:0002264)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.132.659.822.187')`         |              1 | [UBERON:0002289](https://bioregistry.io/UBERON:0002289)                                                                                                                   |
| `MESH:('MESH', 'A16.254.610')`                         |              1 | [UBERON:0002328](https://bioregistry.io/UBERON:0002328)                                                                                                                   |
| `MESH:('MESH', 'A16.254.425.660.750')`                 |              1 | [UBERON:0002329](https://bioregistry.io/UBERON:0002329)                                                                                                                   |
| `MESH:('MESH', 'A16.254.789')`                         |              1 | [UBERON:0002331](https://bioregistry.io/UBERON:0002331)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.362')`             |              1 | [UBERON:0002336](https://bioregistry.io/UBERON:0002336)                                                                                                                   |
| `MESH:('MESH', 'A16.254.600')`                         |              1 | [UBERON:0002342](https://bioregistry.io/UBERON:0002342)                                                                                                                   |
| `MESH:('MESH', 'A01.673')`                             |              1 | [UBERON:0002355](https://bioregistry.io/UBERON:0002355)                                                                                                                   |
| `MESH:('MESH', 'A01.047.025.600')`                     |              1 | [UBERON:0002358](https://bioregistry.io/UBERON:0002358)                                                                                                                   |
| `MESH:('MESH', 'A09.246.397.873')`                     |              1 | [UBERON:0002364](https://bioregistry.io/UBERON:0002364)                                                                                                                   |
| `MESH:('MESH', 'A03.867.603.925')`                     |              1 | [UBERON:0002372](https://bioregistry.io/UBERON:0002372)                                                                                                                   |
| `MESH:('MESH', 'A02.165.507.211')`                     |              1 | [UBERON:0002375](https://bioregistry.io/UBERON:0002375)                                                                                                                   |
| `MESH:('MESH', 'A12.207.630')`                         |              1 | [UBERON:0002391](https://bioregistry.io/UBERON:0002391)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.300.710.780')`             |              1 | [UBERON:0002395](https://bioregistry.io/UBERON:0002395)                                                                                                                   |
| `MESH:('MESH', 'A01.911.800.650')`                     |              1 | [UBERON:0002402](https://bioregistry.io/UBERON:0002402)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.357.300')`         |              1 | [UBERON:0002430](https://bioregistry.io/UBERON:0002430)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.105.487.550')`     |              1 | [UBERON:0002435](https://bioregistry.io/UBERON:0002435)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.500.624')`                 |              1 | [UBERON:0002446](https://bioregistry.io/UBERON:0002446)                                                                                                                   |
| `MESH:('MESH', 'A14.254.900.265')`                     |              1 | [UBERON:0002487](https://bioregistry.io/UBERON:0002487)                                                                                                                   |
| `MESH:('MESH', 'A16.254.160')`                         |              1 | [UBERON:0002539](https://bioregistry.io/UBERON:0002539)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.357.342')`         |              1 | [UBERON:0002550](https://bioregistry.io/UBERON:0002550)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.357.352.870')`     |              1 | [UBERON:0002620](https://bioregistry.io/UBERON:0002620)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.357.342.063')`     |              1 | [UBERON:0002634](https://bioregistry.io/UBERON:0002634)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.750.800')`             |              1 | [UBERON:0002663](https://bioregistry.io/UBERON:0002663)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.132.659.822.820')`         |              1 | [UBERON:0002691](https://bioregistry.io/UBERON:0002691)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.710.225')`             |              1 | [UBERON:0002728](https://bioregistry.io/UBERON:0002728)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.826.701.460')`     |              1 | [UBERON:0002733](https://bioregistry.io/UBERON:0002733)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.826.701.485')`     |              1 | [UBERON:0002736](https://bioregistry.io/UBERON:0002736)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.826.701.490')`     |              1 | [UBERON:0002739](https://bioregistry.io/UBERON:0002739)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.826.701.080')`     |              1 | [UBERON:0002788](https://bioregistry.io/UBERON:0002788)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.710')`                 |              1 | [UBERON:0002973](https://bioregistry.io/UBERON:0002973)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.385.826.701.485.600')` |              1 | [UBERON:0002981](https://bioregistry.io/UBERON:0002981)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.820')`                 |              1 | [UBERON:0003017](https://bioregistry.io/UBERON:0003017)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.132.659.822.595')`         |              1 | [UBERON:0003040](https://bioregistry.io/UBERON:0003040)                                                                                                                   |
| `MESH:('MESH', 'A16.254.650')`                         |              1 | [UBERON:0003062](https://bioregistry.io/UBERON:0003062)                                                                                                                   |
| `MESH:('MESH', 'A16.254.940')`                         |              1 | [UBERON:0003074](https://bioregistry.io/UBERON:0003074)                                                                                                                   |
| `MESH:('MESH', 'A16.254.403.473')`                     |              1 | [UBERON:0003124](https://bioregistry.io/UBERON:0003124)                                                                                                                   |
| `MESH:('MESH', 'A16.631.886')`                         |              1 | [UBERON:0003125](https://bioregistry.io/UBERON:0003125)                                                                                                                   |
| `MESH:('MESH', 'A14.254.860.525')`                     |              1 | [UBERON:0003655](https://bioregistry.io/UBERON:0003655)                                                                                                                   |
| `MESH:('MESH', 'A14.254')`                             |              1 | [UBERON:0003672](https://bioregistry.io/UBERON:0003672)                                                                                                                   |
| `MESH:('MESH', 'A14.254.860.200')`                     |              1 | [UBERON:0003674](https://bioregistry.io/UBERON:0003674)                                                                                                                   |
| `MESH:('MESH', 'A14.254.900.710')`                     |              1 | [UBERON:0003675](https://bioregistry.io/UBERON:0003675)                                                                                                                   |
| `MESH:('MESH', 'A14.254.900.750')`                     |              1 | [UBERON:0003677](https://bioregistry.io/UBERON:0003677)                                                                                                                   |
| `MESH:('MESH', 'A14.254.900.750.700')`                 |              1 | [UBERON:0003678](https://bioregistry.io/UBERON:0003678)                                                                                                                   |
| `MESH:('MESH', 'A01.047.025')`                         |              1 | [UBERON:0003684](https://bioregistry.io/UBERON:0003684)                                                                                                                   |
| `MESH:('MESH', 'A01.047.025.600.573')`                 |              1 | [UBERON:0003688](https://bioregistry.io/UBERON:0003688)                                                                                                                   |
| `MESH:('MESH', 'A01.047.025.750')`                     |              1 | [UBERON:0003693](https://bioregistry.io/UBERON:0003693)                                                                                                                   |
| `MESH:('MESH', 'A02.835.583.345.512')`                 |              1 | [UBERON:0003695](https://bioregistry.io/UBERON:0003695)                                                                                                                   |
| `MESH:('MESH', 'A01.047.050')`                         |              1 | [UBERON:0003697](https://bioregistry.io/UBERON:0003697)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.620.484.612')`             |              1 | [UBERON:0003705](https://bioregistry.io/UBERON:0003705)                                                                                                                   |
| `MESH:('MESH', 'A08.800.550.700.500.500')`             |              1 | [UBERON:0003718](https://bioregistry.io/UBERON:0003718)                                                                                                                   |
| `MESH:('MESH', 'A08.800.550.700.500.300')`             |              1 | [UBERON:0003719](https://bioregistry.io/UBERON:0003719)                                                                                                                   |
| `MESH:('MESH', 'A08.800.550.700.500.700')`             |              1 | [UBERON:0003719](https://bioregistry.io/UBERON:0003719)                                                                                                                   |
| `MESH:('MESH', 'A01.911.800.500')`                     |              1 | [UBERON:0003728](https://bioregistry.io/UBERON:0003728)                                                                                                                   |
| `MESH:('MESH', 'A16.254.570')`                         |              1 | [UBERON:0003890](https://bioregistry.io/UBERON:0003890)                                                                                                                   |
| `MESH:('MESH', 'A16.254.403.147')`                     |              1 | [UBERON:0004340](https://bioregistry.io/UBERON:0004340)                                                                                                                   |
| `MESH:('MESH', 'A16.254.462')`                         |              1 | [UBERON:0004347](https://bioregistry.io/UBERON:0004347)                                                                                                                   |
| `MESH:('MESH', 'A01.378.610.250.149')`                 |              1 | [UBERON:0004454](https://bioregistry.io/UBERON:0004454)                                                                                                                   |
| `MESH:('MESH', 'A13.473.821')`                         |              1 | [UBERON:0004454](https://bioregistry.io/UBERON:0004454)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.132.659.632')`             |              1 | [UBERON:0004684](https://bioregistry.io/UBERON:0004684)                                                                                                                   |
| `MESH:('MESH', 'A16.254.412')`                         |              1 | [UBERON:0004734](https://bioregistry.io/UBERON:0004734)                                                                                                                   |
| `MESH:('MESH', 'A16.254.085.067')`                     |              1 | [UBERON:0004750](https://bioregistry.io/UBERON:0004750)                                                                                                                   |
| `MESH:('MESH', 'A03.159.183.079.300.900')`             |              1 | [UBERON:0004913](https://bioregistry.io/UBERON:0004913)                                                                                                                   |
| `MESH:('MESH', 'A03.159.183.079.300.900.600')`         |              1 | [UBERON:0004915](https://bioregistry.io/UBERON:0004915)                                                                                                                   |
| `MESH:('MESH', 'A14.254.900.720.265')`                 |              1 | [UBERON:0005176](https://bioregistry.io/UBERON:0005176)                                                                                                                   |
| `MESH:('MESH', 'A03.492')`                             |              1 | [UBERON:0005409](https://bioregistry.io/UBERON:0005409)                                                                                                                   |
| `MESH:('MESH', 'A16.254.403')`                         |              1 | [UBERON:0005630](https://bioregistry.io/UBERON:0005630)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.500')`                     |              1 | [UBERON:0005893](https://bioregistry.io/UBERON:0005893)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.300')`                     |              1 | [UBERON:0005899](https://bioregistry.io/UBERON:0005899)                                                                                                                   |
| `MESH:('MESH', 'A08.663.542')`                         |              1 | [UBERON:0006134](https://bioregistry.io/UBERON:0006134)                                                                                                                   |
| `MESH:('MESH', 'A08.663.542.512')`                     |              1 | [UBERON:0006135](https://bioregistry.io/UBERON:0006135)                                                                                                                   |
| `MESH:('MESH', 'A08.663.542.756')`                     |              1 | [UBERON:0006136](https://bioregistry.io/UBERON:0006136)                                                                                                                   |
| `MESH:('MESH', 'A14.254.860.700')`                     |              1 | [UBERON:0007115](https://bioregistry.io/UBERON:0007115)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.500.247.510')`             |              1 | [UBERON:0007119](https://bioregistry.io/UBERON:0007119)                                                                                                                   |
| `MESH:('MESH', 'A14.254.860.150')`                     |              1 | [UBERON:0007120](https://bioregistry.io/UBERON:0007120)                                                                                                                   |
| `MESH:('MESH', 'A16.631.325')`                         |              1 | [UBERON:0007378](https://bioregistry.io/UBERON:0007378)                                                                                                                   |
| `MESH:('MESH', 'A14.254.900.720')`                     |              1 | [UBERON:0008281](https://bioregistry.io/UBERON:0008281)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.105.880.100')`     |              1 | [UBERON:0010010](https://bioregistry.io/UBERON:0010010)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.105')`             |              1 | [UBERON:0010011](https://bioregistry.io/UBERON:0010011)                                                                                                                   |
| `MESH:('MESH', 'A02.835.232.087.535')`                 |              1 | [UBERON:0010544](https://bioregistry.io/UBERON:0010544)                                                                                                                   |
| `MESH:('MESH', 'A02.165.165')`                         |              1 | [UBERON:0010996](https://bioregistry.io/UBERON:0010996)                                                                                                                   |
| `MESH:('MESH', 'A08.663.542.100.700')`                 |              1 | [UBERON:0011929](https://bioregistry.io/UBERON:0011929)                                                                                                                   |
| `MESH:('MESH', 'A14.254.333')`                         |              1 | [UBERON:0012111](https://bioregistry.io/UBERON:0012111)                                                                                                                   |
| `MESH:('MESH', 'A08.800.550.700.500')`                 |              1 | [UBERON:0012449](https://bioregistry.io/UBERON:0012449)                                                                                                                   |
| `MESH:('MESH', 'B01.500.736.215.895.286')`             |              1 | [UBERON:0014856](https://bioregistry.io/UBERON:0014856)                                                                                                                   |
| `MESH:('MESH', 'A01.911.850')`                         |              1 | [UBERON:0016403](https://bioregistry.io/UBERON:0016403)                                                                                                                   |
| `MESH:('MESH', 'A12.300.300')`                         |              1 | [UBERON:0016482](https://bioregistry.io/UBERON:0016482)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.730.885.213.270')`         |              1 | [UBERON:0016525](https://bioregistry.io/UBERON:0016525)                                                                                                                   |
| `MESH:('MESH', 'A14.254.860.525.500')`                 |              1 | [UBERON:0018377](https://bioregistry.io/UBERON:0018377)                                                                                                                   |
| `MESH:('MESH', 'A08.800.550.700.120')`                 |              1 | [UBERON:0018391](https://bioregistry.io/UBERON:0018391)                                                                                                                   |
| `MESH:('MESH', 'A08.800.050.050.925.450')`             |              1 | [UBERON:0035642](https://bioregistry.io/UBERON:0035642)                                                                                                                   |
| `MESH:('MESH', 'A08.800.800.720.450.760.640')`         |              1 | [UBERON:0035652](https://bioregistry.io/UBERON:0035652)                                                                                                                   |
| `MESH:('MESH', 'A08.186.854.253')`                     |              1 | [UBERON:0035803](https://bioregistry.io/UBERON:0035803)                                                                                                                   |
| `MESH:('MESH', 'G06.535.166.330.100')`                 |              1 | [UBERON:0036185](https://bioregistry.io/UBERON:0036185)                                                                                                                   |

## `MGI`: Mouse Genome Informatics

Overall, there were 262 invalid
xrefs to external prefixed with `MGI` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref            |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|--------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MGI:('MGI', 'anna')`    |            104 | [UBERON:0000057](https://bioregistry.io/UBERON:0000057), [UBERON:0000076](https://bioregistry.io/UBERON:0000076), [UBERON:0000114](https://bioregistry.io/UBERON:0000114), [UBERON:0000325](https://bioregistry.io/UBERON:0000325), [UBERON:0000453](https://bioregistry.io/UBERON:0000453), ... |
| `MGI:('MGI', 'csmith')`  |             73 | [UBERON:0000305](https://bioregistry.io/UBERON:0000305), [UBERON:0000995](https://bioregistry.io/UBERON:0000995), [UBERON:0001063](https://bioregistry.io/UBERON:0001063), [UBERON:0001078](https://bioregistry.io/UBERON:0001078), [UBERON:0001111](https://bioregistry.io/UBERON:0001111), ... |
| `MGI:('MGI', 'cwg')`     |             25 | [UBERON:0001013](https://bioregistry.io/UBERON:0001013), [UBERON:0001542](https://bioregistry.io/UBERON:0001542), [UBERON:0001543](https://bioregistry.io/UBERON:0001543), [UBERON:0001728](https://bioregistry.io/UBERON:0001728), [UBERON:0001729](https://bioregistry.io/UBERON:0001729), ... |
| `MGI:('MGI', 'smb')`     |             24 | [UBERON:0000362](https://bioregistry.io/UBERON:0000362), [UBERON:0000396](https://bioregistry.io/UBERON:0000396), [UBERON:0001295](https://bioregistry.io/UBERON:0001295), [UBERON:0001348](https://bioregistry.io/UBERON:0001348), [UBERON:0001772](https://bioregistry.io/UBERON:0001772), ... |
| `MGI:('MGI', 'llw2')`    |             11 | [UBERON:0000388](https://bioregistry.io/UBERON:0000388), [UBERON:0000959](https://bioregistry.io/UBERON:0000959), [UBERON:0001235](https://bioregistry.io/UBERON:0001235), [UBERON:0001236](https://bioregistry.io/UBERON:0001236), [UBERON:0001451](https://bioregistry.io/UBERON:0001451), ... |
| `MGI:('MGI', 'cs')`      |              8 | [UBERON:0018242](https://bioregistry.io/UBERON:0018242), [UBERON:0034932](https://bioregistry.io/UBERON:0034932), [UBERON:0035617](https://bioregistry.io/UBERON:0035617), [UBERON:0035618](https://bioregistry.io/UBERON:0035618), [UBERON:0035619](https://bioregistry.io/UBERON:0035619), ... |
| `MGI:('MGI', 'pvb')`     |              5 | [UBERON:0000087](https://bioregistry.io/UBERON:0000087), [UBERON:0001000](https://bioregistry.io/UBERON:0001000), [UBERON:0001230](https://bioregistry.io/UBERON:0001230), [UBERON:0001301](https://bioregistry.io/UBERON:0001301), [UBERON:0005623](https://bioregistry.io/UBERON:0005623)      |
| `MGI:('MGI', 'rbabiuk')` |              3 | [UBERON:0001213](https://bioregistry.io/UBERON:0001213), [UBERON:0010412](https://bioregistry.io/UBERON:0010412), [UBERON:0014396](https://bioregistry.io/UBERON:0014396)                                                                                                                        |
| `MGI:('MGI', 'monikat')` |              3 | [UBERON:0002115](https://bioregistry.io/UBERON:0002115), [UBERON:0002493](https://bioregistry.io/UBERON:0002493), [UBERON:0002511](https://bioregistry.io/UBERON:0002511)                                                                                                                        |
| `MGI:('MGI', 'hdene')`   |              2 | [UBERON:0001439](https://bioregistry.io/UBERON:0001439), [UBERON:0001832](https://bioregistry.io/UBERON:0001832)                                                                                                                                                                                 |
| `MGI:('MGI', 'brs')`     |              1 | [UBERON:0001296](https://bioregistry.io/UBERON:0001296)                                                                                                                                                                                                                                          |
| `MGI:('MGI', 'Anna')`    |              1 | [UBERON:0005203](https://bioregistry.io/UBERON:0005203)                                                                                                                                                                                                                                          |
| `MGI:('MGI', 'smith')`   |              1 | [UBERON:0035941](https://bioregistry.io/UBERON:0035941)                                                                                                                                                                                                                                          |
| `MGI:('MGI', 'sbello')`  |              1 | [UBERON:0036145](https://bioregistry.io/UBERON:0036145)                                                                                                                                                                                                                                          |

## `MP`: Mammalian Phenotype Ontology

Overall, there were 37 invalid
xrefs to external prefixed with `MP` (standardized to Bioregistry
prefix [`mp`](https://bioregistry.io/mp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref         |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MP:('MP', 'anna')`   |             19 | [UBERON:0001258](https://bioregistry.io/UBERON:0001258), [UBERON:0001338](https://bioregistry.io/UBERON:0001338), [UBERON:0002068](https://bioregistry.io/UBERON:0002068), [UBERON:0002366](https://bioregistry.io/UBERON:0002366), [UBERON:0002366](https://bioregistry.io/UBERON:0002366), ... |
| `MP:('MP', 'MP')`     |             17 | [UBERON:0000173](https://bioregistry.io/UBERON:0000173), [UBERON:0001259](https://bioregistry.io/UBERON:0001259), [UBERON:0001947](https://bioregistry.io/UBERON:0001947), [UBERON:0005452](https://bioregistry.io/UBERON:0005452), [UBERON:0008835](https://bioregistry.io/UBERON:0008835), ... |
| `MP:('MP', '000999')` |              1 | [UBERON:0035922](https://bioregistry.io/UBERON:0035922)                                                                                                                                                                                                                                          |

## `NCIT`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCIT` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref           |   usages_count | usages                                                  |
|-------------------------|----------------|---------------------------------------------------------|
| `NCIT:('NCIT', 'NCIT')` |              1 | [UBERON:0010499](https://bioregistry.io/UBERON:0010499) |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 230 invalid
xrefs to external prefixed with `ncithesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                                                                     |   usages_count | usages                                                                                                           |
|-----------------------------------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `ncithesaurus:('ncithesaurus', 'Corona_Dentis')`                                  |              2 | [UBERON:0003675](https://bioregistry.io/UBERON:0003675), [UBERON:0003675](https://bioregistry.io/UBERON:0003675) |
| `ncithesaurus:('ncithesaurus', 'Shell')`                                          |              2 | [UBERON:0006612](https://bioregistry.io/UBERON:0006612), [UBERON:0006612](https://bioregistry.io/UBERON:0006612) |
| `ncithesaurus:('ncithesaurus', 'Gland_of_the_Third_Eyelid')`                      |              2 | [UBERON:0013230](https://bioregistry.io/UBERON:0013230), [UBERON:0013230](https://bioregistry.io/UBERON:0013230) |
| `ncithesaurus:('ncithesaurus', 'Cerebral_Subcortex')`                             |              1 | [UBERON:0000454](https://bioregistry.io/UBERON:0000454)                                                          |
| `ncithesaurus:('ncithesaurus', 'Ileal_Vein')`                                     |              1 | [UBERON:0001217](https://bioregistry.io/UBERON:0001217)                                                          |
| `ncithesaurus:('ncithesaurus', 'Median_Basilic_Vein')`                            |              1 | [UBERON:0001414](https://bioregistry.io/UBERON:0001414)                                                          |
| `ncithesaurus:('ncithesaurus', 'Pectoralis_Muscle')`                              |              1 | [UBERON:0001495](https://bioregistry.io/UBERON:0001495)                                                          |
| `ncithesaurus:('ncithesaurus', 'Submental_Vein')`                                 |              1 | [UBERON:0001655](https://bioregistry.io/UBERON:0001655)                                                          |
| `ncithesaurus:('ncithesaurus', 'Deep_Temporal_Vein')`                             |              1 | [UBERON:0001661](https://bioregistry.io/UBERON:0001661)                                                          |
| `ncithesaurus:('ncithesaurus', 'Nucleus_of_Diagonal_Band')`                       |              1 | [UBERON:0001879](https://bioregistry.io/UBERON:0001879)                                                          |
| `ncithesaurus:('ncithesaurus', 'Papillary_Dermis')`                               |              1 | [UBERON:0001992](https://bioregistry.io/UBERON:0001992)                                                          |
| `ncithesaurus:('ncithesaurus', 'Thymic_Lobule')`                                  |              1 | [UBERON:0002125](https://bioregistry.io/UBERON:0002125)                                                          |
| `ncithesaurus:('ncithesaurus', 'Endometrial_Stroma')`                             |              1 | [UBERON:0002337](https://bioregistry.io/UBERON:0002337)                                                          |
| `ncithesaurus:('ncithesaurus', 'Sacral_Lymph_Node')`                              |              1 | [UBERON:0002528](https://bioregistry.io/UBERON:0002528)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anterior_Cruciate_Ligament')`                     |              1 | [UBERON:0003671](https://bioregistry.io/UBERON:0003671)                                                          |
| `ncithesaurus:('ncithesaurus', 'Floor_of_the_Mouth')`                             |              1 | [UBERON:0003679](https://bioregistry.io/UBERON:0003679)                                                          |
| `ncithesaurus:('ncithesaurus', 'Omentum')`                                        |              1 | [UBERON:0003688](https://bioregistry.io/UBERON:0003688)                                                          |
| `ncithesaurus:('ncithesaurus', 'Abdominal_Wall')`                                 |              1 | [UBERON:0003697](https://bioregistry.io/UBERON:0003697)                                                          |
| `ncithesaurus:('ncithesaurus', 'Splenic_Vein')`                                   |              1 | [UBERON:0003713](https://bioregistry.io/UBERON:0003713)                                                          |
| `ncithesaurus:('ncithesaurus', 'CA4_Field_of_the_Cornu_Ammonis')`                 |              1 | [UBERON:0003884](https://bioregistry.io/UBERON:0003884)                                                          |
| `ncithesaurus:('ncithesaurus', 'Cortical_Cell_Layer_of_the_Cerebellum')`          |              1 | [UBERON:0004130](https://bioregistry.io/UBERON:0004130)                                                          |
| `ncithesaurus:('ncithesaurus', 'Bowman_s_Membrane')`                              |              1 | [UBERON:0004370](https://bioregistry.io/UBERON:0004370)                                                          |
| `ncithesaurus:('ncithesaurus', 'Gastric_Vein')`                                   |              1 | [UBERON:0004450](https://bioregistry.io/UBERON:0004450)                                                          |
| `ncithesaurus:('ncithesaurus', 'Digital_Vein')`                                   |              1 | [UBERON:0004562](https://bioregistry.io/UBERON:0004562)                                                          |
| `ncithesaurus:('ncithesaurus', 'Rib_3')`                                          |              1 | [UBERON:0004603](https://bioregistry.io/UBERON:0004603)                                                          |
| `ncithesaurus:('ncithesaurus', 'Rib_4')`                                          |              1 | [UBERON:0004604](https://bioregistry.io/UBERON:0004604)                                                          |
| `ncithesaurus:('ncithesaurus', 'Rib_5')`                                          |              1 | [UBERON:0004605](https://bioregistry.io/UBERON:0004605)                                                          |
| `ncithesaurus:('ncithesaurus', 'Rib_6')`                                          |              1 | [UBERON:0004606](https://bioregistry.io/UBERON:0004606)                                                          |
| `ncithesaurus:('ncithesaurus', 'Rib_7')`                                          |              1 | [UBERON:0004607](https://bioregistry.io/UBERON:0004607)                                                          |
| `ncithesaurus:('ncithesaurus', 'Rib_9')`                                          |              1 | [UBERON:0004608](https://bioregistry.io/UBERON:0004608)                                                          |
| `ncithesaurus:('ncithesaurus', 'C3_Vertebra')`                                    |              1 | [UBERON:0004612](https://bioregistry.io/UBERON:0004612)                                                          |
| `ncithesaurus:('ncithesaurus', 'C4_Vertebra')`                                    |              1 | [UBERON:0004613](https://bioregistry.io/UBERON:0004613)                                                          |
| `ncithesaurus:('ncithesaurus', 'C5_Vertebra')`                                    |              1 | [UBERON:0004614](https://bioregistry.io/UBERON:0004614)                                                          |
| `ncithesaurus:('ncithesaurus', 'C6_Vertebra')`                                    |              1 | [UBERON:0004615](https://bioregistry.io/UBERON:0004615)                                                          |
| `ncithesaurus:('ncithesaurus', 'L1_Vertebra')`                                    |              1 | [UBERON:0004617](https://bioregistry.io/UBERON:0004617)                                                          |
| `ncithesaurus:('ncithesaurus', 'L2_Vertebra')`                                    |              1 | [UBERON:0004618](https://bioregistry.io/UBERON:0004618)                                                          |
| `ncithesaurus:('ncithesaurus', 'L3_Vertebra')`                                    |              1 | [UBERON:0004619](https://bioregistry.io/UBERON:0004619)                                                          |
| `ncithesaurus:('ncithesaurus', 'L4_Vertebra')`                                    |              1 | [UBERON:0004620](https://bioregistry.io/UBERON:0004620)                                                          |
| `ncithesaurus:('ncithesaurus', 'L5_Vertebra')`                                    |              1 | [UBERON:0004621](https://bioregistry.io/UBERON:0004621)                                                          |
| `ncithesaurus:('ncithesaurus', 'T1_Vertebra')`                                    |              1 | [UBERON:0004626](https://bioregistry.io/UBERON:0004626)                                                          |
| `ncithesaurus:('ncithesaurus', 'T2_Vertebra')`                                    |              1 | [UBERON:0004627](https://bioregistry.io/UBERON:0004627)                                                          |
| `ncithesaurus:('ncithesaurus', 'T3_Vertebra')`                                    |              1 | [UBERON:0004628](https://bioregistry.io/UBERON:0004628)                                                          |
| `ncithesaurus:('ncithesaurus', 'T4_Vertebra')`                                    |              1 | [UBERON:0004629](https://bioregistry.io/UBERON:0004629)                                                          |
| `ncithesaurus:('ncithesaurus', 'T5_Vertebra')`                                    |              1 | [UBERON:0004630](https://bioregistry.io/UBERON:0004630)                                                          |
| `ncithesaurus:('ncithesaurus', 'T6_Vertebra')`                                    |              1 | [UBERON:0004631](https://bioregistry.io/UBERON:0004631)                                                          |
| `ncithesaurus:('ncithesaurus', 'T7_Vertebra')`                                    |              1 | [UBERON:0004632](https://bioregistry.io/UBERON:0004632)                                                          |
| `ncithesaurus:('ncithesaurus', 'T9_Vertebra')`                                    |              1 | [UBERON:0004633](https://bioregistry.io/UBERON:0004633)                                                          |
| `ncithesaurus:('ncithesaurus', 'T10_Vertebra')`                                   |              1 | [UBERON:0004634](https://bioregistry.io/UBERON:0004634)                                                          |
| `ncithesaurus:('ncithesaurus', 'T11_Vertebra')`                                   |              1 | [UBERON:0004635](https://bioregistry.io/UBERON:0004635)                                                          |
| `ncithesaurus:('ncithesaurus', 'T12_Vertebra')`                                   |              1 | [UBERON:0004636](https://bioregistry.io/UBERON:0004636)                                                          |
| `ncithesaurus:('ncithesaurus', 'Pancreatico-Duodenal_Vein')`                      |              1 | [UBERON:0004690](https://bioregistry.io/UBERON:0004690)                                                          |
| `ncithesaurus:('ncithesaurus', 'Iliac_Vein')`                                     |              1 | [UBERON:0005610](https://bioregistry.io/UBERON:0005610)                                                          |
| `ncithesaurus:('ncithesaurus', 'Aortic_Segment')`                                 |              1 | [UBERON:0005800](https://bioregistry.io/UBERON:0005800)                                                          |
| `ncithesaurus:('ncithesaurus', 'Myelinated_Nerve_Fiber')`                         |              1 | [UBERON:0006135](https://bioregistry.io/UBERON:0006135)                                                          |
| `ncithesaurus:('ncithesaurus', 'Communicating_Artery')`                           |              1 | [UBERON:0006347](https://bioregistry.io/UBERON:0006347)                                                          |
| `ncithesaurus:('ncithesaurus', 'Epigastric_Artery')`                              |              1 | [UBERON:0006349](https://bioregistry.io/UBERON:0006349)                                                          |
| `ncithesaurus:('ncithesaurus', 'Tooth_Cusp')`                                     |              1 | [UBERON:0006844](https://bioregistry.io/UBERON:0006844)                                                          |
| `ncithesaurus:('ncithesaurus', 'Inferior_Thyroid_Artery')`                        |              1 | [UBERON:0007149](https://bioregistry.io/UBERON:0007149)                                                          |
| `ncithesaurus:('ncithesaurus', 'Inferior_Sagittal_Sinus')`                        |              1 | [UBERON:0007152](https://bioregistry.io/UBERON:0007152)                                                          |
| `ncithesaurus:('ncithesaurus', 'Deep_Epigastric_Vein')`                           |              1 | [UBERON:0007154](https://bioregistry.io/UBERON:0007154)                                                          |
| `ncithesaurus:('ncithesaurus', 'Footpad')`                                        |              1 | [UBERON:0008838](https://bioregistry.io/UBERON:0008838)                                                          |
| `ncithesaurus:('ncithesaurus', 'Lung_Lower_Lobe')`                                |              1 | [UBERON:0008949](https://bioregistry.io/UBERON:0008949)                                                          |
| `ncithesaurus:('ncithesaurus', 'Circumflex_Iliac_Artery')`                        |              1 | [UBERON:0009026](https://bioregistry.io/UBERON:0009026)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anal_Membrane')`                                  |              1 | [UBERON:0009195](https://bioregistry.io/UBERON:0009195)                                                          |
| `ncithesaurus:('ncithesaurus', 'Alveolar_Artery')`                                |              1 | [UBERON:0009654](https://bioregistry.io/UBERON:0009654)                                                          |
| `ncithesaurus:('ncithesaurus', 'Auricular_Artery')`                               |              1 | [UBERON:0009655](https://bioregistry.io/UBERON:0009655)                                                          |
| `ncithesaurus:('ncithesaurus', 'Spermatic_Artery')`                               |              1 | [UBERON:0009659](https://bioregistry.io/UBERON:0009659)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anterior_Inferior_Cerebellar_Artery')`            |              1 | [UBERON:0009689](https://bioregistry.io/UBERON:0009689)                                                          |
| `ncithesaurus:('ncithesaurus', 'Lobe')`                                           |              1 | [UBERON:0009912](https://bioregistry.io/UBERON:0009912)                                                          |
| `ncithesaurus:('ncithesaurus', 'Pulmonary_Lobule')`                               |              1 | [UBERON:0010368](https://bioregistry.io/UBERON:0010368)                                                          |
| `ncithesaurus:('ncithesaurus', 'Parametrium')`                                    |              1 | [UBERON:0010391](https://bioregistry.io/UBERON:0010391)                                                          |
| `ncithesaurus:('ncithesaurus', 'Meningeal_Layer_of_the_Dura_Mater')`              |              1 | [UBERON:0010506](https://bioregistry.io/UBERON:0010506)                                                          |
| `ncithesaurus:('ncithesaurus', 'Rib_8')`                                          |              1 | [UBERON:0010757](https://bioregistry.io/UBERON:0010757)                                                          |
| `ncithesaurus:('ncithesaurus', 'T8_Vertebra')`                                    |              1 | [UBERON:0011050](https://bioregistry.io/UBERON:0011050)                                                          |
| `ncithesaurus:('ncithesaurus', 'Inferior_Pancreatico-Duodenal_Vein')`             |              1 | [UBERON:0011383](https://bioregistry.io/UBERON:0011383)                                                          |
| `ncithesaurus:('ncithesaurus', 'Growing_Follicle')`                               |              1 | [UBERON:0012186](https://bioregistry.io/UBERON:0012186)                                                          |
| `ncithesaurus:('ncithesaurus', 'Phrenic_Vein')`                                   |              1 | [UBERON:0012193](https://bioregistry.io/UBERON:0012193)                                                          |
| `ncithesaurus:('ncithesaurus', 'Endocervical_Glandular_Epithelium')`              |              1 | [UBERON:0012252](https://bioregistry.io/UBERON:0012252)                                                          |
| `ncithesaurus:('ncithesaurus', 'Nasal-Associated_Lymphoid_Tissue')`               |              1 | [UBERON:0012330](https://bioregistry.io/UBERON:0012330)                                                          |
| `ncithesaurus:('ncithesaurus', 'Retromolar_Trigone')`                             |              1 | [UBERON:0012376](https://bioregistry.io/UBERON:0012376)                                                          |
| `ncithesaurus:('ncithesaurus', 'Systemic_Vein')`                                  |              1 | [UBERON:0013140](https://bioregistry.io/UBERON:0013140)                                                          |
| `ncithesaurus:('ncithesaurus', 'Choroidal_Artery')`                               |              1 | [UBERON:0013151](https://bioregistry.io/UBERON:0013151)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anterior_Wall_of_the_Tympanum')`                  |              1 | [UBERON:0013173](https://bioregistry.io/UBERON:0013173)                                                          |
| `ncithesaurus:('ncithesaurus', 'Accessory_Lacrimal_Gland')`                       |              1 | [UBERON:0013226](https://bioregistry.io/UBERON:0013226)                                                          |
| `ncithesaurus:('ncithesaurus', 'Upper_Third_of_the_Esophagus')`                   |              1 | [UBERON:0013472](https://bioregistry.io/UBERON:0013472)                                                          |
| `ncithesaurus:('ncithesaurus', 'Lower_Third_of_the_Esophagus')`                   |              1 | [UBERON:0013473](https://bioregistry.io/UBERON:0013473)                                                          |
| `ncithesaurus:('ncithesaurus', 'Middle_Third_of_the_Esophagus')`                  |              1 | [UBERON:0013474](https://bioregistry.io/UBERON:0013474)                                                          |
| `ncithesaurus:('ncithesaurus', 'Epidermal_Ridges')`                               |              1 | [UBERON:0013487](https://bioregistry.io/UBERON:0013487)                                                          |
| `ncithesaurus:('ncithesaurus', 'Lateral_Lobe_of_the_Prostate')`                   |              1 | [UBERON:0013637](https://bioregistry.io/UBERON:0013637)                                                          |
| `ncithesaurus:('ncithesaurus', 'Temporal_Sulcus')`                                |              1 | [UBERON:0014687](https://bioregistry.io/UBERON:0014687)                                                          |
| `ncithesaurus:('ncithesaurus', 'Middle_Temporal_Sulcus')`                         |              1 | [UBERON:0014689](https://bioregistry.io/UBERON:0014689)                                                          |
| `ncithesaurus:('ncithesaurus', 'Interlobular_Duct')`                              |              1 | [UBERON:0014716](https://bioregistry.io/UBERON:0014716)                                                          |
| `ncithesaurus:('ncithesaurus', 'Intercalated_Duct_of_the_Salivary_Gland_System')` |              1 | [UBERON:0014727](https://bioregistry.io/UBERON:0014727)                                                          |
| `ncithesaurus:('ncithesaurus', 'Perivascular_Space')`                             |              1 | [UBERON:0014930](https://bioregistry.io/UBERON:0014930)                                                          |
| `ncithesaurus:('ncithesaurus', 'Hilar_Portion_of_the_Hepatic_Duct')`              |              1 | [UBERON:0015423](https://bioregistry.io/UBERON:0015423)                                                          |
| `ncithesaurus:('ncithesaurus', 'External_Elastic_Membrane')`                      |              1 | [UBERON:0015433](https://bioregistry.io/UBERON:0015433)                                                          |
| `ncithesaurus:('ncithesaurus', 'Tracheobronchial_Lymph_Node')`                    |              1 | [UBERON:0015472](https://bioregistry.io/UBERON:0015472)                                                          |
| `ncithesaurus:('ncithesaurus', 'Body_of_the_Corpus_Callosum')`                    |              1 | [UBERON:0015510](https://bioregistry.io/UBERON:0015510)                                                          |
| `ncithesaurus:('ncithesaurus', 'Hepatic_Lymph_Node')`                             |              1 | [UBERON:0015859](https://bioregistry.io/UBERON:0015859)                                                          |
| `ncithesaurus:('ncithesaurus', 'Gastric_Lymph_Node')`                             |              1 | [UBERON:0015863](https://bioregistry.io/UBERON:0015863)                                                          |
| `ncithesaurus:('ncithesaurus', 'Pelvic_Lymph_Node')`                              |              1 | [UBERON:0015876](https://bioregistry.io/UBERON:0015876)                                                          |
| `ncithesaurus:('ncithesaurus', 'Neurovascular_Bundle')`                           |              1 | [UBERON:0016630](https://bioregistry.io/UBERON:0016630)                                                          |
| `ncithesaurus:('ncithesaurus', 'Internal_Mammary_Vein')`                          |              1 | [UBERON:0017646](https://bioregistry.io/UBERON:0017646)                                                          |
| `ncithesaurus:('ncithesaurus', 'Infraclavicular_Lymph_Node')`                     |              1 | [UBERON:0035162](https://bioregistry.io/UBERON:0035162)                                                          |
| `ncithesaurus:('ncithesaurus', 'Posterior_Surface_of_the_Prostate')`              |              1 | [UBERON:0035165](https://bioregistry.io/UBERON:0035165)                                                          |
| `ncithesaurus:('ncithesaurus', 'Infraclavicular_Region')`                         |              1 | [UBERON:0035168](https://bioregistry.io/UBERON:0035168)                                                          |
| `ncithesaurus:('ncithesaurus', 'Right_Ear')`                                      |              1 | [UBERON:0035174](https://bioregistry.io/UBERON:0035174)                                                          |
| `ncithesaurus:('ncithesaurus', 'Abdominal_Esophagus')`                            |              1 | [UBERON:0035177](https://bioregistry.io/UBERON:0035177)                                                          |
| `ncithesaurus:('ncithesaurus', 'Calcarine_Artery')`                               |              1 | [UBERON:0035183](https://bioregistry.io/UBERON:0035183)                                                          |
| `ncithesaurus:('ncithesaurus', 'Superficial_Lymphatic_Vessel')`                   |              1 | [UBERON:0035198](https://bioregistry.io/UBERON:0035198)                                                          |
| `ncithesaurus:('ncithesaurus', 'Gastrocolic_Ligament')`                           |              1 | [UBERON:0035201](https://bioregistry.io/UBERON:0035201)                                                          |
| `ncithesaurus:('ncithesaurus', 'Occipital_Lymph_Node')`                           |              1 | [UBERON:0035204](https://bioregistry.io/UBERON:0035204)                                                          |
| `ncithesaurus:('ncithesaurus', 'Deep_Peroneal_Nerve')`                            |              1 | [UBERON:0035207](https://bioregistry.io/UBERON:0035207)                                                          |
| `ncithesaurus:('ncithesaurus', 'Base_of_the_Heart')`                              |              1 | [UBERON:0035213](https://bioregistry.io/UBERON:0035213)                                                          |
| `ncithesaurus:('ncithesaurus', 'Internal_Mammary_Lymph_Node')`                    |              1 | [UBERON:0035219](https://bioregistry.io/UBERON:0035219)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anterior_Temporal_Artery')`                       |              1 | [UBERON:0035225](https://bioregistry.io/UBERON:0035225)                                                          |
| `ncithesaurus:('ncithesaurus', 'Superficial_Middle_Cerebral_Vein')`               |              1 | [UBERON:0035231](https://bioregistry.io/UBERON:0035231)                                                          |
| `ncithesaurus:('ncithesaurus', 'Medial_Femoral_Vein')`                            |              1 | [UBERON:0035234](https://bioregistry.io/UBERON:0035234)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anal_Sinus')`                                     |              1 | [UBERON:0035243](https://bioregistry.io/UBERON:0035243)                                                          |
| `ncithesaurus:('ncithesaurus', 'Posterior_External_Jugular_Vein')`                |              1 | [UBERON:0035249](https://bioregistry.io/UBERON:0035249)                                                          |
| `ncithesaurus:('ncithesaurus', 'Left_Subcostal_Vein')`                            |              1 | [UBERON:0035252](https://bioregistry.io/UBERON:0035252)                                                          |
| `ncithesaurus:('ncithesaurus', 'Gallbladder_Neck')`                               |              1 | [UBERON:0035267](https://bioregistry.io/UBERON:0035267)                                                          |
| `ncithesaurus:('ncithesaurus', 'Epigastric_Region')`                              |              1 | [UBERON:0035276](https://bioregistry.io/UBERON:0035276)                                                          |
| `ncithesaurus:('ncithesaurus', 'Supraclavicular_Lymph_Node')`                     |              1 | [UBERON:0035279](https://bioregistry.io/UBERON:0035279)                                                          |
| `ncithesaurus:('ncithesaurus', 'Left_Ear')`                                       |              1 | [UBERON:0035295](https://bioregistry.io/UBERON:0035295)                                                          |
| `ncithesaurus:('ncithesaurus', 'Inferolateral_Surface_of_the_Prostate')`          |              1 | [UBERON:0035310](https://bioregistry.io/UBERON:0035310)                                                          |
| `ncithesaurus:('ncithesaurus', 'Capsule_of_the_Prostate')`                        |              1 | [UBERON:0035316](https://bioregistry.io/UBERON:0035316)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anterior_Median_Fissure_of_Spinal_Cord')`         |              1 | [UBERON:0035319](https://bioregistry.io/UBERON:0035319)                                                          |
| `ncithesaurus:('ncithesaurus', 'Upper-outer_Quadrant_of_the_Breast')`             |              1 | [UBERON:0035328](https://bioregistry.io/UBERON:0035328)                                                          |
| `ncithesaurus:('ncithesaurus', 'Base_of_the_Prostate')`                           |              1 | [UBERON:0035331](https://bioregistry.io/UBERON:0035331)                                                          |
| `ncithesaurus:('ncithesaurus', 'Posterior_Lobe_of_the_Prostate')`                 |              1 | [UBERON:0035341](https://bioregistry.io/UBERON:0035341)                                                          |
| `ncithesaurus:('ncithesaurus', 'Lower-outer_Quadrant_of_the_Breast')`             |              1 | [UBERON:0035365](https://bioregistry.io/UBERON:0035365)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anterior_Surface_of_the_Kidney')`                 |              1 | [UBERON:0035368](https://bioregistry.io/UBERON:0035368)                                                          |
| `ncithesaurus:('ncithesaurus', 'Retroperitoneal_Lymph_Node')`                     |              1 | [UBERON:0035371](https://bioregistry.io/UBERON:0035371)                                                          |
| `ncithesaurus:('ncithesaurus', 'Small_Cardiac_Vein')`                             |              1 | [UBERON:0035374](https://bioregistry.io/UBERON:0035374)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anterior_Cerebral_Artery_Branch')`                |              1 | [UBERON:0035380](https://bioregistry.io/UBERON:0035380)                                                          |
| `ncithesaurus:('ncithesaurus', 'Cystic_Vein')`                                    |              1 | [UBERON:0035392](https://bioregistry.io/UBERON:0035392)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anterior_Longitudinal_Ligament')`                 |              1 | [UBERON:0035419](https://bioregistry.io/UBERON:0035419)                                                          |
| `ncithesaurus:('ncithesaurus', 'Falx_Cerebelli')`                                 |              1 | [UBERON:0035425](https://bioregistry.io/UBERON:0035425)                                                          |
| `ncithesaurus:('ncithesaurus', 'Mediastinal_Pleura')`                             |              1 | [UBERON:0035431](https://bioregistry.io/UBERON:0035431)                                                          |
| `ncithesaurus:('ncithesaurus', 'Right_Suprarenal_Vein')`                          |              1 | [UBERON:0035435](https://bioregistry.io/UBERON:0035435)                                                          |
| `ncithesaurus:('ncithesaurus', 'Apex_of_the_Prostate')`                           |              1 | [UBERON:0035441](https://bioregistry.io/UBERON:0035441)                                                          |
| `ncithesaurus:('ncithesaurus', 'Cervical_Esophagus')`                             |              1 | [UBERON:0035450](https://bioregistry.io/UBERON:0035450)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anterior_Parietal_Artery')`                       |              1 | [UBERON:0035462](https://bioregistry.io/UBERON:0035462)                                                          |
| `ncithesaurus:('ncithesaurus', 'Endometrial_Cavity')`                             |              1 | [UBERON:0035465](https://bioregistry.io/UBERON:0035465)                                                          |
| `ncithesaurus:('ncithesaurus', 'Costophrenic_Angle')`                             |              1 | [UBERON:0035468](https://bioregistry.io/UBERON:0035468)                                                          |
| `ncithesaurus:('ncithesaurus', 'Right_Subcostal_Vein')`                           |              1 | [UBERON:0035474](https://bioregistry.io/UBERON:0035474)                                                          |
| `ncithesaurus:('ncithesaurus', 'Lower-inner_Quadrant_of_the_Breast')`             |              1 | [UBERON:0035477](https://bioregistry.io/UBERON:0035477)                                                          |
| `ncithesaurus:('ncithesaurus', 'Surface_of_the_Prostate')`                        |              1 | [UBERON:0035480](https://bioregistry.io/UBERON:0035480)                                                          |
| `ncithesaurus:('ncithesaurus', 'Left_Suprarenal_Vein')`                           |              1 | [UBERON:0035483](https://bioregistry.io/UBERON:0035483)                                                          |
| `ncithesaurus:('ncithesaurus', 'Lymph_Node_Hilum')`                               |              1 | [UBERON:0035495](https://bioregistry.io/UBERON:0035495)                                                          |
| `ncithesaurus:('ncithesaurus', 'Free_Nerve_Ending')`                              |              1 | [UBERON:0035501](https://bioregistry.io/UBERON:0035501)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anterior_Mediastinal_Lymph_Node')`                |              1 | [UBERON:0035520](https://bioregistry.io/UBERON:0035520)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anterior_Surface_of_the_Prostate')`               |              1 | [UBERON:0035523](https://bioregistry.io/UBERON:0035523)                                                          |
| `ncithesaurus:('ncithesaurus', 'Superficial_Peroneal_Nerve')`                     |              1 | [UBERON:0035526](https://bioregistry.io/UBERON:0035526)                                                          |
| `ncithesaurus:('ncithesaurus', 'Deep_Middle_Cerebral_Vein')`                      |              1 | [UBERON:0035532](https://bioregistry.io/UBERON:0035532)                                                          |
| `ncithesaurus:('ncithesaurus', 'Gallbladder_Body')`                               |              1 | [UBERON:0035536](https://bioregistry.io/UBERON:0035536)                                                          |
| `ncithesaurus:('ncithesaurus', 'Esophageal_Artery')`                              |              1 | [UBERON:0035539](https://bioregistry.io/UBERON:0035539)                                                          |
| `ncithesaurus:('ncithesaurus', 'Upper-inner_Quadrant_of_the_Breast')`             |              1 | [UBERON:0035542](https://bioregistry.io/UBERON:0035542)                                                          |
| `ncithesaurus:('ncithesaurus', 'Deep_Lymphatic_Vessel')`                          |              1 | [UBERON:0035545](https://bioregistry.io/UBERON:0035545)                                                          |
| `ncithesaurus:('ncithesaurus', 'Superficial_Vein')`                               |              1 | [UBERON:0035550](https://bioregistry.io/UBERON:0035550)                                                          |
| `ncithesaurus:('ncithesaurus', 'Deep_Vein')`                                      |              1 | [UBERON:0035552](https://bioregistry.io/UBERON:0035552)                                                          |
| `ncithesaurus:('ncithesaurus', 'Anterior_Facial_Vein')`                           |              1 | [UBERON:0035675](https://bioregistry.io/UBERON:0035675)                                                          |
| `ncithesaurus:('ncithesaurus', 'Subsegmental_Lymph_Node')`                        |              1 | [UBERON:0035765](https://bioregistry.io/UBERON:0035765)                                                          |
| `ncithesaurus:('ncithesaurus', 'Middle_Lobe_of_the_Prostate')`                    |              1 | [UBERON:0035766](https://bioregistry.io/UBERON:0035766)                                                          |
| `ncithesaurus:('ncithesaurus', 'Splenic_Pulp')`                                   |              1 | [UBERON:1000023](https://bioregistry.io/UBERON:1000023)                                                          |
| `ncithesaurus:('ncithesaurus', 'Muscularis_Propria')`                             |              1 | [UBERON:0000381](https://bioregistry.io/UBERON:0000381)                                                          |
| `ncithesaurus:('ncithesaurus', 'Germinal_Layer')`                                 |              1 | [UBERON:0000923](https://bioregistry.io/UBERON:0000923)                                                          |
| `ncithesaurus:('ncithesaurus', 'Pons_Varolii')`                                   |              1 | [UBERON:0000988](https://bioregistry.io/UBERON:0000988)                                                          |
| `ncithesaurus:('ncithesaurus', 'Cortical_Column')`                                |              1 | [UBERON:0001284](https://bioregistry.io/UBERON:0001284)                                                          |
| `ncithesaurus:('ncithesaurus', 'Epencephalon')`                                   |              1 | [UBERON:0001895](https://bioregistry.io/UBERON:0001895)                                                          |
| `ncithesaurus:('ncithesaurus', 'Internal_Geniculate_Body')`                       |              1 | [UBERON:0001927](https://bioregistry.io/UBERON:0001927)                                                          |
| `ncithesaurus:('ncithesaurus', 'Primordium_of_the_Liver')`                        |              1 | [UBERON:0003894](https://bioregistry.io/UBERON:0003894)                                                          |
| `ncithesaurus:('ncithesaurus', 'Pyramid_of_Malpighi')`                            |              1 | [UBERON:0004200](https://bioregistry.io/UBERON:0004200)                                                          |
| `ncithesaurus:('ncithesaurus', 'Pancreatic_Endocrine_Secretion')`                 |              1 | [UBERON:0004792](https://bioregistry.io/UBERON:0004792)                                                          |
| `ncithesaurus:('ncithesaurus', 'Pancreatic_Exocrine_Secretion')`                  |              1 | [UBERON:0004793](https://bioregistry.io/UBERON:0004793)                                                          |
| `ncithesaurus:('ncithesaurus', 'Molecular_layer')`                                |              1 | [UBERON:0005390](https://bioregistry.io/UBERON:0005390)                                                          |
| `ncithesaurus:('ncithesaurus', 'External_Pyramidal_Cell_Layer')`                  |              1 | [UBERON:0005392](https://bioregistry.io/UBERON:0005392)                                                          |
| `ncithesaurus:('ncithesaurus', 'Superior_Constrictor_Muscle')`                    |              1 | [UBERON:0006329](https://bioregistry.io/UBERON:0006329)                                                          |
| `ncithesaurus:('ncithesaurus', 'Lobe_of_the_Right_Lung')`                         |              1 | [UBERON:0006518](https://bioregistry.io/UBERON:0006518)                                                          |
| `ncithesaurus:('ncithesaurus', 'Tunica_Albuginea')`                               |              1 | [UBERON:0006643](https://bioregistry.io/UBERON:0006643)                                                          |
| `ncithesaurus:('ncithesaurus', 'Posterior')`                                      |              1 | [UBERON:0008788](https://bioregistry.io/UBERON:0008788)                                                          |
| `ncithesaurus:('ncithesaurus', 'Paraganglion')`                                   |              1 | [UBERON:0012279](https://bioregistry.io/UBERON:0012279)                                                          |
| `ncithesaurus:('ncithesaurus', 'Gland_of_Wolfring')`                              |              1 | [UBERON:0013224](https://bioregistry.io/UBERON:0013224)                                                          |
| `ncithesaurus:('ncithesaurus', 'Collum_Dentis')`                                  |              1 | [UBERON:0015181](https://bioregistry.io/UBERON:0015181)                                                          |
| `ncithesaurus:('ncithesaurus', 'Ileocecocolic_Lymph_Node')`                       |              1 | [UBERON:0016378](https://bioregistry.io/UBERON:0016378)                                                          |
| `ncithesaurus:('ncithesaurus', 'Adrenal_Gland_Tissue')`                           |              1 | [UBERON:0018303](https://bioregistry.io/UBERON:0018303)                                                          |
| `ncithesaurus:('ncithesaurus', 'Life')`                                           |              1 | [UBERON:0000104](https://bioregistry.io/UBERON:0000104)                                                          |
| `ncithesaurus:('ncithesaurus', 'Developmental_Stage')`                            |              1 | [UBERON:0000105](https://bioregistry.io/UBERON:0000105)                                                          |
| `ncithesaurus:('ncithesaurus', 'Pleural_Effusion')`                               |              1 | [UBERON:0000175](https://bioregistry.io/UBERON:0000175)                                                          |
| `ncithesaurus:('ncithesaurus', 'Pus')`                                            |              1 | [UBERON:0000177](https://bioregistry.io/UBERON:0000177)                                                          |
| `ncithesaurus:('ncithesaurus', 'Atlanto-occipital_Joint-Atlanto')`                |              1 | [UBERON:0000220](https://bioregistry.io/UBERON:0000220)                                                          |
| `ncithesaurus:('ncithesaurus', 'Myelin')`                                         |              1 | [UBERON:0000345](https://bioregistry.io/UBERON:0000345)                                                          |
| `ncithesaurus:('ncithesaurus', 'Whole_Organism')`                                 |              1 | [UBERON:0000468](https://bioregistry.io/UBERON:0000468)                                                          |
| `ncithesaurus:('ncithesaurus', 'Digestive_System')`                               |              1 | [UBERON:0001007](https://bioregistry.io/UBERON:0001007)                                                          |
| `ncithesaurus:('ncithesaurus', 'Pleural_Fluid')`                                  |              1 | [UBERON:0001087](https://bioregistry.io/UBERON:0001087)                                                          |
| `ncithesaurus:('ncithesaurus', 'Heart_Muscle')`                                   |              1 | [UBERON:0001133](https://bioregistry.io/UBERON:0001133)                                                          |
| `ncithesaurus:('ncithesaurus', 'Peritoneal_Fluid')`                               |              1 | [UBERON:0001268](https://bioregistry.io/UBERON:0001268)                                                          |
| `ncithesaurus:('ncithesaurus', 'Phalanx_of_the_Foot')`                            |              1 | [UBERON:0001449](https://bioregistry.io/UBERON:0001449)                                                          |
| `ncithesaurus:('ncithesaurus', 'Transverse_Sinus')`                               |              1 | [UBERON:0001641](https://bioregistry.io/UBERON:0001641)                                                          |
| `ncithesaurus:('ncithesaurus', 'Upper_Jaw')`                                      |              1 | [UBERON:0001709](https://bioregistry.io/UBERON:0001709)                                                          |
| `ncithesaurus:('ncithesaurus', 'Lower_Jaw')`                                      |              1 | [UBERON:0001710](https://bioregistry.io/UBERON:0001710)                                                          |
| `ncithesaurus:('ncithesaurus', 'Insula')`                                         |              1 | [UBERON:0002022](https://bioregistry.io/UBERON:0002022)                                                          |
| `ncithesaurus:('ncithesaurus', 'Spiral_Organ_of_Corti')`                          |              1 | [UBERON:0002227](https://bioregistry.io/UBERON:0002227)                                                          |
| `ncithesaurus:('ncithesaurus', 'Cerebral_Aqueduct')`                              |              1 | [UBERON:0002289](https://bioregistry.io/UBERON:0002289)                                                          |
| `ncithesaurus:('ncithesaurus', 'Striatum')`                                       |              1 | [UBERON:0002435](https://bioregistry.io/UBERON:0002435)                                                          |
| `ncithesaurus:('ncithesaurus', 'Parieto-occipital_Sulcus')`                       |              1 | [UBERON:0002695](https://bioregistry.io/UBERON:0002695)                                                          |
| `ncithesaurus:('ncithesaurus', 'Middle_Frontal_Gyrus')`                           |              1 | [UBERON:0002702](https://bioregistry.io/UBERON:0002702)                                                          |
| `ncithesaurus:('ncithesaurus', 'Collateral_Sulcus')`                              |              1 | [UBERON:0002716](https://bioregistry.io/UBERON:0002716)                                                          |
| `ncithesaurus:('ncithesaurus', 'Inferior_Temporal_Gyrus')`                        |              1 | [UBERON:0002751](https://bioregistry.io/UBERON:0002751)                                                          |
| `ncithesaurus:('ncithesaurus', 'Superior_Temporal_Gyrus')`                        |              1 | [UBERON:0002769](https://bioregistry.io/UBERON:0002769)                                                          |
| `ncithesaurus:('ncithesaurus', 'Middle_Temporal_Gyrus')`                          |              1 | [UBERON:0002771](https://bioregistry.io/UBERON:0002771)                                                          |
| `ncithesaurus:('ncithesaurus', 'Nucleus_of_the_Hypoglossal_Nerve')`               |              1 | [UBERON:0002871](https://bioregistry.io/UBERON:0002871)                                                          |
| `ncithesaurus:('ncithesaurus', 'Inferior_Frontal_Gyrus')`                         |              1 | [UBERON:0002998](https://bioregistry.io/UBERON:0002998)                                                          |
| `ncithesaurus:('ncithesaurus', 'Meckel_Diverticulum')`                            |              1 | [UBERON:0003705](https://bioregistry.io/UBERON:0003705)                                                          |
| `ncithesaurus:('ncithesaurus', 'Dorsal_Thalamus')`                                |              1 | [UBERON:0004703](https://bioregistry.io/UBERON:0004703)                                                          |
| `ncithesaurus:('ncithesaurus', 'Sigmoid_Sinus')`                                  |              1 | [UBERON:0005475](https://bioregistry.io/UBERON:0005475)                                                          |
| `ncithesaurus:('ncithesaurus', 'Straight_Sinus')`                                 |              1 | [UBERON:0005481](https://bioregistry.io/UBERON:0005481)                                                          |
| `ncithesaurus:('ncithesaurus', 'Adrenal_Artery')`                                 |              1 | [UBERON:0005624](https://bioregistry.io/UBERON:0005624)                                                          |
| `ncithesaurus:('ncithesaurus', 'Meconium')`                                       |              1 | [UBERON:0007109](https://bioregistry.io/UBERON:0007109)                                                          |
| `ncithesaurus:('ncithesaurus', 'Vesicular_Gland')`                                |              1 | [UBERON:0007194](https://bioregistry.io/UBERON:0007194)                                                          |
| `ncithesaurus:('ncithesaurus', 'Egg_Yolk')`                                       |              1 | [UBERON:0007378](https://bioregistry.io/UBERON:0007378)                                                          |
| `ncithesaurus:('ncithesaurus', 'Transudate')`                                     |              1 | [UBERON:0007779](https://bioregistry.io/UBERON:0007779)                                                          |
| `ncithesaurus:('ncithesaurus', 'Exudate')`                                        |              1 | [UBERON:0007780](https://bioregistry.io/UBERON:0007780)                                                          |
| `ncithesaurus:('ncithesaurus', 'Egg_White')`                                      |              1 | [UBERON:0008944](https://bioregistry.io/UBERON:0008944)                                                          |
| `ncithesaurus:('ncithesaurus', 'Nucleus_of_the_Solitary_Tract')`                  |              1 | [UBERON:0009050](https://bioregistry.io/UBERON:0009050)                                                          |
| `ncithesaurus:('ncithesaurus', 'Gravid_Uterus')`                                  |              1 | [UBERON:0009098](https://bioregistry.io/UBERON:0009098)                                                          |

## `OBI`: Ontology for Biomedical Investigations

Overall, there were 1 invalid
xrefs to external prefixed with `OBI` (standardized to Bioregistry
prefix [`obi`](https://bioregistry.io/obi)) that
did not match the standard pattern `^\d{7}$`.

| external_xref       |   usages_count | usages                                                  |
|---------------------|----------------|---------------------------------------------------------|
| `OBI:('OBI', 'MC')` |              1 | [UBERON:0012125](https://bioregistry.io/UBERON:0012125) |

## `PBA`: Primate Brain Atlas

Overall, there were 1 invalid
xrefs to external prefixed with `PBA` (standardized to Bioregistry
prefix [`pba`](https://bioregistry.io/pba)) that
did not match the standard pattern `^\d+$`.

| external_xref       |   usages_count | usages                                                  |
|---------------------|----------------|---------------------------------------------------------|
| `PBA:('PBA', 'BN')` |              1 | [UBERON:0010011](https://bioregistry.io/UBERON:0010011) |

## `UBERON`: Uber Anatomy Ontology

Overall, there were 212 invalid
xrefs to external prefixed with `UBERON` (standardized to Bioregistry
prefix [`uberon`](https://bioregistry.io/uberon)) that
did not match the standard pattern `^\d+$`.

| external_xref                    |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|----------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UBERON:('UBERON', 'cjm')`       |            172 | [UBERON:0000004](https://bioregistry.io/UBERON:0000004), [UBERON:0000004](https://bioregistry.io/UBERON:0000004), [UBERON:0000012](https://bioregistry.io/UBERON:0000012), [UBERON:0000172](https://bioregistry.io/UBERON:0000172), [UBERON:0000977](https://bioregistry.io/UBERON:0000977), ... |
| `UBERON:('UBERON', 'EJS')`       |             19 | [UBERON:1000000](https://bioregistry.io/UBERON:1000000), [UBERON:1000001](https://bioregistry.io/UBERON:1000001), [UBERON:1000002](https://bioregistry.io/UBERON:1000002), [UBERON:1000004](https://bioregistry.io/UBERON:1000004), [UBERON:1000005](https://bioregistry.io/UBERON:1000005), ... |
| `UBERON:('UBERON', 'mah')`       |              4 | [UBERON:0001427](https://bioregistry.io/UBERON:0001427), [UBERON:0001428](https://bioregistry.io/UBERON:0001428), [UBERON:0015001](https://bioregistry.io/UBERON:0015001), [UBERON:0015003](https://bioregistry.io/UBERON:0015003)                                                               |
| `UBERON:('UBERON', 'skansa')`    |              4 | [UBERON:0012288](https://bioregistry.io/UBERON:0012288), [UBERON:0012289](https://bioregistry.io/UBERON:0012289), [UBERON:0012290](https://bioregistry.io/UBERON:0012290), [UBERON:0013649](https://bioregistry.io/UBERON:0013649)                                                               |
| `UBERON:('UBERON', 'xp')`        |              3 | [UBERON:0003133](https://bioregistry.io/UBERON:0003133), [UBERON:0003134](https://bioregistry.io/UBERON:0003134), [UBERON:0003135](https://bioregistry.io/UBERON:0003135)                                                                                                                        |
| `UBERON:('UBERON', 'automatic')` |              2 | [UBERON:0004766](https://bioregistry.io/UBERON:0004766), [UBERON:0004766](https://bioregistry.io/UBERON:0004766)                                                                                                                                                                                 |
| `UBERON:('UBERON', 'gg')`        |              2 | [UBERON:0005982](https://bioregistry.io/UBERON:0005982), [UBERON:0006060](https://bioregistry.io/UBERON:0006060)                                                                                                                                                                                 |
| `UBERON:('UBERON', 'md')`        |              2 | [UBERON:0013739](https://bioregistry.io/UBERON:0013739), [UBERON:0013740](https://bioregistry.io/UBERON:0013740)                                                                                                                                                                                 |
| `UBERON:('UBERON', 'gvg')`       |              1 | [UBERON:0005273](https://bioregistry.io/UBERON:0005273)                                                                                                                                                                                                                                          |
| `UBERON:('UBERON', 'nv')`        |              1 | [UBERON:0016928](https://bioregistry.io/UBERON:0016928)                                                                                                                                                                                                                                          |
| `UBERON:('UBERON', 'drseb')`     |              1 | [UBERON:0019207](https://bioregistry.io/UBERON:0019207)                                                                                                                                                                                                                                          |
| `UBERON:('UBERON', 'rc')`        |              1 | [UBERON:0036015](https://bioregistry.io/UBERON:0036015)                                                                                                                                                                                                                                          |

## `WB`: WormBase database of nematode biology

Overall, there were 3 invalid
xrefs to external prefixed with `WB` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref                |   usages_count | usages                                                  |
|------------------------------|----------------|---------------------------------------------------------|
| `WB:('WB', 'Paper00000938')` |              1 | [UBERON:0000934](https://bioregistry.io/UBERON:0000934) |
| `WB:('WB', 'Paper00000653')` |              1 | [UBERON:0000954](https://bioregistry.io/UBERON:0000954) |
| `WB:('WB', 'rynl')`          |              1 | [UBERON:0001016](https://bioregistry.io/UBERON:0001016) |

## `XAO`: Xenopus Anatomy Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `XAO` (standardized to Bioregistry
prefix [`xao`](https://bioregistry.io/xao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref             |   usages_count | usages                                                                                                                                                                                                                             |
|---------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `XAO:('XAO', 'EJS')`      |              4 | [UBERON:0015179](https://bioregistry.io/UBERON:0015179), [UBERON:3010297](https://bioregistry.io/UBERON:3010297), [UBERON:3010299](https://bioregistry.io/UBERON:3010299), [UBERON:4000013](https://bioregistry.io/UBERON:4000013) |
| `XAO:('XAO', 'curator')`  |              2 | [UBERON:3010326](https://bioregistry.io/UBERON:3010326), [UBERON:3010404](https://bioregistry.io/UBERON:3010404)                                                                                                                   |
| `XAO:('XAO', 'curators')` |              1 | [UBERON:0009500](https://bioregistry.io/UBERON:0009500)                                                                                                                                                                            |

## `ZFA`: Zebrafish anatomy and development ontology

Overall, there were 14 invalid
xrefs to external prefixed with `ZFA` (standardized to Bioregistry
prefix [`zfa`](https://bioregistry.io/zfa)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                      |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFA:('ZFA', 'curator')`           |              9 | [UBERON:0008229](https://bioregistry.io/UBERON:0008229), [UBERON:0014371](https://bioregistry.io/UBERON:0014371), [UBERON:0014903](https://bioregistry.io/UBERON:0014903), [UBERON:0018549](https://bioregistry.io/UBERON:0018549), [UBERON:2000120](https://bioregistry.io/UBERON:2000120), ... |
| `ZFA:('ZFA', 'CVS')`               |              2 | [UBERON:0016499](https://bioregistry.io/UBERON:0016499), [UBERON:0018674](https://bioregistry.io/UBERON:0018674)                                                                                                                                                                                 |
| `ZFA:('ZFA', 'yb')`                |              1 | [UBERON:0002539](https://bioregistry.io/UBERON:0002539)                                                                                                                                                                                                                                          |
| `ZFA:('ZFA', 'YMB')`               |              1 | [UBERON:0016499](https://bioregistry.io/UBERON:0016499)                                                                                                                                                                                                                                          |
| `ZFA:('ZFA', 'ZDB-PUB-060323-12')` |              1 | [UBERON:2005245](https://bioregistry.io/UBERON:2005245)                                                                                                                                                                                                                                          |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 521 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref                |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:('ZFIN', 'curator')`   |            516 | [UBERON:0000007](https://bioregistry.io/UBERON:0000007), [UBERON:0000966](https://bioregistry.io/UBERON:0000966), [UBERON:0000991](https://bioregistry.io/UBERON:0000991), [UBERON:0001016](https://bioregistry.io/UBERON:0001016), [UBERON:0001081](https://bioregistry.io/UBERON:0001081), ... |
| `ZFIN:('ZFIN', 'Curator')`   |              2 | [UBERON:0005817](https://bioregistry.io/UBERON:0005817), [UBERON:2005210](https://bioregistry.io/UBERON:2005210)                                                                                                                                                                                 |
| `ZFIN:('ZFIN', 'yb')`        |              1 | [UBERON:0003066](https://bioregistry.io/UBERON:0003066)                                                                                                                                                                                                                                          |
| `ZFIN:('ZFIN', '090511-18')` |              1 | [UBERON:2002145](https://bioregistry.io/UBERON:2002145)                                                                                                                                                                                                                                          |
| `ZFIN:('ZFIN', 'CVS')`       |              1 | [UBERON:2005265](https://bioregistry.io/UBERON:2005265)                                                                                                                                                                                                                                          |

## `zfin`: Zebrafish Information Network Gene

Overall, there were 1 invalid
xrefs to external prefixed with `zfin` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref              |   usages_count | usages                                                  |
|----------------------------|----------------|---------------------------------------------------------|
| `zfin:('zfin', 'curator')` |              1 | [UBERON:0008911](https://bioregistry.io/UBERON:0008911) |

