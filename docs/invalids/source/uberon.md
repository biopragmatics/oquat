# uberon

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `uberon`. See the [GitHub repository](https://github.com/obophenotype/uberon).


## `AAO`: Amphibian gross anatomy

Overall, there were 535 invalid
xrefs to external prefixed with `AAO` (standardized to Bioregistry
prefix [`aao`](https://bioregistry.io/aao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                 |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AAO:LAP`                     |            251 | [UBERON:0001080](http://purl.obolibrary.org/obo/UBERON_0001080), [UBERON:0002375](http://purl.obolibrary.org/obo/UBERON_0002375), [UBERON:0012129](http://purl.obolibrary.org/obo/UBERON_0012129), [UBERON:0014898](http://purl.obolibrary.org/obo/UBERON_0014898), [UBERON:0034900](http://purl.obolibrary.org/obo/UBERON_0034900), ... |
| `AAO:EJS`                     |            116 | [UBERON:0013732](http://purl.obolibrary.org/obo/UBERON_0013732), [UBERON:3000237](http://purl.obolibrary.org/obo/UBERON_3000237), [UBERON:3000265](http://purl.obolibrary.org/obo/UBERON_3000265), [UBERON:3000288](http://purl.obolibrary.org/obo/UBERON_3000288), [UBERON:3000323](http://purl.obolibrary.org/obo/UBERON_3000323), ... |
| `AAO:BJB`                     |             59 | [UBERON:3000041](http://purl.obolibrary.org/obo/UBERON_3000041), [UBERON:3000044](http://purl.obolibrary.org/obo/UBERON_3000044), [UBERON:3010029](http://purl.obolibrary.org/obo/UBERON_3010029), [UBERON:3010039](http://purl.obolibrary.org/obo/UBERON_3010039), [UBERON:3010042](http://purl.obolibrary.org/obo/UBERON_3010042), ... |
| `AAO:BMZ`                     |             30 | [UBERON:3010586](http://purl.obolibrary.org/obo/UBERON_3010586), [UBERON:3010589](http://purl.obolibrary.org/obo/UBERON_3010589), [UBERON:3010590](http://purl.obolibrary.org/obo/UBERON_3010590), [UBERON:3010613](http://purl.obolibrary.org/obo/UBERON_3010613), [UBERON:3010614](http://purl.obolibrary.org/obo/UBERON_3010614), ... |
| `AAO:MEJ`                     |             17 | [UBERON:3010673](http://purl.obolibrary.org/obo/UBERON_3010673), [UBERON:3010691](http://purl.obolibrary.org/obo/UBERON_3010691), [UBERON:3010692](http://purl.obolibrary.org/obo/UBERON_3010692), [UBERON:3010694](http://purl.obolibrary.org/obo/UBERON_3010694), [UBERON:3010695](http://purl.obolibrary.org/obo/UBERON_3010695), ... |
| `AAO:Trueb_1973`              |              8 | [UBERON:3000711](http://purl.obolibrary.org/obo/UBERON_3000711), [UBERON:3000712](http://purl.obolibrary.org/obo/UBERON_3000712), [UBERON:3000717](http://purl.obolibrary.org/obo/UBERON_3000717), [UBERON:3000793](http://purl.obolibrary.org/obo/UBERON_3000793), [UBERON:3000794](http://purl.obolibrary.org/obo/UBERON_3000794), ... |
| `AAO:SIQ`                     |              8 | [UBERON:3010105](http://purl.obolibrary.org/obo/UBERON_3010105), [UBERON:3010765](http://purl.obolibrary.org/obo/UBERON_3010765), [UBERON:3010778](http://purl.obolibrary.org/obo/UBERON_3010778), [UBERON:3010796](http://purl.obolibrary.org/obo/UBERON_3010796), [UBERON:3010798](http://purl.obolibrary.org/obo/UBERON_3010798), ... |
| `AAO:Francis_1934`            |              6 | [UBERON:3000694](http://purl.obolibrary.org/obo/UBERON_3000694), [UBERON:3000950](http://purl.obolibrary.org/obo/UBERON_3000950), [UBERON:3000951](http://purl.obolibrary.org/obo/UBERON_3000951), [UBERON:3000952](http://purl.obolibrary.org/obo/UBERON_3000952), [UBERON:3000954](http://purl.obolibrary.org/obo/UBERON_3000954), ... |
| `AAO:Pugener_2002`            |              5 | [UBERON:3000711](http://purl.obolibrary.org/obo/UBERON_3000711), [UBERON:3000712](http://purl.obolibrary.org/obo/UBERON_3000712), [UBERON:3000717](http://purl.obolibrary.org/obo/UBERON_3000717), [UBERON:3000727](http://purl.obolibrary.org/obo/UBERON_3000727), [UBERON:3000735](http://purl.obolibrary.org/obo/UBERON_3000735)      |
| `AAO:Maglia_et_al_2007`       |              4 | [UBERON:0006714](http://purl.obolibrary.org/obo/UBERON_0006714), [UBERON:0006715](http://purl.obolibrary.org/obo/UBERON_0006715), [UBERON:3000746](http://purl.obolibrary.org/obo/UBERON_3000746), [UBERON:3000810](http://purl.obolibrary.org/obo/UBERON_3000810)                                                                       |
| `AAO:CAM`                     |              4 | [UBERON:3010720](http://purl.obolibrary.org/obo/UBERON_3010720), [UBERON:3010722](http://purl.obolibrary.org/obo/UBERON_3010722), [UBERON:3010751](http://purl.obolibrary.org/obo/UBERON_3010751), [UBERON:3010764](http://purl.obolibrary.org/obo/UBERON_3010764)                                                                       |
| `AAO:Pugener_and_Maglia_2008` |              3 | [UBERON:0001079](http://purl.obolibrary.org/obo/UBERON_0001079), [UBERON:0006062](http://purl.obolibrary.org/obo/UBERON_0006062), [UBERON:3000745](http://purl.obolibrary.org/obo/UBERON_3000745)                                                                                                                                        |
| `AAO:Duellman_and_Trueb_1994` |              3 | [UBERON:3000707](http://purl.obolibrary.org/obo/UBERON_3000707), [UBERON:3000728](http://purl.obolibrary.org/obo/UBERON_3000728), [UBERON:3000956](http://purl.obolibrary.org/obo/UBERON_3000956)                                                                                                                                        |
| `AAO:Griffiths_1959`          |              3 | [UBERON:3000718](http://purl.obolibrary.org/obo/UBERON_3000718), [UBERON:3000719](http://purl.obolibrary.org/obo/UBERON_3000719), [UBERON:3000720](http://purl.obolibrary.org/obo/UBERON_3000720)                                                                                                                                        |
| `AAO:DSM`                     |              2 | [UBERON:0009121](http://purl.obolibrary.org/obo/UBERON_0009121), [UBERON:3010632](http://purl.obolibrary.org/obo/UBERON_3010632)                                                                                                                                                                                                         |
| `AAO:LT`                      |              2 | [UBERON:3000074](http://purl.obolibrary.org/obo/UBERON_3000074), [UBERON:3010576](http://purl.obolibrary.org/obo/UBERON_3010576)                                                                                                                                                                                                         |
| `AAO:curator`                 |              2 | [UBERON:3000588](http://purl.obolibrary.org/obo/UBERON_3000588), [UBERON:3010138](http://purl.obolibrary.org/obo/UBERON_3010138)                                                                                                                                                                                                         |
| `AAO:Rocek_2003`              |              2 | [UBERON:3000683](http://purl.obolibrary.org/obo/UBERON_3000683), [UBERON:3000685](http://purl.obolibrary.org/obo/UBERON_3000685)                                                                                                                                                                                                         |
| `AAO:Kluge_and_Farris_1969`   |              2 | [UBERON:3000713](http://purl.obolibrary.org/obo/UBERON_3000713), [UBERON:3000714](http://purl.obolibrary.org/obo/UBERON_3000714)                                                                                                                                                                                                         |
| `AAO:Cannatella_1985`         |              2 | [UBERON:3000808](http://purl.obolibrary.org/obo/UBERON_3000808), [UBERON:3000809](http://purl.obolibrary.org/obo/UBERON_3000809)                                                                                                                                                                                                         |
| `AAO:DBW`                     |              2 | [UBERON:3010583](http://purl.obolibrary.org/obo/UBERON_3010583), [UBERON:3010728](http://purl.obolibrary.org/obo/UBERON_3010728)                                                                                                                                                                                                         |
| `AAO:JMG`                     |              2 | [UBERON:3010818](http://purl.obolibrary.org/obo/UBERON_3010818), [UBERON:3010819](http://purl.obolibrary.org/obo/UBERON_3010819)                                                                                                                                                                                                         |
| `AAO:HM`                      |              1 | [UBERON:3010690](http://purl.obolibrary.org/obo/UBERON_3010690)                                                                                                                                                                                                                                                                          |
| `AAO:AMM`                     |              1 | [UBERON:3010821](http://purl.obolibrary.org/obo/UBERON_3010821)                                                                                                                                                                                                                                                                          |

## `AEO`: Anatomical Entity Ontology

Overall, there were 31 invalid
xrefs to external prefixed with `AEO` (standardized to Bioregistry
prefix [`aeo`](https://bioregistry.io/aeo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AEO:JB`        |             30 | [UBERON:0001637](http://purl.obolibrary.org/obo/UBERON_0001637), [UBERON:0004016](http://purl.obolibrary.org/obo/UBERON_0004016), [UBERON:0005866](http://purl.obolibrary.org/obo/UBERON_0005866), [UBERON:0006846](http://purl.obolibrary.org/obo/UBERON_0006846), [UBERON:0007473](http://purl.obolibrary.org/obo/UBERON_0007473), ... |
| `AEO:000020`    |              1 | [UBERON:0001013](http://purl.obolibrary.org/obo/UBERON_0001013)                                                                                                                                                                                                                                                                          |

## `BIRNLEX`: Biomedical Informatics Research Network Lexicon

Overall, there were 2 invalid
xrefs to external prefixed with `BIRNLEX` (standardized to Bioregistry
prefix [`birnlex`](https://bioregistry.io/birnlex)) that
did not match the standard pattern `^\d+$`.

| external_xref           |   usages_count | usages                                                          |
|-------------------------|----------------|-----------------------------------------------------------------|
| `BIRNLEX:Limbic_system` |              1 | [UBERON:0000349](http://purl.obolibrary.org/obo/UBERON_0000349) |
| `BIRNLEX:4106_2`        |              1 | [UBERON:0000396](http://purl.obolibrary.org/obo/UBERON_0000396) |

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

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CARO:DOS`      |              4 | [UBERON:0000026](http://purl.obolibrary.org/obo/UBERON_0000026), [UBERON:0000475](http://purl.obolibrary.org/obo/UBERON_0000475), [UBERON:0000478](http://purl.obolibrary.org/obo/UBERON_0000478), [UBERON:0022295](http://purl.obolibrary.org/obo/UBERON_0022295) |

## `CL`: Cell Ontology

Overall, there were 19 invalid
xrefs to external prefixed with `CL` (standardized to Bioregistry
prefix [`cl`](https://bioregistry.io/cl)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CL:tm`         |             19 | [UBERON:0001249](http://purl.obolibrary.org/obo/UBERON_0001249), [UBERON:0001249](http://purl.obolibrary.org/obo/UBERON_0001249), [UBERON:0001745](http://purl.obolibrary.org/obo/UBERON_0001745), [UBERON:0004041](http://purl.obolibrary.org/obo/UBERON_0004041), [UBERON:0004042](http://purl.obolibrary.org/obo/UBERON_0004042), ... |

## `DHBA`: Developing Human Brain Atlas

Overall, there were 17 invalid
xrefs to external prefixed with `DHBA` (standardized to Bioregistry
prefix [`dhba`](https://bioregistry.io/dhba)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `DHBA:HNM`      |              1 | [UBERON:0001892](http://purl.obolibrary.org/obo/UBERON_0001892) |
| `DHBA:GiRt`     |              1 | [UBERON:0002155](http://purl.obolibrary.org/obo/UBERON_0002155) |
| `DHBA:ILN`      |              1 | [UBERON:0002733](http://purl.obolibrary.org/obo/UBERON_0002733) |
| `DHBA:10N`      |              1 | [UBERON:0002870](http://purl.obolibrary.org/obo/UBERON_0002870) |
| `DHBA:AILN`     |              1 | [UBERON:0002965](http://purl.obolibrary.org/obo/UBERON_0002965) |
| `DHBA:SZ`       |              1 | [UBERON:0004023](http://purl.obolibrary.org/obo/UBERON_0004023) |
| `DHBA:CbV`      |              1 | [UBERON:0004079](http://purl.obolibrary.org/obo/UBERON_0004079) |
| `DHBA:CbVI`     |              1 | [UBERON:0004080](http://purl.obolibrary.org/obo/UBERON_0004080) |
| `DHBA:CbVIIb`   |              1 | [UBERON:0005346](http://purl.obolibrary.org/obo/UBERON_0005346) |
| `DHBA:CbVIIIb`  |              1 | [UBERON:0005349](http://purl.obolibrary.org/obo/UBERON_0005349) |
| `DHBA:HN`       |              1 | [UBERON:0008993](http://purl.obolibrary.org/obo/UBERON_0008993) |
| `DHBA:HGM`      |              1 | [UBERON:0019263](http://purl.obolibrary.org/obo/UBERON_0019263) |
| `DHBA:PILN`     |              1 | [UBERON:0019295](http://purl.obolibrary.org/obo/UBERON_0019295) |
| `DHBA:SHy`      |              1 | [UBERON:0019308](http://purl.obolibrary.org/obo/UBERON_0019308) |
| `DHBA:FIFT`     |              1 | [UBERON:0022247](http://purl.obolibrary.org/obo/UBERON_0022247) |
| `DHBA:cpn`      |              1 | [UBERON:0022271](http://purl.obolibrary.org/obo/UBERON_0022271) |
| `DHBA:cbu-h`    |              1 | [UBERON:0022272](http://purl.obolibrary.org/obo/UBERON_0022272) |

## `DMBA`: Developing Mouse Brain Atlas

Overall, there were 16 invalid
xrefs to external prefixed with `DMBA` (standardized to Bioregistry
prefix [`dmba`](https://bioregistry.io/dmba)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `DMBA:CbHCx`    |              1 | [UBERON:0002129](http://purl.obolibrary.org/obo/UBERON_0002129) |
| `DMBA:Mam`      |              1 | [UBERON:0002206](http://purl.obolibrary.org/obo/UBERON_0002206) |
| `DMBA:dpy`      |              1 | [UBERON:0002755](http://purl.obolibrary.org/obo/UBERON_0002755) |
| `DMBA:OB`       |              1 | [UBERON:0004186](http://purl.obolibrary.org/obo/UBERON_0004186) |
| `DMBA:DTTh`     |              1 | [UBERON:0004703](http://purl.obolibrary.org/obo/UBERON_0004703) |
| `DMBA:OB-Opl`   |              1 | [UBERON:0005376](http://purl.obolibrary.org/obo/UBERON_0005376) |
| `DMBA:AGlom`    |              1 | [UBERON:0007631](http://purl.obolibrary.org/obo/UBERON_0007631) |
| `DMBA:Bar`      |              1 | [UBERON:0007632](http://purl.obolibrary.org/obo/UBERON_0007632) |
| `DMBA:tracts`   |              1 | [UBERON:0007702](http://purl.obolibrary.org/obo/UBERON_0007702) |
| `DMBA:AGr`      |              1 | [UBERON:0015244](http://purl.obolibrary.org/obo/UBERON_0015244) |
| `DMBA:m2`       |              1 | [UBERON:0019274](http://purl.obolibrary.org/obo/UBERON_0019274) |
| `DMBA:r9`       |              1 | [UBERON:0019284](http://purl.obolibrary.org/obo/UBERON_0019284) |
| `DMBA:r10`      |              1 | [UBERON:0019285](http://purl.obolibrary.org/obo/UBERON_0019285) |
| `DMBA:r11`      |              1 | [UBERON:0019286](http://purl.obolibrary.org/obo/UBERON_0019286) |
| `DMBA:AOPl`     |              1 | [UBERON:0019289](http://purl.obolibrary.org/obo/UBERON_0019289) |
| `DMBA:AIPl`     |              1 | [UBERON:0019290](http://purl.obolibrary.org/obo/UBERON_0019290) |

## `EMAPA`: Mouse Developmental Anatomy Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `EMAPA` (standardized to Bioregistry
prefix [`emapa`](https://bioregistry.io/emapa)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `EMAPA:th`      |              1 | [UBERON:0001638](http://purl.obolibrary.org/obo/UBERON_0001638) |

## `FB`: FlyBase Gene

Overall, there were 8 invalid
xrefs to external prefixed with `FB` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FB:gg`         |              7 | [UBERON:0000018](http://purl.obolibrary.org/obo/UBERON_0000018), [UBERON:0000914](http://purl.obolibrary.org/obo/UBERON_0000914), [UBERON:0000918](http://purl.obolibrary.org/obo/UBERON_0000918), [UBERON:0000972](http://purl.obolibrary.org/obo/UBERON_0000972), [UBERON:0000984](http://purl.obolibrary.org/obo/UBERON_0000984), ... |
| `FB:DJS`        |              1 | [UBERON:0001048](http://purl.obolibrary.org/obo/UBERON_0001048)                                                                                                                                                                                                                                                                          |

## `FlyBase`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `FlyBase` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref              |   usages_count | usages                                                          |
|----------------------------|----------------|-----------------------------------------------------------------|
| `FlyBase:FBim0000836.html` |              1 | [UBERON:6004646](http://purl.obolibrary.org/obo/UBERON_6004646) |

## `FMA`: Foundational Model of Anatomy

Overall, there were 1,055 invalid
xrefs to external prefixed with `FMA` (standardized to Bioregistry
prefix [`fma`](https://bioregistry.io/fma)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FMA:TA`        |           1022 | [UBERON:0000002](http://purl.obolibrary.org/obo/UBERON_0000002), [UBERON:0000010](http://purl.obolibrary.org/obo/UBERON_0000010), [UBERON:0000011](http://purl.obolibrary.org/obo/UBERON_0000011), [UBERON:0000013](http://purl.obolibrary.org/obo/UBERON_0000013), [UBERON:0000019](http://purl.obolibrary.org/obo/UBERON_0000019), ... |
| `FMA:FMA`       |             27 | [UBERON:0000485](http://purl.obolibrary.org/obo/UBERON_0000485), [UBERON:0000486](http://purl.obolibrary.org/obo/UBERON_0000486), [UBERON:0001845](http://purl.obolibrary.org/obo/UBERON_0001845), [UBERON:0001943](http://purl.obolibrary.org/obo/UBERON_0001943), [UBERON:0002137](http://purl.obolibrary.org/obo/UBERON_0002137), ... |
| `FMA:CMA`       |              6 | [UBERON:0002022](http://purl.obolibrary.org/obo/UBERON_0002022), [UBERON:0002657](http://purl.obolibrary.org/obo/UBERON_0002657), [UBERON:0002740](http://purl.obolibrary.org/obo/UBERON_0002740), [UBERON:0002756](http://purl.obolibrary.org/obo/UBERON_0002756), [UBERON:0016636](http://purl.obolibrary.org/obo/UBERON_0016636), ... |

## `GO`: Gene Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                           |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------|
| `GO:GO`         |              2 | [UBERON:0000016](http://purl.obolibrary.org/obo/UBERON_0000016), [UBERON:0006003](http://purl.obolibrary.org/obo/UBERON_0006003) |
| `GO:curator`    |              1 | [UBERON:0005863](http://purl.obolibrary.org/obo/UBERON_0005863)                                                                  |

## `HBA`: Human Brain Atlas

Overall, there were 17 invalid
xrefs to external prefixed with `HBA` (standardized to Bioregistry
prefix [`hba`](https://bioregistry.io/hba)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `HBA:GiRt`      |              1 | [UBERON:0002155](http://purl.obolibrary.org/obo/UBERON_0002155) |
| `HBA:DTL`       |              1 | [UBERON:0002736](http://purl.obolibrary.org/obo/UBERON_0002736) |
| `HBA:ILr`       |              1 | [UBERON:0002965](http://purl.obolibrary.org/obo/UBERON_0002965) |
| `HBA:DTLd`      |              1 | [UBERON:0002984](http://purl.obolibrary.org/obo/UBERON_0002984) |
| `HBA:TELWM`     |              1 | [UBERON:0011299](http://purl.obolibrary.org/obo/UBERON_0011299) |
| `HBA:FLs`       |              1 | [UBERON:0014639](http://purl.obolibrary.org/obo/UBERON_0014639) |
| `HBA:TLs`       |              1 | [UBERON:0014687](http://purl.obolibrary.org/obo/UBERON_0014687) |
| `HBA:MESWM`     |              1 | [UBERON:0016554](http://purl.obolibrary.org/obo/UBERON_0016554) |
| `HBA:MYWM`      |              1 | [UBERON:0019262](http://purl.obolibrary.org/obo/UBERON_0019262) |
| `HBA:PoWM`      |              1 | [UBERON:0019293](http://purl.obolibrary.org/obo/UBERON_0019293) |
| `HBA:TELCom`    |              1 | [UBERON:0019294](http://purl.obolibrary.org/obo/UBERON_0019294) |
| `HBA:ILc`       |              1 | [UBERON:0019295](http://purl.obolibrary.org/obo/UBERON_0019295) |
| `HBA:SolVL`     |              1 | [UBERON:0019312](http://purl.obolibrary.org/obo/UBERON_0019312) |
| `HBA:AOrG`      |              1 | [UBERON:0022244](http://purl.obolibrary.org/obo/UBERON_0022244) |
| `HBA:EL`        |              1 | [UBERON:0022258](http://purl.obolibrary.org/obo/UBERON_0022258) |
| `HBA:PLT`       |              1 | [UBERON:0022268](http://purl.obolibrary.org/obo/UBERON_0022268) |
| `HBA:cpn`       |              1 | [UBERON:0022271](http://purl.obolibrary.org/obo/UBERON_0022271) |

## `HPO`: Human Phenotype Ontology

Overall, there were 5 invalid
xrefs to external prefixed with `HPO` (standardized to Bioregistry
prefix [`hp`](https://bioregistry.io/hp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                           |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------|
| `HPO:curators`  |              2 | [UBERON:0014386](http://purl.obolibrary.org/obo/UBERON_0014386), [UBERON:0034908](http://purl.obolibrary.org/obo/UBERON_0034908) |
| `HPO:pr`        |              2 | [UBERON:0001750](http://purl.obolibrary.org/obo/UBERON_0001750), [UBERON:0035639](http://purl.obolibrary.org/obo/UBERON_0035639) |
| `HPO:probinson` |              1 | [UBERON:0017732](http://purl.obolibrary.org/obo/UBERON_0017732)                                                                  |

## `ISBN`: International Standard Book Number

Overall, there were 1 invalid
xrefs to external prefixed with `ISBN` (standardized to Bioregistry
prefix [`isbn`](https://bioregistry.io/isbn)) that
did not match the standard pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`.

| external_xref                   |   usages_count | usages                                                          |
|---------------------------------|----------------|-----------------------------------------------------------------|
| `ISBN:9004086161,9789004086166` |              1 | [UBERON:7500120](http://purl.obolibrary.org/obo/UBERON_7500120) |

## `MA`: Mouse adult gross anatomy

Overall, there were 16 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
prefix [`ma`](https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MA:th`         |             16 | [UBERON:0000983](http://purl.obolibrary.org/obo/UBERON_0000983), [UBERON:0002470](http://purl.obolibrary.org/obo/UBERON_0002470), [UBERON:0002471](http://purl.obolibrary.org/obo/UBERON_0002471), [UBERON:0002472](http://purl.obolibrary.org/obo/UBERON_0002472), [UBERON:0003282](http://purl.obolibrary.org/obo/UBERON_0003282), ... |

## `MESH`: Medical Subject Headings

Overall, there were 170 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                          |   usages_count | usages                                                                                                                                                                                            |
|----------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MESH:A10.165.265.507`                 |              3 | [UBERON:0014730](http://purl.obolibrary.org/obo/UBERON_0014730), [UBERON:0014730](http://purl.obolibrary.org/obo/UBERON_0014730), [UBERON:0014731](http://purl.obolibrary.org/obo/UBERON_0014731) |
| `MESH:A09.246.631.909.625.125`         |              2 | [UBERON:0000054](http://purl.obolibrary.org/obo/UBERON_0000054), [UBERON:0000054](http://purl.obolibrary.org/obo/UBERON_0000054)                                                                  |
| `MESH:A04.531.621.578`                 |              2 | [UBERON:0001764](http://purl.obolibrary.org/obo/UBERON_0001764), [UBERON:0001764](http://purl.obolibrary.org/obo/UBERON_0001764)                                                                  |
| `MESH:A02.835.232.500.247.343`         |              2 | [UBERON:0006767](http://purl.obolibrary.org/obo/UBERON_0006767), [UBERON:0006767](http://purl.obolibrary.org/obo/UBERON_0006767)                                                                  |
| `MESH:A12.200.946`                     |              2 | [UBERON:0007108](http://purl.obolibrary.org/obo/UBERON_0007108), [UBERON:0007108](http://purl.obolibrary.org/obo/UBERON_0007108)                                                                  |
| `MESH:A13.869.524`                     |              2 | [UBERON:0007362](http://purl.obolibrary.org/obo/UBERON_0007362), [UBERON:0007362](http://purl.obolibrary.org/obo/UBERON_0007362)                                                                  |
| `MESH:D24.185.926.580.590`             |              2 | [UBERON:0008274](http://purl.obolibrary.org/obo/UBERON_0008274), [UBERON:0008274](http://purl.obolibrary.org/obo/UBERON_0008274)                                                                  |
| `MESH:D24.185.926.580.230`             |              2 | [UBERON:0008280](http://purl.obolibrary.org/obo/UBERON_0008280), [UBERON:0008280](http://purl.obolibrary.org/obo/UBERON_0008280)                                                                  |
| `MESH:A13.660`                         |              2 | [UBERON:0010207](http://purl.obolibrary.org/obo/UBERON_0010207), [UBERON:0010207](http://purl.obolibrary.org/obo/UBERON_0010207)                                                                  |
| `MESH:A09.246.631.246.280`             |              2 | [UBERON:0011060](http://purl.obolibrary.org/obo/UBERON_0011060), [UBERON:0011060](http://purl.obolibrary.org/obo/UBERON_0011060)                                                                  |
| `MESH:A06.224.736`                     |              2 | [UBERON:0012279](http://purl.obolibrary.org/obo/UBERON_0012279), [UBERON:0012279](http://purl.obolibrary.org/obo/UBERON_0012279)                                                                  |
| `MESH:A02.513.170`                     |              2 | [UBERON:0012332](http://purl.obolibrary.org/obo/UBERON_0012332), [UBERON:0012332](http://purl.obolibrary.org/obo/UBERON_0012332)                                                                  |
| `MESH:A08.800.550`                     |              2 | [UBERON:0012453](http://purl.obolibrary.org/obo/UBERON_0012453), [UBERON:0012453](http://purl.obolibrary.org/obo/UBERON_0012453)                                                                  |
| `MESH:D24.185.965.850.325`             |              2 | [UBERON:0013106](http://purl.obolibrary.org/obo/UBERON_0013106), [UBERON:0013106](http://purl.obolibrary.org/obo/UBERON_0013106)                                                                  |
| `MESH:D24.185.965.850.480`             |              2 | [UBERON:0013110](http://purl.obolibrary.org/obo/UBERON_0013110), [UBERON:0013110](http://purl.obolibrary.org/obo/UBERON_0013110)                                                                  |
| `MESH:D24.185.965.850.960`             |              2 | [UBERON:0013112](http://purl.obolibrary.org/obo/UBERON_0013112), [UBERON:0013112](http://purl.obolibrary.org/obo/UBERON_0013112)                                                                  |
| `MESH:A08.186.211.577.699`             |              2 | [UBERON:0013201](http://purl.obolibrary.org/obo/UBERON_0013201), [UBERON:0013201](http://purl.obolibrary.org/obo/UBERON_0013201)                                                                  |
| `MESH:A08.186.211.132.810.428.200.462` |              2 | [UBERON:0014908](http://purl.obolibrary.org/obo/UBERON_0014908), [UBERON:0014908](http://purl.obolibrary.org/obo/UBERON_0014908)                                                                  |
| `MESH:G06.535.805`                     |              2 | [UBERON:0018229](http://purl.obolibrary.org/obo/UBERON_0018229), [UBERON:0018229](http://purl.obolibrary.org/obo/UBERON_0018229)                                                                  |
| `MESH:A08.612.600`                     |              2 | [UBERON:0034931](http://purl.obolibrary.org/obo/UBERON_0034931), [UBERON:0034931](http://purl.obolibrary.org/obo/UBERON_0034931)                                                                  |
| `MESH:A08.800.550.700.650`             |              2 | [UBERON:0035017](http://purl.obolibrary.org/obo/UBERON_0035017), [UBERON:0035017](http://purl.obolibrary.org/obo/UBERON_0035017)                                                                  |
| `MESH:A08.800.550.700.840`             |              2 | [UBERON:0035018](http://purl.obolibrary.org/obo/UBERON_0035018), [UBERON:0035018](http://purl.obolibrary.org/obo/UBERON_0035018)                                                                  |
| `MESH:A08.800.050.800.900.700`         |              2 | [UBERON:0004019](http://purl.obolibrary.org/obo/UBERON_0004019), [UBERON:0018392](http://purl.obolibrary.org/obo/UBERON_0018392)                                                                  |
| `MESH:A03.734.414`                     |              1 | [UBERON:0000006](http://purl.obolibrary.org/obo/UBERON_0000006)                                                                                                                                   |
| `MESH:A09.371.729.522`                 |              1 | [UBERON:0000053](http://purl.obolibrary.org/obo/UBERON_0000053)                                                                                                                                   |
| `MESH:A01.456.810`                     |              1 | [UBERON:0000403](http://purl.obolibrary.org/obo/UBERON_0000403)                                                                                                                                   |
| `MESH:A08.186.211.730.385.800.240`     |              1 | [UBERON:0000432](http://purl.obolibrary.org/obo/UBERON_0000432)                                                                                                                                   |
| `MESH:A07.541.510`                     |              1 | [UBERON:0000946](http://purl.obolibrary.org/obo/UBERON_0000946)                                                                                                                                   |
| `MESH:A07.231.114.056`                 |              1 | [UBERON:0000947](http://purl.obolibrary.org/obo/UBERON_0000947)                                                                                                                                   |
| `MESH:A09.371.060.217`                 |              1 | [UBERON:0000964](http://purl.obolibrary.org/obo/UBERON_0000964)                                                                                                                                   |
| `MESH:A10.165.114`                     |              1 | [UBERON:0001013](http://purl.obolibrary.org/obo/UBERON_0001013)                                                                                                                                   |
| `MESH:A13.641`                         |              1 | [UBERON:0001058](http://purl.obolibrary.org/obo/UBERON_0001058)                                                                                                                                   |
| `MESH:A02.633.567.900.500`             |              1 | [UBERON:0001111](http://purl.obolibrary.org/obo/UBERON_0001111)                                                                                                                                   |
| `MESH:A07.231.114.565.755`             |              1 | [UBERON:0001182](http://purl.obolibrary.org/obo/UBERON_0001182)                                                                                                                                   |
| `MESH:A10.549.600`                     |              1 | [UBERON:0001211](http://purl.obolibrary.org/obo/UBERON_0001211)                                                                                                                                   |
| `MESH:A06.407.071.265`                 |              1 | [UBERON:0001236](http://purl.obolibrary.org/obo/UBERON_0001236)                                                                                                                                   |
| `MESH:A05.360.319.679.490`             |              1 | [UBERON:0001295](http://purl.obolibrary.org/obo/UBERON_0001295)                                                                                                                                   |
| `MESH:A02.633.570.500`                 |              1 | [UBERON:0001296](http://purl.obolibrary.org/obo/UBERON_0001296)                                                                                                                                   |
| `MESH:A02.835.232.251`                 |              1 | [UBERON:0001437](http://purl.obolibrary.org/obo/UBERON_0001437)                                                                                                                                   |
| `MESH:A02.835.583.378.062`             |              1 | [UBERON:0001488](http://purl.obolibrary.org/obo/UBERON_0001488)                                                                                                                                   |
| `MESH:A04.531.621.827`                 |              1 | [UBERON:0001724](http://purl.obolibrary.org/obo/UBERON_0001724)                                                                                                                                   |
| `MESH:A09.371.060.067`                 |              1 | [UBERON:0001766](http://purl.obolibrary.org/obo/UBERON_0001766)                                                                                                                                   |
| `MESH:A09.371.060.217.325`             |              1 | [UBERON:0001772](http://purl.obolibrary.org/obo/UBERON_0001772)                                                                                                                                   |
| `MESH:A09.371.060.217.228`             |              1 | [UBERON:0001777](http://purl.obolibrary.org/obo/UBERON_0001777)                                                                                                                                   |
| `MESH:A08.800.800.720`                 |              1 | [UBERON:0001780](http://purl.obolibrary.org/obo/UBERON_0001780)                                                                                                                                   |
| `MESH:A09.371.060`                     |              1 | [UBERON:0001801](http://purl.obolibrary.org/obo/UBERON_0001801)                                                                                                                                   |
| `MESH:A09.371.060.200`                 |              1 | [UBERON:0001811](http://purl.obolibrary.org/obo/UBERON_0001811)                                                                                                                                   |
| `MESH:A12.200.194`                     |              1 | [UBERON:0001914](http://purl.obolibrary.org/obo/UBERON_0001914)                                                                                                                                   |
| `MESH:A07.231.432.952`                 |              1 | [UBERON:0001979](http://purl.obolibrary.org/obo/UBERON_0001979)                                                                                                                                   |
| `MESH:A10.272.491`                     |              1 | [UBERON:0001986](http://purl.obolibrary.org/obo/UBERON_0001986)                                                                                                                                   |
| `MESH:A08.186.211.132.810.428.200`     |              1 | [UBERON:0002037](http://purl.obolibrary.org/obo/UBERON_0002037)                                                                                                                                   |
| `MESH:A06.407.071.140.960`             |              1 | [UBERON:0002053](http://purl.obolibrary.org/obo/UBERON_0002053)                                                                                                                                   |
| `MESH:A06.407.071.140.950`             |              1 | [UBERON:0002054](http://purl.obolibrary.org/obo/UBERON_0002054)                                                                                                                                   |
| `MESH:A06.407.071.140.970`             |              1 | [UBERON:0002055](http://purl.obolibrary.org/obo/UBERON_0002055)                                                                                                                                   |
| `MESH:A07.541.459`                     |              1 | [UBERON:0002099](http://purl.obolibrary.org/obo/UBERON_0002099)                                                                                                                                   |
| `MESH:A08.186.211.132.810.406.286`     |              1 | [UBERON:0002162](http://purl.obolibrary.org/obo/UBERON_0002162)                                                                                                                                   |
| `MESH:A08.186.854.610.800`             |              1 | [UBERON:0002181](http://purl.obolibrary.org/obo/UBERON_0002181)                                                                                                                                   |
| `MESH:A04.411.125`                     |              1 | [UBERON:0002185](http://purl.obolibrary.org/obo/UBERON_0002185)                                                                                                                                   |
| `MESH:A07.231.114.681`                 |              1 | [UBERON:0002250](http://purl.obolibrary.org/obo/UBERON_0002250)                                                                                                                                   |
| `MESH:A12.200.147`                     |              1 | [UBERON:0002297](http://purl.obolibrary.org/obo/UBERON_0002297)                                                                                                                                   |
| `MESH:A05.810.453.736.520.380`         |              1 | [UBERON:0002320](http://purl.obolibrary.org/obo/UBERON_0002320)                                                                                                                                   |
| `MESH:A08.340.315.350.800`             |              1 | [UBERON:0002441](http://purl.obolibrary.org/obo/UBERON_0002441)                                                                                                                                   |
| `MESH:A08.186.211.730.317.357.342.063` |              1 | [UBERON:0002634](http://purl.obolibrary.org/obo/UBERON_0002634)                                                                                                                                   |
| `MESH:A08.186.211.730.385.357.362`     |              1 | [UBERON:0002770](http://purl.obolibrary.org/obo/UBERON_0002770)                                                                                                                                   |
| `MESH:A10.615.284.473`                 |              1 | [UBERON:0003124](http://purl.obolibrary.org/obo/UBERON_0003124)                                                                                                                                   |
| `MESH:A02.513.514.475`                 |              1 | [UBERON:0003676](http://purl.obolibrary.org/obo/UBERON_0003676)                                                                                                                                   |
| `MESH:A02.633.567.600`                 |              1 | [UBERON:0003681](http://purl.obolibrary.org/obo/UBERON_0003681)                                                                                                                                   |
| `MESH:A02.633.567.750`                 |              1 | [UBERON:0003682](http://purl.obolibrary.org/obo/UBERON_0003682)                                                                                                                                   |
| `MESH:A01.047.412`                     |              1 | [UBERON:0003702](http://purl.obolibrary.org/obo/UBERON_0003702)                                                                                                                                   |
| `MESH:A03.159.183.079`                 |              1 | [UBERON:0003703](http://purl.obolibrary.org/obo/UBERON_0003703)                                                                                                                                   |
| `MESH:A03.159.183.158`                 |              1 | [UBERON:0003704](http://purl.obolibrary.org/obo/UBERON_0003704)                                                                                                                                   |
| `MESH:A07.231.836`                     |              1 | [UBERON:0003710](http://purl.obolibrary.org/obo/UBERON_0003710)                                                                                                                                   |
| `MESH:A01.456.830.165`                 |              1 | [UBERON:0003722](http://purl.obolibrary.org/obo/UBERON_0003722)                                                                                                                                   |
| `MESH:A08.800.800.720.800`             |              1 | [UBERON:0003726](http://purl.obolibrary.org/obo/UBERON_0003726)                                                                                                                                   |
| `MESH:A04.760`                         |              1 | [UBERON:0004785](http://purl.obolibrary.org/obo/UBERON_0004785)                                                                                                                                   |
| `MESH:A05.360.444.849`                 |              1 | [UBERON:0005212](http://purl.obolibrary.org/obo/UBERON_0005212)                                                                                                                                   |
| `MESH:A04.531.520.573`                 |              1 | [UBERON:0005386](http://purl.obolibrary.org/obo/UBERON_0005386)                                                                                                                                   |
| `MESH:A07.541.278.395`                 |              1 | [UBERON:0005440](http://purl.obolibrary.org/obo/UBERON_0005440)                                                                                                                                   |
| `MESH:A07.231.114.565`                 |              1 | [UBERON:0005616](http://purl.obolibrary.org/obo/UBERON_0005616)                                                                                                                                   |
| `MESH:A07.231.908.670.385`             |              1 | [UBERON:0005617](http://purl.obolibrary.org/obo/UBERON_0005617)                                                                                                                                   |
| `MESH:A12.207`                         |              1 | [UBERON:0006314](http://purl.obolibrary.org/obo/UBERON_0006314)                                                                                                                                   |
| `MESH:A05.810.453.537.503`             |              1 | [UBERON:0006517](http://purl.obolibrary.org/obo/UBERON_0006517)                                                                                                                                   |
| `MESH:A02.633.567.700`                 |              1 | [UBERON:0006531](http://purl.obolibrary.org/obo/UBERON_0006531)                                                                                                                                   |
| `MESH:A02.513.803`                     |              1 | [UBERON:0006589](http://purl.obolibrary.org/obo/UBERON_0006589)                                                                                                                                   |
| `MESH:A12.200.935`                     |              1 | [UBERON:0007113](http://purl.obolibrary.org/obo/UBERON_0007113)                                                                                                                                   |
| `MESH:A14.254.245`                     |              1 | [UBERON:0007116](http://purl.obolibrary.org/obo/UBERON_0007116)                                                                                                                                   |
| `MESH:A01.047.849`                     |              1 | [UBERON:0007118](http://purl.obolibrary.org/obo/UBERON_0007118)                                                                                                                                   |
| `MESH:A13.869.106`                     |              1 | [UBERON:0007358](http://purl.obolibrary.org/obo/UBERON_0007358)                                                                                                                                   |
| `MESH:A13.869.697`                     |              1 | [UBERON:0007361](http://purl.obolibrary.org/obo/UBERON_0007361)                                                                                                                                   |
| `MESH:A13.869.804`                     |              1 | [UBERON:0007365](http://purl.obolibrary.org/obo/UBERON_0007365)                                                                                                                                   |
| `MESH:A07.231.114.895`                 |              1 | [UBERON:0007610](http://purl.obolibrary.org/obo/UBERON_0007610)                                                                                                                                   |
| `MESH:A14.254.237`                     |              1 | [UBERON:0007774](http://purl.obolibrary.org/obo/UBERON_0007774)                                                                                                                                   |
| `MESH:A14.254.860.715`                 |              1 | [UBERON:0007776](http://purl.obolibrary.org/obo/UBERON_0007776)                                                                                                                                   |
| `MESH:A12.383`                         |              1 | [UBERON:0007780](http://purl.obolibrary.org/obo/UBERON_0007780)                                                                                                                                   |
| `MESH:A12.207.119`                     |              1 | [UBERON:0007795](http://purl.obolibrary.org/obo/UBERON_0007795)                                                                                                                                   |
| `MESH:A14.254.229`                     |              1 | [UBERON:0007799](http://purl.obolibrary.org/obo/UBERON_0007799)                                                                                                                                   |
| `MESH:A09.246.631.663`                 |              1 | [UBERON:0007833](http://purl.obolibrary.org/obo/UBERON_0007833)                                                                                                                                   |
| `MESH:A01.456.505.580`                 |              1 | [UBERON:0008200](http://purl.obolibrary.org/obo/UBERON_0008200)                                                                                                                                   |
| `MESH:A01.047.365`                     |              1 | [UBERON:0008337](http://purl.obolibrary.org/obo/UBERON_0008337)                                                                                                                                   |
| `MESH:A02.633.567.825`                 |              1 | [UBERON:0008450](http://purl.obolibrary.org/obo/UBERON_0008450)                                                                                                                                   |
| `MESH:A01.456.830.200`                 |              1 | [UBERON:0008788](http://purl.obolibrary.org/obo/UBERON_0008788)                                                                                                                                   |
| `MESH:A08.186.211.730.885.213.670.675` |              1 | [UBERON:0008930](http://purl.obolibrary.org/obo/UBERON_0008930)                                                                                                                                   |
| `MESH:A08.800.800.720.725`             |              1 | [UBERON:0009623](http://purl.obolibrary.org/obo/UBERON_0009623)                                                                                                                                   |
| `MESH:A14.254.860.700.500`             |              1 | [UBERON:0009977](http://purl.obolibrary.org/obo/UBERON_0009977)                                                                                                                                   |
| `MESH:A07.231.432`                     |              1 | [UBERON:0010523](http://purl.obolibrary.org/obo/UBERON_0010523)                                                                                                                                   |
| `MESH:A08.663.542.100`                 |              1 | [UBERON:0011924](http://purl.obolibrary.org/obo/UBERON_0011924)                                                                                                                                   |
| `MESH:A08.663.542.122`                 |              1 | [UBERON:0011925](http://purl.obolibrary.org/obo/UBERON_0011925)                                                                                                                                   |
| `MESH:D24.185.965.850`                 |              1 | [UBERON:0013076](http://purl.obolibrary.org/obo/UBERON_0013076)                                                                                                                                   |
| `MESH:A08.800.550.700.120.600.350`     |              1 | [UBERON:0034972](http://purl.obolibrary.org/obo/UBERON_0034972)                                                                                                                                   |
| `MESH:A08.800.550.700.120.600`         |              1 | [UBERON:0034979](http://purl.obolibrary.org/obo/UBERON_0034979)                                                                                                                                   |
| `MESH:A16.254.500`                     |              1 | [UBERON:0000080](http://purl.obolibrary.org/obo/UBERON_0000080)                                                                                                                                   |
| `MESH:A01.378.610`                     |              1 | [UBERON:0000978](http://purl.obolibrary.org/obo/UBERON_0000978)                                                                                                                                   |
| `MESH:A03.734.667`                     |              1 | [UBERON:0001064](http://purl.obolibrary.org/obo/UBERON_0001064)                                                                                                                                   |
| `MESH:A02.835.232.834`                 |              1 | [UBERON:0001130](http://purl.obolibrary.org/obo/UBERON_0001130)                                                                                                                                   |
| `MESH:A05.360.319.779.479`             |              1 | [UBERON:0001346](http://purl.obolibrary.org/obo/UBERON_0001346)                                                                                                                                   |
| `MESH:A01.378.800`                     |              1 | [UBERON:0001460](http://purl.obolibrary.org/obo/UBERON_0001460)                                                                                                                                   |
| `MESH:A14.254.646`                     |              1 | [UBERON:0001758](http://purl.obolibrary.org/obo/UBERON_0001758)                                                                                                                                   |
| `MESH:A08.800.800.120.680.660`         |              1 | [UBERON:0001783](http://purl.obolibrary.org/obo/UBERON_0001783)                                                                                                                                   |
| `MESH:A08.800.050.050.150`             |              1 | [UBERON:0002010](http://purl.obolibrary.org/obo/UBERON_0002010)                                                                                                                                   |
| `MESH:A02.835.232`                     |              1 | [UBERON:0002481](http://purl.obolibrary.org/obo/UBERON_0002481)                                                                                                                                   |
| `MESH:A09.246.631.909.625`             |              1 | [UBERON:0002518](http://purl.obolibrary.org/obo/UBERON_0002518)                                                                                                                                   |
| `MESH:A08.186.211.730.385.357.352`     |              1 | [UBERON:0002555](http://purl.obolibrary.org/obo/UBERON_0002555)                                                                                                                                   |
| `MESH:A07.231.114.891`                 |              1 | [UBERON:0003473](http://purl.obolibrary.org/obo/UBERON_0003473)                                                                                                                                   |
| `MESH:A04.329.364.737`                 |              1 | [UBERON:0003706](http://purl.obolibrary.org/obo/UBERON_0003706)                                                                                                                                   |
| `MESH:A01.378.610.500`                 |              1 | [UBERON:0003823](http://purl.obolibrary.org/obo/UBERON_0003823)                                                                                                                                   |
| `MESH:A09.371.894.223.250`             |              1 | [UBERON:0003957](http://purl.obolibrary.org/obo/UBERON_0003957)                                                                                                                                   |
| `MESH:A05.810.453.736.560.570`         |              1 | [UBERON:0004134](http://purl.obolibrary.org/obo/UBERON_0004134)                                                                                                                                   |
| `MESH:A12.207.571`                     |              1 | [UBERON:0006586](http://purl.obolibrary.org/obo/UBERON_0006586)                                                                                                                                   |
| `MESH:A09.246.631.246.930`             |              1 | [UBERON:0006724](http://purl.obolibrary.org/obo/UBERON_0006724)                                                                                                                                   |
| `MESH:A16.254.891`                     |              1 | [UBERON:0007105](http://purl.obolibrary.org/obo/UBERON_0007105)                                                                                                                                   |
| `MESH:A16.254.403.473.200`             |              1 | [UBERON:0007106](http://purl.obolibrary.org/obo/UBERON_0007106)                                                                                                                                   |
| `MESH:A01.047.025.600.225`             |              1 | [UBERON:0007111](http://purl.obolibrary.org/obo/UBERON_0007111)                                                                                                                                   |
| `MESH:A09.371.670`                     |              1 | [UBERON:0007625](http://purl.obolibrary.org/obo/UBERON_0007625)                                                                                                                                   |
| `MESH:A03.365.414`                     |              1 | [UBERON:0007650](http://purl.obolibrary.org/obo/UBERON_0007650)                                                                                                                                   |
| `MESH:A02.835.583.378.900`             |              1 | [UBERON:0007721](http://purl.obolibrary.org/obo/UBERON_0007721)                                                                                                                                   |
| `MESH:A02.835.583.378.831`             |              1 | [UBERON:0008447](http://purl.obolibrary.org/obo/UBERON_0008447)                                                                                                                                   |
| `MESH:A06.407.747.357`                 |              1 | [UBERON:0009976](http://purl.obolibrary.org/obo/UBERON_0009976)                                                                                                                                   |
| `MESH:A06.224`                         |              1 | [UBERON:0010074](http://purl.obolibrary.org/obo/UBERON_0010074)                                                                                                                                   |
| `MESH:A08.663.542.075.800`             |              1 | [UBERON:0011926](http://purl.obolibrary.org/obo/UBERON_0011926)                                                                                                                                   |
| `MESH:A12.207.152.200`                 |              1 | [UBERON:0012168](http://purl.obolibrary.org/obo/UBERON_0012168)                                                                                                                                   |
| `MESH:A13.734`                         |              1 | [UBERON:0012281](http://purl.obolibrary.org/obo/UBERON_0012281)                                                                                                                                   |
| `MESH:A08.800.800.720.725.150`         |              1 | [UBERON:0012337](http://purl.obolibrary.org/obo/UBERON_0012337)                                                                                                                                   |
| `MESH:A11.284.180.565`                 |              1 | [UBERON:0012423](http://purl.obolibrary.org/obo/UBERON_0012423)                                                                                                                                   |
| `MESH:A08.800.550.700`                 |              1 | [UBERON:0012451](http://purl.obolibrary.org/obo/UBERON_0012451)                                                                                                                                   |
| `MESH:A13.970`                         |              1 | [UBERON:0013196](http://purl.obolibrary.org/obo/UBERON_0013196)                                                                                                                                   |
| `MESH:E05.256`                         |              1 | [UBERON:0013487](http://purl.obolibrary.org/obo/UBERON_0013487)                                                                                                                                   |

## `MGI`: Mouse Genome Informatics

Overall, there were 262 invalid
xrefs to external prefixed with `MGI` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MGI:anna`      |            104 | [UBERON:0000057](http://purl.obolibrary.org/obo/UBERON_0000057), [UBERON:0000076](http://purl.obolibrary.org/obo/UBERON_0000076), [UBERON:0000114](http://purl.obolibrary.org/obo/UBERON_0000114), [UBERON:0000325](http://purl.obolibrary.org/obo/UBERON_0000325), [UBERON:0000453](http://purl.obolibrary.org/obo/UBERON_0000453), ... |
| `MGI:csmith`    |             73 | [UBERON:0000305](http://purl.obolibrary.org/obo/UBERON_0000305), [UBERON:0000995](http://purl.obolibrary.org/obo/UBERON_0000995), [UBERON:0001063](http://purl.obolibrary.org/obo/UBERON_0001063), [UBERON:0001078](http://purl.obolibrary.org/obo/UBERON_0001078), [UBERON:0001111](http://purl.obolibrary.org/obo/UBERON_0001111), ... |
| `MGI:cwg`       |             25 | [UBERON:0001013](http://purl.obolibrary.org/obo/UBERON_0001013), [UBERON:0001542](http://purl.obolibrary.org/obo/UBERON_0001542), [UBERON:0001543](http://purl.obolibrary.org/obo/UBERON_0001543), [UBERON:0001728](http://purl.obolibrary.org/obo/UBERON_0001728), [UBERON:0001729](http://purl.obolibrary.org/obo/UBERON_0001729), ... |
| `MGI:smb`       |             24 | [UBERON:0000362](http://purl.obolibrary.org/obo/UBERON_0000362), [UBERON:0000396](http://purl.obolibrary.org/obo/UBERON_0000396), [UBERON:0001295](http://purl.obolibrary.org/obo/UBERON_0001295), [UBERON:0001348](http://purl.obolibrary.org/obo/UBERON_0001348), [UBERON:0001772](http://purl.obolibrary.org/obo/UBERON_0001772), ... |
| `MGI:llw2`      |             11 | [UBERON:0000388](http://purl.obolibrary.org/obo/UBERON_0000388), [UBERON:0000959](http://purl.obolibrary.org/obo/UBERON_0000959), [UBERON:0001235](http://purl.obolibrary.org/obo/UBERON_0001235), [UBERON:0001236](http://purl.obolibrary.org/obo/UBERON_0001236), [UBERON:0001451](http://purl.obolibrary.org/obo/UBERON_0001451), ... |
| `MGI:cs`        |              8 | [UBERON:0018242](http://purl.obolibrary.org/obo/UBERON_0018242), [UBERON:0034932](http://purl.obolibrary.org/obo/UBERON_0034932), [UBERON:0035617](http://purl.obolibrary.org/obo/UBERON_0035617), [UBERON:0035618](http://purl.obolibrary.org/obo/UBERON_0035618), [UBERON:0035619](http://purl.obolibrary.org/obo/UBERON_0035619), ... |
| `MGI:pvb`       |              5 | [UBERON:0000087](http://purl.obolibrary.org/obo/UBERON_0000087), [UBERON:0001000](http://purl.obolibrary.org/obo/UBERON_0001000), [UBERON:0001230](http://purl.obolibrary.org/obo/UBERON_0001230), [UBERON:0001301](http://purl.obolibrary.org/obo/UBERON_0001301), [UBERON:0005623](http://purl.obolibrary.org/obo/UBERON_0005623)      |
| `MGI:rbabiuk`   |              3 | [UBERON:0001213](http://purl.obolibrary.org/obo/UBERON_0001213), [UBERON:0010412](http://purl.obolibrary.org/obo/UBERON_0010412), [UBERON:0014396](http://purl.obolibrary.org/obo/UBERON_0014396)                                                                                                                                        |
| `MGI:monikat`   |              3 | [UBERON:0002115](http://purl.obolibrary.org/obo/UBERON_0002115), [UBERON:0002493](http://purl.obolibrary.org/obo/UBERON_0002493), [UBERON:0002511](http://purl.obolibrary.org/obo/UBERON_0002511)                                                                                                                                        |
| `MGI:hdene`     |              2 | [UBERON:0001439](http://purl.obolibrary.org/obo/UBERON_0001439), [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832)                                                                                                                                                                                                         |
| `MGI:brs`       |              1 | [UBERON:0001296](http://purl.obolibrary.org/obo/UBERON_0001296)                                                                                                                                                                                                                                                                          |
| `MGI:Anna`      |              1 | [UBERON:0005203](http://purl.obolibrary.org/obo/UBERON_0005203)                                                                                                                                                                                                                                                                          |
| `MGI:smith`     |              1 | [UBERON:0035941](http://purl.obolibrary.org/obo/UBERON_0035941)                                                                                                                                                                                                                                                                          |
| `MGI:sbello`    |              1 | [UBERON:0036145](http://purl.obolibrary.org/obo/UBERON_0036145)                                                                                                                                                                                                                                                                          |

## `MP`: Mammalian Phenotype Ontology

Overall, there were 37 invalid
xrefs to external prefixed with `MP` (standardized to Bioregistry
prefix [`mp`](https://bioregistry.io/mp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MP:anna`       |             19 | [UBERON:0001258](http://purl.obolibrary.org/obo/UBERON_0001258), [UBERON:0001338](http://purl.obolibrary.org/obo/UBERON_0001338), [UBERON:0002068](http://purl.obolibrary.org/obo/UBERON_0002068), [UBERON:0002366](http://purl.obolibrary.org/obo/UBERON_0002366), [UBERON:0002366](http://purl.obolibrary.org/obo/UBERON_0002366), ... |
| `MP:MP`         |             17 | [UBERON:0000173](http://purl.obolibrary.org/obo/UBERON_0000173), [UBERON:0001259](http://purl.obolibrary.org/obo/UBERON_0001259), [UBERON:0001947](http://purl.obolibrary.org/obo/UBERON_0001947), [UBERON:0005452](http://purl.obolibrary.org/obo/UBERON_0005452), [UBERON:0008835](http://purl.obolibrary.org/obo/UBERON_0008835), ... |
| `MP:000999`     |              1 | [UBERON:0035922](http://purl.obolibrary.org/obo/UBERON_0035922)                                                                                                                                                                                                                                                                          |

## `NCIT`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCIT` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `NCIT:NCIT`     |              1 | [UBERON:0010499](http://purl.obolibrary.org/obo/UBERON_0010499) |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 230 invalid
xrefs to external prefixed with `ncithesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                                                 |   usages_count | usages                                                                                                                           |
|---------------------------------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------|
| `ncithesaurus:Corona_Dentis`                                  |              2 | [UBERON:0003675](http://purl.obolibrary.org/obo/UBERON_0003675), [UBERON:0003675](http://purl.obolibrary.org/obo/UBERON_0003675) |
| `ncithesaurus:Shell`                                          |              2 | [UBERON:0006612](http://purl.obolibrary.org/obo/UBERON_0006612), [UBERON:0006612](http://purl.obolibrary.org/obo/UBERON_0006612) |
| `ncithesaurus:Gland_of_the_Third_Eyelid`                      |              2 | [UBERON:0013230](http://purl.obolibrary.org/obo/UBERON_0013230), [UBERON:0013230](http://purl.obolibrary.org/obo/UBERON_0013230) |
| `ncithesaurus:Cerebral_Subcortex`                             |              1 | [UBERON:0000454](http://purl.obolibrary.org/obo/UBERON_0000454)                                                                  |
| `ncithesaurus:Ileal_Vein`                                     |              1 | [UBERON:0001217](http://purl.obolibrary.org/obo/UBERON_0001217)                                                                  |
| `ncithesaurus:Median_Basilic_Vein`                            |              1 | [UBERON:0001414](http://purl.obolibrary.org/obo/UBERON_0001414)                                                                  |
| `ncithesaurus:Pectoralis_Muscle`                              |              1 | [UBERON:0001495](http://purl.obolibrary.org/obo/UBERON_0001495)                                                                  |
| `ncithesaurus:Submental_Vein`                                 |              1 | [UBERON:0001655](http://purl.obolibrary.org/obo/UBERON_0001655)                                                                  |
| `ncithesaurus:Deep_Temporal_Vein`                             |              1 | [UBERON:0001661](http://purl.obolibrary.org/obo/UBERON_0001661)                                                                  |
| `ncithesaurus:Nucleus_of_Diagonal_Band`                       |              1 | [UBERON:0001879](http://purl.obolibrary.org/obo/UBERON_0001879)                                                                  |
| `ncithesaurus:Papillary_Dermis`                               |              1 | [UBERON:0001992](http://purl.obolibrary.org/obo/UBERON_0001992)                                                                  |
| `ncithesaurus:Thymic_Lobule`                                  |              1 | [UBERON:0002125](http://purl.obolibrary.org/obo/UBERON_0002125)                                                                  |
| `ncithesaurus:Endometrial_Stroma`                             |              1 | [UBERON:0002337](http://purl.obolibrary.org/obo/UBERON_0002337)                                                                  |
| `ncithesaurus:Sacral_Lymph_Node`                              |              1 | [UBERON:0002528](http://purl.obolibrary.org/obo/UBERON_0002528)                                                                  |
| `ncithesaurus:Anterior_Cruciate_Ligament`                     |              1 | [UBERON:0003671](http://purl.obolibrary.org/obo/UBERON_0003671)                                                                  |
| `ncithesaurus:Floor_of_the_Mouth`                             |              1 | [UBERON:0003679](http://purl.obolibrary.org/obo/UBERON_0003679)                                                                  |
| `ncithesaurus:Omentum`                                        |              1 | [UBERON:0003688](http://purl.obolibrary.org/obo/UBERON_0003688)                                                                  |
| `ncithesaurus:Abdominal_Wall`                                 |              1 | [UBERON:0003697](http://purl.obolibrary.org/obo/UBERON_0003697)                                                                  |
| `ncithesaurus:Splenic_Vein`                                   |              1 | [UBERON:0003713](http://purl.obolibrary.org/obo/UBERON_0003713)                                                                  |
| `ncithesaurus:CA4_Field_of_the_Cornu_Ammonis`                 |              1 | [UBERON:0003884](http://purl.obolibrary.org/obo/UBERON_0003884)                                                                  |
| `ncithesaurus:Cortical_Cell_Layer_of_the_Cerebellum`          |              1 | [UBERON:0004130](http://purl.obolibrary.org/obo/UBERON_0004130)                                                                  |
| `ncithesaurus:Bowman_s_Membrane`                              |              1 | [UBERON:0004370](http://purl.obolibrary.org/obo/UBERON_0004370)                                                                  |
| `ncithesaurus:Gastric_Vein`                                   |              1 | [UBERON:0004450](http://purl.obolibrary.org/obo/UBERON_0004450)                                                                  |
| `ncithesaurus:Digital_Vein`                                   |              1 | [UBERON:0004562](http://purl.obolibrary.org/obo/UBERON_0004562)                                                                  |
| `ncithesaurus:Rib_3`                                          |              1 | [UBERON:0004603](http://purl.obolibrary.org/obo/UBERON_0004603)                                                                  |
| `ncithesaurus:Rib_4`                                          |              1 | [UBERON:0004604](http://purl.obolibrary.org/obo/UBERON_0004604)                                                                  |
| `ncithesaurus:Rib_5`                                          |              1 | [UBERON:0004605](http://purl.obolibrary.org/obo/UBERON_0004605)                                                                  |
| `ncithesaurus:Rib_6`                                          |              1 | [UBERON:0004606](http://purl.obolibrary.org/obo/UBERON_0004606)                                                                  |
| `ncithesaurus:Rib_7`                                          |              1 | [UBERON:0004607](http://purl.obolibrary.org/obo/UBERON_0004607)                                                                  |
| `ncithesaurus:Rib_9`                                          |              1 | [UBERON:0004608](http://purl.obolibrary.org/obo/UBERON_0004608)                                                                  |
| `ncithesaurus:C3_Vertebra`                                    |              1 | [UBERON:0004612](http://purl.obolibrary.org/obo/UBERON_0004612)                                                                  |
| `ncithesaurus:C4_Vertebra`                                    |              1 | [UBERON:0004613](http://purl.obolibrary.org/obo/UBERON_0004613)                                                                  |
| `ncithesaurus:C5_Vertebra`                                    |              1 | [UBERON:0004614](http://purl.obolibrary.org/obo/UBERON_0004614)                                                                  |
| `ncithesaurus:C6_Vertebra`                                    |              1 | [UBERON:0004615](http://purl.obolibrary.org/obo/UBERON_0004615)                                                                  |
| `ncithesaurus:L1_Vertebra`                                    |              1 | [UBERON:0004617](http://purl.obolibrary.org/obo/UBERON_0004617)                                                                  |
| `ncithesaurus:L2_Vertebra`                                    |              1 | [UBERON:0004618](http://purl.obolibrary.org/obo/UBERON_0004618)                                                                  |
| `ncithesaurus:L3_Vertebra`                                    |              1 | [UBERON:0004619](http://purl.obolibrary.org/obo/UBERON_0004619)                                                                  |
| `ncithesaurus:L4_Vertebra`                                    |              1 | [UBERON:0004620](http://purl.obolibrary.org/obo/UBERON_0004620)                                                                  |
| `ncithesaurus:L5_Vertebra`                                    |              1 | [UBERON:0004621](http://purl.obolibrary.org/obo/UBERON_0004621)                                                                  |
| `ncithesaurus:T1_Vertebra`                                    |              1 | [UBERON:0004626](http://purl.obolibrary.org/obo/UBERON_0004626)                                                                  |
| `ncithesaurus:T2_Vertebra`                                    |              1 | [UBERON:0004627](http://purl.obolibrary.org/obo/UBERON_0004627)                                                                  |
| `ncithesaurus:T3_Vertebra`                                    |              1 | [UBERON:0004628](http://purl.obolibrary.org/obo/UBERON_0004628)                                                                  |
| `ncithesaurus:T4_Vertebra`                                    |              1 | [UBERON:0004629](http://purl.obolibrary.org/obo/UBERON_0004629)                                                                  |
| `ncithesaurus:T5_Vertebra`                                    |              1 | [UBERON:0004630](http://purl.obolibrary.org/obo/UBERON_0004630)                                                                  |
| `ncithesaurus:T6_Vertebra`                                    |              1 | [UBERON:0004631](http://purl.obolibrary.org/obo/UBERON_0004631)                                                                  |
| `ncithesaurus:T7_Vertebra`                                    |              1 | [UBERON:0004632](http://purl.obolibrary.org/obo/UBERON_0004632)                                                                  |
| `ncithesaurus:T9_Vertebra`                                    |              1 | [UBERON:0004633](http://purl.obolibrary.org/obo/UBERON_0004633)                                                                  |
| `ncithesaurus:T10_Vertebra`                                   |              1 | [UBERON:0004634](http://purl.obolibrary.org/obo/UBERON_0004634)                                                                  |
| `ncithesaurus:T11_Vertebra`                                   |              1 | [UBERON:0004635](http://purl.obolibrary.org/obo/UBERON_0004635)                                                                  |
| `ncithesaurus:T12_Vertebra`                                   |              1 | [UBERON:0004636](http://purl.obolibrary.org/obo/UBERON_0004636)                                                                  |
| `ncithesaurus:Pancreatico-Duodenal_Vein`                      |              1 | [UBERON:0004690](http://purl.obolibrary.org/obo/UBERON_0004690)                                                                  |
| `ncithesaurus:Iliac_Vein`                                     |              1 | [UBERON:0005610](http://purl.obolibrary.org/obo/UBERON_0005610)                                                                  |
| `ncithesaurus:Aortic_Segment`                                 |              1 | [UBERON:0005800](http://purl.obolibrary.org/obo/UBERON_0005800)                                                                  |
| `ncithesaurus:Myelinated_Nerve_Fiber`                         |              1 | [UBERON:0006135](http://purl.obolibrary.org/obo/UBERON_0006135)                                                                  |
| `ncithesaurus:Communicating_Artery`                           |              1 | [UBERON:0006347](http://purl.obolibrary.org/obo/UBERON_0006347)                                                                  |
| `ncithesaurus:Epigastric_Artery`                              |              1 | [UBERON:0006349](http://purl.obolibrary.org/obo/UBERON_0006349)                                                                  |
| `ncithesaurus:Tooth_Cusp`                                     |              1 | [UBERON:0006844](http://purl.obolibrary.org/obo/UBERON_0006844)                                                                  |
| `ncithesaurus:Inferior_Thyroid_Artery`                        |              1 | [UBERON:0007149](http://purl.obolibrary.org/obo/UBERON_0007149)                                                                  |
| `ncithesaurus:Inferior_Sagittal_Sinus`                        |              1 | [UBERON:0007152](http://purl.obolibrary.org/obo/UBERON_0007152)                                                                  |
| `ncithesaurus:Deep_Epigastric_Vein`                           |              1 | [UBERON:0007154](http://purl.obolibrary.org/obo/UBERON_0007154)                                                                  |
| `ncithesaurus:Footpad`                                        |              1 | [UBERON:0008838](http://purl.obolibrary.org/obo/UBERON_0008838)                                                                  |
| `ncithesaurus:Lung_Lower_Lobe`                                |              1 | [UBERON:0008949](http://purl.obolibrary.org/obo/UBERON_0008949)                                                                  |
| `ncithesaurus:Circumflex_Iliac_Artery`                        |              1 | [UBERON:0009026](http://purl.obolibrary.org/obo/UBERON_0009026)                                                                  |
| `ncithesaurus:Anal_Membrane`                                  |              1 | [UBERON:0009195](http://purl.obolibrary.org/obo/UBERON_0009195)                                                                  |
| `ncithesaurus:Alveolar_Artery`                                |              1 | [UBERON:0009654](http://purl.obolibrary.org/obo/UBERON_0009654)                                                                  |
| `ncithesaurus:Auricular_Artery`                               |              1 | [UBERON:0009655](http://purl.obolibrary.org/obo/UBERON_0009655)                                                                  |
| `ncithesaurus:Spermatic_Artery`                               |              1 | [UBERON:0009659](http://purl.obolibrary.org/obo/UBERON_0009659)                                                                  |
| `ncithesaurus:Anterior_Inferior_Cerebellar_Artery`            |              1 | [UBERON:0009689](http://purl.obolibrary.org/obo/UBERON_0009689)                                                                  |
| `ncithesaurus:Lobe`                                           |              1 | [UBERON:0009912](http://purl.obolibrary.org/obo/UBERON_0009912)                                                                  |
| `ncithesaurus:Pulmonary_Lobule`                               |              1 | [UBERON:0010368](http://purl.obolibrary.org/obo/UBERON_0010368)                                                                  |
| `ncithesaurus:Parametrium`                                    |              1 | [UBERON:0010391](http://purl.obolibrary.org/obo/UBERON_0010391)                                                                  |
| `ncithesaurus:Meningeal_Layer_of_the_Dura_Mater`              |              1 | [UBERON:0010506](http://purl.obolibrary.org/obo/UBERON_0010506)                                                                  |
| `ncithesaurus:Rib_8`                                          |              1 | [UBERON:0010757](http://purl.obolibrary.org/obo/UBERON_0010757)                                                                  |
| `ncithesaurus:T8_Vertebra`                                    |              1 | [UBERON:0011050](http://purl.obolibrary.org/obo/UBERON_0011050)                                                                  |
| `ncithesaurus:Inferior_Pancreatico-Duodenal_Vein`             |              1 | [UBERON:0011383](http://purl.obolibrary.org/obo/UBERON_0011383)                                                                  |
| `ncithesaurus:Growing_Follicle`                               |              1 | [UBERON:0012186](http://purl.obolibrary.org/obo/UBERON_0012186)                                                                  |
| `ncithesaurus:Phrenic_Vein`                                   |              1 | [UBERON:0012193](http://purl.obolibrary.org/obo/UBERON_0012193)                                                                  |
| `ncithesaurus:Endocervical_Glandular_Epithelium`              |              1 | [UBERON:0012252](http://purl.obolibrary.org/obo/UBERON_0012252)                                                                  |
| `ncithesaurus:Nasal-Associated_Lymphoid_Tissue`               |              1 | [UBERON:0012330](http://purl.obolibrary.org/obo/UBERON_0012330)                                                                  |
| `ncithesaurus:Retromolar_Trigone`                             |              1 | [UBERON:0012376](http://purl.obolibrary.org/obo/UBERON_0012376)                                                                  |
| `ncithesaurus:Systemic_Vein`                                  |              1 | [UBERON:0013140](http://purl.obolibrary.org/obo/UBERON_0013140)                                                                  |
| `ncithesaurus:Choroidal_Artery`                               |              1 | [UBERON:0013151](http://purl.obolibrary.org/obo/UBERON_0013151)                                                                  |
| `ncithesaurus:Anterior_Wall_of_the_Tympanum`                  |              1 | [UBERON:0013173](http://purl.obolibrary.org/obo/UBERON_0013173)                                                                  |
| `ncithesaurus:Accessory_Lacrimal_Gland`                       |              1 | [UBERON:0013226](http://purl.obolibrary.org/obo/UBERON_0013226)                                                                  |
| `ncithesaurus:Upper_Third_of_the_Esophagus`                   |              1 | [UBERON:0013472](http://purl.obolibrary.org/obo/UBERON_0013472)                                                                  |
| `ncithesaurus:Lower_Third_of_the_Esophagus`                   |              1 | [UBERON:0013473](http://purl.obolibrary.org/obo/UBERON_0013473)                                                                  |
| `ncithesaurus:Middle_Third_of_the_Esophagus`                  |              1 | [UBERON:0013474](http://purl.obolibrary.org/obo/UBERON_0013474)                                                                  |
| `ncithesaurus:Epidermal_Ridges`                               |              1 | [UBERON:0013487](http://purl.obolibrary.org/obo/UBERON_0013487)                                                                  |
| `ncithesaurus:Lateral_Lobe_of_the_Prostate`                   |              1 | [UBERON:0013637](http://purl.obolibrary.org/obo/UBERON_0013637)                                                                  |
| `ncithesaurus:Temporal_Sulcus`                                |              1 | [UBERON:0014687](http://purl.obolibrary.org/obo/UBERON_0014687)                                                                  |
| `ncithesaurus:Middle_Temporal_Sulcus`                         |              1 | [UBERON:0014689](http://purl.obolibrary.org/obo/UBERON_0014689)                                                                  |
| `ncithesaurus:Interlobular_Duct`                              |              1 | [UBERON:0014716](http://purl.obolibrary.org/obo/UBERON_0014716)                                                                  |
| `ncithesaurus:Intercalated_Duct_of_the_Salivary_Gland_System` |              1 | [UBERON:0014727](http://purl.obolibrary.org/obo/UBERON_0014727)                                                                  |
| `ncithesaurus:Perivascular_Space`                             |              1 | [UBERON:0014930](http://purl.obolibrary.org/obo/UBERON_0014930)                                                                  |
| `ncithesaurus:Hilar_Portion_of_the_Hepatic_Duct`              |              1 | [UBERON:0015423](http://purl.obolibrary.org/obo/UBERON_0015423)                                                                  |
| `ncithesaurus:External_Elastic_Membrane`                      |              1 | [UBERON:0015433](http://purl.obolibrary.org/obo/UBERON_0015433)                                                                  |
| `ncithesaurus:Tracheobronchial_Lymph_Node`                    |              1 | [UBERON:0015472](http://purl.obolibrary.org/obo/UBERON_0015472)                                                                  |
| `ncithesaurus:Body_of_the_Corpus_Callosum`                    |              1 | [UBERON:0015510](http://purl.obolibrary.org/obo/UBERON_0015510)                                                                  |
| `ncithesaurus:Hepatic_Lymph_Node`                             |              1 | [UBERON:0015859](http://purl.obolibrary.org/obo/UBERON_0015859)                                                                  |
| `ncithesaurus:Gastric_Lymph_Node`                             |              1 | [UBERON:0015863](http://purl.obolibrary.org/obo/UBERON_0015863)                                                                  |
| `ncithesaurus:Pelvic_Lymph_Node`                              |              1 | [UBERON:0015876](http://purl.obolibrary.org/obo/UBERON_0015876)                                                                  |
| `ncithesaurus:Neurovascular_Bundle`                           |              1 | [UBERON:0016630](http://purl.obolibrary.org/obo/UBERON_0016630)                                                                  |
| `ncithesaurus:Internal_Mammary_Vein`                          |              1 | [UBERON:0017646](http://purl.obolibrary.org/obo/UBERON_0017646)                                                                  |
| `ncithesaurus:Infraclavicular_Lymph_Node`                     |              1 | [UBERON:0035162](http://purl.obolibrary.org/obo/UBERON_0035162)                                                                  |
| `ncithesaurus:Posterior_Surface_of_the_Prostate`              |              1 | [UBERON:0035165](http://purl.obolibrary.org/obo/UBERON_0035165)                                                                  |
| `ncithesaurus:Infraclavicular_Region`                         |              1 | [UBERON:0035168](http://purl.obolibrary.org/obo/UBERON_0035168)                                                                  |
| `ncithesaurus:Right_Ear`                                      |              1 | [UBERON:0035174](http://purl.obolibrary.org/obo/UBERON_0035174)                                                                  |
| `ncithesaurus:Abdominal_Esophagus`                            |              1 | [UBERON:0035177](http://purl.obolibrary.org/obo/UBERON_0035177)                                                                  |
| `ncithesaurus:Calcarine_Artery`                               |              1 | [UBERON:0035183](http://purl.obolibrary.org/obo/UBERON_0035183)                                                                  |
| `ncithesaurus:Superficial_Lymphatic_Vessel`                   |              1 | [UBERON:0035198](http://purl.obolibrary.org/obo/UBERON_0035198)                                                                  |
| `ncithesaurus:Gastrocolic_Ligament`                           |              1 | [UBERON:0035201](http://purl.obolibrary.org/obo/UBERON_0035201)                                                                  |
| `ncithesaurus:Occipital_Lymph_Node`                           |              1 | [UBERON:0035204](http://purl.obolibrary.org/obo/UBERON_0035204)                                                                  |
| `ncithesaurus:Deep_Peroneal_Nerve`                            |              1 | [UBERON:0035207](http://purl.obolibrary.org/obo/UBERON_0035207)                                                                  |
| `ncithesaurus:Base_of_the_Heart`                              |              1 | [UBERON:0035213](http://purl.obolibrary.org/obo/UBERON_0035213)                                                                  |
| `ncithesaurus:Internal_Mammary_Lymph_Node`                    |              1 | [UBERON:0035219](http://purl.obolibrary.org/obo/UBERON_0035219)                                                                  |
| `ncithesaurus:Anterior_Temporal_Artery`                       |              1 | [UBERON:0035225](http://purl.obolibrary.org/obo/UBERON_0035225)                                                                  |
| `ncithesaurus:Superficial_Middle_Cerebral_Vein`               |              1 | [UBERON:0035231](http://purl.obolibrary.org/obo/UBERON_0035231)                                                                  |
| `ncithesaurus:Medial_Femoral_Vein`                            |              1 | [UBERON:0035234](http://purl.obolibrary.org/obo/UBERON_0035234)                                                                  |
| `ncithesaurus:Anal_Sinus`                                     |              1 | [UBERON:0035243](http://purl.obolibrary.org/obo/UBERON_0035243)                                                                  |
| `ncithesaurus:Posterior_External_Jugular_Vein`                |              1 | [UBERON:0035249](http://purl.obolibrary.org/obo/UBERON_0035249)                                                                  |
| `ncithesaurus:Left_Subcostal_Vein`                            |              1 | [UBERON:0035252](http://purl.obolibrary.org/obo/UBERON_0035252)                                                                  |
| `ncithesaurus:Gallbladder_Neck`                               |              1 | [UBERON:0035267](http://purl.obolibrary.org/obo/UBERON_0035267)                                                                  |
| `ncithesaurus:Epigastric_Region`                              |              1 | [UBERON:0035276](http://purl.obolibrary.org/obo/UBERON_0035276)                                                                  |
| `ncithesaurus:Supraclavicular_Lymph_Node`                     |              1 | [UBERON:0035279](http://purl.obolibrary.org/obo/UBERON_0035279)                                                                  |
| `ncithesaurus:Left_Ear`                                       |              1 | [UBERON:0035295](http://purl.obolibrary.org/obo/UBERON_0035295)                                                                  |
| `ncithesaurus:Inferolateral_Surface_of_the_Prostate`          |              1 | [UBERON:0035310](http://purl.obolibrary.org/obo/UBERON_0035310)                                                                  |
| `ncithesaurus:Capsule_of_the_Prostate`                        |              1 | [UBERON:0035316](http://purl.obolibrary.org/obo/UBERON_0035316)                                                                  |
| `ncithesaurus:Anterior_Median_Fissure_of_Spinal_Cord`         |              1 | [UBERON:0035319](http://purl.obolibrary.org/obo/UBERON_0035319)                                                                  |
| `ncithesaurus:Upper-outer_Quadrant_of_the_Breast`             |              1 | [UBERON:0035328](http://purl.obolibrary.org/obo/UBERON_0035328)                                                                  |
| `ncithesaurus:Base_of_the_Prostate`                           |              1 | [UBERON:0035331](http://purl.obolibrary.org/obo/UBERON_0035331)                                                                  |
| `ncithesaurus:Posterior_Lobe_of_the_Prostate`                 |              1 | [UBERON:0035341](http://purl.obolibrary.org/obo/UBERON_0035341)                                                                  |
| `ncithesaurus:Lower-outer_Quadrant_of_the_Breast`             |              1 | [UBERON:0035365](http://purl.obolibrary.org/obo/UBERON_0035365)                                                                  |
| `ncithesaurus:Anterior_Surface_of_the_Kidney`                 |              1 | [UBERON:0035368](http://purl.obolibrary.org/obo/UBERON_0035368)                                                                  |
| `ncithesaurus:Retroperitoneal_Lymph_Node`                     |              1 | [UBERON:0035371](http://purl.obolibrary.org/obo/UBERON_0035371)                                                                  |
| `ncithesaurus:Small_Cardiac_Vein`                             |              1 | [UBERON:0035374](http://purl.obolibrary.org/obo/UBERON_0035374)                                                                  |
| `ncithesaurus:Anterior_Cerebral_Artery_Branch`                |              1 | [UBERON:0035380](http://purl.obolibrary.org/obo/UBERON_0035380)                                                                  |
| `ncithesaurus:Cystic_Vein`                                    |              1 | [UBERON:0035392](http://purl.obolibrary.org/obo/UBERON_0035392)                                                                  |
| `ncithesaurus:Anterior_Longitudinal_Ligament`                 |              1 | [UBERON:0035419](http://purl.obolibrary.org/obo/UBERON_0035419)                                                                  |
| `ncithesaurus:Falx_Cerebelli`                                 |              1 | [UBERON:0035425](http://purl.obolibrary.org/obo/UBERON_0035425)                                                                  |
| `ncithesaurus:Mediastinal_Pleura`                             |              1 | [UBERON:0035431](http://purl.obolibrary.org/obo/UBERON_0035431)                                                                  |
| `ncithesaurus:Right_Suprarenal_Vein`                          |              1 | [UBERON:0035435](http://purl.obolibrary.org/obo/UBERON_0035435)                                                                  |
| `ncithesaurus:Apex_of_the_Prostate`                           |              1 | [UBERON:0035441](http://purl.obolibrary.org/obo/UBERON_0035441)                                                                  |
| `ncithesaurus:Cervical_Esophagus`                             |              1 | [UBERON:0035450](http://purl.obolibrary.org/obo/UBERON_0035450)                                                                  |
| `ncithesaurus:Anterior_Parietal_Artery`                       |              1 | [UBERON:0035462](http://purl.obolibrary.org/obo/UBERON_0035462)                                                                  |
| `ncithesaurus:Endometrial_Cavity`                             |              1 | [UBERON:0035465](http://purl.obolibrary.org/obo/UBERON_0035465)                                                                  |
| `ncithesaurus:Costophrenic_Angle`                             |              1 | [UBERON:0035468](http://purl.obolibrary.org/obo/UBERON_0035468)                                                                  |
| `ncithesaurus:Right_Subcostal_Vein`                           |              1 | [UBERON:0035474](http://purl.obolibrary.org/obo/UBERON_0035474)                                                                  |
| `ncithesaurus:Lower-inner_Quadrant_of_the_Breast`             |              1 | [UBERON:0035477](http://purl.obolibrary.org/obo/UBERON_0035477)                                                                  |
| `ncithesaurus:Surface_of_the_Prostate`                        |              1 | [UBERON:0035480](http://purl.obolibrary.org/obo/UBERON_0035480)                                                                  |
| `ncithesaurus:Left_Suprarenal_Vein`                           |              1 | [UBERON:0035483](http://purl.obolibrary.org/obo/UBERON_0035483)                                                                  |
| `ncithesaurus:Lymph_Node_Hilum`                               |              1 | [UBERON:0035495](http://purl.obolibrary.org/obo/UBERON_0035495)                                                                  |
| `ncithesaurus:Free_Nerve_Ending`                              |              1 | [UBERON:0035501](http://purl.obolibrary.org/obo/UBERON_0035501)                                                                  |
| `ncithesaurus:Anterior_Mediastinal_Lymph_Node`                |              1 | [UBERON:0035520](http://purl.obolibrary.org/obo/UBERON_0035520)                                                                  |
| `ncithesaurus:Anterior_Surface_of_the_Prostate`               |              1 | [UBERON:0035523](http://purl.obolibrary.org/obo/UBERON_0035523)                                                                  |
| `ncithesaurus:Superficial_Peroneal_Nerve`                     |              1 | [UBERON:0035526](http://purl.obolibrary.org/obo/UBERON_0035526)                                                                  |
| `ncithesaurus:Deep_Middle_Cerebral_Vein`                      |              1 | [UBERON:0035532](http://purl.obolibrary.org/obo/UBERON_0035532)                                                                  |
| `ncithesaurus:Gallbladder_Body`                               |              1 | [UBERON:0035536](http://purl.obolibrary.org/obo/UBERON_0035536)                                                                  |
| `ncithesaurus:Esophageal_Artery`                              |              1 | [UBERON:0035539](http://purl.obolibrary.org/obo/UBERON_0035539)                                                                  |
| `ncithesaurus:Upper-inner_Quadrant_of_the_Breast`             |              1 | [UBERON:0035542](http://purl.obolibrary.org/obo/UBERON_0035542)                                                                  |
| `ncithesaurus:Deep_Lymphatic_Vessel`                          |              1 | [UBERON:0035545](http://purl.obolibrary.org/obo/UBERON_0035545)                                                                  |
| `ncithesaurus:Superficial_Vein`                               |              1 | [UBERON:0035550](http://purl.obolibrary.org/obo/UBERON_0035550)                                                                  |
| `ncithesaurus:Deep_Vein`                                      |              1 | [UBERON:0035552](http://purl.obolibrary.org/obo/UBERON_0035552)                                                                  |
| `ncithesaurus:Anterior_Facial_Vein`                           |              1 | [UBERON:0035675](http://purl.obolibrary.org/obo/UBERON_0035675)                                                                  |
| `ncithesaurus:Subsegmental_Lymph_Node`                        |              1 | [UBERON:0035765](http://purl.obolibrary.org/obo/UBERON_0035765)                                                                  |
| `ncithesaurus:Middle_Lobe_of_the_Prostate`                    |              1 | [UBERON:0035766](http://purl.obolibrary.org/obo/UBERON_0035766)                                                                  |
| `ncithesaurus:Splenic_Pulp`                                   |              1 | [UBERON:1000023](http://purl.obolibrary.org/obo/UBERON_1000023)                                                                  |
| `ncithesaurus:Muscularis_Propria`                             |              1 | [UBERON:0000381](http://purl.obolibrary.org/obo/UBERON_0000381)                                                                  |
| `ncithesaurus:Germinal_Layer`                                 |              1 | [UBERON:0000923](http://purl.obolibrary.org/obo/UBERON_0000923)                                                                  |
| `ncithesaurus:Pons_Varolii`                                   |              1 | [UBERON:0000988](http://purl.obolibrary.org/obo/UBERON_0000988)                                                                  |
| `ncithesaurus:Cortical_Column`                                |              1 | [UBERON:0001284](http://purl.obolibrary.org/obo/UBERON_0001284)                                                                  |
| `ncithesaurus:Epencephalon`                                   |              1 | [UBERON:0001895](http://purl.obolibrary.org/obo/UBERON_0001895)                                                                  |
| `ncithesaurus:Internal_Geniculate_Body`                       |              1 | [UBERON:0001927](http://purl.obolibrary.org/obo/UBERON_0001927)                                                                  |
| `ncithesaurus:Primordium_of_the_Liver`                        |              1 | [UBERON:0003894](http://purl.obolibrary.org/obo/UBERON_0003894)                                                                  |
| `ncithesaurus:Pyramid_of_Malpighi`                            |              1 | [UBERON:0004200](http://purl.obolibrary.org/obo/UBERON_0004200)                                                                  |
| `ncithesaurus:Pancreatic_Endocrine_Secretion`                 |              1 | [UBERON:0004792](http://purl.obolibrary.org/obo/UBERON_0004792)                                                                  |
| `ncithesaurus:Pancreatic_Exocrine_Secretion`                  |              1 | [UBERON:0004793](http://purl.obolibrary.org/obo/UBERON_0004793)                                                                  |
| `ncithesaurus:Molecular_layer`                                |              1 | [UBERON:0005390](http://purl.obolibrary.org/obo/UBERON_0005390)                                                                  |
| `ncithesaurus:External_Pyramidal_Cell_Layer`                  |              1 | [UBERON:0005392](http://purl.obolibrary.org/obo/UBERON_0005392)                                                                  |
| `ncithesaurus:Superior_Constrictor_Muscle`                    |              1 | [UBERON:0006329](http://purl.obolibrary.org/obo/UBERON_0006329)                                                                  |
| `ncithesaurus:Lobe_of_the_Right_Lung`                         |              1 | [UBERON:0006518](http://purl.obolibrary.org/obo/UBERON_0006518)                                                                  |
| `ncithesaurus:Tunica_Albuginea`                               |              1 | [UBERON:0006643](http://purl.obolibrary.org/obo/UBERON_0006643)                                                                  |
| `ncithesaurus:Posterior`                                      |              1 | [UBERON:0008788](http://purl.obolibrary.org/obo/UBERON_0008788)                                                                  |
| `ncithesaurus:Paraganglion`                                   |              1 | [UBERON:0012279](http://purl.obolibrary.org/obo/UBERON_0012279)                                                                  |
| `ncithesaurus:Gland_of_Wolfring`                              |              1 | [UBERON:0013224](http://purl.obolibrary.org/obo/UBERON_0013224)                                                                  |
| `ncithesaurus:Collum_Dentis`                                  |              1 | [UBERON:0015181](http://purl.obolibrary.org/obo/UBERON_0015181)                                                                  |
| `ncithesaurus:Ileocecocolic_Lymph_Node`                       |              1 | [UBERON:0016378](http://purl.obolibrary.org/obo/UBERON_0016378)                                                                  |
| `ncithesaurus:Adrenal_Gland_Tissue`                           |              1 | [UBERON:0018303](http://purl.obolibrary.org/obo/UBERON_0018303)                                                                  |
| `ncithesaurus:Life`                                           |              1 | [UBERON:0000104](http://purl.obolibrary.org/obo/UBERON_0000104)                                                                  |
| `ncithesaurus:Developmental_Stage`                            |              1 | [UBERON:0000105](http://purl.obolibrary.org/obo/UBERON_0000105)                                                                  |
| `ncithesaurus:Pleural_Effusion`                               |              1 | [UBERON:0000175](http://purl.obolibrary.org/obo/UBERON_0000175)                                                                  |
| `ncithesaurus:Pus`                                            |              1 | [UBERON:0000177](http://purl.obolibrary.org/obo/UBERON_0000177)                                                                  |
| `ncithesaurus:Atlanto-occipital_Joint-Atlanto`                |              1 | [UBERON:0000220](http://purl.obolibrary.org/obo/UBERON_0000220)                                                                  |
| `ncithesaurus:Myelin`                                         |              1 | [UBERON:0000345](http://purl.obolibrary.org/obo/UBERON_0000345)                                                                  |
| `ncithesaurus:Whole_Organism`                                 |              1 | [UBERON:0000468](http://purl.obolibrary.org/obo/UBERON_0000468)                                                                  |
| `ncithesaurus:Digestive_System`                               |              1 | [UBERON:0001007](http://purl.obolibrary.org/obo/UBERON_0001007)                                                                  |
| `ncithesaurus:Pleural_Fluid`                                  |              1 | [UBERON:0001087](http://purl.obolibrary.org/obo/UBERON_0001087)                                                                  |
| `ncithesaurus:Heart_Muscle`                                   |              1 | [UBERON:0001133](http://purl.obolibrary.org/obo/UBERON_0001133)                                                                  |
| `ncithesaurus:Peritoneal_Fluid`                               |              1 | [UBERON:0001268](http://purl.obolibrary.org/obo/UBERON_0001268)                                                                  |
| `ncithesaurus:Phalanx_of_the_Foot`                            |              1 | [UBERON:0001449](http://purl.obolibrary.org/obo/UBERON_0001449)                                                                  |
| `ncithesaurus:Transverse_Sinus`                               |              1 | [UBERON:0001641](http://purl.obolibrary.org/obo/UBERON_0001641)                                                                  |
| `ncithesaurus:Upper_Jaw`                                      |              1 | [UBERON:0001709](http://purl.obolibrary.org/obo/UBERON_0001709)                                                                  |
| `ncithesaurus:Lower_Jaw`                                      |              1 | [UBERON:0001710](http://purl.obolibrary.org/obo/UBERON_0001710)                                                                  |
| `ncithesaurus:Insula`                                         |              1 | [UBERON:0002022](http://purl.obolibrary.org/obo/UBERON_0002022)                                                                  |
| `ncithesaurus:Spiral_Organ_of_Corti`                          |              1 | [UBERON:0002227](http://purl.obolibrary.org/obo/UBERON_0002227)                                                                  |
| `ncithesaurus:Cerebral_Aqueduct`                              |              1 | [UBERON:0002289](http://purl.obolibrary.org/obo/UBERON_0002289)                                                                  |
| `ncithesaurus:Striatum`                                       |              1 | [UBERON:0002435](http://purl.obolibrary.org/obo/UBERON_0002435)                                                                  |
| `ncithesaurus:Parieto-occipital_Sulcus`                       |              1 | [UBERON:0002695](http://purl.obolibrary.org/obo/UBERON_0002695)                                                                  |
| `ncithesaurus:Middle_Frontal_Gyrus`                           |              1 | [UBERON:0002702](http://purl.obolibrary.org/obo/UBERON_0002702)                                                                  |
| `ncithesaurus:Collateral_Sulcus`                              |              1 | [UBERON:0002716](http://purl.obolibrary.org/obo/UBERON_0002716)                                                                  |
| `ncithesaurus:Inferior_Temporal_Gyrus`                        |              1 | [UBERON:0002751](http://purl.obolibrary.org/obo/UBERON_0002751)                                                                  |
| `ncithesaurus:Superior_Temporal_Gyrus`                        |              1 | [UBERON:0002769](http://purl.obolibrary.org/obo/UBERON_0002769)                                                                  |
| `ncithesaurus:Middle_Temporal_Gyrus`                          |              1 | [UBERON:0002771](http://purl.obolibrary.org/obo/UBERON_0002771)                                                                  |
| `ncithesaurus:Nucleus_of_the_Hypoglossal_Nerve`               |              1 | [UBERON:0002871](http://purl.obolibrary.org/obo/UBERON_0002871)                                                                  |
| `ncithesaurus:Inferior_Frontal_Gyrus`                         |              1 | [UBERON:0002998](http://purl.obolibrary.org/obo/UBERON_0002998)                                                                  |
| `ncithesaurus:Meckel_Diverticulum`                            |              1 | [UBERON:0003705](http://purl.obolibrary.org/obo/UBERON_0003705)                                                                  |
| `ncithesaurus:Dorsal_Thalamus`                                |              1 | [UBERON:0004703](http://purl.obolibrary.org/obo/UBERON_0004703)                                                                  |
| `ncithesaurus:Sigmoid_Sinus`                                  |              1 | [UBERON:0005475](http://purl.obolibrary.org/obo/UBERON_0005475)                                                                  |
| `ncithesaurus:Straight_Sinus`                                 |              1 | [UBERON:0005481](http://purl.obolibrary.org/obo/UBERON_0005481)                                                                  |
| `ncithesaurus:Adrenal_Artery`                                 |              1 | [UBERON:0005624](http://purl.obolibrary.org/obo/UBERON_0005624)                                                                  |
| `ncithesaurus:Meconium`                                       |              1 | [UBERON:0007109](http://purl.obolibrary.org/obo/UBERON_0007109)                                                                  |
| `ncithesaurus:Vesicular_Gland`                                |              1 | [UBERON:0007194](http://purl.obolibrary.org/obo/UBERON_0007194)                                                                  |
| `ncithesaurus:Egg_Yolk`                                       |              1 | [UBERON:0007378](http://purl.obolibrary.org/obo/UBERON_0007378)                                                                  |
| `ncithesaurus:Transudate`                                     |              1 | [UBERON:0007779](http://purl.obolibrary.org/obo/UBERON_0007779)                                                                  |
| `ncithesaurus:Exudate`                                        |              1 | [UBERON:0007780](http://purl.obolibrary.org/obo/UBERON_0007780)                                                                  |
| `ncithesaurus:Egg_White`                                      |              1 | [UBERON:0008944](http://purl.obolibrary.org/obo/UBERON_0008944)                                                                  |
| `ncithesaurus:Nucleus_of_the_Solitary_Tract`                  |              1 | [UBERON:0009050](http://purl.obolibrary.org/obo/UBERON_0009050)                                                                  |
| `ncithesaurus:Gravid_Uterus`                                  |              1 | [UBERON:0009098](http://purl.obolibrary.org/obo/UBERON_0009098)                                                                  |

## `neuronames`: NeuroNames

Overall, there were 3 invalid
xrefs to external prefixed with `neuronames` (standardized to Bioregistry
prefix [`neuronames`](https://bioregistry.io/neuronames)) that
did not match the standard pattern `^\d+$`.

| external_xref                  |   usages_count | usages                                                          |
|--------------------------------|----------------|-----------------------------------------------------------------|
| `neuronames:1192&questID=2709` |              1 | [UBERON:8440024](http://purl.obolibrary.org/obo/UBERON_8440024) |
| `neuronames:3451&questID=1771` |              1 | [UBERON:8440026](http://purl.obolibrary.org/obo/UBERON_8440026) |
| `neuronames:3452&questID=1771` |              1 | [UBERON:8440027](http://purl.obolibrary.org/obo/UBERON_8440027) |

## `NIF_Subcellular`: NIF Standard Ontology: Subcellular Entities

Overall, there were 12 invalid
xrefs to external prefixed with `NIF_Subcellular` (standardized to Bioregistry
prefix [`nlx.sub`](https://bioregistry.io/nlx.sub)) that
did not match the standard pattern `^\d+$`.

| external_xref                          |   usages_count | usages                                                                                                                           |
|----------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------|
| `NIF_Subcellular:nlx_subcell_20090504` |              2 | [UBERON:0011917](http://purl.obolibrary.org/obo/UBERON_0011917), [UBERON:0011917](http://purl.obolibrary.org/obo/UBERON_0011917) |
| `NIF_Subcellular:nlx_subcell_100205`   |              1 | [UBERON:0000201](http://purl.obolibrary.org/obo/UBERON_0000201)                                                                  |
| `NIF_Subcellular:sao1397492660`        |              1 | [UBERON:0000482](http://purl.obolibrary.org/obo/UBERON_0000482)                                                                  |
| `NIF_Subcellular:sao1145756102`        |              1 | [UBERON:0001130](http://purl.obolibrary.org/obo/UBERON_0001130)                                                                  |
| `NIF_Subcellular:sao205380252`         |              1 | [UBERON:0002606](http://purl.obolibrary.org/obo/UBERON_0002606)                                                                  |
| `NIF_Subcellular:FMA_83604`            |              1 | [UBERON:0003719](http://purl.obolibrary.org/obo/UBERON_0003719)                                                                  |
| `NIF_Subcellular:nlx_subcell_20090503` |              1 | [UBERON:0005387](http://purl.obolibrary.org/obo/UBERON_0005387)                                                                  |
| `NIF_Subcellular:sao7547390221`        |              1 | [UBERON:0011860](http://purl.obolibrary.org/obo/UBERON_0011860)                                                                  |
| `NIF_Subcellular:nlx_subcell_20090502` |              1 | [UBERON:0011915](http://purl.obolibrary.org/obo/UBERON_0011915)                                                                  |
| `NIF_Subcellular:FMA_83606`            |              1 | [UBERON:0012456](http://purl.obolibrary.org/obo/UBERON_0012456)                                                                  |
| `NIF_Subcellular:nlx_subcell_100209`   |              1 | [UBERON:0018687](http://purl.obolibrary.org/obo/UBERON_0018687)                                                                  |

## `NIFSTD`: NIF Standard Ontology

Overall, there were 337 invalid
xrefs to external prefixed with `NIFSTD` (standardized to Bioregistry
prefix [`nif.std`](https://bioregistry.io/nif.std)) that
did not match the standard pattern `^BAMSC\d+$`.

| external_xref                                     |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `NIFSTD:NeuroNames_abbrevSource`                  |            265 | [UBERON:0000007](http://purl.obolibrary.org/obo/UBERON_0000007), [UBERON:0000435](http://purl.obolibrary.org/obo/UBERON_0000435), [UBERON:0000941](http://purl.obolibrary.org/obo/UBERON_0000941), [UBERON:0001579](http://purl.obolibrary.org/obo/UBERON_0001579), [UBERON:0001643](http://purl.obolibrary.org/obo/UBERON_0001643), ... |
| `NIFSTD:SumsDB_abbrevSource`                      |             52 | [UBERON:0004717](http://purl.obolibrary.org/obo/UBERON_0004717), [UBERON:0004718](http://purl.obolibrary.org/obo/UBERON_0004718), [UBERON:0006095](http://purl.obolibrary.org/obo/UBERON_0006095), [UBERON:0006096](http://purl.obolibrary.org/obo/UBERON_0006096), [UBERON:0006099](http://purl.obolibrary.org/obo/UBERON_0006099), ... |
| `NIFSTD:Swanson-rat-1998_abbrevSource`            |             13 | [UBERON:0014589](http://purl.obolibrary.org/obo/UBERON_0014589), [UBERON:0014590](http://purl.obolibrary.org/obo/UBERON_0014590), [UBERON:0014591](http://purl.obolibrary.org/obo/UBERON_0014591), [UBERON:0014592](http://purl.obolibrary.org/obo/UBERON_0014592), [UBERON:0014593](http://purl.obolibrary.org/obo/UBERON_0014593), ... |
| `NIFSTD:Swanson-rat-1992_abbrevSource`            |              3 | [UBERON:0014602](http://purl.obolibrary.org/obo/UBERON_0014602), [UBERON:0014603](http://purl.obolibrary.org/obo/UBERON_0014603), [UBERON:0014604](http://purl.obolibrary.org/obo/UBERON_0014604)                                                                                                                                        |
| `NIFSTD:oen_0001107`                              |              2 | [UBERON:0035015](http://purl.obolibrary.org/obo/UBERON_0035015), [UBERON:0035015](http://purl.obolibrary.org/obo/UBERON_0035015)                                                                                                                                                                                                         |
| `NIFSTD:FMAID_7191`                               |              1 | [UBERON:0002104](http://purl.obolibrary.org/obo/UBERON_0002104)                                                                                                                                                                                                                                                                          |
| `NIFSTD:Paxinos-Franklin-mouse-2001_abbrevSource` |              1 | [UBERON:0002701](http://purl.obolibrary.org/obo/UBERON_0002701)                                                                                                                                                                                                                                                                          |

## `NLM`: National Library of Medicine Catalog

Overall, there were 4 invalid
xrefs to external prefixed with `NLM` (standardized to Bioregistry
prefix [`nlm`](https://bioregistry.io/nlm)) that
did not match the standard pattern `^\d+$`.

| external_xref           |   usages_count | usages                                                          |
|-------------------------|----------------|-----------------------------------------------------------------|
| `NLM:endocrine+system`  |              1 | [UBERON:0000949](http://purl.obolibrary.org/obo/UBERON_0000949) |
| `NLM:alimentary+system` |              1 | [UBERON:0001007](http://purl.obolibrary.org/obo/UBERON_0001007) |
| `NLM:nervous+system`    |              1 | [UBERON:0001016](http://purl.obolibrary.org/obo/UBERON_0001016) |
| `NLM:thymus`            |              1 | [UBERON:0002370](http://purl.obolibrary.org/obo/UBERON_0002370) |

## `OBI`: Ontology for Biomedical Investigations

Overall, there were 1 invalid
xrefs to external prefixed with `OBI` (standardized to Bioregistry
prefix [`obi`](https://bioregistry.io/obi)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `OBI:MC`        |              1 | [UBERON:0012125](http://purl.obolibrary.org/obo/UBERON_0012125) |

## `PBA`: Primate Brain Atlas

Overall, there were 1 invalid
xrefs to external prefixed with `PBA` (standardized to Bioregistry
prefix [`pba`](https://bioregistry.io/pba)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `PBA:BN`        |              1 | [UBERON:0010011](http://purl.obolibrary.org/obo/UBERON_0010011) |

## `TAO`: Teleost Anatomy Ontology

Overall, there were 603 invalid
xrefs to external prefixed with `TAO` (standardized to Bioregistry
prefix [`tao`](https://bioregistry.io/tao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                              |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TAO:wd`                                   |            481 | [UBERON:0002534](http://purl.obolibrary.org/obo/UBERON_0002534), [UBERON:0002543](http://purl.obolibrary.org/obo/UBERON_0002543), [UBERON:0004740](http://purl.obolibrary.org/obo/UBERON_0004740), [UBERON:0006606](http://purl.obolibrary.org/obo/UBERON_0006606), [UBERON:0008917](http://purl.obolibrary.org/obo/UBERON_0008917), ... |
| `TAO:GA_TG`                                |             66 | [UBERON:0004865](http://purl.obolibrary.org/obo/UBERON_0004865), [UBERON:2000104](http://purl.obolibrary.org/obo/UBERON_2000104), [UBERON:2000127](http://purl.obolibrary.org/obo/UBERON_2000127), [UBERON:2000250](http://purl.obolibrary.org/obo/UBERON_2000250), [UBERON:2000364](http://purl.obolibrary.org/obo/UBERON_2000364), ... |
| `TAO:curator`                              |             27 | [UBERON:0000151](http://purl.obolibrary.org/obo/UBERON_0000151), [UBERON:0000152](http://purl.obolibrary.org/obo/UBERON_0000152), [UBERON:0003097](http://purl.obolibrary.org/obo/UBERON_0003097), [UBERON:0005744](http://purl.obolibrary.org/obo/UBERON_0005744), [UBERON:0007380](http://purl.obolibrary.org/obo/UBERON_0007380), ... |
| `TAO:pem`                                  |              7 | [UBERON:2001675](http://purl.obolibrary.org/obo/UBERON_2001675), [UBERON:2001676](http://purl.obolibrary.org/obo/UBERON_2001676), [UBERON:2001677](http://purl.obolibrary.org/obo/UBERON_2001677), [UBERON:2001678](http://purl.obolibrary.org/obo/UBERON_2001678), [UBERON:2001680](http://purl.obolibrary.org/obo/UBERON_2001680), ... |
| `TAO:Arratia_2008`                         |              4 | [UBERON:2001584](http://purl.obolibrary.org/obo/UBERON_2001584), [UBERON:2001829](http://purl.obolibrary.org/obo/UBERON_2001829), [UBERON:2001830](http://purl.obolibrary.org/obo/UBERON_2001830), [UBERON:2002165](http://purl.obolibrary.org/obo/UBERON_2002165)                                                                       |
| `TAO:ga_tg`                                |              3 | [UBERON:2000103](http://purl.obolibrary.org/obo/UBERON_2000103), [UBERON:2002020](http://purl.obolibrary.org/obo/UBERON_2002020), [UBERON:2002089](http://purl.obolibrary.org/obo/UBERON_2002089)                                                                                                                                        |
| `TAO:doi:10.1046/j.1096-3642.2002.00014.x` |              2 | [UBERON:2001191](http://purl.obolibrary.org/obo/UBERON_2001191), [UBERON:2001192](http://purl.obolibrary.org/obo/UBERON_2001192)                                                                                                                                                                                                         |
| `TAO:MAH`                                  |              1 | [UBERON:0001703](http://purl.obolibrary.org/obo/UBERON_0001703)                                                                                                                                                                                                                                                                          |
| `TAO:Arratia_Schultze_1992`                |              1 | [UBERON:2000602](http://purl.obolibrary.org/obo/UBERON_2000602)                                                                                                                                                                                                                                                                          |
| `TAO:Patterson_1968`                       |              1 | [UBERON:2000602](http://purl.obolibrary.org/obo/UBERON_2000602)                                                                                                                                                                                                                                                                          |
| `TAO:je`                                   |              1 | [UBERON:2001275](http://purl.obolibrary.org/obo/UBERON_2001275)                                                                                                                                                                                                                                                                          |
| `TAO:w`                                    |              1 | [UBERON:2001957](http://purl.obolibrary.org/obo/UBERON_2001957)                                                                                                                                                                                                                                                                          |
| `TAO:Bridge_1877`                          |              1 | [UBERON:2000127](http://purl.obolibrary.org/obo/UBERON_2000127)                                                                                                                                                                                                                                                                          |
| `TAO:Goodrich_1930`                        |              1 | [UBERON:2000127](http://purl.obolibrary.org/obo/UBERON_2000127)                                                                                                                                                                                                                                                                          |
| `TAO:Jollie_1984`                          |              1 | [UBERON:2000127](http://purl.obolibrary.org/obo/UBERON_2000127)                                                                                                                                                                                                                                                                          |
| `TAO:Regan_1923`                           |              1 | [UBERON:2000127](http://purl.obolibrary.org/obo/UBERON_2000127)                                                                                                                                                                                                                                                                          |
| `TAO:Arratia_Schultze_1990`                |              1 | [UBERON:2000452](http://purl.obolibrary.org/obo/UBERON_2000452)                                                                                                                                                                                                                                                                          |
| `TAO:Harrington_1955`                      |              1 | [UBERON:2000663](http://purl.obolibrary.org/obo/UBERON_2000663)                                                                                                                                                                                                                                                                          |
| `TAO:Weitzman_1962`                        |              1 | [UBERON:2000663](http://purl.obolibrary.org/obo/UBERON_2000663)                                                                                                                                                                                                                                                                          |
| `TAO:Bird_2003`                            |              1 | [UBERON:2001553](http://purl.obolibrary.org/obo/UBERON_2001553)                                                                                                                                                                                                                                                                          |

## `UBERON`: Uber Anatomy Ontology

Overall, there were 213 invalid
xrefs to external prefixed with `UBERON` (standardized to Bioregistry
prefix [`uberon`](https://bioregistry.io/uberon)) that
did not match the standard pattern `^\d+$`.

| external_xref      |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|--------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UBERON:cjm`       |            173 | [UBERON:0000004](http://purl.obolibrary.org/obo/UBERON_0000004), [UBERON:0000004](http://purl.obolibrary.org/obo/UBERON_0000004), [UBERON:0000012](http://purl.obolibrary.org/obo/UBERON_0000012), [UBERON:0000172](http://purl.obolibrary.org/obo/UBERON_0000172), [UBERON:0000977](http://purl.obolibrary.org/obo/UBERON_0000977), ... |
| `UBERON:EJS`       |             19 | [UBERON:1000000](http://purl.obolibrary.org/obo/UBERON_1000000), [UBERON:1000001](http://purl.obolibrary.org/obo/UBERON_1000001), [UBERON:1000002](http://purl.obolibrary.org/obo/UBERON_1000002), [UBERON:1000004](http://purl.obolibrary.org/obo/UBERON_1000004), [UBERON:1000005](http://purl.obolibrary.org/obo/UBERON_1000005), ... |
| `UBERON:mah`       |              4 | [UBERON:0001427](http://purl.obolibrary.org/obo/UBERON_0001427), [UBERON:0001428](http://purl.obolibrary.org/obo/UBERON_0001428), [UBERON:0015001](http://purl.obolibrary.org/obo/UBERON_0015001), [UBERON:0015003](http://purl.obolibrary.org/obo/UBERON_0015003)                                                                       |
| `UBERON:skansa`    |              4 | [UBERON:0012288](http://purl.obolibrary.org/obo/UBERON_0012288), [UBERON:0012289](http://purl.obolibrary.org/obo/UBERON_0012289), [UBERON:0012290](http://purl.obolibrary.org/obo/UBERON_0012290), [UBERON:0013649](http://purl.obolibrary.org/obo/UBERON_0013649)                                                                       |
| `UBERON:xp`        |              3 | [UBERON:0003133](http://purl.obolibrary.org/obo/UBERON_0003133), [UBERON:0003134](http://purl.obolibrary.org/obo/UBERON_0003134), [UBERON:0003135](http://purl.obolibrary.org/obo/UBERON_0003135)                                                                                                                                        |
| `UBERON:automatic` |              2 | [UBERON:0004766](http://purl.obolibrary.org/obo/UBERON_0004766), [UBERON:0004766](http://purl.obolibrary.org/obo/UBERON_0004766)                                                                                                                                                                                                         |
| `UBERON:gg`        |              2 | [UBERON:0005982](http://purl.obolibrary.org/obo/UBERON_0005982), [UBERON:0006060](http://purl.obolibrary.org/obo/UBERON_0006060)                                                                                                                                                                                                         |
| `UBERON:md`        |              2 | [UBERON:0013739](http://purl.obolibrary.org/obo/UBERON_0013739), [UBERON:0013740](http://purl.obolibrary.org/obo/UBERON_0013740)                                                                                                                                                                                                         |
| `UBERON:gvg`       |              1 | [UBERON:0005273](http://purl.obolibrary.org/obo/UBERON_0005273)                                                                                                                                                                                                                                                                          |
| `UBERON:nv`        |              1 | [UBERON:0016928](http://purl.obolibrary.org/obo/UBERON_0016928)                                                                                                                                                                                                                                                                          |
| `UBERON:drseb`     |              1 | [UBERON:0019207](http://purl.obolibrary.org/obo/UBERON_0019207)                                                                                                                                                                                                                                                                          |
| `UBERON:rc`        |              1 | [UBERON:0036015](http://purl.obolibrary.org/obo/UBERON_0036015)                                                                                                                                                                                                                                                                          |

## `VHOG`: Vertebrate Homologous Organ Group Ontology

Overall, there were 5 invalid
xrefs to external prefixed with `VHOG` (standardized to Bioregistry
prefix [`vhog`](https://bioregistry.io/vhog)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `VHOG:OG`       |              4 | [UBERON:0005872](http://purl.obolibrary.org/obo/UBERON_0005872), [UBERON:0005873](http://purl.obolibrary.org/obo/UBERON_0005873), [UBERON:0005874](http://purl.obolibrary.org/obo/UBERON_0005874), [UBERON:0005875](http://purl.obolibrary.org/obo/UBERON_0005875) |
| `VHOG:FB`       |              1 | [UBERON:0000112](http://purl.obolibrary.org/obo/UBERON_0000112)                                                                                                                                                                                                    |

## `WB`: Wormbase Gene

Overall, there were 3 invalid
xrefs to external prefixed with `WB` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref      |   usages_count | usages                                                          |
|--------------------|----------------|-----------------------------------------------------------------|
| `WB:Paper00000938` |              1 | [UBERON:0000934](http://purl.obolibrary.org/obo/UBERON_0000934) |
| `WB:Paper00000653` |              1 | [UBERON:0000954](http://purl.obolibrary.org/obo/UBERON_0000954) |
| `WB:rynl`          |              1 | [UBERON:0001016](http://purl.obolibrary.org/obo/UBERON_0001016) |

## `XAO`: Xenopus Anatomy Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `XAO` (standardized to Bioregistry
prefix [`xao`](https://bioregistry.io/xao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `XAO:EJS`       |              4 | [UBERON:0015179](http://purl.obolibrary.org/obo/UBERON_0015179), [UBERON:3010297](http://purl.obolibrary.org/obo/UBERON_3010297), [UBERON:3010299](http://purl.obolibrary.org/obo/UBERON_3010299), [UBERON:4000013](http://purl.obolibrary.org/obo/UBERON_4000013) |
| `XAO:curator`   |              2 | [UBERON:3010326](http://purl.obolibrary.org/obo/UBERON_3010326), [UBERON:3010404](http://purl.obolibrary.org/obo/UBERON_3010404)                                                                                                                                   |
| `XAO:curators`  |              1 | [UBERON:0009500](http://purl.obolibrary.org/obo/UBERON_0009500)                                                                                                                                                                                                    |

## `ZFA`: Zebrafish anatomy and development ontology

Overall, there were 14 invalid
xrefs to external prefixed with `ZFA` (standardized to Bioregistry
prefix [`zfa`](https://bioregistry.io/zfa)) that
did not match the standard pattern `^\d{7}$`.

| external_xref           |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFA:curator`           |              9 | [UBERON:0008229](http://purl.obolibrary.org/obo/UBERON_0008229), [UBERON:0014371](http://purl.obolibrary.org/obo/UBERON_0014371), [UBERON:0014903](http://purl.obolibrary.org/obo/UBERON_0014903), [UBERON:0018549](http://purl.obolibrary.org/obo/UBERON_0018549), [UBERON:2000120](http://purl.obolibrary.org/obo/UBERON_2000120), ... |
| `ZFA:CVS`               |              2 | [UBERON:0016499](http://purl.obolibrary.org/obo/UBERON_0016499), [UBERON:0018674](http://purl.obolibrary.org/obo/UBERON_0018674)                                                                                                                                                                                                         |
| `ZFA:yb`                |              1 | [UBERON:0002539](http://purl.obolibrary.org/obo/UBERON_0002539)                                                                                                                                                                                                                                                                          |
| `ZFA:YMB`               |              1 | [UBERON:0016499](http://purl.obolibrary.org/obo/UBERON_0016499)                                                                                                                                                                                                                                                                          |
| `ZFA:ZDB-PUB-060323-12` |              1 | [UBERON:2005245](http://purl.obolibrary.org/obo/UBERON_2005245)                                                                                                                                                                                                                                                                          |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 520 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref    |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:curator`   |            515 | [UBERON:0000007](http://purl.obolibrary.org/obo/UBERON_0000007), [UBERON:0000966](http://purl.obolibrary.org/obo/UBERON_0000966), [UBERON:0000991](http://purl.obolibrary.org/obo/UBERON_0000991), [UBERON:0001016](http://purl.obolibrary.org/obo/UBERON_0001016), [UBERON:0001081](http://purl.obolibrary.org/obo/UBERON_0001081), ... |
| `ZFIN:Curator`   |              2 | [UBERON:0005817](http://purl.obolibrary.org/obo/UBERON_0005817), [UBERON:2005210](http://purl.obolibrary.org/obo/UBERON_2005210)                                                                                                                                                                                                         |
| `ZFIN:yb`        |              1 | [UBERON:0003066](http://purl.obolibrary.org/obo/UBERON_0003066)                                                                                                                                                                                                                                                                          |
| `ZFIN:090511-18` |              1 | [UBERON:2002145](http://purl.obolibrary.org/obo/UBERON_2002145)                                                                                                                                                                                                                                                                          |
| `ZFIN:CVS`       |              1 | [UBERON:2005265](http://purl.obolibrary.org/obo/UBERON_2005265)                                                                                                                                                                                                                                                                          |

## `zfin`: Zebrafish Information Network Gene

Overall, there were 1 invalid
xrefs to external prefixed with `zfin` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `zfin:curator`  |              1 | [UBERON:0008911](http://purl.obolibrary.org/obo/UBERON_0008911) |

