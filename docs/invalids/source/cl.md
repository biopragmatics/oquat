# cl

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `cl`. See the [GitHub repository](https://github.com/obophenotype/cell-ontology).


## `BTO`: BRENDA tissue / enzyme source

Overall, there were 1 invalid
xrefs to external prefixed with `BTO` (standardized to Bioregistry
entry [`bto`]((https://bioregistry.io/bto)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                          |
|-----------------|----------------|-------------------------------------------------|
| `BTO:000125`    |              1 | [CL:1000398](https://bioregistry.io/CL:1000398) |

## `CL`: Cell Ontology

Overall, there were 22 invalid
xrefs to external prefixed with `CL` (standardized to Bioregistry
entry [`cl`]((https://bioregistry.io/cl)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                            |   usages_count | usages                                                                                                                                                                                                                                                   |
|------------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CL:CVS`                                 |             16 | [CL:0000212](https://bioregistry.io/CL:0000212), [CL:0005000](https://bioregistry.io/CL:0005000), [CL:0005001](https://bioregistry.io/CL:0005001), [CL:0005002](https://bioregistry.io/CL:0005002), [CL:0005003](https://bioregistry.io/CL:0005003), ... |
| `CL:MAH`                                 |              3 | [CL:0007007](https://bioregistry.io/CL:0007007), [CL:0007008](https://bioregistry.io/CL:0007008), [CL:0007011](https://bioregistry.io/CL:0007011)                                                                                                        |
| `CL:curator`                             |              1 | [CL:0005018](https://bioregistry.io/CL:0005018)                                                                                                                                                                                                          |
| `CL:patterns/cellPartOfAnatomicalEntity` |              1 | [CL:0011030](https://bioregistry.io/CL:0011030)                                                                                                                                                                                                          |
| `CL:cjm`                                 |              1 | [CL:1000742](https://bioregistry.io/CL:1000742)                                                                                                                                                                                                          |

## `DOI`: Digital Object Identifier

Overall, there were 1 invalid
xrefs to external prefixed with `DOI` (standardized to Bioregistry
entry [`doi`]((https://bioregistry.io/doi)) that
did not match the standard pattern `^(doi\:)?\d{2}\.\d{4}.*$`.

| external_xref                               |   usages_count | usages                                          |
|---------------------------------------------|----------------|-------------------------------------------------|
| `DOI:https://doi.org/10.1378/chest.12-2762` |              1 | [CL:0000158](https://bioregistry.io/CL:0000158) |

## `FB`: FlyBase Gene

Overall, there were 25 invalid
xrefs to external prefixed with `FB` (standardized to Bioregistry
entry [`flybase`]((https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                   |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FB:ma`         |             25 | [CL:0000004](https://bioregistry.io/CL:0000004), [CL:0000063](https://bioregistry.io/CL:0000063), [CL:0000066](https://bioregistry.io/CL:0000066), [CL:0000134](https://bioregistry.io/CL:0000134), [CL:0000144](https://bioregistry.io/CL:0000144), ... |

## `Flybase`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `Flybase` (standardized to Bioregistry
entry [`flybase`]((https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                          |
|-----------------|----------------|-------------------------------------------------|
| `Flybase:dsj`   |              1 | [CL:0000362](https://bioregistry.io/CL:0000362) |

## `FlyBase`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `FlyBase` (standardized to Bioregistry
entry [`flybase`]((https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                          |
|-----------------|----------------|-------------------------------------------------|
| `FlyBase:ds`    |              1 | [CL:0000463](https://bioregistry.io/CL:0000463) |

## `GC`: Genetic Code

Overall, there were 1 invalid
xrefs to external prefixed with `GC` (standardized to Bioregistry
entry [`gc`]((https://bioregistry.io/gc)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                          |
|-----------------|----------------|-------------------------------------------------|
| `GC:tfm`        |              1 | [CL:0002597](https://bioregistry.io/CL:0002597) |

## `GO`: Gene Ontology

Overall, there were 17 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
entry [`go`]((https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                   |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:tfm`        |             16 | [CL:0000478](https://bioregistry.io/CL:0000478), [CL:0000479](https://bioregistry.io/CL:0000479), [CL:0000480](https://bioregistry.io/CL:0000480), [CL:0000481](https://bioregistry.io/CL:0000481), [CL:0000482](https://bioregistry.io/CL:0000482), ... |
| `GO:cvs`        |              1 | [CL:0005008](https://bioregistry.io/CL:0005008)                                                                                                                                                                                                          |

## `HPA`: Human Protein Atlas tissue profile information

Overall, there were 7 invalid
xrefs to external prefixed with `HPA` (standardized to Bioregistry
entry [`hpa`]((https://bioregistry.io/hpa)) that
did not match the standard pattern `^ENSG\d{11}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                   |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HPA:HPA`       |              6 | [CL:1001586](https://bioregistry.io/CL:1001586), [CL:1001591](https://bioregistry.io/CL:1001591), [CL:1001593](https://bioregistry.io/CL:1001593), [CL:1001596](https://bioregistry.io/CL:1001596), [CL:1001599](https://bioregistry.io/CL:1001599), ... |
| `HPA:Breast`    |              1 | [CL:1001583](https://bioregistry.io/CL:1001583)                                                                                                                                                                                                          |

## `MA`: Mouse adult gross anatomy

Overall, there were 4 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
entry [`ma`]((https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                             |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MA:ma`         |              4 | [CL:0000362](https://bioregistry.io/CL:0000362), [CL:0000724](https://bioregistry.io/CL:0000724), [CL:0000730](https://bioregistry.io/CL:0000730), [CL:0000731](https://bioregistry.io/CL:0000731) |

## `MESH`: Medical Subject Headings

Overall, there were 101 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
entry [`mesh`]((https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                              |   usages_count | usages                                                                                                                                            |
|--------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `MESH:A05.360.319.114.630.278.400`         |              3 | [CL:0000175](https://bioregistry.io/CL:0000175), [CL:0000590](https://bioregistry.io/CL:0000590), [CL:0000592](https://bioregistry.io/CL:0000592) |
| `MESH:A08.637`                             |              2 | [CL:0000125](https://bioregistry.io/CL:0000125), [CL:0000243](https://bioregistry.io/CL:0000243)                                                  |
| `MESH:A11.329.372.300`                     |              2 | [CL:0002150](https://bioregistry.io/CL:0002150), [CL:0002150](https://bioregistry.io/CL:0002150)                                                  |
| `MESH:A02.633.565.700`                     |              2 | [CL:0002211](https://bioregistry.io/CL:0002211), [CL:0002211](https://bioregistry.io/CL:0002211)                                                  |
| `MESH:A05.360.490.890.880`                 |              1 | [CL:0000017](https://bioregistry.io/CL:0000017)                                                                                                   |
| `MESH:A05.360.490.890.860`                 |              1 | [CL:0000018](https://bioregistry.io/CL:0000018)                                                                                                   |
| `MESH:A05.360.490.890`                     |              1 | [CL:0000019](https://bioregistry.io/CL:0000019)                                                                                                   |
| `MESH:A05.360.490.890.900`                 |              1 | [CL:0000020](https://bioregistry.io/CL:0000020)                                                                                                   |
| `MESH:A11.872`                             |              1 | [CL:0000034](https://bioregistry.io/CL:0000034)                                                                                                   |
| `MESH:A11.635`                             |              1 | [CL:0000056](https://bioregistry.io/CL:0000056)                                                                                                   |
| `MESH:A11.329.228`                         |              1 | [CL:0000057](https://bioregistry.io/CL:0000057)                                                                                                   |
| `MESH:A11.436.107`                         |              1 | [CL:0000059](https://bioregistry.io/CL:0000059)                                                                                                   |
| `MESH:A11.329.629`                         |              1 | [CL:0000062](https://bioregistry.io/CL:0000062)                                                                                                   |
| `MESH:A11.436`                             |              1 | [CL:0000066](https://bioregistry.io/CL:0000066)                                                                                                   |
| `MESH:A11.329.372.588`                     |              1 | [CL:0000091](https://bioregistry.io/CL:0000091)                                                                                                   |
| `MESH:A11.118.637.415`                     |              1 | [CL:0000094](https://bioregistry.io/CL:0000094)                                                                                                   |
| `MESH:A11.118.637.415.583`                 |              1 | [CL:0000096](https://bioregistry.io/CL:0000096)                                                                                                   |
| `MESH:A11.329.427`                         |              1 | [CL:0000097](https://bioregistry.io/CL:0000097)                                                                                                   |
| `MESH:A08.663.358`                         |              1 | [CL:0000099](https://bioregistry.io/CL:0000099)                                                                                                   |
| `MESH:A08.663.655.500`                     |              1 | [CL:0000100](https://bioregistry.io/CL:0000100)                                                                                                   |
| `MESH:A08.186.211.132.810.428.200.212.600` |              1 | [CL:0000121](https://bioregistry.io/CL:0000121)                                                                                                   |
| `MESH:A08.637.200`                         |              1 | [CL:0000127](https://bioregistry.io/CL:0000127)                                                                                                   |
| `MESH:A08.637.600`                         |              1 | [CL:0000128](https://bioregistry.io/CL:0000128)                                                                                                   |
| `MESH:A09.371.060.067.31`                  |              1 | [CL:0000132](https://bioregistry.io/CL:0000132)                                                                                                   |
| `MESH:A11.329.114`                         |              1 | [CL:0000136](https://bioregistry.io/CL:0000136)                                                                                                   |
| `MESH:A11.329.629.500`                     |              1 | [CL:0000137](https://bioregistry.io/CL:0000137)                                                                                                   |
| `MESH:A11.329.171`                         |              1 | [CL:0000138](https://bioregistry.io/CL:0000138)                                                                                                   |
| `MESH:A03.492.411.369.320`                 |              1 | [CL:0000160](https://bioregistry.io/CL:0000160)                                                                                                   |
| `MESH:A06.407`                             |              1 | [CL:0000163](https://bioregistry.io/CL:0000163)                                                                                                   |
| `MESH:A06.688`                             |              1 | [CL:0000165](https://bioregistry.io/CL:0000165)                                                                                                   |
| `MESH:A06.224.161`                         |              1 | [CL:0000166](https://bioregistry.io/CL:0000166)                                                                                                   |
| `MESH:A11.436.348`                         |              1 | [CL:0000182](https://bioregistry.io/CL:0000182)                                                                                                   |
| `MESH:A11.620`                             |              1 | [CL:0000187](https://bioregistry.io/CL:0000187)                                                                                                   |
| `MESH:A11.620.520`                         |              1 | [CL:0000192](https://bioregistry.io/CL:0000192)                                                                                                   |
| `MESH:A11.620.500`                         |              1 | [CL:0000193](https://bioregistry.io/CL:0000193)                                                                                                   |
| `MESH:A08.800.550.700.650`                 |              1 | [CL:0000198](https://bioregistry.io/CL:0000198)                                                                                                   |
| `MESH:A08.800.550.700.500`                 |              1 | [CL:0000199](https://bioregistry.io/CL:0000199)                                                                                                   |
| `MESH:A08.663.650.250`                     |              1 | [CL:0000202](https://bioregistry.io/CL:0000202)                                                                                                   |
| `MESH:A08.800.550.700.840`                 |              1 | [CL:0000205](https://bioregistry.io/CL:0000205)                                                                                                   |
| `MESH:A08.800.550.700.120`                 |              1 | [CL:0000206](https://bioregistry.io/CL:0000206)                                                                                                   |
| `MESH:A08.663.650.650`                     |              1 | [CL:0000210](https://bioregistry.io/CL:0000210)                                                                                                   |
| `MESH:A05.360.444.849.789`                 |              1 | [CL:0000216](https://bioregistry.io/CL:0000216)                                                                                                   |
| `MESH:A08.637.800`                         |              1 | [CL:0000218](https://bioregistry.io/CL:0000218)                                                                                                   |
| `MESH:A16.254.425.273`                     |              1 | [CL:0000221](https://bioregistry.io/CL:0000221)                                                                                                   |
| `MESH:A16.254.425.660`                     |              1 | [CL:0000222](https://bioregistry.io/CL:0000222)                                                                                                   |
| `MESH:A16.254.425.407`                     |              1 | [CL:0000223](https://bioregistry.io/CL:0000223)                                                                                                   |
| `MESH:A11.118.290`                         |              1 | [CL:0000232](https://bioregistry.io/CL:0000232)                                                                                                   |
| `MESH:A11.118.188`                         |              1 | [CL:0000233](https://bioregistry.io/CL:0000233)                                                                                                   |
| `MESH:A08.800.550.700.500.425`             |              1 | [CL:0000242](https://bioregistry.io/CL:0000242)                                                                                                   |
| `MESH:A11.436.397`                         |              1 | [CL:0000312](https://bioregistry.io/CL:0000312)                                                                                                   |
| `MESH:A12.200.882`                         |              1 | [CL:0000315](https://bioregistry.io/CL:0000315)                                                                                                   |
| `MESH:A12.200.702`                         |              1 | [CL:0000317](https://bioregistry.io/CL:0000317)                                                                                                   |
| `MESH:A12.200.849`                         |              1 | [CL:0000318](https://bioregistry.io/CL:0000318)                                                                                                   |
| `MESH:A16.254.600`                         |              1 | [CL:0000333](https://bioregistry.io/CL:0000333)                                                                                                   |
| `MESH:A11.936`                             |              1 | [CL:0000351](https://bioregistry.io/CL:0000351)                                                                                                   |
| `MESH:A11.104`                             |              1 | [CL:0000353](https://bioregistry.io/CL:0000353)                                                                                                   |
| `MESH:A16.254.270.550`                     |              1 | [CL:0000360](https://bioregistry.io/CL:0000360)                                                                                                   |
| `MESH:A16.254.412`                         |              1 | [CL:0000361](https://bioregistry.io/CL:0000361)                                                                                                   |
| `MESH:A11.329.114.500`                     |              1 | [CL:0000448](https://bioregistry.io/CL:0000448)                                                                                                   |
| `MESH:A10.165.114.322`                     |              1 | [CL:0000449](https://bioregistry.io/CL:0000449)                                                                                                   |
| `MESH:A11.118.637.555.567.569.200.400`     |              1 | [CL:0000492](https://bioregistry.io/CL:0000492)                                                                                                   |
| `MESH:A11.329.830`                         |              1 | [CL:0000499](https://bioregistry.io/CL:0000499)                                                                                                   |
| `MESH:A05.360.319.114.630.535.200`         |              1 | [CL:0000501](https://bioregistry.io/CL:0000501)                                                                                                   |
| `MESH:A03.492.766.440.175`                 |              1 | [CL:0000502](https://bioregistry.io/CL:0000502)                                                                                                   |
| `MESH:A05.360.319.114.630.535.400`         |              1 | [CL:0000503](https://bioregistry.io/CL:0000503)                                                                                                   |
| `MESH:A06.224.365`                         |              1 | [CL:0000504](https://bioregistry.io/CL:0000504)                                                                                                   |
| `MESH:A03.492.766.440.300`                 |              1 | [CL:0000508](https://bioregistry.io/CL:0000508)                                                                                                   |
| `MESH:A03.492.411.369.700`                 |              1 | [CL:0000510](https://bioregistry.io/CL:0000510)                                                                                                   |
| `MESH:A11.635.470`                         |              1 | [CL:0000513](https://bioregistry.io/CL:0000513)                                                                                                   |
| `MESH:A11.635.510`                         |              1 | [CL:0000514](https://bioregistry.io/CL:0000514)                                                                                                   |
| `MESH:A08.340.685`                         |              1 | [CL:0000516](https://bioregistry.io/CL:0000516)                                                                                                   |
| `MESH:A11.868`                             |              1 | [CL:0000524](https://bioregistry.io/CL:0000524)                                                                                                   |
| `MESH:A08.663.650`                         |              1 | [CL:0000526](https://bioregistry.io/CL:0000526)                                                                                                   |
| `MESH:A08.663.655`                         |              1 | [CL:0000527](https://bioregistry.io/CL:0000527)                                                                                                   |
| `MESH:A08.663.748`                         |              1 | [CL:0000528](https://bioregistry.io/CL:0000528)                                                                                                   |
| `MESH:A08.663`                             |              1 | [CL:0000540](https://bioregistry.io/CL:0000540)                                                                                                   |
| `MESH:A11.118.290.350.200`                 |              1 | [CL:0000547](https://bioregistry.io/CL:0000547)                                                                                                   |
| `MESH:A08.663.358.050`                     |              1 | [CL:0000561](https://bioregistry.io/CL:0000561)                                                                                                   |
| `MESH:A11.070`                             |              1 | [CL:0000568](https://bioregistry.io/CL:0000568)                                                                                                   |
| `MESH:A08.663.650.650.670.100`             |              1 | [CL:0000573](https://bioregistry.io/CL:0000573)                                                                                                   |
| `MESH:A11.118.637.555.652`                 |              1 | [CL:0000576](https://bioregistry.io/CL:0000576)                                                                                                   |
| `MESH:A03.492.766.440.250`                 |              1 | [CL:0000577](https://bioregistry.io/CL:0000577)                                                                                                   |
| `MESH:A11.329.372.630`                     |              1 | [CL:0000581](https://bioregistry.io/CL:0000581)                                                                                                   |
| `MESH:A11.329.372.600`                     |              1 | [CL:0000583](https://bioregistry.io/CL:0000583)                                                                                                   |
| `MESH:A05.360.490`                         |              1 | [CL:0000586](https://bioregistry.io/CL:0000586)                                                                                                   |
| `MESH:A11.329.679`                         |              1 | [CL:0000588](https://bioregistry.io/CL:0000588)                                                                                                   |
| `MESH:A08.663.650.250.250`                 |              1 | [CL:0000589](https://bioregistry.io/CL:0000589)                                                                                                   |
| `MESH:A11.635.500.700`                     |              1 | [CL:0000594](https://bioregistry.io/CL:0000594)                                                                                                   |
| `MESH:A08.186.211.577.405.700`             |              1 | [CL:0000598](https://bioregistry.io/CL:0000598)                                                                                                   |
| `MESH:A08.663.650.250.315`                 |              1 | [CL:0000601](https://bioregistry.io/CL:0000601)                                                                                                   |
| `MESH:A08.800.050.800.900.700`             |              1 | [CL:0000602](https://bioregistry.io/CL:0000602)                                                                                                   |
| `MESH:A08.663.650.650.670.650`             |              1 | [CL:0000604](https://bioregistry.io/CL:0000604)                                                                                                   |
| `MESH:A08.663.650.250.380`                 |              1 | [CL:0000609](https://bioregistry.io/CL:0000609)                                                                                                   |
| `MESH:A09.246.631.246.577.543`             |              1 | [CL:0000631](https://bioregistry.io/CL:0000631)                                                                                                   |
| `MESH:D06.472.317.525`                     |              1 | [CL:0002272](https://bioregistry.io/CL:0002272)                                                                                                   |
| `MESH:A10.615.550.599`                     |              1 | [CL:0002336](https://bioregistry.io/CL:0002336)                                                                                                   |

## `MP`: Mammalian Phenotype Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `MP` (standardized to Bioregistry
entry [`mp`]((https://bioregistry.io/mp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                          |
|-----------------|----------------|-------------------------------------------------|
| `MP:19876834`   |              1 | [CL:0002488](https://bioregistry.io/CL:0002488) |

## `NCI_Thesaurus`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCI_Thesaurus` (standardized to Bioregistry
entry [`ncit`]((https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                                   |   usages_count | usages                                          |
|-------------------------------------------------|----------------|-------------------------------------------------|
| `NCI_Thesaurus:Small_Intestinal_Glandular_Cell` |              1 | [CL:1001598](https://bioregistry.io/CL:1001598) |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 4 invalid
xrefs to external prefixed with `ncithesaurus` (standardized to Bioregistry
entry [`ncit`]((https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                     |   usages_count | usages                                          |
|-----------------------------------|----------------|-------------------------------------------------|
| `ncithesaurus:Spermatogenic_Cell` |              1 | [CL:0000015](https://bioregistry.io/CL:0000015) |
| `ncithesaurus:Egg`                |              1 | [CL:0000021](https://bioregistry.io/CL:0000021) |
| `ncithesaurus:Beta_Cell`          |              1 | [CL:0000169](https://bioregistry.io/CL:0000169) |
| `ncithesaurus:Blastemal_Cell`     |              1 | [CL:0000354](https://bioregistry.io/CL:0000354) |

## `PMID`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
entry [`pubmed`]((https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref    |   usages_count | usages                                          |
|------------------|----------------|-------------------------------------------------|
| `PMID:10102814j` |              1 | [CL:0000134](https://bioregistry.io/CL:0000134) |

## `SGD`: Saccharomyces Genome Database

Overall, there were 19 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
entry [`sgd`]((https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                   |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:clt`       |             19 | [CL:0000596](https://bioregistry.io/CL:0000596), [CL:0000597](https://bioregistry.io/CL:0000597), [CL:0000599](https://bioregistry.io/CL:0000599), [CL:0000605](https://bioregistry.io/CL:0000605), [CL:0000606](https://bioregistry.io/CL:0000606), ... |

## `Wikipedia`: Wikipedia

Overall, there were 6 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
entry [`wikipedia.en`]((https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                       |   usages_count | usages                                          |
|-----------------------------------------------------|----------------|-------------------------------------------------|
| `Wikipedia:Alpha_motor_neuron&oldid=957148643`      |              1 | [CL:0008038](https://bioregistry.io/CL:0008038) |
| `Wikipedia:Lower_motor_neuron&oldid=952547294`      |              1 | [CL:0008039](https://bioregistry.io/CL:0008039) |
| `Wikipedia:Extrafusal_muscle_fiber&oldid=978415293` |              1 | [CL:0008046](https://bioregistry.io/CL:0008046) |
| `Wikipedia:Intrafusal_muscle_fiber&oldid=937508784` |              1 | [CL:0008047](https://bioregistry.io/CL:0008047) |
| `Wikipedia:Upper_motor_neuron&oldid=943248837`      |              1 | [CL:0008048](https://bioregistry.io/CL:0008048) |
| `Wikipedia:Betz_cell&oldid=977472330`               |              1 | [CL:0008049](https://bioregistry.io/CL:0008049) |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 6 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
entry [`zfin`]((https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                              |
|-----------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:CVS`      |              5 | [CL:0005023](https://bioregistry.io/CL:0005023), [CL:0005024](https://bioregistry.io/CL:0005024), [CL:0005025](https://bioregistry.io/CL:0005025), [CL:0011100](https://bioregistry.io/CL:0011100), [CL:0015000](https://bioregistry.io/CL:0015000) |
| `ZFIN:YB`       |              1 | [CL:0011100](https://bioregistry.io/CL:0011100)                                                                                                                                                                                                     |

