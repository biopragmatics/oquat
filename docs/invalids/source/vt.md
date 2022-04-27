# vt

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vt`. See the [GitHub repository](https://github.com/AnimalGenome/vertebrate-trait-ontology)


## `MESH`: Medical Subject Headings

- Normalized prefix: `mesh`
- [https://bioregistry.io/mesh](https://bioregistry.io/mesh)
- Pattern:`^(C|D)\d{6,9}$`

| identifier             |   appearances | examples                                        |
|------------------------|---------------|-------------------------------------------------|
| `MESH:D12.776.034.145` |             1 | [VT:0002484](https://bioregistry.io/VT:0002484) |
| `MESH:D12.776.049.790` |             1 | [VT:0002486](https://bioregistry.io/VT:0002486) |

## `MeSH`: Medical Subject Headings

- Normalized prefix: `mesh`
- [https://bioregistry.io/mesh](https://bioregistry.io/mesh)
- Pattern:`^(C|D)\d{6,9}$`

| identifier                     |   appearances | examples                                        |
|--------------------------------|---------------|-------------------------------------------------|
| `MeSH:D12.776.049.790`         |             1 | [VT:0010037](https://bioregistry.io/VT:0010037) |
| `MeSH:D12.644.276.374.500.800` |             1 | [VT:0010160](https://bioregistry.io/VT:0010160) |

## `MGI`: Mouse Genome Informatics

- Normalized prefix: `mgi`
- [https://bioregistry.io/mgi](https://bioregistry.io/mgi)
- Pattern:`^\d+$`

| identifier   |   appearances | examples                                                                                                                                                                                                                                                 |
|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MGI:smb`    |            73 | [VT:0000976](https://bioregistry.io/VT:0000976), [VT:0015031](https://bioregistry.io/VT:0015031), [VT:0015053](https://bioregistry.io/VT:0015053), [VT:0015059](https://bioregistry.io/VT:0015059), [VT:0015068](https://bioregistry.io/VT:0015068), ... |
| `MGI:cwg`    |            22 | [VT:0000179](https://bioregistry.io/VT:0000179), [VT:0002723](https://bioregistry.io/VT:0002723), [VT:0002723](https://bioregistry.io/VT:0002723), [VT:0010171](https://bioregistry.io/VT:0010171), [VT:0010172](https://bioregistry.io/VT:0010172), ... |
| `MGI:MP`     |            20 | [VT:0000896](https://bioregistry.io/VT:0000896), [VT:0000896](https://bioregistry.io/VT:0000896), [VT:0001052](https://bioregistry.io/VT:0001052), [VT:0002124](https://bioregistry.io/VT:0002124), [VT:0003713](https://bioregistry.io/VT:0003713), ... |
| `MGI:csmith` |            12 | [VT:0000977](https://bioregistry.io/VT:0000977), [VT:0001332](https://bioregistry.io/VT:0001332), [VT:0001884](https://bioregistry.io/VT:0001884), [VT:0002085](https://bioregistry.io/VT:0002085), [VT:0002093](https://bioregistry.io/VT:0002093), ... |
| `MGI:mb`     |            10 | [VT:0010472](https://bioregistry.io/VT:0010472), [VT:0010472](https://bioregistry.io/VT:0010472), [VT:0010512](https://bioregistry.io/VT:0010512), [VT:0010512](https://bioregistry.io/VT:0010512), [VT:0010692](https://bioregistry.io/VT:0010692), ... |
| `MGI:anna`   |             2 | [VT:0004291](https://bioregistry.io/VT:0004291), [VT:0006028](https://bioregistry.io/VT:0006028)                                                                                                                                                         |
| `MGI:brs`    |             1 | [VT:0003847](https://bioregistry.io/VT:0003847)                                                                                                                                                                                                          |
| `MGI:hdene`  |             1 | [VT:0010158](https://bioregistry.io/VT:0010158)                                                                                                                                                                                                          |
| `MGI:pvb`    |             1 | [VT:0010162](https://bioregistry.io/VT:0010162)                                                                                                                                                                                                          |

## `MP`: Mammalian Phenotype Ontology

- Normalized prefix: `mp`
- [https://bioregistry.io/mp](https://bioregistry.io/mp)
- Pattern:`^\d{7}$`

| identifier              |   appearances | examples                                        |
|-------------------------|---------------|-------------------------------------------------|
| `MP:001324`             |             1 | [VT:0001324](https://bioregistry.io/VT:0001324) |
| `MP:00004293`           |             1 | [VT:0004293](https://bioregistry.io/VT:0004293) |
| `MP:MammalianPhenotype` |             1 | [VT:0010442](https://bioregistry.io/VT:0010442) |
| `MP:00003257`           |             1 | [VT:0010453](https://bioregistry.io/VT:0010453) |

## `MS`: Mass spectrometry ontology

- Normalized prefix: `ms`
- [https://bioregistry.io/ms](https://bioregistry.io/ms)
- Pattern:`^\d{7}$`

| identifier   |   appearances | examples                                                                                                                                                                                           |
|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MS:RGD`     |             4 | [VT:0000466](https://bioregistry.io/VT:0000466), [VT:0010213](https://bioregistry.io/VT:0010213), [VT:0010239](https://bioregistry.io/VT:0010239), [VT:1000711](https://bioregistry.io/VT:1000711) |

## `PMID`: PubMed

- Normalized prefix: `pubmed`
- [https://bioregistry.io/pubmed](https://bioregistry.io/pubmed)
- Pattern:`^\d+$`

| identifier           |   appearances | examples                                        |
|----------------------|---------------|-------------------------------------------------|
| `PMID:0-87893-258-5` |             1 | [VT:0003359](https://bioregistry.io/VT:0003359) |

## `RGD`: Rat Genome Database

- Normalized prefix: `rgd`
- [https://bioregistry.io/rgd](https://bioregistry.io/rgd)
- Pattern:`^\d{4,}$`

| identifier   |   appearances | examples                                                                                                                                                                                                                                                 |
|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RGD:cur`    |           198 | [VT:0010564](https://bioregistry.io/VT:0010564), [VT:0010706](https://bioregistry.io/VT:0010706), [VT:0010764](https://bioregistry.io/VT:0010764), [VT:0010776](https://bioregistry.io/VT:0010776), [VT:0010779](https://bioregistry.io/VT:0010779), ... |
| `RGD:MS`     |            62 | [VT:0001661](https://bioregistry.io/VT:0001661), [VT:0001757](https://bioregistry.io/VT:0001757), [VT:0100028](https://bioregistry.io/VT:0100028), [VT:1000197](https://bioregistry.io/VT:1000197), [VT:1000205](https://bioregistry.io/VT:1000205), ... |
| `RGD:dhm`    |            55 | [VT:0000189](https://bioregistry.io/VT:0000189), [VT:0000189](https://bioregistry.io/VT:0000189), [VT:0000341](https://bioregistry.io/VT:0000341), [VT:0001756](https://bioregistry.io/VT:0001756), [VT:4000009](https://bioregistry.io/VT:4000009), ... |
| `RGD:ms`     |            18 | [VT:0002295](https://bioregistry.io/VT:0002295), [VT:0002504](https://bioregistry.io/VT:0002504), [VT:0002792](https://bioregistry.io/VT:0002792), [VT:0002792](https://bioregistry.io/VT:0002792), [VT:0002937](https://bioregistry.io/VT:0002937), ... |

## `RGD `: Rat Genome Database

- Normalized prefix: `rgd`
- [https://bioregistry.io/rgd](https://bioregistry.io/rgd)
- Pattern:`^\d{4,}$`

| identifier   |   appearances | examples                                        |
|--------------|---------------|-------------------------------------------------|
| `RGD :MS`    |             1 | [VT:0010265](https://bioregistry.io/VT:0010265) |

## `VTO`: Vertebrate Taxonomy Ontology

- Normalized prefix: `vto`
- [https://bioregistry.io/vto](https://bioregistry.io/vto)
- Pattern:`^\d{7}$`

| identifier   |   appearances | examples                                                                                                                                                                                                                                                 |
|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `VTO:INRA`   |           229 | [VT:0010314](https://bioregistry.io/VT:0010314), [VT:0010314](https://bioregistry.io/VT:0010314), [VT:0010402](https://bioregistry.io/VT:0010402), [VT:0010966](https://bioregistry.io/VT:0010966), [VT:1000226](https://bioregistry.io/VT:1000226), ... |
| `VTO:CP`     |           224 | [VT:0010316](https://bioregistry.io/VT:0010316), [VT:0010336](https://bioregistry.io/VT:0010336), [VT:0010356](https://bioregistry.io/VT:0010356), [VT:1000067](https://bioregistry.io/VT:1000067), [VT:1000528](https://bioregistry.io/VT:1000528), ... |

