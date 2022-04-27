# eco

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `eco`. See the [GitHub repository](https://github.com/evidenceontology/evidenceontology).


## `DisProt`: DisProt

Overall, there were 7 invalid
xrefs to external prefixed with `DisProt` (standardized to Bioregistry
entry [`disprot`](https://bioregistry.io/disprot)) that
did not match the standard pattern `^DP\d{5}$`.

| external_xref            |   usages_count | usages                                                                                                                                                                                                                                                             |
|--------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DisProt:BalintMeszaros` |              7 | [ECO:0006183](https://bioregistry.io/ECO:0006183), [ECO:0006185](https://bioregistry.io/ECO:0006185), [ECO:0006187](https://bioregistry.io/ECO:0006187), [ECO:0006188](https://bioregistry.io/ECO:0006188), [ECO:0006189](https://bioregistry.io/ECO:0006189), ... |

## `ECO`: Evidence ontology

Overall, there were 1,411 invalid
xrefs to external prefixed with `ECO` (standardized to Bioregistry
entry [`eco`](https://bioregistry.io/eco)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ECO:RCT`       |            718 | [ECO:0000009](https://bioregistry.io/ECO:0000009), [ECO:0000011](https://bioregistry.io/ECO:0000011), [ECO:0000033](https://bioregistry.io/ECO:0000033), [ECO:0000053](https://bioregistry.io/ECO:0000053), [ECO:0000054](https://bioregistry.io/ECO:0000054), ... |
| `ECO:SN`        |            328 | [ECO:0000001](https://bioregistry.io/ECO:0000001), [ECO:0000002](https://bioregistry.io/ECO:0000002), [ECO:0000018](https://bioregistry.io/ECO:0000018), [ECO:0000021](https://bioregistry.io/ECO:0000021), [ECO:0000028](https://bioregistry.io/ECO:0000028), ... |
| `ECO:MCC`       |            297 | [ECO:0000000](https://bioregistry.io/ECO:0000000), [ECO:0000007](https://bioregistry.io/ECO:0000007), [ECO:0000008](https://bioregistry.io/ECO:0000008), [ECO:0000019](https://bioregistry.io/ECO:0000019), [ECO:0000020](https://bioregistry.io/ECO:0000020), ... |
| `ECO:SW`        |             58 | [ECO:0000085](https://bioregistry.io/ECO:0000085), [ECO:0000095](https://bioregistry.io/ECO:0000095), [ECO:0000096](https://bioregistry.io/ECO:0000096), [ECO:0000106](https://bioregistry.io/ECO:0000106), [ECO:0000109](https://bioregistry.io/ECO:0000109), ... |
| `ECO:KAV`       |              3 | [ECO:0000003](https://bioregistry.io/ECO:0000003), [ECO:0000154](https://bioregistry.io/ECO:0000154), [ECO:0000164](https://bioregistry.io/ECO:0000164)                                                                                                            |
| `ECO:KIM`       |              2 | [ECO:0000004](https://bioregistry.io/ECO:0000004), [ECO:0000096](https://bioregistry.io/ECO:0000096)                                                                                                                                                               |
| `ECO:RCJ`       |              2 | [ECO:0001828](https://bioregistry.io/ECO:0001828), [ECO:0007850](https://bioregistry.io/ECO:0007850)                                                                                                                                                               |
| `ECO:MG`        |              2 | [ECO:0006186](https://bioregistry.io/ECO:0006186), [ECO:0006252](https://bioregistry.io/ECO:0006252)                                                                                                                                                               |
| `ECO:cjm`       |              1 | [ECO:0000501](https://bioregistry.io/ECO:0000501)                                                                                                                                                                                                                  |

## `EDAM`: Bioinformatics operations, data types, formats, identifiers and topics

Overall, there were 1 invalid
xrefs to external prefixed with `EDAM` (standardized to Bioregistry
entry [`edam`](https://bioregistry.io/edam)) that
did not match the standard pattern `^(data|topic|operation|format)\_\d{4}$`.

| external_xref     |   usages_count | usages                                            |
|-------------------|----------------|---------------------------------------------------|
| `EDAM:topic:3298` |              1 | [ECO:0007075](https://bioregistry.io/ECO:0007075) |

## `GO`: Gene Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
entry [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                  |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:IEP`        |              3 | [ECO:0000008](https://bioregistry.io/ECO:0000008), [ECO:0007006](https://bioregistry.io/ECO:0007006), [ECO:0007007](https://bioregistry.io/ECO:0007007) |
| `GO:IMP`        |              3 | [ECO:0000015](https://bioregistry.io/ECO:0000015), [ECO:0007000](https://bioregistry.io/ECO:0007000), [ECO:0007001](https://bioregistry.io/ECO:0007001) |
| `GO:TAS`        |              1 | [ECO:0000033](https://bioregistry.io/ECO:0000033)                                                                                                       |

## `HPO`: Human Phenotype Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `HPO` (standardized to Bioregistry
entry [`hp`](https://bioregistry.io/hp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                            |
|-----------------|----------------|---------------------------------------------------|
| `HPO:PCS`       |              1 | [ECO:0006017](https://bioregistry.io/ECO:0006017) |
| `HPO:ICE`       |              1 | [ECO:0006019](https://bioregistry.io/ECO:0006019) |

## `PMC`: Pubmed Central

Overall, there were 22 invalid
xrefs to external prefixed with `PMC` (standardized to Bioregistry
entry [`pmc`](https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref   |   usages_count | usages                                                                                               |
|-----------------|----------------|------------------------------------------------------------------------------------------------------|
| `PMC:102612`    |              2 | [ECO:0000138](https://bioregistry.io/ECO:0000138), [ECO:0006084](https://bioregistry.io/ECO:0006084) |
| `PMC:4029002`   |              1 | [ECO:0000010](https://bioregistry.io/ECO:0000010)                                                    |
| `PMC:2686546`   |              1 | [ECO:0000029](https://bioregistry.io/ECO:0000029)                                                    |
| `PMC:38513`     |              1 | [ECO:0000077](https://bioregistry.io/ECO:0000077)                                                    |
| `PMC:2881125`   |              1 | [ECO:0000359](https://bioregistry.io/ECO:0000359)                                                    |
| `PMC:3929704`   |              1 | [ECO:0001004](https://bioregistry.io/ECO:0001004)                                                    |
| `PMC:3478843`   |              1 | [ECO:0001008](https://bioregistry.io/ECO:0001008)                                                    |
| `PMC:3169266`   |              1 | [ECO:0001011](https://bioregistry.io/ECO:0001011)                                                    |
| `PMC:3185625`   |              1 | [ECO:0001022](https://bioregistry.io/ECO:0001022)                                                    |
| `PMC:3074624`   |              1 | [ECO:0001026](https://bioregistry.io/ECO:0001026)                                                    |
| `PMC:3572410`   |              1 | [ECO:0001030](https://bioregistry.io/ECO:0001030)                                                    |
| `PMC:4401164`   |              1 | [ECO:0001039](https://bioregistry.io/ECO:0001039)                                                    |
| `PMC:2217636`   |              1 | [ECO:0001042](https://bioregistry.io/ECO:0001042)                                                    |
| `PMC:346675`    |              1 | [ECO:0001047](https://bioregistry.io/ECO:0001047)                                                    |
| `PMC:2782548`   |              1 | [ECO:0001091](https://bioregistry.io/ECO:0001091)                                                    |
| `PMC:1534009`   |              1 | [ECO:0001102](https://bioregistry.io/ECO:0001102)                                                    |
| `PMC:3149870`   |              1 | [ECO:0001107](https://bioregistry.io/ECO:0001107)                                                    |
| `PMC:1828913`   |              1 | [ECO:0001117](https://bioregistry.io/ECO:0001117)                                                    |
| `PMC:1808921`   |              1 | [ECO:0001129](https://bioregistry.io/ECO:0001129)                                                    |
| `PMC:3908118`   |              1 | [ECO:0005008](https://bioregistry.io/ECO:0005008)                                                    |
| `PMC:3667641`   |              1 | [ECO:0005021](https://bioregistry.io/ECO:0005021)                                                    |

## `PMCID`: Pubmed Central

Overall, there were 1 invalid
xrefs to external prefixed with `PMCID` (standardized to Bioregistry
entry [`pmc`](https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref   |   usages_count | usages                                            |
|-----------------|----------------|---------------------------------------------------|
| `PMCID:3277431` |              1 | [ECO:0001811](https://bioregistry.io/ECO:0001811) |

## `PMID`: PubMed

Overall, there were 2 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
entry [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref    |   usages_count | usages                                            |
|------------------|----------------|---------------------------------------------------|
| `PMID: 16428685` |              1 | [ECO:0006163](https://bioregistry.io/ECO:0006163) |
| `PMID: 23036848` |              1 | [ECO:0006163](https://bioregistry.io/ECO:0006163) |

## `PomBase`: PomBase

Overall, there were 1 invalid
xrefs to external prefixed with `PomBase` (standardized to Bioregistry
entry [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref   |   usages_count | usages                                            |
|-----------------|----------------|---------------------------------------------------|
| `PomBase:MAH`   |              1 | [ECO:0000095](https://bioregistry.io/ECO:0000095) |

## `PSI-MI`: Molecular Interactions Controlled Vocabulary

Overall, there were 3 invalid
xrefs to external prefixed with `PSI-MI` (standardized to Bioregistry
entry [`mi`](https://bioregistry.io/mi)) that
did not match the standard pattern `^\d{4}$`.

| external_xref    |   usages_count | usages                                            |
|------------------|----------------|---------------------------------------------------|
| `PSI-MI:MI:0400` |              1 | [ECO:0000023](https://bioregistry.io/ECO:0000023) |
| `PSI-MI:MI:0090` |              1 | [ECO:0000025](https://bioregistry.io/ECO:0000025) |
| `PSI-MI:MI:0432` |              1 | [ECO:0000066](https://bioregistry.io/ECO:0000066) |

