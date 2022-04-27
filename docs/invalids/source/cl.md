# cl

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `cl`. See the [GitHub repository](https://github.com/obophenotype/cell-ontology).


## `BTO`: BRENDA tissue / enzyme source

Overall, there were 1 invalid
xrefs to external prefixed with `BTO` (standardized to Bioregistry
prefix [`bto`](https://bioregistry.io/bto)) that
did not match the standard pattern `^\d{7}$`.

| external_xref           |   usages_count | usages                                                  |
|-------------------------|----------------|---------------------------------------------------------|
| `BTO:('BTO', '000125')` |              1 | [CL:1000398](http://purl.obolibrary.org/obo/CL_1000398) |

## `CL`: Cell Ontology

Overall, there were 22 invalid
xrefs to external prefixed with `CL` (standardized to Bioregistry
prefix [`cl`](https://bioregistry.io/cl)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                                      |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CL:('CL', 'CVS')`                                 |             16 | [CL:0000212](http://purl.obolibrary.org/obo/CL_0000212), [CL:0005000](http://purl.obolibrary.org/obo/CL_0005000), [CL:0005001](http://purl.obolibrary.org/obo/CL_0005001), [CL:0005002](http://purl.obolibrary.org/obo/CL_0005002), [CL:0005003](http://purl.obolibrary.org/obo/CL_0005003), ... |
| `CL:('CL', 'MAH')`                                 |              3 | [CL:0007007](http://purl.obolibrary.org/obo/CL_0007007), [CL:0007008](http://purl.obolibrary.org/obo/CL_0007008), [CL:0007011](http://purl.obolibrary.org/obo/CL_0007011)                                                                                                                        |
| `CL:('CL', 'curator')`                             |              1 | [CL:0005018](http://purl.obolibrary.org/obo/CL_0005018)                                                                                                                                                                                                                                          |
| `CL:('CL', 'patterns/cellPartOfAnatomicalEntity')` |              1 | [CL:0011030](http://purl.obolibrary.org/obo/CL_0011030)                                                                                                                                                                                                                                          |
| `CL:('CL', 'cjm')`                                 |              1 | [CL:1000742](http://purl.obolibrary.org/obo/CL_1000742)                                                                                                                                                                                                                                          |

## `DOI`: Digital Object Identifier

Overall, there were 1 invalid
xrefs to external prefixed with `DOI` (standardized to Bioregistry
prefix [`doi`](https://bioregistry.io/doi)) that
did not match the standard pattern `^(doi\:)?\d{2}\.\d{4}.*$`.

| external_xref                                          |   usages_count | usages                                                  |
|--------------------------------------------------------|----------------|---------------------------------------------------------|
| `DOI:('DOI', 'https://doi.org/10.1378/chest.12-2762')` |              1 | [CL:0000158](http://purl.obolibrary.org/obo/CL_0000158) |

## `FB`: FlyBase Gene

Overall, there were 25 invalid
xrefs to external prefixed with `FB` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref     |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FB:('FB', 'ma')` |             25 | [CL:0000004](http://purl.obolibrary.org/obo/CL_0000004), [CL:0000063](http://purl.obolibrary.org/obo/CL_0000063), [CL:0000066](http://purl.obolibrary.org/obo/CL_0000066), [CL:0000134](http://purl.obolibrary.org/obo/CL_0000134), [CL:0000144](http://purl.obolibrary.org/obo/CL_0000144), ... |

## `Flybase`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `Flybase` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref                |   usages_count | usages                                                  |
|------------------------------|----------------|---------------------------------------------------------|
| `Flybase:('Flybase', 'dsj')` |              1 | [CL:0000362](http://purl.obolibrary.org/obo/CL_0000362) |

## `FlyBase`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `FlyBase` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref               |   usages_count | usages                                                  |
|-----------------------------|----------------|---------------------------------------------------------|
| `FlyBase:('FlyBase', 'ds')` |              1 | [CL:0000463](http://purl.obolibrary.org/obo/CL_0000463) |

## `GC`: Genetic Code

Overall, there were 1 invalid
xrefs to external prefixed with `GC` (standardized to Bioregistry
prefix [`gc`](https://bioregistry.io/gc)) that
did not match the standard pattern `^\d+$`.

| external_xref      |   usages_count | usages                                                  |
|--------------------|----------------|---------------------------------------------------------|
| `GC:('GC', 'tfm')` |              1 | [CL:0002597](http://purl.obolibrary.org/obo/CL_0002597) |

## `GO`: Gene Ontology

Overall, there were 17 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref      |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|--------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:('GO', 'tfm')` |             16 | [CL:0000478](http://purl.obolibrary.org/obo/CL_0000478), [CL:0000479](http://purl.obolibrary.org/obo/CL_0000479), [CL:0000480](http://purl.obolibrary.org/obo/CL_0000480), [CL:0000481](http://purl.obolibrary.org/obo/CL_0000481), [CL:0000482](http://purl.obolibrary.org/obo/CL_0000482), ... |
| `GO:('GO', 'cvs')` |              1 | [CL:0005008](http://purl.obolibrary.org/obo/CL_0005008)                                                                                                                                                                                                                                          |

## `HPA`: Human Protein Atlas tissue profile information

Overall, there were 7 invalid
xrefs to external prefixed with `HPA` (standardized to Bioregistry
prefix [`hpa`](https://bioregistry.io/hpa)) that
did not match the standard pattern `^ENSG\d{11}$`.

| external_xref           |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HPA:('HPA', 'HPA')`    |              6 | [CL:1001586](http://purl.obolibrary.org/obo/CL_1001586), [CL:1001591](http://purl.obolibrary.org/obo/CL_1001591), [CL:1001593](http://purl.obolibrary.org/obo/CL_1001593), [CL:1001596](http://purl.obolibrary.org/obo/CL_1001596), [CL:1001599](http://purl.obolibrary.org/obo/CL_1001599), ... |
| `HPA:('HPA', 'Breast')` |              1 | [CL:1001583](http://purl.obolibrary.org/obo/CL_1001583)                                                                                                                                                                                                                                          |

## `MA`: Mouse adult gross anatomy

Overall, there were 4 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
prefix [`ma`](https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref     |   usages_count | usages                                                                                                                                                                                                                             |
|-------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MA:('MA', 'ma')` |              4 | [CL:0000362](http://purl.obolibrary.org/obo/CL_0000362), [CL:0000724](http://purl.obolibrary.org/obo/CL_0000724), [CL:0000730](http://purl.obolibrary.org/obo/CL_0000730), [CL:0000731](http://purl.obolibrary.org/obo/CL_0000731) |

## `MESH`: Medical Subject Headings

Overall, there were 101 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                                          |   usages_count | usages                                                                                                                                                                    |
|--------------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MESH:('MESH', 'A05.360.319.114.630.278.400')`         |              3 | [CL:0000175](http://purl.obolibrary.org/obo/CL_0000175), [CL:0000590](http://purl.obolibrary.org/obo/CL_0000590), [CL:0000592](http://purl.obolibrary.org/obo/CL_0000592) |
| `MESH:('MESH', 'A08.637')`                             |              2 | [CL:0000125](http://purl.obolibrary.org/obo/CL_0000125), [CL:0000243](http://purl.obolibrary.org/obo/CL_0000243)                                                          |
| `MESH:('MESH', 'A11.329.372.300')`                     |              2 | [CL:0002150](http://purl.obolibrary.org/obo/CL_0002150), [CL:0002150](http://purl.obolibrary.org/obo/CL_0002150)                                                          |
| `MESH:('MESH', 'A02.633.565.700')`                     |              2 | [CL:0002211](http://purl.obolibrary.org/obo/CL_0002211), [CL:0002211](http://purl.obolibrary.org/obo/CL_0002211)                                                          |
| `MESH:('MESH', 'A05.360.490.890.880')`                 |              1 | [CL:0000017](http://purl.obolibrary.org/obo/CL_0000017)                                                                                                                   |
| `MESH:('MESH', 'A05.360.490.890.860')`                 |              1 | [CL:0000018](http://purl.obolibrary.org/obo/CL_0000018)                                                                                                                   |
| `MESH:('MESH', 'A05.360.490.890')`                     |              1 | [CL:0000019](http://purl.obolibrary.org/obo/CL_0000019)                                                                                                                   |
| `MESH:('MESH', 'A05.360.490.890.900')`                 |              1 | [CL:0000020](http://purl.obolibrary.org/obo/CL_0000020)                                                                                                                   |
| `MESH:('MESH', 'A11.872')`                             |              1 | [CL:0000034](http://purl.obolibrary.org/obo/CL_0000034)                                                                                                                   |
| `MESH:('MESH', 'A11.635')`                             |              1 | [CL:0000056](http://purl.obolibrary.org/obo/CL_0000056)                                                                                                                   |
| `MESH:('MESH', 'A11.329.228')`                         |              1 | [CL:0000057](http://purl.obolibrary.org/obo/CL_0000057)                                                                                                                   |
| `MESH:('MESH', 'A11.436.107')`                         |              1 | [CL:0000059](http://purl.obolibrary.org/obo/CL_0000059)                                                                                                                   |
| `MESH:('MESH', 'A11.329.629')`                         |              1 | [CL:0000062](http://purl.obolibrary.org/obo/CL_0000062)                                                                                                                   |
| `MESH:('MESH', 'A11.436')`                             |              1 | [CL:0000066](http://purl.obolibrary.org/obo/CL_0000066)                                                                                                                   |
| `MESH:('MESH', 'A11.329.372.588')`                     |              1 | [CL:0000091](http://purl.obolibrary.org/obo/CL_0000091)                                                                                                                   |
| `MESH:('MESH', 'A11.118.637.415')`                     |              1 | [CL:0000094](http://purl.obolibrary.org/obo/CL_0000094)                                                                                                                   |
| `MESH:('MESH', 'A11.118.637.415.583')`                 |              1 | [CL:0000096](http://purl.obolibrary.org/obo/CL_0000096)                                                                                                                   |
| `MESH:('MESH', 'A11.329.427')`                         |              1 | [CL:0000097](http://purl.obolibrary.org/obo/CL_0000097)                                                                                                                   |
| `MESH:('MESH', 'A08.663.358')`                         |              1 | [CL:0000099](http://purl.obolibrary.org/obo/CL_0000099)                                                                                                                   |
| `MESH:('MESH', 'A08.663.655.500')`                     |              1 | [CL:0000100](http://purl.obolibrary.org/obo/CL_0000100)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.132.810.428.200.212.600')` |              1 | [CL:0000121](http://purl.obolibrary.org/obo/CL_0000121)                                                                                                                   |
| `MESH:('MESH', 'A08.637.200')`                         |              1 | [CL:0000127](http://purl.obolibrary.org/obo/CL_0000127)                                                                                                                   |
| `MESH:('MESH', 'A08.637.600')`                         |              1 | [CL:0000128](http://purl.obolibrary.org/obo/CL_0000128)                                                                                                                   |
| `MESH:('MESH', 'A09.371.060.067.31')`                  |              1 | [CL:0000132](http://purl.obolibrary.org/obo/CL_0000132)                                                                                                                   |
| `MESH:('MESH', 'A11.329.114')`                         |              1 | [CL:0000136](http://purl.obolibrary.org/obo/CL_0000136)                                                                                                                   |
| `MESH:('MESH', 'A11.329.629.500')`                     |              1 | [CL:0000137](http://purl.obolibrary.org/obo/CL_0000137)                                                                                                                   |
| `MESH:('MESH', 'A11.329.171')`                         |              1 | [CL:0000138](http://purl.obolibrary.org/obo/CL_0000138)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.369.320')`                 |              1 | [CL:0000160](http://purl.obolibrary.org/obo/CL_0000160)                                                                                                                   |
| `MESH:('MESH', 'A06.407')`                             |              1 | [CL:0000163](http://purl.obolibrary.org/obo/CL_0000163)                                                                                                                   |
| `MESH:('MESH', 'A06.688')`                             |              1 | [CL:0000165](http://purl.obolibrary.org/obo/CL_0000165)                                                                                                                   |
| `MESH:('MESH', 'A06.224.161')`                         |              1 | [CL:0000166](http://purl.obolibrary.org/obo/CL_0000166)                                                                                                                   |
| `MESH:('MESH', 'A11.436.348')`                         |              1 | [CL:0000182](http://purl.obolibrary.org/obo/CL_0000182)                                                                                                                   |
| `MESH:('MESH', 'A11.620')`                             |              1 | [CL:0000187](http://purl.obolibrary.org/obo/CL_0000187)                                                                                                                   |
| `MESH:('MESH', 'A11.620.520')`                         |              1 | [CL:0000192](http://purl.obolibrary.org/obo/CL_0000192)                                                                                                                   |
| `MESH:('MESH', 'A11.620.500')`                         |              1 | [CL:0000193](http://purl.obolibrary.org/obo/CL_0000193)                                                                                                                   |
| `MESH:('MESH', 'A08.800.550.700.650')`                 |              1 | [CL:0000198](http://purl.obolibrary.org/obo/CL_0000198)                                                                                                                   |
| `MESH:('MESH', 'A08.800.550.700.500')`                 |              1 | [CL:0000199](http://purl.obolibrary.org/obo/CL_0000199)                                                                                                                   |
| `MESH:('MESH', 'A08.663.650.250')`                     |              1 | [CL:0000202](http://purl.obolibrary.org/obo/CL_0000202)                                                                                                                   |
| `MESH:('MESH', 'A08.800.550.700.840')`                 |              1 | [CL:0000205](http://purl.obolibrary.org/obo/CL_0000205)                                                                                                                   |
| `MESH:('MESH', 'A08.800.550.700.120')`                 |              1 | [CL:0000206](http://purl.obolibrary.org/obo/CL_0000206)                                                                                                                   |
| `MESH:('MESH', 'A08.663.650.650')`                     |              1 | [CL:0000210](http://purl.obolibrary.org/obo/CL_0000210)                                                                                                                   |
| `MESH:('MESH', 'A05.360.444.849.789')`                 |              1 | [CL:0000216](http://purl.obolibrary.org/obo/CL_0000216)                                                                                                                   |
| `MESH:('MESH', 'A08.637.800')`                         |              1 | [CL:0000218](http://purl.obolibrary.org/obo/CL_0000218)                                                                                                                   |
| `MESH:('MESH', 'A16.254.425.273')`                     |              1 | [CL:0000221](http://purl.obolibrary.org/obo/CL_0000221)                                                                                                                   |
| `MESH:('MESH', 'A16.254.425.660')`                     |              1 | [CL:0000222](http://purl.obolibrary.org/obo/CL_0000222)                                                                                                                   |
| `MESH:('MESH', 'A16.254.425.407')`                     |              1 | [CL:0000223](http://purl.obolibrary.org/obo/CL_0000223)                                                                                                                   |
| `MESH:('MESH', 'A11.118.290')`                         |              1 | [CL:0000232](http://purl.obolibrary.org/obo/CL_0000232)                                                                                                                   |
| `MESH:('MESH', 'A11.118.188')`                         |              1 | [CL:0000233](http://purl.obolibrary.org/obo/CL_0000233)                                                                                                                   |
| `MESH:('MESH', 'A08.800.550.700.500.425')`             |              1 | [CL:0000242](http://purl.obolibrary.org/obo/CL_0000242)                                                                                                                   |
| `MESH:('MESH', 'A11.436.397')`                         |              1 | [CL:0000312](http://purl.obolibrary.org/obo/CL_0000312)                                                                                                                   |
| `MESH:('MESH', 'A12.200.882')`                         |              1 | [CL:0000315](http://purl.obolibrary.org/obo/CL_0000315)                                                                                                                   |
| `MESH:('MESH', 'A12.200.702')`                         |              1 | [CL:0000317](http://purl.obolibrary.org/obo/CL_0000317)                                                                                                                   |
| `MESH:('MESH', 'A12.200.849')`                         |              1 | [CL:0000318](http://purl.obolibrary.org/obo/CL_0000318)                                                                                                                   |
| `MESH:('MESH', 'A16.254.600')`                         |              1 | [CL:0000333](http://purl.obolibrary.org/obo/CL_0000333)                                                                                                                   |
| `MESH:('MESH', 'A11.936')`                             |              1 | [CL:0000351](http://purl.obolibrary.org/obo/CL_0000351)                                                                                                                   |
| `MESH:('MESH', 'A11.104')`                             |              1 | [CL:0000353](http://purl.obolibrary.org/obo/CL_0000353)                                                                                                                   |
| `MESH:('MESH', 'A16.254.270.550')`                     |              1 | [CL:0000360](http://purl.obolibrary.org/obo/CL_0000360)                                                                                                                   |
| `MESH:('MESH', 'A16.254.412')`                         |              1 | [CL:0000361](http://purl.obolibrary.org/obo/CL_0000361)                                                                                                                   |
| `MESH:('MESH', 'A11.329.114.500')`                     |              1 | [CL:0000448](http://purl.obolibrary.org/obo/CL_0000448)                                                                                                                   |
| `MESH:('MESH', 'A10.165.114.322')`                     |              1 | [CL:0000449](http://purl.obolibrary.org/obo/CL_0000449)                                                                                                                   |
| `MESH:('MESH', 'A11.118.637.555.567.569.200.400')`     |              1 | [CL:0000492](http://purl.obolibrary.org/obo/CL_0000492)                                                                                                                   |
| `MESH:('MESH', 'A11.329.830')`                         |              1 | [CL:0000499](http://purl.obolibrary.org/obo/CL_0000499)                                                                                                                   |
| `MESH:('MESH', 'A05.360.319.114.630.535.200')`         |              1 | [CL:0000501](http://purl.obolibrary.org/obo/CL_0000501)                                                                                                                   |
| `MESH:('MESH', 'A03.492.766.440.175')`                 |              1 | [CL:0000502](http://purl.obolibrary.org/obo/CL_0000502)                                                                                                                   |
| `MESH:('MESH', 'A05.360.319.114.630.535.400')`         |              1 | [CL:0000503](http://purl.obolibrary.org/obo/CL_0000503)                                                                                                                   |
| `MESH:('MESH', 'A06.224.365')`                         |              1 | [CL:0000504](http://purl.obolibrary.org/obo/CL_0000504)                                                                                                                   |
| `MESH:('MESH', 'A03.492.766.440.300')`                 |              1 | [CL:0000508](http://purl.obolibrary.org/obo/CL_0000508)                                                                                                                   |
| `MESH:('MESH', 'A03.492.411.369.700')`                 |              1 | [CL:0000510](http://purl.obolibrary.org/obo/CL_0000510)                                                                                                                   |
| `MESH:('MESH', 'A11.635.470')`                         |              1 | [CL:0000513](http://purl.obolibrary.org/obo/CL_0000513)                                                                                                                   |
| `MESH:('MESH', 'A11.635.510')`                         |              1 | [CL:0000514](http://purl.obolibrary.org/obo/CL_0000514)                                                                                                                   |
| `MESH:('MESH', 'A08.340.685')`                         |              1 | [CL:0000516](http://purl.obolibrary.org/obo/CL_0000516)                                                                                                                   |
| `MESH:('MESH', 'A11.868')`                             |              1 | [CL:0000524](http://purl.obolibrary.org/obo/CL_0000524)                                                                                                                   |
| `MESH:('MESH', 'A08.663.650')`                         |              1 | [CL:0000526](http://purl.obolibrary.org/obo/CL_0000526)                                                                                                                   |
| `MESH:('MESH', 'A08.663.655')`                         |              1 | [CL:0000527](http://purl.obolibrary.org/obo/CL_0000527)                                                                                                                   |
| `MESH:('MESH', 'A08.663.748')`                         |              1 | [CL:0000528](http://purl.obolibrary.org/obo/CL_0000528)                                                                                                                   |
| `MESH:('MESH', 'A08.663')`                             |              1 | [CL:0000540](http://purl.obolibrary.org/obo/CL_0000540)                                                                                                                   |
| `MESH:('MESH', 'A11.118.290.350.200')`                 |              1 | [CL:0000547](http://purl.obolibrary.org/obo/CL_0000547)                                                                                                                   |
| `MESH:('MESH', 'A08.663.358.050')`                     |              1 | [CL:0000561](http://purl.obolibrary.org/obo/CL_0000561)                                                                                                                   |
| `MESH:('MESH', 'A11.070')`                             |              1 | [CL:0000568](http://purl.obolibrary.org/obo/CL_0000568)                                                                                                                   |
| `MESH:('MESH', 'A08.663.650.650.670.100')`             |              1 | [CL:0000573](http://purl.obolibrary.org/obo/CL_0000573)                                                                                                                   |
| `MESH:('MESH', 'A11.118.637.555.652')`                 |              1 | [CL:0000576](http://purl.obolibrary.org/obo/CL_0000576)                                                                                                                   |
| `MESH:('MESH', 'A03.492.766.440.250')`                 |              1 | [CL:0000577](http://purl.obolibrary.org/obo/CL_0000577)                                                                                                                   |
| `MESH:('MESH', 'A11.329.372.630')`                     |              1 | [CL:0000581](http://purl.obolibrary.org/obo/CL_0000581)                                                                                                                   |
| `MESH:('MESH', 'A11.329.372.600')`                     |              1 | [CL:0000583](http://purl.obolibrary.org/obo/CL_0000583)                                                                                                                   |
| `MESH:('MESH', 'A05.360.490')`                         |              1 | [CL:0000586](http://purl.obolibrary.org/obo/CL_0000586)                                                                                                                   |
| `MESH:('MESH', 'A11.329.679')`                         |              1 | [CL:0000588](http://purl.obolibrary.org/obo/CL_0000588)                                                                                                                   |
| `MESH:('MESH', 'A08.663.650.250.250')`                 |              1 | [CL:0000589](http://purl.obolibrary.org/obo/CL_0000589)                                                                                                                   |
| `MESH:('MESH', 'A11.635.500.700')`                     |              1 | [CL:0000594](http://purl.obolibrary.org/obo/CL_0000594)                                                                                                                   |
| `MESH:('MESH', 'A08.186.211.577.405.700')`             |              1 | [CL:0000598](http://purl.obolibrary.org/obo/CL_0000598)                                                                                                                   |
| `MESH:('MESH', 'A08.663.650.250.315')`                 |              1 | [CL:0000601](http://purl.obolibrary.org/obo/CL_0000601)                                                                                                                   |
| `MESH:('MESH', 'A08.800.050.800.900.700')`             |              1 | [CL:0000602](http://purl.obolibrary.org/obo/CL_0000602)                                                                                                                   |
| `MESH:('MESH', 'A08.663.650.650.670.650')`             |              1 | [CL:0000604](http://purl.obolibrary.org/obo/CL_0000604)                                                                                                                   |
| `MESH:('MESH', 'A08.663.650.250.380')`                 |              1 | [CL:0000609](http://purl.obolibrary.org/obo/CL_0000609)                                                                                                                   |
| `MESH:('MESH', 'A09.246.631.246.577.543')`             |              1 | [CL:0000631](http://purl.obolibrary.org/obo/CL_0000631)                                                                                                                   |
| `MESH:('MESH', 'D06.472.317.525')`                     |              1 | [CL:0002272](http://purl.obolibrary.org/obo/CL_0002272)                                                                                                                   |
| `MESH:('MESH', 'A10.615.550.599')`                     |              1 | [CL:0002336](http://purl.obolibrary.org/obo/CL_0002336)                                                                                                                   |

## `MP`: Mammalian Phenotype Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `MP` (standardized to Bioregistry
prefix [`mp`](https://bioregistry.io/mp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref           |   usages_count | usages                                                  |
|-------------------------|----------------|---------------------------------------------------------|
| `MP:('MP', '19876834')` |              1 | [CL:0002488](http://purl.obolibrary.org/obo/CL_0002488) |

## `NCI_Thesaurus`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCI_Thesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                                                        |   usages_count | usages                                                  |
|----------------------------------------------------------------------|----------------|---------------------------------------------------------|
| `NCI_Thesaurus:('NCI_Thesaurus', 'Small_Intestinal_Glandular_Cell')` |              1 | [CL:1001598](http://purl.obolibrary.org/obo/CL_1001598) |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 4 invalid
xrefs to external prefixed with `ncithesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                                         |   usages_count | usages                                                  |
|-------------------------------------------------------|----------------|---------------------------------------------------------|
| `ncithesaurus:('ncithesaurus', 'Spermatogenic_Cell')` |              1 | [CL:0000015](http://purl.obolibrary.org/obo/CL_0000015) |
| `ncithesaurus:('ncithesaurus', 'Egg')`                |              1 | [CL:0000021](http://purl.obolibrary.org/obo/CL_0000021) |
| `ncithesaurus:('ncithesaurus', 'Beta_Cell')`          |              1 | [CL:0000169](http://purl.obolibrary.org/obo/CL_0000169) |
| `ncithesaurus:('ncithesaurus', 'Blastemal_Cell')`     |              1 | [CL:0000354](http://purl.obolibrary.org/obo/CL_0000354) |

## `PMID`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                |   usages_count | usages                                                  |
|------------------------------|----------------|---------------------------------------------------------|
| `PMID:('PMID', '10102814j')` |              1 | [CL:0000134](http://purl.obolibrary.org/obo/CL_0000134) |

## `SGD`: Saccharomyces Genome Database

Overall, there were 19 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
prefix [`sgd`](https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|----------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:('SGD', 'clt')` |             19 | [CL:0000596](http://purl.obolibrary.org/obo/CL_0000596), [CL:0000597](http://purl.obolibrary.org/obo/CL_0000597), [CL:0000599](http://purl.obolibrary.org/obo/CL_0000599), [CL:0000605](http://purl.obolibrary.org/obo/CL_0000605), [CL:0000606](http://purl.obolibrary.org/obo/CL_0000606), ... |

## `Wikipedia`: Wikipedia

Overall, there were 6 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                                        |   usages_count | usages                                                  |
|----------------------------------------------------------------------|----------------|---------------------------------------------------------|
| `Wikipedia:('Wikipedia', 'Alpha_motor_neuron&oldid=957148643')`      |              1 | [CL:0008038](http://purl.obolibrary.org/obo/CL_0008038) |
| `Wikipedia:('Wikipedia', 'Lower_motor_neuron&oldid=952547294')`      |              1 | [CL:0008039](http://purl.obolibrary.org/obo/CL_0008039) |
| `Wikipedia:('Wikipedia', 'Extrafusal_muscle_fiber&oldid=978415293')` |              1 | [CL:0008046](http://purl.obolibrary.org/obo/CL_0008046) |
| `Wikipedia:('Wikipedia', 'Intrafusal_muscle_fiber&oldid=937508784')` |              1 | [CL:0008047](http://purl.obolibrary.org/obo/CL_0008047) |
| `Wikipedia:('Wikipedia', 'Upper_motor_neuron&oldid=943248837')`      |              1 | [CL:0008048](http://purl.obolibrary.org/obo/CL_0008048) |
| `Wikipedia:('Wikipedia', 'Betz_cell&oldid=977472330')`               |              1 | [CL:0008049](http://purl.obolibrary.org/obo/CL_0008049) |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 6 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref          |   usages_count | usages                                                                                                                                                                                                                                                                                      |
|------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:('ZFIN', 'CVS')` |              5 | [CL:0005023](http://purl.obolibrary.org/obo/CL_0005023), [CL:0005024](http://purl.obolibrary.org/obo/CL_0005024), [CL:0005025](http://purl.obolibrary.org/obo/CL_0005025), [CL:0011100](http://purl.obolibrary.org/obo/CL_0011100), [CL:0015000](http://purl.obolibrary.org/obo/CL_0015000) |
| `ZFIN:('ZFIN', 'YB')`  |              1 | [CL:0011100](http://purl.obolibrary.org/obo/CL_0011100)                                                                                                                                                                                                                                     |

