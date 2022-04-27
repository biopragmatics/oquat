# cl

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `cl`. See the [GitHub repository](https://github.com/obophenotype/cell-ontology)


## `BTO`: BRENDA tissue / enzyme source

- Normalized prefix: `bto`
- [https://bioregistry.io/bto](https://bioregistry.io/bto)
- Pattern:`^\d{7}$`

| identifier   |   appearances | examples                                        |
|--------------|---------------|-------------------------------------------------|
| `BTO:000125` |             1 | [CL:1000398](https://bioregistry.io/CL:1000398) |

## `CL`: Cell Ontology

- Normalized prefix: `cl`
- [https://bioregistry.io/cl](https://bioregistry.io/cl)
- Pattern:`^\d{7}$`

| identifier                               |   appearances | examples                                                                                                                                                                                                                                                 |
|------------------------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CL:CVS`                                 |            16 | [CL:0005003](https://bioregistry.io/CL:0005003), [CL:0005004](https://bioregistry.io/CL:0005004), [CL:0005004](https://bioregistry.io/CL:0005004), [CL:0005004](https://bioregistry.io/CL:0005004), [CL:0005012](https://bioregistry.io/CL:0005012), ... |
| `CL:MAH`                                 |             3 | [CL:0007007](https://bioregistry.io/CL:0007007), [CL:0007008](https://bioregistry.io/CL:0007008), [CL:0007011](https://bioregistry.io/CL:0007011)                                                                                                        |
| `CL:curator`                             |             1 | [CL:0005018](https://bioregistry.io/CL:0005018)                                                                                                                                                                                                          |
| `CL:patterns/cellPartOfAnatomicalEntity` |             1 | [CL:0011030](https://bioregistry.io/CL:0011030)                                                                                                                                                                                                          |
| `CL:cjm`                                 |             1 | [CL:1000742](https://bioregistry.io/CL:1000742)                                                                                                                                                                                                          |

## `DOI`: Digital Object Identifier

- Normalized prefix: `doi`
- [https://bioregistry.io/doi](https://bioregistry.io/doi)
- Pattern:`^(doi\:)?\d{2}\.\d{4}.*$`

| identifier                                  |   appearances | examples                                        |
|---------------------------------------------|---------------|-------------------------------------------------|
| `DOI:https://doi.org/10.1378/chest.12-2762` |             1 | [CL:0000158](https://bioregistry.io/CL:0000158) |

## `FB`: FlyBase Gene

- Normalized prefix: `flybase`
- [https://bioregistry.io/flybase](https://bioregistry.io/flybase)
- Pattern:`^FB\w{2}\d{7}$`

| identifier   |   appearances | examples                                                                                                                                                                                                                                                 |
|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FB:ma`      |            25 | [CL:0000393](https://bioregistry.io/CL:0000393), [CL:0000404](https://bioregistry.io/CL:0000404), [CL:0000414](https://bioregistry.io/CL:0000414), [CL:0000565](https://bioregistry.io/CL:0000565), [CL:0000578](https://bioregistry.io/CL:0000578), ... |

## `Flybase`: FlyBase Gene

- Normalized prefix: `flybase`
- [https://bioregistry.io/flybase](https://bioregistry.io/flybase)
- Pattern:`^FB\w{2}\d{7}$`

| identifier    |   appearances | examples                                        |
|---------------|---------------|-------------------------------------------------|
| `Flybase:dsj` |             1 | [CL:0000362](https://bioregistry.io/CL:0000362) |

## `FlyBase`: FlyBase Gene

- Normalized prefix: `flybase`
- [https://bioregistry.io/flybase](https://bioregistry.io/flybase)
- Pattern:`^FB\w{2}\d{7}$`

| identifier   |   appearances | examples                                        |
|--------------|---------------|-------------------------------------------------|
| `FlyBase:ds` |             1 | [CL:0000463](https://bioregistry.io/CL:0000463) |

## `GC`: Genetic Code

- Normalized prefix: `gc`
- [https://bioregistry.io/gc](https://bioregistry.io/gc)
- Pattern:`^\d+$`

| identifier   |   appearances | examples                                        |
|--------------|---------------|-------------------------------------------------|
| `GC:tfm`     |             1 | [CL:0002597](https://bioregistry.io/CL:0002597) |

## `GO`: Gene Ontology

- Normalized prefix: `go`
- [https://bioregistry.io/go](https://bioregistry.io/go)
- Pattern:`^\d{7}$`

| identifier   |   appearances | examples                                                                                                                                                                                                                                                 |
|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:tfm`     |            16 | [CL:0000480](https://bioregistry.io/CL:0000480), [CL:0000483](https://bioregistry.io/CL:0000483), [CL:0000483](https://bioregistry.io/CL:0000483), [CL:0000496](https://bioregistry.io/CL:0000496), [CL:0000511](https://bioregistry.io/CL:0000511), ... |
| `GO:cvs`     |             1 | [CL:0005008](https://bioregistry.io/CL:0005008)                                                                                                                                                                                                          |

## `HPA`: Human Protein Atlas tissue profile information

- Normalized prefix: `hpa`
- [https://bioregistry.io/hpa](https://bioregistry.io/hpa)
- Pattern:`^ENSG\d{11}$`

| identifier   |   appearances | examples                                                                                                                                                                                                                                                 |
|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HPA:HPA`    |             6 | [CL:1001591](https://bioregistry.io/CL:1001591), [CL:1001596](https://bioregistry.io/CL:1001596), [CL:1001596](https://bioregistry.io/CL:1001596), [CL:1001596](https://bioregistry.io/CL:1001596), [CL:1001603](https://bioregistry.io/CL:1001603), ... |
| `HPA:Breast` |             1 | [CL:1001583](https://bioregistry.io/CL:1001583)                                                                                                                                                                                                          |

## `MA`: Mouse adult gross anatomy

- Normalized prefix: `ma`
- [https://bioregistry.io/ma](https://bioregistry.io/ma)
- Pattern:`^\d+$`

| identifier   |   appearances | examples                                                                                                                                                                                           |
|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MA:ma`      |             4 | [CL:0000362](https://bioregistry.io/CL:0000362), [CL:0000724](https://bioregistry.io/CL:0000724), [CL:0000730](https://bioregistry.io/CL:0000730), [CL:0000731](https://bioregistry.io/CL:0000731) |

## `MESH`: Medical Subject Headings

- Normalized prefix: `mesh`
- [https://bioregistry.io/mesh](https://bioregistry.io/mesh)
- Pattern:`^(C|D)\d{6,9}$`

| identifier                                 |   appearances | examples                                                                                                                                          |
|--------------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `MESH:A05.360.319.114.630.278.400`         |             3 | [CL:0000175](https://bioregistry.io/CL:0000175), [CL:0000590](https://bioregistry.io/CL:0000590), [CL:0000592](https://bioregistry.io/CL:0000592) |
| `MESH:A08.637`                             |             2 | [CL:0000125](https://bioregistry.io/CL:0000125), [CL:0000243](https://bioregistry.io/CL:0000243)                                                  |
| `MESH:A11.329.372.300`                     |             2 | [CL:0002150](https://bioregistry.io/CL:0002150), [CL:0002150](https://bioregistry.io/CL:0002150)                                                  |
| `MESH:A02.633.565.700`                     |             2 | [CL:0002211](https://bioregistry.io/CL:0002211), [CL:0002211](https://bioregistry.io/CL:0002211)                                                  |
| `MESH:A05.360.490.890.880`                 |             1 | [CL:0000017](https://bioregistry.io/CL:0000017)                                                                                                   |
| `MESH:A05.360.490.890.860`                 |             1 | [CL:0000018](https://bioregistry.io/CL:0000018)                                                                                                   |
| `MESH:A05.360.490.890`                     |             1 | [CL:0000019](https://bioregistry.io/CL:0000019)                                                                                                   |
| `MESH:A05.360.490.890.900`                 |             1 | [CL:0000020](https://bioregistry.io/CL:0000020)                                                                                                   |
| `MESH:A11.872`                             |             1 | [CL:0000034](https://bioregistry.io/CL:0000034)                                                                                                   |
| `MESH:A11.635`                             |             1 | [CL:0000056](https://bioregistry.io/CL:0000056)                                                                                                   |
| `MESH:A11.329.228`                         |             1 | [CL:0000057](https://bioregistry.io/CL:0000057)                                                                                                   |
| `MESH:A11.436.107`                         |             1 | [CL:0000059](https://bioregistry.io/CL:0000059)                                                                                                   |
| `MESH:A11.329.629`                         |             1 | [CL:0000062](https://bioregistry.io/CL:0000062)                                                                                                   |
| `MESH:A11.436`                             |             1 | [CL:0000066](https://bioregistry.io/CL:0000066)                                                                                                   |
| `MESH:A11.329.372.588`                     |             1 | [CL:0000091](https://bioregistry.io/CL:0000091)                                                                                                   |
| `MESH:A11.118.637.415`                     |             1 | [CL:0000094](https://bioregistry.io/CL:0000094)                                                                                                   |
| `MESH:A11.118.637.415.583`                 |             1 | [CL:0000096](https://bioregistry.io/CL:0000096)                                                                                                   |
| `MESH:A11.329.427`                         |             1 | [CL:0000097](https://bioregistry.io/CL:0000097)                                                                                                   |
| `MESH:A08.663.358`                         |             1 | [CL:0000099](https://bioregistry.io/CL:0000099)                                                                                                   |
| `MESH:A08.663.655.500`                     |             1 | [CL:0000100](https://bioregistry.io/CL:0000100)                                                                                                   |
| `MESH:A08.186.211.132.810.428.200.212.600` |             1 | [CL:0000121](https://bioregistry.io/CL:0000121)                                                                                                   |
| `MESH:A08.637.200`                         |             1 | [CL:0000127](https://bioregistry.io/CL:0000127)                                                                                                   |
| `MESH:A08.637.600`                         |             1 | [CL:0000128](https://bioregistry.io/CL:0000128)                                                                                                   |
| `MESH:A09.371.060.067.31`                  |             1 | [CL:0000132](https://bioregistry.io/CL:0000132)                                                                                                   |
| `MESH:A11.329.114`                         |             1 | [CL:0000136](https://bioregistry.io/CL:0000136)                                                                                                   |
| `MESH:A11.329.629.500`                     |             1 | [CL:0000137](https://bioregistry.io/CL:0000137)                                                                                                   |
| `MESH:A11.329.171`                         |             1 | [CL:0000138](https://bioregistry.io/CL:0000138)                                                                                                   |
| `MESH:A03.492.411.369.320`                 |             1 | [CL:0000160](https://bioregistry.io/CL:0000160)                                                                                                   |
| `MESH:A06.407`                             |             1 | [CL:0000163](https://bioregistry.io/CL:0000163)                                                                                                   |
| `MESH:A06.688`                             |             1 | [CL:0000165](https://bioregistry.io/CL:0000165)                                                                                                   |
| `MESH:A06.224.161`                         |             1 | [CL:0000166](https://bioregistry.io/CL:0000166)                                                                                                   |
| `MESH:A11.436.348`                         |             1 | [CL:0000182](https://bioregistry.io/CL:0000182)                                                                                                   |
| `MESH:A11.620`                             |             1 | [CL:0000187](https://bioregistry.io/CL:0000187)                                                                                                   |
| `MESH:A11.620.520`                         |             1 | [CL:0000192](https://bioregistry.io/CL:0000192)                                                                                                   |
| `MESH:A11.620.500`                         |             1 | [CL:0000193](https://bioregistry.io/CL:0000193)                                                                                                   |
| `MESH:A08.800.550.700.650`                 |             1 | [CL:0000198](https://bioregistry.io/CL:0000198)                                                                                                   |
| `MESH:A08.800.550.700.500`                 |             1 | [CL:0000199](https://bioregistry.io/CL:0000199)                                                                                                   |
| `MESH:A08.663.650.250`                     |             1 | [CL:0000202](https://bioregistry.io/CL:0000202)                                                                                                   |
| `MESH:A08.800.550.700.840`                 |             1 | [CL:0000205](https://bioregistry.io/CL:0000205)                                                                                                   |
| `MESH:A08.800.550.700.120`                 |             1 | [CL:0000206](https://bioregistry.io/CL:0000206)                                                                                                   |
| `MESH:A08.663.650.650`                     |             1 | [CL:0000210](https://bioregistry.io/CL:0000210)                                                                                                   |
| `MESH:A05.360.444.849.789`                 |             1 | [CL:0000216](https://bioregistry.io/CL:0000216)                                                                                                   |
| `MESH:A08.637.800`                         |             1 | [CL:0000218](https://bioregistry.io/CL:0000218)                                                                                                   |
| `MESH:A16.254.425.273`                     |             1 | [CL:0000221](https://bioregistry.io/CL:0000221)                                                                                                   |
| `MESH:A16.254.425.660`                     |             1 | [CL:0000222](https://bioregistry.io/CL:0000222)                                                                                                   |
| `MESH:A16.254.425.407`                     |             1 | [CL:0000223](https://bioregistry.io/CL:0000223)                                                                                                   |
| `MESH:A11.118.290`                         |             1 | [CL:0000232](https://bioregistry.io/CL:0000232)                                                                                                   |
| `MESH:A11.118.188`                         |             1 | [CL:0000233](https://bioregistry.io/CL:0000233)                                                                                                   |
| `MESH:A08.800.550.700.500.425`             |             1 | [CL:0000242](https://bioregistry.io/CL:0000242)                                                                                                   |
| `MESH:A11.436.397`                         |             1 | [CL:0000312](https://bioregistry.io/CL:0000312)                                                                                                   |
| `MESH:A12.200.882`                         |             1 | [CL:0000315](https://bioregistry.io/CL:0000315)                                                                                                   |
| `MESH:A12.200.702`                         |             1 | [CL:0000317](https://bioregistry.io/CL:0000317)                                                                                                   |
| `MESH:A12.200.849`                         |             1 | [CL:0000318](https://bioregistry.io/CL:0000318)                                                                                                   |
| `MESH:A16.254.600`                         |             1 | [CL:0000333](https://bioregistry.io/CL:0000333)                                                                                                   |
| `MESH:A11.936`                             |             1 | [CL:0000351](https://bioregistry.io/CL:0000351)                                                                                                   |
| `MESH:A11.104`                             |             1 | [CL:0000353](https://bioregistry.io/CL:0000353)                                                                                                   |
| `MESH:A16.254.270.550`                     |             1 | [CL:0000360](https://bioregistry.io/CL:0000360)                                                                                                   |
| `MESH:A16.254.412`                         |             1 | [CL:0000361](https://bioregistry.io/CL:0000361)                                                                                                   |
| `MESH:A11.329.114.500`                     |             1 | [CL:0000448](https://bioregistry.io/CL:0000448)                                                                                                   |
| `MESH:A10.165.114.322`                     |             1 | [CL:0000449](https://bioregistry.io/CL:0000449)                                                                                                   |
| `MESH:A11.118.637.555.567.569.200.400`     |             1 | [CL:0000492](https://bioregistry.io/CL:0000492)                                                                                                   |
| `MESH:A11.329.830`                         |             1 | [CL:0000499](https://bioregistry.io/CL:0000499)                                                                                                   |
| `MESH:A05.360.319.114.630.535.200`         |             1 | [CL:0000501](https://bioregistry.io/CL:0000501)                                                                                                   |
| `MESH:A03.492.766.440.175`                 |             1 | [CL:0000502](https://bioregistry.io/CL:0000502)                                                                                                   |
| `MESH:A05.360.319.114.630.535.400`         |             1 | [CL:0000503](https://bioregistry.io/CL:0000503)                                                                                                   |
| `MESH:A06.224.365`                         |             1 | [CL:0000504](https://bioregistry.io/CL:0000504)                                                                                                   |
| `MESH:A03.492.766.440.300`                 |             1 | [CL:0000508](https://bioregistry.io/CL:0000508)                                                                                                   |
| `MESH:A03.492.411.369.700`                 |             1 | [CL:0000510](https://bioregistry.io/CL:0000510)                                                                                                   |
| `MESH:A11.635.470`                         |             1 | [CL:0000513](https://bioregistry.io/CL:0000513)                                                                                                   |
| `MESH:A11.635.510`                         |             1 | [CL:0000514](https://bioregistry.io/CL:0000514)                                                                                                   |
| `MESH:A08.340.685`                         |             1 | [CL:0000516](https://bioregistry.io/CL:0000516)                                                                                                   |
| `MESH:A11.868`                             |             1 | [CL:0000524](https://bioregistry.io/CL:0000524)                                                                                                   |
| `MESH:A08.663.650`                         |             1 | [CL:0000526](https://bioregistry.io/CL:0000526)                                                                                                   |
| `MESH:A08.663.655`                         |             1 | [CL:0000527](https://bioregistry.io/CL:0000527)                                                                                                   |
| `MESH:A08.663.748`                         |             1 | [CL:0000528](https://bioregistry.io/CL:0000528)                                                                                                   |
| `MESH:A08.663`                             |             1 | [CL:0000540](https://bioregistry.io/CL:0000540)                                                                                                   |
| `MESH:A11.118.290.350.200`                 |             1 | [CL:0000547](https://bioregistry.io/CL:0000547)                                                                                                   |
| `MESH:A08.663.358.050`                     |             1 | [CL:0000561](https://bioregistry.io/CL:0000561)                                                                                                   |
| `MESH:A11.070`                             |             1 | [CL:0000568](https://bioregistry.io/CL:0000568)                                                                                                   |
| `MESH:A08.663.650.650.670.100`             |             1 | [CL:0000573](https://bioregistry.io/CL:0000573)                                                                                                   |
| `MESH:A11.118.637.555.652`                 |             1 | [CL:0000576](https://bioregistry.io/CL:0000576)                                                                                                   |
| `MESH:A03.492.766.440.250`                 |             1 | [CL:0000577](https://bioregistry.io/CL:0000577)                                                                                                   |
| `MESH:A11.329.372.630`                     |             1 | [CL:0000581](https://bioregistry.io/CL:0000581)                                                                                                   |
| `MESH:A11.329.372.600`                     |             1 | [CL:0000583](https://bioregistry.io/CL:0000583)                                                                                                   |
| `MESH:A05.360.490`                         |             1 | [CL:0000586](https://bioregistry.io/CL:0000586)                                                                                                   |
| `MESH:A11.329.679`                         |             1 | [CL:0000588](https://bioregistry.io/CL:0000588)                                                                                                   |
| `MESH:A08.663.650.250.250`                 |             1 | [CL:0000589](https://bioregistry.io/CL:0000589)                                                                                                   |
| `MESH:A11.635.500.700`                     |             1 | [CL:0000594](https://bioregistry.io/CL:0000594)                                                                                                   |
| `MESH:A08.186.211.577.405.700`             |             1 | [CL:0000598](https://bioregistry.io/CL:0000598)                                                                                                   |
| `MESH:A08.663.650.250.315`                 |             1 | [CL:0000601](https://bioregistry.io/CL:0000601)                                                                                                   |
| `MESH:A08.800.050.800.900.700`             |             1 | [CL:0000602](https://bioregistry.io/CL:0000602)                                                                                                   |
| `MESH:A08.663.650.650.670.650`             |             1 | [CL:0000604](https://bioregistry.io/CL:0000604)                                                                                                   |
| `MESH:A08.663.650.250.380`                 |             1 | [CL:0000609](https://bioregistry.io/CL:0000609)                                                                                                   |
| `MESH:A09.246.631.246.577.543`             |             1 | [CL:0000631](https://bioregistry.io/CL:0000631)                                                                                                   |
| `MESH:D06.472.317.525`                     |             1 | [CL:0002272](https://bioregistry.io/CL:0002272)                                                                                                   |
| `MESH:A10.615.550.599`                     |             1 | [CL:0002336](https://bioregistry.io/CL:0002336)                                                                                                   |

## `MP`: Mammalian Phenotype Ontology

- Normalized prefix: `mp`
- [https://bioregistry.io/mp](https://bioregistry.io/mp)
- Pattern:`^\d{7}$`

| identifier    |   appearances | examples                                        |
|---------------|---------------|-------------------------------------------------|
| `MP:19876834` |             1 | [CL:0002488](https://bioregistry.io/CL:0002488) |

## `NCI_Thesaurus`: NCI Thesaurus

- Normalized prefix: `ncit`
- [https://bioregistry.io/ncit](https://bioregistry.io/ncit)
- Pattern:`^C\d+$`

| identifier                                      |   appearances | examples                                        |
|-------------------------------------------------|---------------|-------------------------------------------------|
| `NCI_Thesaurus:Small_Intestinal_Glandular_Cell` |             1 | [CL:1001598](https://bioregistry.io/CL:1001598) |

## `ncithesaurus`: NCI Thesaurus

- Normalized prefix: `ncit`
- [https://bioregistry.io/ncit](https://bioregistry.io/ncit)
- Pattern:`^C\d+$`

| identifier                        |   appearances | examples                                        |
|-----------------------------------|---------------|-------------------------------------------------|
| `ncithesaurus:Spermatogenic_Cell` |             1 | [CL:0000015](https://bioregistry.io/CL:0000015) |
| `ncithesaurus:Egg`                |             1 | [CL:0000021](https://bioregistry.io/CL:0000021) |
| `ncithesaurus:Beta_Cell`          |             1 | [CL:0000169](https://bioregistry.io/CL:0000169) |
| `ncithesaurus:Blastemal_Cell`     |             1 | [CL:0000354](https://bioregistry.io/CL:0000354) |

## `PMID`: PubMed

- Normalized prefix: `pubmed`
- [https://bioregistry.io/pubmed](https://bioregistry.io/pubmed)
- Pattern:`^\d+$`

| identifier       |   appearances | examples                                        |
|------------------|---------------|-------------------------------------------------|
| `PMID:10102814j` |             1 | [CL:0000134](https://bioregistry.io/CL:0000134) |

## `SGD`: Saccharomyces Genome Database

- Normalized prefix: `sgd`
- [https://bioregistry.io/sgd](https://bioregistry.io/sgd)
- Pattern:`^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`

| identifier   |   appearances | examples                                                                                                                                                                                                                                                 |
|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:clt`    |            19 | [CL:0000606](https://bioregistry.io/CL:0000606), [CL:0002386](https://bioregistry.io/CL:0002386), [CL:0002389](https://bioregistry.io/CL:0002389), [CL:0002390](https://bioregistry.io/CL:0002390), [CL:0002390](https://bioregistry.io/CL:0002390), ... |

## `Wikipedia`: Wikipedia

- Normalized prefix: `wikipedia.en`
- [https://bioregistry.io/wikipedia.en](https://bioregistry.io/wikipedia.en)
- Pattern:`^[A-Za-z-0-9_]+$`

| identifier                                          |   appearances | examples                                        |
|-----------------------------------------------------|---------------|-------------------------------------------------|
| `Wikipedia:Alpha_motor_neuron&oldid=957148643`      |             1 | [CL:0008038](https://bioregistry.io/CL:0008038) |
| `Wikipedia:Lower_motor_neuron&oldid=952547294`      |             1 | [CL:0008039](https://bioregistry.io/CL:0008039) |
| `Wikipedia:Extrafusal_muscle_fiber&oldid=978415293` |             1 | [CL:0008046](https://bioregistry.io/CL:0008046) |
| `Wikipedia:Intrafusal_muscle_fiber&oldid=937508784` |             1 | [CL:0008047](https://bioregistry.io/CL:0008047) |
| `Wikipedia:Upper_motor_neuron&oldid=943248837`      |             1 | [CL:0008048](https://bioregistry.io/CL:0008048) |
| `Wikipedia:Betz_cell&oldid=977472330`               |             1 | [CL:0008049](https://bioregistry.io/CL:0008049) |

## `ZFIN`: Zebrafish Information Network Gene

- Normalized prefix: `zfin`
- [https://bioregistry.io/zfin](https://bioregistry.io/zfin)
- Pattern:`^ZDB\-\w+\-\d+\-\d+$`

| identifier   |   appearances | examples                                                                                                                                                                                                                                            |
|--------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:CVS`   |             5 | [CL:0005023](https://bioregistry.io/CL:0005023), [CL:0005024](https://bioregistry.io/CL:0005024), [CL:0005025](https://bioregistry.io/CL:0005025), [CL:0011100](https://bioregistry.io/CL:0011100), [CL:0015000](https://bioregistry.io/CL:0015000) |
| `ZFIN:YB`    |             1 | [CL:0011100](https://bioregistry.io/CL:0011100)                                                                                                                                                                                                     |

