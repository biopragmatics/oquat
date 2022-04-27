# vt

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vt`. See the [GitHub repository](https://github.com/AnimalGenome/vertebrate-trait-ontology).


## `MESH`: Medical Subject Headings

Overall, there were 2 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
entry [`mesh`]((https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref          |   usages_count | usages                                          |
|------------------------|----------------|-------------------------------------------------|
| `MESH:D12.776.034.145` |              1 | [VT:0002484](https://bioregistry.io/VT:0002484) |
| `MESH:D12.776.049.790` |              1 | [VT:0002486](https://bioregistry.io/VT:0002486) |

## `MeSH`: Medical Subject Headings

Overall, there were 2 invalid
xrefs to external prefixed with `MeSH` (standardized to Bioregistry
entry [`mesh`]((https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                  |   usages_count | usages                                          |
|--------------------------------|----------------|-------------------------------------------------|
| `MeSH:D12.776.049.790`         |              1 | [VT:0010037](https://bioregistry.io/VT:0010037) |
| `MeSH:D12.644.276.374.500.800` |              1 | [VT:0010160](https://bioregistry.io/VT:0010160) |

## `MGI`: Mouse Genome Informatics

Overall, there were 142 invalid
xrefs to external prefixed with `MGI` (standardized to Bioregistry
entry [`mgi`]((https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                   |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MGI:smb`       |             73 | [VT:0000013](https://bioregistry.io/VT:0000013), [VT:0000061](https://bioregistry.io/VT:0000061), [VT:0000135](https://bioregistry.io/VT:0000135), [VT:0000179](https://bioregistry.io/VT:0000179), [VT:0000269](https://bioregistry.io/VT:0000269), ... |
| `MGI:cwg`       |             22 | [VT:0000023](https://bioregistry.io/VT:0000023), [VT:0000179](https://bioregistry.io/VT:0000179), [VT:0001777](https://bioregistry.io/VT:0001777), [VT:0002204](https://bioregistry.io/VT:0002204), [VT:0002278](https://bioregistry.io/VT:0002278), ... |
| `MGI:MP`        |             20 | [VT:0000023](https://bioregistry.io/VT:0000023), [VT:0000895](https://bioregistry.io/VT:0000895), [VT:0000896](https://bioregistry.io/VT:0000896), [VT:0000968](https://bioregistry.io/VT:0000968), [VT:0000974](https://bioregistry.io/VT:0000974), ... |
| `MGI:csmith`    |             12 | [VT:0000940](https://bioregistry.io/VT:0000940), [VT:0000977](https://bioregistry.io/VT:0000977), [VT:0001332](https://bioregistry.io/VT:0001332), [VT:0001747](https://bioregistry.io/VT:0001747), [VT:0001884](https://bioregistry.io/VT:0001884), ... |
| `MGI:mb`        |             10 | [VT:0010471](https://bioregistry.io/VT:0010471), [VT:0010472](https://bioregistry.io/VT:0010472), [VT:0010474](https://bioregistry.io/VT:0010474), [VT:0010512](https://bioregistry.io/VT:0010512), [VT:0010689](https://bioregistry.io/VT:0010689), ... |
| `MGI:anna`      |              2 | [VT:0004291](https://bioregistry.io/VT:0004291), [VT:0006028](https://bioregistry.io/VT:0006028)                                                                                                                                                         |
| `MGI:brs`       |              1 | [VT:0003847](https://bioregistry.io/VT:0003847)                                                                                                                                                                                                          |
| `MGI:hdene`     |              1 | [VT:0010158](https://bioregistry.io/VT:0010158)                                                                                                                                                                                                          |
| `MGI:pvb`       |              1 | [VT:0010162](https://bioregistry.io/VT:0010162)                                                                                                                                                                                                          |

## `MP`: Mammalian Phenotype Ontology

Overall, there were 4 invalid
xrefs to external prefixed with `MP` (standardized to Bioregistry
entry [`mp`]((https://bioregistry.io/mp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref           |   usages_count | usages                                          |
|-------------------------|----------------|-------------------------------------------------|
| `MP:001324`             |              1 | [VT:0001324](https://bioregistry.io/VT:0001324) |
| `MP:00004293`           |              1 | [VT:0004293](https://bioregistry.io/VT:0004293) |
| `MP:MammalianPhenotype` |              1 | [VT:0010442](https://bioregistry.io/VT:0010442) |
| `MP:00003257`           |              1 | [VT:0010453](https://bioregistry.io/VT:0010453) |

## `MS`: Mass spectrometry ontology

Overall, there were 4 invalid
xrefs to external prefixed with `MS` (standardized to Bioregistry
entry [`ms`]((https://bioregistry.io/ms)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                             |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MS:RGD`        |              4 | [VT:0000466](https://bioregistry.io/VT:0000466), [VT:0010213](https://bioregistry.io/VT:0010213), [VT:0010239](https://bioregistry.io/VT:0010239), [VT:1000711](https://bioregistry.io/VT:1000711) |

## `PMID`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
entry [`pubmed`]((https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref        |   usages_count | usages                                          |
|----------------------|----------------|-------------------------------------------------|
| `PMID:0-87893-258-5` |              1 | [VT:0003359](https://bioregistry.io/VT:0003359) |

## `RGD`: Rat Genome Database

Overall, there were 333 invalid
xrefs to external prefixed with `RGD` (standardized to Bioregistry
entry [`rgd`]((https://bioregistry.io/rgd)) that
did not match the standard pattern `^\d{4,}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                   |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RGD:cur`       |            198 | [VT:0002871](https://bioregistry.io/VT:0002871), [VT:0002928](https://bioregistry.io/VT:0002928), [VT:0002929](https://bioregistry.io/VT:0002929), [VT:0002932](https://bioregistry.io/VT:0002932), [VT:0003015](https://bioregistry.io/VT:0003015), ... |
| `RGD:MS`        |             62 | [VT:0000073](https://bioregistry.io/VT:0000073), [VT:0000222](https://bioregistry.io/VT:0000222), [VT:0000524](https://bioregistry.io/VT:0000524), [VT:0000535](https://bioregistry.io/VT:0000535), [VT:0000544](https://bioregistry.io/VT:0000544), ... |
| `RGD:dhm`       |             55 | [VT:0000050](https://bioregistry.io/VT:0000050), [VT:0000066](https://bioregistry.io/VT:0000066), [VT:0000153](https://bioregistry.io/VT:0000153), [VT:0000154](https://bioregistry.io/VT:0000154), [VT:0000170](https://bioregistry.io/VT:0000170), ... |
| `RGD:ms`        |             18 | [VT:0002128](https://bioregistry.io/VT:0002128), [VT:0002295](https://bioregistry.io/VT:0002295), [VT:0002504](https://bioregistry.io/VT:0002504), [VT:0002726](https://bioregistry.io/VT:0002726), [VT:0002792](https://bioregistry.io/VT:0002792), ... |

## `RGD `: Rat Genome Database

Overall, there were 1 invalid
xrefs to external prefixed with `RGD ` (standardized to Bioregistry
entry [`rgd`]((https://bioregistry.io/rgd)) that
did not match the standard pattern `^\d{4,}$`.

| external_xref   |   usages_count | usages                                          |
|-----------------|----------------|-------------------------------------------------|
| `RGD :MS`       |              1 | [VT:0010265](https://bioregistry.io/VT:0010265) |

## `VTO`: Vertebrate Taxonomy Ontology

Overall, there were 453 invalid
xrefs to external prefixed with `VTO` (standardized to Bioregistry
entry [`vto`]((https://bioregistry.io/vto)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                   |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `VTO:INRA`      |            229 | [VT:0001131](https://bioregistry.io/VT:0001131), [VT:0010001](https://bioregistry.io/VT:0010001), [VT:0010004](https://bioregistry.io/VT:0010004), [VT:0010018](https://bioregistry.io/VT:0010018), [VT:0010029](https://bioregistry.io/VT:0010029), ... |
| `VTO:CP`        |            224 | [VT:0000001](https://bioregistry.io/VT:0000001), [VT:0000009](https://bioregistry.io/VT:0000009), [VT:0000072](https://bioregistry.io/VT:0000072), [VT:0000116](https://bioregistry.io/VT:0000116), [VT:0000444](https://bioregistry.io/VT:0000444), ... |

