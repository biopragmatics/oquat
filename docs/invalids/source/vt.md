# vt

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vt`. See the [GitHub repository](https://github.com/AnimalGenome/vertebrate-trait-ontology).


## `MESH`: Medical Subject Headings

Overall, there were 2 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref          |   usages_count | usages                                                  |
|------------------------|----------------|---------------------------------------------------------|
| `MESH:D12.776.034.145` |              1 | [VT:0002484](http://purl.obolibrary.org/obo/VT_0002484) |
| `MESH:D12.776.049.790` |              1 | [VT:0002486](http://purl.obolibrary.org/obo/VT_0002486) |

## `MeSH`: Medical Subject Headings

Overall, there were 2 invalid
xrefs to external prefixed with `MeSH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                  |   usages_count | usages                                                  |
|--------------------------------|----------------|---------------------------------------------------------|
| `MeSH:D12.776.049.790`         |              1 | [VT:0010037](http://purl.obolibrary.org/obo/VT_0010037) |
| `MeSH:D12.644.276.374.500.800` |              1 | [VT:0010160](http://purl.obolibrary.org/obo/VT_0010160) |

## `MGI`: Mouse Genome Informatics

Overall, there were 142 invalid
xrefs to external prefixed with `MGI` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MGI:smb`       |             73 | [VT:0000013](http://purl.obolibrary.org/obo/VT_0000013), [VT:0000061](http://purl.obolibrary.org/obo/VT_0000061), [VT:0000135](http://purl.obolibrary.org/obo/VT_0000135), [VT:0000179](http://purl.obolibrary.org/obo/VT_0000179), [VT:0000269](http://purl.obolibrary.org/obo/VT_0000269), ... |
| `MGI:cwg`       |             22 | [VT:0000023](http://purl.obolibrary.org/obo/VT_0000023), [VT:0000179](http://purl.obolibrary.org/obo/VT_0000179), [VT:0001777](http://purl.obolibrary.org/obo/VT_0001777), [VT:0002204](http://purl.obolibrary.org/obo/VT_0002204), [VT:0002278](http://purl.obolibrary.org/obo/VT_0002278), ... |
| `MGI:MP`        |             20 | [VT:0000023](http://purl.obolibrary.org/obo/VT_0000023), [VT:0000895](http://purl.obolibrary.org/obo/VT_0000895), [VT:0000896](http://purl.obolibrary.org/obo/VT_0000896), [VT:0000968](http://purl.obolibrary.org/obo/VT_0000968), [VT:0000974](http://purl.obolibrary.org/obo/VT_0000974), ... |
| `MGI:csmith`    |             12 | [VT:0000940](http://purl.obolibrary.org/obo/VT_0000940), [VT:0000977](http://purl.obolibrary.org/obo/VT_0000977), [VT:0001332](http://purl.obolibrary.org/obo/VT_0001332), [VT:0001747](http://purl.obolibrary.org/obo/VT_0001747), [VT:0001884](http://purl.obolibrary.org/obo/VT_0001884), ... |
| `MGI:mb`        |             10 | [VT:0010471](http://purl.obolibrary.org/obo/VT_0010471), [VT:0010472](http://purl.obolibrary.org/obo/VT_0010472), [VT:0010474](http://purl.obolibrary.org/obo/VT_0010474), [VT:0010512](http://purl.obolibrary.org/obo/VT_0010512), [VT:0010689](http://purl.obolibrary.org/obo/VT_0010689), ... |
| `MGI:anna`      |              2 | [VT:0004291](http://purl.obolibrary.org/obo/VT_0004291), [VT:0006028](http://purl.obolibrary.org/obo/VT_0006028)                                                                                                                                                                                 |
| `MGI:brs`       |              1 | [VT:0003847](http://purl.obolibrary.org/obo/VT_0003847)                                                                                                                                                                                                                                          |
| `MGI:hdene`     |              1 | [VT:0010158](http://purl.obolibrary.org/obo/VT_0010158)                                                                                                                                                                                                                                          |
| `MGI:pvb`       |              1 | [VT:0010162](http://purl.obolibrary.org/obo/VT_0010162)                                                                                                                                                                                                                                          |

## `MP`: Mammalian Phenotype Ontology

Overall, there were 4 invalid
xrefs to external prefixed with `MP` (standardized to Bioregistry
prefix [`mp`](https://bioregistry.io/mp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref           |   usages_count | usages                                                  |
|-------------------------|----------------|---------------------------------------------------------|
| `MP:001324`             |              1 | [VT:0001324](http://purl.obolibrary.org/obo/VT_0001324) |
| `MP:00004293`           |              1 | [VT:0004293](http://purl.obolibrary.org/obo/VT_0004293) |
| `MP:MammalianPhenotype` |              1 | [VT:0010442](http://purl.obolibrary.org/obo/VT_0010442) |
| `MP:00003257`           |              1 | [VT:0010453](http://purl.obolibrary.org/obo/VT_0010453) |

## `MS`: Mass spectrometry ontology

Overall, there were 4 invalid
xrefs to external prefixed with `MS` (standardized to Bioregistry
prefix [`ms`](https://bioregistry.io/ms)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                             |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MS:RGD`        |              4 | [VT:0000466](http://purl.obolibrary.org/obo/VT_0000466), [VT:0010213](http://purl.obolibrary.org/obo/VT_0010213), [VT:0010239](http://purl.obolibrary.org/obo/VT_0010239), [VT:1000711](http://purl.obolibrary.org/obo/VT_1000711) |

## `PMID`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref        |   usages_count | usages                                                  |
|----------------------|----------------|---------------------------------------------------------|
| `PMID:0-87893-258-5` |              1 | [VT:0003359](http://purl.obolibrary.org/obo/VT_0003359) |

## `RGD`: Rat Genome Database

Overall, there were 336 invalid
xrefs to external prefixed with `RGD` (standardized to Bioregistry
prefix [`rgd`](https://bioregistry.io/rgd)) that
did not match the standard pattern `^\d{4,}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RGD:cur`       |            201 | [VT:0000032](http://purl.obolibrary.org/obo/VT_0000032), [VT:0002871](http://purl.obolibrary.org/obo/VT_0002871), [VT:0002928](http://purl.obolibrary.org/obo/VT_0002928), [VT:0002929](http://purl.obolibrary.org/obo/VT_0002929), [VT:0002932](http://purl.obolibrary.org/obo/VT_0002932), ... |
| `RGD:MS`        |             62 | [VT:0000073](http://purl.obolibrary.org/obo/VT_0000073), [VT:0000222](http://purl.obolibrary.org/obo/VT_0000222), [VT:0000524](http://purl.obolibrary.org/obo/VT_0000524), [VT:0000535](http://purl.obolibrary.org/obo/VT_0000535), [VT:0000544](http://purl.obolibrary.org/obo/VT_0000544), ... |
| `RGD:dhm`       |             55 | [VT:0000050](http://purl.obolibrary.org/obo/VT_0000050), [VT:0000066](http://purl.obolibrary.org/obo/VT_0000066), [VT:0000153](http://purl.obolibrary.org/obo/VT_0000153), [VT:0000154](http://purl.obolibrary.org/obo/VT_0000154), [VT:0000170](http://purl.obolibrary.org/obo/VT_0000170), ... |
| `RGD:ms`        |             18 | [VT:0002128](http://purl.obolibrary.org/obo/VT_0002128), [VT:0002295](http://purl.obolibrary.org/obo/VT_0002295), [VT:0002504](http://purl.obolibrary.org/obo/VT_0002504), [VT:0002726](http://purl.obolibrary.org/obo/VT_0002726), [VT:0002792](http://purl.obolibrary.org/obo/VT_0002792), ... |

## `RGD `: Rat Genome Database

Overall, there were 1 invalid
xrefs to external prefixed with `RGD ` (standardized to Bioregistry
prefix [`rgd`](https://bioregistry.io/rgd)) that
did not match the standard pattern `^\d{4,}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `RGD :MS`       |              1 | [VT:0010265](http://purl.obolibrary.org/obo/VT_0010265) |

## `VTO`: Vertebrate Taxonomy Ontology

Overall, there were 453 invalid
xrefs to external prefixed with `VTO` (standardized to Bioregistry
prefix [`vto`](https://bioregistry.io/vto)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `VTO:INRA`      |            229 | [VT:0001131](http://purl.obolibrary.org/obo/VT_0001131), [VT:0010001](http://purl.obolibrary.org/obo/VT_0010001), [VT:0010004](http://purl.obolibrary.org/obo/VT_0010004), [VT:0010018](http://purl.obolibrary.org/obo/VT_0010018), [VT:0010029](http://purl.obolibrary.org/obo/VT_0010029), ... |
| `VTO:CP`        |            224 | [VT:0000001](http://purl.obolibrary.org/obo/VT_0000001), [VT:0000009](http://purl.obolibrary.org/obo/VT_0000009), [VT:0000072](http://purl.obolibrary.org/obo/VT_0000072), [VT:0000116](http://purl.obolibrary.org/obo/VT_0000116), [VT:0000444](http://purl.obolibrary.org/obo/VT_0000444), ... |

