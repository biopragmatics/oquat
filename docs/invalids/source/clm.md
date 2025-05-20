# clm

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `clm`. See the [GitHub repository](https://github.com/Cellular-Semantics/CellMark).


## `AAO`: Amphibian gross anatomy

Overall, there were 5 invalid
xrefs to external prefixed with `AAO` (standardized to Bioregistry
prefix [`aao`](https://bioregistry.io/aao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                              |
|-----------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AAO:EJS`       |              5 | [UBERON:3000961](http://purl.obolibrary.org/obo/UBERON_3000961), [UBERON:3000972](http://purl.obolibrary.org/obo/UBERON_3000972), [UBERON:3000977](http://purl.obolibrary.org/obo/UBERON_3000977), [UBERON:3000982](http://purl.obolibrary.org/obo/UBERON_3000982), [UBERON:3010200](http://purl.obolibrary.org/obo/UBERON_3010200) |

## `AEO`: Anatomical Entity Ontology

Overall, there were 23 invalid
xrefs to external prefixed with `AEO` (standardized to Bioregistry
prefix [`aeo`](https://bioregistry.io/aeo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AEO:JB`        |             22 | [UBERON:0001637](http://purl.obolibrary.org/obo/UBERON_0001637), [UBERON:0004016](http://purl.obolibrary.org/obo/UBERON_0004016), [UBERON:0005866](http://purl.obolibrary.org/obo/UBERON_0005866), [UBERON:0006846](http://purl.obolibrary.org/obo/UBERON_0006846), [UBERON:0007473](http://purl.obolibrary.org/obo/UBERON_0007473), ... |
| `AEO:000020`    |              1 | [UBERON:0001013](http://purl.obolibrary.org/obo/UBERON_0001013)                                                                                                                                                                                                                                                                          |

## `BTO`: BRENDA Tissue Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `BTO` (standardized to Bioregistry
prefix [`bto`](https://bioregistry.io/bto)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `BTO:000125`    |              1 | [CL:1000398](http://purl.obolibrary.org/obo/CL_1000398) |

## `CALOHA`: CALIPHO Group Ontology of Human Anatomy

Overall, there were 3 invalid
xrefs to external prefixed with `CALOHA` (standardized to Bioregistry
prefix [`caloha`](https://bioregistry.io/caloha)) that
did not match the standard pattern `^TS-\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                            |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CALOHA:paula`  |              3 | [UBERON:0007808](http://purl.obolibrary.org/obo/UBERON_0007808), [UBERON:0014454](http://purl.obolibrary.org/obo/UBERON_0014454), [UBERON:0014455](http://purl.obolibrary.org/obo/UBERON_0014455) |

## `CARO`: Common Anatomy Reference Ontology

Overall, there were 4 invalid
xrefs to external prefixed with `CARO` (standardized to Bioregistry
prefix [`caro`](https://bioregistry.io/caro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                            |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CARO:DOS`      |              3 | [UBERON:0000026](http://purl.obolibrary.org/obo/UBERON_0000026), [UBERON:0000475](http://purl.obolibrary.org/obo/UBERON_0000475), [UBERON:0000478](http://purl.obolibrary.org/obo/UBERON_0000478) |
| `CARO:mah`      |              1 | [CL:0000000](http://purl.obolibrary.org/obo/CL_0000000)                                                                                                                                           |

## `CL`: Cell Ontology

Overall, there were 4 invalid
xrefs to external prefixed with `CL` (standardized to Bioregistry
prefix [`cl`](https://bioregistry.io/cl)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                            |   usages_count | usages                                                                                                           |
|------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `CL:CVS`                                 |              2 | [CL:0005000](http://purl.obolibrary.org/obo/CL_0005000), [CL:0005012](http://purl.obolibrary.org/obo/CL_0005012) |
| `CL:patterns/cellPartOfAnatomicalEntity` |              1 | [CL:0011030](http://purl.obolibrary.org/obo/CL_0011030)                                                          |
| `CL:tm`                                  |              1 | [UBERON:0005158](http://purl.obolibrary.org/obo/UBERON_0005158)                                                  |

## `doi`: Digital Object Identifier

Overall, there were 2 invalid
xrefs to external prefixed with `doi` (standardized to Bioregistry
prefix [`doi`](https://bioregistry.io/doi)) that
did not match the standard pattern `^10.\d{2,9}/.*$`.

| external_xref                             |   usages_count | usages                                                  |
|-------------------------------------------|----------------|---------------------------------------------------------|
| `doi:/10.1016/B978-0-12-410424-2.00003-2` |              1 | [CL:0000079](http://purl.obolibrary.org/obo/CL_0000079) |
| `doi:/10.1038/s41467-021-27901-5`         |              1 | [CL:4052006](http://purl.obolibrary.org/obo/CL_4052006) |

## `FB`: FlyBase Gene

Overall, there were 16 invalid
xrefs to external prefixed with `FB` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FB:ma`         |             13 | [CL:0000066](http://purl.obolibrary.org/obo/CL_0000066), [CL:0000134](http://purl.obolibrary.org/obo/CL_0000134), [CL:0000183](http://purl.obolibrary.org/obo/CL_0000183), [CL:0000211](http://purl.obolibrary.org/obo/CL_0000211), [CL:0000219](http://purl.obolibrary.org/obo/CL_0000219), ... |
| `FB:gg`         |              2 | [UBERON:0000018](http://purl.obolibrary.org/obo/UBERON_0000018), [UBERON:0001007](http://purl.obolibrary.org/obo/UBERON_0001007)                                                                                                                                                                 |
| `FB:DJS`        |              1 | [UBERON:0001048](http://purl.obolibrary.org/obo/UBERON_0001048)                                                                                                                                                                                                                                  |

## `Flybase`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `Flybase` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `Flybase:dsj`   |              1 | [CL:0000362](http://purl.obolibrary.org/obo/CL_0000362) |

## `FMA`: Foundational Model of Anatomy

Overall, there were 8 invalid
xrefs to external prefixed with `FMA` (standardized to Bioregistry
prefix [`fma`](https://bioregistry.io/fma)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FMA:FMA`       |              8 | [UBERON:0000485](http://purl.obolibrary.org/obo/UBERON_0000485), [UBERON:0000486](http://purl.obolibrary.org/obo/UBERON_0000486), [UBERON:0001943](http://purl.obolibrary.org/obo/UBERON_0001943), [UBERON:0002167](http://purl.obolibrary.org/obo/UBERON_0002167), [UBERON:0002168](http://purl.obolibrary.org/obo/UBERON_0002168), ... |

## `GO`: Gene Ontology

Overall, there were 9 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                             |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:jl`         |              4 | [GO:0044092](http://purl.obolibrary.org/obo/GO_0044092), [GO:0044093](http://purl.obolibrary.org/obo/GO_0044093), [GO:1902679](http://purl.obolibrary.org/obo/GO_1902679), [GO:1902680](http://purl.obolibrary.org/obo/GO_1902680) |
| `GO:tfm`        |              3 | [CL:0000506](http://purl.obolibrary.org/obo/CL_0000506), [CL:0000507](http://purl.obolibrary.org/obo/CL_0000507), [CL:0000509](http://purl.obolibrary.org/obo/CL_0000509)                                                          |
| `GO:GO`         |              1 | [UBERON:0000016](http://purl.obolibrary.org/obo/UBERON_0000016)                                                                                                                                                                    |
| `GO:curator`    |              1 | [UBERON:0005863](http://purl.obolibrary.org/obo/UBERON_0005863)                                                                                                                                                                    |

## `HPA`: Human Protein Atlas tissue profile information

Overall, there were 2 invalid
xrefs to external prefixed with `HPA` (standardized to Bioregistry
prefix [`hpa`](https://bioregistry.io/hpa)) that
did not match the standard pattern `^ENSG\d{11}$`.

| external_xref   |   usages_count | usages                                                                                                           |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `HPA:HPA`       |              2 | [CL:1001599](http://purl.obolibrary.org/obo/CL_1001599), [CL:1001603](http://purl.obolibrary.org/obo/CL_1001603) |

## `HPO`: Human Phenotype Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `HPO` (standardized to Bioregistry
prefix [`hp`](https://bioregistry.io/hp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `HPO:pr`        |              1 | [UBERON:0035639](http://purl.obolibrary.org/obo/UBERON_0035639) |

## `MA`: Mouse adult gross anatomy

Overall, there were 1 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
prefix [`ma`](https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `MA:ma`         |              1 | [CL:0000362](http://purl.obolibrary.org/obo/CL_0000362) |

## `MESH`: Medical Subject Headings

Overall, there were 23 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D|M)\d{6,9}$`.

| external_xref                      |   usages_count | usages                                                          |
|------------------------------------|----------------|-----------------------------------------------------------------|
| `MESH:A03.734.414`                 |              1 | [UBERON:0000006](http://purl.obolibrary.org/obo/UBERON_0000006) |
| `MESH:A07.231.114.056`             |              1 | [UBERON:0000947](http://purl.obolibrary.org/obo/UBERON_0000947) |
| `MESH:A09.371.060.217`             |              1 | [UBERON:0000964](http://purl.obolibrary.org/obo/UBERON_0000964) |
| `MESH:A10.165.114`                 |              1 | [UBERON:0001013](http://purl.obolibrary.org/obo/UBERON_0001013) |
| `MESH:A09.371.060.067`             |              1 | [UBERON:0001766](http://purl.obolibrary.org/obo/UBERON_0001766) |
| `MESH:A09.371.060.217.325`         |              1 | [UBERON:0001772](http://purl.obolibrary.org/obo/UBERON_0001772) |
| `MESH:A09.371.060.217.228`         |              1 | [UBERON:0001777](http://purl.obolibrary.org/obo/UBERON_0001777) |
| `MESH:A08.800.800.720`             |              1 | [UBERON:0001780](http://purl.obolibrary.org/obo/UBERON_0001780) |
| `MESH:A09.371.060`                 |              1 | [UBERON:0001801](http://purl.obolibrary.org/obo/UBERON_0001801) |
| `MESH:A07.231.432.952`             |              1 | [UBERON:0001979](http://purl.obolibrary.org/obo/UBERON_0001979) |
| `MESH:A10.272.491`                 |              1 | [UBERON:0001986](http://purl.obolibrary.org/obo/UBERON_0001986) |
| `MESH:A08.186.211.132.810.428.200` |              1 | [UBERON:0002037](http://purl.obolibrary.org/obo/UBERON_0002037) |
| `MESH:A07.541.459`                 |              1 | [UBERON:0002099](http://purl.obolibrary.org/obo/UBERON_0002099) |
| `MESH:A04.411.125`                 |              1 | [UBERON:0002185](http://purl.obolibrary.org/obo/UBERON_0002185) |
| `MESH:A03.159.183.079`             |              1 | [UBERON:0003703](http://purl.obolibrary.org/obo/UBERON_0003703) |
| `MESH:A03.159.183.158`             |              1 | [UBERON:0003704](http://purl.obolibrary.org/obo/UBERON_0003704) |
| `MESH:A08.800.800.720.800`         |              1 | [UBERON:0003726](http://purl.obolibrary.org/obo/UBERON_0003726) |
| `MESH:A04.760`                     |              1 | [UBERON:0004785](http://purl.obolibrary.org/obo/UBERON_0004785) |
| `MESH:A07.231.114.565`             |              1 | [UBERON:0005616](http://purl.obolibrary.org/obo/UBERON_0005616) |
| `MESH:A07.231.908.670.385`         |              1 | [UBERON:0005617](http://purl.obolibrary.org/obo/UBERON_0005617) |
| `MESH:A12.207`                     |              1 | [UBERON:0006314](http://purl.obolibrary.org/obo/UBERON_0006314) |
| `MESH:A07.231.432`                 |              1 | [UBERON:0010523](http://purl.obolibrary.org/obo/UBERON_0010523) |
| `MESH:A08.663.542.122`             |              1 | [UBERON:0011925](http://purl.obolibrary.org/obo/UBERON_0011925) |

## `MGI`: Mouse Genome Informatics

Overall, there were 49 invalid
xrefs to external prefixed with `MGI` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MGI:csmith`    |             19 | [UBERON:0001166](http://purl.obolibrary.org/obo/UBERON_0001166), [UBERON:0001167](http://purl.obolibrary.org/obo/UBERON_0001167), [UBERON:0001174](http://purl.obolibrary.org/obo/UBERON_0001174), [UBERON:0001200](http://purl.obolibrary.org/obo/UBERON_0001200), [UBERON:0001201](http://purl.obolibrary.org/obo/UBERON_0001201), ... |
| `MGI:anna`      |             12 | [UBERON:0000076](http://purl.obolibrary.org/obo/UBERON_0000076), [UBERON:0000114](http://purl.obolibrary.org/obo/UBERON_0000114), [UBERON:0000325](http://purl.obolibrary.org/obo/UBERON_0000325), [UBERON:0001070](http://purl.obolibrary.org/obo/UBERON_0001070), [UBERON:0001532](http://purl.obolibrary.org/obo/UBERON_0001532), ... |
| `MGI:cwg`       |              9 | [UBERON:0001013](http://purl.obolibrary.org/obo/UBERON_0001013), [UBERON:0001901](http://purl.obolibrary.org/obo/UBERON_0001901), [UBERON:0002173](http://purl.obolibrary.org/obo/UBERON_0002173), [UBERON:0002185](http://purl.obolibrary.org/obo/UBERON_0002185), [UBERON:0002186](http://purl.obolibrary.org/obo/UBERON_0002186), ... |
| `MGI:smb`       |              4 | [UBERON:0001772](http://purl.obolibrary.org/obo/UBERON_0001772), [UBERON:0001804](http://purl.obolibrary.org/obo/UBERON_0001804), [UBERON:0003604](http://purl.obolibrary.org/obo/UBERON_0003604), [UBERON:0014389](http://purl.obolibrary.org/obo/UBERON_0014389)                                                                       |
| `MGI:pvb`       |              1 | [UBERON:0000087](http://purl.obolibrary.org/obo/UBERON_0000087)                                                                                                                                                                                                                                                                          |
| `MGI:rbabiuk`   |              1 | [UBERON:0001213](http://purl.obolibrary.org/obo/UBERON_0001213)                                                                                                                                                                                                                                                                          |
| `MGI:monikat`   |              1 | [UBERON:0002511](http://purl.obolibrary.org/obo/UBERON_0002511)                                                                                                                                                                                                                                                                          |
| `MGI:Anna`      |              1 | [UBERON:0005203](http://purl.obolibrary.org/obo/UBERON_0005203)                                                                                                                                                                                                                                                                          |
| `MGI:cs`        |              1 | [UBERON:0034932](http://purl.obolibrary.org/obo/UBERON_0034932)                                                                                                                                                                                                                                                                          |

## `MP`: Mammalian Phenotype Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `MP` (standardized to Bioregistry
prefix [`mp`](https://bioregistry.io/mp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `MP:MP`         |              1 | [UBERON:0008835](http://purl.obolibrary.org/obo/UBERON_0008835) |

## `NCI_Thesaurus`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCI_Thesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^[CRPA]\d+$`.

| external_xref                                   |   usages_count | usages                                                  |
|-------------------------------------------------|----------------|---------------------------------------------------------|
| `NCI_Thesaurus:Small_Intestinal_Glandular_Cell` |              1 | [CL:1001598](http://purl.obolibrary.org/obo/CL_1001598) |

## `NCIT`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCIT` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^[CRPA]\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `NCIT:NCIT`     |              1 | [UBERON:0010499](http://purl.obolibrary.org/obo/UBERON_0010499) |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 32 invalid
xrefs to external prefixed with `ncithesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^[CRPA]\d+$`.

| external_xref                                        |   usages_count | usages                                                          |
|------------------------------------------------------|----------------|-----------------------------------------------------------------|
| `ncithesaurus:Abdominal_Wall`                        |              1 | [UBERON:0003697](http://purl.obolibrary.org/obo/UBERON_0003697) |
| `ncithesaurus:Splenic_Vein`                          |              1 | [UBERON:0003713](http://purl.obolibrary.org/obo/UBERON_0003713) |
| `ncithesaurus:Cortical_Cell_Layer_of_the_Cerebellum` |              1 | [UBERON:0004130](http://purl.obolibrary.org/obo/UBERON_0004130) |
| `ncithesaurus:Bowman_s_Membrane`                     |              1 | [UBERON:0004370](http://purl.obolibrary.org/obo/UBERON_0004370) |
| `ncithesaurus:Aortic_Segment`                        |              1 | [UBERON:0005800](http://purl.obolibrary.org/obo/UBERON_0005800) |
| `ncithesaurus:Myelinated_Nerve_Fiber`                |              1 | [UBERON:0006135](http://purl.obolibrary.org/obo/UBERON_0006135) |
| `ncithesaurus:Communicating_Artery`                  |              1 | [UBERON:0006347](http://purl.obolibrary.org/obo/UBERON_0006347) |
| `ncithesaurus:Lobe`                                  |              1 | [UBERON:0009912](http://purl.obolibrary.org/obo/UBERON_0009912) |
| `ncithesaurus:Pulmonary_Lobule`                      |              1 | [UBERON:0010368](http://purl.obolibrary.org/obo/UBERON_0010368) |
| `ncithesaurus:Phrenic_Vein`                          |              1 | [UBERON:0012193](http://purl.obolibrary.org/obo/UBERON_0012193) |
| `ncithesaurus:Systemic_Vein`                         |              1 | [UBERON:0013140](http://purl.obolibrary.org/obo/UBERON_0013140) |
| `ncithesaurus:Choroidal_Artery`                      |              1 | [UBERON:0013151](http://purl.obolibrary.org/obo/UBERON_0013151) |
| `ncithesaurus:Interlobular_Duct`                     |              1 | [UBERON:0014716](http://purl.obolibrary.org/obo/UBERON_0014716) |
| `ncithesaurus:Perivascular_Space`                    |              1 | [UBERON:0014930](http://purl.obolibrary.org/obo/UBERON_0014930) |
| `ncithesaurus:Right_Ear`                             |              1 | [UBERON:0035174](http://purl.obolibrary.org/obo/UBERON_0035174) |
| `ncithesaurus:Left_Ear`                              |              1 | [UBERON:0035295](http://purl.obolibrary.org/obo/UBERON_0035295) |
| `ncithesaurus:Esophageal_Artery`                     |              1 | [UBERON:0035539](http://purl.obolibrary.org/obo/UBERON_0035539) |
| `ncithesaurus:Superficial_Vein`                      |              1 | [UBERON:0035550](http://purl.obolibrary.org/obo/UBERON_0035550) |
| `ncithesaurus:Deep_Vein`                             |              1 | [UBERON:0035552](http://purl.obolibrary.org/obo/UBERON_0035552) |
| `ncithesaurus:Egg`                                   |              1 | [CL:0000021](http://purl.obolibrary.org/obo/CL_0000021)         |
| `ncithesaurus:Beta_Cell`                             |              1 | [CL:0000169](http://purl.obolibrary.org/obo/CL_0000169)         |
| `ncithesaurus:Life`                                  |              1 | [UBERON:0000104](http://purl.obolibrary.org/obo/UBERON_0000104) |
| `ncithesaurus:Developmental_Stage`                   |              1 | [UBERON:0000105](http://purl.obolibrary.org/obo/UBERON_0000105) |
| `ncithesaurus:Atlanto-occipital_Joint-Atlanto`       |              1 | [UBERON:0000220](http://purl.obolibrary.org/obo/UBERON_0000220) |
| `ncithesaurus:Whole_Organism`                        |              1 | [UBERON:0000468](http://purl.obolibrary.org/obo/UBERON_0000468) |
| `ncithesaurus:Digestive_System`                      |              1 | [UBERON:0001007](http://purl.obolibrary.org/obo/UBERON_0001007) |
| `ncithesaurus:Pleural_Fluid`                         |              1 | [UBERON:0001087](http://purl.obolibrary.org/obo/UBERON_0001087) |
| `ncithesaurus:Heart_Muscle`                          |              1 | [UBERON:0001133](http://purl.obolibrary.org/obo/UBERON_0001133) |
| `ncithesaurus:Peritoneal_Fluid`                      |              1 | [UBERON:0001268](http://purl.obolibrary.org/obo/UBERON_0001268) |
| `ncithesaurus:Upper_Jaw`                             |              1 | [UBERON:0001709](http://purl.obolibrary.org/obo/UBERON_0001709) |
| `ncithesaurus:Lower_Jaw`                             |              1 | [UBERON:0001710](http://purl.obolibrary.org/obo/UBERON_0001710) |
| `ncithesaurus:Transudate`                            |              1 | [UBERON:0007779](http://purl.obolibrary.org/obo/UBERON_0007779) |

## `NIF_Subcellular`: NIF Standard Ontology: Subcellular Entities

Overall, there were 52 invalid
xrefs to external prefixed with `NIF_Subcellular` (standardized to Bioregistry
prefix [`nlx.sub`](https://bioregistry.io/nlx.sub)) that
did not match the standard pattern `^\d+$`.

| external_xref                          |   usages_count | usages                                                                                                           |
|----------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `NIF_Subcellular:nlx_subcell_20090513` |              2 | [GO:0031012](http://purl.obolibrary.org/obo/GO_0031012), [GO:0031012](http://purl.obolibrary.org/obo/GO_0031012) |
| `NIF_Subcellular:sao772007592`         |              2 | [GO:0031045](http://purl.obolibrary.org/obo/GO_0031045), [GO:0031045](http://purl.obolibrary.org/obo/GO_0031045) |
| `NIF_Subcellular:sao593830697`         |              2 | [GO:0043209](http://purl.obolibrary.org/obo/GO_0043209), [GO:0043209](http://purl.obolibrary.org/obo/GO_0043209) |
| `NIF_Subcellular:sao1872343973`        |              2 | [GO:0097427](http://purl.obolibrary.org/obo/GO_0097427), [GO:0097427](http://purl.obolibrary.org/obo/GO_0097427) |
| `NIF_Subcellular:sao1890444066`        |              2 | [GO:0097454](http://purl.obolibrary.org/obo/GO_0097454), [GO:0097454](http://purl.obolibrary.org/obo/GO_0097454) |
| `NIF_Subcellular:sao707332678`         |              2 | [GO:1901589](http://purl.obolibrary.org/obo/GO_1901589), [GO:1901589](http://purl.obolibrary.org/obo/GO_1901589) |
| `NIF_Subcellular:sao1615953555`        |              1 | [GO:0000785](http://purl.obolibrary.org/obo/GO_0000785)                                                          |
| `NIF_Subcellular:sao445485807`         |              1 | [GO:0000791](http://purl.obolibrary.org/obo/GO_0000791)                                                          |
| `NIF_Subcellular:sao581845896`         |              1 | [GO:0000792](http://purl.obolibrary.org/obo/GO_0000792)                                                          |
| `NIF_Subcellular:sao1337158144`        |              1 | [GO:0005575](http://purl.obolibrary.org/obo/GO_0005575)                                                          |
| `NIF_Subcellular:sao1425028079`        |              1 | [GO:0005615](http://purl.obolibrary.org/obo/GO_0005615)                                                          |
| `NIF_Subcellular:sao1702920020`        |              1 | [GO:0005634](http://purl.obolibrary.org/obo/GO_0005634)                                                          |
| `NIF_Subcellular:sao1617136075`        |              1 | [GO:0005640](http://purl.obolibrary.org/obo/GO_0005640)                                                          |
| `NIF_Subcellular:sao1820400233`        |              1 | [GO:0005730](http://purl.obolibrary.org/obo/GO_0005730)                                                          |
| `NIF_Subcellular:sao585356902`         |              1 | [GO:0005764](http://purl.obolibrary.org/obo/GO_0005764)                                                          |
| `NIF_Subcellular:sao1140587416`        |              1 | [GO:0005766](http://purl.obolibrary.org/obo/GO_0005766)                                                          |
| `NIF_Subcellular:sao451912436`         |              1 | [GO:0005794](http://purl.obolibrary.org/obo/GO_0005794)                                                          |
| `NIF_Subcellular:sao819927218`         |              1 | [GO:0005798](http://purl.obolibrary.org/obo/GO_0005798)                                                          |
| `NIF_Subcellular:sao95019936`          |              1 | [GO:0005814](http://purl.obolibrary.org/obo/GO_0005814)                                                          |
| `NIF_Subcellular:sao101633890`         |              1 | [GO:0005829](http://purl.obolibrary.org/obo/GO_0005829)                                                          |
| `NIF_Subcellular:sao1429207766`        |              1 | [GO:0005840](http://purl.obolibrary.org/obo/GO_0005840)                                                          |
| `NIF_Subcellular:sao1846835077`        |              1 | [GO:0005874](http://purl.obolibrary.org/obo/GO_0005874)                                                          |
| `NIF_Subcellular:sao952483289`         |              1 | [GO:0005882](http://purl.obolibrary.org/obo/GO_0005882)                                                          |
| `NIF_Subcellular:sao1588493326`        |              1 | [GO:0005884](http://purl.obolibrary.org/obo/GO_0005884)                                                          |
| `NIF_Subcellular:sao1663586795`        |              1 | [GO:0005886](http://purl.obolibrary.org/obo/GO_0005886)                                                          |
| `NIF_Subcellular:sao671419673`         |              1 | [GO:0005902](http://purl.obolibrary.org/obo/GO_0005902)                                                          |
| `NIF_Subcellular:sao1922892319`        |              1 | [GO:0005911](http://purl.obolibrary.org/obo/GO_0005911)                                                          |
| `NIF_Subcellular:sao787716553`         |              1 | [GO:0005929](http://purl.obolibrary.org/obo/GO_0005929)                                                          |
| `NIF_Subcellular:sao1153182838`        |              1 | [GO:0012506](http://purl.obolibrary.org/obo/GO_0012506)                                                          |
| `NIF_Subcellular:sao885490876`         |              1 | [GO:0030133](http://purl.obolibrary.org/obo/GO_0030133)                                                          |
| `NIF_Subcellular:sao1770195789`        |              1 | [GO:0030424](http://purl.obolibrary.org/obo/GO_0030424)                                                          |
| `NIF_Subcellular:sao830981606`         |              1 | [GO:0031090](http://purl.obolibrary.org/obo/GO_0031090)                                                          |
| `NIF_Subcellular:sao180601769`         |              1 | [GO:0031410](http://purl.obolibrary.org/obo/GO_0031410)                                                          |
| `NIF_Subcellular:sao1124888485`        |              1 | [GO:0031594](http://purl.obolibrary.org/obo/GO_0031594)                                                          |
| `NIF_Subcellular:sao1687101204`        |              1 | [GO:0031965](http://purl.obolibrary.org/obo/GO_0031965)                                                          |
| `NIF_Subcellular:sao221389602`         |              1 | [GO:0031982](http://purl.obolibrary.org/obo/GO_0031982)                                                          |
| `NIF_Subcellular:sao11978067`          |              1 | [GO:0036064](http://purl.obolibrary.org/obo/GO_0036064)                                                          |
| `NIF_Subcellular:sao867568886`         |              1 | [GO:0043005](http://purl.obolibrary.org/obo/GO_0043005)                                                          |
| `NIF_Subcellular:sao1044911821`        |              1 | [GO:0043025](http://purl.obolibrary.org/obo/GO_0043025)                                                          |
| `NIF_Subcellular:sao1539965131`        |              1 | [GO:0043226](http://purl.obolibrary.org/obo/GO_0043226)                                                          |
| `NIF_Subcellular:sao414196390`         |              1 | [GO:0043227](http://purl.obolibrary.org/obo/GO_0043227)                                                          |
| `NIF_Subcellular:sao1456184038`        |              1 | [GO:0043228](http://purl.obolibrary.org/obo/GO_0043228)                                                          |
| `NIF_Subcellular:sao914572699`         |              1 | [GO:0045202](http://purl.obolibrary.org/obo/GO_0045202)                                                          |
| `NIF_Subcellular:sao1397492660`        |              1 | [UBERON:0000482](http://purl.obolibrary.org/obo/UBERON_0000482)                                                  |
| `NIF_Subcellular:sao1145756102`        |              1 | [UBERON:0001130](http://purl.obolibrary.org/obo/UBERON_0001130)                                                  |
| `NIF_Subcellular:sao7547390221`        |              1 | [UBERON:0011860](http://purl.obolibrary.org/obo/UBERON_0011860)                                                  |

## `NIFSTD`: NIF Standard Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `NIFSTD` (standardized to Bioregistry
prefix [`nif.std`](https://bioregistry.io/nif.std)) that
did not match the standard pattern `^BAMSC\d+$`.

| external_xref          |   usages_count | usages                                                          |
|------------------------|----------------|-----------------------------------------------------------------|
| `NIFSTD:sao1415726815` |              1 | [CL:0000119](http://purl.obolibrary.org/obo/CL_0000119)         |
| `NIFSTD:FMAID_7191`    |              1 | [UBERON:0002104](http://purl.obolibrary.org/obo/UBERON_0002104) |
| `NIFSTD:sao862606388`  |              1 | [CL:0000598](http://purl.obolibrary.org/obo/CL_0000598)         |

## `NLM`: National Library of Medicine Catalog

Overall, there were 3 invalid
xrefs to external prefixed with `NLM` (standardized to Bioregistry
prefix [`nlm`](https://bioregistry.io/nlm)) that
did not match the standard pattern `^\d+$`.

| external_xref           |   usages_count | usages                                                          |
|-------------------------|----------------|-----------------------------------------------------------------|
| `NLM:endocrine+system`  |              1 | [UBERON:0000949](http://purl.obolibrary.org/obo/UBERON_0000949) |
| `NLM:alimentary+system` |              1 | [UBERON:0001007](http://purl.obolibrary.org/obo/UBERON_0001007) |
| `NLM:nervous+system`    |              1 | [UBERON:0001016](http://purl.obolibrary.org/obo/UBERON_0001016) |

## `SO`: Sequence types and features ontology

Overall, there were 6 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                                                                                                                                                    |
|----------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SO:ke`              |              3 | [SO:0000001](http://purl.obolibrary.org/obo/SO_0000001), [SO:0000110](http://purl.obolibrary.org/obo/SO_0000110), [SO:0001260](http://purl.obolibrary.org/obo/SO_0001260) |
| `SO:immuno_workshop` |              1 | [SO:0000704](http://purl.obolibrary.org/obo/SO_0000704)                                                                                                                   |
| `SO:cb`              |              1 | [SO:0001411](http://purl.obolibrary.org/obo/SO_0001411)                                                                                                                   |
| `SO:ma`              |              1 | [SO:0005855](http://purl.obolibrary.org/obo/SO_0005855)                                                                                                                   |

## `TAO`: Teleost Anatomy Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `TAO` (standardized to Bioregistry
prefix [`tao`](https://bioregistry.io/tao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                           |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------|
| `TAO:curator`   |              2 | [UBERON:0005744](http://purl.obolibrary.org/obo/UBERON_0005744), [UBERON:0013685](http://purl.obolibrary.org/obo/UBERON_0013685) |
| `TAO:MAH`       |              1 | [UBERON:0001703](http://purl.obolibrary.org/obo/UBERON_0001703)                                                                  |

## `UBERON`: Uber Anatomy Ontology

Overall, there were 45 invalid
xrefs to external prefixed with `UBERON` (standardized to Bioregistry
prefix [`uberon`](https://bioregistry.io/uberon)) that
did not match the standard pattern `^\d+$`.

| external_xref      |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|--------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UBERON:cjm`       |             38 | [UBERON:0000004](http://purl.obolibrary.org/obo/UBERON_0000004), [UBERON:0000977](http://purl.obolibrary.org/obo/UBERON_0000977), [UBERON:0001027](http://purl.obolibrary.org/obo/UBERON_0001027), [UBERON:0001242](http://purl.obolibrary.org/obo/UBERON_0001242), [UBERON:0001277](http://purl.obolibrary.org/obo/UBERON_0001277), ... |
| `UBERON:xp`        |              2 | [UBERON:0003133](http://purl.obolibrary.org/obo/UBERON_0003133), [UBERON:0003134](http://purl.obolibrary.org/obo/UBERON_0003134)                                                                                                                                                                                                         |
| `UBERON:md`        |              2 | [UBERON:0013739](http://purl.obolibrary.org/obo/UBERON_0013739), [UBERON:0013740](http://purl.obolibrary.org/obo/UBERON_0013740)                                                                                                                                                                                                         |
| `UBERON:automatic` |              1 | [UBERON:0004766](http://purl.obolibrary.org/obo/UBERON_0004766)                                                                                                                                                                                                                                                                          |
| `UBERON:drseb`     |              1 | [UBERON:0019207](http://purl.obolibrary.org/obo/UBERON_0019207)                                                                                                                                                                                                                                                                          |
| `UBERON:EJS`       |              1 | [UBERON:1000021](http://purl.obolibrary.org/obo/UBERON_1000021)                                                                                                                                                                                                                                                                          |

## `VSAO`: Vertebrate Skeletal Anatomy Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `VSAO` (standardized to Bioregistry
prefix [`vsao`](https://bioregistry.io/vsao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref           |   usages_count | usages                                                          |
|-------------------------|----------------|-----------------------------------------------------------------|
| `VSAO:curator`          |              1 | [UBERON:0002204](http://purl.obolibrary.org/obo/UBERON_0002204) |
| `VSAO:0000150-modified` |              1 | [UBERON:0004710](http://purl.obolibrary.org/obo/UBERON_0004710) |
| `VSAO:NI`               |              1 | [UBERON:0007272](http://purl.obolibrary.org/obo/UBERON_0007272) |

## `WB`: WormBase

Overall, there were 1 invalid
xrefs to external prefixed with `WB` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^(CE[0-9]{5}|WB[A-Z][a-z]+\d+)$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `WB:rynl`       |              1 | [UBERON:0001016](http://purl.obolibrary.org/obo/UBERON_0001016) |

## `XAO`: Xenopus Anatomy Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `XAO` (standardized to Bioregistry
prefix [`xao`](https://bioregistry.io/xao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `XAO:curators`  |              1 | [UBERON:0009500](http://purl.obolibrary.org/obo/UBERON_0009500) |
| `XAO:EJS`       |              1 | [UBERON:0015179](http://purl.obolibrary.org/obo/UBERON_0015179) |

## `ZFA`: Zebrafish anatomy and development ontology

Overall, there were 5 invalid
xrefs to external prefixed with `ZFA` (standardized to Bioregistry
prefix [`zfa`](https://bioregistry.io/zfa)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                            |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFA:curator`   |              3 | [UBERON:0008229](http://purl.obolibrary.org/obo/UBERON_0008229), [UBERON:0014371](http://purl.obolibrary.org/obo/UBERON_0014371), [UBERON:0014903](http://purl.obolibrary.org/obo/UBERON_0014903) |
| `ZFA:yb`        |              1 | [UBERON:0002539](http://purl.obolibrary.org/obo/UBERON_0002539)                                                                                                                                   |
| `ZFA:CVS`       |              1 | [UBERON:0018674](http://purl.obolibrary.org/obo/UBERON_0018674)                                                                                                                                   |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 37 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:curator`  |             35 | [UBERON:0000966](http://purl.obolibrary.org/obo/UBERON_0000966), [UBERON:0000991](http://purl.obolibrary.org/obo/UBERON_0000991), [UBERON:0001016](http://purl.obolibrary.org/obo/UBERON_0001016), [UBERON:0001081](http://purl.obolibrary.org/obo/UBERON_0001081), [UBERON:0001083](http://purl.obolibrary.org/obo/UBERON_0001083), ... |
| `ZFIN:dsf`      |              1 | [GO:0044458](http://purl.obolibrary.org/obo/GO_0044458)                                                                                                                                                                                                                                                                                  |
| `ZFIN:yb`       |              1 | [UBERON:0003066](http://purl.obolibrary.org/obo/UBERON_0003066)                                                                                                                                                                                                                                                                          |

