# enm

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `enm`.


## `AGR`: Agricultural Online Access

Overall, there were 6 invalid
xrefs to external prefixed with `AGR` (standardized to Bioregistry
prefix [`agricola`](https://bioregistry.io/agricola)) that
did not match the standard pattern `^\d+$`.

| external_xref     |   usages_count | usages                                                      |
|-------------------|----------------|-------------------------------------------------------------|
| `AGR:IND84086009` |              1 | [CHEBI:136643](http://purl.obolibrary.org/obo/CHEBI_136643) |
| `AGR:IND20386178` |              1 | [CHEBI:136644](http://purl.obolibrary.org/obo/CHEBI_136644) |
| `AGR:IND84086011` |              1 | [CHEBI:136644](http://purl.obolibrary.org/obo/CHEBI_136644) |
| `AGR:IND89021681` |              1 | [CHEBI:136644](http://purl.obolibrary.org/obo/CHEBI_136644) |
| `AGR:IND92003154` |              1 | [CHEBI:136644](http://purl.obolibrary.org/obo/CHEBI_136644) |
| `AGR:IND43789627` |              1 | [CHEBI:136646](http://purl.obolibrary.org/obo/CHEBI_136646) |

## `CARO`: Common Anatomy Reference Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `CARO` (standardized to Bioregistry
prefix [`caro`](https://bioregistry.io/caro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                           |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `CARO:mah`      |              2 | [CL:0000000](http://purl.obolibrary.org/obo/CL_0000000), [CL:0000003](http://purl.obolibrary.org/obo/CL_0000003) |

## `CAS`: CAS Registry Number

Overall, there were 2 invalid
xrefs to external prefixed with `CAS` (standardized to Bioregistry
prefix [`cas`](https://bioregistry.io/cas)) that
did not match the standard pattern `^\d{1,7}\-\d{2}\-\d$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `CAS:1583915`   |              1 | [EFO:0022198](http://www.ebi.ac.uk/efo/EFO_0022198) |
| `CAS:5466678`   |              1 | [EFO:0022199](http://www.ebi.ac.uk/efo/EFO_0022199) |

## `doi`: Digital Object Identifier

Overall, there were 1 invalid
xrefs to external prefixed with `doi` (standardized to Bioregistry
prefix [`doi`](https://bioregistry.io/doi)) that
did not match the standard pattern `^10.\d{2,9}/.*$`.

| external_xref            |   usages_count | usages                                              |
|--------------------------|----------------|-----------------------------------------------------|
| `doi: 10.1111/nmo.12871` |              1 | [EFO:0011032](http://www.ebi.ac.uk/efo/EFO_0011032) |

## `FAO`: Fungal gross anatomy

Overall, there were 27 invalid
xrefs to external prefixed with `FAO` (standardized to Bioregistry
prefix [`fao`](https://bioregistry.io/fao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                                             |   usages_count | usages                                                                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FAO:http://fao.org/ag/agl/agll/wrb/doc/wrb2006final.pdf` |             27 | [ENVO:00002229](http://purl.obolibrary.org/obo/ENVO_00002229), [ENVO:00002231](http://purl.obolibrary.org/obo/ENVO_00002231), [ENVO:00002233](http://purl.obolibrary.org/obo/ENVO_00002233), [ENVO:00002234](http://purl.obolibrary.org/obo/ENVO_00002234), [ENVO:00002235](http://purl.obolibrary.org/obo/ENVO_00002235), ... |

## `FBtc`: Flybase Cell Line

Overall, there were 3 invalid
xrefs to external prefixed with `FBtc` (standardized to Bioregistry
prefix [`fbtc`](https://bioregistry.io/fbtc)) that
did not match the standard pattern `^\d{7}$`.

| external_xref      |   usages_count | usages                                              |
|--------------------|----------------|-----------------------------------------------------|
| `FBtc:FBtc0000151` |              1 | [EFO:0005743](http://www.ebi.ac.uk/efo/EFO_0005743) |
| `FBtc:FBtc0000155` |              1 | [EFO:0005744](http://www.ebi.ac.uk/efo/EFO_0005744) |
| `FBtc:FBtc0000191` |              1 | [EFO:0005745](http://www.ebi.ac.uk/efo/EFO_0005745) |

## `Geonames`: GeoNames

Overall, there were 4 invalid
xrefs to external prefixed with `Geonames` (standardized to Bioregistry
prefix [`geonames`](https://bioregistry.io/geonames)) that
did not match the standard pattern `^\d+$`.

| external_xref      |   usages_count | usages                                                        |
|--------------------|----------------|---------------------------------------------------------------|
| `Geonames:feature` |              1 | [ENVO:00000194](http://purl.obolibrary.org/obo/ENVO_00000194) |
| `Geonames:T.TAL`   |              1 | [ENVO:00000194](http://purl.obolibrary.org/obo/ENVO_00000194) |
| `Geonames:T.RK`    |              1 | [ENVO:00001995](http://purl.obolibrary.org/obo/ENVO_00001995) |
| `Geonames:T.RKS`   |              1 | [ENVO:00001995](http://purl.obolibrary.org/obo/ENVO_00001995) |

## `Gmelin`: Gmelins Handbuch der anorganischen Chemie

Overall, there were 1 invalid
xrefs to external prefixed with `Gmelin` (standardized to Bioregistry
prefix [`gmelin`](https://bioregistry.io/gmelin)) that
did not match the standard pattern `^[1-9][0-9]{3,6}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `Gmelin:485`    |              1 | [CHEBI:15379](http://purl.obolibrary.org/obo/CHEBI_15379) |

## `HMDB`: Human Metabolome Database

Overall, there were 85 invalid
xrefs to external prefixed with `HMDB` (standardized to Bioregistry
prefix [`hmdb`](https://bioregistry.io/hmdb)) that
did not match the standard pattern `^HMDB\d+$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `HMDB:0031682`  |              1 | [EFO:0803383](http://www.ebi.ac.uk/efo/EFO_0803383) |
| `HMDB:0000958`  |              1 | [EFO:0803384](http://www.ebi.ac.uk/efo/EFO_0803384) |
| `HMDB:0035590`  |              1 | [EFO:0803385](http://www.ebi.ac.uk/efo/EFO_0803385) |
| `HMDB:0062477`  |              1 | [EFO:0803386](http://www.ebi.ac.uk/efo/EFO_0803386) |
| `HMDB:0000634`  |              1 | [EFO:0803387](http://www.ebi.ac.uk/efo/EFO_0803387) |
| `HMDB:0037285`  |              1 | [EFO:0803388](http://www.ebi.ac.uk/efo/EFO_0803388) |
| `HMDB:0060745`  |              1 | [EFO:0803389](http://www.ebi.ac.uk/efo/EFO_0803389) |
| `HMDB:0039972`  |              1 | [EFO:0803390](http://www.ebi.ac.uk/efo/EFO_0803390) |
| `HMDB:0032802`  |              1 | [EFO:0803391](http://www.ebi.ac.uk/efo/EFO_0803391) |
| `HMDB:0039133`  |              1 | [EFO:0803392](http://www.ebi.ac.uk/efo/EFO_0803392) |
| `HMDB:0059993`  |              1 | [EFO:0803393](http://www.ebi.ac.uk/efo/EFO_0803393) |
| `HMDB:0059784`  |              1 | [EFO:0803394](http://www.ebi.ac.uk/efo/EFO_0803394) |
| `HMDB:0000472`  |              1 | [EFO:0803395](http://www.ebi.ac.uk/efo/EFO_0803395) |
| `HMDB:0032822`  |              1 | [EFO:0803396](http://www.ebi.ac.uk/efo/EFO_0803396) |
| `HMDB:0037146`  |              1 | [EFO:0803397](http://www.ebi.ac.uk/efo/EFO_0803397) |
| `HMDB:0034022`  |              1 | [EFO:0803398](http://www.ebi.ac.uk/efo/EFO_0803398) |
| `HMDB:0031885`  |              1 | [EFO:0803399](http://www.ebi.ac.uk/efo/EFO_0803399) |
| `HMDB:0000446`  |              1 | [EFO:0803400](http://www.ebi.ac.uk/efo/EFO_0803400) |
| `HMDB:0015554`  |              1 | [EFO:0803401](http://www.ebi.ac.uk/efo/EFO_0803401) |
| `HMDB:0000194`  |              1 | [EFO:0803402](http://www.ebi.ac.uk/efo/EFO_0803402) |
| `HMDB:0002212`  |              1 | [EFO:0803403](http://www.ebi.ac.uk/efo/EFO_0803403) |
| `HMDB:0032173`  |              1 | [EFO:0803404](http://www.ebi.ac.uk/efo/EFO_0803404) |
| `HMDB:0041188`  |              1 | [EFO:0803405](http://www.ebi.ac.uk/efo/EFO_0803405) |
| `HMDB:0002322`  |              1 | [EFO:0803406](http://www.ebi.ac.uk/efo/EFO_0803406) |
| `HMDB:0000567`  |              1 | [EFO:0803407](http://www.ebi.ac.uk/efo/EFO_0803407) |
| `HMDB:0002035`  |              1 | [EFO:0803408](http://www.ebi.ac.uk/efo/EFO_0803408) |
| `HMDB:0035701`  |              1 | [EFO:0803409](http://www.ebi.ac.uk/efo/EFO_0803409) |
| `HMDB:0001413`  |              1 | [EFO:0803410](http://www.ebi.ac.uk/efo/EFO_0803410) |
| `HMDB:0000905`  |              1 | [EFO:0803411](http://www.ebi.ac.uk/efo/EFO_0803411) |
| `HMDB:0037173`  |              1 | [EFO:0803412](http://www.ebi.ac.uk/efo/EFO_0803412) |
| `HMDB:0001370`  |              1 | [EFO:0803413](http://www.ebi.ac.uk/efo/EFO_0803413) |
| `HMDB:0032216`  |              1 | [EFO:0803414](http://www.ebi.ac.uk/efo/EFO_0803414) |
| `HMDB:0002226`  |              1 | [EFO:0803415](http://www.ebi.ac.uk/efo/EFO_0803415) |
| `HMDB:0000954`  |              1 | [EFO:0803416](http://www.ebi.ac.uk/efo/EFO_0803416) |
| `HMDB:0001254`  |              1 | [EFO:0803417](http://www.ebi.ac.uk/efo/EFO_0803417) |
| `HMDB:0001514`  |              1 | [EFO:0803418](http://www.ebi.ac.uk/efo/EFO_0803418) |
| `HMDB:0031089`  |              1 | [EFO:0803419](http://www.ebi.ac.uk/efo/EFO_0803419) |
| `HMDB:0002259`  |              1 | [EFO:0803420](http://www.ebi.ac.uk/efo/EFO_0803420) |
| `HMDB:0000130`  |              1 | [EFO:0803421](http://www.ebi.ac.uk/efo/EFO_0803421) |
| `HMDB:0060039`  |              1 | [EFO:0803422](http://www.ebi.ac.uk/efo/EFO_0803422) |
| `HMDB:0003447`  |              1 | [EFO:0803423](http://www.ebi.ac.uk/efo/EFO_0803423) |
| `HMDB:0060001`  |              1 | [EFO:0803424](http://www.ebi.ac.uk/efo/EFO_0803424) |
| `HMDB:0003335`  |              1 | [EFO:0803425](http://www.ebi.ac.uk/efo/EFO_0803425) |
| `HMDB:0002250`  |              1 | [EFO:0803426](http://www.ebi.ac.uk/efo/EFO_0803426) |
| `HMDB:0035372`  |              1 | [EFO:0803427](http://www.ebi.ac.uk/efo/EFO_0803427) |
| `HMDB:0011482`  |              1 | [EFO:0803428](http://www.ebi.ac.uk/efo/EFO_0803428) |
| `HMDB:0035068`  |              1 | [EFO:0803429](http://www.ebi.ac.uk/efo/EFO_0803429) |
| `HMDB:0029598`  |              1 | [EFO:0803430](http://www.ebi.ac.uk/efo/EFO_0803430) |
| `HMDB:0036583`  |              1 | [EFO:0803431](http://www.ebi.ac.uk/efo/EFO_0803431) |
| `HMDB:0011561`  |              1 | [EFO:0803432](http://www.ebi.ac.uk/efo/EFO_0803432) |
| `HMDB:0011567`  |              1 | [EFO:0803433](http://www.ebi.ac.uk/efo/EFO_0803433) |
| `HMDB:0013250`  |              1 | [EFO:0803434](http://www.ebi.ac.uk/efo/EFO_0803434) |
| `HMDB:0033442`  |              1 | [EFO:0803435](http://www.ebi.ac.uk/efo/EFO_0803435) |
| `HMDB:0041537`  |              1 | [EFO:0803436](http://www.ebi.ac.uk/efo/EFO_0803436) |
| `HMDB:0061051`  |              1 | [EFO:0803437](http://www.ebi.ac.uk/efo/EFO_0803437) |
| `HMDB:0032740`  |              1 | [EFO:0803438](http://www.ebi.ac.uk/efo/EFO_0803438) |
| `HMDB:0033438`  |              1 | [EFO:0803439](http://www.ebi.ac.uk/efo/EFO_0803439) |
| `HMDB:0013287`  |              1 | [EFO:0803440](http://www.ebi.ac.uk/efo/EFO_0803440) |
| `HMDB:0001132`  |              1 | [EFO:0803441](http://www.ebi.ac.uk/efo/EFO_0803441) |
| `HMDB:0002059`  |              1 | [EFO:0803442](http://www.ebi.ac.uk/efo/EFO_0803442) |
| `HMDB:0000225`  |              1 | [EFO:0803443](http://www.ebi.ac.uk/efo/EFO_0803443) |
| `HMDB:0029239`  |              1 | [EFO:0803444](http://www.ebi.ac.uk/efo/EFO_0803444) |
| `HMDB:0029803`  |              1 | [EFO:0803445](http://www.ebi.ac.uk/efo/EFO_0803445) |
| `HMDB:0030527`  |              1 | [EFO:0803446](http://www.ebi.ac.uk/efo/EFO_0803446) |
| `HMDB:0031149`  |              1 | [EFO:0803447](http://www.ebi.ac.uk/efo/EFO_0803447) |
| `HMDB:0001565`  |              1 | [EFO:0803448](http://www.ebi.ac.uk/efo/EFO_0803448) |
| `HMDB:0000272`  |              1 | [EFO:0803449](http://www.ebi.ac.uk/efo/EFO_0803449) |
| `HMDB:0032472`  |              1 | [EFO:0803450](http://www.ebi.ac.uk/efo/EFO_0803450) |
| `HMDB:0003072`  |              1 | [EFO:0803451](http://www.ebi.ac.uk/efo/EFO_0803451) |
| `HMDB:0015436`  |              1 | [EFO:0803452](http://www.ebi.ac.uk/efo/EFO_0803452) |
| `HMDB:0035802`  |              1 | [EFO:0803453](http://www.ebi.ac.uk/efo/EFO_0803453) |
| `HMDB:0038140`  |              1 | [EFO:0803454](http://www.ebi.ac.uk/efo/EFO_0803454) |
| `HMDB:0038585`  |              1 | [EFO:0803455](http://www.ebi.ac.uk/efo/EFO_0803455) |
| `HMDB:0029890`  |              1 | [EFO:0803456](http://www.ebi.ac.uk/efo/EFO_0803456) |
| `HMDB:0000996`  |              1 | [EFO:0803457](http://www.ebi.ac.uk/efo/EFO_0803457) |
| `HMDB:0005792`  |              1 | [EFO:0803458](http://www.ebi.ac.uk/efo/EFO_0803458) |
| `HMDB:0000757`  |              1 | [EFO:0803459](http://www.ebi.ac.uk/efo/EFO_0803459) |
| `HMDB:0060412`  |              1 | [EFO:0803460](http://www.ebi.ac.uk/efo/EFO_0803460) |
| `HMDB:0040824`  |              1 | [EFO:0803461](http://www.ebi.ac.uk/efo/EFO_0803461) |
| `HMDB:0041785`  |              1 | [EFO:0803462](http://www.ebi.ac.uk/efo/EFO_0803462) |
| `HMDB:0000881`  |              1 | [EFO:0803463](http://www.ebi.ac.uk/efo/EFO_0803463) |
| `HMDB:0000208`  |              1 | [EFO:0803464](http://www.ebi.ac.uk/efo/EFO_0803464) |
| `HMDB:0041919`  |              1 | [EFO:0803465](http://www.ebi.ac.uk/efo/EFO_0803465) |
| `HMDB:0001852`  |              1 | [EFO:0803466](http://www.ebi.ac.uk/efo/EFO_0803466) |
| `HMDB:0001934`  |              1 | [EFO:0803467](http://www.ebi.ac.uk/efo/EFO_0803467) |

## `HPA`: Human Protein Atlas tissue profile information

Overall, there were 1 invalid
xrefs to external prefixed with `HPA` (standardized to Bioregistry
prefix [`hpa`](https://bioregistry.io/hpa)) that
did not match the standard pattern `^ENSG\d{11}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `HPA:HPA`       |              1 | [CL:1001603](http://purl.obolibrary.org/obo/CL_1001603) |

## `ICD9`: International Classification of Diseases, 9th Revision

Overall, there were 3 invalid
xrefs to external prefixed with `ICD9` (standardized to Bioregistry
prefix [`icd9`](https://bioregistry.io/icd9)) that
did not match the standard pattern `^(\d\d\d|V\d\d|E[8-9]\d\d)(\.\d{1,2})?$`.

| external_xref     |   usages_count | usages                                              |
|-------------------|----------------|-----------------------------------------------------|
| `ICD9:89.52`      |              1 | [EFO:0004327](http://www.ebi.ac.uk/efo/EFO_0004327) |
| `ICD9:V85-V85.99` |              1 | [EFO:0004340](http://www.ebi.ac.uk/efo/EFO_0004340) |
| `ICD9:V86-V86.99` |              1 | [EFO:0005512](http://www.ebi.ac.uk/efo/EFO_0005512) |

## `LANGUAL`: Langua aLimentaria Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `LANGUAL` (standardized to Bioregistry
prefix [`langual`](https://bioregistry.io/langual)) that
did not match the standard pattern `^B\d+$`.

| external_xref   |   usages_count | usages                                                            |
|-----------------|----------------|-------------------------------------------------------------------|
| `LANGUAL:C0195` |              1 | [FOODON:00001216](http://purl.obolibrary.org/obo/FOODON_00001216) |

## `MA`: Mouse adult gross anatomy

Overall, there were 11 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
prefix [`ma`](https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                         |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MA:ma`         |             11 | [ENVO:00000447](http://purl.obolibrary.org/obo/ENVO_00000447), [ENVO:00000873](http://purl.obolibrary.org/obo/ENVO_00000873), [ENVO:00001995](http://purl.obolibrary.org/obo/ENVO_00001995), [ENVO:00002006](http://purl.obolibrary.org/obo/ENVO_00002006), [ENVO:00002047](http://purl.obolibrary.org/obo/ENVO_00002047), ... |

## `MedDRA`: Medical Dictionary for Regulatory Activities Terminology

Overall, there were 1 invalid
xrefs to external prefixed with `MedDRA` (standardized to Bioregistry
prefix [`meddra`](https://bioregistry.io/meddra)) that
did not match the standard pattern `^\d+$`.

| external_xref            |   usages_count | usages                                              |
|--------------------------|----------------|-----------------------------------------------------|
| `MedDRA:1005MedDRA:1006` |              1 | [EFO:0009248](http://www.ebi.ac.uk/efo/EFO_0009248) |

## `MeSH`: Medical Subject Headings

Overall, there were 1 invalid
xrefs to external prefixed with `MeSH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `MeSH:Q000401`  |              1 | [EFO:0004352](http://www.ebi.ac.uk/efo/EFO_0004352) |

## `MGI`: Mouse Genome Informatics

Overall, there were 1 invalid
xrefs to external prefixed with `MGI` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `MGI:csmith`    |              1 | [UBERON:0002530](http://purl.obolibrary.org/obo/UBERON_0002530) |

## `NIFSTD`: NIF Standard Ontology

Overall, there were 6 invalid
xrefs to external prefixed with `NIFSTD` (standardized to Bioregistry
prefix [`nif.std`](https://bioregistry.io/nif.std)) that
did not match the standard pattern `^BAMSC\d+$`.

| external_xref         |   usages_count | usages                                              |
|-----------------------|----------------|-----------------------------------------------------|
| `NIFSTD:birnlex_2052` |              1 | [EFO:0000433](http://www.ebi.ac.uk/efo/EFO_0000433) |
| `NIFSTD:birnlex_2023` |              1 | [EFO:0000513](http://www.ebi.ac.uk/efo/EFO_0000513) |
| `NIFSTD:birnlex_228`  |              1 | [EFO:0001272](http://www.ebi.ac.uk/efo/EFO_0001272) |
| `NIFSTD:birnlex_681`  |              1 | [EFO:0001272](http://www.ebi.ac.uk/efo/EFO_0001272) |
| `NIFSTD:sao279801585` |              1 | [EFO:0001444](http://www.ebi.ac.uk/efo/EFO_0001444) |
| `NIFSTD:birnlex_2117` |              1 | [EFO:0002694](http://www.ebi.ac.uk/efo/EFO_0002694) |

## `OBO_REL`: Relation Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `OBO_REL` (standardized to Bioregistry
prefix [`ro`](https://bioregistry.io/ro)) that
did not match the standard pattern `^(HOM)?\d{7}$`.

| external_xref      |   usages_count | usages                                                      |
|--------------------|----------------|-------------------------------------------------------------|
| `OBO_REL:has_part` |              1 | [PATO:0001555](http://purl.obolibrary.org/obo/PATO_0001555) |

## `PATO`: Phenotype And Trait Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `PATO` (standardized to Bioregistry
prefix [`pato`](https://bioregistry.io/pato)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                          |
|-----------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PATO:GVG`      |              5 | [PATO:0000911](http://purl.obolibrary.org/obo/PATO_0000911), [PATO:0000912](http://purl.obolibrary.org/obo/PATO_0000912), [PATO:0001596](http://purl.obolibrary.org/obo/PATO_0001596), [PATO:0001663](http://purl.obolibrary.org/obo/PATO_0001663), [PATO:0001664](http://purl.obolibrary.org/obo/PATO_0001664) |
| `PATO:DS`       |              1 | [PATO:0002390](http://purl.obolibrary.org/obo/PATO_0002390)                                                                                                                                                                                                                                                     |
| `PATO:MAH`      |              1 | [PATO:0002632](http://purl.obolibrary.org/obo/PATO_0002632)                                                                                                                                                                                                                                                     |

## `PMID`: PubMed

Overall, there were 6 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref     |   usages_count | usages                                              |
|-------------------|----------------|-----------------------------------------------------|
| `PMID:PMC1531688` |              1 | [EFO:0005725](http://www.ebi.ac.uk/efo/EFO_0005725) |
| `PMID: 3897439`   |              1 | [EFO:0005910](http://www.ebi.ac.uk/efo/EFO_0005910) |
| `PMID: 8788275`   |              1 | [EFO:0005913](http://www.ebi.ac.uk/efo/EFO_0005913) |
| `PMID:27149984 `  |              1 | [EFO:0007836](http://www.ebi.ac.uk/efo/EFO_0007836) |
| `PMID: 31636452`  |              1 | [EFO:0010605](http://www.ebi.ac.uk/efo/EFO_0010605) |
| `PMID: 32355309`  |              1 | [EFO:0010749](http://www.ebi.ac.uk/efo/EFO_0010749) |

## `ReO`: Reagent Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `ReO` (standardized to Bioregistry
prefix [`reo`](https://bioregistry.io/reo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                           |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `ReO:mhb`       |              2 | [CL:0000010](http://purl.obolibrary.org/obo/CL_0000010), [CL:0001034](http://purl.obolibrary.org/obo/CL_0001034) |

## `SO`: Sequence types and features ontology

Overall, there were 1 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                          |
|-----------------|----------------|-------------------------------------------------------------------------------------------------|
| `SO:cjm`        |              1 | [uberon#spatially:disjoint:from](http://purl.obolibrary.org/obo/uberon#spatially_disjoint_from) |

## `UBERON`: Uber Anatomy Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `UBERON` (standardized to Bioregistry
prefix [`uberon`](https://bioregistry.io/uberon)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `UBERON:cjm`    |              1 | [UBERON:0006925](http://purl.obolibrary.org/obo/UBERON_0006925) |

## `WWF`: World Wildlife Fund Ecoregion

Overall, there were 13 invalid
xrefs to external prefixed with `WWF` (standardized to Bioregistry
prefix [`wwf.ecoregion`](https://bioregistry.io/wwf.ecoregion)) that
did not match the standard pattern `^AT\d+$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `WWF:Biome`     |              1 | [ENVO:00000428](http://purl.obolibrary.org/obo/ENVO_00000428) |
| `WWF:AA1310`    |              1 | [ENVO:01001569](http://purl.obolibrary.org/obo/ENVO_01001569) |
| `WWF:AA1309`    |              1 | [ENVO:01001572](http://purl.obolibrary.org/obo/ENVO_01001572) |
| `WWF:AA1308`    |              1 | [ENVO:01001573](http://purl.obolibrary.org/obo/ENVO_01001573) |
| `WWF:AA1307`    |              1 | [ENVO:01001574](http://purl.obolibrary.org/obo/ENVO_01001574) |
| `WWF:AA1301`    |              1 | [ENVO:01001575](http://purl.obolibrary.org/obo/ENVO_01001575) |
| `WWF:AA1302`    |              1 | [ENVO:01001576](http://purl.obolibrary.org/obo/ENVO_01001576) |
| `WWF:AA1303`    |              1 | [ENVO:01001577](http://purl.obolibrary.org/obo/ENVO_01001577) |
| `WWF:AA1304`    |              1 | [ENVO:01001578](http://purl.obolibrary.org/obo/ENVO_01001578) |
| `WWF:AA1305`    |              1 | [ENVO:01001579](http://purl.obolibrary.org/obo/ENVO_01001579) |
| `WWF:AA1306`    |              1 | [ENVO:01001580](http://purl.obolibrary.org/obo/ENVO_01001580) |
| `WWF:IM1304`    |              1 | [ENVO:01001627](http://purl.obolibrary.org/obo/ENVO_01001627) |
| `WWF:IM1303`    |              1 | [ENVO:01001628](http://purl.obolibrary.org/obo/ENVO_01001628) |

