# xao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `xao`. See the [GitHub repository](https://github.com/xenopus-anatomy/xao).


## `CARO`: Common Anatomy Reference Ontology

Overall, there were 4 invalid
xrefs to external prefixed with `CARO` (standardized to Bioregistry
prefix [`caro`](https://bioregistry.io/caro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                     |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CARO:MAH`      |              4 | [XAO:0004007](http://purl.obolibrary.org/obo/XAO_0004007), [XAO:0004008](http://purl.obolibrary.org/obo/XAO_0004008), [XAO:0004009](http://purl.obolibrary.org/obo/XAO_0004009), [XAO:0004010](http://purl.obolibrary.org/obo/XAO_0004010) |

## `NCIt`: NCI Thesaurus

Overall, there were 16 invalid
xrefs to external prefixed with `NCIt` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^[CRPA]\d+$`.

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
| `NCIt:Abdominal_Wall`          |              1 | [XAO:0005504](http://purl.obolibrary.org/obo/XAO_0005504) |

## `VSAO`: Vertebrate Skeletal Anatomy Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `VSAO` (standardized to Bioregistry
prefix [`vsao`](https://bioregistry.io/vsao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `VSAO:00000082` |              1 | [XAO:0004023](http://purl.obolibrary.org/obo/XAO_0004023) |

## `XAO`: Xenopus Anatomy Ontology

Overall, there were 5 invalid
xrefs to external prefixed with `XAO` (standardized to Bioregistry
prefix [`xao`](https://bioregistry.io/xao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                |
|-----------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `XAO:curator`   |              5 | [XAO:0000202](http://purl.obolibrary.org/obo/XAO_0000202), [XAO:0000280](http://purl.obolibrary.org/obo/XAO_0000280), [XAO:0003228](http://purl.obolibrary.org/obo/XAO_0003228), [XAO:0004088](http://purl.obolibrary.org/obo/XAO_0004088), [XAO:0004113](http://purl.obolibrary.org/obo/XAO_0004113) |

## `Xenbase`: Xenbase

Overall, there were 240 invalid
xrefs to external prefixed with `Xenbase` (standardized to Bioregistry
prefix [`xenbase`](https://bioregistry.io/xenbase)) that
did not match the standard pattern `^XB\-\w+\-\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Xenbase:Staff` |            221 | [XAO:0000013](http://purl.obolibrary.org/obo/XAO_0000013), [XAO:0000029](http://purl.obolibrary.org/obo/XAO_0000029), [XAO:0000030](http://purl.obolibrary.org/obo/XAO_0000030), [XAO:0000032](http://purl.obolibrary.org/obo/XAO_0000032), [XAO:0000034](http://purl.obolibrary.org/obo/XAO_0000034), ... |
| `Xenbase:KAB`   |             19 | [XAO:0004389](http://purl.obolibrary.org/obo/XAO_0004389), [XAO:0004525](http://purl.obolibrary.org/obo/XAO_0004525), [XAO:0004526](http://purl.obolibrary.org/obo/XAO_0004526), [XAO:0004527](http://purl.obolibrary.org/obo/XAO_0004527), [XAO:0004533](http://purl.obolibrary.org/obo/XAO_0004533), ... |

