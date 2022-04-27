# xao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `xao`. See the [GitHub repository](https://github.com/xenopus-anatomy/xao)


## `NCIt`: NCI Thesaurus

Overall, there were 15 invalid
xrefs to external prefixed with `NCIt` (standardized to Bioregistry
entry [`ncit`]((https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                  |   usages_count | usages                                            |
|--------------------------------|----------------|---------------------------------------------------|
| `NCIt:Peripheral_Nerve`        |              1 | [XAO:0000204](https://bioregistry.io/XAO:0000204) |
| `NCIt:Dorsal`                  |              1 | [XAO:0000298](https://bioregistry.io/XAO:0000298) |
| `NCIt:Ventral`                 |              1 | [XAO:0000299](https://bioregistry.io/XAO:0000299) |
| `NCIt:Deep`                    |              1 | [XAO:0000301](https://bioregistry.io/XAO:0000301) |
| `NCIt:Lateral`                 |              1 | [XAO:0000304](https://bioregistry.io/XAO:0000304) |
| `NCIt:Anterior`                |              1 | [XAO:0003056](https://bioregistry.io/XAO:0003056) |
| `NCIt:Posterior`               |              1 | [XAO:0003057](https://bioregistry.io/XAO:0003057) |
| `NCIt:Spermatid`               |              1 | [XAO:0003151](https://bioregistry.io/XAO:0003151) |
| `NCIt:Medial`                  |              1 | [XAO:0003187](https://bioregistry.io/XAO:0003187) |
| `NCIt:Proximal`                |              1 | [XAO:0003188](https://bioregistry.io/XAO:0003188) |
| `NCIt:Distal`                  |              1 | [XAO:0003189](https://bioregistry.io/XAO:0003189) |
| `NCIt:Inner_Limiting_Membrane` |              1 | [XAO:0003222](https://bioregistry.io/XAO:0003222) |
| `NCIt:Outer_Limiting_Membrane` |              1 | [XAO:0003224](https://bioregistry.io/XAO:0003224) |
| `NCIt:Left`                    |              1 | [XAO:0005005](https://bioregistry.io/XAO:0005005) |
| `NCIt:Right`                   |              1 | [XAO:0005006](https://bioregistry.io/XAO:0005006) |

## `XAO`: Xenopus Anatomy Ontology

Overall, there were 659 invalid
xrefs to external prefixed with `XAO` (standardized to Bioregistry
entry [`xao`]((https://bioregistry.io/xao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `XAO:EJS`       |            352 | [XAO:0004261](https://bioregistry.io/XAO:0004261), [XAO:0004342](https://bioregistry.io/XAO:0004342), [XAO:0004441](https://bioregistry.io/XAO:0004441), [XAO:0004443](https://bioregistry.io/XAO:0004443), [XAO:0005180](https://bioregistry.io/XAO:0005180), ... |
| `XAO:curators`  |            211 | [XAO:0000205](https://bioregistry.io/XAO:0000205), [XAO:0003183](https://bioregistry.io/XAO:0003183), [XAO:0003267](https://bioregistry.io/XAO:0003267), [XAO:0004375](https://bioregistry.io/XAO:0004375), [XAO:0004516](https://bioregistry.io/XAO:0004516), ... |
| `XAO:CJZ`       |             56 | [XAO:0004499](https://bioregistry.io/XAO:0004499), [XAO:0004513](https://bioregistry.io/XAO:0004513), [XAO:0004524](https://bioregistry.io/XAO:0004524), [XAO:0005242](https://bioregistry.io/XAO:0005242), [XAO:0005242](https://bioregistry.io/XAO:0005242), ... |
| `XAO:KAB`       |             19 | [XAO:0004389](https://bioregistry.io/XAO:0004389), [XAO:0004539](https://bioregistry.io/XAO:0004539), [XAO:0004540](https://bioregistry.io/XAO:0004540), [XAO:0004546](https://bioregistry.io/XAO:0004546), [XAO:0005008](https://bioregistry.io/XAO:0005008), ... |
| `XAO:MEF`       |             16 | [XAO:0005298](https://bioregistry.io/XAO:0005298), [XAO:0005302](https://bioregistry.io/XAO:0005302), [XAO:0005303](https://bioregistry.io/XAO:0005303), [XAO:0005303](https://bioregistry.io/XAO:0005303), [XAO:0005303](https://bioregistry.io/XAO:0005303), ... |
| `XAO:curator`   |              5 | [XAO:0000202](https://bioregistry.io/XAO:0000202), [XAO:0000280](https://bioregistry.io/XAO:0000280), [XAO:0003228](https://bioregistry.io/XAO:0003228), [XAO:0004088](https://bioregistry.io/XAO:0004088), [XAO:0004113](https://bioregistry.io/XAO:0004113)      |

