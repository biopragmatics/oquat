# xao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `xao`. See the [GitHub repository](https://github.com/xenopus-anatomy/xao).


## `NCIt`: NCI Thesaurus

Overall, there were 15 invalid
xrefs to external prefixed with `NCIt` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                  |   usages_count | usages                                                    |
|--------------------------------|----------------|-----------------------------------------------------------|
| `NCIt:Peripheral_Nerve`        |              1 | [XAO:0000204](http://purl.obolibrary.org/obo/XAO_0000204) |
| `NCIt:Dorsal`                  |              1 | [XAO:0000298](http://purl.obolibrary.org/obo/XAO_0000298) |
| `NCIt:Ventral`                 |              1 | [XAO:0000299](http://purl.obolibrary.org/obo/XAO_0000299) |
| `NCIt:Deep`                    |              1 | [XAO:0000301](http://purl.obolibrary.org/obo/XAO_0000301) |
| `NCIt:Lateral`                 |              1 | [XAO:0000304](http://purl.obolibrary.org/obo/XAO_0000304) |
| `NCIt:Anterior`                |              1 | [XAO:0003056](http://purl.obolibrary.org/obo/XAO_0003056) |
| `NCIt:Posterior`               |              1 | [XAO:0003057](http://purl.obolibrary.org/obo/XAO_0003057) |
| `NCIt:Spermatid`               |              1 | [XAO:0003151](http://purl.obolibrary.org/obo/XAO_0003151) |
| `NCIt:Medial`                  |              1 | [XAO:0003187](http://purl.obolibrary.org/obo/XAO_0003187) |
| `NCIt:Proximal`                |              1 | [XAO:0003188](http://purl.obolibrary.org/obo/XAO_0003188) |
| `NCIt:Distal`                  |              1 | [XAO:0003189](http://purl.obolibrary.org/obo/XAO_0003189) |
| `NCIt:Inner_Limiting_Membrane` |              1 | [XAO:0003222](http://purl.obolibrary.org/obo/XAO_0003222) |
| `NCIt:Outer_Limiting_Membrane` |              1 | [XAO:0003224](http://purl.obolibrary.org/obo/XAO_0003224) |
| `NCIt:Left`                    |              1 | [XAO:0005005](http://purl.obolibrary.org/obo/XAO_0005005) |
| `NCIt:Right`                   |              1 | [XAO:0005006](http://purl.obolibrary.org/obo/XAO_0005006) |

## `XAO`: Xenopus Anatomy Ontology

Overall, there were 659 invalid
xrefs to external prefixed with `XAO` (standardized to Bioregistry
prefix [`xao`](https://bioregistry.io/xao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `XAO:EJS`       |            352 | [XAO:0000000](http://purl.obolibrary.org/obo/XAO_0000000), [XAO:0000027](http://purl.obolibrary.org/obo/XAO_0000027), [XAO:0000054](http://purl.obolibrary.org/obo/XAO_0000054), [XAO:0000069](http://purl.obolibrary.org/obo/XAO_0000069), [XAO:0000070](http://purl.obolibrary.org/obo/XAO_0000070), ... |
| `XAO:curators`  |            211 | [XAO:0000013](http://purl.obolibrary.org/obo/XAO_0000013), [XAO:0000029](http://purl.obolibrary.org/obo/XAO_0000029), [XAO:0000030](http://purl.obolibrary.org/obo/XAO_0000030), [XAO:0000032](http://purl.obolibrary.org/obo/XAO_0000032), [XAO:0000034](http://purl.obolibrary.org/obo/XAO_0000034), ... |
| `XAO:CJZ`       |             56 | [XAO:0000026](http://purl.obolibrary.org/obo/XAO_0000026), [XAO:0000048](http://purl.obolibrary.org/obo/XAO_0000048), [XAO:0000062](http://purl.obolibrary.org/obo/XAO_0000062), [XAO:0000063](http://purl.obolibrary.org/obo/XAO_0000063), [XAO:0000085](http://purl.obolibrary.org/obo/XAO_0000085), ... |
| `XAO:KAB`       |             19 | [XAO:0004389](http://purl.obolibrary.org/obo/XAO_0004389), [XAO:0004525](http://purl.obolibrary.org/obo/XAO_0004525), [XAO:0004526](http://purl.obolibrary.org/obo/XAO_0004526), [XAO:0004527](http://purl.obolibrary.org/obo/XAO_0004527), [XAO:0004533](http://purl.obolibrary.org/obo/XAO_0004533), ... |
| `XAO:MEF`       |             16 | [XAO:0005225](http://purl.obolibrary.org/obo/XAO_0005225), [XAO:0005282](http://purl.obolibrary.org/obo/XAO_0005282), [XAO:0005297](http://purl.obolibrary.org/obo/XAO_0005297), [XAO:0005298](http://purl.obolibrary.org/obo/XAO_0005298), [XAO:0005299](http://purl.obolibrary.org/obo/XAO_0005299), ... |
| `XAO:curator`   |              5 | [XAO:0000202](http://purl.obolibrary.org/obo/XAO_0000202), [XAO:0000280](http://purl.obolibrary.org/obo/XAO_0000280), [XAO:0003228](http://purl.obolibrary.org/obo/XAO_0003228), [XAO:0004088](http://purl.obolibrary.org/obo/XAO_0004088), [XAO:0004113](http://purl.obolibrary.org/obo/XAO_0004113)      |

