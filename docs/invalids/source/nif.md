# nif

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `nif`.


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

## `AGR`: Agricultural Online Access

Overall, there were 15 invalid
xrefs to external prefixed with `AGR` (standardized to Bioregistry
prefix [`agricola`](https://bioregistry.io/agricola)) that
did not match the standard pattern `^\d+$`.

| external_xref      |   usages_count | usages                                                      |
|--------------------|----------------|-------------------------------------------------------------|
| `AGR:IND84086009`  |              1 | [CHEBI:136643](http://purl.obolibrary.org/obo/CHEBI_136643) |
| `AGR:IND20386178`  |              1 | [CHEBI:136644](http://purl.obolibrary.org/obo/CHEBI_136644) |
| `AGR:IND84086011`  |              1 | [CHEBI:136644](http://purl.obolibrary.org/obo/CHEBI_136644) |
| `AGR:IND89021681`  |              1 | [CHEBI:136644](http://purl.obolibrary.org/obo/CHEBI_136644) |
| `AGR:IND92003154`  |              1 | [CHEBI:136644](http://purl.obolibrary.org/obo/CHEBI_136644) |
| `AGR:IND81078502`  |              1 | [CHEBI:15955](http://purl.obolibrary.org/obo/CHEBI_15955)   |
| `AGR:IND605478333` |              1 | [CHEBI:16522](http://purl.obolibrary.org/obo/CHEBI_16522)   |
| `AGR:IND607198670` |              1 | [CHEBI:16709](http://purl.obolibrary.org/obo/CHEBI_16709)   |
| `AGR:IND93002823`  |              1 | [CHEBI:195233](http://purl.obolibrary.org/obo/CHEBI_195233) |
| `AGR:IND606960789` |              1 | [CHEBI:27470](http://purl.obolibrary.org/obo/CHEBI_27470)   |
| `AGR:IND605848433` |              1 | [CHEBI:28934](http://purl.obolibrary.org/obo/CHEBI_28934)   |
| `AGR:IND607339542` |              1 | [CHEBI:3312](http://purl.obolibrary.org/obo/CHEBI_3312)     |
| `AGR:IND43941110`  |              1 | [CHEBI:62546](http://purl.obolibrary.org/obo/CHEBI_62546)   |
| `AGR:IND44688035`  |              1 | [CHEBI:87230](http://purl.obolibrary.org/obo/CHEBI_87230)   |
| `AGR:IND607175662` |              1 | [CHEBI:9506](http://purl.obolibrary.org/obo/CHEBI_9506)     |

## `BioRXiv`: bioRxiv

Overall, there were 1 invalid
xrefs to external prefixed with `BioRXiv` (standardized to Bioregistry
prefix [`biorxiv`](https://bioregistry.io/biorxiv)) that
did not match the standard pattern `^(\d{4}\.\d{2}\.\d{2}\.)?\d{6,8}(v\d{1,3})?$`.

| external_xref                            |   usages_count | usages                                                  |
|------------------------------------------|----------------|---------------------------------------------------------|
| `BioRXiv:https://doi.org/10.1101/584664` |              1 | [SO:0002223](http://purl.obolibrary.org/obo/SO_0002223) |

## `BIRNLEX`: Biomedical Informatics Research Network Lexicon

Overall, there were 2 invalid
xrefs to external prefixed with `BIRNLEX` (standardized to Bioregistry
prefix [`birnlex`](https://bioregistry.io/birnlex)) that
did not match the standard pattern `^\d+$`.

| external_xref           |   usages_count | usages                                                          |
|-------------------------|----------------|-----------------------------------------------------------------|
| `BIRNLEX:Limbic_system` |              1 | [UBERON:0000349](http://purl.obolibrary.org/obo/UBERON_0000349) |
| `BIRNLEX:4106_2`        |              1 | [UBERON:0000396](http://purl.obolibrary.org/obo/UBERON_0000396) |

## `BSPO`: Biological Spatial Ontology

Overall, there were 25 invalid
xrefs to external prefixed with `BSPO` (standardized to Bioregistry
prefix [`bspo`](https://bioregistry.io/bspo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|----------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BSPO:cjm`           |             15 | [BSPO:0000096](http://purl.obolibrary.org/obo/BSPO_0000096), [BSPO:0000097](http://purl.obolibrary.org/obo/BSPO_0000097), [BSPO:0000098](http://purl.obolibrary.org/obo/BSPO_0000098), [BSPO:0000099](http://purl.obolibrary.org/obo/BSPO_0000099), [BSPO:0000100](http://purl.obolibrary.org/obo/BSPO_0000100), ... |
| `BSPO:PATO_mtg_2009` |              6 | [BSPO:0000120](http://purl.obolibrary.org/obo/BSPO_0000120), [BSPO:0000121](http://purl.obolibrary.org/obo/BSPO_0000121), [BSPO:0000122](http://purl.obolibrary.org/obo/BSPO_0000122), [BSPO:0000123](http://purl.obolibrary.org/obo/BSPO_0000123), [BSPO:0000124](http://purl.obolibrary.org/obo/BSPO_0000124), ... |
| `BSPO:curators`      |              4 | [BSPO:0001107](http://purl.obolibrary.org/obo/BSPO_0001107), [BSPO:0015009](http://purl.obolibrary.org/obo/BSPO_0015009), [BSPO:0015012](http://purl.obolibrary.org/obo/BSPO_0015012), [BSPO:0015014](http://purl.obolibrary.org/obo/BSPO_0015014)                                                                   |

## `BTO`: BRENDA Tissue Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `BTO` (standardized to Bioregistry
prefix [`bto`](https://bioregistry.io/bto)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `BTO:000125`    |              1 | [CL:1000398](http://purl.obolibrary.org/obo/CL_1000398) |

## `CALOHA`: CALIPHO Group Ontology of Human Anatomy

Overall, there were 3 invalid
xrefs to external prefixed with `CALOHA` (standardized to Bioregistry
prefix [`caloha`](https://bioregistry.io/caloha)) that
did not match the standard pattern `^TS-\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                            |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CALOHA:paula`  |              3 | [UBERON:0007808](http://purl.obolibrary.org/obo/UBERON_0007808), [UBERON:0014454](http://purl.obolibrary.org/obo/UBERON_0014454), [UBERON:0014455](http://purl.obolibrary.org/obo/UBERON_0014455) |

## `CARO`: Common Anatomy Reference Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `CARO` (standardized to Bioregistry
prefix [`caro`](https://bioregistry.io/caro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CARO:DOS`      |              4 | [UBERON:0000026](http://purl.obolibrary.org/obo/UBERON_0000026), [UBERON:0000475](http://purl.obolibrary.org/obo/UBERON_0000475), [UBERON:0000478](http://purl.obolibrary.org/obo/UBERON_0000478), [UBERON:0022295](http://purl.obolibrary.org/obo/UBERON_0022295) |
| `CARO:mah`      |              2 | [CL:0000000](http://purl.obolibrary.org/obo/CL_0000000), [CL:0000003](http://purl.obolibrary.org/obo/CL_0000003)                                                                                                                                                   |
| `CARO:MAH`      |              1 | [CARO:0000000](http://purl.obolibrary.org/obo/CARO_0000000)                                                                                                                                                                                                        |

## `CL`: Cell Ontology

Overall, there were 27 invalid
xrefs to external prefixed with `CL` (standardized to Bioregistry
prefix [`cl`](https://bioregistry.io/cl)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                            |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CL:tm`                                  |             19 | [UBERON:0001249](http://purl.obolibrary.org/obo/UBERON_0001249), [UBERON:0001249](http://purl.obolibrary.org/obo/UBERON_0001249), [UBERON:0001745](http://purl.obolibrary.org/obo/UBERON_0001745), [UBERON:0004041](http://purl.obolibrary.org/obo/UBERON_0004041), [UBERON:0004042](http://purl.obolibrary.org/obo/UBERON_0004042), ... |
| `CL:CVS`                                 |              6 | [CL:0005000](http://purl.obolibrary.org/obo/CL_0005000), [CL:0005009](http://purl.obolibrary.org/obo/CL_0005009), [CL:0005012](http://purl.obolibrary.org/obo/CL_0005012), [CL:0005014](http://purl.obolibrary.org/obo/CL_0005014), [CL:0005020](http://purl.obolibrary.org/obo/CL_0005020), ...                                         |
| `CL:MAH`                                 |              1 | [CL:0007011](http://purl.obolibrary.org/obo/CL_0007011)                                                                                                                                                                                                                                                                                  |
| `CL:patterns/cellPartOfAnatomicalEntity` |              1 | [CL:0011030](http://purl.obolibrary.org/obo/CL_0011030)                                                                                                                                                                                                                                                                                  |

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

## `DO`: Human Disease Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `DO` (standardized to Bioregistry
prefix [`doid`](https://bioregistry.io/doid)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `DO:wk`         |              1 | [DOID:0050178](http://purl.obolibrary.org/obo/DOID_0050178) |
| `DO:lh`         |              1 | [DOID:462](http://purl.obolibrary.org/obo/DOID_462)         |

## `DOI`: Digital Object Identifier

Overall, there were 8 invalid
xrefs to external prefixed with `DOI` (standardized to Bioregistry
prefix [`doi`](https://bioregistry.io/doi)) that
did not match the standard pattern `^10.\d{2,9}/.*$`.

| external_xref                               |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|---------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DOI:10.1126`                               |              7 | [SO:0001486](http://purl.obolibrary.org/obo/SO_0001486), [SO:0001487](http://purl.obolibrary.org/obo/SO_0001487), [SO:0001488](http://purl.obolibrary.org/obo/SO_0001488), [SO:0001489](http://purl.obolibrary.org/obo/SO_0001489), [SO:0001490](http://purl.obolibrary.org/obo/SO_0001490), ... |
| `DOI:https://doi.org/10.1378/chest.12-2762` |              1 | [CL:0000158](http://purl.obolibrary.org/obo/CL_0000158)                                                                                                                                                                                                                                          |

## `DrugBank`: DrugBank

Overall, there were 3 invalid
xrefs to external prefixed with `DrugBank` (standardized to Bioregistry
prefix [`drugbank`](https://bioregistry.io/drugbank)) that
did not match the standard pattern `^DB\d{5}$`.

| external_xref           |   usages_count | usages                                                    |
|-------------------------|----------------|-----------------------------------------------------------|
| `DrugBank:DBSALT000889` |              1 | [CHEBI:5556](http://purl.obolibrary.org/obo/CHEBI_5556)   |
| `DrugBank:DBSALT003069` |              1 | [CHEBI:91243](http://purl.obolibrary.org/obo/CHEBI_91243) |
| `DrugBank:DBSALT001257` |              1 | [CHEBI:9925](http://purl.obolibrary.org/obo/CHEBI_9925)   |

## `EC`: Enzyme Commission Code

Overall, there were 1,036 invalid
xrefs to external prefixed with `EC` (standardized to Bioregistry
prefix [`eccode`](https://bioregistry.io/eccode)) that
did not match the standard pattern `^\d{1,2}(((\.\d{1,3}){1,3})|(\.\d+){2}\.n\d{1,3})?$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `EC:1.14.13.-`  |            114 | [GO:0016709](http://purl.obolibrary.org/obo/GO_0016709), [GO:0018471](http://purl.obolibrary.org/obo/GO_0018471), [GO:0018630](http://purl.obolibrary.org/obo/GO_0018630), [GO:0018631](http://purl.obolibrary.org/obo/GO_0018631), [GO:0018633](http://purl.obolibrary.org/obo/GO_0018633), ... |
| `EC:2.4.1.-`    |             94 | [GO:0016758](http://purl.obolibrary.org/obo/GO_0016758), [GO:0080002](http://purl.obolibrary.org/obo/GO_0080002), [GO:0102154](http://purl.obolibrary.org/obo/GO_0102154), [GO:0102156](http://purl.obolibrary.org/obo/GO_0102156), [GO:0102163](http://purl.obolibrary.org/obo/GO_0102163), ... |
| `EC:2.1.1.-`    |             64 | [GO:0008168](http://purl.obolibrary.org/obo/GO_0008168), [GO:0008169](http://purl.obolibrary.org/obo/GO_0008169), [GO:0008170](http://purl.obolibrary.org/obo/GO_0008170), [GO:0008171](http://purl.obolibrary.org/obo/GO_0008171), [GO:0008172](http://purl.obolibrary.org/obo/GO_0008172), ... |
| `EC:1.13.11.-`  |             45 | [GO:0016702](http://purl.obolibrary.org/obo/GO_0016702), [GO:0018542](http://purl.obolibrary.org/obo/GO_0018542), [GO:0018555](http://purl.obolibrary.org/obo/GO_0018555), [GO:0018556](http://purl.obolibrary.org/obo/GO_0018556), [GO:0018557](http://purl.obolibrary.org/obo/GO_0018557), ... |
| `EC:2.3.1.-`    |             41 | [GO:0016747](http://purl.obolibrary.org/obo/GO_0016747), [GO:0016747](http://purl.obolibrary.org/obo/GO_0016747), [GO:0034915](http://purl.obolibrary.org/obo/GO_0034915), [GO:0034945](http://purl.obolibrary.org/obo/GO_0034945), [GO:0043806](http://purl.obolibrary.org/obo/GO_0043806), ... |
| `EC:1.14.11.-`  |             25 | [GO:0016706](http://purl.obolibrary.org/obo/GO_0016706), [GO:0102111](http://purl.obolibrary.org/obo/GO_0102111), [GO:0102494](http://purl.obolibrary.org/obo/GO_0102494), [GO:0102495](http://purl.obolibrary.org/obo/GO_0102495), [GO:0102496](http://purl.obolibrary.org/obo/GO_0102496), ... |
| `EC:1.14.12.-`  |             20 | [GO:0016708](http://purl.obolibrary.org/obo/GO_0016708), [GO:0018603](http://purl.obolibrary.org/obo/GO_0018603), [GO:0018604](http://purl.obolibrary.org/obo/GO_0018604), [GO:0018606](http://purl.obolibrary.org/obo/GO_0018606), [GO:0018607](http://purl.obolibrary.org/obo/GO_0018607), ... |
| `EC:1.3.1.-`    |             18 | [GO:0016628](http://purl.obolibrary.org/obo/GO_0016628), [GO:0035671](http://purl.obolibrary.org/obo/GO_0035671), [GO:0102233](http://purl.obolibrary.org/obo/GO_0102233), [GO:0102234](http://purl.obolibrary.org/obo/GO_0102234), [GO:0102678](http://purl.obolibrary.org/obo/GO_0102678), ... |
| `EC:4.2.3.-`    |             17 | [GO:0010333](http://purl.obolibrary.org/obo/GO_0010333), [GO:0010334](http://purl.obolibrary.org/obo/GO_0010334), [GO:0016838](http://purl.obolibrary.org/obo/GO_0016838), [GO:0016838](http://purl.obolibrary.org/obo/GO_0016838), [GO:0080015](http://purl.obolibrary.org/obo/GO_0080015), ... |
| `EC:1.14.19.-`  |             16 | [GO:0016717](http://purl.obolibrary.org/obo/GO_0016717), [GO:0102656](http://purl.obolibrary.org/obo/GO_0102656), [GO:0102676](http://purl.obolibrary.org/obo/GO_0102676), [GO:0102845](http://purl.obolibrary.org/obo/GO_0102845), [GO:0102846](http://purl.obolibrary.org/obo/GO_0102846), ... |
| `EC:1.97.1.-`   |             16 | [GO:0018698](http://purl.obolibrary.org/obo/GO_0018698), [GO:0018699](http://purl.obolibrary.org/obo/GO_0018699), [GO:0018700](http://purl.obolibrary.org/obo/GO_0018700), [GO:0018701](http://purl.obolibrary.org/obo/GO_0018701), [GO:0018702](http://purl.obolibrary.org/obo/GO_0018702), ... |
| `EC:3.3.2.-`    |             13 | [GO:0008096](http://purl.obolibrary.org/obo/GO_0008096), [GO:0016803](http://purl.obolibrary.org/obo/GO_0016803), [GO:0016803](http://purl.obolibrary.org/obo/GO_0016803), [GO:0018742](http://purl.obolibrary.org/obo/GO_0018742), [GO:0018743](http://purl.obolibrary.org/obo/GO_0018743), ... |
| `EC:6.2.1.-`    |             13 | [GO:0010435](http://purl.obolibrary.org/obo/GO_0010435), [GO:0016878](http://purl.obolibrary.org/obo/GO_0016878), [GO:0016878](http://purl.obolibrary.org/obo/GO_0016878), [GO:0018853](http://purl.obolibrary.org/obo/GO_0018853), [GO:0047473](http://purl.obolibrary.org/obo/GO_0047473), ... |
| `EC:6.3.-.-`    |             12 | [GO:0016879](http://purl.obolibrary.org/obo/GO_0016879), [GO:0102050](http://purl.obolibrary.org/obo/GO_0102050), [GO:0102051](http://purl.obolibrary.org/obo/GO_0102051), [GO:0102052](http://purl.obolibrary.org/obo/GO_0102052), [GO:0102085](http://purl.obolibrary.org/obo/GO_0102085), ... |
| `EC:3.2.1.-`    |             10 | [GO:0004553](http://purl.obolibrary.org/obo/GO_0004553), [GO:0008843](http://purl.obolibrary.org/obo/GO_0008843), [GO:0035885](http://purl.obolibrary.org/obo/GO_0035885), [GO:0102224](http://purl.obolibrary.org/obo/GO_0102224), [GO:0102277](http://purl.obolibrary.org/obo/GO_0102277), ... |
| `EC:1.2.1.-`    |             10 | [GO:0016620](http://purl.obolibrary.org/obo/GO_0016620), [GO:0018474](http://purl.obolibrary.org/obo/GO_0018474), [GO:0019115](http://purl.obolibrary.org/obo/GO_0019115), [GO:0034520](http://purl.obolibrary.org/obo/GO_0034520), [GO:0034530](http://purl.obolibrary.org/obo/GO_0034530), ... |
| `EC:4.2.1.-`    |              9 | [GO:0016836](http://purl.obolibrary.org/obo/GO_0016836), [GO:0016836](http://purl.obolibrary.org/obo/GO_0016836), [GO:0018128](http://purl.obolibrary.org/obo/GO_0018128), [GO:0018135](http://purl.obolibrary.org/obo/GO_0018135), [GO:0102471](http://purl.obolibrary.org/obo/GO_0102471), ... |
| `EC:1.14.-.-`   |              9 | [GO:0016705](http://purl.obolibrary.org/obo/GO_0016705), [GO:0018600](http://purl.obolibrary.org/obo/GO_0018600), [GO:0102123](http://purl.obolibrary.org/obo/GO_0102123), [GO:0102124](http://purl.obolibrary.org/obo/GO_0102124), [GO:0102125](http://purl.obolibrary.org/obo/GO_0102125), ... |
| `EC:2.8.2.-`    |              8 | [GO:0001537](http://purl.obolibrary.org/obo/GO_0001537), [GO:0008146](http://purl.obolibrary.org/obo/GO_0008146), [GO:0019111](http://purl.obolibrary.org/obo/GO_0019111), [GO:0050698](http://purl.obolibrary.org/obo/GO_0050698), [GO:0080131](http://purl.obolibrary.org/obo/GO_0080131), ... |
| `EC:2.5.1.-`    |              8 | [GO:0016765](http://purl.obolibrary.org/obo/GO_0016765), [GO:0043888](http://purl.obolibrary.org/obo/GO_0043888), [GO:0052622](http://purl.obolibrary.org/obo/GO_0052622), [GO:0052623](http://purl.obolibrary.org/obo/GO_0052623), [GO:0102298](http://purl.obolibrary.org/obo/GO_0102298), ... |
| `EC:1.14.15.-`  |              8 | [GO:0016713](http://purl.obolibrary.org/obo/GO_0016713), [GO:0018680](http://purl.obolibrary.org/obo/GO_0018680), [GO:0018681](http://purl.obolibrary.org/obo/GO_0018681), [GO:0018682](http://purl.obolibrary.org/obo/GO_0018682), [GO:0034577](http://purl.obolibrary.org/obo/GO_0034577), ... |
| `EC:1.3.99.-`   |              8 | [GO:0034580](http://purl.obolibrary.org/obo/GO_0034580), [GO:0034845](http://purl.obolibrary.org/obo/GO_0034845), [GO:0034916](http://purl.obolibrary.org/obo/GO_0034916), [GO:0043820](http://purl.obolibrary.org/obo/GO_0043820), [GO:0043830](http://purl.obolibrary.org/obo/GO_0043830), ... |
| `EC:3.1.2.-`    |              7 | [GO:0016790](http://purl.obolibrary.org/obo/GO_0016790), [GO:0016790](http://purl.obolibrary.org/obo/GO_0016790), [GO:0102150](http://purl.obolibrary.org/obo/GO_0102150), [GO:0102327](http://purl.obolibrary.org/obo/GO_0102327), [GO:0102574](http://purl.obolibrary.org/obo/GO_0102574), ... |
| `EC:2.4.2.-`    |              7 | [GO:0016763](http://purl.obolibrary.org/obo/GO_0016763), [GO:0018071](http://purl.obolibrary.org/obo/GO_0018071), [GO:0018121](http://purl.obolibrary.org/obo/GO_0018121), [GO:0018127](http://purl.obolibrary.org/obo/GO_0018127), [GO:0102562](http://purl.obolibrary.org/obo/GO_0102562), ... |
| `EC:2.6.1.-`    |              7 | [GO:0008483](http://purl.obolibrary.org/obo/GO_0008483), [GO:0036136](http://purl.obolibrary.org/obo/GO_0036136), [GO:0036137](http://purl.obolibrary.org/obo/GO_0036137), [GO:0102081](http://purl.obolibrary.org/obo/GO_0102081), [GO:0102570](http://purl.obolibrary.org/obo/GO_0102570), ... |
| `EC:2.7.1.-`    |              6 | [GO:0016773](http://purl.obolibrary.org/obo/GO_0016773), [GO:0051717](http://purl.obolibrary.org/obo/GO_0051717), [GO:0051723](http://purl.obolibrary.org/obo/GO_0051723), [GO:0102238](http://purl.obolibrary.org/obo/GO_0102238), [GO:0102731](http://purl.obolibrary.org/obo/GO_0102731), ... |
| `EC:1.13.12.-`  |              6 | [GO:0016703](http://purl.obolibrary.org/obo/GO_0016703), [GO:0034835](http://purl.obolibrary.org/obo/GO_0034835), [GO:0034836](http://purl.obolibrary.org/obo/GO_0034836), [GO:0034850](http://purl.obolibrary.org/obo/GO_0034850), [GO:0034898](http://purl.obolibrary.org/obo/GO_0034898), ... |
| `EC:2.3.3.-`    |              6 | [GO:0046912](http://purl.obolibrary.org/obo/GO_0046912), [GO:0103079](http://purl.obolibrary.org/obo/GO_0103079), [GO:0103082](http://purl.obolibrary.org/obo/GO_0103082), [GO:0103085](http://purl.obolibrary.org/obo/GO_0103085), [GO:0103088](http://purl.obolibrary.org/obo/GO_0103088), ... |
| `EC:5.4.4.-`    |              6 | [GO:0050486](http://purl.obolibrary.org/obo/GO_0050486), [GO:0103080](http://purl.obolibrary.org/obo/GO_0103080), [GO:0103083](http://purl.obolibrary.org/obo/GO_0103083), [GO:0103086](http://purl.obolibrary.org/obo/GO_0103086), [GO:0103089](http://purl.obolibrary.org/obo/GO_0103089), ... |
| `EC:3.5.99.-`   |              6 | [GO:0034544](http://purl.obolibrary.org/obo/GO_0034544), [GO:0034565](http://purl.obolibrary.org/obo/GO_0034565), [GO:0034886](http://purl.obolibrary.org/obo/GO_0034886), [GO:0034896](http://purl.obolibrary.org/obo/GO_0034896), [GO:0034900](http://purl.obolibrary.org/obo/GO_0034900), ... |
| `EC:4.1.3.-`    |              5 | [GO:0016833](http://purl.obolibrary.org/obo/GO_0016833), [GO:0016833](http://purl.obolibrary.org/obo/GO_0016833), [GO:0034815](http://purl.obolibrary.org/obo/GO_0034815), [GO:0034830](http://purl.obolibrary.org/obo/GO_0034830), [GO:0034905](http://purl.obolibrary.org/obo/GO_0034905)      |
| `EC:4.3.-.-`    |              5 | [GO:0016840](http://purl.obolibrary.org/obo/GO_0016840), [GO:0016840](http://purl.obolibrary.org/obo/GO_0016840), [GO:0016841](http://purl.obolibrary.org/obo/GO_0016841), [GO:0016842](http://purl.obolibrary.org/obo/GO_0016842), [GO:0016843](http://purl.obolibrary.org/obo/GO_0016843)      |
| `EC:3.5.1.-`    |              5 | [GO:0016811](http://purl.obolibrary.org/obo/GO_0016811), [GO:0052790](http://purl.obolibrary.org/obo/GO_0052790), [GO:0102281](http://purl.obolibrary.org/obo/GO_0102281), [GO:0102572](http://purl.obolibrary.org/obo/GO_0102572), [GO:0102622](http://purl.obolibrary.org/obo/GO_0102622)      |
| `EC:3.1.3.-`    |              5 | [GO:0016791](http://purl.obolibrary.org/obo/GO_0016791), [GO:0102520](http://purl.obolibrary.org/obo/GO_0102520), [GO:0102537](http://purl.obolibrary.org/obo/GO_0102537), [GO:0103026](http://purl.obolibrary.org/obo/GO_0103026), [GO:0103027](http://purl.obolibrary.org/obo/GO_0103027)      |
| `EC:1.5.99.-`   |              5 | [GO:0018532](http://purl.obolibrary.org/obo/GO_0018532), [GO:0018534](http://purl.obolibrary.org/obo/GO_0018534), [GO:0034568](http://purl.obolibrary.org/obo/GO_0034568), [GO:0034570](http://purl.obolibrary.org/obo/GO_0034570), [GO:0034572](http://purl.obolibrary.org/obo/GO_0034572)      |
| `EC:1.1.1.-`    |              4 | [GO:0016616](http://purl.obolibrary.org/obo/GO_0016616), [GO:0016616](http://purl.obolibrary.org/obo/GO_0016616), [GO:0102182](http://purl.obolibrary.org/obo/GO_0102182), [GO:0102727](http://purl.obolibrary.org/obo/GO_0102727)                                                               |
| `EC:6.3.1.-`    |              4 | [GO:0016211](http://purl.obolibrary.org/obo/GO_0016211), [GO:0016880](http://purl.obolibrary.org/obo/GO_0016880), [GO:0043860](http://purl.obolibrary.org/obo/GO_0043860), [GO:0102115](http://purl.obolibrary.org/obo/GO_0102115)                                                               |
| `EC:4.1.1.-`    |              4 | [GO:0016831](http://purl.obolibrary.org/obo/GO_0016831), [GO:0043728](http://purl.obolibrary.org/obo/GO_0043728), [GO:0102328](http://purl.obolibrary.org/obo/GO_0102328), [GO:0102765](http://purl.obolibrary.org/obo/GO_0102765)                                                               |
| `EC:5.5.1.-`    |              4 | [GO:0016872](http://purl.obolibrary.org/obo/GO_0016872), [GO:0018847](http://purl.obolibrary.org/obo/GO_0018847), [GO:0018848](http://purl.obolibrary.org/obo/GO_0018848), [GO:0034794](http://purl.obolibrary.org/obo/GO_0034794)                                                               |
| `EC:4.5.1.-`    |              4 | [GO:0018827](http://purl.obolibrary.org/obo/GO_0018827), [GO:0018829](http://purl.obolibrary.org/obo/GO_0018829), [GO:0018830](http://purl.obolibrary.org/obo/GO_0018830), [GO:0018831](http://purl.obolibrary.org/obo/GO_0018831)                                                               |
| `EC:5.3.99.-`   |              4 | [GO:0018844](http://purl.obolibrary.org/obo/GO_0018844), [GO:0034528](http://purl.obolibrary.org/obo/GO_0034528), [GO:0034532](http://purl.obolibrary.org/obo/GO_0034532), [GO:0034536](http://purl.obolibrary.org/obo/GO_0034536)                                                               |
| `EC:3.1.4.-`    |              3 | [GO:0005966](http://purl.obolibrary.org/obo/GO_0005966), [GO:0008081](http://purl.obolibrary.org/obo/GO_0008081), [GO:0008081](http://purl.obolibrary.org/obo/GO_0008081)                                                                                                                        |
| `EC:2.1.2.-`    |              3 | [GO:0016742](http://purl.obolibrary.org/obo/GO_0016742), [GO:0016742](http://purl.obolibrary.org/obo/GO_0016742), [GO:0044685](http://purl.obolibrary.org/obo/GO_0044685)                                                                                                                        |
| `EC:5.3.-.-`    |              3 | [GO:0016860](http://purl.obolibrary.org/obo/GO_0016860), [GO:0016860](http://purl.obolibrary.org/obo/GO_0016860), [GO:0102929](http://purl.obolibrary.org/obo/GO_0102929)                                                                                                                        |
| `EC:3.1.1.-`    |              3 | [GO:0052689](http://purl.obolibrary.org/obo/GO_0052689), [GO:0052689](http://purl.obolibrary.org/obo/GO_0052689), [GO:0102140](http://purl.obolibrary.org/obo/GO_0102140)                                                                                                                        |
| `EC:2.3.2.-`    |              3 | [GO:0016755](http://purl.obolibrary.org/obo/GO_0016755), [GO:0102272](http://purl.obolibrary.org/obo/GO_0102272), [GO:0102273](http://purl.obolibrary.org/obo/GO_0102273)                                                                                                                        |
| `EC:3.7.1.-`    |              3 | [GO:0016823](http://purl.obolibrary.org/obo/GO_0016823), [GO:0034948](http://purl.obolibrary.org/obo/GO_0034948), [GO:0102324](http://purl.obolibrary.org/obo/GO_0102324)                                                                                                                        |
| `EC:2.7.4.-`    |              3 | [GO:0016776](http://purl.obolibrary.org/obo/GO_0016776), [GO:0102352](http://purl.obolibrary.org/obo/GO_0102352), [GO:0102763](http://purl.obolibrary.org/obo/GO_0102763)                                                                                                                        |
| `EC:5.1.3.-`    |              3 | [GO:0016857](http://purl.obolibrary.org/obo/GO_0016857), [GO:0102540](http://purl.obolibrary.org/obo/GO_0102540), [GO:0102541](http://purl.obolibrary.org/obo/GO_0102541)                                                                                                                        |
| `EC:2.2.1.-`    |              3 | [GO:0016744](http://purl.obolibrary.org/obo/GO_0016744), [GO:0102647](http://purl.obolibrary.org/obo/GO_0102647), [GO:0102648](http://purl.obolibrary.org/obo/GO_0102648)                                                                                                                        |
| `EC:6.3.2.-`    |              3 | [GO:0016881](http://purl.obolibrary.org/obo/GO_0016881), [GO:0102650](http://purl.obolibrary.org/obo/GO_0102650), [GO:0103044](http://purl.obolibrary.org/obo/GO_0103044)                                                                                                                        |
| `EC:3.1.-.-`    |              3 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788), [GO:0102666](http://purl.obolibrary.org/obo/GO_0102666), [GO:0102667](http://purl.obolibrary.org/obo/GO_0102667)                                                                                                                        |
| `EC:1.3.-.-`    |              3 | [GO:0003995](http://purl.obolibrary.org/obo/GO_0003995), [GO:0016627](http://purl.obolibrary.org/obo/GO_0016627), [GO:0102725](http://purl.obolibrary.org/obo/GO_0102725)                                                                                                                        |
| `EC:1.6.5.-`    |              3 | [GO:0016655](http://purl.obolibrary.org/obo/GO_0016655), [GO:0050625](http://purl.obolibrary.org/obo/GO_0050625), [GO:0103035](http://purl.obolibrary.org/obo/GO_0103035)                                                                                                                        |
| `EC:4.1.-.-`    |              3 | [GO:0016830](http://purl.obolibrary.org/obo/GO_0016830), [GO:0103071](http://purl.obolibrary.org/obo/GO_0103071), [GO:0103072](http://purl.obolibrary.org/obo/GO_0103072)                                                                                                                        |
| `EC:5.2.1.-`    |              3 | [GO:0018839](http://purl.obolibrary.org/obo/GO_0018839), [GO:0034872](http://purl.obolibrary.org/obo/GO_0034872), [GO:0047466](http://purl.obolibrary.org/obo/GO_0047466)                                                                                                                        |
| `EC:3.1.13.-`   |              3 | [GO:0000175](http://purl.obolibrary.org/obo/GO_0000175), [GO:0004534](http://purl.obolibrary.org/obo/GO_0004534), [GO:0016896](http://purl.obolibrary.org/obo/GO_0016896)                                                                                                                        |
| `EC:3.1.11.-`   |              3 | [GO:0008856](http://purl.obolibrary.org/obo/GO_0008856), [GO:0008997](http://purl.obolibrary.org/obo/GO_0008997), [GO:0016895](http://purl.obolibrary.org/obo/GO_0016895)                                                                                                                        |
| `EC:1.14.14.-`  |              3 | [GO:0016712](http://purl.obolibrary.org/obo/GO_0016712), [GO:0018679](http://purl.obolibrary.org/obo/GO_0018679), [GO:0034938](http://purl.obolibrary.org/obo/GO_0034938)                                                                                                                        |
| `EC:1.17.4.-`   |              3 | [GO:0016728](http://purl.obolibrary.org/obo/GO_0016728), [GO:0051064](http://purl.obolibrary.org/obo/GO_0051064), [GO:0051065](http://purl.obolibrary.org/obo/GO_0051065)                                                                                                                        |
| `EC:6.3.4.-`    |              3 | [GO:0018271](http://purl.obolibrary.org/obo/GO_0018271), [GO:0032267](http://purl.obolibrary.org/obo/GO_0032267), [GO:0071734](http://purl.obolibrary.org/obo/GO_0071734)                                                                                                                        |
| `EC:1.17.99.-`  |              3 | [GO:0034569](http://purl.obolibrary.org/obo/GO_0034569), [GO:0034574](http://purl.obolibrary.org/obo/GO_0034574), [GO:0034575](http://purl.obolibrary.org/obo/GO_0034575)                                                                                                                        |
| `EC:5.4.99.-`   |              3 | [GO:0034784](http://purl.obolibrary.org/obo/GO_0034784), [GO:0034951](http://purl.obolibrary.org/obo/GO_0034951), [GO:0042300](http://purl.obolibrary.org/obo/GO_0042300)                                                                                                                        |
| `EC:3.4.19.-`   |              2 | [GO:0008242](http://purl.obolibrary.org/obo/GO_0008242), [GO:0008242](http://purl.obolibrary.org/obo/GO_0008242)                                                                                                                                                                                 |
| `EC:7.5.2.-`    |              2 | [GO:0015407](http://purl.obolibrary.org/obo/GO_0015407), [GO:0015407](http://purl.obolibrary.org/obo/GO_0015407)                                                                                                                                                                                 |
| `EC:1.4.-.-`    |              2 | [GO:0015930](http://purl.obolibrary.org/obo/GO_0015930), [GO:0016638](http://purl.obolibrary.org/obo/GO_0016638)                                                                                                                                                                                 |
| `EC:3.1.8.-`    |              2 | [GO:0016795](http://purl.obolibrary.org/obo/GO_0016795), [GO:0016795](http://purl.obolibrary.org/obo/GO_0016795)                                                                                                                                                                                 |
| `EC:3.3.1.-`    |              2 | [GO:0016802](http://purl.obolibrary.org/obo/GO_0016802), [GO:0016802](http://purl.obolibrary.org/obo/GO_0016802)                                                                                                                                                                                 |
| `EC:4.2.-.-`    |              2 | [GO:0016835](http://purl.obolibrary.org/obo/GO_0016835), [GO:0016835](http://purl.obolibrary.org/obo/GO_0016835)                                                                                                                                                                                 |
| `EC:4.4.-.-`    |              2 | [GO:0016846](http://purl.obolibrary.org/obo/GO_0016846), [GO:0016846](http://purl.obolibrary.org/obo/GO_0016846)                                                                                                                                                                                 |
| `EC:5.3.3.-`    |              2 | [GO:0016863](http://purl.obolibrary.org/obo/GO_0016863), [GO:0016863](http://purl.obolibrary.org/obo/GO_0016863)                                                                                                                                                                                 |
| `EC:5.3.4.-`    |              2 | [GO:0016864](http://purl.obolibrary.org/obo/GO_0016864), [GO:0016864](http://purl.obolibrary.org/obo/GO_0016864)                                                                                                                                                                                 |
| `EC:6.1.-.-`    |              2 | [GO:0016875](http://purl.obolibrary.org/obo/GO_0016875), [GO:0016875](http://purl.obolibrary.org/obo/GO_0016875)                                                                                                                                                                                 |
| `EC:6.2.-.-`    |              2 | [GO:0016877](http://purl.obolibrary.org/obo/GO_0016877), [GO:0016877](http://purl.obolibrary.org/obo/GO_0016877)                                                                                                                                                                                 |
| `EC:6.4.-.-`    |              2 | [GO:0016885](http://purl.obolibrary.org/obo/GO_0016885), [GO:0016885](http://purl.obolibrary.org/obo/GO_0016885)                                                                                                                                                                                 |
| `EC:6.5.-.-`    |              2 | [GO:0016886](http://purl.obolibrary.org/obo/GO_0016886), [GO:0016886](http://purl.obolibrary.org/obo/GO_0016886)                                                                                                                                                                                 |
| `EC:1.17.5.-`   |              2 | [GO:0033695](http://purl.obolibrary.org/obo/GO_0033695), [GO:0033695](http://purl.obolibrary.org/obo/GO_0033695)                                                                                                                                                                                 |
| `EC:3.5.4.-`    |              2 | [GO:0016814](http://purl.obolibrary.org/obo/GO_0016814), [GO:0035888](http://purl.obolibrary.org/obo/GO_0035888)                                                                                                                                                                                 |
| `EC:1.16.8.-`   |              2 | [GO:0043783](http://purl.obolibrary.org/obo/GO_0043783), [GO:0043783](http://purl.obolibrary.org/obo/GO_0043783)                                                                                                                                                                                 |
| `EC:1.6.3.-`    |              2 | [GO:0050664](http://purl.obolibrary.org/obo/GO_0050664), [GO:0050664](http://purl.obolibrary.org/obo/GO_0050664)                                                                                                                                                                                 |
| `EC:6.6.-.-`    |              2 | [GO:0051002](http://purl.obolibrary.org/obo/GO_0051002), [GO:0051002](http://purl.obolibrary.org/obo/GO_0051002)                                                                                                                                                                                 |
| `EC:6.6.1.-`    |              2 | [GO:0051003](http://purl.obolibrary.org/obo/GO_0051003), [GO:0051003](http://purl.obolibrary.org/obo/GO_0051003)                                                                                                                                                                                 |
| `EC:2.-.-.-`    |              2 | [GO:0016740](http://purl.obolibrary.org/obo/GO_0016740), [GO:0051972](http://purl.obolibrary.org/obo/GO_0051972)                                                                                                                                                                                 |
| `EC:1.2.5.-`    |              2 | [GO:0052738](http://purl.obolibrary.org/obo/GO_0052738), [GO:0052738](http://purl.obolibrary.org/obo/GO_0052738)                                                                                                                                                                                 |
| `EC:1.21.3.-`   |              2 | [GO:0046993](http://purl.obolibrary.org/obo/GO_0046993), [GO:0102089](http://purl.obolibrary.org/obo/GO_0102089)                                                                                                                                                                                 |
| `EC:2.7.8.-`    |              2 | [GO:0016780](http://purl.obolibrary.org/obo/GO_0016780), [GO:0102249](http://purl.obolibrary.org/obo/GO_0102249)                                                                                                                                                                                 |
| `EC:3.4.17.-`   |              2 | [GO:0004181](http://purl.obolibrary.org/obo/GO_0004181), [GO:0102274](http://purl.obolibrary.org/obo/GO_0102274)                                                                                                                                                                                 |
| `EC:1.17.1.-`   |              2 | [GO:0016726](http://purl.obolibrary.org/obo/GO_0016726), [GO:0102310](http://purl.obolibrary.org/obo/GO_0102310)                                                                                                                                                                                 |
| `EC:1.3.8.-`    |              2 | [GO:0052890](http://purl.obolibrary.org/obo/GO_0052890), [GO:0102393](http://purl.obolibrary.org/obo/GO_0102393)                                                                                                                                                                                 |
| `EC:1.5.1.-`    |              2 | [GO:0016646](http://purl.obolibrary.org/obo/GO_0016646), [GO:0102544](http://purl.obolibrary.org/obo/GO_0102544)                                                                                                                                                                                 |
| `EC:3.2.2.-`    |              2 | [GO:0016799](http://purl.obolibrary.org/obo/GO_0016799), [GO:0102682](http://purl.obolibrary.org/obo/GO_0102682)                                                                                                                                                                                 |
| `EC:1.10.3.-`   |              2 | [GO:0016682](http://purl.obolibrary.org/obo/GO_0016682), [GO:0102910](http://purl.obolibrary.org/obo/GO_0102910)                                                                                                                                                                                 |
| `EC:1.11.-.-`   |              2 | [GO:0016684](http://purl.obolibrary.org/obo/GO_0016684), [GO:0103003](http://purl.obolibrary.org/obo/GO_0103003)                                                                                                                                                                                 |
| `EC:4.2.2.-`    |              2 | [GO:0016837](http://purl.obolibrary.org/obo/GO_0016837), [GO:0103028](http://purl.obolibrary.org/obo/GO_0103028)                                                                                                                                                                                 |
| `EC:5.1.1.-`    |              2 | [GO:0016855](http://purl.obolibrary.org/obo/GO_0016855), [GO:0103031](http://purl.obolibrary.org/obo/GO_0103031)                                                                                                                                                                                 |
| `EC:5.4.1.-`    |              2 | [GO:0016867](http://purl.obolibrary.org/obo/GO_0016867), [GO:0103033](http://purl.obolibrary.org/obo/GO_0103033)                                                                                                                                                                                 |
| `EC:1.1.5.-`    |              2 | [GO:0016901](http://purl.obolibrary.org/obo/GO_0016901), [GO:0103040](http://purl.obolibrary.org/obo/GO_0103040)                                                                                                                                                                                 |
| `EC:2.8.1.-`    |              2 | [GO:0016783](http://purl.obolibrary.org/obo/GO_0016783), [GO:0103041](http://purl.obolibrary.org/obo/GO_0103041)                                                                                                                                                                                 |
| `EC:3.1.25.-`   |              2 | [GO:0016890](http://purl.obolibrary.org/obo/GO_0016890), [GO:1990043](http://purl.obolibrary.org/obo/GO_1990043)                                                                                                                                                                                 |
| `EC:3.4.25.-`   |              2 | [GO:0004298](http://purl.obolibrary.org/obo/GO_0004298), [GO:0004298](http://purl.obolibrary.org/obo/GO_0004298)                                                                                                                                                                                 |
| `EC:6.3.5.-`    |              2 | [GO:0016884](http://purl.obolibrary.org/obo/GO_0016884), [GO:0050567](http://purl.obolibrary.org/obo/GO_0050567)                                                                                                                                                                                 |
| `EC:2.7.3.-`    |              2 | [GO:0000155](http://purl.obolibrary.org/obo/GO_0000155), [GO:0016775](http://purl.obolibrary.org/obo/GO_0016775)                                                                                                                                                                                 |
| `EC:3.4.11.-`   |              2 | [GO:0004177](http://purl.obolibrary.org/obo/GO_0004177), [GO:0016284](http://purl.obolibrary.org/obo/GO_0016284)                                                                                                                                                                                 |
| `EC:3.4.23.-`   |              2 | [GO:0004190](http://purl.obolibrary.org/obo/GO_0004190), [GO:0042500](http://purl.obolibrary.org/obo/GO_0042500)                                                                                                                                                                                 |
| `EC:1.16.1.-`   |              2 | [GO:0008823](http://purl.obolibrary.org/obo/GO_0008823), [GO:0016723](http://purl.obolibrary.org/obo/GO_0016723)                                                                                                                                                                                 |
| `EC:7.-.-.-`    |              2 | [GO:0015399](http://purl.obolibrary.org/obo/GO_0015399), [GO:0106178](http://purl.obolibrary.org/obo/GO_0106178)                                                                                                                                                                                 |
| `EC:3.1.26.-`   |              2 | [GO:0016443](http://purl.obolibrary.org/obo/GO_0016443), [GO:0016891](http://purl.obolibrary.org/obo/GO_0016891)                                                                                                                                                                                 |
| `EC:1.4.3.-`    |              2 | [GO:0016641](http://purl.obolibrary.org/obo/GO_0016641), [GO:0043912](http://purl.obolibrary.org/obo/GO_0043912)                                                                                                                                                                                 |
| `EC:1.14.18.-`  |              2 | [GO:0016716](http://purl.obolibrary.org/obo/GO_0016716), [GO:0018686](http://purl.obolibrary.org/obo/GO_0018686)                                                                                                                                                                                 |
| `EC:2.7.2.-`    |              2 | [GO:0016774](http://purl.obolibrary.org/obo/GO_0016774), [GO:0036357](http://purl.obolibrary.org/obo/GO_0036357)                                                                                                                                                                                 |
| `EC:2.7.9.-`    |              2 | [GO:0016781](http://purl.obolibrary.org/obo/GO_0016781), [GO:0043749](http://purl.obolibrary.org/obo/GO_0043749)                                                                                                                                                                                 |
| `EC:4.6.-.-`    |              2 | [GO:0016849](http://purl.obolibrary.org/obo/GO_0016849), [GO:0042408](http://purl.obolibrary.org/obo/GO_0042408)                                                                                                                                                                                 |
| `EC:1.1.3.-`    |              2 | [GO:0016899](http://purl.obolibrary.org/obo/GO_0016899), [GO:0046563](http://purl.obolibrary.org/obo/GO_0046563)                                                                                                                                                                                 |
| `EC:1.2.-.-`    |              2 | [GO:0016903](http://purl.obolibrary.org/obo/GO_0016903), [GO:0051269](http://purl.obolibrary.org/obo/GO_0051269)                                                                                                                                                                                 |
| `EC:6.4.1.-`    |              2 | [GO:0018524](http://purl.obolibrary.org/obo/GO_0018524), [GO:0018862](http://purl.obolibrary.org/obo/GO_0018862)                                                                                                                                                                                 |
| `EC:1.7.99.-`   |              2 | [GO:0034800](http://purl.obolibrary.org/obo/GO_0034800), [GO:0034914](http://purl.obolibrary.org/obo/GO_0034914)                                                                                                                                                                                 |
| `EC:4.4.1.-`    |              2 | [GO:0034860](http://purl.obolibrary.org/obo/GO_0034860), [GO:0050312](http://purl.obolibrary.org/obo/GO_0050312)                                                                                                                                                                                 |
| `EC:1.14.21.-`  |              2 | [GO:0046996](http://purl.obolibrary.org/obo/GO_0046996), [GO:0080004](http://purl.obolibrary.org/obo/GO_0080004)                                                                                                                                                                                 |
| `EC:5.99.1.-`   |              1 | [GO:0008724](http://purl.obolibrary.org/obo/GO_0008724)                                                                                                                                                                                                                                          |
| `EC:3.6.5.-`    |              1 | [GO:0050800](http://purl.obolibrary.org/obo/GO_0050800)                                                                                                                                                                                                                                          |
| `EC:3.6.3.-`    |              1 | [GO:0103113](http://purl.obolibrary.org/obo/GO_0103113)                                                                                                                                                                                                                                          |
| `EC:1.5.1.33e`  |              1 | [GO:0047040](http://purl.obolibrary.org/obo/GO_0047040)                                                                                                                                                                                                                                          |
| `EC:3.4.16.-`   |              1 | [GO:0004185](http://purl.obolibrary.org/obo/GO_0004185)                                                                                                                                                                                                                                          |
| `EC:3.4.22.-`   |              1 | [GO:0004197](http://purl.obolibrary.org/obo/GO_0004197)                                                                                                                                                                                                                                          |
| `EC:3.4.24.-`   |              1 | [GO:0004222](http://purl.obolibrary.org/obo/GO_0004222)                                                                                                                                                                                                                                          |
| `EC:3.4.21.-`   |              1 | [GO:0004252](http://purl.obolibrary.org/obo/GO_0004252)                                                                                                                                                                                                                                          |
| `EC:1.11.1.-`   |              1 | [GO:0004601](http://purl.obolibrary.org/obo/GO_0004601)                                                                                                                                                                                                                                          |
| `EC:2.7.11.-`   |              1 | [GO:0004702](http://purl.obolibrary.org/obo/GO_0004702)                                                                                                                                                                                                                                          |
| `EC:2.7.10.-`   |              1 | [GO:0004716](http://purl.obolibrary.org/obo/GO_0004716)                                                                                                                                                                                                                                          |
| `EC:6.1.1.-`    |              1 | [GO:0004812](http://purl.obolibrary.org/obo/GO_0004812)                                                                                                                                                                                                                                          |
| `EC:3.4.-.-`    |              1 | [GO:0008233](http://purl.obolibrary.org/obo/GO_0008233)                                                                                                                                                                                                                                          |
| `EC:3.4.15.-`   |              1 | [GO:0008241](http://purl.obolibrary.org/obo/GO_0008241)                                                                                                                                                                                                                                          |
| `EC:2.4.3.-`    |              1 | [GO:0008373](http://purl.obolibrary.org/obo/GO_0008373)                                                                                                                                                                                                                                          |
| `EC:2.8.3.-`    |              1 | [GO:0008410](http://purl.obolibrary.org/obo/GO_0008410)                                                                                                                                                                                                                                          |
| `EC:3.1.6.-`    |              1 | [GO:0008484](http://purl.obolibrary.org/obo/GO_0008484)                                                                                                                                                                                                                                          |
| `EC:2.1.4.-`    |              1 | [GO:0015067](http://purl.obolibrary.org/obo/GO_0015067)                                                                                                                                                                                                                                          |
| `EC:1.-.-.-`    |              1 | [GO:0016491](http://purl.obolibrary.org/obo/GO_0016491)                                                                                                                                                                                                                                          |
| `EC:1.1.-.-`    |              1 | [GO:0016614](http://purl.obolibrary.org/obo/GO_0016614)                                                                                                                                                                                                                                          |
| `EC:1.2.2.-`    |              1 | [GO:0016622](http://purl.obolibrary.org/obo/GO_0016622)                                                                                                                                                                                                                                          |
| `EC:1.2.3.-`    |              1 | [GO:0016623](http://purl.obolibrary.org/obo/GO_0016623)                                                                                                                                                                                                                                          |
| `EC:1.2.4.-`    |              1 | [GO:0016624](http://purl.obolibrary.org/obo/GO_0016624)                                                                                                                                                                                                                                          |
| `EC:1.2.7.-`    |              1 | [GO:0016625](http://purl.obolibrary.org/obo/GO_0016625)                                                                                                                                                                                                                                          |
| `EC:1.3.2.-`    |              1 | [GO:0016632](http://purl.obolibrary.org/obo/GO_0016632)                                                                                                                                                                                                                                          |
| `EC:1.3.3.-`    |              1 | [GO:0016634](http://purl.obolibrary.org/obo/GO_0016634)                                                                                                                                                                                                                                          |
| `EC:1.3.5.-`    |              1 | [GO:0016635](http://purl.obolibrary.org/obo/GO_0016635)                                                                                                                                                                                                                                          |
| `EC:1.3.7.-`    |              1 | [GO:0016636](http://purl.obolibrary.org/obo/GO_0016636)                                                                                                                                                                                                                                          |
| `EC:1.4.1.-`    |              1 | [GO:0016639](http://purl.obolibrary.org/obo/GO_0016639)                                                                                                                                                                                                                                          |
| `EC:1.4.2.-`    |              1 | [GO:0016640](http://purl.obolibrary.org/obo/GO_0016640)                                                                                                                                                                                                                                          |
| `EC:1.4.4.-`    |              1 | [GO:0016642](http://purl.obolibrary.org/obo/GO_0016642)                                                                                                                                                                                                                                          |
| `EC:1.4.7.-`    |              1 | [GO:0016643](http://purl.obolibrary.org/obo/GO_0016643)                                                                                                                                                                                                                                          |
| `EC:1.5.-.-`    |              1 | [GO:0016645](http://purl.obolibrary.org/obo/GO_0016645)                                                                                                                                                                                                                                          |
| `EC:1.5.3.-`    |              1 | [GO:0016647](http://purl.obolibrary.org/obo/GO_0016647)                                                                                                                                                                                                                                          |
| `EC:1.5.4.-`    |              1 | [GO:0016648](http://purl.obolibrary.org/obo/GO_0016648)                                                                                                                                                                                                                                          |
| `EC:1.5.5.-`    |              1 | [GO:0016649](http://purl.obolibrary.org/obo/GO_0016649)                                                                                                                                                                                                                                          |
| `EC:1.6.-.-`    |              1 | [GO:0016651](http://purl.obolibrary.org/obo/GO_0016651)                                                                                                                                                                                                                                          |
| `EC:1.6.1.-`    |              1 | [GO:0016652](http://purl.obolibrary.org/obo/GO_0016652)                                                                                                                                                                                                                                          |
| `EC:1.6.2.-`    |              1 | [GO:0016653](http://purl.obolibrary.org/obo/GO_0016653)                                                                                                                                                                                                                                          |
| `EC:1.6.6.-`    |              1 | [GO:0016657](http://purl.obolibrary.org/obo/GO_0016657)                                                                                                                                                                                                                                          |
| `EC:1.7.-.-`    |              1 | [GO:0016661](http://purl.obolibrary.org/obo/GO_0016661)                                                                                                                                                                                                                                          |
| `EC:1.7.2.-`    |              1 | [GO:0016662](http://purl.obolibrary.org/obo/GO_0016662)                                                                                                                                                                                                                                          |
| `EC:1.7.3.-`    |              1 | [GO:0016663](http://purl.obolibrary.org/obo/GO_0016663)                                                                                                                                                                                                                                          |
| `EC:1.7.7.-`    |              1 | [GO:0016664](http://purl.obolibrary.org/obo/GO_0016664)                                                                                                                                                                                                                                          |
| `EC:1.8.-.-`    |              1 | [GO:0016667](http://purl.obolibrary.org/obo/GO_0016667)                                                                                                                                                                                                                                          |
| `EC:1.8.1.-`    |              1 | [GO:0016668](http://purl.obolibrary.org/obo/GO_0016668)                                                                                                                                                                                                                                          |
| `EC:1.8.2.-`    |              1 | [GO:0016669](http://purl.obolibrary.org/obo/GO_0016669)                                                                                                                                                                                                                                          |
| `EC:1.8.3.-`    |              1 | [GO:0016670](http://purl.obolibrary.org/obo/GO_0016670)                                                                                                                                                                                                                                          |
| `EC:1.8.4.-`    |              1 | [GO:0016671](http://purl.obolibrary.org/obo/GO_0016671)                                                                                                                                                                                                                                          |
| `EC:1.8.5.-`    |              1 | [GO:0016672](http://purl.obolibrary.org/obo/GO_0016672)                                                                                                                                                                                                                                          |
| `EC:1.8.7.-`    |              1 | [GO:0016673](http://purl.obolibrary.org/obo/GO_0016673)                                                                                                                                                                                                                                          |
| `EC:1.9.-.-`    |              1 | [GO:0016675](http://purl.obolibrary.org/obo/GO_0016675)                                                                                                                                                                                                                                          |
| `EC:1.9.3.-`    |              1 | [GO:0016676](http://purl.obolibrary.org/obo/GO_0016676)                                                                                                                                                                                                                                          |
| `EC:1.9.6.-`    |              1 | [GO:0016677](http://purl.obolibrary.org/obo/GO_0016677)                                                                                                                                                                                                                                          |
| `EC:1.10.-.-`   |              1 | [GO:0016679](http://purl.obolibrary.org/obo/GO_0016679)                                                                                                                                                                                                                                          |
| `EC:1.10.1.-`   |              1 | [GO:0016680](http://purl.obolibrary.org/obo/GO_0016680)                                                                                                                                                                                                                                          |
| `EC:1.10.2.-`   |              1 | [GO:0016681](http://purl.obolibrary.org/obo/GO_0016681)                                                                                                                                                                                                                                          |
| `EC:1.12.-.-`   |              1 | [GO:0016695](http://purl.obolibrary.org/obo/GO_0016695)                                                                                                                                                                                                                                          |
| `EC:1.12.1.-`   |              1 | [GO:0016696](http://purl.obolibrary.org/obo/GO_0016696)                                                                                                                                                                                                                                          |
| `EC:1.12.2.-`   |              1 | [GO:0016697](http://purl.obolibrary.org/obo/GO_0016697)                                                                                                                                                                                                                                          |
| `EC:1.12.7.-`   |              1 | [GO:0016699](http://purl.obolibrary.org/obo/GO_0016699)                                                                                                                                                                                                                                          |
| `EC:1.13.-.-`   |              1 | [GO:0016701](http://purl.obolibrary.org/obo/GO_0016701)                                                                                                                                                                                                                                          |
| `EC:1.14.16.-`  |              1 | [GO:0016714](http://purl.obolibrary.org/obo/GO_0016714)                                                                                                                                                                                                                                          |
| `EC:1.14.17.-`  |              1 | [GO:0016715](http://purl.obolibrary.org/obo/GO_0016715)                                                                                                                                                                                                                                          |
| `EC:1.15.-.-`   |              1 | [GO:0016721](http://purl.obolibrary.org/obo/GO_0016721)                                                                                                                                                                                                                                          |
| `EC:1.16.-.-`   |              1 | [GO:0016722](http://purl.obolibrary.org/obo/GO_0016722)                                                                                                                                                                                                                                          |
| `EC:1.16.3.-`   |              1 | [GO:0016724](http://purl.obolibrary.org/obo/GO_0016724)                                                                                                                                                                                                                                          |
| `EC:1.17.-.-`   |              1 | [GO:0016725](http://purl.obolibrary.org/obo/GO_0016725)                                                                                                                                                                                                                                          |
| `EC:1.17.3.-`   |              1 | [GO:0016727](http://purl.obolibrary.org/obo/GO_0016727)                                                                                                                                                                                                                                          |
| `EC:1.18.-.-`   |              1 | [GO:0016730](http://purl.obolibrary.org/obo/GO_0016730)                                                                                                                                                                                                                                          |
| `EC:1.18.1.-`   |              1 | [GO:0016731](http://purl.obolibrary.org/obo/GO_0016731)                                                                                                                                                                                                                                          |
| `EC:1.18.6.-`   |              1 | [GO:0016732](http://purl.obolibrary.org/obo/GO_0016732)                                                                                                                                                                                                                                          |
| `EC:1.19.-.-`   |              1 | [GO:0016737](http://purl.obolibrary.org/obo/GO_0016737)                                                                                                                                                                                                                                          |
| `EC:1.19.6.-`   |              1 | [GO:0016738](http://purl.obolibrary.org/obo/GO_0016738)                                                                                                                                                                                                                                          |
| `EC:2.1.-.-`    |              1 | [GO:0016741](http://purl.obolibrary.org/obo/GO_0016741)                                                                                                                                                                                                                                          |
| `EC:2.1.3.-`    |              1 | [GO:0016743](http://purl.obolibrary.org/obo/GO_0016743)                                                                                                                                                                                                                                          |
| `EC:2.3.-.-`    |              1 | [GO:0016746](http://purl.obolibrary.org/obo/GO_0016746)                                                                                                                                                                                                                                          |
| `EC:2.4.-.-`    |              1 | [GO:0016757](http://purl.obolibrary.org/obo/GO_0016757)                                                                                                                                                                                                                                          |
| `EC:2.6.-.-`    |              1 | [GO:0016769](http://purl.obolibrary.org/obo/GO_0016769)                                                                                                                                                                                                                                          |
| `EC:2.7.-.-`    |              1 | [GO:0016772](http://purl.obolibrary.org/obo/GO_0016772)                                                                                                                                                                                                                                          |
| `EC:2.7.6.-`    |              1 | [GO:0016778](http://purl.obolibrary.org/obo/GO_0016778)                                                                                                                                                                                                                                          |
| `EC:2.7.7.-`    |              1 | [GO:0016779](http://purl.obolibrary.org/obo/GO_0016779)                                                                                                                                                                                                                                          |
| `EC:2.8.-.-`    |              1 | [GO:0016782](http://purl.obolibrary.org/obo/GO_0016782)                                                                                                                                                                                                                                          |
| `EC:2.9.1.-`    |              1 | [GO:0016785](http://purl.obolibrary.org/obo/GO_0016785)                                                                                                                                                                                                                                          |
| `EC:3.-.-.-`    |              1 | [GO:0016787](http://purl.obolibrary.org/obo/GO_0016787)                                                                                                                                                                                                                                          |
| `EC:3.1.5.-`    |              1 | [GO:0016793](http://purl.obolibrary.org/obo/GO_0016793)                                                                                                                                                                                                                                          |
| `EC:3.1.7.-`    |              1 | [GO:0016794](http://purl.obolibrary.org/obo/GO_0016794)                                                                                                                                                                                                                                          |
| `EC:3.1.15.-`   |              1 | [GO:0016796](http://purl.obolibrary.org/obo/GO_0016796)                                                                                                                                                                                                                                          |
| `EC:3.1.16.-`   |              1 | [GO:0016797](http://purl.obolibrary.org/obo/GO_0016797)                                                                                                                                                                                                                                          |
| `EC:3.2.-.-`    |              1 | [GO:0016798](http://purl.obolibrary.org/obo/GO_0016798)                                                                                                                                                                                                                                          |
| `EC:3.3.-.-`    |              1 | [GO:0016801](http://purl.obolibrary.org/obo/GO_0016801)                                                                                                                                                                                                                                          |
| `EC:3.4.13.-`   |              1 | [GO:0016805](http://purl.obolibrary.org/obo/GO_0016805)                                                                                                                                                                                                                                          |
| `EC:3.4.14.-`   |              1 | [GO:0016806](http://purl.obolibrary.org/obo/GO_0016806)                                                                                                                                                                                                                                          |
| `EC:3.4.18.-`   |              1 | [GO:0016807](http://purl.obolibrary.org/obo/GO_0016807)                                                                                                                                                                                                                                          |
| `EC:3.5.-.-`    |              1 | [GO:0016810](http://purl.obolibrary.org/obo/GO_0016810)                                                                                                                                                                                                                                          |
| `EC:3.5.2.-`    |              1 | [GO:0016812](http://purl.obolibrary.org/obo/GO_0016812)                                                                                                                                                                                                                                          |
| `EC:3.5.3.-`    |              1 | [GO:0016813](http://purl.obolibrary.org/obo/GO_0016813)                                                                                                                                                                                                                                          |
| `EC:3.5.5.-`    |              1 | [GO:0016815](http://purl.obolibrary.org/obo/GO_0016815)                                                                                                                                                                                                                                          |
| `EC:3.6.-.-`    |              1 | [GO:0016817](http://purl.obolibrary.org/obo/GO_0016817)                                                                                                                                                                                                                                          |
| `EC:3.6.1.-`    |              1 | [GO:0016818](http://purl.obolibrary.org/obo/GO_0016818)                                                                                                                                                                                                                                          |
| `EC:3.6.2.-`    |              1 | [GO:0016819](http://purl.obolibrary.org/obo/GO_0016819)                                                                                                                                                                                                                                          |
| `EC:3.7.-.-`    |              1 | [GO:0016822](http://purl.obolibrary.org/obo/GO_0016822)                                                                                                                                                                                                                                          |
| `EC:3.8.-.-`    |              1 | [GO:0016824](http://purl.obolibrary.org/obo/GO_0016824)                                                                                                                                                                                                                                          |
| `EC:3.9.1.-`    |              1 | [GO:0016825](http://purl.obolibrary.org/obo/GO_0016825)                                                                                                                                                                                                                                          |
| `EC:3.10.-.-`   |              1 | [GO:0016826](http://purl.obolibrary.org/obo/GO_0016826)                                                                                                                                                                                                                                          |
| `EC:3.11.-.-`   |              1 | [GO:0016827](http://purl.obolibrary.org/obo/GO_0016827)                                                                                                                                                                                                                                          |
| `EC:3.12.-.-`   |              1 | [GO:0016828](http://purl.obolibrary.org/obo/GO_0016828)                                                                                                                                                                                                                                          |
| `EC:4.-.-.-`    |              1 | [GO:0016829](http://purl.obolibrary.org/obo/GO_0016829)                                                                                                                                                                                                                                          |
| `EC:4.1.2.-`    |              1 | [GO:0016832](http://purl.obolibrary.org/obo/GO_0016832)                                                                                                                                                                                                                                          |
| `EC:4.3.1.-`    |              1 | [GO:0016841](http://purl.obolibrary.org/obo/GO_0016841)                                                                                                                                                                                                                                          |
| `EC:4.3.2.-`    |              1 | [GO:0016842](http://purl.obolibrary.org/obo/GO_0016842)                                                                                                                                                                                                                                          |
| `EC:4.3.3.-`    |              1 | [GO:0016843](http://purl.obolibrary.org/obo/GO_0016843)                                                                                                                                                                                                                                          |
| `EC:4.5.-.-`    |              1 | [GO:0016848](http://purl.obolibrary.org/obo/GO_0016848)                                                                                                                                                                                                                                          |
| `EC:5.-.-.-`    |              1 | [GO:0016853](http://purl.obolibrary.org/obo/GO_0016853)                                                                                                                                                                                                                                          |
| `EC:5.1.-.-`    |              1 | [GO:0016854](http://purl.obolibrary.org/obo/GO_0016854)                                                                                                                                                                                                                                          |
| `EC:5.1.2.-`    |              1 | [GO:0016856](http://purl.obolibrary.org/obo/GO_0016856)                                                                                                                                                                                                                                          |
| `EC:5.2.-.-`    |              1 | [GO:0016859](http://purl.obolibrary.org/obo/GO_0016859)                                                                                                                                                                                                                                          |
| `EC:5.3.1.-`    |              1 | [GO:0016861](http://purl.obolibrary.org/obo/GO_0016861)                                                                                                                                                                                                                                          |
| `EC:5.3.2.-`    |              1 | [GO:0016862](http://purl.obolibrary.org/obo/GO_0016862)                                                                                                                                                                                                                                          |
| `EC:5.4.-.-`    |              1 | [GO:0016866](http://purl.obolibrary.org/obo/GO_0016866)                                                                                                                                                                                                                                          |
| `EC:5.4.2.-`    |              1 | [GO:0016868](http://purl.obolibrary.org/obo/GO_0016868)                                                                                                                                                                                                                                          |
| `EC:5.4.3.-`    |              1 | [GO:0016869](http://purl.obolibrary.org/obo/GO_0016869)                                                                                                                                                                                                                                          |
| `EC:6.-.-.-`    |              1 | [GO:0016874](http://purl.obolibrary.org/obo/GO_0016874)                                                                                                                                                                                                                                          |
| `EC:6.3.3.-`    |              1 | [GO:0016882](http://purl.obolibrary.org/obo/GO_0016882)                                                                                                                                                                                                                                          |
| `EC:3.1.21.-`   |              1 | [GO:0016888](http://purl.obolibrary.org/obo/GO_0016888)                                                                                                                                                                                                                                          |
| `EC:3.1.22.-`   |              1 | [GO:0016889](http://purl.obolibrary.org/obo/GO_0016889)                                                                                                                                                                                                                                          |
| `EC:3.1.27.-`   |              1 | [GO:0016892](http://purl.obolibrary.org/obo/GO_0016892)                                                                                                                                                                                                                                          |
| `EC:3.1.30.-`   |              1 | [GO:0016893](http://purl.obolibrary.org/obo/GO_0016893)                                                                                                                                                                                                                                          |
| `EC:3.1.14.-`   |              1 | [GO:0016897](http://purl.obolibrary.org/obo/GO_0016897)                                                                                                                                                                                                                                          |
| `EC:1.1.2.-`    |              1 | [GO:0016898](http://purl.obolibrary.org/obo/GO_0016898)                                                                                                                                                                                                                                          |
| `EC:1.1.4.-`    |              1 | [GO:0016900](http://purl.obolibrary.org/obo/GO_0016900)                                                                                                                                                                                                                                          |
| `EC:1.1.99.-`   |              1 | [GO:0018466](http://purl.obolibrary.org/obo/GO_0018466)                                                                                                                                                                                                                                          |
| `EC:1.13.99.-`  |              1 | [GO:0018584](http://purl.obolibrary.org/obo/GO_0018584)                                                                                                                                                                                                                                          |
| `EC:4.7.1.-`    |              1 | [GO:0018835](http://purl.obolibrary.org/obo/GO_0018835)                                                                                                                                                                                                                                          |
| `EC:3.8.1.-`    |              1 | [GO:0019120](http://purl.obolibrary.org/obo/GO_0019120)                                                                                                                                                                                                                                          |
| `EC:1.20.-.-`   |              1 | [GO:0030613](http://purl.obolibrary.org/obo/GO_0030613)                                                                                                                                                                                                                                          |
| `EC:1.20.4.-`   |              1 | [GO:0030614](http://purl.obolibrary.org/obo/GO_0030614)                                                                                                                                                                                                                                          |
| `EC:1.5.7.-`    |              1 | [GO:0033694](http://purl.obolibrary.org/obo/GO_0033694)                                                                                                                                                                                                                                          |
| `EC:3.13.1.-`   |              1 | [GO:0034861](http://purl.obolibrary.org/obo/GO_0034861)                                                                                                                                                                                                                                          |
| `EC:7.2.2.-`    |              1 | [GO:0042626](http://purl.obolibrary.org/obo/GO_0042626)                                                                                                                                                                                                                                          |
| `EC:1.2.99.-`   |              1 | [GO:0043794](http://purl.obolibrary.org/obo/GO_0043794)                                                                                                                                                                                                                                          |
| `EC:3.13.-.-`   |              1 | [GO:0046508](http://purl.obolibrary.org/obo/GO_0046508)                                                                                                                                                                                                                                          |
| `EC:1.7.1.-`    |              1 | [GO:0046857](http://purl.obolibrary.org/obo/GO_0046857)                                                                                                                                                                                                                                          |
| `EC:1.21.-.-`   |              1 | [GO:0046992](http://purl.obolibrary.org/obo/GO_0046992)                                                                                                                                                                                                                                          |
| `EC:1.12.5.-`   |              1 | [GO:0046994](http://purl.obolibrary.org/obo/GO_0046994)                                                                                                                                                                                                                                          |
| `EC:1.12.98.-`  |              1 | [GO:0046995](http://purl.obolibrary.org/obo/GO_0046995)                                                                                                                                                                                                                                          |
| `EC:1.5.8.-`    |              1 | [GO:0046997](http://purl.obolibrary.org/obo/GO_0046997)                                                                                                                                                                                                                                          |
| `EC:1.21.4.-`   |              1 | [GO:0050485](http://purl.obolibrary.org/obo/GO_0050485)                                                                                                                                                                                                                                          |
| `EC:2.8.4.-`    |              1 | [GO:0050497](http://purl.obolibrary.org/obo/GO_0050497)                                                                                                                                                                                                                                          |
| `EC:1.14.20.-`  |              1 | [GO:0050498](http://purl.obolibrary.org/obo/GO_0050498)                                                                                                                                                                                                                                          |
| `EC:1.20.1.-`   |              1 | [GO:0050499](http://purl.obolibrary.org/obo/GO_0050499)                                                                                                                                                                                                                                          |
| `EC:1.20.98.-`  |              1 | [GO:0050522](http://purl.obolibrary.org/obo/GO_0050522)                                                                                                                                                                                                                                          |
| `EC:1.22.-.-`   |              1 | [GO:0052583](http://purl.obolibrary.org/obo/GO_0052583)                                                                                                                                                                                                                                          |
| `EC:1.22.1.-`   |              1 | [GO:0052584](http://purl.obolibrary.org/obo/GO_0052584)                                                                                                                                                                                                                                          |
| `EC:1.4.5.-`    |              1 | [GO:0052585](http://purl.obolibrary.org/obo/GO_0052585)                                                                                                                                                                                                                                          |
| `EC:1.7.5.-`    |              1 | [GO:0052586](http://purl.obolibrary.org/obo/GO_0052586)                                                                                                                                                                                                                                          |
| `EC:1.17.7.-`   |              1 | [GO:0052592](http://purl.obolibrary.org/obo/GO_0052592)                                                                                                                                                                                                                                          |
| `EC:1.4.9.-`    |              1 | [GO:0052877](http://purl.obolibrary.org/obo/GO_0052877)                                                                                                                                                                                                                                          |
| `EC:1.10.9.-`   |              1 | [GO:0052880](http://purl.obolibrary.org/obo/GO_0052880)                                                                                                                                                                                                                                          |
| `EC:1.20.9.-`   |              1 | [GO:0052882](http://purl.obolibrary.org/obo/GO_0052882)                                                                                                                                                                                                                                          |
| `EC:7.2.-.-`    |              1 | [GO:0106179](http://purl.obolibrary.org/obo/GO_0106179)                                                                                                                                                                                                                                          |
| `EC:7.1.-.-`    |              1 | [GO:0106180](http://purl.obolibrary.org/obo/GO_0106180)                                                                                                                                                                                                                                          |
| `EC:7.3.-.-`    |              1 | [GO:0106181](http://purl.obolibrary.org/obo/GO_0106181)                                                                                                                                                                                                                                          |
| `EC:7.4.-.-`    |              1 | [GO:0106182](http://purl.obolibrary.org/obo/GO_0106182)                                                                                                                                                                                                                                          |
| `EC:7.5.-.-`    |              1 | [GO:0106183](http://purl.obolibrary.org/obo/GO_0106183)                                                                                                                                                                                                                                          |
| `EC:7.6.-.-`    |              1 | [GO:0106184](http://purl.obolibrary.org/obo/GO_0106184)                                                                                                                                                                                                                                          |
| `EC:7.1.1.-`    |              1 | [GO:0106187](http://purl.obolibrary.org/obo/GO_0106187)                                                                                                                                                                                                                                          |
| `EC:7.1.2.-`    |              1 | [GO:0106188](http://purl.obolibrary.org/obo/GO_0106188)                                                                                                                                                                                                                                          |
| `EC:7.1.3.-`    |              1 | [GO:0106189](http://purl.obolibrary.org/obo/GO_0106189)                                                                                                                                                                                                                                          |
| `EC:7.1.4.-`    |              1 | [GO:0106190](http://purl.obolibrary.org/obo/GO_0106190)                                                                                                                                                                                                                                          |
| `EC:7.2.1.-`    |              1 | [GO:0106191](http://purl.obolibrary.org/obo/GO_0106191)                                                                                                                                                                                                                                          |
| `EC:7.2.3.-`    |              1 | [GO:0106193](http://purl.obolibrary.org/obo/GO_0106193)                                                                                                                                                                                                                                          |
| `EC:7.2.4.-`    |              1 | [GO:0106194](http://purl.obolibrary.org/obo/GO_0106194)                                                                                                                                                                                                                                          |
| `EC:7.3.1.-`    |              1 | [GO:0106195](http://purl.obolibrary.org/obo/GO_0106195)                                                                                                                                                                                                                                          |
| `EC:7.3.2.-`    |              1 | [GO:0106196](http://purl.obolibrary.org/obo/GO_0106196)                                                                                                                                                                                                                                          |
| `EC:7.3.3.-`    |              1 | [GO:0106197](http://purl.obolibrary.org/obo/GO_0106197)                                                                                                                                                                                                                                          |
| `EC:7.3.4.-`    |              1 | [GO:0106198](http://purl.obolibrary.org/obo/GO_0106198)                                                                                                                                                                                                                                          |
| `EC:7.4.1.-`    |              1 | [GO:0106199](http://purl.obolibrary.org/obo/GO_0106199)                                                                                                                                                                                                                                          |
| `EC:7.4.2.-`    |              1 | [GO:0106200](http://purl.obolibrary.org/obo/GO_0106200)                                                                                                                                                                                                                                          |
| `EC:7.4.3.-`    |              1 | [GO:0106201](http://purl.obolibrary.org/obo/GO_0106201)                                                                                                                                                                                                                                          |
| `EC:7.4.4.-`    |              1 | [GO:0106202](http://purl.obolibrary.org/obo/GO_0106202)                                                                                                                                                                                                                                          |
| `EC:4.3.99.-`   |              1 | [GO:0140740](http://purl.obolibrary.org/obo/GO_0140740)                                                                                                                                                                                                                                          |

## `ECO`: Evidence ontology

Overall, there were 11 invalid
xrefs to external prefixed with `ECO` (standardized to Bioregistry
prefix [`eco`](https://bioregistry.io/eco)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ECO:RCT`       |              9 | [ECO:0007636](http://purl.obolibrary.org/obo/ECO_0007636), [ECO:0007638](http://purl.obolibrary.org/obo/ECO_0007638), [ECO:0007639](http://purl.obolibrary.org/obo/ECO_0007639), [ECO:0007640](http://purl.obolibrary.org/obo/ECO_0007640), [ECO:0007642](http://purl.obolibrary.org/obo/ECO_0007642), ... |
| `ECO:MCC`       |              1 | [ECO:0000000](http://purl.obolibrary.org/obo/ECO_0000000)                                                                                                                                                                                                                                                  |
| `ECO:00000060`  |              1 | [RO:HOM0000017](http://purl.obolibrary.org/obo/RO_HOM0000017)                                                                                                                                                                                                                                              |

## `EMAPA`: Mouse Developmental Anatomy Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `EMAPA` (standardized to Bioregistry
prefix [`emapa`](https://bioregistry.io/emapa)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `EMAPA:th`      |              1 | [UBERON:0001638](http://purl.obolibrary.org/obo/UBERON_0001638) |

## `EnvO`: Environment Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `EnvO` (standardized to Bioregistry
prefix [`envo`](https://bioregistry.io/envo)) that
did not match the standard pattern `^\d{7,8}$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `EnvO:EnvO`     |              1 | [ENVO:01000739](http://purl.obolibrary.org/obo/ENVO_01000739) |

## `ENVO`: Environment Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `ENVO` (standardized to Bioregistry
prefix [`envo`](https://bioregistry.io/envo)) that
did not match the standard pattern `^\d{7,8}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ENVO:pb`       |              3 | [PATO:0015017](http://purl.obolibrary.org/obo/PATO_0015017), [PATO:0015018](http://purl.obolibrary.org/obo/PATO_0015018), [PATO:0015029](http://purl.obolibrary.org/obo/PATO_0015029) |

## `FB`: FlyBase Gene

Overall, there were 64 invalid
xrefs to external prefixed with `FB` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref         |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-----------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FB:reference_manual` |             24 | [SO:0000062](http://purl.obolibrary.org/obo/SO_0000062), [SO:0000453](http://purl.obolibrary.org/obo/SO_0000453), [SO:0001784](http://purl.obolibrary.org/obo/SO_0001784), [SO:1000044](http://purl.obolibrary.org/obo/SO_1000044), [SO:1000046](http://purl.obolibrary.org/obo/SO_1000046), ...                                         |
| `FB:ma`               |             14 | [CL:0000066](http://purl.obolibrary.org/obo/CL_0000066), [CL:0000134](http://purl.obolibrary.org/obo/CL_0000134), [CL:0000183](http://purl.obolibrary.org/obo/CL_0000183), [CL:0000211](http://purl.obolibrary.org/obo/CL_0000211), [CL:0000219](http://purl.obolibrary.org/obo/CL_0000219), ...                                         |
| `FB:gg`               |              7 | [UBERON:0000018](http://purl.obolibrary.org/obo/UBERON_0000018), [UBERON:0000914](http://purl.obolibrary.org/obo/UBERON_0000914), [UBERON:0000918](http://purl.obolibrary.org/obo/UBERON_0000918), [UBERON:0000972](http://purl.obolibrary.org/obo/UBERON_0000972), [UBERON:0000984](http://purl.obolibrary.org/obo/UBERON_0000984), ... |
| `FB:km`               |              6 | [SO:0000461](http://purl.obolibrary.org/obo/SO_0000461), [SO:0000465](http://purl.obolibrary.org/obo/SO_0000465), [SO:0000512](http://purl.obolibrary.org/obo/SO_0000512), [SO:0000547](http://purl.obolibrary.org/obo/SO_0000547), [SO:0000549](http://purl.obolibrary.org/obo/SO_0000549), ...                                         |
| `FB:mc`               |              4 | [SO:0000796](http://purl.obolibrary.org/obo/SO_0000796), [SO:0000797](http://purl.obolibrary.org/obo/SO_0000797), [SO:0000798](http://purl.obolibrary.org/obo/SO_0000798), [SO:0000799](http://purl.obolibrary.org/obo/SO_0000799)                                                                                                       |
| `FB:gm`               |              4 | [SO:0000800](http://purl.obolibrary.org/obo/SO_0000800), [SO:0000801](http://purl.obolibrary.org/obo/SO_0000801), [SO:0000802](http://purl.obolibrary.org/obo/SO_0000802), [SO:0000803](http://purl.obolibrary.org/obo/SO_0000803)                                                                                                       |
| `FB:manual`           |              2 | [SO:1000142](http://purl.obolibrary.org/obo/SO_1000142), [SO:1000143](http://purl.obolibrary.org/obo/SO_1000143)                                                                                                                                                                                                                         |
| `FB:WG`               |              1 | [SO:0000719](http://purl.obolibrary.org/obo/SO_0000719)                                                                                                                                                                                                                                                                                  |
| `FB:cds`              |              1 | [SO:0000934](http://purl.obolibrary.org/obo/SO_0000934)                                                                                                                                                                                                                                                                                  |
| `FB:DJS`              |              1 | [UBERON:0001048](http://purl.obolibrary.org/obo/UBERON_0001048)                                                                                                                                                                                                                                                                          |

## `Flybase`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `Flybase` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `Flybase:dsj`   |              1 | [CL:0000362](http://purl.obolibrary.org/obo/CL_0000362) |

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

## `GC`: Genetic Code

Overall, there were 1 invalid
xrefs to external prefixed with `GC` (standardized to Bioregistry
prefix [`gc`](https://bioregistry.io/gc)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `GC:tfm`        |              1 | [CL:0002597](http://purl.obolibrary.org/obo/CL_0002597) |

## `Gmelin`: Gmelins Handbuch der anorganischen Chemie

Overall, there were 26 invalid
xrefs to external prefixed with `Gmelin` (standardized to Bioregistry
prefix [`gmelin`](https://bioregistry.io/gmelin)) that
did not match the standard pattern `^[1-9][0-9]{3,6}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `Gmelin:117`    |              1 | [CHEBI:15377](http://purl.obolibrary.org/obo/CHEBI_15377) |
| `Gmelin:485`    |              1 | [CHEBI:15379](http://purl.obolibrary.org/obo/CHEBI_15379) |
| `Gmelin:897`    |              1 | [CHEBI:15862](http://purl.obolibrary.org/obo/CHEBI_15862) |
| `Gmelin:79`     |              1 | [CHEBI:16134](http://purl.obolibrary.org/obo/CHEBI_16134) |
| `Gmelin:303`    |              1 | [CHEBI:16136](http://purl.obolibrary.org/obo/CHEBI_16136) |
| `Gmelin:59`     |              1 | [CHEBI:16183](http://purl.obolibrary.org/obo/CHEBI_16183) |
| `Gmelin:787`    |              1 | [CHEBI:16236](http://purl.obolibrary.org/obo/CHEBI_16236) |
| `Gmelin:509`    |              1 | [CHEBI:16240](http://purl.obolibrary.org/obo/CHEBI_16240) |
| `Gmelin:977`    |              1 | [CHEBI:16301](http://purl.obolibrary.org/obo/CHEBI_16301) |
| `Gmelin:451`    |              1 | [CHEBI:16480](http://purl.obolibrary.org/obo/CHEBI_16480) |
| `Gmelin:989`    |              1 | [CHEBI:16526](http://purl.obolibrary.org/obo/CHEBI_16526) |
| `Gmelin:421`    |              1 | [CHEBI:17245](http://purl.obolibrary.org/obo/CHEBI_17245) |
| `Gmelin:89`     |              1 | [CHEBI:17514](http://purl.obolibrary.org/obo/CHEBI_17514) |
| `Gmelin:449`    |              1 | [CHEBI:17790](http://purl.obolibrary.org/obo/CHEBI_17790) |
| `Gmelin:322`    |              1 | [CHEBI:17883](http://purl.obolibrary.org/obo/CHEBI_17883) |
| `Gmelin:983`    |              1 | [CHEBI:25567](http://purl.obolibrary.org/obo/CHEBI_25567) |
| `Gmelin:676`    |              1 | [CHEBI:27561](http://purl.obolibrary.org/obo/CHEBI_27561) |
| `Gmelin:84`     |              1 | [CHEBI:28938](http://purl.obolibrary.org/obo/CHEBI_28938) |
| `Gmelin:507`    |              1 | [CHEBI:29192](http://purl.obolibrary.org/obo/CHEBI_29192) |
| `Gmelin:141`    |              1 | [CHEBI:29412](http://purl.obolibrary.org/obo/CHEBI_29412) |
| `Gmelin:773`    |              1 | [CHEBI:29449](http://purl.obolibrary.org/obo/CHEBI_29449) |
| `Gmelin:508`    |              1 | [CHEBI:29793](http://purl.obolibrary.org/obo/CHEBI_29793) |
| `Gmelin:307`    |              1 | [CHEBI:30488](http://purl.obolibrary.org/obo/CHEBI_30488) |
| `Gmelin:113`    |              1 | [CHEBI:36856](http://purl.obolibrary.org/obo/CHEBI_36856) |
| `Gmelin:620`    |              1 | [CHEBI:47266](http://purl.obolibrary.org/obo/CHEBI_47266) |
| `Gmelin:331`    |              1 | [CHEBI:50315](http://purl.obolibrary.org/obo/CHEBI_50315) |

## `GO`: Gene Ontology

Overall, there were 43 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                  |
|-----------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:jl`         |             12 | [GO:0044092](http://purl.obolibrary.org/obo/GO_0044092), [GO:0044093](http://purl.obolibrary.org/obo/GO_0044093), [GO:0044110](http://purl.obolibrary.org/obo/GO_0044110), [GO:0044111](http://purl.obolibrary.org/obo/GO_0044111), [GO:0044113](http://purl.obolibrary.org/obo/GO_0044113), ...                        |
| `GO:tfm`        |              5 | [CL:0000482](http://purl.obolibrary.org/obo/CL_0000482), [CL:0000506](http://purl.obolibrary.org/obo/CL_0000506), [CL:0000507](http://purl.obolibrary.org/obo/CL_0000507), [CL:0000509](http://purl.obolibrary.org/obo/CL_0000509), [CL:0000511](http://purl.obolibrary.org/obo/CL_0000511)                             |
| `GO:GO`         |              5 | [PATO:0001440](http://purl.obolibrary.org/obo/PATO_0001440), [PATO:0001441](http://purl.obolibrary.org/obo/PATO_0001441), [PATO:0001720](http://purl.obolibrary.org/obo/PATO_0001720), [UBERON:0000016](http://purl.obolibrary.org/obo/UBERON_0000016), [UBERON:0006003](http://purl.obolibrary.org/obo/UBERON_0006003) |
| `GO:kmv`        |              3 | [GO:1901074](http://purl.obolibrary.org/obo/GO_1901074), [GO:1901075](http://purl.obolibrary.org/obo/GO_1901075), [GO:1901076](http://purl.obolibrary.org/obo/GO_1901076)                                                                                                                                               |
| `GO:mah`        |              3 | [SO:0001861](http://purl.obolibrary.org/obo/SO_0001861), [SO:0001861](http://purl.obolibrary.org/obo/SO_0001861), [SO:0001871](http://purl.obolibrary.org/obo/SO_0001871)                                                                                                                                               |
| `GO:dos`        |              2 | [GO:0099046](http://purl.obolibrary.org/obo/GO_0099046), [GO:0099047](http://purl.obolibrary.org/obo/GO_0099047)                                                                                                                                                                                                        |
| `GO:dph`        |              2 | [GO:0002093](http://purl.obolibrary.org/obo/GO_0002093), [UBERON:0000089](http://purl.obolibrary.org/obo/UBERON_0000089)                                                                                                                                                                                                |
| `GO:cvs`        |              1 | [CL:0005008](http://purl.obolibrary.org/obo/CL_0005008)                                                                                                                                                                                                                                                                 |
| `GO:hjd`        |              1 | [GO:0002189](http://purl.obolibrary.org/obo/GO_0002189)                                                                                                                                                                                                                                                                 |
| `GO:bf`         |              1 | [GO:0035348](http://purl.obolibrary.org/obo/GO_0035348)                                                                                                                                                                                                                                                                 |
| `GO:sl`         |              1 | [GO:0035364](http://purl.obolibrary.org/obo/GO_0035364)                                                                                                                                                                                                                                                                 |
| `GO:add`        |              1 | [GO:0035525](http://purl.obolibrary.org/obo/GO_0035525)                                                                                                                                                                                                                                                                 |
| `GO:bhm`        |              1 | [GO:0140091](http://purl.obolibrary.org/obo/GO_0140091)                                                                                                                                                                                                                                                                 |
| `GO:bc`         |              1 | [GO:0150014](http://purl.obolibrary.org/obo/GO_0150014)                                                                                                                                                                                                                                                                 |
| `GO:curator`    |              1 | [UBERON:0005863](http://purl.obolibrary.org/obo/UBERON_0005863)                                                                                                                                                                                                                                                         |
| `GO:curators`   |              1 | [GO:0004479](http://purl.obolibrary.org/obo/GO_0004479)                                                                                                                                                                                                                                                                 |
| `GO:krc`        |              1 | [GO:0120132](http://purl.obolibrary.org/obo/GO_0120132)                                                                                                                                                                                                                                                                 |
| `GO:ach`        |              1 | [GO:0120312](http://purl.obolibrary.org/obo/GO_0120312)                                                                                                                                                                                                                                                                 |

## `GOA`: Gene Ontology Annotation Database

Overall, there were 38 invalid
xrefs to external prefixed with `GOA` (standardized to Bioregistry
prefix [`goa`](https://bioregistry.io/goa)) that
did not match the standard pattern `^(([A-N,R-Z][0-9][A-Z][A-Z, 0-9][A-Z, 0-9][0-9])|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9]))|(URS[0-9A-F]{10}(_[0-9]+){0,1})|(EBI-[0-9]+)$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GOA:UniProtKB` |             19 | [PR:000026262](http://purl.obolibrary.org/obo/PR_000026262), [PR:000026264](http://purl.obolibrary.org/obo/PR_000026264), [PR:000026266](http://purl.obolibrary.org/obo/PR_000026266), [PR:000026268](http://purl.obolibrary.org/obo/PR_000026268), [PR:000026281](http://purl.obolibrary.org/obo/PR_000026281), ... |
| `GOA:IntAct`    |             15 | [PR:000026246](http://purl.obolibrary.org/obo/PR_000026246), [PR:000026256](http://purl.obolibrary.org/obo/PR_000026256), [PR:000026258](http://purl.obolibrary.org/obo/PR_000026258), [PR:000026260](http://purl.obolibrary.org/obo/PR_000026260), [PR:000026277](http://purl.obolibrary.org/obo/PR_000026277), ... |
| `GOA:BHF-UCL`   |              3 | [PR:000026248](http://purl.obolibrary.org/obo/PR_000026248), [PR:000026250](http://purl.obolibrary.org/obo/PR_000026250), [PR:000026252](http://purl.obolibrary.org/obo/PR_000026252)                                                                                                                                |
| `GOA:als`       |              1 | [GO:1903985](http://purl.obolibrary.org/obo/GO_1903985)                                                                                                                                                                                                                                                              |

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

## `HGNC`: HUGO Gene Nomenclature Committee

Overall, there were 1 invalid
xrefs to external prefixed with `HGNC` (standardized to Bioregistry
prefix [`hgnc`](https://bioregistry.io/hgnc)) that
did not match the standard pattern `^\d{1,5}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `HGNC:mw`       |              1 | [SO:0001877](http://purl.obolibrary.org/obo/SO_0001877) |

## `HPA`: Human Protein Atlas tissue profile information

Overall, there were 6 invalid
xrefs to external prefixed with `HPA` (standardized to Bioregistry
prefix [`hpa`](https://bioregistry.io/hpa)) that
did not match the standard pattern `^ENSG\d{11}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HPA:HPA`       |              6 | [CL:1001586](http://purl.obolibrary.org/obo/CL_1001586), [CL:1001591](http://purl.obolibrary.org/obo/CL_1001591), [CL:1001593](http://purl.obolibrary.org/obo/CL_1001593), [CL:1001596](http://purl.obolibrary.org/obo/CL_1001596), [CL:1001599](http://purl.obolibrary.org/obo/CL_1001599), ... |

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

## `ICD10CM`: International Classification of Diseases, 10th Revision, Clinical Modification

Overall, there were 2 invalid
xrefs to external prefixed with `ICD10CM` (standardized to Bioregistry
prefix [`icd10cm`](https://bioregistry.io/icd10cm)) that
did not match the standard pattern `^([A-Z][0-9][0-9AB]((-[A-Z][0-9][0-9AB])|(\.[0-9A-KXZ]([0-9A-EXYZ]([0-9A-HX][0-59A-HJKMNP-S]?)?)?)?))$`.

| external_xref    |   usages_count | usages                                                      |
|------------------|----------------|-------------------------------------------------------------|
| `ICD10CM:E74.0+` |              1 | [DOID:0090101](http://purl.obolibrary.org/obo/DOID_0090101) |
| `ICD10CM:G73.6*` |              1 | [DOID:0090101](http://purl.obolibrary.org/obo/DOID_0090101) |

## `ICD11`: International Classification of Diseases, 11th Revision

Overall, there were 1 invalid
xrefs to external prefixed with `ICD11` (standardized to Bioregistry
prefix [`icd11`](https://bioregistry.io/icd11)) that
did not match the standard pattern `^[1-9]\d*$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `ICD11:4B24`    |              1 | [DOID:0081267](http://purl.obolibrary.org/obo/DOID_0081267) |

## `ICD9CM`: International Classification of Diseases, 9th Revision, Clinical Modification

Overall, there were 13 invalid
xrefs to external prefixed with `ICD9CM` (standardized to Bioregistry
prefix [`icd9cm`](https://bioregistry.io/icd9cm)) that
did not match the standard pattern `^([\dA-Z]\d{2}(\.\d{1,3}|))|(\d{2}(\.\d{1,2}|))$`.

| external_xref       |   usages_count | usages                                                  |
|---------------------|----------------|---------------------------------------------------------|
| `ICD9CM:001-009.99` |              1 | [DOID:100](http://purl.obolibrary.org/obo/DOID_100)     |
| `ICD9CM:401-405.99` |              1 | [DOID:10763](http://purl.obolibrary.org/obo/DOID_10763) |
| `ICD9CM:110-118.99` |              1 | [DOID:1564](http://purl.obolibrary.org/obo/DOID_1564)   |
| `ICD9CM:390-392.99` |              1 | [DOID:1586](http://purl.obolibrary.org/obo/DOID_1586)   |
| `ICD9CM:209-209.99` |              1 | [DOID:169](http://purl.obolibrary.org/obo/DOID_169)     |
| `ICD9CM:410-414.99` |              1 | [DOID:3393](http://purl.obolibrary.org/obo/DOID_3393)   |
| `ICD9CM:610-612.99` |              1 | [DOID:3463](http://purl.obolibrary.org/obo/DOID_3463)   |
| `ICD9CM:042-042.99` |              1 | [DOID:526](http://purl.obolibrary.org/obo/DOID_526)     |
| `ICD9CM:520-579.99` |              1 | [DOID:77](http://purl.obolibrary.org/obo/DOID_77)       |
| `ICD9CM:540-543.99` |              1 | [DOID:8337](http://purl.obolibrary.org/obo/DOID_8337)   |
| `ICD9CM:230-234.99` |              1 | [DOID:8719](http://purl.obolibrary.org/obo/DOID_8719)   |
| `ICD9CM:120-129.99` |              1 | [DOID:883](http://purl.obolibrary.org/obo/DOID_883)     |
| `ICD9CM:060-066.99` |              1 | [DOID:934](http://purl.obolibrary.org/obo/DOID_934)     |

## `ICDO`: International Classification of Diseases for Oncology

Overall, there were 2 invalid
xrefs to external prefixed with `ICDO` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref   |   usages_count | usages                                                |
|-----------------|----------------|-------------------------------------------------------|
| `ICDO:8480/6`   |              1 | [DOID:3559](http://purl.obolibrary.org/obo/DOID_3559) |
| `ICDO:8800/9`   |              1 | [DOID:7615](http://purl.obolibrary.org/obo/DOID_7615) |

## `IEDB`: Immune Epitope Database

Overall, there were 1 invalid
xrefs to external prefixed with `IEDB` (standardized to Bioregistry
prefix [`iedb`](https://bioregistry.io/iedb)) that
did not match the standard pattern `^[0-9]+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `IEDB:BP`       |              1 | [PR:000000001](http://purl.obolibrary.org/obo/PR_000000001) |

## `ISBN`: International Standard Book Number

Overall, there were 1 invalid
xrefs to external prefixed with `ISBN` (standardized to Bioregistry
prefix [`isbn`](https://bioregistry.io/isbn)) that
did not match the standard pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`.

| external_xref                   |   usages_count | usages                                                          |
|---------------------------------|----------------|-----------------------------------------------------------------|
| `ISBN:9004086161,9789004086166` |              1 | [UBERON:7500120](http://purl.obolibrary.org/obo/UBERON_7500120) |

## `ISSN`: International Standard Serial Number

Overall, there were 16 invalid
xrefs to external prefixed with `ISSN` (standardized to Bioregistry
prefix [`issn`](https://bioregistry.io/issn)) that
did not match the standard pattern `^\d{4}-\d{3}[\dX]$`.

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|----------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ISSN:15518507`      |              9 | [GO:0060102](http://purl.obolibrary.org/obo/GO_0060102), [GO:0060104](http://purl.obolibrary.org/obo/GO_0060104), [GO:0060105](http://purl.obolibrary.org/obo/GO_0060105), [GO:0060106](http://purl.obolibrary.org/obo/GO_0060106), [GO:0060107](http://purl.obolibrary.org/obo/GO_0060107), ... |
| `ISSN:09498257`      |              6 | [GO:0006777](http://purl.obolibrary.org/obo/GO_0006777), [GO:0019720](http://purl.obolibrary.org/obo/GO_0019720), [GO:0042046](http://purl.obolibrary.org/obo/GO_0042046), [GO:0042047](http://purl.obolibrary.org/obo/GO_0042047), [GO:0043545](http://purl.obolibrary.org/obo/GO_0043545), ... |
| `ISSN:9781496335418` |              1 | [PATO:0001744](http://purl.obolibrary.org/obo/PATO_0001744)                                                                                                                                                                                                                                      |

## `JAX`: Jackson Laboratories Strain

Overall, there were 2 invalid
xrefs to external prefixed with `JAX` (standardized to Bioregistry
prefix [`jax`](https://bioregistry.io/jax)) that
did not match the standard pattern `^\d{6}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `JAX:hdene`     |              1 | [SO:0001500](http://purl.obolibrary.org/obo/SO_0001500) |
| `JAX:hd`        |              1 | [SO:0001841](http://purl.obolibrary.org/obo/SO_0001841) |

## `KEGG`: Kyoto Encyclopedia of Genes and Genomes

Overall, there were 36 invalid
xrefs to external prefixed with `KEGG` (standardized to Bioregistry
prefix [`kegg`](https://bioregistry.io/kegg)) that
did not match the standard pattern `^([CHDEGTMKR]\d+)|(\w+:[\w\d\.-]*)|([a-z]{3,5})|(\w{2,4}\d{5})$`.

| external_xref   |   usages_count | usages                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------|
| `KEGG:05321`    |              2 | [DOID:0050589](http://purl.obolibrary.org/obo/DOID_0050589), [DOID:9778](http://purl.obolibrary.org/obo/DOID_9778) |
| `KEGG:05215`    |              2 | [DOID:10283](http://purl.obolibrary.org/obo/DOID_10283), [DOID:10286](http://purl.obolibrary.org/obo/DOID_10286)   |
| `KEGG:04950`    |              1 | [DOID:0050524](http://purl.obolibrary.org/obo/DOID_0050524)                                                        |
| `KEGG:05034`    |              1 | [DOID:0050741](http://purl.obolibrary.org/obo/DOID_0050741)                                                        |
| `KEGG:05143`    |              1 | [DOID:10112](http://purl.obolibrary.org/obo/DOID_10112)                                                            |
| `KEGG:05010`    |              1 | [DOID:10652](http://purl.obolibrary.org/obo/DOID_10652)                                                            |
| `KEGG:05219`    |              1 | [DOID:11054](http://purl.obolibrary.org/obo/DOID_11054)                                                            |
| `KEGG:05133`    |              1 | [DOID:1116](http://purl.obolibrary.org/obo/DOID_1116)                                                              |
| `KEGG:05410`    |              1 | [DOID:11984](http://purl.obolibrary.org/obo/DOID_11984)                                                            |
| `KEGG:05142`    |              1 | [DOID:12140](http://purl.obolibrary.org/obo/DOID_12140)                                                            |
| `KEGG:05131`    |              1 | [DOID:12385](http://purl.obolibrary.org/obo/DOID_12385)                                                            |
| `KEGG:05016`    |              1 | [DOID:12858](http://purl.obolibrary.org/obo/DOID_12858)                                                            |
| `KEGG:05414`    |              1 | [DOID:12930](http://purl.obolibrary.org/obo/DOID_12930)                                                            |
| `KEGG:05213`    |              1 | [DOID:1380](http://purl.obolibrary.org/obo/DOID_1380)                                                              |
| `KEGG:05012`    |              1 | [DOID:14330](http://purl.obolibrary.org/obo/DOID_14330)                                                            |
| `KEGG:05216`    |              1 | [DOID:1781](http://purl.obolibrary.org/obo/DOID_1781)                                                              |
| `KEGG:05212`    |              1 | [DOID:1793](http://purl.obolibrary.org/obo/DOID_1793)                                                              |
| `KEGG:05218`    |              1 | [DOID:1909](http://purl.obolibrary.org/obo/DOID_1909)                                                              |
| `KEGG:05217`    |              1 | [DOID:2513](http://purl.obolibrary.org/obo/DOID_2513)                                                              |
| `KEGG:05310`    |              1 | [DOID:2841](http://purl.obolibrary.org/obo/DOID_2841)                                                              |
| `KEGG:05214`    |              1 | [DOID:3070](http://purl.obolibrary.org/obo/DOID_3070)                                                              |
| `KEGG:05014`    |              1 | [DOID:332](http://purl.obolibrary.org/obo/DOID_332)                                                                |
| `KEGG:05223`    |              1 | [DOID:3908](http://purl.obolibrary.org/obo/DOID_3908)                                                              |
| `KEGG:05222`    |              1 | [DOID:5409](http://purl.obolibrary.org/obo/DOID_5409)                                                              |
| `KEGG:05340`    |              1 | [DOID:612](http://purl.obolibrary.org/obo/DOID_612)                                                                |
| `KEGG:05020`    |              1 | [DOID:649](http://purl.obolibrary.org/obo/DOID_649)                                                                |
| `KEGG:05323`    |              1 | [DOID:7148](http://purl.obolibrary.org/obo/DOID_7148)                                                              |
| `KEGG:05416`    |              1 | [DOID:820](http://purl.obolibrary.org/obo/DOID_820)                                                                |
| `KEGG:05220`    |              1 | [DOID:8552](http://purl.obolibrary.org/obo/DOID_8552)                                                              |
| `KEGG:05322`    |              1 | [DOID:9074](http://purl.obolibrary.org/obo/DOID_9074)                                                              |
| `KEGG:05221`    |              1 | [DOID:9119](http://purl.obolibrary.org/obo/DOID_9119)                                                              |
| `KEGG:05210`    |              1 | [DOID:9256](http://purl.obolibrary.org/obo/DOID_9256)                                                              |
| `KEGG:04930`    |              1 | [DOID:9352](http://purl.obolibrary.org/obo/DOID_9352)                                                              |
| `KEGG:04940`    |              1 | [DOID:9744](http://purl.obolibrary.org/obo/DOID_9744)                                                              |

## `KEGG COMPOUND`: KEGG Compound

Overall, there were 2 invalid
xrefs to external prefixed with `KEGG COMPOUND` (standardized to Bioregistry
prefix [`kegg.compound`](https://bioregistry.io/kegg.compound)) that
did not match the standard pattern `^C\d+$`.

| external_xref             |   usages_count | usages                                                    |
|---------------------------|----------------|-----------------------------------------------------------|
| `KEGG COMPOUND:87-51-4`   |              1 | [CHEBI:16411](http://purl.obolibrary.org/obo/CHEBI_16411) |
| `KEGG COMPOUND:6894-38-8` |              1 | [CHEBI:18292](http://purl.obolibrary.org/obo/CHEBI_18292) |

## `KUPO`: Kidney and Urinary Pathway Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `KUPO` (standardized to Bioregistry
prefix [`kupo`](https://bioregistry.io/kupo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `KUPO:SJ`       |              1 | [CL:0002518](http://purl.obolibrary.org/obo/CL_0002518) |

## `LIPID_MAPS_class`: LIPID MAPS

Overall, there were 7 invalid
xrefs to external prefixed with `LIPID_MAPS_class` (standardized to Bioregistry
prefix [`lipidmaps`](https://bioregistry.io/lipidmaps)) that
did not match the standard pattern `^LM(FA|GL|GP|SP|ST|PR|SL|PK)[0-9]{4}([0-9a-zA-Z]{4,6})?$`.

| external_xref             |   usages_count | usages                                                    |
|---------------------------|----------------|-----------------------------------------------------------|
| `LIPID_MAPS_class:LMSP02` |              1 | [CHEBI:17761](http://purl.obolibrary.org/obo/CHEBI_17761) |
| `LIPID_MAPS_class:LMFA03` |              1 | [CHEBI:23899](http://purl.obolibrary.org/obo/CHEBI_23899) |
| `LIPID_MAPS_class:LMFA05` |              1 | [CHEBI:24026](http://purl.obolibrary.org/obo/CHEBI_24026) |
| `LIPID_MAPS_class:LMPR01` |              1 | [CHEBI:24913](http://purl.obolibrary.org/obo/CHEBI_24913) |
| `LIPID_MAPS_class:LMFA08` |              1 | [CHEBI:29348](http://purl.obolibrary.org/obo/CHEBI_29348) |
| `LIPID_MAPS_class:LMST04` |              1 | [CHEBI:36078](http://purl.obolibrary.org/obo/CHEBI_36078) |
| `LIPID_MAPS_class:LMGP12` |              1 | [CHEBI:76529](http://purl.obolibrary.org/obo/CHEBI_76529) |

## `MA`: Mouse adult gross anatomy

Overall, there were 19 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
prefix [`ma`](https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MA:th`         |             17 | [BSPO:1000000](http://purl.obolibrary.org/obo/BSPO_1000000), [UBERON:0000983](http://purl.obolibrary.org/obo/UBERON_0000983), [UBERON:0002470](http://purl.obolibrary.org/obo/UBERON_0002470), [UBERON:0002471](http://purl.obolibrary.org/obo/UBERON_0002471), [UBERON:0002472](http://purl.obolibrary.org/obo/UBERON_0002472), ... |
| `MA:ma`         |              2 | [CL:0000362](http://purl.obolibrary.org/obo/CL_0000362), [CL:0000731](http://purl.obolibrary.org/obo/CL_0000731)                                                                                                                                                                                                                     |

## `Medline`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `Medline` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                                |   usages_count | usages                                                      |
|----------------------------------------------|----------------|-------------------------------------------------------------|
| `Medline:http://www.nlm.nih.gov/medlineplus` |              1 | [PATO:0002048](http://purl.obolibrary.org/obo/PATO_0002048) |

## `MeSH`: Medical Subject Headings

Overall, there were 4 invalid
xrefs to external prefixed with `MeSH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                       |   usages_count | usages                                                                                                                       |
|-------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------|
| `MeSH:Synteny`                      |              2 | [RO:HOM0000010](http://purl.obolibrary.org/obo/RO_HOM0000010), [RO:HOM0000010](http://purl.obolibrary.org/obo/RO_HOM0000010) |
| `MeSH:Structural_Homology,_Protein` |              1 | [RO:HOM0000015](http://purl.obolibrary.org/obo/RO_HOM0000015)                                                                |
| `MeSH:Chromosome_Pairing`           |              1 | [RO:HOM0000047](http://purl.obolibrary.org/obo/RO_HOM0000047)                                                                |

## `MESH`: Medical Subject Headings

Overall, there were 168 invalid
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

## `MetaCyc`: Metabolic Encyclopedia of metabolic and other pathways

Overall, there were 1 invalid
xrefs to external prefixed with `MetaCyc` (standardized to Bioregistry
prefix [`metacyc.compound`](https://bioregistry.io/metacyc.compound)) that
did not match the standard pattern `^[A-Za-z0-9+_.%-:]+$`.

| external_xref                                 |   usages_count | usages                                                  |
|-----------------------------------------------|----------------|---------------------------------------------------------|
| `MetaCyc:[ACETYL-COA-CARBOXYLASE]-KINASE-RXN` |              1 | [GO:0050405](http://purl.obolibrary.org/obo/GO_0050405) |

## `MGD`: Mouse Genome Informatics

Overall, there were 1 invalid
xrefs to external prefixed with `MGD` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `MGD:tm`        |              1 | [SO:0001644](http://purl.obolibrary.org/obo/SO_0001644) |

## `MGI`: Mouse Genome Informatics

Overall, there were 264 invalid
xrefs to external prefixed with `MGI` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MGI:anna`      |            104 | [UBERON:0000057](http://purl.obolibrary.org/obo/UBERON_0000057), [UBERON:0000076](http://purl.obolibrary.org/obo/UBERON_0000076), [UBERON:0000114](http://purl.obolibrary.org/obo/UBERON_0000114), [UBERON:0000325](http://purl.obolibrary.org/obo/UBERON_0000325), [UBERON:0000453](http://purl.obolibrary.org/obo/UBERON_0000453), ... |
| `MGI:csmith`    |             74 | [GO:1903702](http://purl.obolibrary.org/obo/GO_1903702), [UBERON:0000305](http://purl.obolibrary.org/obo/UBERON_0000305), [UBERON:0000995](http://purl.obolibrary.org/obo/UBERON_0000995), [UBERON:0001063](http://purl.obolibrary.org/obo/UBERON_0001063), [UBERON:0001078](http://purl.obolibrary.org/obo/UBERON_0001078), ...         |
| `MGI:cwg`       |             25 | [UBERON:0001013](http://purl.obolibrary.org/obo/UBERON_0001013), [UBERON:0001542](http://purl.obolibrary.org/obo/UBERON_0001542), [UBERON:0001543](http://purl.obolibrary.org/obo/UBERON_0001543), [UBERON:0001728](http://purl.obolibrary.org/obo/UBERON_0001728), [UBERON:0001729](http://purl.obolibrary.org/obo/UBERON_0001729), ... |
| `MGI:smb`       |             24 | [UBERON:0000362](http://purl.obolibrary.org/obo/UBERON_0000362), [UBERON:0000396](http://purl.obolibrary.org/obo/UBERON_0000396), [UBERON:0001295](http://purl.obolibrary.org/obo/UBERON_0001295), [UBERON:0001348](http://purl.obolibrary.org/obo/UBERON_0001348), [UBERON:0001772](http://purl.obolibrary.org/obo/UBERON_0001772), ... |
| `MGI:llw2`      |             11 | [UBERON:0000388](http://purl.obolibrary.org/obo/UBERON_0000388), [UBERON:0000959](http://purl.obolibrary.org/obo/UBERON_0000959), [UBERON:0001235](http://purl.obolibrary.org/obo/UBERON_0001235), [UBERON:0001236](http://purl.obolibrary.org/obo/UBERON_0001236), [UBERON:0001451](http://purl.obolibrary.org/obo/UBERON_0001451), ... |
| `MGI:cs`        |              8 | [UBERON:0018242](http://purl.obolibrary.org/obo/UBERON_0018242), [UBERON:0034932](http://purl.obolibrary.org/obo/UBERON_0034932), [UBERON:0035617](http://purl.obolibrary.org/obo/UBERON_0035617), [UBERON:0035618](http://purl.obolibrary.org/obo/UBERON_0035618), [UBERON:0035619](http://purl.obolibrary.org/obo/UBERON_0035619), ... |
| `MGI:pvb`       |              5 | [UBERON:0000087](http://purl.obolibrary.org/obo/UBERON_0000087), [UBERON:0001000](http://purl.obolibrary.org/obo/UBERON_0001000), [UBERON:0001230](http://purl.obolibrary.org/obo/UBERON_0001230), [UBERON:0001301](http://purl.obolibrary.org/obo/UBERON_0001301), [UBERON:0005623](http://purl.obolibrary.org/obo/UBERON_0005623)      |
| `MGI:rbabiuk`   |              3 | [UBERON:0001213](http://purl.obolibrary.org/obo/UBERON_0001213), [UBERON:0010412](http://purl.obolibrary.org/obo/UBERON_0010412), [UBERON:0014396](http://purl.obolibrary.org/obo/UBERON_0014396)                                                                                                                                        |
| `MGI:monikat`   |              3 | [UBERON:0002115](http://purl.obolibrary.org/obo/UBERON_0002115), [UBERON:0002493](http://purl.obolibrary.org/obo/UBERON_0002493), [UBERON:0002511](http://purl.obolibrary.org/obo/UBERON_0002511)                                                                                                                                        |
| `MGI:hdene`     |              2 | [UBERON:0001439](http://purl.obolibrary.org/obo/UBERON_0001439), [UBERON:0001832](http://purl.obolibrary.org/obo/UBERON_0001832)                                                                                                                                                                                                         |
| `MGI:hdeen`     |              1 | [SO:0001503](http://purl.obolibrary.org/obo/SO_0001503)                                                                                                                                                                                                                                                                                  |
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

## `NCI`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCI` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `NCI:131302`    |              1 | [DOID:0080925](http://purl.obolibrary.org/obo/DOID_0080925) |

## `NCI_Thesaurus`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCI_Thesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                                   |   usages_count | usages                                                  |
|-------------------------------------------------|----------------|---------------------------------------------------------|
| `NCI_Thesaurus:Small_Intestinal_Glandular_Cell` |              1 | [CL:1001598](http://purl.obolibrary.org/obo/CL_1001598) |

## `NCIT`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCIT` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `NCIT:NCIT`     |              1 | [UBERON:0010499](http://purl.obolibrary.org/obo/UBERON_0010499) |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 234 invalid
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
| `ncithesaurus:Spermatogenic_Cell`                             |              1 | [CL:0000015](http://purl.obolibrary.org/obo/CL_0000015)                                                                          |
| `ncithesaurus:Egg`                                            |              1 | [CL:0000021](http://purl.obolibrary.org/obo/CL_0000021)                                                                          |
| `ncithesaurus:Beta_Cell`                                      |              1 | [CL:0000169](http://purl.obolibrary.org/obo/CL_0000169)                                                                          |
| `ncithesaurus:Blastemal_Cell`                                 |              1 | [CL:0000354](http://purl.obolibrary.org/obo/CL_0000354)                                                                          |
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

## `neurolex`: NIF Standard Ontology: Neurolex

Overall, there were 2 invalid
xrefs to external prefixed with `neurolex` (standardized to Bioregistry
prefix [`neurolex`](https://bioregistry.io/neurolex)) that
did not match the standard pattern `^\d+$`.

| external_xref                                                           |   usages_count | usages                                                      |
|-------------------------------------------------------------------------|----------------|-------------------------------------------------------------|
| `neurolex:http://neurolex.org/`                                         |              1 | [PATO:0002216](http://purl.obolibrary.org/obo/PATO_0002216) |
| `neurolex:http://neurolex.org/wiki/Category:Nitrated_Molecular_Quality` |              1 | [PATO:0002217](http://purl.obolibrary.org/obo/PATO_0002217) |

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

Overall, there were 415 invalid
xrefs to external prefixed with `NIF_Subcellular` (standardized to Bioregistry
prefix [`nlx.sub`](https://bioregistry.io/nlx.sub)) that
did not match the standard pattern `^\d+$`.

| external_xref                          |   usages_count | usages                                                                                                                                                                                                                                                                                      |
|----------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `NIF_Subcellular:sao28175134`          |              5 | [GO:0044292](http://purl.obolibrary.org/obo/GO_0044292), [GO:0044292](http://purl.obolibrary.org/obo/GO_0044292), [GO:0044292](http://purl.obolibrary.org/obo/GO_0044292), [GO:0044293](http://purl.obolibrary.org/obo/GO_0044293), [GO:0044293](http://purl.obolibrary.org/obo/GO_0044293) |
| `NIF_Subcellular:sao1186862860`        |              4 | [GO:0044225](http://purl.obolibrary.org/obo/GO_0044225), [GO:0044225](http://purl.obolibrary.org/obo/GO_0044225), [GO:0044226](http://purl.obolibrary.org/obo/GO_0044226), [GO:0044226](http://purl.obolibrary.org/obo/GO_0044226)                                                          |
| `NIF_Subcellular:sao1038025871`        |              3 | [GO:0005844](http://purl.obolibrary.org/obo/GO_0005844), [GO:0005844](http://purl.obolibrary.org/obo/GO_0005844), [GO:0005844](http://purl.obolibrary.org/obo/GO_0005844)                                                                                                                   |
| `NIF_Subcellular:sao1145756102`        |              3 | [GO:0044309](http://purl.obolibrary.org/obo/GO_0044309), [GO:0044309](http://purl.obolibrary.org/obo/GO_0044309), [UBERON:0001130](http://purl.obolibrary.org/obo/UBERON_0001130)                                                                                                           |
| `NIF_Subcellular:sao1079900774`        |              3 | [GO:0097441](http://purl.obolibrary.org/obo/GO_0097441), [GO:0097441](http://purl.obolibrary.org/obo/GO_0097441), [GO:0097441](http://purl.obolibrary.org/obo/GO_0097441)                                                                                                                   |
| `NIF_Subcellular:sao1571698684`        |              2 | [GO:0001740](http://purl.obolibrary.org/obo/GO_0001740), [GO:0001740](http://purl.obolibrary.org/obo/GO_0001740)                                                                                                                                                                            |
| `NIF_Subcellular:sao1337158144`        |              2 | [GO:0005575](http://purl.obolibrary.org/obo/GO_0005575), [GO:0005575](http://purl.obolibrary.org/obo/GO_0005575)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090701` |              2 | [GO:0005769](http://purl.obolibrary.org/obo/GO_0005769), [GO:0005769](http://purl.obolibrary.org/obo/GO_0005769)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090702` |              2 | [GO:0005770](http://purl.obolibrary.org/obo/GO_0005770), [GO:0005770](http://purl.obolibrary.org/obo/GO_0005770)                                                                                                                                                                            |
| `NIF_Subcellular:sao1969557946`        |              2 | [GO:0005905](http://purl.obolibrary.org/obo/GO_0005905), [GO:0005905](http://purl.obolibrary.org/obo/GO_0005905)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_090901`   |              2 | [GO:0015030](http://purl.obolibrary.org/obo/GO_0015030), [GO:0015030](http://purl.obolibrary.org/obo/GO_0015030)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090513` |              2 | [GO:0031012](http://purl.obolibrary.org/obo/GO_0031012), [GO:0031012](http://purl.obolibrary.org/obo/GO_0031012)                                                                                                                                                                            |
| `NIF_Subcellular:sao772007592`         |              2 | [GO:0031045](http://purl.obolibrary.org/obo/GO_0031045), [GO:0031045](http://purl.obolibrary.org/obo/GO_0031045)                                                                                                                                                                            |
| `NIF_Subcellular:sao1045389829`        |              2 | [GO:0031966](http://purl.obolibrary.org/obo/GO_0031966), [GO:0031966](http://purl.obolibrary.org/obo/GO_0031966)                                                                                                                                                                            |
| `NIF_Subcellular:sao936144858`         |              2 | [GO:0033270](http://purl.obolibrary.org/obo/GO_0033270), [GO:0033270](http://purl.obolibrary.org/obo/GO_0033270)                                                                                                                                                                            |
| `NIF_Subcellular:sao593830697`         |              2 | [GO:0043209](http://purl.obolibrary.org/obo/GO_0043209), [GO:0043209](http://purl.obolibrary.org/obo/GO_0043209)                                                                                                                                                                            |
| `NIF_Subcellular:sao1123256993`        |              2 | [GO:0043218](http://purl.obolibrary.org/obo/GO_0043218), [GO:0043218](http://purl.obolibrary.org/obo/GO_0043218)                                                                                                                                                                            |
| `NIF_Subcellular:sao1938587839`        |              2 | [GO:0044280](http://purl.obolibrary.org/obo/GO_0044280), [GO:0044280](http://purl.obolibrary.org/obo/GO_0044280)                                                                                                                                                                            |
| `NIF_Subcellular:sao1943947957`        |              2 | [GO:0044286](http://purl.obolibrary.org/obo/GO_0044286), [GO:0044286](http://purl.obolibrary.org/obo/GO_0044286)                                                                                                                                                                            |
| `NIF_Subcellular:sao257629430`         |              2 | [GO:0044288](http://purl.obolibrary.org/obo/GO_0044288), [GO:0044288](http://purl.obolibrary.org/obo/GO_0044288)                                                                                                                                                                            |
| `NIF_Subcellular:sao508958414`         |              2 | [GO:0044290](http://purl.obolibrary.org/obo/GO_0044290), [GO:0044290](http://purl.obolibrary.org/obo/GO_0044290)                                                                                                                                                                            |
| `NIF_Subcellular:sao1299635018`        |              2 | [GO:0044291](http://purl.obolibrary.org/obo/GO_0044291), [GO:0044291](http://purl.obolibrary.org/obo/GO_0044291)                                                                                                                                                                            |
| `NIF_Subcellular:sao295057932`         |              2 | [GO:0044293](http://purl.obolibrary.org/obo/GO_0044293), [GO:0044293](http://purl.obolibrary.org/obo/GO_0044293)                                                                                                                                                                            |
| `NIF_Subcellular:sao203987954`         |              2 | [GO:0044295](http://purl.obolibrary.org/obo/GO_0044295), [GO:0044295](http://purl.obolibrary.org/obo/GO_0044295)                                                                                                                                                                            |
| `NIF_Subcellular:sao1340260079`        |              2 | [GO:0044296](http://purl.obolibrary.org/obo/GO_0044296), [GO:0044296](http://purl.obolibrary.org/obo/GO_0044296)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090210` |              2 | [GO:0044299](http://purl.obolibrary.org/obo/GO_0044299), [GO:0044299](http://purl.obolibrary.org/obo/GO_0044299)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090209` |              2 | [GO:0044300](http://purl.obolibrary.org/obo/GO_0044300), [GO:0044300](http://purl.obolibrary.org/obo/GO_0044300)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090203` |              2 | [GO:0044301](http://purl.obolibrary.org/obo/GO_0044301), [GO:0044301](http://purl.obolibrary.org/obo/GO_0044301)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090601` |              2 | [GO:0044302](http://purl.obolibrary.org/obo/GO_0044302), [GO:0044302](http://purl.obolibrary.org/obo/GO_0044302)                                                                                                                                                                            |
| `NIF_Subcellular:sao1470140754`        |              2 | [GO:0044303](http://purl.obolibrary.org/obo/GO_0044303), [GO:0044303](http://purl.obolibrary.org/obo/GO_0044303)                                                                                                                                                                            |
| `NIF_Subcellular:sao1596975044`        |              2 | [GO:0044304](http://purl.obolibrary.org/obo/GO_0044304), [GO:0044304](http://purl.obolibrary.org/obo/GO_0044304)                                                                                                                                                                            |
| `NIF_Subcellular:sao1684283879`        |              2 | [GO:0044305](http://purl.obolibrary.org/obo/GO_0044305), [GO:0044305](http://purl.obolibrary.org/obo/GO_0044305)                                                                                                                                                                            |
| `NIF_Subcellular:sao884265541`         |              2 | [GO:0044307](http://purl.obolibrary.org/obo/GO_0044307), [GO:0044307](http://purl.obolibrary.org/obo/GO_0044307)                                                                                                                                                                            |
| `NIF_Subcellular:sao18239917`          |              2 | [GO:0044308](http://purl.obolibrary.org/obo/GO_0044308), [GO:0044308](http://purl.obolibrary.org/obo/GO_0044308)                                                                                                                                                                            |
| `NIF_Subcellular:sao8444068431`        |              2 | [GO:0044754](http://purl.obolibrary.org/obo/GO_0044754), [GO:0044754](http://purl.obolibrary.org/obo/GO_0044754)                                                                                                                                                                            |
| `NIF_Subcellular:sao1470121605`        |              2 | [GO:0048788](http://purl.obolibrary.org/obo/GO_0048788), [GO:0048788](http://purl.obolibrary.org/obo/GO_0048788)                                                                                                                                                                            |
| `NIF_Subcellular:sao124393998`         |              2 | [GO:0070971](http://purl.obolibrary.org/obo/GO_0070971), [GO:0070971](http://purl.obolibrary.org/obo/GO_0070971)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090101` |              2 | [GO:0097407](http://purl.obolibrary.org/obo/GO_0097407), [GO:0097407](http://purl.obolibrary.org/obo/GO_0097407)                                                                                                                                                                            |
| `NIF_Subcellular:sao967812059`         |              2 | [GO:0097408](http://purl.obolibrary.org/obo/GO_0097408), [GO:0097408](http://purl.obolibrary.org/obo/GO_0097408)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090703` |              2 | [GO:0097409](http://purl.obolibrary.org/obo/GO_0097409), [GO:0097409](http://purl.obolibrary.org/obo/GO_0097409)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090104` |              2 | [GO:0097412](http://purl.obolibrary.org/obo/GO_0097412), [GO:0097412](http://purl.obolibrary.org/obo/GO_0097412)                                                                                                                                                                            |
| `NIF_Subcellular:sao4933778419`        |              2 | [GO:0097413](http://purl.obolibrary.org/obo/GO_0097413), [GO:0097413](http://purl.obolibrary.org/obo/GO_0097413)                                                                                                                                                                            |
| `NIF_Subcellular:sao4749542545`        |              2 | [GO:0097414](http://purl.obolibrary.org/obo/GO_0097414), [GO:0097414](http://purl.obolibrary.org/obo/GO_0097414)                                                                                                                                                                            |
| `NIF_Subcellular:sao4040591221`        |              2 | [GO:0097415](http://purl.obolibrary.org/obo/GO_0097415), [GO:0097415](http://purl.obolibrary.org/obo/GO_0097415)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090105` |              2 | [GO:0097416](http://purl.obolibrary.org/obo/GO_0097416), [GO:0097416](http://purl.obolibrary.org/obo/GO_0097416)                                                                                                                                                                            |
| `NIF_Subcellular:sao138430598`         |              2 | [GO:0097417](http://purl.obolibrary.org/obo/GO_0097417), [GO:0097417](http://purl.obolibrary.org/obo/GO_0097417)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090201` |              2 | [GO:0097418](http://purl.obolibrary.org/obo/GO_0097418), [GO:0097418](http://purl.obolibrary.org/obo/GO_0097418)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090202` |              2 | [GO:0097418](http://purl.obolibrary.org/obo/GO_0097418), [GO:0097418](http://purl.obolibrary.org/obo/GO_0097418)                                                                                                                                                                            |
| `NIF_Subcellular:sao2409833926`        |              2 | [GO:0097418](http://purl.obolibrary.org/obo/GO_0097418), [GO:0097418](http://purl.obolibrary.org/obo/GO_0097418)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090102` |              2 | [GO:0097419](http://purl.obolibrary.org/obo/GO_0097419), [GO:0097419](http://purl.obolibrary.org/obo/GO_0097419)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090103` |              2 | [GO:0097420](http://purl.obolibrary.org/obo/GO_0097420), [GO:0097420](http://purl.obolibrary.org/obo/GO_0097420)                                                                                                                                                                            |
| `NIF_Subcellular:sao1570660411`        |              2 | [GO:0097422](http://purl.obolibrary.org/obo/GO_0097422), [GO:0097422](http://purl.obolibrary.org/obo/GO_0097422)                                                                                                                                                                            |
| `NIF_Subcellular:sao694815499`         |              2 | [GO:0097422](http://purl.obolibrary.org/obo/GO_0097422), [GO:0097422](http://purl.obolibrary.org/obo/GO_0097422)                                                                                                                                                                            |
| `NIF_Subcellular:sao1933817066`        |              2 | [GO:0097423](http://purl.obolibrary.org/obo/GO_0097423), [GO:0097423](http://purl.obolibrary.org/obo/GO_0097423)                                                                                                                                                                            |
| `NIF_Subcellular:sao1210952635`        |              2 | [GO:0097424](http://purl.obolibrary.org/obo/GO_0097424), [GO:0097424](http://purl.obolibrary.org/obo/GO_0097424)                                                                                                                                                                            |
| `NIF_Subcellular:sao184202831`         |              2 | [GO:0097425](http://purl.obolibrary.org/obo/GO_0097425), [GO:0097425](http://purl.obolibrary.org/obo/GO_0097425)                                                                                                                                                                            |
| `NIF_Subcellular:sao1863852493`        |              2 | [GO:0097426](http://purl.obolibrary.org/obo/GO_0097426), [GO:0097426](http://purl.obolibrary.org/obo/GO_0097426)                                                                                                                                                                            |
| `NIF_Subcellular:sao1872343973`        |              2 | [GO:0097427](http://purl.obolibrary.org/obo/GO_0097427), [GO:0097427](http://purl.obolibrary.org/obo/GO_0097427)                                                                                                                                                                            |
| `NIF_Subcellular:sao730872736`         |              2 | [GO:0097433](http://purl.obolibrary.org/obo/GO_0097433), [GO:0097433](http://purl.obolibrary.org/obo/GO_0097433)                                                                                                                                                                            |
| `NIF_Subcellular:sao273773228`         |              2 | [GO:0097440](http://purl.obolibrary.org/obo/GO_0097440), [GO:0097440](http://purl.obolibrary.org/obo/GO_0097440)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_1005001`  |              2 | [GO:0097442](http://purl.obolibrary.org/obo/GO_0097442), [GO:0097442](http://purl.obolibrary.org/obo/GO_0097442)                                                                                                                                                                            |
| `NIF_Subcellular:sao1028571114`        |              2 | [GO:0097443](http://purl.obolibrary.org/obo/GO_0097443), [GO:0097443](http://purl.obolibrary.org/obo/GO_0097443)                                                                                                                                                                            |
| `NIF_Subcellular:sao725931194`         |              2 | [GO:0097444](http://purl.obolibrary.org/obo/GO_0097444), [GO:0097444](http://purl.obolibrary.org/obo/GO_0097444)                                                                                                                                                                            |
| `NIF_Subcellular:sao494258938`         |              2 | [GO:0097445](http://purl.obolibrary.org/obo/GO_0097445), [GO:0097445](http://purl.obolibrary.org/obo/GO_0097445)                                                                                                                                                                            |
| `NIF_Subcellular:sao172297168`         |              2 | [GO:0097447](http://purl.obolibrary.org/obo/GO_0097447), [GO:0097447](http://purl.obolibrary.org/obo/GO_0097447)                                                                                                                                                                            |
| `NIF_Subcellular:sao2128156969`        |              2 | [GO:0097448](http://purl.obolibrary.org/obo/GO_0097448), [GO:0097448](http://purl.obolibrary.org/obo/GO_0097448)                                                                                                                                                                            |
| `NIF_Subcellular:sao1630537580`        |              2 | [GO:0097449](http://purl.obolibrary.org/obo/GO_0097449), [GO:0097449](http://purl.obolibrary.org/obo/GO_0097449)                                                                                                                                                                            |
| `NIF_Subcellular:sao388182739`         |              2 | [GO:0097450](http://purl.obolibrary.org/obo/GO_0097450), [GO:0097450](http://purl.obolibrary.org/obo/GO_0097450)                                                                                                                                                                            |
| `NIF_Subcellular:sao181458425`         |              2 | [GO:0097451](http://purl.obolibrary.org/obo/GO_0097451), [GO:0097451](http://purl.obolibrary.org/obo/GO_0097451)                                                                                                                                                                            |
| `NIF_Subcellular:sao2127666702`        |              2 | [GO:0097453](http://purl.obolibrary.org/obo/GO_0097453), [GO:0097453](http://purl.obolibrary.org/obo/GO_0097453)                                                                                                                                                                            |
| `NIF_Subcellular:sao1890444066`        |              2 | [GO:0097454](http://purl.obolibrary.org/obo/GO_0097454), [GO:0097454](http://purl.obolibrary.org/obo/GO_0097454)                                                                                                                                                                            |
| `NIF_Subcellular:sao937871668`         |              2 | [GO:0097455](http://purl.obolibrary.org/obo/GO_0097455), [GO:0097455](http://purl.obolibrary.org/obo/GO_0097455)                                                                                                                                                                            |
| `NIF_Subcellular:sao924713546`         |              2 | [GO:0097456](http://purl.obolibrary.org/obo/GO_0097456), [GO:0097456](http://purl.obolibrary.org/obo/GO_0097456)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_100312`   |              2 | [GO:0097457](http://purl.obolibrary.org/obo/GO_0097457), [GO:0097457](http://purl.obolibrary.org/obo/GO_0097457)                                                                                                                                                                            |
| `NIF_Subcellular:sao601362597`         |              2 | [GO:0097462](http://purl.obolibrary.org/obo/GO_0097462), [GO:0097462](http://purl.obolibrary.org/obo/GO_0097462)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_1005003`  |              2 | [GO:0097463](http://purl.obolibrary.org/obo/GO_0097463), [GO:0097463](http://purl.obolibrary.org/obo/GO_0097463)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_467`              |              2 | [GO:0097464](http://purl.obolibrary.org/obo/GO_0097464), [GO:0097464](http://purl.obolibrary.org/obo/GO_0097464)                                                                                                                                                                            |
| `NIF_Subcellular:sao2048514053`        |              2 | [GO:0097465](http://purl.obolibrary.org/obo/GO_0097465), [GO:0097465](http://purl.obolibrary.org/obo/GO_0097465)                                                                                                                                                                            |
| `NIF_Subcellular:sao1884931180`        |              2 | [GO:0097470](http://purl.obolibrary.org/obo/GO_0097470), [GO:0097470](http://purl.obolibrary.org/obo/GO_0097470)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_091021`   |              2 | [GO:0097471](http://purl.obolibrary.org/obo/GO_0097471), [GO:0097471](http://purl.obolibrary.org/obo/GO_0097471)                                                                                                                                                                            |
| `NIF_Subcellular:sao110773650`         |              2 | [GO:1901588](http://purl.obolibrary.org/obo/GO_1901588), [GO:1901588](http://purl.obolibrary.org/obo/GO_1901588)                                                                                                                                                                            |
| `NIF_Subcellular:sao707332678`         |              2 | [GO:1901589](http://purl.obolibrary.org/obo/GO_1901589), [GO:1901589](http://purl.obolibrary.org/obo/GO_1901589)                                                                                                                                                                            |
| `NIF_Subcellular:sao478230652`         |              2 | [GO:1990005](http://purl.obolibrary.org/obo/GO_1990005), [GO:1990005](http://purl.obolibrary.org/obo/GO_1990005)                                                                                                                                                                            |
| `NIF_Subcellular:sao1531915298`        |              2 | [GO:1990006](http://purl.obolibrary.org/obo/GO_1990006), [GO:1990006](http://purl.obolibrary.org/obo/GO_1990006)                                                                                                                                                                            |
| `NIF_Subcellular:sao2114874506`        |              2 | [GO:1990007](http://purl.obolibrary.org/obo/GO_1990007), [GO:1990007](http://purl.obolibrary.org/obo/GO_1990007)                                                                                                                                                                            |
| `NIF_Subcellular:sao2031592629`        |              2 | [GO:1990008](http://purl.obolibrary.org/obo/GO_1990008), [GO:1990008](http://purl.obolibrary.org/obo/GO_1990008)                                                                                                                                                                            |
| `NIF_Subcellular:sao506721981`         |              2 | [GO:1990011](http://purl.obolibrary.org/obo/GO_1990011), [GO:1990011](http://purl.obolibrary.org/obo/GO_1990011)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_151681`           |              2 | [GO:1990012](http://purl.obolibrary.org/obo/GO_1990012), [GO:1990012](http://purl.obolibrary.org/obo/GO_1990012)                                                                                                                                                                            |
| `NIF_Subcellular:sao1730664005`        |              2 | [GO:1990013](http://purl.obolibrary.org/obo/GO_1990013), [GO:1990013](http://purl.obolibrary.org/obo/GO_1990013)                                                                                                                                                                            |
| `NIF_Subcellular:sao1747012216`        |              2 | [GO:1990014](http://purl.obolibrary.org/obo/GO_1990014), [GO:1990014](http://purl.obolibrary.org/obo/GO_1990014)                                                                                                                                                                            |
| `NIF_Subcellular:sao1376748732`        |              2 | [GO:1990015](http://purl.obolibrary.org/obo/GO_1990015), [GO:1990015](http://purl.obolibrary.org/obo/GO_1990015)                                                                                                                                                                            |
| `NIF_Subcellular:sao901230115`         |              2 | [GO:1990016](http://purl.obolibrary.org/obo/GO_1990016), [GO:1990016](http://purl.obolibrary.org/obo/GO_1990016)                                                                                                                                                                            |
| `NIF_Subcellular:sao401910342`         |              2 | [GO:1990017](http://purl.obolibrary.org/obo/GO_1990017), [GO:1990017](http://purl.obolibrary.org/obo/GO_1990017)                                                                                                                                                                            |
| `NIF_Subcellular:sao1749953771`        |              2 | [GO:1990018](http://purl.obolibrary.org/obo/GO_1990018), [GO:1990018](http://purl.obolibrary.org/obo/GO_1990018)                                                                                                                                                                            |
| `NIF_Subcellular:sao1642494436`        |              2 | [GO:1990020](http://purl.obolibrary.org/obo/GO_1990020), [GO:1990020](http://purl.obolibrary.org/obo/GO_1990020)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090511` |              2 | [GO:1990021](http://purl.obolibrary.org/obo/GO_1990021), [GO:1990021](http://purl.obolibrary.org/obo/GO_1990021)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_100208`   |              2 | [GO:1990024](http://purl.obolibrary.org/obo/GO_1990024), [GO:1990024](http://purl.obolibrary.org/obo/GO_1990024)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_100206`   |              2 | [GO:1990025](http://purl.obolibrary.org/obo/GO_1990025), [GO:1990025](http://purl.obolibrary.org/obo/GO_1990025)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_1005002`  |              2 | [GO:1990026](http://purl.obolibrary.org/obo/GO_1990026), [GO:1990026](http://purl.obolibrary.org/obo/GO_1990026)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_100207`   |              2 | [GO:1990027](http://purl.obolibrary.org/obo/GO_1990027), [GO:1990027](http://purl.obolibrary.org/obo/GO_1990027)                                                                                                                                                                            |
| `NIF_Subcellular:sao413722576`         |              2 | [GO:1990030](http://purl.obolibrary.org/obo/GO_1990030), [GO:1990030](http://purl.obolibrary.org/obo/GO_1990030)                                                                                                                                                                            |
| `NIF_Subcellular:sao109906988`         |              2 | [GO:1990031](http://purl.obolibrary.org/obo/GO_1990031), [GO:1990031](http://purl.obolibrary.org/obo/GO_1990031)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_330`              |              2 | [GO:1990032](http://purl.obolibrary.org/obo/GO_1990032), [GO:1990032](http://purl.obolibrary.org/obo/GO_1990032)                                                                                                                                                                            |
| `NIF_Subcellular:sao1348591767`        |              2 | [GO:1990033](http://purl.obolibrary.org/obo/GO_1990033), [GO:1990033](http://purl.obolibrary.org/obo/GO_1990033)                                                                                                                                                                            |
| `NIF_Subcellular:sao6587439252`        |              2 | [GO:1990037](http://purl.obolibrary.org/obo/GO_1990037), [GO:1990037](http://purl.obolibrary.org/obo/GO_1990037)                                                                                                                                                                            |
| `NIF_Subcellular:sao5764355747`        |              2 | [GO:1990038](http://purl.obolibrary.org/obo/GO_1990038), [GO:1990038](http://purl.obolibrary.org/obo/GO_1990038)                                                                                                                                                                            |
| `NIF_Subcellular:sao1634374950`        |              2 | [GO:1990039](http://purl.obolibrary.org/obo/GO_1990039), [GO:1990039](http://purl.obolibrary.org/obo/GO_1990039)                                                                                                                                                                            |
| `NIF_Subcellular:sao128470897`         |              2 | [GO:1990040](http://purl.obolibrary.org/obo/GO_1990040), [GO:1990040](http://purl.obolibrary.org/obo/GO_1990040)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090504` |              2 | [UBERON:0011917](http://purl.obolibrary.org/obo/UBERON_0011917), [UBERON:0011917](http://purl.obolibrary.org/obo/UBERON_0011917)                                                                                                                                                            |
| `NIF_Subcellular:sao1841764412`        |              2 | [GO:0001651](http://purl.obolibrary.org/obo/GO_0001651), [GO:0001651](http://purl.obolibrary.org/obo/GO_0001651)                                                                                                                                                                            |
| `NIF_Subcellular:sao1217793903`        |              2 | [GO:0001652](http://purl.obolibrary.org/obo/GO_0001652), [GO:0001652](http://purl.obolibrary.org/obo/GO_0001652)                                                                                                                                                                            |
| `NIF_Subcellular:sao8663416959`        |              2 | [GO:0005776](http://purl.obolibrary.org/obo/GO_0005776), [GO:0005776](http://purl.obolibrary.org/obo/GO_0005776)                                                                                                                                                                            |
| `NIF_Subcellular:sao632188024`         |              2 | [GO:0005801](http://purl.obolibrary.org/obo/GO_0005801), [GO:0005801](http://purl.obolibrary.org/obo/GO_0005801)                                                                                                                                                                            |
| `NIF_Subcellular:sao671419673`         |              2 | [GO:0005902](http://purl.obolibrary.org/obo/GO_0005902), [GO:0005902](http://purl.obolibrary.org/obo/GO_0005902)                                                                                                                                                                            |
| `NIF_Subcellular:sao1311109124`        |              2 | [GO:0005921](http://purl.obolibrary.org/obo/GO_0005921), [GO:0045202](http://purl.obolibrary.org/obo/GO_0045202)                                                                                                                                                                            |
| `NIF_Subcellular:sao978443756`         |              2 | [GO:0010008](http://purl.obolibrary.org/obo/GO_0010008), [GO:0010008](http://purl.obolibrary.org/obo/GO_0010008)                                                                                                                                                                            |
| `NIF_Subcellular:sao120573470`         |              2 | [GO:0016234](http://purl.obolibrary.org/obo/GO_0016234), [GO:0016234](http://purl.obolibrary.org/obo/GO_0016234)                                                                                                                                                                            |
| `NIF_Subcellular:sao333328131`         |              2 | [GO:0030061](http://purl.obolibrary.org/obo/GO_0030061), [GO:0030061](http://purl.obolibrary.org/obo/GO_0030061)                                                                                                                                                                            |
| `NIF_Subcellular:sao3089754107`        |              2 | [GO:0030867](http://purl.obolibrary.org/obo/GO_0030867), [GO:0030867](http://purl.obolibrary.org/obo/GO_0030867)                                                                                                                                                                            |
| `NIF_Subcellular:sao830981606`         |              2 | [GO:0031090](http://purl.obolibrary.org/obo/GO_0031090), [GO:0031090](http://purl.obolibrary.org/obo/GO_0031090)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_20090512` |              2 | [GO:0031594](http://purl.obolibrary.org/obo/GO_0031594), [GO:0043679](http://purl.obolibrary.org/obo/GO_0043679)                                                                                                                                                                            |
| `NIF_Subcellular:sao561419532`         |              2 | [GO:0031985](http://purl.obolibrary.org/obo/GO_0031985), [GO:0031985](http://purl.obolibrary.org/obo/GO_0031985)                                                                                                                                                                            |
| `NIF_Subcellular:sao187426937`         |              2 | [GO:0043195](http://purl.obolibrary.org/obo/GO_0043195), [GO:0043195](http://purl.obolibrary.org/obo/GO_0043195)                                                                                                                                                                            |
| `NIF_Subcellular:sao1067215520`        |              2 | [GO:0043219](http://purl.obolibrary.org/obo/GO_0043219), [GO:0043219](http://purl.obolibrary.org/obo/GO_0043219)                                                                                                                                                                            |
| `NIF_Subcellular:sao1354781919`        |              2 | [GO:0043219](http://purl.obolibrary.org/obo/GO_0043219), [GO:0043219](http://purl.obolibrary.org/obo/GO_0043219)                                                                                                                                                                            |
| `NIF_Subcellular:sao1642908940`        |              2 | [GO:0044326](http://purl.obolibrary.org/obo/GO_0044326), [GO:0044326](http://purl.obolibrary.org/obo/GO_0044326)                                                                                                                                                                            |
| `NIF_Subcellular:sao952643730`         |              2 | [GO:0044327](http://purl.obolibrary.org/obo/GO_0044327), [GO:0044327](http://purl.obolibrary.org/obo/GO_0044327)                                                                                                                                                                            |
| `NIF_Subcellular:sao1925368674`        |              2 | [GO:0044352](http://purl.obolibrary.org/obo/GO_0044352), [GO:0044352](http://purl.obolibrary.org/obo/GO_0044352)                                                                                                                                                                            |
| `NIF_Subcellular:sao1635329413`        |              2 | [GO:0044430](http://purl.obolibrary.org/obo/GO_0044430), [GO:0044430](http://purl.obolibrary.org/obo/GO_0044430)                                                                                                                                                                            |
| `NIF_Subcellular:sao1784069613`        |              2 | [GO:0044456](http://purl.obolibrary.org/obo/GO_0044456), [GO:0044456](http://purl.obolibrary.org/obo/GO_0044456)                                                                                                                                                                            |
| `NIF_Subcellular:sao2038461087`        |              2 | [GO:0048787](http://purl.obolibrary.org/obo/GO_0048787), [GO:0048787](http://purl.obolibrary.org/obo/GO_0048787)                                                                                                                                                                            |
| `NIF_Subcellular:sao18461326`          |              2 | [GO:0097002](http://purl.obolibrary.org/obo/GO_0097002), [GO:0097002](http://purl.obolibrary.org/obo/GO_0097002)                                                                                                                                                                            |
| `NIF_Subcellular:sao1594955670`        |              2 | [GO:0044294](http://purl.obolibrary.org/obo/GO_0044294), [GO:0044295](http://purl.obolibrary.org/obo/GO_0044295)                                                                                                                                                                            |
| `NIF_Subcellular:nlx_subcell_100315`   |              1 | [GO:0005575](http://purl.obolibrary.org/obo/GO_0005575)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao138219748`         |              1 | [GO:0005798](http://purl.obolibrary.org/obo/GO_0005798)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1039242387`        |              1 | [GO:0005802](http://purl.obolibrary.org/obo/GO_0005802)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1139385046`        |              1 | [GO:0005840](http://purl.obolibrary.org/obo/GO_0005840)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1291545653`        |              1 | [GO:0005840](http://purl.obolibrary.org/obo/GO_0005840)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao248349196`         |              1 | [GO:0005874](http://purl.obolibrary.org/obo/GO_0005874)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao6433132645`        |              1 | [GO:0005886](http://purl.obolibrary.org/obo/GO_0005886)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1395777368`        |              1 | [GO:0005911](http://purl.obolibrary.org/obo/GO_0005911)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao700839054`         |              1 | [GO:0005921](http://purl.obolibrary.org/obo/GO_0005921)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao403156667`         |              1 | [GO:0008021](http://purl.obolibrary.org/obo/GO_0008021)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao188049490`         |              1 | [GO:0033268](http://purl.obolibrary.org/obo/GO_0033268)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao250931889`         |              1 | [GO:0043005](http://purl.obolibrary.org/obo/GO_0043005)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1232858786`        |              1 | [GO:0043197](http://purl.obolibrary.org/obo/GO_0043197)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1536532595`        |              1 | [GO:0043197](http://purl.obolibrary.org/obo/GO_0043197)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao317384566`         |              1 | [GO:0043197](http://purl.obolibrary.org/obo/GO_0043197)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao876577163`         |              1 | [GO:0043197](http://purl.obolibrary.org/obo/GO_0043197)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao965204139`         |              1 | [GO:0043197](http://purl.obolibrary.org/obo/GO_0043197)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1078172392`        |              1 | [GO:0043198](http://purl.obolibrary.org/obo/GO_0043198)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:nlx_subcell_20090204` |              1 | [GO:0043209](http://purl.obolibrary.org/obo/GO_0043209)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1279474730`        |              1 | [GO:0043209](http://purl.obolibrary.org/obo/GO_0043209)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1186642361`        |              1 | [GO:0043218](http://purl.obolibrary.org/obo/GO_0043218)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao2007137787`        |              1 | [GO:0043679](http://purl.obolibrary.org/obo/GO_0043679)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1191319089`        |              1 | [GO:0044224](http://purl.obolibrary.org/obo/GO_0044224)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao9117790637`        |              1 | [GO:0044421](http://purl.obolibrary.org/obo/GO_0044421)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1499850686`        |              1 | [GO:0044428](http://purl.obolibrary.org/obo/GO_0044428)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao666410040`         |              1 | [GO:0044429](http://purl.obolibrary.org/obo/GO_0044429)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao624292949`         |              1 | [GO:0044431](http://purl.obolibrary.org/obo/GO_0044431)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1683772610`        |              1 | [GO:0044440](http://purl.obolibrary.org/obo/GO_0044440)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao628508602`         |              1 | [GO:0044464](http://purl.obolibrary.org/obo/GO_0044464)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1506103497`        |              1 | [GO:0045202](http://purl.obolibrary.org/obo/GO_0045202)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1911631652`        |              1 | [GO:0048786](http://purl.obolibrary.org/obo/GO_0048786)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1111202255`        |              1 | [GO:0048788](http://purl.obolibrary.org/obo/GO_0048788)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1488888179`        |              1 | [GO:0048788](http://purl.obolibrary.org/obo/GO_0048788)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1842028314`        |              1 | [GO:0097425](http://purl.obolibrary.org/obo/GO_0097425)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1004601938`        |              1 | [GO:0097444](http://purl.obolibrary.org/obo/GO_0097444)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1189060993`        |              1 | [GO:0097449](http://purl.obolibrary.org/obo/GO_0097449)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1573004591`        |              1 | [GO:0097449](http://purl.obolibrary.org/obo/GO_0097449)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1950673097`        |              1 | [GO:1990021](http://purl.obolibrary.org/obo/GO_1990021)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1186327184`        |              1 | [GO:0000262](http://purl.obolibrary.org/obo/GO_0000262)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1615953555`        |              1 | [GO:0000785](http://purl.obolibrary.org/obo/GO_0000785)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao445485807`         |              1 | [GO:0000791](http://purl.obolibrary.org/obo/GO_0000791)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao581845896`         |              1 | [GO:0000792](http://purl.obolibrary.org/obo/GO_0000792)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao785001660`         |              1 | [GO:0001518](http://purl.obolibrary.org/obo/GO_0001518)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1425028079`        |              1 | [GO:0005615](http://purl.obolibrary.org/obo/GO_0005615)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1813327414`        |              1 | [GO:0005623](http://purl.obolibrary.org/obo/GO_0005623)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1702920020`        |              1 | [GO:0005634](http://purl.obolibrary.org/obo/GO_0005634)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1612527463`        |              1 | [GO:0005637](http://purl.obolibrary.org/obo/GO_0005637)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1617136075`        |              1 | [GO:0005640](http://purl.obolibrary.org/obo/GO_0005640)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao220861693`         |              1 | [GO:0005643](http://purl.obolibrary.org/obo/GO_0005643)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1455996588`        |              1 | [GO:0005652](http://purl.obolibrary.org/obo/GO_0005652)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao661522542`         |              1 | [GO:0005654](http://purl.obolibrary.org/obo/GO_0005654)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1820400233`        |              1 | [GO:0005730](http://purl.obolibrary.org/obo/GO_0005730)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1860313010`        |              1 | [GO:0005739](http://purl.obolibrary.org/obo/GO_0005739)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1289741256`        |              1 | [GO:0005741](http://purl.obolibrary.org/obo/GO_0005741)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1371347282`        |              1 | [GO:0005743](http://purl.obolibrary.org/obo/GO_0005743)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao118944228`         |              1 | [GO:0005758](http://purl.obolibrary.org/obo/GO_0005758)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1804523077`        |              1 | [GO:0005759](http://purl.obolibrary.org/obo/GO_0005759)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao585356902`         |              1 | [GO:0005764](http://purl.obolibrary.org/obo/GO_0005764)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1140587416`        |              1 | [GO:0005766](http://purl.obolibrary.org/obo/GO_0005766)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1549842807`        |              1 | [GO:0005767](http://purl.obolibrary.org/obo/GO_0005767)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1720343330`        |              1 | [GO:0005768](http://purl.obolibrary.org/obo/GO_0005768)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao2045955158`        |              1 | [GO:0005771](http://purl.obolibrary.org/obo/GO_0005771)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao499555322`         |              1 | [GO:0005777](http://purl.obolibrary.org/obo/GO_0005777)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1036339110`        |              1 | [GO:0005783](http://purl.obolibrary.org/obo/GO_0005783)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao710427438`         |              1 | [GO:0005790](http://purl.obolibrary.org/obo/GO_0005790)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1881364067`        |              1 | [GO:0005791](http://purl.obolibrary.org/obo/GO_0005791)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao451912436`         |              1 | [GO:0005794](http://purl.obolibrary.org/obo/GO_0005794)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao819927218`         |              1 | [GO:0005798](http://purl.obolibrary.org/obo/GO_0005798)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao9456487`           |              1 | [GO:0005802](http://purl.obolibrary.org/obo/GO_0005802)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao95019936`          |              1 | [GO:0005814](http://purl.obolibrary.org/obo/GO_0005814)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao101633890`         |              1 | [GO:0005829](http://purl.obolibrary.org/obo/GO_0005829)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1429207766`        |              1 | [GO:0005840](http://purl.obolibrary.org/obo/GO_0005840)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1846835077`        |              1 | [GO:0005874](http://purl.obolibrary.org/obo/GO_0005874)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao952483289`         |              1 | [GO:0005882](http://purl.obolibrary.org/obo/GO_0005882)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1316272517`        |              1 | [GO:0005883](http://purl.obolibrary.org/obo/GO_0005883)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1588493326`        |              1 | [GO:0005884](http://purl.obolibrary.org/obo/GO_0005884)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1663586795`        |              1 | [GO:0005886](http://purl.obolibrary.org/obo/GO_0005886)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1922892319`        |              1 | [GO:0005911](http://purl.obolibrary.org/obo/GO_0005911)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1400623473`        |              1 | [GO:0005915](http://purl.obolibrary.org/obo/GO_0005915)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao427941916`         |              1 | [GO:0005918](http://purl.obolibrary.org/obo/GO_0005918)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao118541872`         |              1 | [GO:0005921](http://purl.obolibrary.org/obo/GO_0005921)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao445019788`         |              1 | [GO:0005922](http://purl.obolibrary.org/obo/GO_0005922)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1939999134`        |              1 | [GO:0005923](http://purl.obolibrary.org/obo/GO_0005923)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao787716553`         |              1 | [GO:0005929](http://purl.obolibrary.org/obo/GO_0005929)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1071221672`        |              1 | [GO:0008021](http://purl.obolibrary.org/obo/GO_0008021)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao371494298`         |              1 | [GO:0008076](http://purl.obolibrary.org/obo/GO_0008076)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao536287099`         |              1 | [GO:0008091](http://purl.obolibrary.org/obo/GO_0008091)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1153182838`        |              1 | [GO:0012506](http://purl.obolibrary.org/obo/GO_0012506)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1196688972`        |              1 | [GO:0014069](http://purl.obolibrary.org/obo/GO_0014069)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao505137457`         |              1 | [GO:0016604](http://purl.obolibrary.org/obo/GO_0016604)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao879919129`         |              1 | [GO:0030118](http://purl.obolibrary.org/obo/GO_0030118)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1177708494`        |              1 | [GO:0030120](http://purl.obolibrary.org/obo/GO_0030120)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao885490876`         |              1 | [GO:0030133](http://purl.obolibrary.org/obo/GO_0030133)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1985096626`        |              1 | [GO:0030135](http://purl.obolibrary.org/obo/GO_0030135)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao148845161`         |              1 | [GO:0030136](http://purl.obolibrary.org/obo/GO_0030136)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1362520468`        |              1 | [GO:0030139](http://purl.obolibrary.org/obo/GO_0030139)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1382918459`        |              1 | [GO:0030143](http://purl.obolibrary.org/obo/GO_0030143)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1046371754`        |              1 | [GO:0030175](http://purl.obolibrary.org/obo/GO_0030175)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1770195789`        |              1 | [GO:0030424](http://purl.obolibrary.org/obo/GO_0030424)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1211023249`        |              1 | [GO:0030425](http://purl.obolibrary.org/obo/GO_0030425)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao250772229`         |              1 | [GO:0030673](http://purl.obolibrary.org/obo/GO_0030673)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1596955044`        |              1 | [GO:0030868](http://purl.obolibrary.org/obo/GO_0030868)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao180601769`         |              1 | [GO:0031410](http://purl.obolibrary.org/obo/GO_0031410)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1124888485`        |              1 | [GO:0031594](http://purl.obolibrary.org/obo/GO_0031594)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1547508851`        |              1 | [GO:0031904](http://purl.obolibrary.org/obo/GO_0031904)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1687101204`        |              1 | [GO:0031965](http://purl.obolibrary.org/obo/GO_0031965)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao221389602`         |              1 | [GO:0031982](http://purl.obolibrary.org/obo/GO_0031982)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao797538226`         |              1 | [GO:0031983](http://purl.obolibrary.org/obo/GO_0031983)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:birnlex_1152_2`       |              1 | [GO:0033268](http://purl.obolibrary.org/obo/GO_0033268)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao206157942`         |              1 | [GO:0033269](http://purl.obolibrary.org/obo/GO_0033269)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao234066064`         |              1 | [GO:0033270](http://purl.obolibrary.org/obo/GO_0033270)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1049471211`        |              1 | [GO:0035061](http://purl.obolibrary.org/obo/GO_0035061)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao11978067`          |              1 | [GO:0036064](http://purl.obolibrary.org/obo/GO_0036064)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1081228141`        |              1 | [GO:0042587](http://purl.obolibrary.org/obo/GO_0042587)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1379604862`        |              1 | [GO:0042599](http://purl.obolibrary.org/obo/GO_0042599)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao867568886`         |              1 | [GO:0043005](http://purl.obolibrary.org/obo/GO_0043005)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1044911821`        |              1 | [GO:0043025](http://purl.obolibrary.org/obo/GO_0043025)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao243541954`         |              1 | [GO:0043083](http://purl.obolibrary.org/obo/GO_0043083)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao256000789`         |              1 | [GO:0043194](http://purl.obolibrary.org/obo/GO_0043194)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1799103720`        |              1 | [GO:0043197](http://purl.obolibrary.org/obo/GO_0043197)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao2034472720`        |              1 | [GO:0043198](http://purl.obolibrary.org/obo/GO_0043198)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao627227260`         |              1 | [GO:0043203](http://purl.obolibrary.org/obo/GO_0043203)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao254777664`         |              1 | [GO:0043220](http://purl.obolibrary.org/obo/GO_0043220)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1539965131`        |              1 | [GO:0043226](http://purl.obolibrary.org/obo/GO_0043226)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao414196390`         |              1 | [GO:0043227](http://purl.obolibrary.org/obo/GO_0043227)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1456184038`        |              1 | [GO:0043228](http://purl.obolibrary.org/obo/GO_0043228)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao758620702`         |              1 | [GO:0044224](http://purl.obolibrary.org/obo/GO_0044224)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao914572699`         |              1 | [GO:0045202](http://purl.obolibrary.org/obo/GO_0045202)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1243595998`        |              1 | [GO:0045334](http://purl.obolibrary.org/obo/GO_0045334)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao1819509473`        |              1 | [GO:0048237](http://purl.obolibrary.org/obo/GO_0048237)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao927884761`         |              1 | [GO:0048238](http://purl.obolibrary.org/obo/GO_0048238)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:sao792027222`         |              1 | [GO:0048786](http://purl.obolibrary.org/obo/GO_0048786)                                                                                                                                                                                                                                     |
| `NIF_Subcellular:nlx_subcell_100205`   |              1 | [UBERON:0000201](http://purl.obolibrary.org/obo/UBERON_0000201)                                                                                                                                                                                                                             |
| `NIF_Subcellular:sao1397492660`        |              1 | [UBERON:0000482](http://purl.obolibrary.org/obo/UBERON_0000482)                                                                                                                                                                                                                             |
| `NIF_Subcellular:sao205380252`         |              1 | [UBERON:0002606](http://purl.obolibrary.org/obo/UBERON_0002606)                                                                                                                                                                                                                             |
| `NIF_Subcellular:FMA_83604`            |              1 | [UBERON:0003719](http://purl.obolibrary.org/obo/UBERON_0003719)                                                                                                                                                                                                                             |
| `NIF_Subcellular:nlx_subcell_20090503` |              1 | [UBERON:0005387](http://purl.obolibrary.org/obo/UBERON_0005387)                                                                                                                                                                                                                             |
| `NIF_Subcellular:sao7547390221`        |              1 | [UBERON:0011860](http://purl.obolibrary.org/obo/UBERON_0011860)                                                                                                                                                                                                                             |
| `NIF_Subcellular:nlx_subcell_20090502` |              1 | [UBERON:0011915](http://purl.obolibrary.org/obo/UBERON_0011915)                                                                                                                                                                                                                             |
| `NIF_Subcellular:FMA_83606`            |              1 | [UBERON:0012456](http://purl.obolibrary.org/obo/UBERON_0012456)                                                                                                                                                                                                                             |
| `NIF_Subcellular:nlx_subcell_100209`   |              1 | [UBERON:0018687](http://purl.obolibrary.org/obo/UBERON_0018687)                                                                                                                                                                                                                             |

## `NIFSTD`: NIF Standard Ontology

Overall, there were 341 invalid
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
| `NIFSTD:sao131261273`                             |              2 | [CL:1001571](http://purl.obolibrary.org/obo/CL_1001571), [CL:1001571](http://purl.obolibrary.org/obo/CL_1001571)                                                                                                                                                                                                                         |
| `NIFSTD:sao1415726815`                            |              1 | [CL:0000119](http://purl.obolibrary.org/obo/CL_0000119)                                                                                                                                                                                                                                                                                  |
| `NIFSTD:FMAID_7191`                               |              1 | [UBERON:0002104](http://purl.obolibrary.org/obo/UBERON_0002104)                                                                                                                                                                                                                                                                          |
| `NIFSTD:Paxinos-Franklin-mouse-2001_abbrevSource` |              1 | [UBERON:0002701](http://purl.obolibrary.org/obo/UBERON_0002701)                                                                                                                                                                                                                                                                          |
| `NIFSTD:sao862606388`                             |              1 | [CL:0000598](http://purl.obolibrary.org/obo/CL_0000598)                                                                                                                                                                                                                                                                                  |

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

Overall, there were 2 invalid
xrefs to external prefixed with `OBI` (standardized to Bioregistry
prefix [`obi`](https://bioregistry.io/obi)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `OBI:OBI`       |              1 | [PATO:0001985](http://purl.obolibrary.org/obo/PATO_0001985)     |
| `OBI:MC`        |              1 | [UBERON:0012125](http://purl.obolibrary.org/obo/UBERON_0012125) |

## `OBO_REL`: Relation Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `OBO_REL` (standardized to Bioregistry
prefix [`ro`](https://bioregistry.io/ro)) that
did not match the standard pattern `^(HOM)?\d{7}$`.

| external_xref        |   usages_count | usages                                                      |
|----------------------|----------------|-------------------------------------------------------------|
| `OBO_REL:has_part`   |              1 | [PATO:0001555](http://purl.obolibrary.org/obo/PATO_0001555) |
| `OBO_REL:lacks_part` |              1 | [PATO:0002000](http://purl.obolibrary.org/obo/PATO_0002000) |

## `OMIM`: Online Mendelian Inheritance in Man

Overall, there were 271 invalid
xrefs to external prefixed with `OMIM` (standardized to Bioregistry
prefix [`omim`](https://bioregistry.io/omim)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `OMIM:PS267700` |              1 | [DOID:0050120](http://purl.obolibrary.org/obo/DOID_0050120) |
| `OMIM:PS275200` |              1 | [DOID:0050328](http://purl.obolibrary.org/obo/DOID_0050328) |
| `OMIM:PS608415` |              1 | [DOID:0050335](http://purl.obolibrary.org/obo/DOID_0050335) |
| `OMIM:PS175100` |              1 | [DOID:0050424](http://purl.obolibrary.org/obo/DOID_0050424) |
| `OMIM:PS102300` |              1 | [DOID:0050425](http://purl.obolibrary.org/obo/DOID_0050425) |
| `OMIM:PS107970` |              1 | [DOID:0050431](http://purl.obolibrary.org/obo/DOID_0050431) |
| `OMIM:PS608638` |              1 | [DOID:0050432](http://purl.obolibrary.org/obo/DOID_0050432) |
| `OMIM:PS276900` |              1 | [DOID:0050439](http://purl.obolibrary.org/obo/DOID_0050439) |
| `OMIM:PS151660` |              1 | [DOID:0050440](http://purl.obolibrary.org/obo/DOID_0050440) |
| `OMIM:PS193900` |              1 | [DOID:0050448](http://purl.obolibrary.org/obo/DOID_0050448) |
| `OMIM:PS167200` |              1 | [DOID:0050449](http://purl.obolibrary.org/obo/DOID_0050449) |
| `OMIM:PS601144` |              1 | [DOID:0050451](http://purl.obolibrary.org/obo/DOID_0050451) |
| `OMIM:PS607432` |              1 | [DOID:0050453](http://purl.obolibrary.org/obo/DOID_0050453) |
| `OMIM:PS133200` |              1 | [DOID:0050467](http://purl.obolibrary.org/obo/DOID_0050467) |
| `OMIM:PS277600` |              1 | [DOID:0050475](http://purl.obolibrary.org/obo/DOID_0050475) |
| `OMIM:PS138800` |              1 | [DOID:0050489](http://purl.obolibrary.org/obo/DOID_0050489) |
| `OMIM:PS310500` |              1 | [DOID:0050534](http://purl.obolibrary.org/obo/DOID_0050534) |
| `OMIM:PS133780` |              1 | [DOID:0050535](http://purl.obolibrary.org/obo/DOID_0050535) |
| `OMIM:PS306955` |              1 | [DOID:0050545](http://purl.obolibrary.org/obo/DOID_0050545) |
| `OMIM:PS162400` |              1 | [DOID:0050548](http://purl.obolibrary.org/obo/DOID_0050548) |
| `OMIM:PS124900` |              1 | [DOID:0050564](http://purl.obolibrary.org/obo/DOID_0050564) |
| `OMIM:PS220290` |              1 | [DOID:0050565](http://purl.obolibrary.org/obo/DOID_0050565) |
| `OMIM:PS304500` |              1 | [DOID:0050566](http://purl.obolibrary.org/obo/DOID_0050566) |
| `OMIM:PS119530` |              1 | [DOID:0050567](http://purl.obolibrary.org/obo/DOID_0050567) |
| `OMIM:PS277300` |              1 | [DOID:0050568](http://purl.obolibrary.org/obo/DOID_0050568) |
| `OMIM:PS210600` |              1 | [DOID:0050569](http://purl.obolibrary.org/obo/DOID_0050569) |
| `OMIM:PS212065` |              1 | [DOID:0050570](http://purl.obolibrary.org/obo/DOID_0050570) |
| `OMIM:PS212066` |              1 | [DOID:0050571](http://purl.obolibrary.org/obo/DOID_0050571) |
| `OMIM:PS600721` |              1 | [DOID:0050575](http://purl.obolibrary.org/obo/DOID_0050575) |
| `OMIM:PS266900` |              1 | [DOID:0050576](http://purl.obolibrary.org/obo/DOID_0050576) |
| `OMIM:PS218330` |              1 | [DOID:0050577](http://purl.obolibrary.org/obo/DOID_0050577) |
| `OMIM:PS153100` |              1 | [DOID:0050580](http://purl.obolibrary.org/obo/DOID_0050580) |
| `OMIM:PS608594` |              1 | [DOID:0050585](http://purl.obolibrary.org/obo/DOID_0050585) |
| `OMIM:PS266600` |              1 | [DOID:0050589](http://purl.obolibrary.org/obo/DOID_0050589) |
| `OMIM:PS202700` |              1 | [DOID:0050590](http://purl.obolibrary.org/obo/DOID_0050590) |
| `OMIM:PS106600` |              1 | [DOID:0050591](http://purl.obolibrary.org/obo/DOID_0050591) |
| `OMIM:PS208500` |              1 | [DOID:0050592](http://purl.obolibrary.org/obo/DOID_0050592) |
| `OMIM:PS604348` |              1 | [DOID:0050628](http://purl.obolibrary.org/obo/DOID_0050628) |
| `OMIM:PS225750` |              1 | [DOID:0050629](http://purl.obolibrary.org/obo/DOID_0050629) |
| `OMIM:PS203100` |              1 | [DOID:0050632](http://purl.obolibrary.org/obo/DOID_0050632) |
| `OMIM:PS104290` |              1 | [DOID:0050635](http://purl.obolibrary.org/obo/DOID_0050635) |
| `OMIM:PS105250` |              1 | [DOID:0050639](http://purl.obolibrary.org/obo/DOID_0050639) |
| `OMIM:PS108120` |              1 | [DOID:0050646](http://purl.obolibrary.org/obo/DOID_0050646) |
| `OMIM:PS608583` |              1 | [DOID:0050650](http://purl.obolibrary.org/obo/DOID_0050650) |
| `OMIM:PS211530` |              1 | [DOID:0050694](http://purl.obolibrary.org/obo/DOID_0050694) |
| `OMIM:PS210200` |              1 | [DOID:0050710](http://purl.obolibrary.org/obo/DOID_0050710) |
| `OMIM:PS607426` |              1 | [DOID:0050730](http://purl.obolibrary.org/obo/DOID_0050730) |
| `OMIM:PS208085` |              1 | [DOID:0050763](http://purl.obolibrary.org/obo/DOID_0050763) |
| `OMIM:PS168000` |              1 | [DOID:0050773](http://purl.obolibrary.org/obo/DOID_0050773) |
| `OMIM:PS309530` |              1 | [DOID:0050776](http://purl.obolibrary.org/obo/DOID_0050776) |
| `OMIM:PS213300` |              1 | [DOID:0050777](http://purl.obolibrary.org/obo/DOID_0050777) |
| `OMIM:PS249000` |              1 | [DOID:0050778](http://purl.obolibrary.org/obo/DOID_0050778) |
| `OMIM:PS236680` |              1 | [DOID:0050779](http://purl.obolibrary.org/obo/DOID_0050779) |
| `OMIM:PS185800` |              1 | [DOID:0050788](http://purl.obolibrary.org/obo/DOID_0050788) |
| `OMIM:PS186500` |              1 | [DOID:0050794](http://purl.obolibrary.org/obo/DOID_0050794) |
| `OMIM:PS300352` |              1 | [DOID:0050798](http://purl.obolibrary.org/obo/DOID_0050798) |
| `OMIM:PS236730` |              1 | [DOID:0050816](http://purl.obolibrary.org/obo/DOID_0050816) |
| `OMIM:PS233400` |              1 | [DOID:0050857](http://purl.obolibrary.org/obo/DOID_0050857) |
| `OMIM:PS167320` |              1 | [DOID:0050881](http://purl.obolibrary.org/obo/DOID_0050881) |
| `OMIM:PS213200` |              1 | [DOID:0050950](http://purl.obolibrary.org/obo/DOID_0050950) |
| `OMIM:PS601764` |              1 | [DOID:0060169](http://purl.obolibrary.org/obo/DOID_0060169) |
| `OMIM:PS257920` |              1 | [DOID:0060225](http://purl.obolibrary.org/obo/DOID_0060225) |
| `OMIM:PS100300` |              1 | [DOID:0060227](http://purl.obolibrary.org/obo/DOID_0060227) |
| `OMIM:PS105800` |              1 | [DOID:0060228](http://purl.obolibrary.org/obo/DOID_0060228) |
| `OMIM:PS243310` |              1 | [DOID:0060229](http://purl.obolibrary.org/obo/DOID_0060229) |
| `OMIM:PS115150` |              1 | [DOID:0060233](http://purl.obolibrary.org/obo/DOID_0060233) |
| `OMIM:PS278300` |              1 | [DOID:0060236](http://purl.obolibrary.org/obo/DOID_0060236) |
| `OMIM:PS600118` |              1 | [DOID:0060237](http://purl.obolibrary.org/obo/DOID_0060237) |
| `OMIM:PS601390` |              1 | [DOID:0060238](http://purl.obolibrary.org/obo/DOID_0060238) |
| `OMIM:PS600630` |              1 | [DOID:0060240](http://purl.obolibrary.org/obo/DOID_0060240) |
| `OMIM:PS607326` |              1 | [DOID:0060247](http://purl.obolibrary.org/obo/DOID_0060247) |
| `OMIM:PS269500` |              1 | [DOID:0060251](http://purl.obolibrary.org/obo/DOID_0060251) |
| `OMIM:PS268310` |              1 | [DOID:0060254](http://purl.obolibrary.org/obo/DOID_0060254) |
| `OMIM:PS607596` |              1 | [DOID:0060264](http://purl.obolibrary.org/obo/DOID_0060264) |
| `OMIM:PS609060` |              1 | [DOID:0060286](http://purl.obolibrary.org/obo/DOID_0060286) |
| `OMIM:PS258315` |              1 | [DOID:0060288](http://purl.obolibrary.org/obo/DOID_0060288) |
| `OMIM:PS272430` |              1 | [DOID:0060294](http://purl.obolibrary.org/obo/DOID_0060294) |
| `OMIM:PS224690` |              1 | [DOID:0060306](http://purl.obolibrary.org/obo/DOID_0060306) |
| `OMIM:PS156200` |              1 | [DOID:0060307](http://purl.obolibrary.org/obo/DOID_0060307) |
| `OMIM:PS249500` |              1 | [DOID:0060308](http://purl.obolibrary.org/obo/DOID_0060308) |
| `OMIM:PS309510` |              1 | [DOID:0060309](http://purl.obolibrary.org/obo/DOID_0060309) |
| `OMIM:PS250950` |              1 | [DOID:0060336](http://purl.obolibrary.org/obo/DOID_0060336) |
| `OMIM:PS122100` |              1 | [DOID:0060451](http://purl.obolibrary.org/obo/DOID_0060451) |
| `OMIM:PS122000` |              1 | [DOID:0060457](http://purl.obolibrary.org/obo/DOID_0060457) |
| `OMIM:PS228520` |              1 | [DOID:0060465](http://purl.obolibrary.org/obo/DOID_0060465) |
| `OMIM:PS253310` |              1 | [DOID:0060558](http://purl.obolibrary.org/obo/DOID_0060558) |
| `OMIM:PS220210` |              1 | [DOID:0060565](http://purl.obolibrary.org/obo/DOID_0060565) |
| `OMIM:PS605552` |              1 | [DOID:0060611](http://purl.obolibrary.org/obo/DOID_0060611) |
| `OMIM:PS107250` |              1 | [DOID:0060648](http://purl.obolibrary.org/obo/DOID_0060648) |
| `OMIM:PS242300` |              1 | [DOID:0060655](http://purl.obolibrary.org/obo/DOID_0060655) |
| `OMIM:PS604772` |              1 | [DOID:0060674](http://purl.obolibrary.org/obo/DOID_0060674) |
| `OMIM:PS600513` |              1 | [DOID:0060681](http://purl.obolibrary.org/obo/DOID_0060681) |
| `OMIM:PS149400` |              1 | [DOID:0060695](http://purl.obolibrary.org/obo/DOID_0060695) |
| `OMIM:PS145980` |              1 | [DOID:0060699](http://purl.obolibrary.org/obo/DOID_0060699) |
| `OMIM:PS308240` |              1 | [DOID:0060704](http://purl.obolibrary.org/obo/DOID_0060704) |
| `OMIM:PS275210` |              1 | [DOID:0060762](http://purl.obolibrary.org/obo/DOID_0060762) |
| `OMIM:PS214700` |              1 | [DOID:0060774](http://purl.obolibrary.org/obo/DOID_0060774) |
| `OMIM:PS312080` |              1 | [DOID:0060786](http://purl.obolibrary.org/obo/DOID_0060786) |
| `OMIM:PS214450` |              1 | [DOID:0060831](http://purl.obolibrary.org/obo/DOID_0060831) |
| `OMIM:PS169150` |              1 | [DOID:0060863](http://purl.obolibrary.org/obo/DOID_0060863) |
| `OMIM:PS603896` |              1 | [DOID:0060868](http://purl.obolibrary.org/obo/DOID_0060868) |
| `OMIM:PS602014` |              1 | [DOID:0060879](http://purl.obolibrary.org/obo/DOID_0060879) |
| `OMIM:PS254130` |              1 | [DOID:0070198](http://purl.obolibrary.org/obo/DOID_0070198) |
| `OMIM:PS211600` |              1 | [DOID:0070221](http://purl.obolibrary.org/obo/DOID_0070221) |
| `OMIM:PS243300` |              1 | [DOID:0070230](http://purl.obolibrary.org/obo/DOID_0070230) |
| `OMIM:PS251200` |              1 | [DOID:0070296](http://purl.obolibrary.org/obo/DOID_0070296) |
| `OMIM:PS603041` |              1 | [DOID:0070329](http://purl.obolibrary.org/obo/DOID_0070329) |
| `OMIM:PS605711` |              1 | [DOID:0070330](http://purl.obolibrary.org/obo/DOID_0070330) |
| `OMIM:PS158600` |              1 | [DOID:0070348](http://purl.obolibrary.org/obo/DOID_0070348) |
| `OMIM:PS239300` |              1 | [DOID:0070431](http://purl.obolibrary.org/obo/DOID_0070431) |
| `OMIM:PS136550` |              1 | [DOID:0070438](http://purl.obolibrary.org/obo/DOID_0070438) |
| `OMIM:PS123000` |              1 | [DOID:0080033](http://purl.obolibrary.org/obo/DOID_0080033) |
| `OMIM:PS200600` |              1 | [DOID:0080043](http://purl.obolibrary.org/obo/DOID_0080043) |
| `OMIM:PS108300` |              1 | [DOID:0080046](http://purl.obolibrary.org/obo/DOID_0080046) |
| `OMIM:PS178110` |              1 | [DOID:0080110](http://purl.obolibrary.org/obo/DOID_0080110) |
| `OMIM:PS135700` |              1 | [DOID:0080143](http://purl.obolibrary.org/obo/DOID_0080143) |
| `OMIM:PS610805` |              1 | [DOID:0080205](http://purl.obolibrary.org/obo/DOID_0080205) |
| `OMIM:PS601419` |              1 | [DOID:0080307](http://purl.obolibrary.org/obo/DOID_0080307) |
| `OMIM:PS604004` |              1 | [DOID:0080315](http://purl.obolibrary.org/obo/DOID_0080315) |
| `OMIM:PS173900` |              1 | [DOID:0080322](http://purl.obolibrary.org/obo/DOID_0080322) |
| `OMIM:PS192600` |              1 | [DOID:0080326](http://purl.obolibrary.org/obo/DOID_0080326) |
| `OMIM:PS109730` |              1 | [DOID:0080332](http://purl.obolibrary.org/obo/DOID_0080332) |
| `OMIM:PS119580` |              1 | [DOID:0080344](http://purl.obolibrary.org/obo/DOID_0080344) |
| `OMIM:PS214100` |              1 | [DOID:0080377](http://purl.obolibrary.org/obo/DOID_0080377) |
| `OMIM:PS614080` |              1 | [DOID:0080503](http://purl.obolibrary.org/obo/DOID_0080503) |
| `OMIM:PS613280` |              1 | [DOID:0080535](http://purl.obolibrary.org/obo/DOID_0080535) |
| `OMIM:PS308230` |              1 | [DOID:0080544](http://purl.obolibrary.org/obo/DOID_0080544) |
| `OMIM:PS147060` |              1 | [DOID:0080545](http://purl.obolibrary.org/obo/DOID_0080545) |
| `OMIM:PS610253` |              1 | [DOID:0080597](http://purl.obolibrary.org/obo/DOID_0080597) |
| `OMIM:PS202200` |              1 | [DOID:0080620](http://purl.obolibrary.org/obo/DOID_0080620) |
| `OMIM:PS203650` |              1 | [DOID:0080627](http://purl.obolibrary.org/obo/DOID_0080627) |
| `OMIM:PS600165` |              1 | [DOID:0080634](http://purl.obolibrary.org/obo/DOID_0080634) |
| `OMIM:PS309800` |              1 | [DOID:0080636](http://purl.obolibrary.org/obo/DOID_0080636) |
| `OMIM:PS612286` |              1 | [DOID:0080655](http://purl.obolibrary.org/obo/DOID_0080655) |
| `OMIM:PS161050` |              1 | [DOID:0080683](http://purl.obolibrary.org/obo/DOID_0080683) |
| `OMIM:PS257300` |              1 | [DOID:0080688](http://purl.obolibrary.org/obo/DOID_0080688) |
| `OMIM:PS251300` |              1 | [DOID:0080694](http://purl.obolibrary.org/obo/DOID_0080694) |
| `OMIM:PS615438` |              1 | [DOID:0080716](http://purl.obolibrary.org/obo/DOID_0080716) |
| `OMIM:PS127000` |              1 | [DOID:0080724](http://purl.obolibrary.org/obo/DOID_0080724) |
| `OMIM:PS214150` |              1 | [DOID:0080910](http://purl.obolibrary.org/obo/DOID_0080910) |
| `OMIM:PS607095` |              1 | [DOID:0080942](http://purl.obolibrary.org/obo/DOID_0080942) |
| `OMIM:PS617468` |              1 | [DOID:0080954](http://purl.obolibrary.org/obo/DOID_0080954) |
| `OMIM:PS136760` |              1 | [DOID:0081044](http://purl.obolibrary.org/obo/DOID_0081044) |
| `OMIM:PS213980` |              1 | [DOID:0081072](http://purl.obolibrary.org/obo/DOID_0081072) |
| `OMIM:PS145420` |              1 | [DOID:0081073](http://purl.obolibrary.org/obo/DOID_0081073) |
| `OMIM:PS300291` |              1 | [DOID:0081077](http://purl.obolibrary.org/obo/DOID_0081077) |
| `OMIM:PS613339` |              1 | [DOID:0081104](http://purl.obolibrary.org/obo/DOID_0081104) |
| `OMIM:PS248370` |              1 | [DOID:0081127](http://purl.obolibrary.org/obo/DOID_0081127) |
| `OMIM:PS164310` |              1 | [DOID:0081296](http://purl.obolibrary.org/obo/DOID_0081296) |
| `OMIM:PS149730` |              1 | [DOID:0081370](http://purl.obolibrary.org/obo/DOID_0081370) |
| `OMIM:PS219000` |              1 | [DOID:0090001](http://purl.obolibrary.org/obo/DOID_0090001) |
| `OMIM:PS242860` |              1 | [DOID:0090007](http://purl.obolibrary.org/obo/DOID_0090007) |
| `OMIM:PS183600` |              1 | [DOID:0090020](http://purl.obolibrary.org/obo/DOID_0090020) |
| `OMIM:PS120100` |              1 | [DOID:0090061](http://purl.obolibrary.org/obo/DOID_0090061) |
| `OMIM:PS147950` |              1 | [DOID:0090070](http://purl.obolibrary.org/obo/DOID_0090070) |
| `OMIM:PS601198` |              1 | [DOID:0090109](http://purl.obolibrary.org/obo/DOID_0090109) |
| `OMIM:PS614039` |              1 | [DOID:0090131](http://purl.obolibrary.org/obo/DOID_0090131) |
| `OMIM:PS604931` |              1 | [DOID:0090139](http://purl.obolibrary.org/obo/DOID_0090139) |
| `OMIM:PS603511` |              1 | [DOID:0110273](http://purl.obolibrary.org/obo/DOID_0110273) |
| `OMIM:PS253600` |              1 | [DOID:0110274](http://purl.obolibrary.org/obo/DOID_0110274) |
| `OMIM:PS234200` |              1 | [DOID:0110734](http://purl.obolibrary.org/obo/DOID_0110734) |
| `OMIM:PS113900` |              1 | [DOID:0111073](http://purl.obolibrary.org/obo/DOID_0111073) |
| `OMIM:PS252150` |              1 | [DOID:0111165](http://purl.obolibrary.org/obo/DOID_0111165) |
| `OMIM:PS236670` |              1 | [DOID:0111229](http://purl.obolibrary.org/obo/DOID_0111229) |
| `OMIM:PS121210` |              1 | [DOID:0111297](http://purl.obolibrary.org/obo/DOID_0111297) |
| `OMIM:PS208150` |              1 | [DOID:0111375](http://purl.obolibrary.org/obo/DOID_0111375) |
| `OMIM:PS222470` |              1 | [DOID:0111414](http://purl.obolibrary.org/obo/DOID_0111414) |
| `OMIM:PS601068` |              1 | [DOID:0111689](http://purl.obolibrary.org/obo/DOID_0111689) |
| `OMIM:PS231050` |              1 | [DOID:0111724](http://purl.obolibrary.org/obo/DOID_0111724) |
| `OMIM:PS615040` |              1 | [DOID:0111728](http://purl.obolibrary.org/obo/DOID_0111728) |
| `OMIM:PS400043` |              1 | [DOID:0111757](http://purl.obolibrary.org/obo/DOID_0111757) |
| `OMIM:PS305620` |              1 | [DOID:0111785](http://purl.obolibrary.org/obo/DOID_0111785) |
| `OMIM:PS601675` |              1 | [DOID:0111866](http://purl.obolibrary.org/obo/DOID_0111866) |
| `OMIM:PS309801` |              1 | [DOID:0111875](http://purl.obolibrary.org/obo/DOID_0111875) |
| `OMIM:PS258150` |              1 | [DOID:0111910](http://purl.obolibrary.org/obo/DOID_0111910) |
| `OMIM:PS252010` |              1 | [DOID:0112065](http://purl.obolibrary.org/obo/DOID_0112065) |
| `OMIM:PS271640` |              1 | [DOID:0112197](http://purl.obolibrary.org/obo/DOID_0112197) |
| `OMIM:PS308350` |              1 | [DOID:0112202](http://purl.obolibrary.org/obo/DOID_0112202) |
| `OMIM:PS175780` |              1 | [DOID:0112313](http://purl.obolibrary.org/obo/DOID_0112313) |
| `OMIM:PS613155` |              1 | [DOID:0112375](http://purl.obolibrary.org/obo/DOID_0112375) |
| `OMIM:PS118100` |              1 | [DOID:10426](http://purl.obolibrary.org/obo/DOID_10426)     |
| `OMIM:PS268000` |              1 | [DOID:10584](http://purl.obolibrary.org/obo/DOID_10584)     |
| `OMIM:PS118220` |              1 | [DOID:10595](http://purl.obolibrary.org/obo/DOID_10595)     |
| `OMIM:PS134600` |              1 | [DOID:1062](http://purl.obolibrary.org/obo/DOID_1062)       |
| `OMIM:PS133100` |              1 | [DOID:10780](http://purl.obolibrary.org/obo/DOID_10780)     |
| `OMIM:PS603075` |              1 | [DOID:10871](http://purl.obolibrary.org/obo/DOID_10871)     |
| `OMIM:PS612900` |              1 | [DOID:10970](http://purl.obolibrary.org/obo/DOID_10970)     |
| `OMIM:PS122470` |              1 | [DOID:11725](http://purl.obolibrary.org/obo/DOID_11725)     |
| `OMIM:PS310300` |              1 | [DOID:11726](http://purl.obolibrary.org/obo/DOID_11726)     |
| `OMIM:PS115430` |              1 | [DOID:12169](http://purl.obolibrary.org/obo/DOID_12169)     |
| `OMIM:PS607594` |              1 | [DOID:12177](http://purl.obolibrary.org/obo/DOID_12177)     |
| `OMIM:PS109720` |              1 | [DOID:12236](http://purl.obolibrary.org/obo/DOID_12236)     |
| `OMIM:PS166200` |              1 | [DOID:12347](http://purl.obolibrary.org/obo/DOID_12347)     |
| `OMIM:PS157640` |              1 | [DOID:12558](http://purl.obolibrary.org/obo/DOID_12558)     |
| `OMIM:PS256100` |              1 | [DOID:12712](http://purl.obolibrary.org/obo/DOID_12712)     |
| `OMIM:PS607014` |              1 | [DOID:12798](http://purl.obolibrary.org/obo/DOID_12798)     |
| `OMIM:PS115200` |              1 | [DOID:12930](http://purl.obolibrary.org/obo/DOID_12930)     |
| `OMIM:PS603278` |              1 | [DOID:1312](http://purl.obolibrary.org/obo/DOID_1312)       |
| `OMIM:PS256450` |              1 | [DOID:13317](http://purl.obolibrary.org/obo/DOID_13317)     |
| `OMIM:PS130000` |              1 | [DOID:13359](http://purl.obolibrary.org/obo/DOID_13359)     |
| `OMIM:PS224120` |              1 | [DOID:1338](http://purl.obolibrary.org/obo/DOID_1338)       |
| `OMIM:PS105650` |              1 | [DOID:1339](http://purl.obolibrary.org/obo/DOID_1339)       |
| `OMIM:PS191100` |              1 | [DOID:13515](http://purl.obolibrary.org/obo/DOID_13515)     |
| `OMIM:PS259700` |              1 | [DOID:13533](http://purl.obolibrary.org/obo/DOID_13533)     |
| `OMIM:PS607634` |              1 | [DOID:13533](http://purl.obolibrary.org/obo/DOID_13533)     |
| `OMIM:PS227650` |              1 | [DOID:13636](http://purl.obolibrary.org/obo/DOID_13636)     |
| `OMIM:PS226400` |              1 | [DOID:13777](http://purl.obolibrary.org/obo/DOID_13777)     |
| `OMIM:PS125310` |              1 | [DOID:13945](http://purl.obolibrary.org/obo/DOID_13945)     |
| `OMIM:PS151100` |              1 | [DOID:14291](http://purl.obolibrary.org/obo/DOID_14291)     |
| `OMIM:PS168600` |              1 | [DOID:14330](http://purl.obolibrary.org/obo/DOID_14330)     |
| `OMIM:PS164400` |              1 | [DOID:1441](http://purl.obolibrary.org/obo/DOID_1441)       |
| `OMIM:PS400044` |              1 | [DOID:14448](http://purl.obolibrary.org/obo/DOID_14448)     |
| `OMIM:PS233300` |              1 | [DOID:14450](http://purl.obolibrary.org/obo/DOID_14450)     |
| `OMIM:PS256730` |              1 | [DOID:14503](http://purl.obolibrary.org/obo/DOID_14503)     |
| `OMIM:PS117550` |              1 | [DOID:14748](http://purl.obolibrary.org/obo/DOID_14748)     |
| `OMIM:PS204000` |              1 | [DOID:14791](http://purl.obolibrary.org/obo/DOID_14791)     |
| `OMIM:PS108800` |              1 | [DOID:1882](http://purl.obolibrary.org/obo/DOID_1882)       |
| `OMIM:PS135900` |              1 | [DOID:1925](http://purl.obolibrary.org/obo/DOID_1925)       |
| `OMIM:PS209900` |              1 | [DOID:1935](http://purl.obolibrary.org/obo/DOID_1935)       |
| `OMIM:PS305100` |              1 | [DOID:2121](http://purl.obolibrary.org/obo/DOID_2121)       |
| `OMIM:PS104500` |              1 | [DOID:2187](http://purl.obolibrary.org/obo/DOID_2187)       |
| `OMIM:PS235200` |              1 | [DOID:2352](http://purl.obolibrary.org/obo/DOID_2352)       |
| `OMIM:PS188050` |              1 | [DOID:2452](http://purl.obolibrary.org/obo/DOID_2452)       |
| `OMIM:PS303350` |              1 | [DOID:2476](http://purl.obolibrary.org/obo/DOID_2476)       |
| `OMIM:PS109400` |              1 | [DOID:2512](http://purl.obolibrary.org/obo/DOID_2512)       |
| `OMIM:PS215100` |              1 | [DOID:2580](http://purl.obolibrary.org/obo/DOID_2580)       |
| `OMIM:PS601495` |              1 | [DOID:2583](http://purl.obolibrary.org/obo/DOID_2583)       |
| `OMIM:PS256300` |              1 | [DOID:2590](http://purl.obolibrary.org/obo/DOID_2590)       |
| `OMIM:PS127550` |              1 | [DOID:2729](http://purl.obolibrary.org/obo/DOID_2729)       |
| `OMIM:PS192500` |              1 | [DOID:2843](http://purl.obolibrary.org/obo/DOID_2843)       |
| `OMIM:PS154500` |              1 | [DOID:2908](http://purl.obolibrary.org/obo/DOID_2908)       |
| `OMIM:PS259900` |              1 | [DOID:2977](http://purl.obolibrary.org/obo/DOID_2977)       |
| `OMIM:PS151623` |              1 | [DOID:3012](http://purl.obolibrary.org/obo/DOID_3012)       |
| `OMIM:PS137800` |              1 | [DOID:3070](http://purl.obolibrary.org/obo/DOID_3070)       |
| `OMIM:PS123700` |              1 | [DOID:3144](http://purl.obolibrary.org/obo/DOID_3144)       |
| `OMIM:PS161800` |              1 | [DOID:3191](http://purl.obolibrary.org/obo/DOID_3191)       |
| `OMIM:PS306400` |              1 | [DOID:3265](http://purl.obolibrary.org/obo/DOID_3265)       |
| `OMIM:PS603165` |              1 | [DOID:3310](http://purl.obolibrary.org/obo/DOID_3310)       |
| `OMIM:PS105400` |              1 | [DOID:332](http://purl.obolibrary.org/obo/DOID_332)         |
| `OMIM:PS600512` |              1 | [DOID:3328](http://purl.obolibrary.org/obo/DOID_3328)       |
| `OMIM:PS163950` |              1 | [DOID:3490](http://purl.obolibrary.org/obo/DOID_3490)       |
| `OMIM:PS601462` |              1 | [DOID:3635](http://purl.obolibrary.org/obo/DOID_3635)       |
| `OMIM:PS203300` |              1 | [DOID:3753](http://purl.obolibrary.org/obo/DOID_3753)       |
| `OMIM:PS220110` |              1 | [DOID:3762](http://purl.obolibrary.org/obo/DOID_3762)       |
| `OMIM:PS102200` |              1 | [DOID:3829](http://purl.obolibrary.org/obo/DOID_3829)       |
| `OMIM:PS120435` |              1 | [DOID:3883](http://purl.obolibrary.org/obo/DOID_3883)       |
| `OMIM:PS115210` |              1 | [DOID:397](http://purl.obolibrary.org/obo/DOID_397)         |
| `OMIM:PS601678` |              1 | [DOID:445](http://purl.obolibrary.org/obo/DOID_445)         |
| `OMIM:PS605389` |              1 | [DOID:4535](http://purl.obolibrary.org/obo/DOID_4535)       |
| `OMIM:PS113800` |              1 | [DOID:4603](http://purl.obolibrary.org/obo/DOID_4603)       |
| `OMIM:PS236100` |              1 | [DOID:4621](http://purl.obolibrary.org/obo/DOID_4621)       |
| `OMIM:PS190300` |              1 | [DOID:4990](http://purl.obolibrary.org/obo/DOID_4990)       |
| `OMIM:PS167250` |              1 | [DOID:5408](http://purl.obolibrary.org/obo/DOID_5408)       |
| `OMIM:PS311360` |              1 | [DOID:5426](http://purl.obolibrary.org/obo/DOID_5426)       |
| `OMIM:PS128100` |              1 | [DOID:543](http://purl.obolibrary.org/obo/DOID_543)         |
| `OMIM:PS265450` |              1 | [DOID:5453](http://purl.obolibrary.org/obo/DOID_5453)       |
| `OMIM:PS165500` |              1 | [DOID:5723](http://purl.obolibrary.org/obo/DOID_5723)       |
| `OMIM:PS300755` |              1 | [DOID:612](http://purl.obolibrary.org/obo/DOID_612)         |
| `OMIM:PS158350` |              1 | [DOID:6457](http://purl.obolibrary.org/obo/DOID_6457)       |
| `OMIM:PS106300` |              1 | [DOID:7147](http://purl.obolibrary.org/obo/DOID_7147)       |
| `OMIM:PS116200` |              1 | [DOID:83](http://purl.obolibrary.org/obo/DOID_83)           |
| `OMIM:PS145600` |              1 | [DOID:8545](http://purl.obolibrary.org/obo/DOID_8545)       |
| `OMIM:PS177900` |              1 | [DOID:8893](http://purl.obolibrary.org/obo/DOID_8893)       |
| `OMIM:PS254800` |              1 | [DOID:891](http://purl.obolibrary.org/obo/DOID_891)         |
| `OMIM:PS300751` |              1 | [DOID:8955](http://purl.obolibrary.org/obo/DOID_8955)       |
| `OMIM:PS193500` |              1 | [DOID:9258](http://purl.obolibrary.org/obo/DOID_9258)       |
| `OMIM:PS613038` |              1 | [DOID:9410](http://purl.obolibrary.org/obo/DOID_9410)       |
| `OMIM:PS244400` |              1 | [DOID:9562](http://purl.obolibrary.org/obo/DOID_9562)       |
| `OMIM:PS211400` |              1 | [DOID:9563](http://purl.obolibrary.org/obo/DOID_9563)       |
| `OMIM:PS310700` |              1 | [DOID:9649](http://purl.obolibrary.org/obo/DOID_9649)       |
| `OMIM:PS203655` |              1 | [DOID:987](http://purl.obolibrary.org/obo/DOID_987)         |

## `PATO`: Phenotype And Trait Ontology

Overall, there were 69 invalid
xrefs to external prefixed with `PATO` (standardized to Bioregistry
prefix [`pato`](https://bioregistry.io/pato)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PATO:GVG`      |             54 | [PATO:0000911](http://purl.obolibrary.org/obo/PATO_0000911), [PATO:0000912](http://purl.obolibrary.org/obo/PATO_0000912), [PATO:0001153](http://purl.obolibrary.org/obo/PATO_0001153), [PATO:0001304](http://purl.obolibrary.org/obo/PATO_0001304), [PATO:0001313](http://purl.obolibrary.org/obo/PATO_0001313), ... |
| `PATO:MAH`      |              8 | [PATO:0000428](http://purl.obolibrary.org/obo/PATO_0000428), [PATO:0001559](http://purl.obolibrary.org/obo/PATO_0001559), [PATO:0001624](http://purl.obolibrary.org/obo/PATO_0001624), [PATO:0001625](http://purl.obolibrary.org/obo/PATO_0001625), [PATO:0002629](http://purl.obolibrary.org/obo/PATO_0002629), ... |
| `PATO:LC`       |              2 | [PATO:0000694](http://purl.obolibrary.org/obo/PATO_0000694), [PATO:0002363](http://purl.obolibrary.org/obo/PATO_0002363)                                                                                                                                                                                             |
| `PATO:WS`       |              1 | [PATO:0002311](http://purl.obolibrary.org/obo/PATO_0002311)                                                                                                                                                                                                                                                          |
| `PATO:WC`       |              1 | [PATO:0002320](http://purl.obolibrary.org/obo/PATO_0002320)                                                                                                                                                                                                                                                          |
| `PATO:PG`       |              1 | [PATO:0002389](http://purl.obolibrary.org/obo/PATO_0002389)                                                                                                                                                                                                                                                          |
| `PATO:DS`       |              1 | [PATO:0002390](http://purl.obolibrary.org/obo/PATO_0002390)                                                                                                                                                                                                                                                          |
| `PATO:JL`       |              1 | [PATO:0002454](http://purl.obolibrary.org/obo/PATO_0002454)                                                                                                                                                                                                                                                          |

## `PBA`: Primate Brain Atlas

Overall, there were 1 invalid
xrefs to external prefixed with `PBA` (standardized to Bioregistry
prefix [`pba`](https://bioregistry.io/pba)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `PBA:BN`        |              1 | [UBERON:0010011](http://purl.obolibrary.org/obo/UBERON_0010011) |

## `PDBeChem`: Chemical Component Dictionary

Overall, there were 6 invalid
xrefs to external prefixed with `PDBeChem` (standardized to Bioregistry
prefix [`pdb-ccd`](https://bioregistry.io/pdb-ccd)) that
did not match the standard pattern `^\w{1,3}$`.

| external_xref       |   usages_count | usages                                                    |
|---------------------|----------------|-----------------------------------------------------------|
| `PDBeChem:LEU_LFOH` |              1 | [CHEBI:15603](http://purl.obolibrary.org/obo/CHEBI_15603) |
| `PDBeChem:DAH_LFOH` |              1 | [CHEBI:15765](http://purl.obolibrary.org/obo/CHEBI_15765) |
| `PDBeChem:GLU_LFOH` |              1 | [CHEBI:16015](http://purl.obolibrary.org/obo/CHEBI_16015) |
| `PDBeChem:MET_LFOH` |              1 | [CHEBI:16643](http://purl.obolibrary.org/obo/CHEBI_16643) |
| `PDBeChem:ALA_LFOH` |              1 | [CHEBI:16977](http://purl.obolibrary.org/obo/CHEBI_16977) |
| `PDBeChem:ORN_LFOH` |              1 | [CHEBI:44667](http://purl.obolibrary.org/obo/CHEBI_44667) |

## `PID`: NCI Pathway Interaction Database: Pathway

Overall, there were 10 invalid
xrefs to external prefixed with `PID` (standardized to Bioregistry
prefix [`pid.pathway`](https://bioregistry.io/pid.pathway)) that
did not match the standard pattern `^\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b$`.

| external_xref                       |   usages_count | usages                                                                                                                   |
|-------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------|
| `PID:TGFB/TGFBR2/TGFBR1`            |              2 | [PR:000003176](http://purl.obolibrary.org/obo/PR_000003176), [PR:000025962](http://purl.obolibrary.org/obo/PR_000025962) |
| `PID:SHC`                           |              2 | [PR:000003187](http://purl.obolibrary.org/obo/PR_000003187), [PR:000003190](http://purl.obolibrary.org/obo/PR_000003190) |
| `PID:cd8tcrpathway`                 |              1 | [PR:000003103](http://purl.obolibrary.org/obo/PR_000003103)                                                              |
| `PID:pi3kciaktpathway`              |              1 | [PR:000003103](http://purl.obolibrary.org/obo/PR_000003103)                                                              |
| `PID:ptp1bpathway`                  |              1 | [PR:000003103](http://purl.obolibrary.org/obo/PR_000003103)                                                              |
| `PID:tcrpathway`                    |              1 | [PR:000003103](http://purl.obolibrary.org/obo/PR_000003103)                                                              |
| `PID:TGFB/TGFBR2/TGFBR1/WWP1/SMAD8` |              1 | [PR:000003173](http://purl.obolibrary.org/obo/PR_000003173)                                                              |
| `PID:STRAP`                         |              1 | [PR:000003207](http://purl.obolibrary.org/obo/PR_000003207)                                                              |

## `PIRSF`: PIR Superfamily Classification System

Overall, there were 1 invalid
xrefs to external prefixed with `PIRSF` (standardized to Bioregistry
prefix [`pirsf`](https://bioregistry.io/pirsf)) that
did not match the standard pattern `^PIRSF\d{6}$`.

| external_xref        |   usages_count | usages                                                      |
|----------------------|----------------|-------------------------------------------------------------|
| `PIRSF:PIRSF0000550` |              1 | [PR:000003057](http://purl.obolibrary.org/obo/PR_000003057) |

## `PMC`: PubMed Central

Overall, there were 1 invalid
xrefs to external prefixed with `PMC` (standardized to Bioregistry
prefix [`pmc`](https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `PMC:126017`    |              1 | [SO:0002095](http://purl.obolibrary.org/obo/SO_0002095) |

## `PMID`: PubMed

Overall, there were 21 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                 |   usages_count | usages                                                                                                                                                                                                                                                                                      |
|-------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PMID: 24572720`              |              5 | [SO:0002344](http://purl.obolibrary.org/obo/SO_0002344), [SO:0002345](http://purl.obolibrary.org/obo/SO_0002345), [SO:0002346](http://purl.obolibrary.org/obo/SO_0002346), [SO:0002347](http://purl.obolibrary.org/obo/SO_0002347), [SO:0002348](http://purl.obolibrary.org/obo/SO_0002348) |
| `PMID:12537576:16827941`      |              4 | [SO:0001158](http://purl.obolibrary.org/obo/SO_0001158), [SO:0001159](http://purl.obolibrary.org/obo/SO_0001159), [SO:0001160](http://purl.obolibrary.org/obo/SO_0001160), [SO:0001161](http://purl.obolibrary.org/obo/SO_0001161)                                                          |
| `PMID: 118436`                |              2 | [SO:0002336](http://purl.obolibrary.org/obo/SO_0002336), [SO:0002337](http://purl.obolibrary.org/obo/SO_0002337)                                                                                                                                                                            |
| `PMID: 29474379`              |              2 | [SO:0002336](http://purl.obolibrary.org/obo/SO_0002336), [SO:0002337](http://purl.obolibrary.org/obo/SO_0002337)                                                                                                                                                                            |
| `PMID: 3136294`               |              2 | [SO:0002336](http://purl.obolibrary.org/obo/SO_0002336), [SO:0002337](http://purl.obolibrary.org/obo/SO_0002337)                                                                                                                                                                            |
| `PMID:16827941:12537576`      |              1 | [SO:0001157](http://purl.obolibrary.org/obo/SO_0001157)                                                                                                                                                                                                                                     |
| `PMID:12537576:15231738`      |              1 | [SO:0001162](http://purl.obolibrary.org/obo/SO_0001162)                                                                                                                                                                                                                                     |
| `PMID:15388847,PMID:16524884` |              1 | [SO:0002235](http://purl.obolibrary.org/obo/SO_0002235)                                                                                                                                                                                                                                     |
| `PMID: 19407924`              |              1 | [SO:0002293](http://purl.obolibrary.org/obo/SO_0002293)                                                                                                                                                                                                                                     |
| `PMID: 16236432`              |              1 | [SO:0002350](http://purl.obolibrary.org/obo/SO_0002350)                                                                                                                                                                                                                                     |
| `PMID: 17608616`              |              1 | [SO:0002350](http://purl.obolibrary.org/obo/SO_0002350)                                                                                                                                                                                                                                     |

## `PomBase`: PomBase

Overall, there were 76 invalid
xrefs to external prefixed with `PomBase` (standardized to Bioregistry
prefix [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PomBase:MAH`   |             64 | [PR:000027500](http://purl.obolibrary.org/obo/PR_000027500), [PR:000027503](http://purl.obolibrary.org/obo/PR_000027503), [PR:000027507](http://purl.obolibrary.org/obo/PR_000027507), [PR:000027509](http://purl.obolibrary.org/obo/PR_000027509), [PR:000027512](http://purl.obolibrary.org/obo/PR_000027512), ... |
| `PomBase:mah`   |              6 | [SO:0001808](http://purl.obolibrary.org/obo/SO_0001808), [SO:0001811](http://purl.obolibrary.org/obo/SO_0001811), [SO:0001812](http://purl.obolibrary.org/obo/SO_0001812), [SO:0001813](http://purl.obolibrary.org/obo/SO_0001813), [SO:0001905](http://purl.obolibrary.org/obo/SO_0001905), ...                     |
| `PomBase:al`    |              3 | [SO:0000370](http://purl.obolibrary.org/obo/SO_0000370), [SO:0002022](http://purl.obolibrary.org/obo/SO_0002022), [SO:0002207](http://purl.obolibrary.org/obo/SO_0002207)                                                                                                                                            |
| `PomBase:vw`    |              2 | [SO:0002025](http://purl.obolibrary.org/obo/SO_0002025), [SO:0002215](http://purl.obolibrary.org/obo/SO_0002215)                                                                                                                                                                                                     |
| `PomBase:mh`    |              1 | [SO:0002208](http://purl.obolibrary.org/obo/SO_0002208)                                                                                                                                                                                                                                                              |

## `POMBASE`: PomBase

Overall, there were 3 invalid
xrefs to external prefixed with `POMBASE` (standardized to Bioregistry
prefix [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref   |   usages_count | usages                                                                                                           |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `POMBASE:mah`   |              2 | [SO:0002027](http://purl.obolibrary.org/obo/SO_0002027), [SO:0002028](http://purl.obolibrary.org/obo/SO_0002028) |
| `POMBASE:vw`    |              1 | [SO:0002029](http://purl.obolibrary.org/obo/SO_0002029)                                                          |

## `PRO`: Protein Ontology

Overall, there were 28,110 invalid
xrefs to external prefixed with `PRO` (standardized to Bioregistry
prefix [`pr`](https://bioregistry.io/pr)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                       |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PRO:DNx`       |          22510 | [PR:000001002](http://purl.obolibrary.org/obo/PR_000001002), [PR:000001003](http://purl.obolibrary.org/obo/PR_000001003), [PR:000001004](http://purl.obolibrary.org/obo/PR_000001004), [PR:000001006](http://purl.obolibrary.org/obo/PR_000001006), [PR:000001012](http://purl.obolibrary.org/obo/PR_000001012), ...                                         |
| `PRO:CNA`       |           2772 | [NCBITaxon:204722](http://purl.obolibrary.org/obo/NCBITaxon_204722), [NCBITaxon:224914](http://purl.obolibrary.org/obo/NCBITaxon_224914), [NCBITaxon:262698](http://purl.obolibrary.org/obo/NCBITaxon_262698), [NCBITaxon:359391](http://purl.obolibrary.org/obo/NCBITaxon_359391), [NCBITaxon:444178](http://purl.obolibrary.org/obo/NCBITaxon_444178), ... |
| `PRO:WCB`       |            905 | [PR:000000001](http://purl.obolibrary.org/obo/PR_000000001), [PR:000000679](http://purl.obolibrary.org/obo/PR_000000679), [PR:000000680](http://purl.obolibrary.org/obo/PR_000000680), [PR:000000681](http://purl.obolibrary.org/obo/PR_000000681), [PR:000000687](http://purl.obolibrary.org/obo/PR_000000687), ...                                         |
| `PRO:DAN`       |            562 | [CHEBI:33708](http://purl.obolibrary.org/obo/CHEBI_33708), [MOD:00033](http://purl.obolibrary.org/obo/MOD_00033), [MOD:00127](http://purl.obolibrary.org/obo/MOD_00127), [MOD:00128](http://purl.obolibrary.org/obo/MOD_00128), [MOD:00213](http://purl.obolibrary.org/obo/MOD_00213), ...                                                                   |
| `PRO:HJD`       |            470 | [PR:000000699](http://purl.obolibrary.org/obo/PR_000000699), [PR:000000776](http://purl.obolibrary.org/obo/PR_000000776), [PR:000000777](http://purl.obolibrary.org/obo/PR_000000777), [PR:000000937](http://purl.obolibrary.org/obo/PR_000000937), [PR:000001787](http://purl.obolibrary.org/obo/PR_000001787), ...                                         |
| `PRO:JAN`       |            288 | [PR:000001317](http://purl.obolibrary.org/obo/PR_000001317), [PR:000001318](http://purl.obolibrary.org/obo/PR_000001318), [PR:000001363](http://purl.obolibrary.org/obo/PR_000001363), [PR:000001388](http://purl.obolibrary.org/obo/PR_000001388), [PR:000001389](http://purl.obolibrary.org/obo/PR_000001389), ...                                         |
| `PRO:PD`        |            258 | [PR:000027209](http://purl.obolibrary.org/obo/PR_000027209), [PR:000027210](http://purl.obolibrary.org/obo/PR_000027210), [PR:000027211](http://purl.obolibrary.org/obo/PR_000027211), [PR:000027212](http://purl.obolibrary.org/obo/PR_000027212), [PR:000027238](http://purl.obolibrary.org/obo/PR_000027238), ...                                         |
| `PRO:CNx`       |            196 | [PR:000026170](http://purl.obolibrary.org/obo/PR_000026170), [PR:000026171](http://purl.obolibrary.org/obo/PR_000026171), [PR:000026172](http://purl.obolibrary.org/obo/PR_000026172), [PR:000026173](http://purl.obolibrary.org/obo/PR_000026173), [PR:000026174](http://purl.obolibrary.org/obo/PR_000026174), ...                                         |
| `PRO:CG`        |             60 | [PR:000027429](http://purl.obolibrary.org/obo/PR_000027429), [PR:000027430](http://purl.obolibrary.org/obo/PR_000027430), [PR:000027431](http://purl.obolibrary.org/obo/PR_000027431), [PR:000027451](http://purl.obolibrary.org/obo/PR_000027451), [PR:000027452](http://purl.obolibrary.org/obo/PR_000027452), ...                                         |
| `PRO:PDE`       |             27 | [PR:000028429](http://purl.obolibrary.org/obo/PR_000028429), [PR:000028430](http://purl.obolibrary.org/obo/PR_000028430), [PR:000028431](http://purl.obolibrary.org/obo/PR_000028431), [PR:000028432](http://purl.obolibrary.org/obo/PR_000028432), [PR:000028433](http://purl.obolibrary.org/obo/PR_000028433), ...                                         |
| `PRO:CJB`       |             23 | [PR:000025354](http://purl.obolibrary.org/obo/PR_000025354), [PR:000025760](http://purl.obolibrary.org/obo/PR_000025760), [PR:000025761](http://purl.obolibrary.org/obo/PR_000025761), [PR:000025762](http://purl.obolibrary.org/obo/PR_000025762), [PR:000026295](http://purl.obolibrary.org/obo/PR_000026295), ...                                         |
| `PRO:CL`        |             14 | [PR:000003001](http://purl.obolibrary.org/obo/PR_000003001), [PR:000003006](http://purl.obolibrary.org/obo/PR_000003006), [PR:000003034](http://purl.obolibrary.org/obo/PR_000003034), [PR:000003039](http://purl.obolibrary.org/obo/PR_000003039), [PR:000003040](http://purl.obolibrary.org/obo/PR_000003040), ...                                         |
| `PRO:SY`        |             10 | [PR:000002193](http://purl.obolibrary.org/obo/PR_000002193), [PR:000002299](http://purl.obolibrary.org/obo/PR_000002299), [PR:000002300](http://purl.obolibrary.org/obo/PR_000002300), [PR:000002301](http://purl.obolibrary.org/obo/PR_000002301), [PR:000002302](http://purl.obolibrary.org/obo/PR_000002302), ...                                         |
| `PRO:AL`        |             10 | [PR:000003025](http://purl.obolibrary.org/obo/PR_000003025), [PR:000003026](http://purl.obolibrary.org/obo/PR_000003026), [PR:000003029](http://purl.obolibrary.org/obo/PR_000003029), [PR:000003042](http://purl.obolibrary.org/obo/PR_000003042), [PR:000003043](http://purl.obolibrary.org/obo/PR_000003043), ...                                         |
| `PRO:CC`        |              2 | [PR:000021967](http://purl.obolibrary.org/obo/PR_000021967), [PR:000021968](http://purl.obolibrary.org/obo/PR_000021968)                                                                                                                                                                                                                                     |
| `PRO:ADD`       |              2 | [PR:000050216](http://purl.obolibrary.org/obo/PR_000050216), [PR:P08575-8](http://purl.obolibrary.org/obo/PR_P08575-8)                                                                                                                                                                                                                                       |
| `PRO:JP`        |              1 | [PR:000025992](http://purl.obolibrary.org/obo/PR_000025992)                                                                                                                                                                                                                                                                                                  |

## `Prosite`: PROSITE

Overall, there were 3 invalid
xrefs to external prefixed with `Prosite` (standardized to Bioregistry
prefix [`prosite`](https://bioregistry.io/prosite)) that
did not match the standard pattern `^PS\d{5}$`.

| external_xref       |   usages_count | usages                                                  |
|---------------------|----------------|---------------------------------------------------------|
| `Prosite:PDOC0038`  |              1 | [GO:0043398](http://purl.obolibrary.org/obo/GO_0043398) |
| `Prosite:PDOC50021` |              1 | [GO:0051401](http://purl.obolibrary.org/obo/GO_0051401) |
| `Prosite:PDOC51022` |              1 | [GO:0097016](http://purl.obolibrary.org/obo/GO_0097016) |

## `Reactome`: Reactome

Overall, there were 736 invalid
xrefs to external prefixed with `Reactome` (standardized to Bioregistry
prefix [`reactome`](https://bioregistry.io/reactome)) that
did not match the standard pattern `^R-[A-Z]{3}-\d+(-\d+)?(\.\d+)?$`.

| external_xref            |   usages_count | usages                                                                                                                                                                                                                                                                                                          |
|--------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Reactome:REACT_6390`    |              5 | [PR:000027133](http://purl.obolibrary.org/obo/PR_000027133), [PR:000027133](http://purl.obolibrary.org/obo/PR_000027133), [PR:000027143](http://purl.obolibrary.org/obo/PR_000027143), [PR:000027143](http://purl.obolibrary.org/obo/PR_000027143), [PR:000027143](http://purl.obolibrary.org/obo/PR_000027143) |
| `Reactome:REACT_6540`    |              5 | [PR:000027134](http://purl.obolibrary.org/obo/PR_000027134), [PR:000027134](http://purl.obolibrary.org/obo/PR_000027134), [PR:000027144](http://purl.obolibrary.org/obo/PR_000027144), [PR:000027144](http://purl.obolibrary.org/obo/PR_000027144), [PR:000027144](http://purl.obolibrary.org/obo/PR_000027144) |
| `Reactome:REACT_6474`    |              5 | [PR:000027135](http://purl.obolibrary.org/obo/PR_000027135), [PR:000027135](http://purl.obolibrary.org/obo/PR_000027135), [PR:000027145](http://purl.obolibrary.org/obo/PR_000027145), [PR:000027145](http://purl.obolibrary.org/obo/PR_000027145), [PR:000027145](http://purl.obolibrary.org/obo/PR_000027145) |
| `Reactome:REACT_6566`    |              5 | [PR:000027136](http://purl.obolibrary.org/obo/PR_000027136), [PR:000027136](http://purl.obolibrary.org/obo/PR_000027136), [PR:000027146](http://purl.obolibrary.org/obo/PR_000027146), [PR:000027146](http://purl.obolibrary.org/obo/PR_000027146), [PR:000027146](http://purl.obolibrary.org/obo/PR_000027146) |
| `Reactome:REACT_6578`    |              5 | [PR:000027137](http://purl.obolibrary.org/obo/PR_000027137), [PR:000027137](http://purl.obolibrary.org/obo/PR_000027137), [PR:000027147](http://purl.obolibrary.org/obo/PR_000027147), [PR:000027147](http://purl.obolibrary.org/obo/PR_000027147), [PR:000027147](http://purl.obolibrary.org/obo/PR_000027147) |
| `Reactome:REACT_6646`    |              5 | [PR:000027137](http://purl.obolibrary.org/obo/PR_000027137), [PR:000027137](http://purl.obolibrary.org/obo/PR_000027137), [PR:000027147](http://purl.obolibrary.org/obo/PR_000027147), [PR:000027147](http://purl.obolibrary.org/obo/PR_000027147), [PR:000027147](http://purl.obolibrary.org/obo/PR_000027147) |
| `Reactome:REACT_4066`    |              5 | [PR:000027138](http://purl.obolibrary.org/obo/PR_000027138), [PR:000027138](http://purl.obolibrary.org/obo/PR_000027138), [PR:000027148](http://purl.obolibrary.org/obo/PR_000027148), [PR:000027148](http://purl.obolibrary.org/obo/PR_000027148), [PR:000027148](http://purl.obolibrary.org/obo/PR_000027148) |
| `Reactome:REACT_6445`    |              5 | [PR:000027139](http://purl.obolibrary.org/obo/PR_000027139), [PR:000027139](http://purl.obolibrary.org/obo/PR_000027139), [PR:000027149](http://purl.obolibrary.org/obo/PR_000027149), [PR:000027149](http://purl.obolibrary.org/obo/PR_000027149), [PR:000027149](http://purl.obolibrary.org/obo/PR_000027149) |
| `Reactome:REACT_4903`    |              5 | [PR:000027140](http://purl.obolibrary.org/obo/PR_000027140), [PR:000027140](http://purl.obolibrary.org/obo/PR_000027140), [PR:000027150](http://purl.obolibrary.org/obo/PR_000027150), [PR:000027150](http://purl.obolibrary.org/obo/PR_000027150), [PR:000027150](http://purl.obolibrary.org/obo/PR_000027150) |
| `Reactome:REACT_5446`    |              5 | [PR:000027140](http://purl.obolibrary.org/obo/PR_000027140), [PR:000027140](http://purl.obolibrary.org/obo/PR_000027140), [PR:000027150](http://purl.obolibrary.org/obo/PR_000027150), [PR:000027150](http://purl.obolibrary.org/obo/PR_000027150), [PR:000027150](http://purl.obolibrary.org/obo/PR_000027150) |
| `Reactome:REACT_2714`    |              5 | [PR:000027141](http://purl.obolibrary.org/obo/PR_000027141), [PR:000027141](http://purl.obolibrary.org/obo/PR_000027141), [PR:000027151](http://purl.obolibrary.org/obo/PR_000027151), [PR:000027151](http://purl.obolibrary.org/obo/PR_000027151), [PR:000027151](http://purl.obolibrary.org/obo/PR_000027151) |
| `Reactome:REACT_3967`    |              5 | [PR:000027142](http://purl.obolibrary.org/obo/PR_000027142), [PR:000027142](http://purl.obolibrary.org/obo/PR_000027142), [PR:000027152](http://purl.obolibrary.org/obo/PR_000027152), [PR:000027152](http://purl.obolibrary.org/obo/PR_000027152), [PR:000027152](http://purl.obolibrary.org/obo/PR_000027152) |
| `Reactome:REACT_7861`    |              5 | [PR:000027205](http://purl.obolibrary.org/obo/PR_000027205), [PR:000027207](http://purl.obolibrary.org/obo/PR_000027207), [PR:000027208](http://purl.obolibrary.org/obo/PR_000027208), [PR:000027208](http://purl.obolibrary.org/obo/PR_000027208), [PR:000027208](http://purl.obolibrary.org/obo/PR_000027208) |
| `Reactome:REACT_26882`   |              5 | [PR:000027254](http://purl.obolibrary.org/obo/PR_000027254), [PR:000027254](http://purl.obolibrary.org/obo/PR_000027254), [PR:000027399](http://purl.obolibrary.org/obo/PR_000027399), [PR:000027399](http://purl.obolibrary.org/obo/PR_000027399), [PR:000027399](http://purl.obolibrary.org/obo/PR_000027399) |
| `Reactome:REACT_26993`   |              5 | [PR:000027256](http://purl.obolibrary.org/obo/PR_000027256), [PR:000027256](http://purl.obolibrary.org/obo/PR_000027256), [PR:000027405](http://purl.obolibrary.org/obo/PR_000027405), [PR:000027405](http://purl.obolibrary.org/obo/PR_000027405), [PR:000027405](http://purl.obolibrary.org/obo/PR_000027405) |
| `Reactome:REACT_26054`   |              5 | [PR:000027258](http://purl.obolibrary.org/obo/PR_000027258), [PR:000027258](http://purl.obolibrary.org/obo/PR_000027258), [PR:000027409](http://purl.obolibrary.org/obo/PR_000027409), [PR:000027409](http://purl.obolibrary.org/obo/PR_000027409), [PR:000027409](http://purl.obolibrary.org/obo/PR_000027409) |
| `Reactome:REACT_4228`    |              5 | [PR:000027284](http://purl.obolibrary.org/obo/PR_000027284), [PR:000027284](http://purl.obolibrary.org/obo/PR_000027284), [PR:000027416](http://purl.obolibrary.org/obo/PR_000027416), [PR:000027416](http://purl.obolibrary.org/obo/PR_000027416), [PR:000027416](http://purl.obolibrary.org/obo/PR_000027416) |
| `Reactome:REACT_2915`    |              5 | [PR:000027286](http://purl.obolibrary.org/obo/PR_000027286), [PR:000027286](http://purl.obolibrary.org/obo/PR_000027286), [PR:000027421](http://purl.obolibrary.org/obo/PR_000027421), [PR:000027421](http://purl.obolibrary.org/obo/PR_000027421), [PR:000027421](http://purl.obolibrary.org/obo/PR_000027421) |
| `Reactome:REACT_5899`    |              5 | [PR:000027287](http://purl.obolibrary.org/obo/PR_000027287), [PR:000027287](http://purl.obolibrary.org/obo/PR_000027287), [PR:000027424](http://purl.obolibrary.org/obo/PR_000027424), [PR:000027424](http://purl.obolibrary.org/obo/PR_000027424), [PR:000027424](http://purl.obolibrary.org/obo/PR_000027424) |
| `Reactome:REACT_25948`   |              5 | [PR:000028679](http://purl.obolibrary.org/obo/PR_000028679), [PR:000028679](http://purl.obolibrary.org/obo/PR_000028679), [PR:000028680](http://purl.obolibrary.org/obo/PR_000028680), [PR:000028680](http://purl.obolibrary.org/obo/PR_000028680), [PR:000028680](http://purl.obolibrary.org/obo/PR_000028680) |
| `Reactome:REACT_6632`    |              4 | [PR:000026179](http://purl.obolibrary.org/obo/PR_000026179), [PR:000026180](http://purl.obolibrary.org/obo/PR_000026180), [PR:000026181](http://purl.obolibrary.org/obo/PR_000026181), [PR:000026181](http://purl.obolibrary.org/obo/PR_000026181)                                                              |
| `Reactome:REACT_13080`   |              4 | [PR:000026186](http://purl.obolibrary.org/obo/PR_000026186), [PR:000026188](http://purl.obolibrary.org/obo/PR_000026188), [PR:000026223](http://purl.obolibrary.org/obo/PR_000026223), [PR:000026223](http://purl.obolibrary.org/obo/PR_000026223)                                                              |
| `Reactome:REACT_22838`   |              4 | [PR:000026190](http://purl.obolibrary.org/obo/PR_000026190), [PR:000026192](http://purl.obolibrary.org/obo/PR_000026192), [PR:000026222](http://purl.obolibrary.org/obo/PR_000026222), [PR:000026222](http://purl.obolibrary.org/obo/PR_000026222)                                                              |
| `Reactome:REACT_15579`   |              4 | [PR:000026197](http://purl.obolibrary.org/obo/PR_000026197), [PR:000026199](http://purl.obolibrary.org/obo/PR_000026199), [PR:000026219](http://purl.obolibrary.org/obo/PR_000026219), [PR:000026219](http://purl.obolibrary.org/obo/PR_000026219)                                                              |
| `Reactome:REACT_6685`    |              4 | [PR:000027121](http://purl.obolibrary.org/obo/PR_000027121), [PR:000027123](http://purl.obolibrary.org/obo/PR_000027123), [PR:000027123](http://purl.obolibrary.org/obo/PR_000027123), [PR:000027123](http://purl.obolibrary.org/obo/PR_000027123)                                                              |
| `Reactome:REACT_6547`    |              4 | [PR:000027122](http://purl.obolibrary.org/obo/PR_000027122), [PR:000027124](http://purl.obolibrary.org/obo/PR_000027124), [PR:000027124](http://purl.obolibrary.org/obo/PR_000027124), [PR:000027124](http://purl.obolibrary.org/obo/PR_000027124)                                                              |
| `Reactome:REACT_26477`   |              4 | [PR:000027255](http://purl.obolibrary.org/obo/PR_000027255), [PR:000027397](http://purl.obolibrary.org/obo/PR_000027397), [PR:000027397](http://purl.obolibrary.org/obo/PR_000027397), [PR:000027397](http://purl.obolibrary.org/obo/PR_000027397)                                                              |
| `Reactome:REACT_22820`   |              4 | [PR:000027261](http://purl.obolibrary.org/obo/PR_000027261), [PR:000027403](http://purl.obolibrary.org/obo/PR_000027403), [PR:000027403](http://purl.obolibrary.org/obo/PR_000027403), [PR:000027403](http://purl.obolibrary.org/obo/PR_000027403)                                                              |
| `Reactome:REACT_26862`   |              4 | [PR:000027263](http://purl.obolibrary.org/obo/PR_000027263), [PR:000027425](http://purl.obolibrary.org/obo/PR_000027425), [PR:000027425](http://purl.obolibrary.org/obo/PR_000027425), [PR:000027425](http://purl.obolibrary.org/obo/PR_000027425)                                                              |
| `Reactome:REACT_26798`   |              4 | [PR:000027264](http://purl.obolibrary.org/obo/PR_000027264), [PR:000027428](http://purl.obolibrary.org/obo/PR_000027428), [PR:000027428](http://purl.obolibrary.org/obo/PR_000027428), [PR:000027428](http://purl.obolibrary.org/obo/PR_000027428)                                                              |
| `Reactome:REACT_8578`    |              4 | [PR:000027280](http://purl.obolibrary.org/obo/PR_000027280), [PR:000027400](http://purl.obolibrary.org/obo/PR_000027400), [PR:000027400](http://purl.obolibrary.org/obo/PR_000027400), [PR:000027400](http://purl.obolibrary.org/obo/PR_000027400)                                                              |
| `Reactome:REACT_5445`    |              4 | [PR:000027281](http://purl.obolibrary.org/obo/PR_000027281), [PR:000027413](http://purl.obolibrary.org/obo/PR_000027413), [PR:000027413](http://purl.obolibrary.org/obo/PR_000027413), [PR:000027413](http://purl.obolibrary.org/obo/PR_000027413)                                                              |
| `Reactome:REACT_8836`    |              4 | [PR:000027282](http://purl.obolibrary.org/obo/PR_000027282), [PR:000027414](http://purl.obolibrary.org/obo/PR_000027414), [PR:000027414](http://purl.obolibrary.org/obo/PR_000027414), [PR:000027414](http://purl.obolibrary.org/obo/PR_000027414)                                                              |
| `Reactome:REACT_5456`    |              4 | [PR:000027283](http://purl.obolibrary.org/obo/PR_000027283), [PR:000027415](http://purl.obolibrary.org/obo/PR_000027415), [PR:000027415](http://purl.obolibrary.org/obo/PR_000027415), [PR:000027415](http://purl.obolibrary.org/obo/PR_000027415)                                                              |
| `Reactome:REACT_5684`    |              4 | [PR:000027285](http://purl.obolibrary.org/obo/PR_000027285), [PR:000027419](http://purl.obolibrary.org/obo/PR_000027419), [PR:000027419](http://purl.obolibrary.org/obo/PR_000027419), [PR:000027419](http://purl.obolibrary.org/obo/PR_000027419)                                                              |
| `Reactome:REACT_8936`    |              4 | [PR:000027288](http://purl.obolibrary.org/obo/PR_000027288), [PR:000027396](http://purl.obolibrary.org/obo/PR_000027396), [PR:000027396](http://purl.obolibrary.org/obo/PR_000027396), [PR:000027396](http://purl.obolibrary.org/obo/PR_000027396)                                                              |
| `Reactome:REACT_4025`    |              4 | [PR:000027291](http://purl.obolibrary.org/obo/PR_000027291), [PR:000027291](http://purl.obolibrary.org/obo/PR_000027291), [PR:000027411](http://purl.obolibrary.org/obo/PR_000027411), [PR:000027411](http://purl.obolibrary.org/obo/PR_000027411)                                                              |
| `Reactome:REACT_5518`    |              4 | [PR:000027292](http://purl.obolibrary.org/obo/PR_000027292), [PR:000027292](http://purl.obolibrary.org/obo/PR_000027292), [PR:000027412](http://purl.obolibrary.org/obo/PR_000027412), [PR:000027412](http://purl.obolibrary.org/obo/PR_000027412)                                                              |
| `Reactome:REACT_7083`    |              4 | [PR:000027204](http://purl.obolibrary.org/obo/PR_000027204), [PR:000028678](http://purl.obolibrary.org/obo/PR_000028678), [PR:000028678](http://purl.obolibrary.org/obo/PR_000028678), [PR:000028678](http://purl.obolibrary.org/obo/PR_000028678)                                                              |
| `Reactome:REACT_25852`   |              4 | [PR:000028688](http://purl.obolibrary.org/obo/PR_000028688), [PR:000028690](http://purl.obolibrary.org/obo/PR_000028690), [PR:000028691](http://purl.obolibrary.org/obo/PR_000028691), [PR:000028691](http://purl.obolibrary.org/obo/PR_000028691)                                                              |
| `Reactome:REACT_26959`   |              4 | [PR:000028697](http://purl.obolibrary.org/obo/PR_000028697), [PR:000028698](http://purl.obolibrary.org/obo/PR_000028698), [PR:000028698](http://purl.obolibrary.org/obo/PR_000028698), [PR:000028698](http://purl.obolibrary.org/obo/PR_000028698)                                                              |
| `Reactome:REACT_27000`   |              4 | [PR:000028699](http://purl.obolibrary.org/obo/PR_000028699), [PR:000028700](http://purl.obolibrary.org/obo/PR_000028700), [PR:000028700](http://purl.obolibrary.org/obo/PR_000028700), [PR:000028700](http://purl.obolibrary.org/obo/PR_000028700)                                                              |
| `Reactome:REACT_7415`    |              3 | [GO:0070019](http://purl.obolibrary.org/obo/GO_0070019), [GO:0070022](http://purl.obolibrary.org/obo/GO_0070022), [PR:000025976](http://purl.obolibrary.org/obo/PR_000025976)                                                                                                                                   |
| `Reactome:REACT_13021`   |              3 | [PR:000025777](http://purl.obolibrary.org/obo/PR_000025777), [PR:000025777](http://purl.obolibrary.org/obo/PR_000025777), [PR:000025780](http://purl.obolibrary.org/obo/PR_000025780)                                                                                                                           |
| `Reactome:REACT_5060`    |              3 | [PR:000026171](http://purl.obolibrary.org/obo/PR_000026171), [PR:000026172](http://purl.obolibrary.org/obo/PR_000026172), [PR:000026173](http://purl.obolibrary.org/obo/PR_000026173)                                                                                                                           |
| `Reactome:REACT_3158`    |              3 | [PR:000026174](http://purl.obolibrary.org/obo/PR_000026174), [PR:000026210](http://purl.obolibrary.org/obo/PR_000026210), [PR:000026210](http://purl.obolibrary.org/obo/PR_000026210)                                                                                                                           |
| `Reactome:REACT_3122`    |              3 | [PR:000026177](http://purl.obolibrary.org/obo/PR_000026177), [PR:000026178](http://purl.obolibrary.org/obo/PR_000026178), [PR:000026178](http://purl.obolibrary.org/obo/PR_000026178)                                                                                                                           |
| `Reactome:REACT_21980`   |              3 | [PR:000026185](http://purl.obolibrary.org/obo/PR_000026185), [PR:000026215](http://purl.obolibrary.org/obo/PR_000026215), [PR:000026215](http://purl.obolibrary.org/obo/PR_000026215)                                                                                                                           |
| `Reactome:REACT_24199`   |              3 | [PR:000026193](http://purl.obolibrary.org/obo/PR_000026193), [PR:000026221](http://purl.obolibrary.org/obo/PR_000026221), [PR:000026221](http://purl.obolibrary.org/obo/PR_000026221)                                                                                                                           |
| `Reactome:REACT_5701`    |              3 | [PR:000026196](http://purl.obolibrary.org/obo/PR_000026196), [PR:000026220](http://purl.obolibrary.org/obo/PR_000026220), [PR:000026220](http://purl.obolibrary.org/obo/PR_000026220)                                                                                                                           |
| `Reactome:REACT_18202`   |              3 | [PR:000026200](http://purl.obolibrary.org/obo/PR_000026200), [PR:000026218](http://purl.obolibrary.org/obo/PR_000026218), [PR:000026218](http://purl.obolibrary.org/obo/PR_000026218)                                                                                                                           |
| `Reactome:REACT_4567`    |              3 | [PR:000026203](http://purl.obolibrary.org/obo/PR_000026203), [PR:000026217](http://purl.obolibrary.org/obo/PR_000026217), [PR:000026217](http://purl.obolibrary.org/obo/PR_000026217)                                                                                                                           |
| `Reactome:REACT_7632`    |              3 | [PR:000026206](http://purl.obolibrary.org/obo/PR_000026206), [PR:000026216](http://purl.obolibrary.org/obo/PR_000026216), [PR:000026216](http://purl.obolibrary.org/obo/PR_000026216)                                                                                                                           |
| `Reactome:REACT_12327`   |              3 | [PR:000026209](http://purl.obolibrary.org/obo/PR_000026209), [PR:000026214](http://purl.obolibrary.org/obo/PR_000026214), [PR:000026214](http://purl.obolibrary.org/obo/PR_000026214)                                                                                                                           |
| `Reactome:REACT_17255`   |              3 | [PR:000026430](http://purl.obolibrary.org/obo/PR_000026430), [PR:000026430](http://purl.obolibrary.org/obo/PR_000026430), [PR:000026430](http://purl.obolibrary.org/obo/PR_000026430)                                                                                                                           |
| `Reactome:REACT_5844`    |              3 | [PR:000026431](http://purl.obolibrary.org/obo/PR_000026431), [PR:000026431](http://purl.obolibrary.org/obo/PR_000026431), [PR:000026431](http://purl.obolibrary.org/obo/PR_000026431)                                                                                                                           |
| `Reactome:REACT_3727`    |              3 | [PR:000026432](http://purl.obolibrary.org/obo/PR_000026432), [PR:000026432](http://purl.obolibrary.org/obo/PR_000026432), [PR:000026432](http://purl.obolibrary.org/obo/PR_000026432)                                                                                                                           |
| `Reactome:REACT_4881`    |              3 | [PR:000026434](http://purl.obolibrary.org/obo/PR_000026434), [PR:000026434](http://purl.obolibrary.org/obo/PR_000026434), [PR:000026434](http://purl.obolibrary.org/obo/PR_000026434)                                                                                                                           |
| `Reactome:REACT_3503`    |              3 | [PR:000026435](http://purl.obolibrary.org/obo/PR_000026435), [PR:000026435](http://purl.obolibrary.org/obo/PR_000026435), [PR:000026435](http://purl.obolibrary.org/obo/PR_000026435)                                                                                                                           |
| `Reactome:REACT_4763`    |              3 | [PR:000026436](http://purl.obolibrary.org/obo/PR_000026436), [PR:000026436](http://purl.obolibrary.org/obo/PR_000026436), [PR:000026436](http://purl.obolibrary.org/obo/PR_000026436)                                                                                                                           |
| `Reactome:REACT_11329`   |              3 | [PR:000026437](http://purl.obolibrary.org/obo/PR_000026437), [PR:000026437](http://purl.obolibrary.org/obo/PR_000026437), [PR:000026437](http://purl.obolibrary.org/obo/PR_000026437)                                                                                                                           |
| `Reactome:REACT_15768`   |              3 | [PR:000026438](http://purl.obolibrary.org/obo/PR_000026438), [PR:000026438](http://purl.obolibrary.org/obo/PR_000026438), [PR:000026438](http://purl.obolibrary.org/obo/PR_000026438)                                                                                                                           |
| `Reactome:REACT_9166`    |              3 | [PR:000026439](http://purl.obolibrary.org/obo/PR_000026439), [PR:000026439](http://purl.obolibrary.org/obo/PR_000026439), [PR:000026439](http://purl.obolibrary.org/obo/PR_000026439)                                                                                                                           |
| `Reactome:REACT_2542`    |              3 | [PR:000026440](http://purl.obolibrary.org/obo/PR_000026440), [PR:000026440](http://purl.obolibrary.org/obo/PR_000026440), [PR:000026440](http://purl.obolibrary.org/obo/PR_000026440)                                                                                                                           |
| `Reactome:REACT_5886`    |              3 | [PR:000026441](http://purl.obolibrary.org/obo/PR_000026441), [PR:000026441](http://purl.obolibrary.org/obo/PR_000026441), [PR:000026441](http://purl.obolibrary.org/obo/PR_000026441)                                                                                                                           |
| `Reactome:REACT_3725`    |              3 | [PR:000026442](http://purl.obolibrary.org/obo/PR_000026442), [PR:000026442](http://purl.obolibrary.org/obo/PR_000026442), [PR:000026442](http://purl.obolibrary.org/obo/PR_000026442)                                                                                                                           |
| `Reactome:REACT_4708`    |              3 | [PR:000026443](http://purl.obolibrary.org/obo/PR_000026443), [PR:000026443](http://purl.obolibrary.org/obo/PR_000026443), [PR:000026443](http://purl.obolibrary.org/obo/PR_000026443)                                                                                                                           |
| `Reactome:REACT_3506`    |              3 | [PR:000026450](http://purl.obolibrary.org/obo/PR_000026450), [PR:000026450](http://purl.obolibrary.org/obo/PR_000026450), [PR:000026450](http://purl.obolibrary.org/obo/PR_000026450)                                                                                                                           |
| `Reactome:REACT_7693`    |              3 | [PR:000026457](http://purl.obolibrary.org/obo/PR_000026457), [PR:000026457](http://purl.obolibrary.org/obo/PR_000026457), [PR:000026457](http://purl.obolibrary.org/obo/PR_000026457)                                                                                                                           |
| `Reactome:REACT_3427`    |              3 | [PR:000026458](http://purl.obolibrary.org/obo/PR_000026458), [PR:000026458](http://purl.obolibrary.org/obo/PR_000026458), [PR:000026458](http://purl.obolibrary.org/obo/PR_000026458)                                                                                                                           |
| `Reactome:REACT_18602`   |              3 | [PR:000026644](http://purl.obolibrary.org/obo/PR_000026644), [PR:000026644](http://purl.obolibrary.org/obo/PR_000026644), [PR:000026644](http://purl.obolibrary.org/obo/PR_000026644)                                                                                                                           |
| `Reactome:REACT_2587`    |              3 | [PR:000026767](http://purl.obolibrary.org/obo/PR_000026767), [PR:000026767](http://purl.obolibrary.org/obo/PR_000026767), [PR:000026767](http://purl.obolibrary.org/obo/PR_000026767)                                                                                                                           |
| `Reactome:REACT_22981`   |              3 | [PR:000026771](http://purl.obolibrary.org/obo/PR_000026771), [PR:000026771](http://purl.obolibrary.org/obo/PR_000026771), [PR:000026771](http://purl.obolibrary.org/obo/PR_000026771)                                                                                                                           |
| `Reactome:REACT_19863`   |              3 | [PR:000026773](http://purl.obolibrary.org/obo/PR_000026773), [PR:000026773](http://purl.obolibrary.org/obo/PR_000026773), [PR:000026773](http://purl.obolibrary.org/obo/PR_000026773)                                                                                                                           |
| `Reactome:REACT_3400`    |              3 | [PR:000026777](http://purl.obolibrary.org/obo/PR_000026777), [PR:000026777](http://purl.obolibrary.org/obo/PR_000026777), [PR:000026777](http://purl.obolibrary.org/obo/PR_000026777)                                                                                                                           |
| `Reactome:REACT_11382`   |              3 | [PR:000026797](http://purl.obolibrary.org/obo/PR_000026797), [PR:000026802](http://purl.obolibrary.org/obo/PR_000026802), [PR:000026802](http://purl.obolibrary.org/obo/PR_000026802)                                                                                                                           |
| `Reactome:REACT_4039`    |              3 | [PR:000026806](http://purl.obolibrary.org/obo/PR_000026806), [PR:000026806](http://purl.obolibrary.org/obo/PR_000026806), [PR:000026806](http://purl.obolibrary.org/obo/PR_000026806)                                                                                                                           |
| `Reactome:REACT_4194`    |              3 | [PR:000026826](http://purl.obolibrary.org/obo/PR_000026826), [PR:000026827](http://purl.obolibrary.org/obo/PR_000026827), [PR:000026827](http://purl.obolibrary.org/obo/PR_000026827)                                                                                                                           |
| `Reactome:REACT_11747`   |              3 | [PR:000026859](http://purl.obolibrary.org/obo/PR_000026859), [PR:000026860](http://purl.obolibrary.org/obo/PR_000026860), [PR:000026860](http://purl.obolibrary.org/obo/PR_000026860)                                                                                                                           |
| `Reactome:REACT_17977`   |              3 | [PR:000026865](http://purl.obolibrary.org/obo/PR_000026865), [PR:000026866](http://purl.obolibrary.org/obo/PR_000026866), [PR:000026866](http://purl.obolibrary.org/obo/PR_000026866)                                                                                                                           |
| `Reactome:REACT_22575`   |              3 | [PR:000026867](http://purl.obolibrary.org/obo/PR_000026867), [PR:000026868](http://purl.obolibrary.org/obo/PR_000026868), [PR:000026868](http://purl.obolibrary.org/obo/PR_000026868)                                                                                                                           |
| `Reactome:REACT_22901`   |              3 | [PR:000003145](http://purl.obolibrary.org/obo/PR_000003145), [PR:000027047](http://purl.obolibrary.org/obo/PR_000027047), [PR:000027047](http://purl.obolibrary.org/obo/PR_000027047)                                                                                                                           |
| `Reactome:REACT_7864`    |              3 | [PR:000027186](http://purl.obolibrary.org/obo/PR_000027186), [PR:000027186](http://purl.obolibrary.org/obo/PR_000027186), [PR:000027186](http://purl.obolibrary.org/obo/PR_000027186)                                                                                                                           |
| `Reactome:REACT_26936`   |              3 | [PR:000027257](http://purl.obolibrary.org/obo/PR_000027257), [PR:000027408](http://purl.obolibrary.org/obo/PR_000027408), [PR:000027408](http://purl.obolibrary.org/obo/PR_000027408)                                                                                                                           |
| `Reactome:REACT_27040`   |              3 | [PR:000027259](http://purl.obolibrary.org/obo/PR_000027259), [PR:000027417](http://purl.obolibrary.org/obo/PR_000027417), [PR:000027417](http://purl.obolibrary.org/obo/PR_000027417)                                                                                                                           |
| `Reactome:REACT_26887`   |              3 | [PR:000027260](http://purl.obolibrary.org/obo/PR_000027260), [PR:000027418](http://purl.obolibrary.org/obo/PR_000027418), [PR:000027418](http://purl.obolibrary.org/obo/PR_000027418)                                                                                                                           |
| `Reactome:REACT_25964`   |              3 | [PR:000027262](http://purl.obolibrary.org/obo/PR_000027262), [PR:000027423](http://purl.obolibrary.org/obo/PR_000027423), [PR:000027423](http://purl.obolibrary.org/obo/PR_000027423)                                                                                                                           |
| `Reactome:REACT_2546`    |              3 | [PR:000027289](http://purl.obolibrary.org/obo/PR_000027289), [PR:000027402](http://purl.obolibrary.org/obo/PR_000027402), [PR:000027402](http://purl.obolibrary.org/obo/PR_000027402)                                                                                                                           |
| `Reactome:REACT_3100`    |              3 | [PR:000027290](http://purl.obolibrary.org/obo/PR_000027290), [PR:000027404](http://purl.obolibrary.org/obo/PR_000027404), [PR:000027404](http://purl.obolibrary.org/obo/PR_000027404)                                                                                                                           |
| `Reactome:REACT_12291`   |              3 | [PR:000027308](http://purl.obolibrary.org/obo/PR_000027308), [PR:000027308](http://purl.obolibrary.org/obo/PR_000027308), [PR:000027308](http://purl.obolibrary.org/obo/PR_000027308)                                                                                                                           |
| `Reactome:REACT_5717`    |              3 | [PR:000027394](http://purl.obolibrary.org/obo/PR_000027394), [PR:000027394](http://purl.obolibrary.org/obo/PR_000027394), [PR:000027394](http://purl.obolibrary.org/obo/PR_000027394)                                                                                                                           |
| `Reactome:REACT_20843`   |              3 | [PR:000027395](http://purl.obolibrary.org/obo/PR_000027395), [PR:000027395](http://purl.obolibrary.org/obo/PR_000027395), [PR:000027395](http://purl.obolibrary.org/obo/PR_000027395)                                                                                                                           |
| `Reactome:REACT_3881`    |              3 | [PR:000027398](http://purl.obolibrary.org/obo/PR_000027398), [PR:000027398](http://purl.obolibrary.org/obo/PR_000027398), [PR:000027398](http://purl.obolibrary.org/obo/PR_000027398)                                                                                                                           |
| `Reactome:REACT_5142`    |              3 | [PR:000027401](http://purl.obolibrary.org/obo/PR_000027401), [PR:000027401](http://purl.obolibrary.org/obo/PR_000027401), [PR:000027401](http://purl.obolibrary.org/obo/PR_000027401)                                                                                                                           |
| `Reactome:REACT_7452`    |              3 | [PR:000027406](http://purl.obolibrary.org/obo/PR_000027406), [PR:000027406](http://purl.obolibrary.org/obo/PR_000027406), [PR:000027406](http://purl.obolibrary.org/obo/PR_000027406)                                                                                                                           |
| `Reactome:REACT_7467`    |              3 | [PR:000027410](http://purl.obolibrary.org/obo/PR_000027410), [PR:000027410](http://purl.obolibrary.org/obo/PR_000027410), [PR:000027410](http://purl.obolibrary.org/obo/PR_000027410)                                                                                                                           |
| `Reactome:REACT_15945`   |              3 | [PR:000027420](http://purl.obolibrary.org/obo/PR_000027420), [PR:000027420](http://purl.obolibrary.org/obo/PR_000027420), [PR:000027420](http://purl.obolibrary.org/obo/PR_000027420)                                                                                                                           |
| `Reactome:REACT_24451`   |              3 | [PR:000027422](http://purl.obolibrary.org/obo/PR_000027422), [PR:000027422](http://purl.obolibrary.org/obo/PR_000027422), [PR:000027422](http://purl.obolibrary.org/obo/PR_000027422)                                                                                                                           |
| `Reactome:REACT_4592`    |              3 | [PR:000027426](http://purl.obolibrary.org/obo/PR_000027426), [PR:000027426](http://purl.obolibrary.org/obo/PR_000027426), [PR:000027426](http://purl.obolibrary.org/obo/PR_000027426)                                                                                                                           |
| `Reactome:REACT_2460`    |              3 | [PR:000027427](http://purl.obolibrary.org/obo/PR_000027427), [PR:000027427](http://purl.obolibrary.org/obo/PR_000027427), [PR:000027427](http://purl.obolibrary.org/obo/PR_000027427)                                                                                                                           |
| `Reactome:REACT_3969`    |              3 | [PR:000028430](http://purl.obolibrary.org/obo/PR_000028430), [PR:000028430](http://purl.obolibrary.org/obo/PR_000028430), [PR:000028430](http://purl.obolibrary.org/obo/PR_000028430)                                                                                                                           |
| `Reactome:REACT_21591`   |              3 | [PR:000028684](http://purl.obolibrary.org/obo/PR_000028684), [PR:000028687](http://purl.obolibrary.org/obo/PR_000028687), [PR:000028687](http://purl.obolibrary.org/obo/PR_000028687)                                                                                                                           |
| `Reactome:REACT_25772`   |              3 | [PR:000028692](http://purl.obolibrary.org/obo/PR_000028692), [PR:000028694](http://purl.obolibrary.org/obo/PR_000028694), [PR:000028695](http://purl.obolibrary.org/obo/PR_000028695)                                                                                                                           |
| `Reactome:REACT_7737`    |              2 | [GO:0070018](http://purl.obolibrary.org/obo/GO_0070018), [GO:0070022](http://purl.obolibrary.org/obo/GO_0070022)                                                                                                                                                                                                |
| `Reactome:REACT_7146`    |              2 | [PR:000025765](http://purl.obolibrary.org/obo/PR_000025765), [PR:000025765](http://purl.obolibrary.org/obo/PR_000025765)                                                                                                                                                                                        |
| `Reactome:REACT_7444`    |              2 | [PR:000025765](http://purl.obolibrary.org/obo/PR_000025765), [PR:000025765](http://purl.obolibrary.org/obo/PR_000025765)                                                                                                                                                                                        |
| `Reactome:REACT_6996`    |              2 | [PR:000025926](http://purl.obolibrary.org/obo/PR_000025926), [PR:000025926](http://purl.obolibrary.org/obo/PR_000025926)                                                                                                                                                                                        |
| `Reactome:REACT_7344`    |              2 | [PR:000025933](http://purl.obolibrary.org/obo/PR_000025933), [PR:000025940](http://purl.obolibrary.org/obo/PR_000025940)                                                                                                                                                                                        |
| `Reactome:REACT_7382`    |              2 | [PR:000025933](http://purl.obolibrary.org/obo/PR_000025933), [PR:000025940](http://purl.obolibrary.org/obo/PR_000025940)                                                                                                                                                                                        |
| `Reactome:REACT_3037`    |              2 | [PR:000026189](http://purl.obolibrary.org/obo/PR_000026189), [PR:000026189](http://purl.obolibrary.org/obo/PR_000026189)                                                                                                                                                                                        |
| `Reactome:REACT_7845`    |              2 | [PR:000026333](http://purl.obolibrary.org/obo/PR_000026333), [PR:000026333](http://purl.obolibrary.org/obo/PR_000026333)                                                                                                                                                                                        |
| `Reactome:REACT_12156`   |              2 | [PR:000026334](http://purl.obolibrary.org/obo/PR_000026334), [PR:000026334](http://purl.obolibrary.org/obo/PR_000026334)                                                                                                                                                                                        |
| `Reactome:REACT_12354`   |              2 | [PR:000026334](http://purl.obolibrary.org/obo/PR_000026334), [PR:000026334](http://purl.obolibrary.org/obo/PR_000026334)                                                                                                                                                                                        |
| `Reactome:REACT_6888`    |              2 | [PR:000026335](http://purl.obolibrary.org/obo/PR_000026335), [PR:000026335](http://purl.obolibrary.org/obo/PR_000026335)                                                                                                                                                                                        |
| `Reactome:REACT_12256`   |              2 | [PR:000026336](http://purl.obolibrary.org/obo/PR_000026336), [PR:000026336](http://purl.obolibrary.org/obo/PR_000026336)                                                                                                                                                                                        |
| `Reactome:REACT_3471`    |              2 | [PR:000026337](http://purl.obolibrary.org/obo/PR_000026337), [PR:000026337](http://purl.obolibrary.org/obo/PR_000026337)                                                                                                                                                                                        |
| `Reactome:REACT_3378`    |              2 | [PR:000026338](http://purl.obolibrary.org/obo/PR_000026338), [PR:000026338](http://purl.obolibrary.org/obo/PR_000026338)                                                                                                                                                                                        |
| `Reactome:REACT_13243`   |              2 | [PR:000026339](http://purl.obolibrary.org/obo/PR_000026339), [PR:000026339](http://purl.obolibrary.org/obo/PR_000026339)                                                                                                                                                                                        |
| `Reactome:REACT_13127`   |              2 | [PR:000026340](http://purl.obolibrary.org/obo/PR_000026340), [PR:000026340](http://purl.obolibrary.org/obo/PR_000026340)                                                                                                                                                                                        |
| `Reactome:REACT_2640`    |              2 | [PR:000026341](http://purl.obolibrary.org/obo/PR_000026341), [PR:000026341](http://purl.obolibrary.org/obo/PR_000026341)                                                                                                                                                                                        |
| `Reactome:REACT_18223`   |              2 | [PR:000026342](http://purl.obolibrary.org/obo/PR_000026342), [PR:000026342](http://purl.obolibrary.org/obo/PR_000026342)                                                                                                                                                                                        |
| `Reactome:REACT_18147`   |              2 | [PR:000026343](http://purl.obolibrary.org/obo/PR_000026343), [PR:000026343](http://purl.obolibrary.org/obo/PR_000026343)                                                                                                                                                                                        |
| `Reactome:REACT_17506`   |              2 | [PR:000026344](http://purl.obolibrary.org/obo/PR_000026344), [PR:000026344](http://purl.obolibrary.org/obo/PR_000026344)                                                                                                                                                                                        |
| `Reactome:REACT_18183`   |              2 | [PR:000026345](http://purl.obolibrary.org/obo/PR_000026345), [PR:000026345](http://purl.obolibrary.org/obo/PR_000026345)                                                                                                                                                                                        |
| `Reactome:REACT_17379`   |              2 | [PR:000026346](http://purl.obolibrary.org/obo/PR_000026346), [PR:000026346](http://purl.obolibrary.org/obo/PR_000026346)                                                                                                                                                                                        |
| `Reactome:REACT_17762`   |              2 | [PR:000026347](http://purl.obolibrary.org/obo/PR_000026347), [PR:000026347](http://purl.obolibrary.org/obo/PR_000026347)                                                                                                                                                                                        |
| `Reactome:REACT_7825`    |              2 | [PR:000026433](http://purl.obolibrary.org/obo/PR_000026433), [PR:000026433](http://purl.obolibrary.org/obo/PR_000026433)                                                                                                                                                                                        |
| `Reactome:REACT_7542`    |              2 | [PR:000026444](http://purl.obolibrary.org/obo/PR_000026444), [PR:000026444](http://purl.obolibrary.org/obo/PR_000026444)                                                                                                                                                                                        |
| `Reactome:REACT_24613`   |              2 | [PR:000026555](http://purl.obolibrary.org/obo/PR_000026555), [PR:000026555](http://purl.obolibrary.org/obo/PR_000026555)                                                                                                                                                                                        |
| `Reactome:REACT_18668`   |              2 | [PR:000026725](http://purl.obolibrary.org/obo/PR_000026725), [PR:000026725](http://purl.obolibrary.org/obo/PR_000026725)                                                                                                                                                                                        |
| `Reactome:REACT_18700`   |              2 | [PR:000026730](http://purl.obolibrary.org/obo/PR_000026730), [PR:000026730](http://purl.obolibrary.org/obo/PR_000026730)                                                                                                                                                                                        |
| `Reactome:REACT_9765`    |              2 | [PR:000026735](http://purl.obolibrary.org/obo/PR_000026735), [PR:000026735](http://purl.obolibrary.org/obo/PR_000026735)                                                                                                                                                                                        |
| `Reactome:REACT_21620`   |              2 | [PR:000026737](http://purl.obolibrary.org/obo/PR_000026737), [PR:000026737](http://purl.obolibrary.org/obo/PR_000026737)                                                                                                                                                                                        |
| `Reactome:REACT_9762`    |              2 | [PR:000026739](http://purl.obolibrary.org/obo/PR_000026739), [PR:000026739](http://purl.obolibrary.org/obo/PR_000026739)                                                                                                                                                                                        |
| `Reactome:REACT_2478`    |              2 | [PR:000026741](http://purl.obolibrary.org/obo/PR_000026741), [PR:000026741](http://purl.obolibrary.org/obo/PR_000026741)                                                                                                                                                                                        |
| `Reactome:REACT_26711`   |              2 | [PR:000026743](http://purl.obolibrary.org/obo/PR_000026743), [PR:000026743](http://purl.obolibrary.org/obo/PR_000026743)                                                                                                                                                                                        |
| `Reactome:REACT_3430`    |              2 | [PR:000026744](http://purl.obolibrary.org/obo/PR_000026744), [PR:000026744](http://purl.obolibrary.org/obo/PR_000026744)                                                                                                                                                                                        |
| `Reactome:REACT_5302`    |              2 | [PR:000026752](http://purl.obolibrary.org/obo/PR_000026752), [PR:000026752](http://purl.obolibrary.org/obo/PR_000026752)                                                                                                                                                                                        |
| `Reactome:REACT_4601`    |              2 | [PR:000026768](http://purl.obolibrary.org/obo/PR_000026768), [PR:000026768](http://purl.obolibrary.org/obo/PR_000026768)                                                                                                                                                                                        |
| `Reactome:REACT_5296`    |              2 | [PR:000026769](http://purl.obolibrary.org/obo/PR_000026769), [PR:000026769](http://purl.obolibrary.org/obo/PR_000026769)                                                                                                                                                                                        |
| `Reactome:REACT_2382`    |              2 | [PR:000026770](http://purl.obolibrary.org/obo/PR_000026770), [PR:000026770](http://purl.obolibrary.org/obo/PR_000026770)                                                                                                                                                                                        |
| `Reactome:REACT_9339`    |              2 | [PR:000026772](http://purl.obolibrary.org/obo/PR_000026772), [PR:000026772](http://purl.obolibrary.org/obo/PR_000026772)                                                                                                                                                                                        |
| `Reactome:REACT_5444`    |              2 | [PR:000026788](http://purl.obolibrary.org/obo/PR_000026788), [PR:000026788](http://purl.obolibrary.org/obo/PR_000026788)                                                                                                                                                                                        |
| `Reactome:REACT_3331`    |              2 | [PR:000026790](http://purl.obolibrary.org/obo/PR_000026790), [PR:000026790](http://purl.obolibrary.org/obo/PR_000026790)                                                                                                                                                                                        |
| `Reactome:REACT_13182`   |              2 | [PR:000026791](http://purl.obolibrary.org/obo/PR_000026791), [PR:000026791](http://purl.obolibrary.org/obo/PR_000026791)                                                                                                                                                                                        |
| `Reactome:REACT_7904`    |              2 | [PR:000026793](http://purl.obolibrary.org/obo/PR_000026793), [PR:000026793](http://purl.obolibrary.org/obo/PR_000026793)                                                                                                                                                                                        |
| `Reactome:REACT_11250`   |              2 | [PR:000026795](http://purl.obolibrary.org/obo/PR_000026795), [PR:000026795](http://purl.obolibrary.org/obo/PR_000026795)                                                                                                                                                                                        |
| `Reactome:REACT_11620`   |              2 | [PR:000026804](http://purl.obolibrary.org/obo/PR_000026804), [PR:000026804](http://purl.obolibrary.org/obo/PR_000026804)                                                                                                                                                                                        |
| `Reactome:REACT_10509`   |              2 | [PR:000026817](http://purl.obolibrary.org/obo/PR_000026817), [PR:000026817](http://purl.obolibrary.org/obo/PR_000026817)                                                                                                                                                                                        |
| `Reactome:REACT_7607`    |              2 | [PR:000026823](http://purl.obolibrary.org/obo/PR_000026823), [PR:000026823](http://purl.obolibrary.org/obo/PR_000026823)                                                                                                                                                                                        |
| `Reactome:REACT_21988`   |              2 | [PR:000026843](http://purl.obolibrary.org/obo/PR_000026843), [PR:000026843](http://purl.obolibrary.org/obo/PR_000026843)                                                                                                                                                                                        |
| `Reactome:REACT_20926`   |              2 | [PR:000026848](http://purl.obolibrary.org/obo/PR_000026848), [PR:000026848](http://purl.obolibrary.org/obo/PR_000026848)                                                                                                                                                                                        |
| `Reactome:REACT_24400`   |              2 | [PR:000026855](http://purl.obolibrary.org/obo/PR_000026855), [PR:000026855](http://purl.obolibrary.org/obo/PR_000026855)                                                                                                                                                                                        |
| `Reactome:REACT_25472`   |              2 | [PR:000026858](http://purl.obolibrary.org/obo/PR_000026858), [PR:000026858](http://purl.obolibrary.org/obo/PR_000026858)                                                                                                                                                                                        |
| `Reactome:REACT_11876`   |              2 | [PR:000026864](http://purl.obolibrary.org/obo/PR_000026864), [PR:000026864](http://purl.obolibrary.org/obo/PR_000026864)                                                                                                                                                                                        |
| `Reactome:REACT_14122`   |              2 | [PR:000026869](http://purl.obolibrary.org/obo/PR_000026869), [PR:000026869](http://purl.obolibrary.org/obo/PR_000026869)                                                                                                                                                                                        |
| `Reactome:REACT_11742`   |              2 | [PR:000026870](http://purl.obolibrary.org/obo/PR_000026870), [PR:000026870](http://purl.obolibrary.org/obo/PR_000026870)                                                                                                                                                                                        |
| `Reactome:REACT_18039`   |              2 | [PR:000026871](http://purl.obolibrary.org/obo/PR_000026871), [PR:000026871](http://purl.obolibrary.org/obo/PR_000026871)                                                                                                                                                                                        |
| `Reactome:REACT_10483`   |              2 | [PR:000026872](http://purl.obolibrary.org/obo/PR_000026872), [PR:000026872](http://purl.obolibrary.org/obo/PR_000026872)                                                                                                                                                                                        |
| `Reactome:REACT_14906`   |              2 | [PR:000026873](http://purl.obolibrary.org/obo/PR_000026873), [PR:000026873](http://purl.obolibrary.org/obo/PR_000026873)                                                                                                                                                                                        |
| `Reactome:REACT_24832`   |              2 | [PR:000026874](http://purl.obolibrary.org/obo/PR_000026874), [PR:000026874](http://purl.obolibrary.org/obo/PR_000026874)                                                                                                                                                                                        |
| `Reactome:REACT_2467`    |              2 | [PR:000026879](http://purl.obolibrary.org/obo/PR_000026879), [PR:000026879](http://purl.obolibrary.org/obo/PR_000026879)                                                                                                                                                                                        |
| `Reactome:REACT_24521`   |              2 | [PR:000026881](http://purl.obolibrary.org/obo/PR_000026881), [PR:000026881](http://purl.obolibrary.org/obo/PR_000026881)                                                                                                                                                                                        |
| `Reactome:REACT_18932`   |              2 | [PR:000026884](http://purl.obolibrary.org/obo/PR_000026884), [PR:000026884](http://purl.obolibrary.org/obo/PR_000026884)                                                                                                                                                                                        |
| `Reactome:REACT_23224`   |              2 | [PR:000026887](http://purl.obolibrary.org/obo/PR_000026887), [PR:000026887](http://purl.obolibrary.org/obo/PR_000026887)                                                                                                                                                                                        |
| `Reactome:REACT_18748`   |              2 | [PR:000026890](http://purl.obolibrary.org/obo/PR_000026890), [PR:000026890](http://purl.obolibrary.org/obo/PR_000026890)                                                                                                                                                                                        |
| `Reactome:REACT_2634`    |              2 | [PR:000026892](http://purl.obolibrary.org/obo/PR_000026892), [PR:000026892](http://purl.obolibrary.org/obo/PR_000026892)                                                                                                                                                                                        |
| `Reactome:REACT_21601`   |              2 | [PR:000026893](http://purl.obolibrary.org/obo/PR_000026893), [PR:000026893](http://purl.obolibrary.org/obo/PR_000026893)                                                                                                                                                                                        |
| `Reactome:REACT_22798`   |              2 | [PR:000026894](http://purl.obolibrary.org/obo/PR_000026894), [PR:000026894](http://purl.obolibrary.org/obo/PR_000026894)                                                                                                                                                                                        |
| `Reactome:REACT_7270`    |              2 | [PR:000026895](http://purl.obolibrary.org/obo/PR_000026895), [PR:000026895](http://purl.obolibrary.org/obo/PR_000026895)                                                                                                                                                                                        |
| `Reactome:REACT_22641`   |              2 | [PR:000026896](http://purl.obolibrary.org/obo/PR_000026896), [PR:000026896](http://purl.obolibrary.org/obo/PR_000026896)                                                                                                                                                                                        |
| `Reactome:REACT_17344`   |              2 | [PR:000026897](http://purl.obolibrary.org/obo/PR_000026897), [PR:000026897](http://purl.obolibrary.org/obo/PR_000026897)                                                                                                                                                                                        |
| `Reactome:REACT_17071`   |              2 | [PR:000026898](http://purl.obolibrary.org/obo/PR_000026898), [PR:000026898](http://purl.obolibrary.org/obo/PR_000026898)                                                                                                                                                                                        |
| `Reactome:REACT_5359`    |              2 | [PR:000026899](http://purl.obolibrary.org/obo/PR_000026899), [PR:000026899](http://purl.obolibrary.org/obo/PR_000026899)                                                                                                                                                                                        |
| `Reactome:REACT_5249`    |              2 | [PR:000026900](http://purl.obolibrary.org/obo/PR_000026900), [PR:000026900](http://purl.obolibrary.org/obo/PR_000026900)                                                                                                                                                                                        |
| `Reactome:REACT_20457`   |              2 | [PR:000026901](http://purl.obolibrary.org/obo/PR_000026901), [PR:000026901](http://purl.obolibrary.org/obo/PR_000026901)                                                                                                                                                                                        |
| `Reactome:REACT_12893`   |              2 | [PR:000026902](http://purl.obolibrary.org/obo/PR_000026902), [PR:000026902](http://purl.obolibrary.org/obo/PR_000026902)                                                                                                                                                                                        |
| `Reactome:REACT_3972`    |              2 | [PR:000026903](http://purl.obolibrary.org/obo/PR_000026903), [PR:000026903](http://purl.obolibrary.org/obo/PR_000026903)                                                                                                                                                                                        |
| `Reactome:REACT_18666`   |              2 | [PR:000026905](http://purl.obolibrary.org/obo/PR_000026905), [PR:000026905](http://purl.obolibrary.org/obo/PR_000026905)                                                                                                                                                                                        |
| `Reactome:REACT_5274`    |              2 | [PR:000026906](http://purl.obolibrary.org/obo/PR_000026906), [PR:000026906](http://purl.obolibrary.org/obo/PR_000026906)                                                                                                                                                                                        |
| `Reactome:REACT_13274`   |              2 | [PR:000026907](http://purl.obolibrary.org/obo/PR_000026907), [PR:000026907](http://purl.obolibrary.org/obo/PR_000026907)                                                                                                                                                                                        |
| `Reactome:REACT_26960`   |              2 | [PR:000026908](http://purl.obolibrary.org/obo/PR_000026908), [PR:000026908](http://purl.obolibrary.org/obo/PR_000026908)                                                                                                                                                                                        |
| `Reactome:REACT_13308`   |              2 | [PR:000026909](http://purl.obolibrary.org/obo/PR_000026909), [PR:000026909](http://purl.obolibrary.org/obo/PR_000026909)                                                                                                                                                                                        |
| `Reactome:REACT_20475`   |              2 | [PR:000026910](http://purl.obolibrary.org/obo/PR_000026910), [PR:000026910](http://purl.obolibrary.org/obo/PR_000026910)                                                                                                                                                                                        |
| `Reactome:REACT_3002`    |              2 | [PR:000026911](http://purl.obolibrary.org/obo/PR_000026911), [PR:000026911](http://purl.obolibrary.org/obo/PR_000026911)                                                                                                                                                                                        |
| `Reactome:REACT_19823`   |              2 | [PR:000026915](http://purl.obolibrary.org/obo/PR_000026915), [PR:000026915](http://purl.obolibrary.org/obo/PR_000026915)                                                                                                                                                                                        |
| `Reactome:REACT_11458`   |              2 | [PR:000026919](http://purl.obolibrary.org/obo/PR_000026919), [PR:000026919](http://purl.obolibrary.org/obo/PR_000026919)                                                                                                                                                                                        |
| `Reactome:REACT_11286`   |              2 | [PR:000026923](http://purl.obolibrary.org/obo/PR_000026923), [PR:000026923](http://purl.obolibrary.org/obo/PR_000026923)                                                                                                                                                                                        |
| `Reactome:REACT_20177`   |              2 | [PR:000026927](http://purl.obolibrary.org/obo/PR_000026927), [PR:000026927](http://purl.obolibrary.org/obo/PR_000026927)                                                                                                                                                                                        |
| `Reactome:REACT_11508`   |              2 | [PR:000026931](http://purl.obolibrary.org/obo/PR_000026931), [PR:000026931](http://purl.obolibrary.org/obo/PR_000026931)                                                                                                                                                                                        |
| `Reactome:REACT_11960`   |              2 | [PR:000026935](http://purl.obolibrary.org/obo/PR_000026935), [PR:000026935](http://purl.obolibrary.org/obo/PR_000026935)                                                                                                                                                                                        |
| `Reactome:REACT_19919`   |              2 | [PR:000026936](http://purl.obolibrary.org/obo/PR_000026936), [PR:000026936](http://purl.obolibrary.org/obo/PR_000026936)                                                                                                                                                                                        |
| `Reactome:REACT_24028`   |              2 | [PR:000026941](http://purl.obolibrary.org/obo/PR_000026941), [PR:000026941](http://purl.obolibrary.org/obo/PR_000026941)                                                                                                                                                                                        |
| `Reactome:REACT_9652`    |              2 | [PR:000026942](http://purl.obolibrary.org/obo/PR_000026942), [PR:000026942](http://purl.obolibrary.org/obo/PR_000026942)                                                                                                                                                                                        |
| `Reactome:REACT_25995`   |              2 | [PR:000026948](http://purl.obolibrary.org/obo/PR_000026948), [PR:000026948](http://purl.obolibrary.org/obo/PR_000026948)                                                                                                                                                                                        |
| `Reactome:REACT_26163`   |              2 | [PR:000026949](http://purl.obolibrary.org/obo/PR_000026949), [PR:000026949](http://purl.obolibrary.org/obo/PR_000026949)                                                                                                                                                                                        |
| `Reactome:REACT_4847`    |              2 | [PR:000026950](http://purl.obolibrary.org/obo/PR_000026950), [PR:000026950](http://purl.obolibrary.org/obo/PR_000026950)                                                                                                                                                                                        |
| `Reactome:REACT_20286`   |              2 | [PR:000026954](http://purl.obolibrary.org/obo/PR_000026954), [PR:000026954](http://purl.obolibrary.org/obo/PR_000026954)                                                                                                                                                                                        |
| `Reactome:REACT_11392`   |              2 | [PR:000026958](http://purl.obolibrary.org/obo/PR_000026958), [PR:000026958](http://purl.obolibrary.org/obo/PR_000026958)                                                                                                                                                                                        |
| `Reactome:REACT_14034`   |              2 | [PR:000026959](http://purl.obolibrary.org/obo/PR_000026959), [PR:000026959](http://purl.obolibrary.org/obo/PR_000026959)                                                                                                                                                                                        |
| `Reactome:REACT_7543`    |              2 | [PR:000026960](http://purl.obolibrary.org/obo/PR_000026960), [PR:000026960](http://purl.obolibrary.org/obo/PR_000026960)                                                                                                                                                                                        |
| `Reactome:REACT_20251`   |              2 | [PR:000026961](http://purl.obolibrary.org/obo/PR_000026961), [PR:000026961](http://purl.obolibrary.org/obo/PR_000026961)                                                                                                                                                                                        |
| `Reactome:REACT_13968`   |              2 | [PR:000026962](http://purl.obolibrary.org/obo/PR_000026962), [PR:000026962](http://purl.obolibrary.org/obo/PR_000026962)                                                                                                                                                                                        |
| `Reactome:REACT_7729`    |              2 | [PR:000026963](http://purl.obolibrary.org/obo/PR_000026963), [PR:000026963](http://purl.obolibrary.org/obo/PR_000026963)                                                                                                                                                                                        |
| `Reactome:REACT_14357`   |              2 | [PR:000026964](http://purl.obolibrary.org/obo/PR_000026964), [PR:000026964](http://purl.obolibrary.org/obo/PR_000026964)                                                                                                                                                                                        |
| `Reactome:REACT_25762`   |              2 | [PR:000026965](http://purl.obolibrary.org/obo/PR_000026965), [PR:000026965](http://purl.obolibrary.org/obo/PR_000026965)                                                                                                                                                                                        |
| `Reactome:REACT_27011`   |              2 | [PR:000026966](http://purl.obolibrary.org/obo/PR_000026966), [PR:000026966](http://purl.obolibrary.org/obo/PR_000026966)                                                                                                                                                                                        |
| `Reactome:REACT_4286`    |              2 | [PR:000026967](http://purl.obolibrary.org/obo/PR_000026967), [PR:000026967](http://purl.obolibrary.org/obo/PR_000026967)                                                                                                                                                                                        |
| `Reactome:REACT_25975`   |              2 | [PR:000026968](http://purl.obolibrary.org/obo/PR_000026968), [PR:000026968](http://purl.obolibrary.org/obo/PR_000026968)                                                                                                                                                                                        |
| `Reactome:REACT_20765`   |              2 | [PR:000026971](http://purl.obolibrary.org/obo/PR_000026971), [PR:000026971](http://purl.obolibrary.org/obo/PR_000026971)                                                                                                                                                                                        |
| `Reactome:REACT_4770`    |              2 | [PR:000026972](http://purl.obolibrary.org/obo/PR_000026972), [PR:000026972](http://purl.obolibrary.org/obo/PR_000026972)                                                                                                                                                                                        |
| `Reactome:REACT_5375`    |              2 | [PR:000026973](http://purl.obolibrary.org/obo/PR_000026973), [PR:000026973](http://purl.obolibrary.org/obo/PR_000026973)                                                                                                                                                                                        |
| `Reactome:REACT_26927`   |              2 | [PR:000026974](http://purl.obolibrary.org/obo/PR_000026974), [PR:000026974](http://purl.obolibrary.org/obo/PR_000026974)                                                                                                                                                                                        |
| `Reactome:REACT_26583`   |              2 | [PR:000026975](http://purl.obolibrary.org/obo/PR_000026975), [PR:000026975](http://purl.obolibrary.org/obo/PR_000026975)                                                                                                                                                                                        |
| `Reactome:REACT_21738`   |              2 | [PR:000026976](http://purl.obolibrary.org/obo/PR_000026976), [PR:000026976](http://purl.obolibrary.org/obo/PR_000026976)                                                                                                                                                                                        |
| `Reactome:REACT_8757`    |              2 | [PR:000026977](http://purl.obolibrary.org/obo/PR_000026977), [PR:000026977](http://purl.obolibrary.org/obo/PR_000026977)                                                                                                                                                                                        |
| `Reactome:REACT_20891`   |              2 | [PR:000026978](http://purl.obolibrary.org/obo/PR_000026978), [PR:000026978](http://purl.obolibrary.org/obo/PR_000026978)                                                                                                                                                                                        |
| `Reactome:REACT_7636`    |              2 | [PR:000026979](http://purl.obolibrary.org/obo/PR_000026979), [PR:000026979](http://purl.obolibrary.org/obo/PR_000026979)                                                                                                                                                                                        |
| `Reactome:REACT_18737`   |              2 | [PR:000026980](http://purl.obolibrary.org/obo/PR_000026980), [PR:000026980](http://purl.obolibrary.org/obo/PR_000026980)                                                                                                                                                                                        |
| `Reactome:REACT_13099`   |              2 | [PR:000026981](http://purl.obolibrary.org/obo/PR_000026981), [PR:000026981](http://purl.obolibrary.org/obo/PR_000026981)                                                                                                                                                                                        |
| `Reactome:REACT_3265`    |              2 | [PR:000026982](http://purl.obolibrary.org/obo/PR_000026982), [PR:000026982](http://purl.obolibrary.org/obo/PR_000026982)                                                                                                                                                                                        |
| `Reactome:REACT_22715`   |              2 | [PR:000027058](http://purl.obolibrary.org/obo/PR_000027058), [PR:000027058](http://purl.obolibrary.org/obo/PR_000027058)                                                                                                                                                                                        |
| `Reactome:REACT_26957`   |              2 | [PR:000027084](http://purl.obolibrary.org/obo/PR_000027084), [PR:000027084](http://purl.obolibrary.org/obo/PR_000027084)                                                                                                                                                                                        |
| `Reactome:REACT_21965`   |              2 | [PR:000027086](http://purl.obolibrary.org/obo/PR_000027086), [PR:000027086](http://purl.obolibrary.org/obo/PR_000027086)                                                                                                                                                                                        |
| `Reactome:REACT_6364`    |              2 | [PR:000027129](http://purl.obolibrary.org/obo/PR_000027129), [PR:000027130](http://purl.obolibrary.org/obo/PR_000027130)                                                                                                                                                                                        |
| `Reactome:REACT_6604`    |              2 | [PR:000027129](http://purl.obolibrary.org/obo/PR_000027129), [PR:000027130](http://purl.obolibrary.org/obo/PR_000027130)                                                                                                                                                                                        |
| `Reactome:REACT_5303`    |              2 | [PR:000027131](http://purl.obolibrary.org/obo/PR_000027131), [PR:000027132](http://purl.obolibrary.org/obo/PR_000027132)                                                                                                                                                                                        |
| `Reactome:REACT_15869`   |              2 | [PR:000027407](http://purl.obolibrary.org/obo/PR_000027407), [PR:000027407](http://purl.obolibrary.org/obo/PR_000027407)                                                                                                                                                                                        |
| `Reactome:REACT_25495`   |              2 | [PR:000027494](http://purl.obolibrary.org/obo/PR_000027494), [PR:000027494](http://purl.obolibrary.org/obo/PR_000027494)                                                                                                                                                                                        |
| `Reactome:REACT_24633`   |              2 | [PR:000028429](http://purl.obolibrary.org/obo/PR_000028429), [PR:000028429](http://purl.obolibrary.org/obo/PR_000028429)                                                                                                                                                                                        |
| `Reactome:REACT_12228`   |              2 | [PR:000028431](http://purl.obolibrary.org/obo/PR_000028431), [PR:000028431](http://purl.obolibrary.org/obo/PR_000028431)                                                                                                                                                                                        |
| `Reactome:REACT_2659`    |              2 | [PR:000028432](http://purl.obolibrary.org/obo/PR_000028432), [PR:000028432](http://purl.obolibrary.org/obo/PR_000028432)                                                                                                                                                                                        |
| `Reactome:REACT_8593`    |              2 | [PR:000028433](http://purl.obolibrary.org/obo/PR_000028433), [PR:000028433](http://purl.obolibrary.org/obo/PR_000028433)                                                                                                                                                                                        |
| `Reactome:REACT_3424`    |              2 | [PR:000028434](http://purl.obolibrary.org/obo/PR_000028434), [PR:000028434](http://purl.obolibrary.org/obo/PR_000028434)                                                                                                                                                                                        |
| `Reactome:REACT_4646`    |              2 | [PR:000028435](http://purl.obolibrary.org/obo/PR_000028435), [PR:000028435](http://purl.obolibrary.org/obo/PR_000028435)                                                                                                                                                                                        |
| `Reactome:REACT_12775`   |              2 | [PR:000028436](http://purl.obolibrary.org/obo/PR_000028436), [PR:000028436](http://purl.obolibrary.org/obo/PR_000028436)                                                                                                                                                                                        |
| `Reactome:REACT_3905`    |              2 | [PR:000028437](http://purl.obolibrary.org/obo/PR_000028437), [PR:000028437](http://purl.obolibrary.org/obo/PR_000028437)                                                                                                                                                                                        |
| `Reactome:REACT_23098`   |              2 | [PR:000028438](http://purl.obolibrary.org/obo/PR_000028438), [PR:000028438](http://purl.obolibrary.org/obo/PR_000028438)                                                                                                                                                                                        |
| `Reactome:REACT_4224`    |              2 | [PR:000028439](http://purl.obolibrary.org/obo/PR_000028439), [PR:000028439](http://purl.obolibrary.org/obo/PR_000028439)                                                                                                                                                                                        |
| `Reactome:REACT_13271`   |              2 | [PR:000028440](http://purl.obolibrary.org/obo/PR_000028440), [PR:000028440](http://purl.obolibrary.org/obo/PR_000028440)                                                                                                                                                                                        |
| `Reactome:REACT_17570`   |              2 | [PR:000028441](http://purl.obolibrary.org/obo/PR_000028441), [PR:000028441](http://purl.obolibrary.org/obo/PR_000028441)                                                                                                                                                                                        |
| `Reactome:REACT_5786`    |              2 | [PR:000028442](http://purl.obolibrary.org/obo/PR_000028442), [PR:000028442](http://purl.obolibrary.org/obo/PR_000028442)                                                                                                                                                                                        |
| `Reactome:REACT_12835`   |              2 | [PR:000028443](http://purl.obolibrary.org/obo/PR_000028443), [PR:000028443](http://purl.obolibrary.org/obo/PR_000028443)                                                                                                                                                                                        |
| `Reactome:REACT_22747`   |              2 | [PR:000028444](http://purl.obolibrary.org/obo/PR_000028444), [PR:000028444](http://purl.obolibrary.org/obo/PR_000028444)                                                                                                                                                                                        |
| `Reactome:REACT_14140`   |              2 | [PR:000028445](http://purl.obolibrary.org/obo/PR_000028445), [PR:000028445](http://purl.obolibrary.org/obo/PR_000028445)                                                                                                                                                                                        |
| `Reactome:REACT_5426`    |              2 | [PR:000028446](http://purl.obolibrary.org/obo/PR_000028446), [PR:000028446](http://purl.obolibrary.org/obo/PR_000028446)                                                                                                                                                                                        |
| `Reactome:REACT_12182`   |              2 | [PR:000028447](http://purl.obolibrary.org/obo/PR_000028447), [PR:000028447](http://purl.obolibrary.org/obo/PR_000028447)                                                                                                                                                                                        |
| `Reactome:REACT_20766`   |              2 | [PR:000028448](http://purl.obolibrary.org/obo/PR_000028448), [PR:000028448](http://purl.obolibrary.org/obo/PR_000028448)                                                                                                                                                                                        |
| `Reactome:REACT_11737`   |              2 | [PR:000028449](http://purl.obolibrary.org/obo/PR_000028449), [PR:000028449](http://purl.obolibrary.org/obo/PR_000028449)                                                                                                                                                                                        |
| `Reactome:REACT_25979`   |              2 | [PR:000028450](http://purl.obolibrary.org/obo/PR_000028450), [PR:000028450](http://purl.obolibrary.org/obo/PR_000028450)                                                                                                                                                                                        |
| `Reactome:REACT_22956`   |              2 | [PR:000028451](http://purl.obolibrary.org/obo/PR_000028451), [PR:000028451](http://purl.obolibrary.org/obo/PR_000028451)                                                                                                                                                                                        |
| `Reactome:REACT_4419`    |              2 | [PR:000028452](http://purl.obolibrary.org/obo/PR_000028452), [PR:000028452](http://purl.obolibrary.org/obo/PR_000028452)                                                                                                                                                                                        |
| `Reactome:REACT_3276`    |              2 | [PR:000028453](http://purl.obolibrary.org/obo/PR_000028453), [PR:000028453](http://purl.obolibrary.org/obo/PR_000028453)                                                                                                                                                                                        |
| `Reactome:REACT_3978`    |              2 | [PR:000028454](http://purl.obolibrary.org/obo/PR_000028454), [PR:000028454](http://purl.obolibrary.org/obo/PR_000028454)                                                                                                                                                                                        |
| `Reactome:REACT_21702`   |              2 | [PR:000028455](http://purl.obolibrary.org/obo/PR_000028455), [PR:000028455](http://purl.obolibrary.org/obo/PR_000028455)                                                                                                                                                                                        |
| `Reactome:REACT_26411`   |              2 | [PR:000028696](http://purl.obolibrary.org/obo/PR_000028696), [PR:000028696](http://purl.obolibrary.org/obo/PR_000028696)                                                                                                                                                                                        |
| `Reactome:REACT_25318`   |              2 | [PR:000028705](http://purl.obolibrary.org/obo/PR_000028705), [PR:000028705](http://purl.obolibrary.org/obo/PR_000028705)                                                                                                                                                                                        |
| `Reactome:REACT_7740.1`  |              2 | [PR:000002147](http://purl.obolibrary.org/obo/PR_000002147), [PR:000002149](http://purl.obolibrary.org/obo/PR_000002149)                                                                                                                                                                                        |
| `Reactome:REACT_25571`   |              2 | [PR:000027190](http://purl.obolibrary.org/obo/PR_000027190), [PR:000027191](http://purl.obolibrary.org/obo/PR_000027191)                                                                                                                                                                                        |
| `Reactome:REACT_7451`    |              2 | [PR:000027744](http://purl.obolibrary.org/obo/PR_000027744), [PR:000027745](http://purl.obolibrary.org/obo/PR_000027745)                                                                                                                                                                                        |
| `Reactome:REACT_7364`    |              2 | [PR:000027746](http://purl.obolibrary.org/obo/PR_000027746), [PR:000027747](http://purl.obolibrary.org/obo/PR_000027747)                                                                                                                                                                                        |
| `Reactome:69278`         |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                                                                                                                                                                                                                         |
| `Reactome:428625`        |              1 | [GO:0005276](http://purl.obolibrary.org/obo/GO_0005276)                                                                                                                                                                                                                                                         |
| `Reactome:163103`        |              1 | [GO:0008389](http://purl.obolibrary.org/obo/GO_0008389)                                                                                                                                                                                                                                                         |
| `Reactome:REACT_3925.1`  |              1 | [PR:000002439](http://purl.obolibrary.org/obo/PR_000002439)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_4414.2`  |              1 | [PR:000003150](http://purl.obolibrary.org/obo/PR_000003150)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_12828.1` |              1 | [PR:000003238](http://purl.obolibrary.org/obo/PR_000003238)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_8478`    |              1 | [PR:000025773](http://purl.obolibrary.org/obo/PR_000025773)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_7694`    |              1 | [PR:000025785](http://purl.obolibrary.org/obo/PR_000025785)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_12828`   |              1 | [PR:000026136](http://purl.obolibrary.org/obo/PR_000026136)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_5366`    |              1 | [PR:000026173](http://purl.obolibrary.org/obo/PR_000026173)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_24452`   |              1 | [PR:000026549](http://purl.obolibrary.org/obo/PR_000026549)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_20709.1` |              1 | [PR:000026550](http://purl.obolibrary.org/obo/PR_000026550)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_24378`   |              1 | [PR:000026550](http://purl.obolibrary.org/obo/PR_000026550)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_3920`    |              1 | [PR:000026904](http://purl.obolibrary.org/obo/PR_000026904)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_25097`   |              1 | [PR:000027191](http://purl.obolibrary.org/obo/PR_000027191)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_7256`    |              1 | [PR:000027495](http://purl.obolibrary.org/obo/PR_000027495)                                                                                                                                                                                                                                                     |
| `Reactome:117805.1`      |              1 | [GO:0038140](http://purl.obolibrary.org/obo/GO_0038140)                                                                                                                                                                                                                                                         |
| `Reactome:REACT_7508.1`  |              1 | [PR:000000523](http://purl.obolibrary.org/obo/PR_000000523)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_12354.1` |              1 | [PR:000000647](http://purl.obolibrary.org/obo/PR_000000647)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_12102.1` |              1 | [PR:000000661](http://purl.obolibrary.org/obo/PR_000000661)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_12302.1` |              1 | [PR:000000666](http://purl.obolibrary.org/obo/PR_000000666)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_7149`    |              1 | [PR:000025763](http://purl.obolibrary.org/obo/PR_000025763)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_7491`    |              1 | [PR:000025770](http://purl.obolibrary.org/obo/PR_000025770)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_13072`   |              1 | [PR:000025780](http://purl.obolibrary.org/obo/PR_000025780)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_13214`   |              1 | [PR:000025782](http://purl.obolibrary.org/obo/PR_000025782)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_7660`    |              1 | [PR:000025786](http://purl.obolibrary.org/obo/PR_000025786)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_20178`   |              1 | [PR:000025790](http://purl.obolibrary.org/obo/PR_000025790)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_20268`   |              1 | [PR:000025792](http://purl.obolibrary.org/obo/PR_000025792)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_7726`    |              1 | [PR:000025927](http://purl.obolibrary.org/obo/PR_000025927)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_7263`    |              1 | [PR:000025934](http://purl.obolibrary.org/obo/PR_000025934)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_7719`    |              1 | [PR:000025934](http://purl.obolibrary.org/obo/PR_000025934)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_7100`    |              1 | [PR:000025938](http://purl.obolibrary.org/obo/PR_000025938)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_7802`    |              1 | [PR:000025938](http://purl.obolibrary.org/obo/PR_000025938)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_5391`    |              1 | [PR:000026211](http://purl.obolibrary.org/obo/PR_000026211)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_10376`   |              1 | [PR:000026735](http://purl.obolibrary.org/obo/PR_000026735)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_3557`    |              1 | [PR:000026876](http://purl.obolibrary.org/obo/PR_000026876)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_4142`    |              1 | [PR:000026877](http://purl.obolibrary.org/obo/PR_000026877)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_3571`    |              1 | [PR:000027057](http://purl.obolibrary.org/obo/PR_000027057)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_21912`   |              1 | [PR:000027082](http://purl.obolibrary.org/obo/PR_000027082)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_26303`   |              1 | [PR:000027111](http://purl.obolibrary.org/obo/PR_000027111)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_4395`    |              1 | [PR:000027127](http://purl.obolibrary.org/obo/PR_000027127)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_5467`    |              1 | [PR:000027127](http://purl.obolibrary.org/obo/PR_000027127)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_7025`    |              1 | [PR:000027183](http://purl.obolibrary.org/obo/PR_000027183)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_25610`   |              1 | [PR:000027184](http://purl.obolibrary.org/obo/PR_000027184)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_26813`   |              1 | [PR:000027192](http://purl.obolibrary.org/obo/PR_000027192)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_7187`    |              1 | [PR:000027201](http://purl.obolibrary.org/obo/PR_000027201)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_8486`    |              1 | [PR:000027273](http://purl.obolibrary.org/obo/PR_000027273)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_7742`    |              1 | [PR:000027492](http://purl.obolibrary.org/obo/PR_000027492)                                                                                                                                                                                                                                                     |
| `Reactome:REACT_26696`   |              1 | [PR:000027493](http://purl.obolibrary.org/obo/PR_000027493)                                                                                                                                                                                                                                                     |

## `REACTOME`: Reactome

Overall, there were 2 invalid
xrefs to external prefixed with `REACTOME` (standardized to Bioregistry
prefix [`reactome`](https://bioregistry.io/reactome)) that
did not match the standard pattern `^R-[A-Z]{3}-\d+(-\d+)?(\.\d+)?$`.

| external_xref          |   usages_count | usages                                                      |
|------------------------|----------------|-------------------------------------------------------------|
| `REACTOME:REACT_26959` |              1 | [PR:000028697](http://purl.obolibrary.org/obo/PR_000028697) |
| `REACTOME:REACT_27000` |              1 | [PR:000028699](http://purl.obolibrary.org/obo/PR_000028699) |

## `RefSeq`: Reference Sequence Collection

Overall, there were 2 invalid
xrefs to external prefixed with `RefSeq` (standardized to Bioregistry
prefix [`refseq`](https://bioregistry.io/refseq)) that
did not match the standard pattern `^(((AC|AP|NC|NG|NM|NP|NR|NT|NW|WP|XM|XP|XR|YP|ZP)_\d+)|(NZ_[A-Z]{2,4}\d+))(\.\d+)?$`.

| external_xref                       |   usages_count | usages                                                      |
|-------------------------------------|----------------|-------------------------------------------------------------|
| `RefSeq:NP_001020102|PMID:21747913` |              1 | [PR:000028836](http://purl.obolibrary.org/obo/PR_000028836) |
| `RefSeq:CAB01006.1`                 |              1 | [PR:000025992](http://purl.obolibrary.org/obo/PR_000025992) |

## `RFAM`: Rfam database of RNA families

Overall, there were 2 invalid
xrefs to external prefixed with `RFAM` (standardized to Bioregistry
prefix [`rfam`](https://bioregistry.io/rfam)) that
did not match the standard pattern `^RF\d{5}$`.

| external_xref   |   usages_count | usages                                                                                                           |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `RFAM:jd`       |              2 | [SO:0001427](http://purl.obolibrary.org/obo/SO_0001427), [SO:0001459](http://purl.obolibrary.org/obo/SO_0001459) |

## `RO_proposed_relation`: Relation Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `RO_proposed_relation` (standardized to Bioregistry
prefix [`ro`](https://bioregistry.io/ro)) that
did not match the standard pattern `^(HOM)?\d{7}$`.

| external_xref                        |   usages_count | usages                                                        |
|--------------------------------------|----------------|---------------------------------------------------------------|
| `RO_proposed_relation:homologous_to` |              1 | [RO:HOM0000007](http://purl.obolibrary.org/obo/RO_HOM0000007) |

## `SAO`: Subcellular Anatomy Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `SAO` (standardized to Bioregistry
prefix [`sao`](https://bioregistry.io/sao)) that
did not match the standard pattern `^\d+$`.

| external_xref      |   usages_count | usages                                                  |
|--------------------|----------------|---------------------------------------------------------|
| `SAO:sao131261273` |              1 | [CL:1001571](http://purl.obolibrary.org/obo/CL_1001571) |

## `SGD`: Saccharomyces Genome Database

Overall, there were 12 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
prefix [`sgd`](https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:jd`        |              6 | [SO:0002001](http://purl.obolibrary.org/obo/SO_0002001), [SO:0002002](http://purl.obolibrary.org/obo/SO_0002002), [SO:0002003](http://purl.obolibrary.org/obo/SO_0002003), [SO:0002004](http://purl.obolibrary.org/obo/SO_0002004), [SO:0002024](http://purl.obolibrary.org/obo/SO_0002024), ... |
| `SGD:rb`        |              3 | [SO:0000236](http://purl.obolibrary.org/obo/SO_0000236), [SO:0000717](http://purl.obolibrary.org/obo/SO_0000717), [SO:0000718](http://purl.obolibrary.org/obo/SO_0000718)                                                                                                                        |
| `SGD:se`        |              3 | [SO:0002048](http://purl.obolibrary.org/obo/SO_0002048), [SO:0002059](http://purl.obolibrary.org/obo/SO_0002059), [SO:0005853](http://purl.obolibrary.org/obo/SO_0005853)                                                                                                                        |

## `SO`: Sequence types and features ontology

Overall, there were 1,239 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                  |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|--------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SO:ke`                        |            893 | [SO:0000001](http://purl.obolibrary.org/obo/SO_0000001), [SO:0000002](http://purl.obolibrary.org/obo/SO_0000002), [SO:0000006](http://purl.obolibrary.org/obo/SO_0000006), [SO:0000013](http://purl.obolibrary.org/obo/SO_0000013), [SO:0000020](http://purl.obolibrary.org/obo/SO_0000020), ... |
| `SO:xp`                        |            109 | [SO:0000078](http://purl.obolibrary.org/obo/SO_0000078), [SO:0000087](http://purl.obolibrary.org/obo/SO_0000087), [SO:0000088](http://purl.obolibrary.org/obo/SO_0000088), [SO:0000089](http://purl.obolibrary.org/obo/SO_0000089), [SO:0000090](http://purl.obolibrary.org/obo/SO_0000090), ... |
| `SO:ma`                        |             76 | [SO:0000036](http://purl.obolibrary.org/obo/SO_0000036), [SO:0000037](http://purl.obolibrary.org/obo/SO_0000037), [SO:0000040](http://purl.obolibrary.org/obo/SO_0000040), [SO:0000042](http://purl.obolibrary.org/obo/SO_0000042), [SO:0000051](http://purl.obolibrary.org/obo/SO_0000051), ... |
| `SO:cb`                        |             41 | [SO:0000059](http://purl.obolibrary.org/obo/SO_0000059), [SO:0000061](http://purl.obolibrary.org/obo/SO_0000061), [SO:0000419](http://purl.obolibrary.org/obo/SO_0000419), [SO:0000694](http://purl.obolibrary.org/obo/SO_0000694), [SO:0000836](http://purl.obolibrary.org/obo/SO_0000836), ... |
| `SO:nlw`                       |             21 | [SO:0000708](http://purl.obolibrary.org/obo/SO_0000708), [SO:0000709](http://purl.obolibrary.org/obo/SO_0000709), [SO:0001464](http://purl.obolibrary.org/obo/SO_0001464), [SO:0001465](http://purl.obolibrary.org/obo/SO_0001465), [SO:0001466](http://purl.obolibrary.org/obo/SO_0001466), ... |
| `SO:as`                        |             14 | [SO:0000140](http://purl.obolibrary.org/obo/SO_0000140), [SO:0000365](http://purl.obolibrary.org/obo/SO_0000365), [SO:0000367](http://purl.obolibrary.org/obo/SO_0000367), [SO:0000942](http://purl.obolibrary.org/obo/SO_0000942), [SO:0000943](http://purl.obolibrary.org/obo/SO_0000943), ... |
| `SO:cjm`                       |             11 | [SO:0000162](http://purl.obolibrary.org/obo/SO_0000162), [SO:0000163](http://purl.obolibrary.org/obo/SO_0000163), [SO:0000164](http://purl.obolibrary.org/obo/SO_0000164), [SO:0000196](http://purl.obolibrary.org/obo/SO_0000196), [SO:0000197](http://purl.obolibrary.org/obo/SO_0000197), ... |
| `SO:immuno_workshop`           |              9 | [SO:0000704](http://purl.obolibrary.org/obo/SO_0000704), [SO:0001023](http://purl.obolibrary.org/obo/SO_0001023), [SO:0001024](http://purl.obolibrary.org/obo/SO_0001024), [SO:0001025](http://purl.obolibrary.org/obo/SO_0001025), [SO:0001026](http://purl.obolibrary.org/obo/SO_0001026), ... |
| `SO:rd`                        |              7 | [SO:0000150](http://purl.obolibrary.org/obo/SO_0000150), [SO:0000307](http://purl.obolibrary.org/obo/SO_0000307), [SO:0000337](http://purl.obolibrary.org/obo/SO_0000337), [SO:0000339](http://purl.obolibrary.org/obo/SO_0000339), [SO:0000468](http://purl.obolibrary.org/obo/SO_0000468), ... |
| `SO:vw`                        |              7 | [SO:0001794](http://purl.obolibrary.org/obo/SO_0001794), [SO:0001795](http://purl.obolibrary.org/obo/SO_0001795), [SO:0001796](http://purl.obolibrary.org/obo/SO_0001796), [SO:0001798](http://purl.obolibrary.org/obo/SO_0001798), [SO:0001799](http://purl.obolibrary.org/obo/SO_0001799), ... |
| `SO:bm`                        |              6 | [SO:0001218](http://purl.obolibrary.org/obo/SO_0001218), [SO:0001483](http://purl.obolibrary.org/obo/SO_0001483), [SO:0001745](http://purl.obolibrary.org/obo/SO_0001745), [SO:0001746](http://purl.obolibrary.org/obo/SO_0001746), [SO:0001902](http://purl.obolibrary.org/obo/SO_0001902), ... |
| `SO:ls`                        |              4 | [SO:0000007](http://purl.obolibrary.org/obo/SO_0000007), [SO:0000148](http://purl.obolibrary.org/obo/SO_0000148), [SO:0000149](http://purl.obolibrary.org/obo/SO_0000149), [SO:0000688](http://purl.obolibrary.org/obo/SO_0000688)                                                               |
| `SO:regcreative`               |              4 | [SO:0000167](http://purl.obolibrary.org/obo/SO_0000167), [SO:0000627](http://purl.obolibrary.org/obo/SO_0000627), [SO:0001055](http://purl.obolibrary.org/obo/SO_0001055), [SO:0001058](http://purl.obolibrary.org/obo/SO_0001058)                                                               |
| `SO:ml`                        |              4 | [SO:0001668](http://purl.obolibrary.org/obo/SO_0001668), [SO:0001980](http://purl.obolibrary.org/obo/SO_0001980), [SO:0001981](http://purl.obolibrary.org/obo/SO_0001981), [SO:0001982](http://purl.obolibrary.org/obo/SO_0001982)                                                               |
| `SO:ds`                        |              4 | [SO:0002329](http://purl.obolibrary.org/obo/SO_0002329), [SO:0002330](http://purl.obolibrary.org/obo/SO_0002330), [SO:0002331](http://purl.obolibrary.org/obo/SO_0002331), [SO:0002332](http://purl.obolibrary.org/obo/SO_0002332)                                                               |
| `SO:andrewgibson`              |              3 | [SO:0001915](http://purl.obolibrary.org/obo/SO_0001915), [SO:0001916](http://purl.obolibrary.org/obo/SO_0001916), [SO:0001917](http://purl.obolibrary.org/obo/SO_0001917)                                                                                                                        |
| `SO:rtapella`                  |              3 | [SO:0001918](http://purl.obolibrary.org/obo/SO_0001918), [SO:0001919](http://purl.obolibrary.org/obo/SO_0001919), [SO:0001920](http://purl.obolibrary.org/obo/SO_0001920)                                                                                                                        |
| `SO:non_functional_homolog_of` |              2 | [RO:HOM0000016](http://purl.obolibrary.org/obo/RO_HOM0000016), [RO:HOM0000016](http://purl.obolibrary.org/obo/RO_HOM0000016)                                                                                                                                                                     |
| `SO:jk`                        |              2 | [SO:0000931](http://purl.obolibrary.org/obo/SO_0000931), [SO:0000978](http://purl.obolibrary.org/obo/SO_0000978)                                                                                                                                                                                 |
| `SO:chado`                     |              2 | [SO:0001416](http://purl.obolibrary.org/obo/SO_0001416), [SO:0001417](http://purl.obolibrary.org/obo/SO_0001417)                                                                                                                                                                                 |
| `SO:jh`                        |              1 | [SO:0000552](http://purl.obolibrary.org/obo/SO_0000552)                                                                                                                                                                                                                                          |
| `SO:SG`                        |              1 | [SO:0000727](http://purl.obolibrary.org/obo/SO_0000727)                                                                                                                                                                                                                                          |
| `SO:GAR`                       |              1 | [SO:0000839](http://purl.obolibrary.org/obo/SO_0000839)                                                                                                                                                                                                                                          |
| `SO:jestill`                   |              1 | [SO:0001642](http://purl.obolibrary.org/obo/SO_0001642)                                                                                                                                                                                                                                          |
| `SO:db`                        |              1 | [SO:0001645](http://purl.obolibrary.org/obo/SO_0001645)                                                                                                                                                                                                                                          |
| `SO:AF`                        |              1 | [SO:0001658](http://purl.obolibrary.org/obo/SO_0001658)                                                                                                                                                                                                                                          |
| `SO:KE`                        |              1 | [SO:0001731](http://purl.obolibrary.org/obo/SO_0001731)                                                                                                                                                                                                                                          |
| `SO:mc`                        |              1 | [SO:0001740](http://purl.obolibrary.org/obo/SO_0001740)                                                                                                                                                                                                                                          |
| `SO:hd`                        |              1 | [SO:0001741](http://purl.obolibrary.org/obo/SO_0001741)                                                                                                                                                                                                                                          |
| `SO:BM`                        |              1 | [SO:0001744](http://purl.obolibrary.org/obo/SO_0001744)                                                                                                                                                                                                                                          |
| `SO:myl`                       |              1 | [SO:0001959](http://purl.obolibrary.org/obo/SO_0001959)                                                                                                                                                                                                                                          |
| `SO:rs`                        |              1 | [SO:0002049](http://purl.obolibrary.org/obo/SO_0002049)                                                                                                                                                                                                                                          |
| `SO:nrs`                       |              1 | [SO:0002095](http://purl.obolibrary.org/obo/SO_0002095)                                                                                                                                                                                                                                          |
| `SO:similar_to`                |              1 | [RO:HOM0000000](http://purl.obolibrary.org/obo/RO_HOM0000000)                                                                                                                                                                                                                                    |
| `SO:homologous_to`             |              1 | [RO:HOM0000007](http://purl.obolibrary.org/obo/RO_HOM0000007)                                                                                                                                                                                                                                    |
| `SO:paralogous_to`             |              1 | [RO:HOM0000011](http://purl.obolibrary.org/obo/RO_HOM0000011)                                                                                                                                                                                                                                    |
| `SO:orthologous_to`            |              1 | [RO:HOM0000017](http://purl.obolibrary.org/obo/RO_HOM0000017)                                                                                                                                                                                                                                    |

## `TAO`: Teleost Anatomy Ontology

Overall, there were 604 invalid
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
| `TAO:homologous_to`                        |              1 | [RO:HOM0000007](http://purl.obolibrary.org/obo/RO_HOM0000007)                                                                                                                                                                                                                                                                            |

## `TC`: Transporter Classification Database

Overall, there were 38 invalid
xrefs to external prefixed with `TC` (standardized to Bioregistry
prefix [`tcdb`](https://bioregistry.io/tcdb)) that
did not match the standard pattern `^\d+(\.[A-Z])?(\.\d+)?(\.\d+)?(\.\d+)?$`.

| external_xref   |   usages_count | usages                                                                                                                                                                    |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TC:2.A.21.3.-` |              3 | [GO:0005362](http://purl.obolibrary.org/obo/GO_0005362), [GO:0005412](http://purl.obolibrary.org/obo/GO_0005412), [GO:0015371](http://purl.obolibrary.org/obo/GO_0015371) |
| `TC:2.A.2.-.-`  |              2 | [GO:0009669](http://purl.obolibrary.org/obo/GO_0009669), [GO:0015486](http://purl.obolibrary.org/obo/GO_0015486)                                                          |
| `TC:3.A.3.-.-`  |              1 | [GO:0003936](http://purl.obolibrary.org/obo/GO_0003936)                                                                                                                   |
| `TC:2.A.22.-.-` |              1 | [GO:0005328](http://purl.obolibrary.org/obo/GO_0005328)                                                                                                                   |
| `TC:2.A.21.4.-` |              1 | [GO:0005367](http://purl.obolibrary.org/obo/GO_0005367)                                                                                                                   |
| `TC:2.A.28.-.-` |              1 | [GO:0008508](http://purl.obolibrary.org/obo/GO_0008508)                                                                                                                   |
| `TC:2.A.53.-.-` |              1 | [GO:0008512](http://purl.obolibrary.org/obo/GO_0008512)                                                                                                                   |
| `TC:2.A.7.-.-`  |              1 | [GO:0009670](http://purl.obolibrary.org/obo/GO_0009670)                                                                                                                   |
| `TC:2.A.20.-.-` |              1 | [GO:0009673](http://purl.obolibrary.org/obo/GO_0009673)                                                                                                                   |
| `TC:2.A.1.-.-`  |              1 | [GO:0009679](http://purl.obolibrary.org/obo/GO_0009679)                                                                                                                   |
| `TC:1.A.38.-.-` |              1 | [GO:0015176](http://purl.obolibrary.org/obo/GO_0015176)                                                                                                                   |
| `TC:1.B.1.-.-`  |              1 | [GO:0015288](http://purl.obolibrary.org/obo/GO_0015288)                                                                                                                   |
| `TC:2.A.1.14.-` |              1 | [GO:0015296](http://purl.obolibrary.org/obo/GO_0015296)                                                                                                                   |
| `TC:2.A.1.2.-`  |              1 | [GO:0015307](http://purl.obolibrary.org/obo/GO_0015307)                                                                                                                   |
| `TC:2.A.1.3.-`  |              1 | [GO:0015307](http://purl.obolibrary.org/obo/GO_0015307)                                                                                                                   |
| `TC:2.A.1.4.-`  |              1 | [GO:0015315](http://purl.obolibrary.org/obo/GO_0015315)                                                                                                                   |
| `TC:2.A.1.9.-`  |              1 | [GO:0015317](http://purl.obolibrary.org/obo/GO_0015317)                                                                                                                   |
| `TC:2.A.17.-.-` |              1 | [GO:0015333](http://purl.obolibrary.org/obo/GO_0015333)                                                                                                                   |
| `TC:2.A.5.-.-`  |              1 | [GO:0015342](http://purl.obolibrary.org/obo/GO_0015342)                                                                                                                   |
| `TC:2.A.19.-.-` |              1 | [GO:0015368](http://purl.obolibrary.org/obo/GO_0015368)                                                                                                                   |
| `TC:2.A.19.2.-` |              1 | [GO:0015369](http://purl.obolibrary.org/obo/GO_0015369)                                                                                                                   |
| `TC:2.A.21.5.-` |              1 | [GO:0015373](http://purl.obolibrary.org/obo/GO_0015373)                                                                                                                   |
| `TC:2.A.30.4.-` |              1 | [GO:0015378](http://purl.obolibrary.org/obo/GO_0015378)                                                                                                                   |
| `TC:2.A.36.-.-` |              1 | [GO:0015385](http://purl.obolibrary.org/obo/GO_0015385)                                                                                                                   |
| `TC:2.A.37.-.-` |              1 | [GO:0015386](http://purl.obolibrary.org/obo/GO_0015386)                                                                                                                   |
| `TC:2.A.38.-.-` |              1 | [GO:0015387](http://purl.obolibrary.org/obo/GO_0015387)                                                                                                                   |
| `TC:3.A.2.-.-`  |              1 | [GO:0015442](http://purl.obolibrary.org/obo/GO_0015442)                                                                                                                   |
| `TC:3.B.-.-.-`  |              1 | [GO:0015451](http://purl.obolibrary.org/obo/GO_0015451)                                                                                                                   |
| `TC:3.C.-.-.-`  |              1 | [GO:0015452](http://purl.obolibrary.org/obo/GO_0015452)                                                                                                                   |
| `TC:3.D.-.-.-`  |              1 | [GO:0015453](http://purl.obolibrary.org/obo/GO_0015453)                                                                                                                   |
| `TC:1.C.1.-.-`  |              1 | [GO:0015468](http://purl.obolibrary.org/obo/GO_0015468)                                                                                                                   |
| `TC:1.B.11.-.-` |              1 | [GO:0015473](http://purl.obolibrary.org/obo/GO_0015473)                                                                                                                   |
| `TC:1.B.12.-.-` |              1 | [GO:0015474](http://purl.obolibrary.org/obo/GO_0015474)                                                                                                                   |
| `TC:1.B.13.-.-` |              1 | [GO:0015477](http://purl.obolibrary.org/obo/GO_0015477)                                                                                                                   |
| `TC:1.B.22.-.-` |              1 | [GO:0015480](http://purl.obolibrary.org/obo/GO_0015480)                                                                                                                   |

## `TO`: Plant Trait Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `TO` (standardized to Bioregistry
prefix [`to`](https://bioregistry.io/to)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                   |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------|
| `TO:TO`         |              2 | [PATO:0001540](http://purl.obolibrary.org/obo/PATO_0001540), [PATO:0001541](http://purl.obolibrary.org/obo/PATO_0001541) |

## `UBERON`: Uber Anatomy Ontology

Overall, there were 215 invalid
xrefs to external prefixed with `UBERON` (standardized to Bioregistry
prefix [`uberon`](https://bioregistry.io/uberon)) that
did not match the standard pattern `^\d+$`.

| external_xref                |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UBERON:cjm`                 |            174 | [BSPO:0000126](http://purl.obolibrary.org/obo/BSPO_0000126), [UBERON:0000004](http://purl.obolibrary.org/obo/UBERON_0000004), [UBERON:0000004](http://purl.obolibrary.org/obo/UBERON_0000004), [UBERON:0000012](http://purl.obolibrary.org/obo/UBERON_0000012), [UBERON:0000172](http://purl.obolibrary.org/obo/UBERON_0000172), ...     |
| `UBERON:EJS`                 |             19 | [UBERON:1000000](http://purl.obolibrary.org/obo/UBERON_1000000), [UBERON:1000001](http://purl.obolibrary.org/obo/UBERON_1000001), [UBERON:1000002](http://purl.obolibrary.org/obo/UBERON_1000002), [UBERON:1000004](http://purl.obolibrary.org/obo/UBERON_1000004), [UBERON:1000005](http://purl.obolibrary.org/obo/UBERON_1000005), ... |
| `UBERON:mah`                 |              4 | [UBERON:0001427](http://purl.obolibrary.org/obo/UBERON_0001427), [UBERON:0001428](http://purl.obolibrary.org/obo/UBERON_0001428), [UBERON:0015001](http://purl.obolibrary.org/obo/UBERON_0015001), [UBERON:0015003](http://purl.obolibrary.org/obo/UBERON_0015003)                                                                       |
| `UBERON:skansa`              |              4 | [UBERON:0012288](http://purl.obolibrary.org/obo/UBERON_0012288), [UBERON:0012289](http://purl.obolibrary.org/obo/UBERON_0012289), [UBERON:0012290](http://purl.obolibrary.org/obo/UBERON_0012290), [UBERON:0013649](http://purl.obolibrary.org/obo/UBERON_0013649)                                                                       |
| `UBERON:xp`                  |              3 | [UBERON:0003133](http://purl.obolibrary.org/obo/UBERON_0003133), [UBERON:0003134](http://purl.obolibrary.org/obo/UBERON_0003134), [UBERON:0003135](http://purl.obolibrary.org/obo/UBERON_0003135)                                                                                                                                        |
| `UBERON:automatic`           |              2 | [UBERON:0004766](http://purl.obolibrary.org/obo/UBERON_0004766), [UBERON:0004766](http://purl.obolibrary.org/obo/UBERON_0004766)                                                                                                                                                                                                         |
| `UBERON:gg`                  |              2 | [UBERON:0005982](http://purl.obolibrary.org/obo/UBERON_0005982), [UBERON:0006060](http://purl.obolibrary.org/obo/UBERON_0006060)                                                                                                                                                                                                         |
| `UBERON:md`                  |              2 | [UBERON:0013739](http://purl.obolibrary.org/obo/UBERON_0013739), [UBERON:0013740](http://purl.obolibrary.org/obo/UBERON_0013740)                                                                                                                                                                                                         |
| `UBERON:gvg`                 |              1 | [UBERON:0005273](http://purl.obolibrary.org/obo/UBERON_0005273)                                                                                                                                                                                                                                                                          |
| `UBERON:CL_meeting_20110725` |              1 | [UBERON:0008921](http://purl.obolibrary.org/obo/UBERON_0008921)                                                                                                                                                                                                                                                                          |
| `UBERON:nv`                  |              1 | [UBERON:0016928](http://purl.obolibrary.org/obo/UBERON_0016928)                                                                                                                                                                                                                                                                          |
| `UBERON:drseb`               |              1 | [UBERON:0019207](http://purl.obolibrary.org/obo/UBERON_0019207)                                                                                                                                                                                                                                                                          |
| `UBERON:rc`                  |              1 | [UBERON:0036015](http://purl.obolibrary.org/obo/UBERON_0036015)                                                                                                                                                                                                                                                                          |

## `UM-BBD_pathwayID`: EAWAG Biocatalysis/Biodegradation Database

Overall, there were 4 invalid
xrefs to external prefixed with `UM-BBD_pathwayID` (standardized to Bioregistry
prefix [`umbbd.pathway`](https://bioregistry.io/umbbd.pathway)) that
did not match the standard pattern `^\w+$`.

| external_xref              |   usages_count | usages                                                                                                           |
|----------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `UM-BBD_pathwayID:2,4,5-t` |              2 | [GO:0018980](http://purl.obolibrary.org/obo/GO_0018980), [GO:0018980](http://purl.obolibrary.org/obo/GO_0018980) |
| `UM-BBD_pathwayID:2,4d`    |              1 | [GO:0018901](http://purl.obolibrary.org/obo/GO_0018901)                                                          |
| `UM-BBD_pathwayID:2,4-d`   |              1 | [GO:0018901](http://purl.obolibrary.org/obo/GO_0018901)                                                          |

## `UM-BBD_reactionID`: EAWAG Biocatalysis/Biodegradation Database

Overall, there were 2 invalid
xrefs to external prefixed with `UM-BBD_reactionID` (standardized to Bioregistry
prefix [`umbbd.reaction`](https://bioregistry.io/umbbd.reaction)) that
did not match the standard pattern `^r\d+$`.

| external_xref            |   usages_count | usages                                                  |
|--------------------------|----------------|---------------------------------------------------------|
| `UM-BBD_reactionID:0129` |              1 | [GO:0018783](http://purl.obolibrary.org/obo/GO_0018783) |
| `UM-BBD_reactionID:1137` |              1 | [GO:0034813](http://purl.obolibrary.org/obo/GO_0034813) |

## `UniProt`: UniProt Protein

Overall, there were 21 invalid
xrefs to external prefixed with `UniProt` (standardized to Bioregistry
prefix [`uniprot`](https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref             |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|---------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UniProt:curation_manual` |             19 | [SO:0001064](http://purl.obolibrary.org/obo/SO_0001064), [SO:0001066](http://purl.obolibrary.org/obo/SO_0001066), [SO:0001067](http://purl.obolibrary.org/obo/SO_0001067), [SO:0001080](http://purl.obolibrary.org/obo/SO_0001080), [SO:0001083](http://purl.obolibrary.org/obo/SO_0001083), ... |
| `UniProt:curator_manual`  |              1 | [SO:0001077](http://purl.obolibrary.org/obo/SO_0001077)                                                                                                                                                                                                                                          |
| `UniProt:Curation_manual` |              1 | [SO:0001093](http://purl.obolibrary.org/obo/SO_0001093)                                                                                                                                                                                                                                          |

## `uniprot`: UniProt Protein

Overall, there were 31 invalid
xrefs to external prefixed with `uniprot` (standardized to Bioregistry
prefix [`uniprot`](https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref          |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uniprot:feature_type` |             28 | [SO:0000417](http://purl.obolibrary.org/obo/SO_0000417), [SO:0000418](http://purl.obolibrary.org/obo/SO_0000418), [SO:0000419](http://purl.obolibrary.org/obo/SO_0000419), [SO:0000691](http://purl.obolibrary.org/obo/SO_0000691), [SO:0000725](http://purl.obolibrary.org/obo/SO_0000725), ... |
| `uniprot:feature`      |              2 | [SO:0001655](http://purl.obolibrary.org/obo/SO_0001655), [SO:0100020](http://purl.obolibrary.org/obo/SO_0100020)                                                                                                                                                                                 |
| `uniprot:curation`     |              1 | [SO:0001091](http://purl.obolibrary.org/obo/SO_0001091)                                                                                                                                                                                                                                          |

## `UniProtKB`: UniProt Protein

Overall, there were 477 invalid
xrefs to external prefixed with `UniProtKB` (standardized to Bioregistry
prefix [`uniprot`](https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref         |   usages_count | usages                                                      |
|-----------------------|----------------|-------------------------------------------------------------|
| `UniProtKB:Q9EQR3-1`  |              1 | [PR:000000761](http://purl.obolibrary.org/obo/PR_000000761) |
| `UniProtKB:Q8CIG3-1`  |              1 | [PR:000003321](http://purl.obolibrary.org/obo/PR_000003321) |
| `UniProtKB:O08599-1`  |              1 | [PR:000003322](http://purl.obolibrary.org/obo/PR_000003322) |
| `UniProtKB:O08599-2`  |              1 | [PR:000003323](http://purl.obolibrary.org/obo/PR_000003323) |
| `UniProtKB:Q9Z0P7-1`  |              1 | [PR:000003325](http://purl.obolibrary.org/obo/PR_000003325) |
| `UniProtKB:Q9Z0P7-3`  |              1 | [PR:000003326](http://purl.obolibrary.org/obo/PR_000003326) |
| `UniProtKB:Q9Z0P7-4`  |              1 | [PR:000003327](http://purl.obolibrary.org/obo/PR_000003327) |
| `UniProtKB:P46734-1`  |              1 | [PR:000021942](http://purl.obolibrary.org/obo/PR_000021942) |
| `UniProtKB:P08152-2`  |              1 | [PR:000022018](http://purl.obolibrary.org/obo/PR_000022018) |
| `UniProtKB:Q9D6R2-1`  |              1 | [PR:000025355](http://purl.obolibrary.org/obo/PR_000025355) |
| `UniProtKB:Q9D6R2-2`  |              1 | [PR:000025356](http://purl.obolibrary.org/obo/PR_000025356) |
| `UniProtKB:Q0QWG9-1`  |              1 | [PR:000025481](http://purl.obolibrary.org/obo/PR_000025481) |
| `UniProtKB:Q0QWG9-2`  |              1 | [PR:000025483](http://purl.obolibrary.org/obo/PR_000025483) |
| `UniProtKB:P40336-1`  |              1 | [PR:000025486](http://purl.obolibrary.org/obo/PR_000025486) |
| `UniProtKB:Q8C460-1`  |              1 | [PR:000025501](http://purl.obolibrary.org/obo/PR_000025501) |
| `UniProtKB:Q8C460-2`  |              1 | [PR:000025503](http://purl.obolibrary.org/obo/PR_000025503) |
| `UniProtKB:Q8C460-3`  |              1 | [PR:000025505](http://purl.obolibrary.org/obo/PR_000025505) |
| `UniProtKB:O88935-2`  |              1 | [PR:000025508](http://purl.obolibrary.org/obo/PR_000025508) |
| `UniProtKB:O88935-1`  |              1 | [PR:000025510](http://purl.obolibrary.org/obo/PR_000025510) |
| `UniProtKB:P17600-2`  |              1 | [PR:000025511](http://purl.obolibrary.org/obo/PR_000025511) |
| `UniProtKB:P17600-1`  |              1 | [PR:000025512](http://purl.obolibrary.org/obo/PR_000025512) |
| `UniProtKB:P17948-1`  |              1 | [PR:000025516](http://purl.obolibrary.org/obo/PR_000025516) |
| `UniProtKB:P35969-1`  |              1 | [PR:000025517](http://purl.obolibrary.org/obo/PR_000025517) |
| `UniProtKB:P17948-2`  |              1 | [PR:000025518](http://purl.obolibrary.org/obo/PR_000025518) |
| `UniProtKB:P05067-1`  |              1 | [PR:000025534](http://purl.obolibrary.org/obo/PR_000025534) |
| `UniProtKB:P05067-2`  |              1 | [PR:000025535](http://purl.obolibrary.org/obo/PR_000025535) |
| `UniProtKB:P05067-3`  |              1 | [PR:000025536](http://purl.obolibrary.org/obo/PR_000025536) |
| `UniProtKB:P05067-4`  |              1 | [PR:000025537](http://purl.obolibrary.org/obo/PR_000025537) |
| `UniProtKB:P05067-5`  |              1 | [PR:000025538](http://purl.obolibrary.org/obo/PR_000025538) |
| `UniProtKB:P05067-6`  |              1 | [PR:000025539](http://purl.obolibrary.org/obo/PR_000025539) |
| `UniProtKB:P05067-7`  |              1 | [PR:000025540](http://purl.obolibrary.org/obo/PR_000025540) |
| `UniProtKB:P05067-8`  |              1 | [PR:000025541](http://purl.obolibrary.org/obo/PR_000025541) |
| `UniProtKB:P05067-9`  |              1 | [PR:000025542](http://purl.obolibrary.org/obo/PR_000025542) |
| `UniProtKB:P05067-10` |              1 | [PR:000025543](http://purl.obolibrary.org/obo/PR_000025543) |
| `UniProtKB:P12023-1`  |              1 | [PR:000025544](http://purl.obolibrary.org/obo/PR_000025544) |
| `UniProtKB:P12023-2`  |              1 | [PR:000025545](http://purl.obolibrary.org/obo/PR_000025545) |
| `UniProtKB:P12023-3`  |              1 | [PR:000025546](http://purl.obolibrary.org/obo/PR_000025546) |
| `UniProtKB:P12023-4`  |              1 | [PR:000025547](http://purl.obolibrary.org/obo/PR_000025547) |
| `UniProtKB:Q9H204-1`  |              1 | [PR:000025632](http://purl.obolibrary.org/obo/PR_000025632) |
| `UniProtKB:Q69ZI1-1`  |              1 | [PR:000025640](http://purl.obolibrary.org/obo/PR_000025640) |
| `UniProtKB:Q920M9-1`  |              1 | [PR:000025643](http://purl.obolibrary.org/obo/PR_000025643) |
| `UniProtKB:P07737-1`  |              1 | [PR:000025645](http://purl.obolibrary.org/obo/PR_000025645) |
| `UniProtKB:P01584-1`  |              1 | [PR:000025647](http://purl.obolibrary.org/obo/PR_000025647) |
| `UniProtKB:P04040-1`  |              1 | [PR:000025649](http://purl.obolibrary.org/obo/PR_000025649) |
| `UniProtKB:P13987-1`  |              1 | [PR:000025651](http://purl.obolibrary.org/obo/PR_000025651) |
| `UniProtKB:P06702-1`  |              1 | [PR:000025653](http://purl.obolibrary.org/obo/PR_000025653) |
| `UniProtKB:Q08380-1`  |              1 | [PR:000025655](http://purl.obolibrary.org/obo/PR_000025655) |
| `UniProtKB:P00915-1`  |              1 | [PR:000025657](http://purl.obolibrary.org/obo/PR_000025657) |
| `UniProtKB:P61769-1`  |              1 | [PR:000025660](http://purl.obolibrary.org/obo/PR_000025660) |
| `UniProtKB:Q03142-1`  |              1 | [PR:000025674](http://purl.obolibrary.org/obo/PR_000025674) |
| `UniProtKB:Q03142-2`  |              1 | [PR:000025675](http://purl.obolibrary.org/obo/PR_000025675) |
| `UniProtKB:Q91V87-1`  |              1 | [PR:000025682](http://purl.obolibrary.org/obo/PR_000025682) |
| `UniProtKB:Q91V87-2`  |              1 | [PR:000025683](http://purl.obolibrary.org/obo/PR_000025683) |
| `UniProtKB:Q7TQM3-1`  |              1 | [PR:000025684](http://purl.obolibrary.org/obo/PR_000025684) |
| `UniProtKB:Q8N441-1`  |              1 | [PR:000025686](http://purl.obolibrary.org/obo/PR_000025686) |
| `UniProtKB:P16092-1`  |              1 | [PR:000025690](http://purl.obolibrary.org/obo/PR_000025690) |
| `UniProtKB:P16092-2`  |              1 | [PR:000025691](http://purl.obolibrary.org/obo/PR_000025691) |
| `UniProtKB:P16092-3`  |              1 | [PR:000025692](http://purl.obolibrary.org/obo/PR_000025692) |
| `UniProtKB:P11362-1`  |              1 | [PR:000025693](http://purl.obolibrary.org/obo/PR_000025693) |
| `UniProtKB:P11362-3`  |              1 | [PR:000025694](http://purl.obolibrary.org/obo/PR_000025694) |
| `UniProtKB:P21803-1`  |              1 | [PR:000025697](http://purl.obolibrary.org/obo/PR_000025697) |
| `UniProtKB:P21803-2`  |              1 | [PR:000025698](http://purl.obolibrary.org/obo/PR_000025698) |
| `UniProtKB:P21802-1`  |              1 | [PR:000025699](http://purl.obolibrary.org/obo/PR_000025699) |
| `UniProtKB:Q61851-1`  |              1 | [PR:000025702](http://purl.obolibrary.org/obo/PR_000025702) |
| `UniProtKB:Q61851-2`  |              1 | [PR:000025703](http://purl.obolibrary.org/obo/PR_000025703) |
| `UniProtKB:Q00613-1`  |              1 | [PR:000025718](http://purl.obolibrary.org/obo/PR_000025718) |
| `UniProtKB:Q00613-2`  |              1 | [PR:000025720](http://purl.obolibrary.org/obo/PR_000025720) |
| `UniProtKB:P38532-1`  |              1 | [PR:000025721](http://purl.obolibrary.org/obo/PR_000025721) |
| `UniProtKB:P38060-1`  |              1 | [PR:000025733](http://purl.obolibrary.org/obo/PR_000025733) |
| `UniProtKB:P35914-1`  |              1 | [PR:000025734](http://purl.obolibrary.org/obo/PR_000025734) |
| `UniProtKB:Q9JHI5-1`  |              1 | [PR:000025739](http://purl.obolibrary.org/obo/PR_000025739) |
| `UniProtKB:P26440-1`  |              1 | [PR:000025740](http://purl.obolibrary.org/obo/PR_000025740) |
| `UniProtKB:P97807-1`  |              1 | [PR:000025755](http://purl.obolibrary.org/obo/PR_000025755) |
| `UniProtKB:P07954-1`  |              1 | [PR:000025756](http://purl.obolibrary.org/obo/PR_000025756) |
| `UniProtKB:P97807-2`  |              1 | [PR:000025758](http://purl.obolibrary.org/obo/PR_000025758) |
| `UniProtKB:P07954-2`  |              1 | [PR:000025759](http://purl.obolibrary.org/obo/PR_000025759) |
| `UniProtKB:P22366-1`  |              1 | [PR:000025766](http://purl.obolibrary.org/obo/PR_000025766) |
| `UniProtKB:P22366-2`  |              1 | [PR:000025767](http://purl.obolibrary.org/obo/PR_000025767) |
| `UniProtKB:Q99836-1`  |              1 | [PR:000025768](http://purl.obolibrary.org/obo/PR_000025768) |
| `UniProtKB:Q99836-2`  |              1 | [PR:000025769](http://purl.obolibrary.org/obo/PR_000025769) |
| `UniProtKB:O35625-1`  |              1 | [PR:000025827](http://purl.obolibrary.org/obo/PR_000025827) |
| `UniProtKB:O15169-1`  |              1 | [PR:000025828](http://purl.obolibrary.org/obo/PR_000025828) |
| `UniProtKB:O35625-2`  |              1 | [PR:000025829](http://purl.obolibrary.org/obo/PR_000025829) |
| `UniProtKB:O15169-2`  |              1 | [PR:000025830](http://purl.obolibrary.org/obo/PR_000025830) |
| `UniProtKB:O70239-1`  |              1 | [PR:000025831](http://purl.obolibrary.org/obo/PR_000025831) |
| `UniProtKB:Q60739-2`  |              1 | [PR:000025859](http://purl.obolibrary.org/obo/PR_000025859) |
| `UniProtKB:Q99933-4`  |              1 | [PR:000025860](http://purl.obolibrary.org/obo/PR_000025860) |
| `UniProtKB:Q99933-1`  |              1 | [PR:000025861](http://purl.obolibrary.org/obo/PR_000025861) |
| `UniProtKB:Q60739-1`  |              1 | [PR:000025862](http://purl.obolibrary.org/obo/PR_000025862) |
| `UniProtKB:Q99933-3`  |              1 | [PR:000025863](http://purl.obolibrary.org/obo/PR_000025863) |
| `UniProtKB:Q99933-2`  |              1 | [PR:000025864](http://purl.obolibrary.org/obo/PR_000025864) |
| `UniProtKB:Q13485-1`  |              1 | [PR:000025939](http://purl.obolibrary.org/obo/PR_000025939) |
| `UniProtKB:P97471-1`  |              1 | [PR:000025941](http://purl.obolibrary.org/obo/PR_000025941) |
| `UniProtKB:P12755-1`  |              1 | [PR:000025949](http://purl.obolibrary.org/obo/PR_000025949) |
| `UniProtKB:Q08048-1`  |              1 | [PR:000025994](http://purl.obolibrary.org/obo/PR_000025994) |
| `UniProtKB:Q08048-2`  |              1 | [PR:000025996](http://purl.obolibrary.org/obo/PR_000025996) |
| `UniProtKB:O88587-1`  |              1 | [PR:000025998](http://purl.obolibrary.org/obo/PR_000025998) |
| `UniProtKB:O88587-2`  |              1 | [PR:000026000](http://purl.obolibrary.org/obo/PR_000026000) |
| `UniProtKB:P23804-1`  |              1 | [PR:000026002](http://purl.obolibrary.org/obo/PR_000026002) |
| `UniProtKB:P23804-2`  |              1 | [PR:000026004](http://purl.obolibrary.org/obo/PR_000026004) |
| `UniProtKB:P97287-1`  |              1 | [PR:000026006](http://purl.obolibrary.org/obo/PR_000026006) |
| `UniProtKB:Q60636-1`  |              1 | [PR:000026010](http://purl.obolibrary.org/obo/PR_000026010) |
| `UniProtKB:Q60636-2`  |              1 | [PR:000026011](http://purl.obolibrary.org/obo/PR_000026011) |
| `UniProtKB:Q99583-1`  |              1 | [PR:000026029](http://purl.obolibrary.org/obo/PR_000026029) |
| `UniProtKB:A2AWL7-1`  |              1 | [PR:000026043](http://purl.obolibrary.org/obo/PR_000026043) |
| `UniProtKB:Q8IWI9-1`  |              1 | [PR:000026044](http://purl.obolibrary.org/obo/PR_000026044) |
| `UniProtKB:P01106-1`  |              1 | [PR:000026047](http://purl.obolibrary.org/obo/PR_000026047) |
| `UniProtKB:P01108-1`  |              1 | [PR:000026048](http://purl.obolibrary.org/obo/PR_000026048) |
| `UniProtKB:P01106-2`  |              1 | [PR:000026049](http://purl.obolibrary.org/obo/PR_000026049) |
| `UniProtKB:Q9Z2D6-1`  |              1 | [PR:000026058](http://purl.obolibrary.org/obo/PR_000026058) |
| `UniProtKB:Q9Z2D6-2`  |              1 | [PR:000026060](http://purl.obolibrary.org/obo/PR_000026060) |
| `UniProtKB:P51608-2`  |              1 | [PR:000026061](http://purl.obolibrary.org/obo/PR_000026061) |
| `UniProtKB:Q00566-2`  |              1 | [PR:000026062](http://purl.obolibrary.org/obo/PR_000026062) |
| `UniProtKB:P51608-1`  |              1 | [PR:000026063](http://purl.obolibrary.org/obo/PR_000026063) |
| `UniProtKB:Q00566-1`  |              1 | [PR:000026064](http://purl.obolibrary.org/obo/PR_000026064) |
| `UniProtKB:Q58A65-1`  |              1 | [PR:000026066](http://purl.obolibrary.org/obo/PR_000026066) |
| `UniProtKB:O60271-1`  |              1 | [PR:000026067](http://purl.obolibrary.org/obo/PR_000026067) |
| `UniProtKB:Q58A65-2`  |              1 | [PR:000026069](http://purl.obolibrary.org/obo/PR_000026069) |
| `UniProtKB:O60271-4`  |              1 | [PR:000026070](http://purl.obolibrary.org/obo/PR_000026070) |
| `UniProtKB:P11416-1`  |              1 | [PR:000026074](http://purl.obolibrary.org/obo/PR_000026074) |
| `UniProtKB:P10276-1`  |              1 | [PR:000026075](http://purl.obolibrary.org/obo/PR_000026075) |
| `UniProtKB:Q13324-1`  |              1 | [PR:000026080](http://purl.obolibrary.org/obo/PR_000026080) |
| `UniProtKB:Q13324-2`  |              1 | [PR:000026082](http://purl.obolibrary.org/obo/PR_000026082) |
| `UniProtKB:Q13324-3`  |              1 | [PR:000026084](http://purl.obolibrary.org/obo/PR_000026084) |
| `UniProtKB:Q60748-1`  |              1 | [PR:000026085](http://purl.obolibrary.org/obo/PR_000026085) |
| `UniProtKB:Q60715-1`  |              1 | [PR:000026094](http://purl.obolibrary.org/obo/PR_000026094) |
| `UniProtKB:P13674-1`  |              1 | [PR:000026095](http://purl.obolibrary.org/obo/PR_000026095) |
| `UniProtKB:Q60715-2`  |              1 | [PR:000026097](http://purl.obolibrary.org/obo/PR_000026097) |
| `UniProtKB:P13674-2`  |              1 | [PR:000026098](http://purl.obolibrary.org/obo/PR_000026098) |
| `UniProtKB:Q60716-1`  |              1 | [PR:000026100](http://purl.obolibrary.org/obo/PR_000026100) |
| `UniProtKB:Q60716-2`  |              1 | [PR:000026102](http://purl.obolibrary.org/obo/PR_000026102) |
| `UniProtKB:Q6W3F0-1`  |              1 | [PR:000026104](http://purl.obolibrary.org/obo/PR_000026104) |
| `UniProtKB:Q96RQ3-1`  |              1 | [PR:000026115](http://purl.obolibrary.org/obo/PR_000026115) |
| `UniProtKB:Q99MR8-1`  |              1 | [PR:000026116](http://purl.obolibrary.org/obo/PR_000026116) |
| `UniProtKB:Q93UV0-1`  |              1 | [PR:000026129](http://purl.obolibrary.org/obo/PR_000026129) |
| `UniProtKB:A5VD79-1`  |              1 | [PR:000026131](http://purl.obolibrary.org/obo/PR_000026131) |
| `UniProtKB:A7BFV6-1`  |              1 | [PR:000026168](http://purl.obolibrary.org/obo/PR_000026168) |
| `UniProtKB:P00742-1`  |              1 | [PR:000026171](http://purl.obolibrary.org/obo/PR_000026171) |
| `UniProtKB:P04070-1`  |              1 | [PR:000026176](http://purl.obolibrary.org/obo/PR_000026176) |
| `UniProtKB:P11216-1`  |              1 | [PR:000026184](http://purl.obolibrary.org/obo/PR_000026184) |
| `UniProtKB:P22681-1`  |              1 | [PR:000026187](http://purl.obolibrary.org/obo/PR_000026187) |
| `UniProtKB:P32004-1`  |              1 | [PR:000026191](http://purl.obolibrary.org/obo/PR_000026191) |
| `UniProtKB:Q02750-1`  |              1 | [PR:000026195](http://purl.obolibrary.org/obo/PR_000026195) |
| `UniProtKB:Q05397-1`  |              1 | [PR:000026198](http://purl.obolibrary.org/obo/PR_000026198) |
| `UniProtKB:Q13315-1`  |              1 | [PR:000026202](http://purl.obolibrary.org/obo/PR_000026202) |
| `UniProtKB:Q13541-1`  |              1 | [PR:000026205](http://purl.obolibrary.org/obo/PR_000026205) |
| `UniProtKB:Q8WU20-1`  |              1 | [PR:000026208](http://purl.obolibrary.org/obo/PR_000026208) |
| `UniProtKB:Q5SS91-1`  |              1 | [PR:000026232](http://purl.obolibrary.org/obo/PR_000026232) |
| `UniProtKB:Q5SS91-2`  |              1 | [PR:000026235](http://purl.obolibrary.org/obo/PR_000026235) |
| `UniProtKB:Q99L45-1`  |              1 | [PR:000026237](http://purl.obolibrary.org/obo/PR_000026237) |
| `UniProtKB:Q6ZWX6-1`  |              1 | [PR:000026239](http://purl.obolibrary.org/obo/PR_000026239) |
| `UniProtKB:P20042-1`  |              1 | [PR:000026240](http://purl.obolibrary.org/obo/PR_000026240) |
| `UniProtKB:P05198-1`  |              1 | [PR:000026241](http://purl.obolibrary.org/obo/PR_000026241) |
| `UniProtKB:Q8TAQ9-1`  |              1 | [PR:000026242](http://purl.obolibrary.org/obo/PR_000026242) |
| `UniProtKB:P53805-1`  |              1 | [PR:000026244](http://purl.obolibrary.org/obo/PR_000026244) |
| `UniProtKB:P53805-2`  |              1 | [PR:000026246](http://purl.obolibrary.org/obo/PR_000026246) |
| `UniProtKB:P51636-1`  |              1 | [PR:000026248](http://purl.obolibrary.org/obo/PR_000026248) |
| `UniProtKB:P51636-2`  |              1 | [PR:000026250](http://purl.obolibrary.org/obo/PR_000026250) |
| `UniProtKB:P51636-3`  |              1 | [PR:000026252](http://purl.obolibrary.org/obo/PR_000026252) |
| `UniProtKB:Q06547-1`  |              1 | [PR:000026254](http://purl.obolibrary.org/obo/PR_000026254) |
| `UniProtKB:Q06547-2`  |              1 | [PR:000026256](http://purl.obolibrary.org/obo/PR_000026256) |
| `UniProtKB:Q06190-1`  |              1 | [PR:000026258](http://purl.obolibrary.org/obo/PR_000026258) |
| `UniProtKB:Q06190-2`  |              1 | [PR:000026260](http://purl.obolibrary.org/obo/PR_000026260) |
| `UniProtKB:Q06710-1`  |              1 | [PR:000026262](http://purl.obolibrary.org/obo/PR_000026262) |
| `UniProtKB:Q06710-2`  |              1 | [PR:000026264](http://purl.obolibrary.org/obo/PR_000026264) |
| `UniProtKB:Q06710-3`  |              1 | [PR:000026266](http://purl.obolibrary.org/obo/PR_000026266) |
| `UniProtKB:Q06710-4`  |              1 | [PR:000026268](http://purl.obolibrary.org/obo/PR_000026268) |
| `UniProtKB:Q16637-1`  |              1 | [PR:000026271](http://purl.obolibrary.org/obo/PR_000026271) |
| `UniProtKB:Q16637-2`  |              1 | [PR:000026274](http://purl.obolibrary.org/obo/PR_000026274) |
| `UniProtKB:Q16637-3`  |              1 | [PR:000026277](http://purl.obolibrary.org/obo/PR_000026277) |
| `UniProtKB:O15392-1`  |              1 | [PR:000026279](http://purl.obolibrary.org/obo/PR_000026279) |
| `UniProtKB:O15392-2`  |              1 | [PR:000026281](http://purl.obolibrary.org/obo/PR_000026281) |
| `UniProtKB:Q9CYB0-1`  |              1 | [PR:000026298](http://purl.obolibrary.org/obo/PR_000026298) |
| `UniProtKB:O60858-1`  |              1 | [PR:000026299](http://purl.obolibrary.org/obo/PR_000026299) |
| `UniProtKB:Q8WV44-1`  |              1 | [PR:000026302](http://purl.obolibrary.org/obo/PR_000026302) |
| `UniProtKB:Q5NCC3-1`  |              1 | [PR:000026303](http://purl.obolibrary.org/obo/PR_000026303) |
| `UniProtKB:Q8WV44-2`  |              1 | [PR:000026305](http://purl.obolibrary.org/obo/PR_000026305) |
| `UniProtKB:Q8WWW0-1`  |              1 | [PR:000026307](http://purl.obolibrary.org/obo/PR_000026307) |
| `UniProtKB:Q8WWW0-2`  |              1 | [PR:000026309](http://purl.obolibrary.org/obo/PR_000026309) |
| `UniProtKB:Q5SXI5-1`  |              1 | [PR:000026311](http://purl.obolibrary.org/obo/PR_000026311) |
| `UniProtKB:Q5SXI5-2`  |              1 | [PR:000026313](http://purl.obolibrary.org/obo/PR_000026313) |
| `UniProtKB:Q96IT1-1`  |              1 | [PR:000026314](http://purl.obolibrary.org/obo/PR_000026314) |
| `UniProtKB:Q5SXI5-3`  |              1 | [PR:000026316](http://purl.obolibrary.org/obo/PR_000026316) |
| `UniProtKB:P34152-3`  |              1 | [PR:000026317](http://purl.obolibrary.org/obo/PR_000026317) |
| `UniProtKB:P21550-1`  |              1 | [PR:000026319](http://purl.obolibrary.org/obo/PR_000026319) |
| `UniProtKB:Q8C042-1`  |              1 | [PR:000026322](http://purl.obolibrary.org/obo/PR_000026322) |
| `UniProtKB:Q8C042-2`  |              1 | [PR:000026324](http://purl.obolibrary.org/obo/PR_000026324) |
| `UniProtKB:P17183-1`  |              1 | [PR:000026326](http://purl.obolibrary.org/obo/PR_000026326) |
| `UniProtKB:P13929-1`  |              1 | [PR:000026329](http://purl.obolibrary.org/obo/PR_000026329) |
| `UniProtKB:P09104-1`  |              1 | [PR:000026332](http://purl.obolibrary.org/obo/PR_000026332) |
| `UniProtKB:P17182-1`  |              1 | [PR:000026349](http://purl.obolibrary.org/obo/PR_000026349) |
| `UniProtKB:Q14BU0-1`  |              1 | [PR:000026351](http://purl.obolibrary.org/obo/PR_000026351) |
| `UniProtKB:Q14BU0-2`  |              1 | [PR:000026353](http://purl.obolibrary.org/obo/PR_000026353) |
| `UniProtKB:P06733-1`  |              1 | [PR:000026354](http://purl.obolibrary.org/obo/PR_000026354) |
| `UniProtKB:C9W8R6-1`  |              1 | [PR:000026356](http://purl.obolibrary.org/obo/PR_000026356) |
| `UniProtKB:C9W8R7-1`  |              1 | [PR:000026358](http://purl.obolibrary.org/obo/PR_000026358) |
| `UniProtKB:P12382-1`  |              1 | [PR:000026460](http://purl.obolibrary.org/obo/PR_000026460) |
| `UniProtKB:P47857-1`  |              1 | [PR:000026464](http://purl.obolibrary.org/obo/PR_000026464) |
| `UniProtKB:Q9WUA3-1`  |              1 | [PR:000026466](http://purl.obolibrary.org/obo/PR_000026466) |
| `UniProtKB:P17858-1`  |              1 | [PR:000026471](http://purl.obolibrary.org/obo/PR_000026471) |
| `UniProtKB:P08237-1`  |              1 | [PR:000026472](http://purl.obolibrary.org/obo/PR_000026472) |
| `UniProtKB:Q01813-1`  |              1 | [PR:000026473](http://purl.obolibrary.org/obo/PR_000026473) |
| `UniProtKB:Q13164-1`  |              1 | [PR:000026478](http://purl.obolibrary.org/obo/PR_000026478) |
| `UniProtKB:Q8WXH0-1`  |              1 | [PR:000026483](http://purl.obolibrary.org/obo/PR_000026483) |
| `UniProtKB:Q8WXH0-2`  |              1 | [PR:000026485](http://purl.obolibrary.org/obo/PR_000026485) |
| `UniProtKB:Q8WXH0-3`  |              1 | [PR:000026487](http://purl.obolibrary.org/obo/PR_000026487) |
| `UniProtKB:Q8WXH0-4`  |              1 | [PR:000026489](http://purl.obolibrary.org/obo/PR_000026489) |
| `UniProtKB:Q8WXH0-5`  |              1 | [PR:000026491](http://purl.obolibrary.org/obo/PR_000026491) |
| `UniProtKB:Q96B01-1`  |              1 | [PR:000026493](http://purl.obolibrary.org/obo/PR_000026493) |
| `UniProtKB:Q96B01-2`  |              1 | [PR:000026495](http://purl.obolibrary.org/obo/PR_000026495) |
| `UniProtKB:Q96B01-3`  |              1 | [PR:000026497](http://purl.obolibrary.org/obo/PR_000026497) |
| `UniProtKB:P29590-1`  |              1 | [PR:000026498](http://purl.obolibrary.org/obo/PR_000026498) |
| `UniProtKB:Q96QF0-1`  |              1 | [PR:000026500](http://purl.obolibrary.org/obo/PR_000026500) |
| `UniProtKB:Q92900-1`  |              1 | [PR:000026503](http://purl.obolibrary.org/obo/PR_000026503) |
| `UniProtKB:Q92900-2`  |              1 | [PR:000026505](http://purl.obolibrary.org/obo/PR_000026505) |
| `UniProtKB:P40337-1`  |              1 | [PR:000026507](http://purl.obolibrary.org/obo/PR_000026507) |
| `UniProtKB:P40337-2`  |              1 | [PR:000026509](http://purl.obolibrary.org/obo/PR_000026509) |
| `UniProtKB:P40337-3`  |              1 | [PR:000026511](http://purl.obolibrary.org/obo/PR_000026511) |
| `UniProtKB:P29590-2`  |              1 | [PR:000026513](http://purl.obolibrary.org/obo/PR_000026513) |
| `UniProtKB:P29590-3`  |              1 | [PR:000026515](http://purl.obolibrary.org/obo/PR_000026515) |
| `UniProtKB:P29590-4`  |              1 | [PR:000026517](http://purl.obolibrary.org/obo/PR_000026517) |
| `UniProtKB:P29590-5`  |              1 | [PR:000026519](http://purl.obolibrary.org/obo/PR_000026519) |
| `UniProtKB:P38398-1`  |              1 | [PR:000026521](http://purl.obolibrary.org/obo/PR_000026521) |
| `UniProtKB:P38398-2`  |              1 | [PR:000026523](http://purl.obolibrary.org/obo/PR_000026523) |
| `UniProtKB:P38398-3`  |              1 | [PR:000026525](http://purl.obolibrary.org/obo/PR_000026525) |
| `UniProtKB:P38398-4`  |              1 | [PR:000026527](http://purl.obolibrary.org/obo/PR_000026527) |
| `UniProtKB:P38398-5`  |              1 | [PR:000026529](http://purl.obolibrary.org/obo/PR_000026529) |
| `UniProtKB:P40855-1`  |              1 | [PR:000026531](http://purl.obolibrary.org/obo/PR_000026531) |
| `UniProtKB:P40855-2`  |              1 | [PR:000026533](http://purl.obolibrary.org/obo/PR_000026533) |
| `UniProtKB:P40855-3`  |              1 | [PR:000026535](http://purl.obolibrary.org/obo/PR_000026535) |
| `UniProtKB:P40855-4`  |              1 | [PR:000026537](http://purl.obolibrary.org/obo/PR_000026537) |
| `UniProtKB:P02545-1`  |              1 | [PR:000026540](http://purl.obolibrary.org/obo/PR_000026540) |
| `UniProtKB:P02545-2`  |              1 | [PR:000026542](http://purl.obolibrary.org/obo/PR_000026542) |
| `UniProtKB:P35240-1`  |              1 | [PR:000026543](http://purl.obolibrary.org/obo/PR_000026543) |
| `UniProtKB:P35240-3`  |              1 | [PR:000026544](http://purl.obolibrary.org/obo/PR_000026544) |
| `UniProtKB:P35240-2`  |              1 | [PR:000026546](http://purl.obolibrary.org/obo/PR_000026546) |
| `UniProtKB:P35240-4`  |              1 | [PR:000026548](http://purl.obolibrary.org/obo/PR_000026548) |
| `UniProtKB:P78324-1`  |              1 | [PR:000026552](http://purl.obolibrary.org/obo/PR_000026552) |
| `UniProtKB:Q96QF0-2`  |              1 | [PR:000026556](http://purl.obolibrary.org/obo/PR_000026556) |
| `UniProtKB:P35710-1`  |              1 | [PR:000026779](http://purl.obolibrary.org/obo/PR_000026779) |
| `UniProtKB:P35710-2`  |              1 | [PR:000026781](http://purl.obolibrary.org/obo/PR_000026781) |
| `UniProtKB:P35710-3`  |              1 | [PR:000026783](http://purl.obolibrary.org/obo/PR_000026783) |
| `UniProtKB:P70444-1`  |              1 | [PR:000026784](http://purl.obolibrary.org/obo/PR_000026784) |
| `UniProtKB:P62993-1`  |              1 | [PR:000026788](http://purl.obolibrary.org/obo/PR_000026788) |
| `UniProtKB:Q14643-1`  |              1 | [PR:000026790](http://purl.obolibrary.org/obo/PR_000026790) |
| `UniProtKB:O14786-1`  |              1 | [PR:000026791](http://purl.obolibrary.org/obo/PR_000026791) |
| `UniProtKB:P49815-1`  |              1 | [PR:000026793](http://purl.obolibrary.org/obo/PR_000026793) |
| `UniProtKB:P60880-1`  |              1 | [PR:000026795](http://purl.obolibrary.org/obo/PR_000026795) |
| `UniProtKB:P60879-1`  |              1 | [PR:000026796](http://purl.obolibrary.org/obo/PR_000026796) |
| `UniProtKB:Q16623-1`  |              1 | [PR:000026798](http://purl.obolibrary.org/obo/PR_000026798) |
| `UniProtKB:Q16623-2`  |              1 | [PR:000026800](http://purl.obolibrary.org/obo/PR_000026800) |
| `UniProtKB:Q16623-3`  |              1 | [PR:000026802](http://purl.obolibrary.org/obo/PR_000026802) |
| `UniProtKB:Q13241-1`  |              1 | [PR:000026804](http://purl.obolibrary.org/obo/PR_000026804) |
| `UniProtKB:O54708-1`  |              1 | [PR:000026805](http://purl.obolibrary.org/obo/PR_000026805) |
| `UniProtKB:Q9CS84-1`  |              1 | [PR:000026808](http://purl.obolibrary.org/obo/PR_000026808) |
| `UniProtKB:Q9CS84-2`  |              1 | [PR:000026810](http://purl.obolibrary.org/obo/PR_000026810) |
| `UniProtKB:Q9CS84-3`  |              1 | [PR:000026812](http://purl.obolibrary.org/obo/PR_000026812) |
| `UniProtKB:Q9ULB1-2`  |              1 | [PR:000026813](http://purl.obolibrary.org/obo/PR_000026813) |
| `UniProtKB:P01138-1`  |              1 | [PR:000026815](http://purl.obolibrary.org/obo/PR_000026815) |
| `UniProtKB:Q60680-1`  |              1 | [PR:000026819](http://purl.obolibrary.org/obo/PR_000026819) |
| `UniProtKB:O15111-1`  |              1 | [PR:000026821](http://purl.obolibrary.org/obo/PR_000026821) |
| `UniProtKB:P49327-1`  |              1 | [PR:000026825](http://purl.obolibrary.org/obo/PR_000026825) |
| `UniProtKB:Q60597-1`  |              1 | [PR:000026831](http://purl.obolibrary.org/obo/PR_000026831) |
| `UniProtKB:Q60597-2`  |              1 | [PR:000026833](http://purl.obolibrary.org/obo/PR_000026833) |
| `UniProtKB:Q9D2G2-1`  |              1 | [PR:000026835](http://purl.obolibrary.org/obo/PR_000026835) |
| `UniProtKB:O08749-1`  |              1 | [PR:000026837](http://purl.obolibrary.org/obo/PR_000026837) |
| `UniProtKB:P01100-1`  |              1 | [PR:000026841](http://purl.obolibrary.org/obo/PR_000026841) |
| `UniProtKB:Q8NHY2-1`  |              1 | [PR:000026845](http://purl.obolibrary.org/obo/PR_000026845) |
| `UniProtKB:P01101-1`  |              1 | [PR:000026849](http://purl.obolibrary.org/obo/PR_000026849) |
| `UniProtKB:Q9R1A8-1`  |              1 | [PR:000026850](http://purl.obolibrary.org/obo/PR_000026850) |
| `UniProtKB:Q9Y6F6-1`  |              1 | [PR:000026853](http://purl.obolibrary.org/obo/PR_000026853) |
| `UniProtKB:P42224-1`  |              1 | [PR:000026856](http://purl.obolibrary.org/obo/PR_000026856) |
| `UniProtKB:P26715-1`  |              1 | [PR:000026860](http://purl.obolibrary.org/obo/PR_000026860) |
| `UniProtKB:Q13477-1`  |              1 | [PR:000026862](http://purl.obolibrary.org/obo/PR_000026862) |
| `UniProtKB:O43157-1`  |              1 | [PR:000026913](http://purl.obolibrary.org/obo/PR_000026913) |
| `UniProtKB:Q86YT9-1`  |              1 | [PR:000026917](http://purl.obolibrary.org/obo/PR_000026917) |
| `UniProtKB:P26010-1`  |              1 | [PR:000026921](http://purl.obolibrary.org/obo/PR_000026921) |
| `UniProtKB:Q9Y6W8-1`  |              1 | [PR:000026925](http://purl.obolibrary.org/obo/PR_000026925) |
| `UniProtKB:P25942-1`  |              1 | [PR:000026929](http://purl.obolibrary.org/obo/PR_000026929) |
| `UniProtKB:P15151-1`  |              1 | [PR:000026933](http://purl.obolibrary.org/obo/PR_000026933) |
| `UniProtKB:O60500-1`  |              1 | [PR:000026939](http://purl.obolibrary.org/obo/PR_000026939) |
| `UniProtKB:P48551-1`  |              1 | [PR:000026944](http://purl.obolibrary.org/obo/PR_000026944) |
| `UniProtKB:P48551-2`  |              1 | [PR:000026946](http://purl.obolibrary.org/obo/PR_000026946) |
| `UniProtKB:Q15223-1`  |              1 | [PR:000026952](http://purl.obolibrary.org/obo/PR_000026952) |
| `UniProtKB:Q92692-1`  |              1 | [PR:000026956](http://purl.obolibrary.org/obo/PR_000026956) |
| `UniProtKB:O88623-1`  |              1 | [PR:000026984](http://purl.obolibrary.org/obo/PR_000026984) |
| `UniProtKB:O88623-2`  |              1 | [PR:000026986](http://purl.obolibrary.org/obo/PR_000026986) |
| `UniProtKB:O88623-3`  |              1 | [PR:000026988](http://purl.obolibrary.org/obo/PR_000026988) |
| `UniProtKB:P10636-1`  |              1 | [PR:000027000](http://purl.obolibrary.org/obo/PR_000027000) |
| `UniProtKB:P10636-2`  |              1 | [PR:000027001](http://purl.obolibrary.org/obo/PR_000027001) |
| `UniProtKB:P10636-3`  |              1 | [PR:000027002](http://purl.obolibrary.org/obo/PR_000027002) |
| `UniProtKB:P10636-4`  |              1 | [PR:000027003](http://purl.obolibrary.org/obo/PR_000027003) |
| `UniProtKB:P10636-5`  |              1 | [PR:000027004](http://purl.obolibrary.org/obo/PR_000027004) |
| `UniProtKB:P10636-6`  |              1 | [PR:000027005](http://purl.obolibrary.org/obo/PR_000027005) |
| `UniProtKB:P10636-7`  |              1 | [PR:000027006](http://purl.obolibrary.org/obo/PR_000027006) |
| `UniProtKB:P10636-8`  |              1 | [PR:000027007](http://purl.obolibrary.org/obo/PR_000027007) |
| `UniProtKB:Q64323-1`  |              1 | [PR:000027010](http://purl.obolibrary.org/obo/PR_000027010) |
| `UniProtKB:Q9CXR4-1`  |              1 | [PR:000027012](http://purl.obolibrary.org/obo/PR_000027012) |
| `UniProtKB:Q5M9N4-1`  |              1 | [PR:000027014](http://purl.obolibrary.org/obo/PR_000027014) |
| `UniProtKB:Q9QYT7-1`  |              1 | [PR:000027016](http://purl.obolibrary.org/obo/PR_000027016) |
| `UniProtKB:Q9JHG1-1`  |              1 | [PR:000027018](http://purl.obolibrary.org/obo/PR_000027018) |
| `UniProtKB:Q9Z324-1`  |              1 | [PR:000027020](http://purl.obolibrary.org/obo/PR_000027020) |
| `UniProtKB:P37287-1`  |              1 | [PR:000027021](http://purl.obolibrary.org/obo/PR_000027021) |
| `UniProtKB:Q92535-1`  |              1 | [PR:000027022](http://purl.obolibrary.org/obo/PR_000027022) |
| `UniProtKB:Q14442-1`  |              1 | [PR:000027023](http://purl.obolibrary.org/obo/PR_000027023) |
| `UniProtKB:Q9BRB3-2`  |              1 | [PR:000027024](http://purl.obolibrary.org/obo/PR_000027024) |
| `UniProtKB:P57054-2`  |              1 | [PR:000027025](http://purl.obolibrary.org/obo/PR_000027025) |
| `UniProtKB:O94777-1`  |              1 | [PR:000027026](http://purl.obolibrary.org/obo/PR_000027026) |
| `UniProtKB:Q9R207-1`  |              1 | [PR:000027034](http://purl.obolibrary.org/obo/PR_000027034) |
| `UniProtKB:P70388-1`  |              1 | [PR:000027036](http://purl.obolibrary.org/obo/PR_000027036) |
| `UniProtKB:Q9JIL9-1`  |              1 | [PR:000027037](http://purl.obolibrary.org/obo/PR_000027037) |
| `UniProtKB:P49959-1`  |              1 | [PR:000027038](http://purl.obolibrary.org/obo/PR_000027038) |
| `UniProtKB:P70388-3`  |              1 | [PR:000027040](http://purl.obolibrary.org/obo/PR_000027040) |
| `UniProtKB:P70388-4`  |              1 | [PR:000027042](http://purl.obolibrary.org/obo/PR_000027042) |
| `UniProtKB:Q61216-1`  |              1 | [PR:000027044](http://purl.obolibrary.org/obo/PR_000027044) |
| `UniProtKB:Q61216-2`  |              1 | [PR:000027046](http://purl.obolibrary.org/obo/PR_000027046) |
| `UniProtKB:Q8N2H9-1`  |              1 | [PR:000027049](http://purl.obolibrary.org/obo/PR_000027049) |
| `UniProtKB:Q8N2H9-2`  |              1 | [PR:000027051](http://purl.obolibrary.org/obo/PR_000027051) |
| `UniProtKB:Q8BXR6-1`  |              1 | [PR:000027052](http://purl.obolibrary.org/obo/PR_000027052) |
| `UniProtKB:Q8BMS1-1`  |              1 | [PR:000027060](http://purl.obolibrary.org/obo/PR_000027060) |
| `UniProtKB:Q99JY0-1`  |              1 | [PR:000027062](http://purl.obolibrary.org/obo/PR_000027062) |
| `UniProtKB:P17679-1`  |              1 | [PR:000027064](http://purl.obolibrary.org/obo/PR_000027064) |
| `UniProtKB:P17679-2`  |              1 | [PR:000027070](http://purl.obolibrary.org/obo/PR_000027070) |
| `UniProtKB:P15976-3`  |              1 | [PR:000027071](http://purl.obolibrary.org/obo/PR_000027071) |
| `UniProtKB:P56477-1`  |              1 | [PR:000027088](http://purl.obolibrary.org/obo/PR_000027088) |
| `UniProtKB:Q13568-1`  |              1 | [PR:000027089](http://purl.obolibrary.org/obo/PR_000027089) |
| `UniProtKB:P30355-1`  |              1 | [PR:000027154](http://purl.obolibrary.org/obo/PR_000027154) |
| `UniProtKB:P48999-1`  |              1 | [PR:000027156](http://purl.obolibrary.org/obo/PR_000027156) |
| `UniProtKB:P07310-1`  |              1 | [PR:000027158](http://purl.obolibrary.org/obo/PR_000027158) |
| `UniProtKB:Q04447-1`  |              1 | [PR:000027160](http://purl.obolibrary.org/obo/PR_000027160) |
| `UniProtKB:P58753-1`  |              1 | [PR:000027186](http://purl.obolibrary.org/obo/PR_000027186) |
| `UniProtKB:Q9NWZ3-1`  |              1 | [PR:000027189](http://purl.obolibrary.org/obo/PR_000027189) |
| `UniProtKB:Q86XR7-1`  |              1 | [PR:000027198](http://purl.obolibrary.org/obo/PR_000027198) |
| `UniProtKB:Q03135-1`  |              1 | [PR:000027210](http://purl.obolibrary.org/obo/PR_000027210) |
| `UniProtKB:P70160-1`  |              1 | [PR:000027225](http://purl.obolibrary.org/obo/PR_000027225) |
| `UniProtKB:Q99JA0-1`  |              1 | [PR:000027227](http://purl.obolibrary.org/obo/PR_000027227) |
| `UniProtKB:P18761-1`  |              1 | [PR:000027229](http://purl.obolibrary.org/obo/PR_000027229) |
| `UniProtKB:Q71UK2-1`  |              1 | [PR:000027231](http://purl.obolibrary.org/obo/PR_000027231) |
| `UniProtKB:P12931-1`  |              1 | [PR:000027236](http://purl.obolibrary.org/obo/PR_000027236) |
| `UniProtKB:P12931-2`  |              1 | [PR:000027240](http://purl.obolibrary.org/obo/PR_000027240) |
| `UniProtKB:Q9Y616-1`  |              1 | [PR:000027242](http://purl.obolibrary.org/obo/PR_000027242) |
| `UniProtKB:Q9QZ06-1`  |              1 | [PR:000027251](http://purl.obolibrary.org/obo/PR_000027251) |
| `UniProtKB:Q99460-2`  |              1 | [PR:000027333](http://purl.obolibrary.org/obo/PR_000027333) |
| `UniProtKB:P60891-1`  |              1 | [PR:000027432](http://purl.obolibrary.org/obo/PR_000027432) |
| `UniProtKB:Q76MX9-1`  |              1 | [PR:000027433](http://purl.obolibrary.org/obo/PR_000027433) |
| `UniProtKB:P11908-1`  |              1 | [PR:000027435](http://purl.obolibrary.org/obo/PR_000027435) |
| `UniProtKB:Q9D0M1-1`  |              1 | [PR:000027437](http://purl.obolibrary.org/obo/PR_000027437) |
| `UniProtKB:Q8R574-1`  |              1 | [PR:000027441](http://purl.obolibrary.org/obo/PR_000027441) |
| `UniProtKB:Q9CS42-1`  |              1 | [PR:000027444](http://purl.obolibrary.org/obo/PR_000027444) |
| `UniProtKB:Q14457-1`  |              1 | [PR:000027469](http://purl.obolibrary.org/obo/PR_000027469) |
| `UniProtKB:P00533-1`  |              1 | [PR:000027475](http://purl.obolibrary.org/obo/PR_000027475) |
| `UniProtKB:P60892-1`  |              1 | [PR:000027481](http://purl.obolibrary.org/obo/PR_000027481) |
| `UniProtKB:P09330-1`  |              1 | [PR:000027482](http://purl.obolibrary.org/obo/PR_000027482) |
| `UniProtKB:O08618-1`  |              1 | [PR:000027483](http://purl.obolibrary.org/obo/PR_000027483) |
| `UniProtKB:Q63468-1`  |              1 | [PR:000027484](http://purl.obolibrary.org/obo/PR_000027484) |
| `UniProtKB:Q07817-1`  |              1 | [PR:000027485](http://purl.obolibrary.org/obo/PR_000027485) |
| `UniProtKB:Q9D2H1-1`  |              1 | [PR:000027489](http://purl.obolibrary.org/obo/PR_000027489) |
| `UniProtKB:P56393-1`  |              1 | [PR:000027491](http://purl.obolibrary.org/obo/PR_000027491) |
| `UniProtKB:Q61239-1`  |              1 | [PR:000027684](http://purl.obolibrary.org/obo/PR_000027684) |
| `UniProtKB:Q8K2I1-1`  |              1 | [PR:000027686](http://purl.obolibrary.org/obo/PR_000027686) |
| `UniProtKB:Q04631-1`  |              1 | [PR:000027687](http://purl.obolibrary.org/obo/PR_000027687) |
| `UniProtKB:Q02293-1`  |              1 | [PR:000027688](http://purl.obolibrary.org/obo/PR_000027688) |
| `UniProtKB:Q9Y6Q9-1`  |              1 | [PR:000027690](http://purl.obolibrary.org/obo/PR_000027690) |
| `UniProtKB:P61922-1`  |              1 | [PR:000027700](http://purl.obolibrary.org/obo/PR_000027700) |
| `UniProtKB:P80404-1`  |              1 | [PR:000027701](http://purl.obolibrary.org/obo/PR_000027701) |
| `UniProtKB:Q8BUY9-1`  |              1 | [PR:000027710](http://purl.obolibrary.org/obo/PR_000027710) |
| `UniProtKB:P53609-1`  |              1 | [PR:000027711](http://purl.obolibrary.org/obo/PR_000027711) |
| `UniProtKB:P53610-1`  |              1 | [PR:000027712](http://purl.obolibrary.org/obo/PR_000027712) |
| `UniProtKB:P03372-1`  |              1 | [PR:000027722](http://purl.obolibrary.org/obo/PR_000027722) |
| `UniProtKB:Q9Z2I9-1`  |              1 | [PR:000027781](http://purl.obolibrary.org/obo/PR_000027781) |
| `UniProtKB:Q9Z2I8-1`  |              1 | [PR:000027786](http://purl.obolibrary.org/obo/PR_000027786) |
| `UniProtKB:Q64279-1`  |              1 | [PR:000027798](http://purl.obolibrary.org/obo/PR_000027798) |
| `UniProtKB:O35615-1`  |              1 | [PR:000027816](http://purl.obolibrary.org/obo/PR_000027816) |
| `UniProtKB:P26687-1`  |              1 | [PR:000027820](http://purl.obolibrary.org/obo/PR_000027820) |
| `UniProtKB:P11983-1`  |              1 | [PR:000027854](http://purl.obolibrary.org/obo/PR_000027854) |
| `UniProtKB:P80318-1`  |              1 | [PR:000027857](http://purl.obolibrary.org/obo/PR_000027857) |
| `UniProtKB:P80315-1`  |              1 | [PR:000027859](http://purl.obolibrary.org/obo/PR_000027859) |
| `UniProtKB:P80316-1`  |              1 | [PR:000027861](http://purl.obolibrary.org/obo/PR_000027861) |
| `UniProtKB:P80317-1`  |              1 | [PR:000027863](http://purl.obolibrary.org/obo/PR_000027863) |
| `UniProtKB:P80314-1`  |              1 | [PR:000027865](http://purl.obolibrary.org/obo/PR_000027865) |
| `UniProtKB:P80313-1`  |              1 | [PR:000027867](http://purl.obolibrary.org/obo/PR_000027867) |
| `UniProtKB:P16627-1`  |              1 | [PR:000027870](http://purl.obolibrary.org/obo/PR_000027870) |
| `UniProtKB:P17879-1`  |              1 | [PR:000027872](http://purl.obolibrary.org/obo/PR_000027872) |
| `UniProtKB:Q6X786-1`  |              1 | [PR:000027874](http://purl.obolibrary.org/obo/PR_000027874) |
| `UniProtKB:P42932-1`  |              1 | [PR:000027876](http://purl.obolibrary.org/obo/PR_000027876) |
| `UniProtKB:Q62522-1`  |              1 | [PR:000027878](http://purl.obolibrary.org/obo/PR_000027878) |
| `UniProtKB:Q12778-1`  |              1 | [PR:000027879](http://purl.obolibrary.org/obo/PR_000027879) |
| `UniProtKB:Q0VET1-1`  |              1 | [PR:000027881](http://purl.obolibrary.org/obo/PR_000027881) |
| `UniProtKB:Q61390-1`  |              1 | [PR:000027883](http://purl.obolibrary.org/obo/PR_000027883) |
| `UniProtKB:Q7TSD4-1`  |              1 | [PR:000027900](http://purl.obolibrary.org/obo/PR_000027900) |
| `UniProtKB:Q7TSD4-2`  |              1 | [PR:000027902](http://purl.obolibrary.org/obo/PR_000027902) |
| `UniProtKB:Q7TSD4-3`  |              1 | [PR:000027904](http://purl.obolibrary.org/obo/PR_000027904) |
| `UniProtKB:Q7TSD4-4`  |              1 | [PR:000027906](http://purl.obolibrary.org/obo/PR_000027906) |
| `UniProtKB:Q7TSD4-5`  |              1 | [PR:000027908](http://purl.obolibrary.org/obo/PR_000027908) |
| `UniProtKB:Q7TSD4-6`  |              1 | [PR:000027910](http://purl.obolibrary.org/obo/PR_000027910) |
| `UniProtKB:Q7TSD4-7`  |              1 | [PR:000027912](http://purl.obolibrary.org/obo/PR_000027912) |
| `UniProtKB:Q7TSD4-8`  |              1 | [PR:000027914](http://purl.obolibrary.org/obo/PR_000027914) |
| `UniProtKB:Q04206-1`  |              1 | [PR:000027916](http://purl.obolibrary.org/obo/PR_000027916) |
| `UniProtKB:P40763-1`  |              1 | [PR:000027922](http://purl.obolibrary.org/obo/PR_000027922) |
| `UniProtKB:Q8CFN5-1`  |              1 | [PR:000027926](http://purl.obolibrary.org/obo/PR_000027926) |
| `UniProtKB:Q8CFN5-2`  |              1 | [PR:000027928](http://purl.obolibrary.org/obo/PR_000027928) |
| `UniProtKB:P50750-1`  |              1 | [PR:000027932](http://purl.obolibrary.org/obo/PR_000027932) |
| `UniProtKB:Q9NR97-1`  |              1 | [PR:000027945](http://purl.obolibrary.org/obo/PR_000027945) |
| `UniProtKB:P58682-1`  |              1 | [PR:000027948](http://purl.obolibrary.org/obo/PR_000027948) |
| `UniProtKB:A5H300-1`  |              1 | [PR:000027949](http://purl.obolibrary.org/obo/PR_000027949) |
| `UniProtKB:P63038-1`  |              1 | [PR:000028332](http://purl.obolibrary.org/obo/PR_000028332) |
| `UniProtKB:Q84UJ3-1`  |              1 | [PR:000028335](http://purl.obolibrary.org/obo/PR_000028335) |
| `UniProtKB:Q9LR78-1`  |              1 | [PR:000028340](http://purl.obolibrary.org/obo/PR_000028340) |
| `UniProtKB:Q94F62-1`  |              1 | [PR:000028345](http://purl.obolibrary.org/obo/PR_000028345) |
| `UniProtKB:O22476-1`  |              1 | [PR:000028355](http://purl.obolibrary.org/obo/PR_000028355) |
| `UniProtKB:O48814-1`  |              1 | [PR:000028481](http://purl.obolibrary.org/obo/PR_000028481) |
| `UniProtKB:Q924A0-1`  |              1 | [PR:000028512](http://purl.obolibrary.org/obo/PR_000028512) |
| `UniProtKB:Q924A0-2`  |              1 | [PR:000028514](http://purl.obolibrary.org/obo/PR_000028514) |
| `UniProtKB:Q924A0-3`  |              1 | [PR:000028516](http://purl.obolibrary.org/obo/PR_000028516) |
| `UniProtKB:Q924A0-4`  |              1 | [PR:000028518](http://purl.obolibrary.org/obo/PR_000028518) |
| `UniProtKB:Q924A0-5`  |              1 | [PR:000028520](http://purl.obolibrary.org/obo/PR_000028520) |
| `UniProtKB:Q924A0-6`  |              1 | [PR:000028522](http://purl.obolibrary.org/obo/PR_000028522) |
| `UniProtKB:Q924A0-7`  |              1 | [PR:000028524](http://purl.obolibrary.org/obo/PR_000028524) |
| `UniProtKB:Q924A0-8`  |              1 | [PR:000028526](http://purl.obolibrary.org/obo/PR_000028526) |
| `UniProtKB:P22561-1`  |              1 | [PR:000028529](http://purl.obolibrary.org/obo/PR_000028529) |
| `UniProtKB:P22561-2`  |              1 | [PR:000028531](http://purl.obolibrary.org/obo/PR_000028531) |
| `UniProtKB:P22561-3`  |              1 | [PR:000028533](http://purl.obolibrary.org/obo/PR_000028533) |
| `UniProtKB:P22561-4`  |              1 | [PR:000028535](http://purl.obolibrary.org/obo/PR_000028535) |
| `UniProtKB:P22561-5`  |              1 | [PR:000028537](http://purl.obolibrary.org/obo/PR_000028537) |
| `UniProtKB:P22561-6`  |              1 | [PR:000028539](http://purl.obolibrary.org/obo/PR_000028539) |
| `UniProtKB:P25963-1`  |              1 | [PR:000028544](http://purl.obolibrary.org/obo/PR_000028544) |
| `UniProtKB:Q3UB40-1`  |              1 | [PR:000028549](http://purl.obolibrary.org/obo/PR_000028549) |
| `UniProtKB:P15336-1`  |              1 | [PR:000028563](http://purl.obolibrary.org/obo/PR_000028563) |
| `UniProtKB:P56545-1`  |              1 | [PR:000028567](http://purl.obolibrary.org/obo/PR_000028567) |
| `UniProtKB:P50549-1`  |              1 | [PR:000028571](http://purl.obolibrary.org/obo/PR_000028571) |
| `UniProtKB:Q96RI1-1`  |              1 | [PR:000028575](http://purl.obolibrary.org/obo/PR_000028575) |
| `UniProtKB:Q13330-1`  |              1 | [PR:000028585](http://purl.obolibrary.org/obo/PR_000028585) |
| `UniProtKB:P23511-1`  |              1 | [PR:000028594](http://purl.obolibrary.org/obo/PR_000028594) |
| `UniProtKB:O15527-1`  |              1 | [PR:000028598](http://purl.obolibrary.org/obo/PR_000028598) |
| `UniProtKB:P00519-1`  |              1 | [PR:000028610](http://purl.obolibrary.org/obo/PR_000028610) |
| `UniProtKB:P00519-2`  |              1 | [PR:000028612](http://purl.obolibrary.org/obo/PR_000028612) |
| `UniProtKB:P36956-1`  |              1 | [PR:000028628](http://purl.obolibrary.org/obo/PR_000028628) |
| `UniProtKB:P00342-1`  |              1 | [PR:000028632](http://purl.obolibrary.org/obo/PR_000028632) |
| `UniProtKB:P16220-2`  |              1 | [PR:000028634](http://purl.obolibrary.org/obo/PR_000028634) |
| `UniProtKB:P16220-1`  |              1 | [PR:000028639](http://purl.obolibrary.org/obo/PR_000028639) |
| `UniProtKB:Q00978-1`  |              1 | [PR:000028648](http://purl.obolibrary.org/obo/PR_000028648) |
| `UniProtKB:P52630-1`  |              1 | [PR:000028652](http://purl.obolibrary.org/obo/PR_000028652) |
| `UniProtKB:Q99612-1`  |              1 | [PR:000028656](http://purl.obolibrary.org/obo/PR_000028656) |
| `UniProtKB:O15265-1`  |              1 | [PR:000028660](http://purl.obolibrary.org/obo/PR_000028660) |
| `UniProtKB:P23771-1`  |              1 | [PR:000028664](http://purl.obolibrary.org/obo/PR_000028664) |
| `UniProtKB:P23771-2`  |              1 | [PR:000028666](http://purl.obolibrary.org/obo/PR_000028666) |
| `UniProtKB:Q14164-1`  |              1 | [PR:000028689](http://purl.obolibrary.org/obo/PR_000028689) |
| `UniProtKB:Q9UHD2-1`  |              1 | [PR:000028693](http://purl.obolibrary.org/obo/PR_000028693) |
| `UniProtKB:Q9H211-1`  |              1 | [PR:000028739](http://purl.obolibrary.org/obo/PR_000028739) |
| `UniProtKB:P33076-1`  |              1 | [PR:000028743](http://purl.obolibrary.org/obo/PR_000028743) |
| `UniProtKB:P60484-1`  |              1 | [PR:000028748](http://purl.obolibrary.org/obo/PR_000028748) |
| `UniProtKB:Q9NP62-1`  |              1 | [PR:000028752](http://purl.obolibrary.org/obo/PR_000028752) |
| `UniProtKB:Q9UBC0-1`  |              1 | [PR:000028756](http://purl.obolibrary.org/obo/PR_000028756) |
| `UniProtKB:P10085-1`  |              1 | [PR:000028760](http://purl.obolibrary.org/obo/PR_000028760) |
| `UniProtKB:Q15699-1`  |              1 | [PR:000028764](http://purl.obolibrary.org/obo/PR_000028764) |
| `UniProtKB:Q01094-1`  |              1 | [PR:000028768](http://purl.obolibrary.org/obo/PR_000028768) |
| `UniProtKB:Q14209-1`  |              1 | [PR:000028772](http://purl.obolibrary.org/obo/PR_000028772) |
| `UniProtKB:O00716-1`  |              1 | [PR:000028776](http://purl.obolibrary.org/obo/PR_000028776) |
| `UniProtKB:Q14526-1`  |              1 | [PR:000028780](http://purl.obolibrary.org/obo/PR_000028780) |
| `UniProtKB:Q14526-2`  |              1 | [PR:000028782](http://purl.obolibrary.org/obo/PR_000028782) |
| `UniProtKB:P06400-1`  |              1 | [PR:000028786](http://purl.obolibrary.org/obo/PR_000028786) |
| `UniProtKB:P10275-1`  |              1 | [PR:000028790](http://purl.obolibrary.org/obo/PR_000028790) |
| `UniProtKB:O60566-1`  |              1 | [PR:000028796](http://purl.obolibrary.org/obo/PR_000028796) |
| `UniProtKB:P97377-1`  |              1 | [PR:000028801](http://purl.obolibrary.org/obo/PR_000028801) |
| `UniProtKB:Q86UQ8-1`  |              1 | [PR:000028807](http://purl.obolibrary.org/obo/PR_000028807) |
| `UniProtKB:P14316-1`  |              1 | [PR:000028811](http://purl.obolibrary.org/obo/PR_000028811) |
| `UniProtKB:Q01543-1`  |              1 | [PR:000028815](http://purl.obolibrary.org/obo/PR_000028815) |
| `UniProtKB:P05017-1`  |              1 | [PR:000028825](http://purl.obolibrary.org/obo/PR_000028825) |
| `UniProtKB:P05017-2`  |              1 | [PR:000028827](http://purl.obolibrary.org/obo/PR_000028827) |
| `UniProtKB:Q8BIF2-1`  |              1 | [PR:000028830](http://purl.obolibrary.org/obo/PR_000028830) |
| `UniProtKB:Q8BIF2-2`  |              1 | [PR:000028832](http://purl.obolibrary.org/obo/PR_000028832) |
| `UniProtKB:Q8BIF2-3`  |              1 | [PR:000028834](http://purl.obolibrary.org/obo/PR_000028834) |
| `UniProtKB:Q8BIF2-4`  |              1 | [PR:000028836](http://purl.obolibrary.org/obo/PR_000028836) |
| `UniProtKB:Q8BIF2-5`  |              1 | [PR:000028838](http://purl.obolibrary.org/obo/PR_000028838) |
| `UniProtKB:Q80VA5-1`  |              1 | [PR:000028843](http://purl.obolibrary.org/obo/PR_000028843) |
| `UniProtKB:P08575-3`  |              1 | [PR:P08575-3](http://purl.obolibrary.org/obo/PR_P08575-3)   |
| `UniProtKB:P08575-8`  |              1 | [PR:P08575-8](http://purl.obolibrary.org/obo/PR_P08575-8)   |

## `UniProtKB-KW`: UniProt Keywords

Overall, there were 1 invalid
xrefs to external prefixed with `UniProtKB-KW` (standardized to Bioregistry
prefix [`uniprot.keyword`](https://bioregistry.io/uniprot.keyword)) that
did not match the standard pattern `^KW-\d{4}$`.

| external_xref         |   usages_count | usages                                                  |
|-----------------------|----------------|---------------------------------------------------------|
| `UniProtKB-KW:KW-984` |              1 | [GO:0039664](http://purl.obolibrary.org/obo/GO_0039664) |

## `UniProtKB_VAR`: UniProt Variants

Overall, there were 64 invalid
xrefs to external prefixed with `UniProtKB_VAR` (standardized to Bioregistry
prefix [`uniprot.var`](https://bioregistry.io/uniprot.var)) that
did not match the standard pattern `^\d+$`.

| external_xref               |   usages_count | usages                                                      |
|-----------------------------|----------------|-------------------------------------------------------------|
| `UniProtKB_VAR:VAR_009931`  |              1 | [PR:000000828](http://purl.obolibrary.org/obo/PR_000000828) |
| `UniProtKB_VAR:VAR_001529.` |              1 | [PR:000000829](http://purl.obolibrary.org/obo/PR_000000829) |
| `UniProtKB_VAR:VAR_009918`  |              1 | [PR:000000833](http://purl.obolibrary.org/obo/PR_000000833) |
| `UniProtKB_VAR:VAR_008944`  |              1 | [PR:000000836](http://purl.obolibrary.org/obo/PR_000000836) |
| `UniProtKB_VAR:VAR_001544`  |              1 | [PR:000000837](http://purl.obolibrary.org/obo/PR_000000837) |
| `UniProtKB_VAR:VAR_009917`  |              1 | [PR:000000838](http://purl.obolibrary.org/obo/PR_000000838) |
| `UniProtKB_VAR:VAR_008943`  |              1 | [PR:000000840](http://purl.obolibrary.org/obo/PR_000000840) |
| `UniProtKB_VAR:VAR_009928`  |              1 | [PR:000000841](http://purl.obolibrary.org/obo/PR_000000841) |
| `UniProtKB_VAR:VAR_044424`  |              1 | [PR:000025560](http://purl.obolibrary.org/obo/PR_000025560) |
| `UniProtKB_VAR:VAR_000016`  |              1 | [PR:000025561](http://purl.obolibrary.org/obo/PR_000025561) |
| `UniProtKB_VAR:VAR_014215`  |              1 | [PR:000025562](http://purl.obolibrary.org/obo/PR_000025562) |
| `UniProtKB_VAR:VAR_014216`  |              1 | [PR:000025563](http://purl.obolibrary.org/obo/PR_000025563) |
| `UniProtKB_VAR:VAR_000017`  |              1 | [PR:000025564](http://purl.obolibrary.org/obo/PR_000025564) |
| `UniProtKB_VAR:VAR_014217`  |              1 | [PR:000025565](http://purl.obolibrary.org/obo/PR_000025565) |
| `UniProtKB_VAR:VAR_032276`  |              1 | [PR:000025566](http://purl.obolibrary.org/obo/PR_000025566) |
| `UniProtKB_VAR:VAR_000019`  |              1 | [PR:000025567](http://purl.obolibrary.org/obo/PR_000025567) |
| `UniProtKB_VAR:VAR_032277`  |              1 | [PR:000025568](http://purl.obolibrary.org/obo/PR_000025568) |
| `UniProtKB_VAR:VAR_014218`  |              1 | [PR:000025569](http://purl.obolibrary.org/obo/PR_000025569) |
| `UniProtKB_VAR:VAR_010108`  |              1 | [PR:000025570](http://purl.obolibrary.org/obo/PR_000025570) |
| `UniProtKB_VAR:VAR_000020`  |              1 | [PR:000025571](http://purl.obolibrary.org/obo/PR_000025571) |
| `UniProtKB_VAR:VAR_000023`  |              1 | [PR:000025572](http://purl.obolibrary.org/obo/PR_000025572) |
| `UniProtKB_VAR:VAR_000022`  |              1 | [PR:000025573](http://purl.obolibrary.org/obo/PR_000025573) |
| `UniProtKB_VAR:VAR_000021`  |              1 | [PR:000025574](http://purl.obolibrary.org/obo/PR_000025574) |
| `UniProtKB_VAR:VAR_014219`  |              1 | [PR:000025575](http://purl.obolibrary.org/obo/PR_000025575) |
| `UniProtKB_VAR:VAR_010109`  |              1 | [PR:000025576](http://purl.obolibrary.org/obo/PR_000025576) |
| `UniProtKB_VAR:VAR_010107`  |              1 | [PR:000025590](http://purl.obolibrary.org/obo/PR_000025590) |
| `UniProtKB_VAR:VAR_000018`  |              1 | [PR:000025593](http://purl.obolibrary.org/obo/PR_000025593) |
| `UniProtKB_VAR:VAR_000015`  |              1 | [PR:000025601](http://purl.obolibrary.org/obo/PR_000025601) |
| `UniProtKB_VAR:VAR_012788`  |              1 | [PR:000026112](http://purl.obolibrary.org/obo/PR_000026112) |
| `UniProtKB_VAR:VAR_012787`  |              1 | [PR:000026113](http://purl.obolibrary.org/obo/PR_000026113) |
| `UniProtKB_VAR:VAR_012785`  |              1 | [PR:000026114](http://purl.obolibrary.org/obo/PR_000026114) |
| `UniProtKB_VAR:VAR_012795`  |              1 | [PR:000026118](http://purl.obolibrary.org/obo/PR_000026118) |
| `UniProtKB_VAR:VAR_012792`  |              1 | [PR:000026119](http://purl.obolibrary.org/obo/PR_000026119) |
| `UniProtKB_VAR:VAR_012800`  |              1 | [PR:000026120](http://purl.obolibrary.org/obo/PR_000026120) |
| `UniProtKB_VAR:VAR_022315`  |              1 | [PR:000028706](http://purl.obolibrary.org/obo/PR_000028706) |
| `UniProtKB_VAR:VAR_019660`  |              1 | [PR:000028709](http://purl.obolibrary.org/obo/PR_000028709) |
| `UniProtKB_VAR:VAR_019661`  |              1 | [PR:000028710](http://purl.obolibrary.org/obo/PR_000028710) |
| `UniProtKB_VAR:VAR_064622`  |              1 | [PR:000028711](http://purl.obolibrary.org/obo/PR_000028711) |
| `UniProtKB_VAR:VAR_064623`  |              1 | [PR:000028712](http://purl.obolibrary.org/obo/PR_000028712) |
| `UniProtKB_VAR:VAR_010340`  |              1 | [PR:000028713](http://purl.obolibrary.org/obo/PR_000028713) |
| `UniProtKB_VAR:VAR_010341`  |              1 | [PR:000028714](http://purl.obolibrary.org/obo/PR_000028714) |
| `UniProtKB_VAR:VAR_056121`  |              1 | [PR:000028715](http://purl.obolibrary.org/obo/PR_000028715) |
| `UniProtKB_VAR:VAR_010342`  |              1 | [PR:000028716](http://purl.obolibrary.org/obo/PR_000028716) |
| `UniProtKB_VAR:VAR_010343`  |              1 | [PR:000028717](http://purl.obolibrary.org/obo/PR_000028717) |
| `UniProtKB_VAR:VAR_010344`  |              1 | [PR:000028718](http://purl.obolibrary.org/obo/PR_000028718) |
| `UniProtKB_VAR:VAR_019662`  |              1 | [PR:000028719](http://purl.obolibrary.org/obo/PR_000028719) |
| `UniProtKB_VAR:VAR_010345`  |              1 | [PR:000028720](http://purl.obolibrary.org/obo/PR_000028720) |
| `UniProtKB_VAR:VAR_010346`  |              1 | [PR:000028721](http://purl.obolibrary.org/obo/PR_000028721) |
| `UniProtKB_VAR:VAR_010347`  |              1 | [PR:000028722](http://purl.obolibrary.org/obo/PR_000028722) |
| `UniProtKB_VAR:VAR_019663`  |              1 | [PR:000028723](http://purl.obolibrary.org/obo/PR_000028723) |
| `UniProtKB_VAR:VAR_019664`  |              1 | [PR:000028724](http://purl.obolibrary.org/obo/PR_000028724) |
| `UniProtKB_VAR:VAR_064624`  |              1 | [PR:000028725](http://purl.obolibrary.org/obo/PR_000028725) |
| `UniProtKB_VAR:VAR_010348`  |              1 | [PR:000028726](http://purl.obolibrary.org/obo/PR_000028726) |
| `UniProtKB_VAR:VAR_010349`  |              1 | [PR:000028727](http://purl.obolibrary.org/obo/PR_000028727) |
| `UniProtKB_VAR:VAR_037439`  |              1 | [PR:000028728](http://purl.obolibrary.org/obo/PR_000028728) |
| `UniProtKB_VAR:VAR_010350`  |              1 | [PR:000028729](http://purl.obolibrary.org/obo/PR_000028729) |
| `UniProtKB_VAR:VAR_037440`  |              1 | [PR:000028730](http://purl.obolibrary.org/obo/PR_000028730) |
| `UniProtKB_VAR:VAR_019665`  |              1 | [PR:000028731](http://purl.obolibrary.org/obo/PR_000028731) |
| `UniProtKB_VAR:VAR_010351`  |              1 | [PR:000028732](http://purl.obolibrary.org/obo/PR_000028732) |
| `UniProtKB_VAR:VAR_019666`  |              1 | [PR:000028733](http://purl.obolibrary.org/obo/PR_000028733) |
| `UniProtKB_VAR:VAR_019667`  |              1 | [PR:000028734](http://purl.obolibrary.org/obo/PR_000028734) |
| `UniProtKB_VAR:VAR_019668`  |              1 | [PR:000028735](http://purl.obolibrary.org/obo/PR_000028735) |
| `UniProtKB_VAR:VAR_010352`  |              1 | [PR:000028736](http://purl.obolibrary.org/obo/PR_000028736) |
| `UniProtKB_VAR:VAR_010353`  |              1 | [PR:000028737](http://purl.obolibrary.org/obo/PR_000028737) |

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

Overall, there were 4 invalid
xrefs to external prefixed with `WB` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref      |   usages_count | usages                                                          |
|--------------------|----------------|-----------------------------------------------------------------|
| `WB:ems`           |              1 | [SO:0000274](http://purl.obolibrary.org/obo/SO_0000274)         |
| `WB:Paper00000938` |              1 | [UBERON:0000934](http://purl.obolibrary.org/obo/UBERON_0000934) |
| `WB:Paper00000653` |              1 | [UBERON:0000954](http://purl.obolibrary.org/obo/UBERON_0000954) |
| `WB:rynl`          |              1 | [UBERON:0001016](http://purl.obolibrary.org/obo/UBERON_0001016) |

## `WB_REF`: Wormbase Gene

Overall, there were 2 invalid
xrefs to external prefixed with `WB_REF` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref        |   usages_count | usages                                                  |
|----------------------|----------------|---------------------------------------------------------|
| `WB_REF:cgc467`      |              1 | [GO:0043052](http://purl.obolibrary.org/obo/GO_0043052) |
| `WB_REF:wm2003ab740` |              1 | [GO:0043055](http://purl.obolibrary.org/obo/GO_0043055) |

## `XAO`: Xenopus Anatomy Ontology

Overall, there were 9 invalid
xrefs to external prefixed with `XAO` (standardized to Bioregistry
prefix [`xao`](https://bioregistry.io/xao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `XAO:EJS`       |              4 | [UBERON:0015179](http://purl.obolibrary.org/obo/UBERON_0015179), [UBERON:3010297](http://purl.obolibrary.org/obo/UBERON_3010297), [UBERON:3010299](http://purl.obolibrary.org/obo/UBERON_3010299), [UBERON:4000013](http://purl.obolibrary.org/obo/UBERON_4000013) |
| `XAO:curator`   |              2 | [UBERON:3010326](http://purl.obolibrary.org/obo/UBERON_3010326), [UBERON:3010404](http://purl.obolibrary.org/obo/UBERON_3010404)                                                                                                                                   |
| `XAO:00002785`  |              1 | [GO:0039019](http://purl.obolibrary.org/obo/GO_0039019)                                                                                                                                                                                                            |
| `XAO:00002000`  |              1 | [GO:0048793](http://purl.obolibrary.org/obo/GO_0048793)                                                                                                                                                                                                            |
| `XAO:curators`  |              1 | [UBERON:0009500](http://purl.obolibrary.org/obo/UBERON_0009500)                                                                                                                                                                                                    |

## `xenbase`: Xenbase

Overall, there were 5 invalid
xrefs to external prefixed with `xenbase` (standardized to Bioregistry
prefix [`xenbase`](https://bioregistry.io/xenbase)) that
did not match the standard pattern `^XB\-\w+\-\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                      |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `xenbase:jb`    |              5 | [SO:0001203](http://purl.obolibrary.org/obo/SO_0001203), [SO:0001204](http://purl.obolibrary.org/obo/SO_0001204), [SO:0001205](http://purl.obolibrary.org/obo/SO_0001205), [SO:0001206](http://purl.obolibrary.org/obo/SO_0001206), [SO:0001207](http://purl.obolibrary.org/obo/SO_0001207) |

## `ZFA`: Zebrafish anatomy and development ontology

Overall, there were 16 invalid
xrefs to external prefixed with `ZFA` (standardized to Bioregistry
prefix [`zfa`](https://bioregistry.io/zfa)) that
did not match the standard pattern `^\d{7}$`.

| external_xref           |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|-------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFA:curator`           |              9 | [UBERON:0008229](http://purl.obolibrary.org/obo/UBERON_0008229), [UBERON:0014371](http://purl.obolibrary.org/obo/UBERON_0014371), [UBERON:0014903](http://purl.obolibrary.org/obo/UBERON_0014903), [UBERON:0018549](http://purl.obolibrary.org/obo/UBERON_0018549), [UBERON:2000120](http://purl.obolibrary.org/obo/UBERON_2000120), ... |
| `ZFA:CVS`               |              2 | [UBERON:0016499](http://purl.obolibrary.org/obo/UBERON_0016499), [UBERON:0018674](http://purl.obolibrary.org/obo/UBERON_0018674)                                                                                                                                                                                                         |
| `ZFA:00001558`          |              1 | [GO:0039008](http://purl.obolibrary.org/obo/GO_0039008)                                                                                                                                                                                                                                                                                  |
| `ZFA:00001557`          |              1 | [GO:0039021](http://purl.obolibrary.org/obo/GO_0039021)                                                                                                                                                                                                                                                                                  |
| `ZFA:yb`                |              1 | [UBERON:0002539](http://purl.obolibrary.org/obo/UBERON_0002539)                                                                                                                                                                                                                                                                          |
| `ZFA:YMB`               |              1 | [UBERON:0016499](http://purl.obolibrary.org/obo/UBERON_0016499)                                                                                                                                                                                                                                                                          |
| `ZFA:ZDB-PUB-060323-12` |              1 | [UBERON:2005245](http://purl.obolibrary.org/obo/UBERON_2005245)                                                                                                                                                                                                                                                                          |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 529 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref    |   usages_count | usages                                                                                                                                                                                                                                                                                                                                   |
|------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:curator`   |            515 | [UBERON:0000007](http://purl.obolibrary.org/obo/UBERON_0000007), [UBERON:0000966](http://purl.obolibrary.org/obo/UBERON_0000966), [UBERON:0000991](http://purl.obolibrary.org/obo/UBERON_0000991), [UBERON:0001016](http://purl.obolibrary.org/obo/UBERON_0001016), [UBERON:0001081](http://purl.obolibrary.org/obo/UBERON_0001081), ... |
| `ZFIN:dh`        |              3 | [SO:0001477](http://purl.obolibrary.org/obo/SO_0001477), [SO:0001478](http://purl.obolibrary.org/obo/SO_0001478), [SO:0001479](http://purl.obolibrary.org/obo/SO_0001479)                                                                                                                                                                |
| `ZFIN:CVS`       |              2 | [CL:0005024](http://purl.obolibrary.org/obo/CL_0005024), [UBERON:2005265](http://purl.obolibrary.org/obo/UBERON_2005265)                                                                                                                                                                                                                 |
| `ZFIN:mh`        |              2 | [SO:0001480](http://purl.obolibrary.org/obo/SO_0001480), [SO:0001481](http://purl.obolibrary.org/obo/SO_0001481)                                                                                                                                                                                                                         |
| `ZFIN:Curator`   |              2 | [UBERON:0005817](http://purl.obolibrary.org/obo/UBERON_0005817), [UBERON:2005210](http://purl.obolibrary.org/obo/UBERON_2005210)                                                                                                                                                                                                         |
| `ZFIN:dsf`       |              1 | [GO:0044458](http://purl.obolibrary.org/obo/GO_0044458)                                                                                                                                                                                                                                                                                  |
| `ZFIN:st`        |              1 | [SO:0002217](http://purl.obolibrary.org/obo/SO_0002217)                                                                                                                                                                                                                                                                                  |
| `ZFIN:cvs`       |              1 | [UBERON:0000089](http://purl.obolibrary.org/obo/UBERON_0000089)                                                                                                                                                                                                                                                                          |
| `ZFIN:yb`        |              1 | [UBERON:0003066](http://purl.obolibrary.org/obo/UBERON_0003066)                                                                                                                                                                                                                                                                          |
| `ZFIN:090511-18` |              1 | [UBERON:2002145](http://purl.obolibrary.org/obo/UBERON_2002145)                                                                                                                                                                                                                                                                          |

## `zfin`: Zebrafish Information Network Gene

Overall, there were 1 invalid
xrefs to external prefixed with `zfin` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `zfin:curator`  |              1 | [UBERON:0008911](http://purl.obolibrary.org/obo/UBERON_0008911) |

