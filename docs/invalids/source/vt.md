# vt

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vt`. See the [GitHub repository](https://github.com/AnimalGenome/vertebrate-trait-ontology)


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
| `MGI:smb`       |             73 | [VT:0003449](https://bioregistry.io/VT:0003449), [VT:0004047](https://bioregistry.io/VT:0004047), [VT:0005372](https://bioregistry.io/VT:0005372), [VT:0007052](https://bioregistry.io/VT:0007052), [VT:0015073](https://bioregistry.io/VT:0015073), ... |
| `MGI:cwg`       |             22 | [VT:0010149](https://bioregistry.io/VT:0010149), [VT:0010167](https://bioregistry.io/VT:0010167), [VT:0010168](https://bioregistry.io/VT:0010168), [VT:0010168](https://bioregistry.io/VT:0010168), [VT:0010176](https://bioregistry.io/VT:0010176), ... |
| `MGI:MP`        |             20 | [VT:0000023](https://bioregistry.io/VT:0000023), [VT:0000979](https://bioregistry.io/VT:0000979), [VT:0001052](https://bioregistry.io/VT:0001052), [VT:0002483](https://bioregistry.io/VT:0002483), [VT:0015107](https://bioregistry.io/VT:0015107), ... |
| `MGI:csmith`    |             12 | [VT:0001332](https://bioregistry.io/VT:0001332), [VT:0001747](https://bioregistry.io/VT:0001747), [VT:0001884](https://bioregistry.io/VT:0001884), [VT:0002181](https://bioregistry.io/VT:0002181), [VT:0003795](https://bioregistry.io/VT:0003795), ... |
| `MGI:mb`        |             10 | [VT:0010471](https://bioregistry.io/VT:0010471), [VT:0010474](https://bioregistry.io/VT:0010474), [VT:0010691](https://bioregistry.io/VT:0010691), [VT:0010691](https://bioregistry.io/VT:0010691), [VT:0010708](https://bioregistry.io/VT:0010708), ... |
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
| `RGD:cur`       |            198 | [VT:0003241](https://bioregistry.io/VT:0003241), [VT:0005581](https://bioregistry.io/VT:0005581), [VT:0010737](https://bioregistry.io/VT:0010737), [VT:0010902](https://bioregistry.io/VT:0010902), [VT:0010936](https://bioregistry.io/VT:0010936), ... |
| `RGD:MS`        |             62 | [VT:0001010](https://bioregistry.io/VT:0001010), [VT:0007010](https://bioregistry.io/VT:0007010), [VT:0008739](https://bioregistry.io/VT:0008739), [VT:0010028](https://bioregistry.io/VT:0010028), [VT:1000197](https://bioregistry.io/VT:1000197), ... |
| `RGD:dhm`       |             55 | [VT:0000185](https://bioregistry.io/VT:0000185), [VT:0000197](https://bioregistry.io/VT:0000197), [VT:2000003](https://bioregistry.io/VT:2000003), [VT:2000005](https://bioregistry.io/VT:2000005), [VT:3000000](https://bioregistry.io/VT:3000000), ... |
| `RGD:ms`        |             18 | [VT:0002128](https://bioregistry.io/VT:0002128), [VT:0002504](https://bioregistry.io/VT:0002504), [VT:0003057](https://bioregistry.io/VT:0003057), [VT:0004124](https://bioregistry.io/VT:0004124), [VT:0004252](https://bioregistry.io/VT:0004252), ... |

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
| `VTO:INRA`      |            229 | [VT:0010320](https://bioregistry.io/VT:0010320), [VT:0010397](https://bioregistry.io/VT:0010397), [VT:0010977](https://bioregistry.io/VT:0010977), [VT:0010993](https://bioregistry.io/VT:0010993), [VT:0100033](https://bioregistry.io/VT:0100033), ... |
| `VTO:CP`        |            224 | [VT:0000072](https://bioregistry.io/VT:0000072), [VT:0010311](https://bioregistry.io/VT:0010311), [VT:0010358](https://bioregistry.io/VT:0010358), [VT:1000060](https://bioregistry.io/VT:1000060), [VT:1000518](https://bioregistry.io/VT:1000518), ... |

