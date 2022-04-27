# xao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `xao`. See the [GitHub repository](https://github.com/xenopus-anatomy/xao).


## `NCIt`: NCI Thesaurus

Overall, there were 15 invalid
xrefs to external prefixed with `NCIt` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                              |   usages_count | usages                                            |
|--------------------------------------------|----------------|---------------------------------------------------|
| `NCIt:('NCIt', 'Peripheral_Nerve')`        |              1 | [XAO:0000204](https://bioregistry.io/XAO:0000204) |
| `NCIt:('NCIt', 'Dorsal')`                  |              1 | [XAO:0000298](https://bioregistry.io/XAO:0000298) |
| `NCIt:('NCIt', 'Ventral')`                 |              1 | [XAO:0000299](https://bioregistry.io/XAO:0000299) |
| `NCIt:('NCIt', 'Deep')`                    |              1 | [XAO:0000301](https://bioregistry.io/XAO:0000301) |
| `NCIt:('NCIt', 'Lateral')`                 |              1 | [XAO:0000304](https://bioregistry.io/XAO:0000304) |
| `NCIt:('NCIt', 'Anterior')`                |              1 | [XAO:0003056](https://bioregistry.io/XAO:0003056) |
| `NCIt:('NCIt', 'Posterior')`               |              1 | [XAO:0003057](https://bioregistry.io/XAO:0003057) |
| `NCIt:('NCIt', 'Spermatid')`               |              1 | [XAO:0003151](https://bioregistry.io/XAO:0003151) |
| `NCIt:('NCIt', 'Medial')`                  |              1 | [XAO:0003187](https://bioregistry.io/XAO:0003187) |
| `NCIt:('NCIt', 'Proximal')`                |              1 | [XAO:0003188](https://bioregistry.io/XAO:0003188) |
| `NCIt:('NCIt', 'Distal')`                  |              1 | [XAO:0003189](https://bioregistry.io/XAO:0003189) |
| `NCIt:('NCIt', 'Inner_Limiting_Membrane')` |              1 | [XAO:0003222](https://bioregistry.io/XAO:0003222) |
| `NCIt:('NCIt', 'Outer_Limiting_Membrane')` |              1 | [XAO:0003224](https://bioregistry.io/XAO:0003224) |
| `NCIt:('NCIt', 'Left')`                    |              1 | [XAO:0005005](https://bioregistry.io/XAO:0005005) |
| `NCIt:('NCIt', 'Right')`                   |              1 | [XAO:0005006](https://bioregistry.io/XAO:0005006) |

## `XAO`: Xenopus Anatomy Ontology

Overall, there were 659 invalid
xrefs to external prefixed with `XAO` (standardized to Bioregistry
prefix [`xao`](https://bioregistry.io/xao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref             |   usages_count | usages                                                                                                                                                                                                                                                             |
|---------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `XAO:('XAO', 'EJS')`      |            352 | [XAO:0000000](https://bioregistry.io/XAO:0000000), [XAO:0000027](https://bioregistry.io/XAO:0000027), [XAO:0000054](https://bioregistry.io/XAO:0000054), [XAO:0000069](https://bioregistry.io/XAO:0000069), [XAO:0000070](https://bioregistry.io/XAO:0000070), ... |
| `XAO:('XAO', 'curators')` |            211 | [XAO:0000013](https://bioregistry.io/XAO:0000013), [XAO:0000029](https://bioregistry.io/XAO:0000029), [XAO:0000030](https://bioregistry.io/XAO:0000030), [XAO:0000032](https://bioregistry.io/XAO:0000032), [XAO:0000034](https://bioregistry.io/XAO:0000034), ... |
| `XAO:('XAO', 'CJZ')`      |             56 | [XAO:0000026](https://bioregistry.io/XAO:0000026), [XAO:0000048](https://bioregistry.io/XAO:0000048), [XAO:0000062](https://bioregistry.io/XAO:0000062), [XAO:0000063](https://bioregistry.io/XAO:0000063), [XAO:0000085](https://bioregistry.io/XAO:0000085), ... |
| `XAO:('XAO', 'KAB')`      |             19 | [XAO:0004389](https://bioregistry.io/XAO:0004389), [XAO:0004525](https://bioregistry.io/XAO:0004525), [XAO:0004526](https://bioregistry.io/XAO:0004526), [XAO:0004527](https://bioregistry.io/XAO:0004527), [XAO:0004533](https://bioregistry.io/XAO:0004533), ... |
| `XAO:('XAO', 'MEF')`      |             16 | [XAO:0005225](https://bioregistry.io/XAO:0005225), [XAO:0005282](https://bioregistry.io/XAO:0005282), [XAO:0005297](https://bioregistry.io/XAO:0005297), [XAO:0005298](https://bioregistry.io/XAO:0005298), [XAO:0005299](https://bioregistry.io/XAO:0005299), ... |
| `XAO:('XAO', 'curator')`  |              5 | [XAO:0000202](https://bioregistry.io/XAO:0000202), [XAO:0000280](https://bioregistry.io/XAO:0000280), [XAO:0003228](https://bioregistry.io/XAO:0003228), [XAO:0004088](https://bioregistry.io/XAO:0004088), [XAO:0004113](https://bioregistry.io/XAO:0004113)      |

