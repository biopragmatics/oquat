# efo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `efo`. See the [GitHub repository](https://github.com/EBISPOT/efo/).


## `BTO`: BRENDA Tissue Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `BTO` (standardized to Bioregistry
prefix [`bto`](https://bioregistry.io/bto)) that
did not match the standard pattern `^\d{7}$`.

| external_xref               |   usages_count | usages                                              |
|-----------------------------|----------------|-----------------------------------------------------|
| `BTO:0002522 `              |              1 | [EFO:0022408](http://www.ebi.ac.uk/efo/EFO_0022408) |
| `BTO:0005715; PMID:7520026` |              1 | [EFO:0022452](http://www.ebi.ac.uk/efo/EFO_0022452) |

## `CAS`: CAS Registry Number

Overall, there were 2 invalid
xrefs to external prefixed with `CAS` (standardized to Bioregistry
prefix [`cas`](https://bioregistry.io/cas)) that
did not match the standard pattern `^\d{1,7}\-\d{2}\-\d$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `CAS:1583915`   |              1 | [EFO:0022198](http://www.ebi.ac.uk/efo/EFO_0022198) |
| `CAS:5466678`   |              1 | [EFO:0022199](http://www.ebi.ac.uk/efo/EFO_0022199) |

## `DI`: UniProt Diseases

Overall, there were 1 invalid
xrefs to external prefixed with `DI` (standardized to Bioregistry
prefix [`uniprot.disease`](https://bioregistry.io/uniprot.disease)) that
did not match the standard pattern `^DI-\d{5}$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `DI:00917`      |              1 | [EFO:0010956](http://www.ebi.ac.uk/efo/EFO_0010956) |

## `doi`: Digital Object Identifier

Overall, there were 1 invalid
xrefs to external prefixed with `doi` (standardized to Bioregistry
prefix [`doi`](https://bioregistry.io/doi)) that
did not match the standard pattern `^10.\d{2,9}/.*$`.

| external_xref            |   usages_count | usages                                              |
|--------------------------|----------------|-----------------------------------------------------|
| `doi: 10.1111/nmo.12871` |              1 | [EFO:0011032](http://www.ebi.ac.uk/efo/EFO_0011032) |

## `FBdv`: Drosophila development

Overall, there were 1 invalid
xrefs to external prefixed with `FBdv` (standardized to Bioregistry
prefix [`fbdv`](https://bioregistry.io/fbdv)) that
did not match the standard pattern `^\d{8}$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `FBdv:0005333`  |              1 | [EFO:0001323](http://www.ebi.ac.uk/efo/EFO_0001323) |

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

## `ICD10`: International Classification of Diseases, 10th Revision

Overall, there were 50 invalid
xrefs to external prefixed with `ICD10` (standardized to Bioregistry
prefix [`icd10`](https://bioregistry.io/icd10)) that
did not match the standard pattern `^(([XVI]+)|([A-Z][0-9]+((-[A-Z][0-9]+)|(\.[0-9]))?))$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `ICD10:C91.10`  |              1 | [EFO:0000095](http://www.ebi.ac.uk/efo/EFO_0000095) |
| `ICD10:C91.00`  |              1 | [EFO:0000220](http://www.ebi.ac.uk/efo/EFO_0000220) |
| `ICD10:C91.90`  |              1 | [EFO:0000220](http://www.ebi.ac.uk/efo/EFO_0000220) |
| `ICD10:C92.00`  |              1 | [EFO:0000222](http://www.ebi.ac.uk/efo/EFO_0000222) |
| `ICD10:C92.40`  |              1 | [EFO:0000224](http://www.ebi.ac.uk/efo/EFO_0000224) |
| `ICD10:C83.70`  |              1 | [EFO:0000309](http://www.ebi.ac.uk/efo/EFO_0000309) |
| `ICD10:C95.90`  |              1 | [EFO:0000565](http://www.ebi.ac.uk/efo/EFO_0000565) |
| `ICD10:C00.D48` |              1 | [EFO:0000616](http://www.ebi.ac.uk/efo/EFO_0000616) |
| `ICD10:H11.00`  |              1 | [EFO:0000678](http://www.ebi.ac.uk/efo/EFO_0000678) |
| `ICD10:H11.009` |              1 | [EFO:0000678](http://www.ebi.ac.uk/efo/EFO_0000678) |
| `ICD10:J84.112` |              1 | [EFO:0000768](http://www.ebi.ac.uk/efo/EFO_0000768) |
| `ICD10:C34.90`  |              1 | [EFO:0001071](http://www.ebi.ac.uk/efo/EFO_0001071) |
| `ICD10:C90.00`  |              1 | [EFO:0001378](http://www.ebi.ac.uk/efo/EFO_0001378) |
| `ICD10:D10.D36` |              1 | [EFO:0002422](http://www.ebi.ac.uk/efo/EFO_0002422) |
| `ICD10:D75.81`  |              1 | [EFO:0002430](http://www.ebi.ac.uk/efo/EFO_0002430) |
| `ICD10:C94.20`  |              1 | [EFO:0003025](http://www.ebi.ac.uk/efo/EFO_0003025) |
| `ICD10:C90.10`  |              1 | [EFO:0006475](http://www.ebi.ac.uk/efo/EFO_0006475) |
| `ICD10:C90.30`  |              1 | [EFO:0006738](http://www.ebi.ac.uk/efo/EFO_0006738) |
| `ICD10:C94.30`  |              1 | [EFO:0007359](http://www.ebi.ac.uk/efo/EFO_0007359) |
| `ICD10:Q85.00`  |              1 | [EFO:0008514](http://www.ebi.ac.uk/efo/EFO_0008514) |
| `ICD10:R10.13`  |              1 | [EFO:0008533](http://www.ebi.ac.uk/efo/EFO_0008533) |
| `ICD10:351.8`   |              1 | [EFO:0009380](http://www.ebi.ac.uk/efo/EFO_0009380) |
| `ICD10:H53.30`  |              1 | [EFO:0009535](http://www.ebi.ac.uk/efo/EFO_0009535) |
| `ICD10:I85.01`  |              1 | [EFO:0009545](http://www.ebi.ac.uk/efo/EFO_0009545) |
| `ICD10:H00.H06` |              1 | [EFO:0009546](http://www.ebi.ac.uk/efo/EFO_0009546) |
| `ICD10:N40.N51` |              1 | [EFO:0009555](http://www.ebi.ac.uk/efo/EFO_0009555) |
| `ICD10:A69.22`  |              1 | [EFO:0009562](http://www.ebi.ac.uk/efo/EFO_0009562) |
| `ICD10:C95.00`  |              1 | [EFO:1000068](http://www.ebi.ac.uk/efo/EFO_1000068) |
| `ICD10:C93.30`  |              1 | [EFO:1000309](http://www.ebi.ac.uk/efo/EFO_1000309) |
| `ICD10:C64.C68` |              1 | [EFO:1000363](http://www.ebi.ac.uk/efo/EFO_1000363) |
| `ICD10:D18.00`  |              1 | [EFO:1000635](http://www.ebi.ac.uk/efo/EFO_1000635) |
| `ICD10:C84.10`  |              1 | [EFO:1000785](http://www.ebi.ac.uk/efo/EFO_1000785) |
| `ICD10:A50.06`  |              1 | [EFO:1000887](http://www.ebi.ac.uk/efo/EFO_1000887) |
| `ICD10:C91.40`  |              1 | [EFO:1000956](http://www.ebi.ac.uk/efo/EFO_1000956) |
| `ICD10:A81.81`  |              1 | [EFO:1001008](http://www.ebi.ac.uk/efo/EFO_1001008) |
| `ICD10:D72.823` |              1 | [EFO:1001014](http://www.ebi.ac.uk/efo/EFO_1001014) |
| `ICD10:C84.00`  |              1 | [EFO:1001051](http://www.ebi.ac.uk/efo/EFO_1001051) |
| `ICD10:C92.30`  |              1 | [EFO:1001052](http://www.ebi.ac.uk/efo/EFO_1001052) |
| `ICD10:A52.02`  |              1 | [EFO:1001206](http://www.ebi.ac.uk/efo/EFO_1001206) |
| `ICD10:K75.81`  |              1 | [EFO:1001249](http://www.ebi.ac.uk/efo/EFO_1001249) |
| `ICD10:J84.116` |              1 | [EFO:1001300](http://www.ebi.ac.uk/efo/EFO_1001300) |
| `ICD10:H47.14`  |              1 | [EFO:1001330](http://www.ebi.ac.uk/efo/EFO_1001330) |
| `ICD10:C51.C58` |              1 | [EFO:1001331](http://www.ebi.ac.uk/efo/EFO_1001331) |
| `ICD10:K76.81`  |              1 | [EFO:1001346](http://www.ebi.ac.uk/efo/EFO_1001346) |
| `ICD10:E75.24`  |              1 | [EFO:1001380](http://www.ebi.ac.uk/efo/EFO_1001380) |
| `ICD10:O43.01`  |              1 | [EFO:1001794](http://www.ebi.ac.uk/efo/EFO_1001794) |
| `ICD10:S52.27`  |              1 | [EFO:1001811](http://www.ebi.ac.uk/efo/EFO_1001811) |
| `ICD10:H05.12`  |              1 | [EFO:1001819](http://www.ebi.ac.uk/efo/EFO_1001819) |
| `ICD10:H11.15`  |              1 | [EFO:1001824](http://www.ebi.ac.uk/efo/EFO_1001824) |
| `ICD10:K68.12`  |              1 | [EFO:1001832](http://www.ebi.ac.uk/efo/EFO_1001832) |

## `ICD11`: International Classification of Diseases, 11th Revision (Foundation Component)

Overall, there were 1 invalid
xrefs to external prefixed with `ICD11` (standardized to Bioregistry
prefix [`icd11`](https://bioregistry.io/icd11)) that
did not match the standard pattern `^[1-9]\d*$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `ICD11:8C62`    |              1 | [EFO:0020094](http://www.ebi.ac.uk/efo/EFO_0020094) |

## `ICD9`: International Classification of Diseases, 9th Revision

Overall, there were 43 invalid
xrefs to external prefixed with `ICD9` (standardized to Bioregistry
prefix [`icd9`](https://bioregistry.io/icd9)) that
did not match the standard pattern `^(\d\d\d|V\d\d|E[8-9]\d\d)(\.\d{1,2})?$`.

| external_xref     |   usages_count | usages                                                                                                   |
|-------------------|----------------|----------------------------------------------------------------------------------------------------------|
| `ICD9:520-579.99` |              2 | [EFO:0000405](http://www.ebi.ac.uk/efo/EFO_0000405), [EFO:0009431](http://www.ebi.ac.uk/efo/EFO_0009431) |
| `ICD9:560-569.99` |              2 | [EFO:0000405](http://www.ebi.ac.uk/efo/EFO_0000405), [EFO:0009431](http://www.ebi.ac.uk/efo/EFO_0009431) |
| `ICD9:570-579.99` |              2 | [EFO:0000405](http://www.ebi.ac.uk/efo/EFO_0000405), [EFO:0009431](http://www.ebi.ac.uk/efo/EFO_0009431) |
| `ICD9:390-459.99` |              1 | [EFO:0000319](http://www.ebi.ac.uk/efo/EFO_0000319)                                                      |
| `ICD9:420-429.99` |              1 | [EFO:0000319](http://www.ebi.ac.uk/efo/EFO_0000319)                                                      |
| `ICD9:490-496.99` |              1 | [EFO:0000341](http://www.ebi.ac.uk/efo/EFO_0000341)                                                      |
| `ICD9:401-405.99` |              1 | [EFO:0000537](http://www.ebi.ac.uk/efo/EFO_0000537)                                                      |
| `ICD9:140-239.99` |              1 | [EFO:0000616](http://www.ebi.ac.uk/efo/EFO_0000616)                                                      |
| `ICD9:290-299.99` |              1 | [EFO:0000677](http://www.ebi.ac.uk/efo/EFO_0000677)                                                      |
| `ICD9:460-519.99` |              1 | [EFO:0000684](http://www.ebi.ac.uk/efo/EFO_0000684)                                                      |
| `ICD9:500-508.99` |              1 | [EFO:0000684](http://www.ebi.ac.uk/efo/EFO_0000684)                                                      |
| `ICD9:510-519.99` |              1 | [EFO:0000684](http://www.ebi.ac.uk/efo/EFO_0000684)                                                      |
| `ICD9:060-066.99` |              1 | [EFO:0000763](http://www.ebi.ac.uk/efo/EFO_0000763)                                                      |
| `ICD9:042-042.99` |              1 | [EFO:0000764](http://www.ebi.ac.uk/efo/EFO_0000764)                                                      |
| `ICD9:010-018.99` |              1 | [EFO:0000774](http://www.ebi.ac.uk/efo/EFO_0000774)                                                      |
| `ICD9:290-319.99` |              1 | [EFO:0001335](http://www.ebi.ac.uk/efo/EFO_0001335)                                                      |
| `ICD9:300-316.99` |              1 | [EFO:0001335](http://www.ebi.ac.uk/efo/EFO_0001335)                                                      |
| `ICD9:410-414.99` |              1 | [EFO:0001645](http://www.ebi.ac.uk/efo/EFO_0001645)                                                      |
| `ICD9:210-229.99` |              1 | [EFO:0002422](http://www.ebi.ac.uk/efo/EFO_0002422)                                                      |
| `ICD9:430-438.99` |              1 | [EFO:0003763](http://www.ebi.ac.uk/efo/EFO_0003763)                                                      |
| `ICD9:338-338.99` |              1 | [EFO:0003843](http://www.ebi.ac.uk/efo/EFO_0003843)                                                      |
| `ICD9:317-319.99` |              1 | [EFO:0003847](http://www.ebi.ac.uk/efo/EFO_0003847)                                                      |
| `ICD9:64.0`       |              1 | [EFO:0003953](http://www.ebi.ac.uk/efo/EFO_0003953)                                                      |
| `ICD9:89.52`      |              1 | [EFO:0004327](http://www.ebi.ac.uk/efo/EFO_0004327)                                                      |
| `ICD9:V85-V85.99` |              1 | [EFO:0004340](http://www.ebi.ac.uk/efo/EFO_0004340)                                                      |
| `ICD9:V86-V86.99` |              1 | [EFO:0005512](http://www.ebi.ac.uk/efo/EFO_0005512)                                                      |
| `ICD9:280-289.99` |              1 | [EFO:0005803](http://www.ebi.ac.uk/efo/EFO_0005803)                                                      |
| `ICD9:540-543.99` |              1 | [EFO:0007149](http://www.ebi.ac.uk/efo/EFO_0007149)                                                      |
| `ICD9:350-359.99` |              1 | [EFO:0009387](http://www.ebi.ac.uk/efo/EFO_0009387)                                                      |
| `ICD9:610-612.99` |              1 | [EFO:0009483](http://www.ebi.ac.uk/efo/EFO_0009483)                                                      |
| `ICD9:600-608.99` |              1 | [EFO:0009555](http://www.ebi.ac.uk/efo/EFO_0009555)                                                      |
| `ICD9:93.90`      |              1 | [EFO:0010719](http://www.ebi.ac.uk/efo/EFO_0010719)                                                      |
| `ICD9:96.7 `      |              1 | [EFO:0010720](http://www.ebi.ac.uk/efo/EFO_0010720)                                                      |
| `ICD9:33.5`       |              1 | [EFO:0010721](http://www.ebi.ac.uk/efo/EFO_0010721)                                                      |
| `ICD9:08-16`      |              1 | [EFO:0010722](http://www.ebi.ac.uk/efo/EFO_0010722)                                                      |
| `ICD9:240-246.99` |              1 | [EFO:1000627](http://www.ebi.ac.uk/efo/EFO_1000627)                                                      |
| `ICD9:390-392.99` |              1 | [EFO:1001160](http://www.ebi.ac.uk/efo/EFO_1001160)                                                      |
| `ICD9:120-129.99` |              1 | [EFO:1001342](http://www.ebi.ac.uk/efo/EFO_1001342)                                                      |
| `ICD9:614-616.99` |              1 | [EFO:1001388](http://www.ebi.ac.uk/efo/EFO_1001388)                                                      |
| `ICD9:209-209.99` |              1 | [EFO:1001901](http://www.ebi.ac.uk/efo/EFO_1001901)                                                      |

## `ICD9CM`: International Classification of Diseases, 9th Revision, Clinical Modification

Overall, there were 2 invalid
xrefs to external prefixed with `ICD9CM` (standardized to Bioregistry
prefix [`icd9cm`](https://bioregistry.io/icd9cm)) that
did not match the standard pattern `^([\dA-Z]\d{2}(\.\d{1,3}|))|(\d{2}(\.\d{1,2}|))$`.

| external_xref       |   usages_count | usages                                              |
|---------------------|----------------|-----------------------------------------------------|
| `ICD9CM:280-289.99` |              1 | [EFO:0005803](http://www.ebi.ac.uk/efo/EFO_0005803) |
| `ICD9CM:390-392.99` |              1 | [EFO:1001160](http://www.ebi.ac.uk/efo/EFO_1001160) |

## `ICDO`: International Classification of Diseases for Oncology

Overall, there were 5 invalid
xrefs to external prefixed with `ICDO` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref   |   usages_count | usages                                                                                                   |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------|
| `ICDO:0000/0`   |              2 | [EFO:1000159](http://www.ebi.ac.uk/efo/EFO_1000159), [EFO:1000508](http://www.ebi.ac.uk/efo/EFO_1000508) |
| `ICDO:M9861/3`  |              1 | [EFO:0000330](http://www.ebi.ac.uk/efo/EFO_0000330)                                                      |
| `ICDO:981-983`  |              1 | [EFO:0004289](http://www.ebi.ac.uk/efo/EFO_0004289)                                                      |
| `ICDO:8000/6`   |              1 | [EFO:0009709](http://www.ebi.ac.uk/efo/EFO_0009709)                                                      |

## `IDO`: Infectious Disease Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `IDO` (standardized to Bioregistry
prefix [`ido`](https://bioregistry.io/ido)) that
did not match the standard pattern `^\d{7}$`.

| external_xref     |   usages_count | usages                                              |
|-------------------|----------------|-----------------------------------------------------|
| `IDO:IDO_0000436` |              1 | [EFO:0005741](http://www.ebi.ac.uk/efo/EFO_0005741) |

## `JAX`: Jackson Laboratories Mouse Strain

Overall, there were 1 invalid
xrefs to external prefixed with `JAX` (standardized to Bioregistry
prefix [`jaxmice`](https://bioregistry.io/jaxmice)) that
did not match the standard pattern `^\d{6}$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `JAX:8075`      |              1 | [EFO:0001341](http://www.ebi.ac.uk/efo/EFO_0001341) |

## `KEGG`: Kyoto Encyclopedia of Genes and Genomes

Overall, there were 7 invalid
xrefs to external prefixed with `KEGG` (standardized to Bioregistry
prefix [`kegg`](https://bioregistry.io/kegg)) that
did not match the standard pattern `^([CHDEGTMKR]\d+)|(\w+:[\w\d\.-]*)|([a-z]{3,5})|(\w{2,4}\d{5})$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `KEGG:05221`    |              1 | [EFO:0000222](http://www.ebi.ac.uk/efo/EFO_0000222) |
| `KEGG:05220`    |              1 | [EFO:0000339](http://www.ebi.ac.uk/efo/EFO_0000339) |
| `KEGG:05222`    |              1 | [EFO:0000702](http://www.ebi.ac.uk/efo/EFO_0000702) |
| `KEGG:05218`    |              1 | [EFO:0000756](http://www.ebi.ac.uk/efo/EFO_0000756) |
| `KEGG:05215`    |              1 | [EFO:0001663](http://www.ebi.ac.uk/efo/EFO_0001663) |
| `KEGG:05223`    |              1 | [EFO:0003060](http://www.ebi.ac.uk/efo/EFO_0003060) |
| `KEGG:05210`    |              1 | [EFO:0005842](http://www.ebi.ac.uk/efo/EFO_0005842) |

## `MAXO`: Medical Action Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `MAXO` (standardized to Bioregistry
prefix [`maxo`](https://bioregistry.io/maxo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `MAXO:748`      |              1 | [EFO:0022844](http://www.ebi.ac.uk/efo/EFO_0022844) |

## `MedDRA`: Medical Dictionary for Regulatory Activities Terminology

Overall, there were 9 invalid
xrefs to external prefixed with `MedDRA` (standardized to Bioregistry
prefix [`meddra`](https://bioregistry.io/meddra)) that
did not match the standard pattern `^\d+$`.

| external_xref            |   usages_count | usages                                              |
|--------------------------|----------------|-----------------------------------------------------|
| `MedDRA:10020MedDRA:100` |              1 | [EFO:0003964](http://www.ebi.ac.uk/efo/EFO_0003964) |
| `MedDRA:100MedDRA:10022` |              1 | [EFO:0007213](http://www.ebi.ac.uk/efo/EFO_0007213) |
| `MedDRA:10045MedDRA:100` |              1 | [EFO:0007529](http://www.ebi.ac.uk/efo/EFO_0007529) |
| `MedDRA:1005MedDRA:1006` |              1 | [EFO:0009248](http://www.ebi.ac.uk/efo/EFO_0009248) |
| `MedDRA:1000MedDRA:1002` |              1 | [EFO:0009657](http://www.ebi.ac.uk/efo/EFO_0009657) |
| `MedDRA:C1535926`        |              1 | [EFO:0010642](http://www.ebi.ac.uk/efo/EFO_0010642) |
| `MedDRA:1001MedDRA:1007` |              1 | [EFO:1000879](http://www.ebi.ac.uk/efo/EFO_1000879) |
| `MedDRA:1001MedDRA:1009` |              1 | [EFO:1000879](http://www.ebi.ac.uk/efo/EFO_1000879) |
| `MedDRA:10049MedDRA:100` |              1 | [EFO:1001835](http://www.ebi.ac.uk/efo/EFO_1001835) |

## `MedGen`: Human Medical Genetics

Overall, there were 6 invalid
xrefs to external prefixed with `MedGen` (standardized to Bioregistry
prefix [`medgen`](https://bioregistry.io/medgen)) that
did not match the standard pattern `^(CN)?\d{2,7}$`.

| external_xref     |   usages_count | usages                                              |
|-------------------|----------------|-----------------------------------------------------|
| `MedGen:C1535926` |              1 | [EFO:0010642](http://www.ebi.ac.uk/efo/EFO_0010642) |
| `MedGen:C4748701` |              1 | [EFO:0010643](http://www.ebi.ac.uk/efo/EFO_0010643) |
| `MedGen:C4288261` |              1 | [EFO:0010647](http://www.ebi.ac.uk/efo/EFO_0010647) |
| `MedGen:C1864399` |              1 | [EFO:0010956](http://www.ebi.ac.uk/efo/EFO_0010956) |
| `MedGen:C1333600` |              1 | [EFO:0022911](http://www.ebi.ac.uk/efo/EFO_0022911) |
| `MedGen:C3502105` |              1 | [EFO:0022913](http://www.ebi.ac.uk/efo/EFO_0022913) |

## `Medgen`: Human Medical Genetics

Overall, there were 3 invalid
xrefs to external prefixed with `Medgen` (standardized to Bioregistry
prefix [`medgen`](https://bioregistry.io/medgen)) that
did not match the standard pattern `^(CN)?\d{2,7}$`.

| external_xref     |   usages_count | usages                                              |
|-------------------|----------------|-----------------------------------------------------|
| `Medgen:C0339526` |              1 | [EFO:0020026](http://www.ebi.ac.uk/efo/EFO_0020026) |
| `Medgen:C3887501` |              1 | [EFO:0020027](http://www.ebi.ac.uk/efo/EFO_0020027) |
| `Medgen:C3150597` |              1 | [EFO:0020031](http://www.ebi.ac.uk/efo/EFO_0020031) |

## `MEDGEN`: Human Medical Genetics

Overall, there were 1 invalid
xrefs to external prefixed with `MEDGEN` (standardized to Bioregistry
prefix [`medgen`](https://bioregistry.io/medgen)) that
did not match the standard pattern `^(CN)?\d{2,7}$`.

| external_xref     |   usages_count | usages                                              |
|-------------------|----------------|-----------------------------------------------------|
| `MEDGEN:C0002768` |              1 | [EFO:0022837](http://www.ebi.ac.uk/efo/EFO_0022837) |

## `MedlinePlus`: MedlinePlus Health Topics

Overall, there were 1 invalid
xrefs to external prefixed with `MedlinePlus` (standardized to Bioregistry
prefix [`medlineplus`](https://bioregistry.io/medlineplus)) that
did not match the standard pattern `^\d+$`.

| external_xref         |   usages_count | usages                                              |
|-----------------------|----------------|-----------------------------------------------------|
| `MedlinePlus: 001381` |              1 | [EFO:0000777](http://www.ebi.ac.uk/efo/EFO_0000777) |

## `MESH`: Medical Subject Headings

Overall, there were 11 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D|M)\d{6,9}$`.

| external_xref           |   usages_count | usages                                                                                                                                                        |
|-------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MESH:NoID`             |              3 | [EFO:0007233](http://www.ebi.ac.uk/efo/EFO_0007233), [EFO:0007422](http://www.ebi.ac.uk/efo/EFO_0007422), [EFO:0007441](http://www.ebi.ac.uk/efo/EFO_0007441) |
| `MESH:D014253-modified` |              1 | [EFO:0007523](http://www.ebi.ac.uk/efo/EFO_0007523)                                                                                                           |
| `MESH:D014323-modified` |              1 | [EFO:0007526](http://www.ebi.ac.uk/efo/EFO_0007526)                                                                                                           |
| `MESH:DO16518`          |              1 | [EFO:0004122](http://www.ebi.ac.uk/efo/EFO_0004122)                                                                                                           |
| `MESH:Q000401`          |              1 | [EFO:0004352](http://www.ebi.ac.uk/efo/EFO_0004352)                                                                                                           |
| `MESH:68062025`         |              1 | [EFO:0010581](http://www.ebi.ac.uk/efo/EFO_0010581)                                                                                                           |
| `MESH:Q000633`          |              1 | [EFO:0011061](http://www.ebi.ac.uk/efo/EFO_0011061)                                                                                                           |
| `MESH:130014`           |              1 | [EFO:0022194](http://www.ebi.ac.uk/efo/EFO_0022194)                                                                                                           |
| `MESH:DO14076`          |              1 | [EFO:1001216](http://www.ebi.ac.uk/efo/EFO_1001216)                                                                                                           |

## `MFO`: Medaka fish anatomy and development

Overall, there were 1 invalid
xrefs to external prefixed with `MFO` (standardized to Bioregistry
prefix [`mfo`](https://bioregistry.io/mfo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `MFO:000290`    |              1 | [EFO:0000791](http://www.ebi.ac.uk/efo/EFO_0000791) |

## `MONDO`: Mondo Disease Ontology

Overall, there were 1,717 invalid
xrefs to external prefixed with `MONDO` (standardized to Bioregistry
prefix [`mondo`](https://bioregistry.io/mondo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                                          |   usages_count | usages                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MONDO:patterns/location`                              |            619 | [EFO:0000178](http://www.ebi.ac.uk/efo/EFO_0000178), [EFO:0000181](http://www.ebi.ac.uk/efo/EFO_0000181), [EFO:0000182](http://www.ebi.ac.uk/efo/EFO_0000182), [EFO:0000191](http://www.ebi.ac.uk/efo/EFO_0000191), [EFO:0000199](http://www.ebi.ac.uk/efo/EFO_0000199), ... |
| `MONDO:design_pattern`                                 |            208 | [EFO:0000191](http://www.ebi.ac.uk/efo/EFO_0000191), [EFO:0000319](http://www.ebi.ac.uk/efo/EFO_0000319), [EFO:0000330](http://www.ebi.ac.uk/efo/EFO_0000330), [EFO:0000405](http://www.ebi.ac.uk/efo/EFO_0000405), [EFO:0000405](http://www.ebi.ac.uk/efo/EFO_0000405), ... |
| `MONDO:patterns/specific_infectious_disease_by_agent`  |            169 | [EFO:0000650](http://www.ebi.ac.uk/efo/EFO_0000650), [EFO:0000694](http://www.ebi.ac.uk/efo/EFO_0000694), [EFO:0000763](http://www.ebi.ac.uk/efo/EFO_0000763), [EFO:0000764](http://www.ebi.ac.uk/efo/EFO_0000764), [EFO:0000769](http://www.ebi.ac.uk/efo/EFO_0000769), ... |
| `MONDO:ambiguous`                                      |            157 | [EFO:0000217](http://www.ebi.ac.uk/efo/EFO_0000217), [EFO:0000220](http://www.ebi.ac.uk/efo/EFO_0000220), [EFO:0000248](http://www.ebi.ac.uk/efo/EFO_0000248), [EFO:0000275](http://www.ebi.ac.uk/efo/EFO_0000275), [EFO:0000284](http://www.ebi.ac.uk/efo/EFO_0000284), ... |
| `MONDO:patterns/location_top`                          |            110 | [EFO:0000319](http://www.ebi.ac.uk/efo/EFO_0000319), [EFO:0000405](http://www.ebi.ac.uk/efo/EFO_0000405), [EFO:0000512](http://www.ebi.ac.uk/efo/EFO_0000512), [EFO:0000540](http://www.ebi.ac.uk/efo/EFO_0000540), [EFO:0000618](http://www.ebi.ac.uk/efo/EFO_0000618), ... |
| `MONDO:Lexical`                                        |             79 | [EFO:0000095](http://www.ebi.ac.uk/efo/EFO_0000095), [EFO:0000174](http://www.ebi.ac.uk/efo/EFO_0000174), [EFO:0000181](http://www.ebi.ac.uk/efo/EFO_0000181), [EFO:0000198](http://www.ebi.ac.uk/efo/EFO_0000198), [EFO:0000222](http://www.ebi.ac.uk/efo/EFO_0000222), ... |
| `MONDO:patterns/neoplasm`                              |             67 | [EFO:0000294](http://www.ebi.ac.uk/efo/EFO_0000294), [EFO:0002431](http://www.ebi.ac.uk/efo/EFO_0002431), [EFO:0002626](http://www.ebi.ac.uk/efo/EFO_0002626), [EFO:0003769](http://www.ebi.ac.uk/efo/EFO_0003769), [EFO:0003817](http://www.ebi.ac.uk/efo/EFO_0003817), ... |
| `MONDO:patterns/inflammatory_disease_by_site`          |             61 | [EFO:0000217](http://www.ebi.ac.uk/efo/EFO_0000217), [EFO:0000278](http://www.ebi.ac.uk/efo/EFO_0000278), [EFO:0000465](http://www.ebi.ac.uk/efo/EFO_0000465), [EFO:0000557](http://www.ebi.ac.uk/efo/EFO_0000557), [EFO:0000649](http://www.ebi.ac.uk/efo/EFO_0000649), ... |
| `MONDO:patterns/carcinoma`                             |             50 | [EFO:0000178](http://www.ebi.ac.uk/efo/EFO_0000178), [EFO:0000182](http://www.ebi.ac.uk/efo/EFO_0000182), [EFO:0000216](http://www.ebi.ac.uk/efo/EFO_0000216), [EFO:0000305](http://www.ebi.ac.uk/efo/EFO_0000305), [EFO:0000501](http://www.ebi.ac.uk/efo/EFO_0000501), ... |
| `MONDO:patterns/cancer`                                |             44 | [EFO:0000178](http://www.ebi.ac.uk/efo/EFO_0000178), [EFO:0000326](http://www.ebi.ac.uk/efo/EFO_0000326), [EFO:0005088](http://www.ebi.ac.uk/efo/EFO_0005088), [EFO:0005553](http://www.ebi.ac.uk/efo/EFO_0005553), [EFO:0005557](http://www.ebi.ac.uk/efo/EFO_0005557), ... |
| `MONDO:patterns/chronic`                               |             16 | [EFO:0000337](http://www.ebi.ac.uk/efo/EFO_0000337), [EFO:0000339](http://www.ebi.ac.uk/efo/EFO_0000339), [EFO:0000341](http://www.ebi.ac.uk/efo/EFO_0000341), [EFO:0000342](http://www.ebi.ac.uk/efo/EFO_0000342), [EFO:0002428](http://www.ebi.ac.uk/efo/EFO_0002428), ... |
| `MONDO:LexicalVariant`                                 |             12 | [EFO:0000384](http://www.ebi.ac.uk/efo/EFO_0000384), [EFO:0003780](http://www.ebi.ac.uk/efo/EFO_0003780), [EFO:0005625](http://www.ebi.ac.uk/efo/EFO_0005625), [EFO:0005627](http://www.ebi.ac.uk/efo/EFO_0005627), [EFO:0005629](http://www.ebi.ac.uk/efo/EFO_0005629), ... |
| `MONDO:patterns/disease_series_by_gene`                |             11 | [EFO:0009071](http://www.ebi.ac.uk/efo/EFO_0009071), [EFO:0009301](http://www.ebi.ac.uk/efo/EFO_0009301), [EFO:1001333](http://www.ebi.ac.uk/efo/EFO_1001333), [EFO:1001501](http://www.ebi.ac.uk/efo/EFO_1001501), [EFO:1001501](http://www.ebi.ac.uk/efo/EFO_1001501), ... |
| `MONDO:patterns/infectious_disease_by_agent`           |             11 | [EFO:0000763](http://www.ebi.ac.uk/efo/EFO_0000763), [EFO:0004249](http://www.ebi.ac.uk/efo/EFO_0004249), [EFO:0007128](http://www.ebi.ac.uk/efo/EFO_0007128), [EFO:0007146](http://www.ebi.ac.uk/efo/EFO_0007146), [EFO:0007173](http://www.ebi.ac.uk/efo/EFO_0007173), ... |
| `MONDO:patterns/sarcoma`                               |             10 | [EFO:0000569](http://www.ebi.ac.uk/efo/EFO_0000569), [EFO:0000637](http://www.ebi.ac.uk/efo/EFO_0000637), [EFO:0002914](http://www.ebi.ac.uk/efo/EFO_0002914), [EFO:0002920](http://www.ebi.ac.uk/efo/EFO_0002920), [EFO:0003968](http://www.ebi.ac.uk/efo/EFO_0003968), ... |
| `MONDO:patterns/malignant`                             |             10 | [EFO:0005567](http://www.ebi.ac.uk/efo/EFO_0005567), [EFO:0008545](http://www.ebi.ac.uk/efo/EFO_0008545), [EFO:1000124](http://www.ebi.ac.uk/efo/EFO_1000124), [EFO:1000348](http://www.ebi.ac.uk/efo/EFO_1000348), [EFO:1000352](http://www.ebi.ac.uk/efo/EFO_1000352), ... |
| `MONDO:patterns/hereditary`                            |              9 | [EFO:0000508](http://www.ebi.ac.uk/efo/EFO_0000508), [EFO:0001356](http://www.ebi.ac.uk/efo/EFO_0001356), [EFO:0001356](http://www.ebi.ac.uk/efo/EFO_0001356), [EFO:0002945](http://www.ebi.ac.uk/efo/EFO_0002945), [EFO:0002945](http://www.ebi.ac.uk/efo/EFO_0002945), ... |
| `MONDO:patterns/basis_in_disruption_of_process`        |              8 | [EFO:0000589](http://www.ebi.ac.uk/efo/EFO_0000589), [EFO:0000677](http://www.ebi.ac.uk/efo/EFO_0000677), [EFO:0000677](http://www.ebi.ac.uk/efo/EFO_0000677), [EFO:0005269](http://www.ebi.ac.uk/efo/EFO_0005269), [EFO:0008499](http://www.ebi.ac.uk/efo/EFO_0008499), ... |
| `MONDO:patterns/neuroendocrine_neoplasm_grade1`        |              8 | [EFO:1000092](http://www.ebi.ac.uk/efo/EFO_1000092), [EFO:1000094](http://www.ebi.ac.uk/efo/EFO_1000094), [EFO:1000154](http://www.ebi.ac.uk/efo/EFO_1000154), [EFO:1000188](http://www.ebi.ac.uk/efo/EFO_1000188), [EFO:1000195](http://www.ebi.ac.uk/efo/EFO_1000195), ... |
| `MONDO:patterns/acute`                                 |              7 | [EFO:0000220](http://www.ebi.ac.uk/efo/EFO_0000220), [EFO:0000221](http://www.ebi.ac.uk/efo/EFO_0000221), [EFO:0000222](http://www.ebi.ac.uk/efo/EFO_0000222), [EFO:0002497](http://www.ebi.ac.uk/efo/EFO_0002497), [EFO:0008583](http://www.ebi.ac.uk/efo/EFO_0008583), ... |
| `MONDO:patterns/allergic_form_of_disease`              |              5 | [EFO:0000274](http://www.ebi.ac.uk/efo/EFO_0000274), [EFO:0005854](http://www.ebi.ac.uk/efo/EFO_0005854), [EFO:0007141](http://www.ebi.ac.uk/efo/EFO_0007141), [EFO:1000668](http://www.ebi.ac.uk/efo/EFO_1000668), [EFO:1000669](http://www.ebi.ac.uk/efo/EFO_1000669)      |
| `MONDO:patterns/benign`                                |              5 | [EFO:0002422](http://www.ebi.ac.uk/efo/EFO_0002422), [EFO:1000028](http://www.ebi.ac.uk/efo/EFO_1000028), [EFO:1000106](http://www.ebi.ac.uk/efo/EFO_1000106), [EFO:1000108](http://www.ebi.ac.uk/efo/EFO_1000108), [EFO:1000485](http://www.ebi.ac.uk/efo/EFO_1000485)      |
| `MONDO:patterns/environmental_stimulus`                |              5 | [EFO:0004712](http://www.ebi.ac.uk/efo/EFO_0004712), [EFO:0007153](http://www.ebi.ac.uk/efo/EFO_0007153), [EFO:1000814](http://www.ebi.ac.uk/efo/EFO_1000814), [EFO:1000851](http://www.ebi.ac.uk/efo/EFO_1000851), [EFO:1001890](http://www.ebi.ac.uk/efo/EFO_1001890)      |
| `MONDO:patterns/acquired`                              |              4 | [EFO:1000639](http://www.ebi.ac.uk/efo/EFO_1000639), [EFO:1000639](http://www.ebi.ac.uk/efo/EFO_1000639), [EFO:1000663](http://www.ebi.ac.uk/efo/EFO_1000663), [EFO:1000691](http://www.ebi.ac.uk/efo/EFO_1000691)                                                           |
| `MONDO:patterns/congenital`                            |              4 | [EFO:0007217](http://www.ebi.ac.uk/efo/EFO_0007217), [EFO:0007218](http://www.ebi.ac.uk/efo/EFO_0007218), [EFO:0007219](http://www.ebi.ac.uk/efo/EFO_0007219), [EFO:0007220](http://www.ebi.ac.uk/efo/EFO_0007220)                                                           |
| `MONDO:patterns/specific_inflammatory_disease_by_site` |              3 | [EFO:0005627](http://www.ebi.ac.uk/efo/EFO_0005627), [EFO:0005629](http://www.ebi.ac.uk/efo/EFO_0005629), [EFO:0005751](http://www.ebi.ac.uk/efo/EFO_0005751)                                                                                                                |
| `MONDO:cjm`                                            |              3 | [EFO:0000182](http://www.ebi.ac.uk/efo/EFO_0000182), [EFO:0000574](http://www.ebi.ac.uk/efo/EFO_0000574), [EFO:0004243](http://www.ebi.ac.uk/efo/EFO_0004243)                                                                                                                |
| `MONDO:patterns/childhood`                             |              3 | [EFO:0000330](http://www.ebi.ac.uk/efo/EFO_0000330), [EFO:0004594](http://www.ebi.ac.uk/efo/EFO_0004594), [EFO:0009052](http://www.ebi.ac.uk/efo/EFO_0009052)                                                                                                                |
| `MONDO:patterns/x_linked`                              |              2 | [EFO:0009064](http://www.ebi.ac.uk/efo/EFO_0009064), [EFO:0009064](http://www.ebi.ac.uk/efo/EFO_0009064)                                                                                                                                                                     |
| `MONDO:patterns/autosomal_recessive`                   |              2 | [EFO:1000017](http://www.ebi.ac.uk/efo/EFO_1000017), [EFO:1000017](http://www.ebi.ac.uk/efo/EFO_1000017)                                                                                                                                                                     |
| `MONDO:patterns/autosomal_dominant`                    |              2 | [EFO:1001496](http://www.ebi.ac.uk/efo/EFO_1001496), [EFO:1001496](http://www.ebi.ac.uk/efo/EFO_1001496)                                                                                                                                                                     |
| `MONDO:DesignPattern`                                  |              2 | [EFO:0000294](http://www.ebi.ac.uk/efo/EFO_0000294), [EFO:1000071](http://www.ebi.ac.uk/efo/EFO_1000071)                                                                                                                                                                     |
| `MONDO:patterns/carcinoma_in_situ`                     |              2 | [EFO:0000432](http://www.ebi.ac.uk/efo/EFO_0000432), [EFO:1000283](http://www.ebi.ac.uk/efo/EFO_1000283)                                                                                                                                                                     |
| `MONDO:patterns/neuroendocrine_neoplasm`               |              2 | [EFO:0005220](http://www.ebi.ac.uk/efo/EFO_0005220), [EFO:1001928](http://www.ebi.ac.uk/efo/EFO_1001928)                                                                                                                                                                     |
| `MONDO:patterns/inborn_metabolic`                      |              2 | [EFO:0005596](http://www.ebi.ac.uk/efo/EFO_0005596), [EFO:0007287](http://www.ebi.ac.uk/efo/EFO_0007287)                                                                                                                                                                     |
| `MONDO:patterns/allergy`                               |              2 | [EFO:0009482](http://www.ebi.ac.uk/efo/EFO_0009482), [EFO:1001890](http://www.ebi.ac.uk/efo/EFO_1001890)                                                                                                                                                                     |
| `MONDO:patterns/adult`                                 |              2 | [EFO:1001933](http://www.ebi.ac.uk/efo/EFO_1001933), [EFO:1001935](http://www.ebi.ac.uk/efo/EFO_1001935)                                                                                                                                                                     |
| `MONDO:design_patterns`                                |              1 | [EFO:0000182](http://www.ebi.ac.uk/efo/EFO_0000182)                                                                                                                                                                                                                          |

## `NCIm`: NCI Metathesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCIm` (standardized to Bioregistry
prefix [`ncim`](https://bioregistry.io/ncim)) that
did not match the standard pattern `^C\d+$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `NCIm:CL455363` |              1 | [EFO:0003918](http://www.ebi.ac.uk/efo/EFO_0003918) |

## `NCIT`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCIT` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^[CRPA]\d+$`.

| external_xref           |   usages_count | usages                                              |
|-------------------------|----------------|-----------------------------------------------------|
| `NCIT:C128346-modified` |              1 | [EFO:0004720](http://www.ebi.ac.uk/efo/EFO_0004720) |

## `NCIt`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCIt` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^[CRPA]\d+$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `NCIt: C12511`  |              1 | [EFO:0001394](http://www.ebi.ac.uk/efo/EFO_0001394) |

## `NIFSTD`: NIF Standard Ontology

Overall, there were 100 invalid
xrefs to external prefixed with `NIFSTD` (standardized to Bioregistry
prefix [`nif.std`](https://bioregistry.io/nif.std)) that
did not match the standard pattern `^BAMSC\d+$`.

| external_xref              |   usages_count | usages                                                                                                   |
|----------------------------|----------------|----------------------------------------------------------------------------------------------------------|
| `NIFSTD:birnlex_2117`      |              2 | [EFO:0002607](http://www.ebi.ac.uk/efo/EFO_0002607), [EFO:0002694](http://www.ebi.ac.uk/efo/EFO_0002694) |
| `NIFSTD:birnlex_734`       |              1 | [EFO:0000107](http://www.ebi.ac.uk/efo/EFO_0000107)                                                      |
| `NIFSTD:birnlex_1581`      |              1 | [EFO:0000230](http://www.ebi.ac.uk/efo/EFO_0000230)                                                      |
| `NIFSTD:birnlex_2092`      |              1 | [EFO:0000249](http://www.ebi.ac.uk/efo/EFO_0000249)                                                      |
| `NIFSTD:birnlex_1241`      |              1 | [EFO:0000252](http://www.ebi.ac.uk/efo/EFO_0000252)                                                      |
| `NIFSTD:birnlex_12566`     |              1 | [EFO:0000253](http://www.ebi.ac.uk/efo/EFO_0000253)                                                      |
| `NIFSTD:birnlex_2110`      |              1 | [EFO:0000264](http://www.ebi.ac.uk/efo/EFO_0000264)                                                      |
| `NIFSTD:birnlex_12754`     |              1 | [EFO:0000289](http://www.ebi.ac.uk/efo/EFO_0000289)                                                      |
| `NIFSTD:birnlex_796`       |              1 | [EFO:0000302](http://www.ebi.ac.uk/efo/EFO_0000302)                                                      |
| `NIFSTD:birnlex_406`       |              1 | [EFO:0000311](http://www.ebi.ac.uk/efo/EFO_0000311)                                                      |
| `NIFSTD:birnlex_1489`      |              1 | [EFO:0000327](http://www.ebi.ac.uk/efo/EFO_0000327)                                                      |
| `NIFSTD:birnlex_934`       |              1 | [EFO:0000343](http://www.ebi.ac.uk/efo/EFO_0000343)                                                      |
| `NIFSTD:birnlex_1190`      |              1 | [EFO:0000357](http://www.ebi.ac.uk/efo/EFO_0000357)                                                      |
| `NIFSTD:birnlex_1672`      |              1 | [EFO:0000381](http://www.ebi.ac.uk/efo/EFO_0000381)                                                      |
| `NIFSTD:nlx_anat_20090201` |              1 | [EFO:0000381](http://www.ebi.ac.uk/efo/EFO_0000381)                                                      |
| `NIFSTD:birnlex_1494`      |              1 | [EFO:0000383](http://www.ebi.ac.uk/efo/EFO_0000383)                                                      |
| `NIFSTD:birnlex_2052`      |              1 | [EFO:0000433](http://www.ebi.ac.uk/efo/EFO_0000433)                                                      |
| `NIFSTD:birnlex_12718`     |              1 | [EFO:0000474](http://www.ebi.ac.uk/efo/EFO_0000474)                                                      |
| `NIFSTD:birnlex_12617`     |              1 | [EFO:0000500](http://www.ebi.ac.uk/efo/EFO_0000500)                                                      |
| `NIFSTD:birnlex_12633`     |              1 | [EFO:0000502](http://www.ebi.ac.uk/efo/EFO_0000502)                                                      |
| `NIFSTD:birnlex_2023`      |              1 | [EFO:0000513](http://www.ebi.ac.uk/efo/EFO_0000513)                                                      |
| `NIFSTD:birnlex_12500`     |              1 | [EFO:0000533](http://www.ebi.ac.uk/efo/EFO_0000533)                                                      |
| `NIFSTD:birnlex_174`       |              1 | [EFO:0000598](http://www.ebi.ac.uk/efo/EFO_0000598)                                                      |
| `NIFSTD:birnlex_557`       |              1 | [EFO:0000600](http://www.ebi.ac.uk/efo/EFO_0000600)                                                      |
| `NIFSTD:birnlex_206`       |              1 | [EFO:0000602](http://www.ebi.ac.uk/efo/EFO_0000602)                                                      |
| `NIFSTD:birnlex_398`       |              1 | [EFO:0000605](http://www.ebi.ac.uk/efo/EFO_0000605)                                                      |
| `NIFSTD:birnlex_393`       |              1 | [EFO:0000606](http://www.ebi.ac.uk/efo/EFO_0000606)                                                      |
| `NIFSTD:birnlex_12631`     |              1 | [EFO:0000621](http://www.ebi.ac.uk/efo/EFO_0000621)                                                      |
| `NIFSTD:birnlex_12604`     |              1 | [EFO:0000622](http://www.ebi.ac.uk/efo/EFO_0000622)                                                      |
| `NIFSTD:birnlex_2087`      |              1 | [EFO:0000651](http://www.ebi.ac.uk/efo/EFO_0000651)                                                      |
| `NIFSTD:birnlex_12606`     |              1 | [EFO:0000658](http://www.ebi.ac.uk/efo/EFO_0000658)                                                      |
| `NIFSTD:birnlex_12669`     |              1 | [EFO:0000677](http://www.ebi.ac.uk/efo/EFO_0000677)                                                      |
| `NIFSTD:birnlex_203`       |              1 | [EFO:0000679](http://www.ebi.ac.uk/efo/EFO_0000679)                                                      |
| `NIFSTD:birnlex_2104`      |              1 | [EFO:0000692](http://www.ebi.ac.uk/efo/EFO_0000692)                                                      |
| `NIFSTD:birnlex_12603`     |              1 | [EFO:0000693](http://www.ebi.ac.uk/efo/EFO_0000693)                                                      |
| `NIFSTD:birnlex_12783`     |              1 | [EFO:0000712](http://www.ebi.ac.uk/efo/EFO_0000712)                                                      |
| `NIFSTD:birnlex_12733`     |              1 | [EFO:0000773](http://www.ebi.ac.uk/efo/EFO_0000773)                                                      |
| `NIFSTD:birnlex_844`       |              1 | [EFO:0000802](http://www.ebi.ac.uk/efo/EFO_0000802)                                                      |
| `NIFSTD:birnlex_1062`      |              1 | [EFO:0000826](http://www.ebi.ac.uk/efo/EFO_0000826)                                                      |
| `NIFSTD:birnlex_1169`      |              1 | [EFO:0000827](http://www.ebi.ac.uk/efo/EFO_0000827)                                                      |
| `NIFSTD:birnlex_1153`      |              1 | [EFO:0000832](http://www.ebi.ac.uk/efo/EFO_0000832)                                                      |
| `NIFSTD:birnlex_1166`      |              1 | [EFO:0000895](http://www.ebi.ac.uk/efo/EFO_0000895)                                                      |
| `NIFSTD:birnlex_2596`      |              1 | [EFO:0000900](http://www.ebi.ac.uk/efo/EFO_0000900)                                                      |
| `NIFSTD:birnlex_826`       |              1 | [EFO:0000904](http://www.ebi.ac.uk/efo/EFO_0000904)                                                      |
| `NIFSTD:birnlex_1234`      |              1 | [EFO:0000905](http://www.ebi.ac.uk/efo/EFO_0000905)                                                      |
| `NIFSTD:birnlex_1373`      |              1 | [EFO:0000907](http://www.ebi.ac.uk/efo/EFO_0000907)                                                      |
| `NIFSTD:birnlex_1099`      |              1 | [EFO:0000908](http://www.ebi.ac.uk/efo/EFO_0000908)                                                      |
| `NIFSTD:birnlex_1509`      |              1 | [EFO:0000909](http://www.ebi.ac.uk/efo/EFO_0000909)                                                      |
| `NIFSTD:birnlex_954`       |              1 | [EFO:0000910](http://www.ebi.ac.uk/efo/EFO_0000910)                                                      |
| `NIFSTD:birnlex_1503`      |              1 | [EFO:0000911](http://www.ebi.ac.uk/efo/EFO_0000911)                                                      |
| `NIFSTD:birnlex_1115`      |              1 | [EFO:0000912](http://www.ebi.ac.uk/efo/EFO_0000912)                                                      |
| `NIFSTD:birnlex_928`       |              1 | [EFO:0000913](http://www.ebi.ac.uk/efo/EFO_0000913)                                                      |
| `NIFSTD:nlx_anat_20090601` |              1 | [EFO:0000913](http://www.ebi.ac.uk/efo/EFO_0000913)                                                      |
| `NIFSTD:birnlex_1710`      |              1 | [EFO:0000918](http://www.ebi.ac.uk/efo/EFO_0000918)                                                      |
| `NIFSTD:birnlex_1667`      |              1 | [EFO:0000919](http://www.ebi.ac.uk/efo/EFO_0000919)                                                      |
| `NIFSTD:birnlex_942`       |              1 | [EFO:0000923](http://www.ebi.ac.uk/efo/EFO_0000923)                                                      |
| `NIFSTD:birnlex_957`       |              1 | [EFO:0000924](http://www.ebi.ac.uk/efo/EFO_0000924)                                                      |
| `NIFSTD:birnlex_1230`      |              1 | [EFO:0000964](http://www.ebi.ac.uk/efo/EFO_0000964)                                                      |
| `NIFSTD:sao1078172392`     |              1 | [EFO:0000966](http://www.ebi.ac.uk/efo/EFO_0000966)                                                      |
| `NIFSTD:sao1642908940`     |              1 | [EFO:0000967](http://www.ebi.ac.uk/efo/EFO_0000967)                                                      |
| `NIFSTD:nlx_dys_20090502`  |              1 | [EFO:0001064](http://www.ebi.ac.uk/efo/EFO_0001064)                                                      |
| `NIFSTD:nlx_dys_20090302`  |              1 | [EFO:0001073](http://www.ebi.ac.uk/efo/EFO_0001073)                                                      |
| `NIFSTD:nlx_dys_20090303`  |              1 | [EFO:0001074](http://www.ebi.ac.uk/efo/EFO_0001074)                                                      |
| `NIFSTD:birnlex_12770`     |              1 | [EFO:0001079](http://www.ebi.ac.uk/efo/EFO_0001079)                                                      |
| `NIFSTD:birnlex_228`       |              1 | [EFO:0001272](http://www.ebi.ac.uk/efo/EFO_0001272)                                                      |
| `NIFSTD:birnlex_681`       |              1 | [EFO:0001272](http://www.ebi.ac.uk/efo/EFO_0001272)                                                      |
| `NIFSTD:birnlex_577`       |              1 | [EFO:0001327](http://www.ebi.ac.uk/efo/EFO_0001327)                                                      |
| `NIFSTD:birnlex_152`       |              1 | [EFO:0001331](http://www.ebi.ac.uk/efo/EFO_0001331)                                                      |
| `NIFSTD:birnlex_106`       |              1 | [EFO:0001332](http://www.ebi.ac.uk/efo/EFO_0001332)                                                      |
| `NIFSTD:birnlex_320`       |              1 | [EFO:0001342](http://www.ebi.ac.uk/efo/EFO_0001342)                                                      |
| `NIFSTD:birnlex_214`       |              1 | [EFO:0001352](http://www.ebi.ac.uk/efo/EFO_0001352)                                                      |
| `NIFSTD:birnlex_266`       |              1 | [EFO:0001352](http://www.ebi.ac.uk/efo/EFO_0001352)                                                      |
| `NIFSTD:birnlex_438`       |              1 | [EFO:0001355](http://www.ebi.ac.uk/efo/EFO_0001355)                                                      |
| `NIFSTD:birnlex_695`       |              1 | [EFO:0001355](http://www.ebi.ac.uk/efo/EFO_0001355)                                                      |
| `NIFSTD:birnlex_12679`     |              1 | [EFO:0001358](http://www.ebi.ac.uk/efo/EFO_0001358)                                                      |
| `NIFSTD:birnlex_12812`     |              1 | [EFO:0001365](http://www.ebi.ac.uk/efo/EFO_0001365)                                                      |
| `NIFSTD:birnlex_1178`      |              1 | [EFO:0001366](http://www.ebi.ac.uk/efo/EFO_0001366)                                                      |
| `NIFSTD:sao1145756102`     |              1 | [EFO:0001369](http://www.ebi.ac.uk/efo/EFO_0001369)                                                      |
| `NIFSTD:birnlex_429`       |              1 | [EFO:0001372](http://www.ebi.ac.uk/efo/EFO_0001372)                                                      |
| `NIFSTD:birnlex_699`       |              1 | [EFO:0001372](http://www.ebi.ac.uk/efo/EFO_0001372)                                                      |
| `NIFSTD:birnlex_733`       |              1 | [EFO:0001394](http://www.ebi.ac.uk/efo/EFO_0001394)                                                      |
| `NIFSTD:sao279801585`      |              1 | [EFO:0001444](http://www.ebi.ac.uk/efo/EFO_0001444)                                                      |
| `NIFSTD:birnlex_2525`      |              1 | [EFO:0001644](http://www.ebi.ac.uk/efo/EFO_0001644)                                                      |
| `NIFSTD:sao2146594471`     |              1 | [EFO:0001651](http://www.ebi.ac.uk/efo/EFO_0001651)                                                      |
| `NIFSTD:sao1703115805`     |              1 | [EFO:0001653](http://www.ebi.ac.uk/efo/EFO_0001653)                                                      |
| `NIFSTD:sao-282380853`     |              1 | [EFO:0001654](http://www.ebi.ac.uk/efo/EFO_0001654)                                                      |
| `NIFSTD:birnlex_2391`      |              1 | [EFO:0001715](http://www.ebi.ac.uk/efo/EFO_0001715)                                                      |
| `NIFSTD:sao196989303`      |              1 | [EFO:0001715](http://www.ebi.ac.uk/efo/EFO_0001715)                                                      |
| `NIFSTD:birnlex_2085`      |              1 | [EFO:0001738](http://www.ebi.ac.uk/efo/EFO_0001738)                                                      |
| `NIFSTD:birnlex_3016`      |              1 | [EFO:0001799](http://www.ebi.ac.uk/efo/EFO_0001799)                                                      |
| `NIFSTD:birnlex_982`       |              1 | [EFO:0001919](http://www.ebi.ac.uk/efo/EFO_0001919)                                                      |
| `NIFSTD:birnlex_1263`      |              1 | [EFO:0001961](http://www.ebi.ac.uk/efo/EFO_0001961)                                                      |
| `NIFSTD:birnlex_1565`      |              1 | [EFO:0001962](http://www.ebi.ac.uk/efo/EFO_0001962)                                                      |
| `NIFSTD:birnlex_1202`      |              1 | [EFO:0001987](http://www.ebi.ac.uk/efo/EFO_0001987)                                                      |
| `NIFSTD:birnlex_12573`     |              1 | [EFO:0002505](http://www.ebi.ac.uk/efo/EFO_0002505)                                                      |
| `NIFSTD:birnlex_2098`      |              1 | [EFO:0002508](http://www.ebi.ac.uk/efo/EFO_0002508)                                                      |
| `NIFSTD:birnlex_12697`     |              1 | [EFO:0002512](http://www.ebi.ac.uk/efo/EFO_0002512)                                                      |
| `NIFSTD:birnlex_484`       |              1 | [EFO:0002543](http://www.ebi.ac.uk/efo/EFO_0002543)                                                      |
| `NIFSTD:birnlex_12648`     |              1 | [EFO:0002624](http://www.ebi.ac.uk/efo/EFO_0002624)                                                      |

## `OBI`: Ontology for Biomedical Investigations

Overall, there were 1 invalid
xrefs to external prefixed with `OBI` (standardized to Bioregistry
prefix [`obi`](https://bioregistry.io/obi)) that
did not match the standard pattern `^\d{7}$`.

| external_xref     |   usages_count | usages                                              |
|-------------------|----------------|-----------------------------------------------------|
| `OBI:OBI_1110054` |              1 | [EFO:0005140](http://www.ebi.ac.uk/efo/EFO_0005140) |

## `ORDO`: Orphanet Rare Disease Ontology

Overall, there were 39 invalid
xrefs to external prefixed with `ORDO` (standardized to Bioregistry
prefix [`orphanet.ordo`](https://bioregistry.io/orphanet.ordo)) that
did not match the standard pattern `^C?\d+$`.

| external_xref          |   usages_count | usages                                                                                                   |
|------------------------|----------------|----------------------------------------------------------------------------------------------------------|
| `ORDO:Orphanet_71273`  |              2 | [EFO:1001838](http://www.ebi.ac.uk/efo/EFO_1001838), [EFO:1001915](http://www.ebi.ac.uk/efo/EFO_1001915) |
| `ORDO:Orphanet_803`    |              1 | [EFO:0000253](http://www.ebi.ac.uk/efo/EFO_0000253)                                                      |
| `ORDO:Orphanet_217569` |              1 | [EFO:0000538](http://www.ebi.ac.uk/efo/EFO_0000538)                                                      |
| `ORDO:Orphanet_3386`   |              1 | [EFO:0008559](http://www.ebi.ac.uk/efo/EFO_0008559)                                                      |
| `ORDO:Orphanet_454710` |              1 | [EFO:0008597](http://www.ebi.ac.uk/efo/EFO_0008597)                                                      |
| `ORDO:Orphanet_79481`  |              1 | [EFO:0008601](http://www.ebi.ac.uk/efo/EFO_0008601)                                                      |
| `ORDO:Orphanet_63455`  |              1 | [EFO:0008602](http://www.ebi.ac.uk/efo/EFO_0008602)                                                      |
| `ORDO:Orphanet_79480`  |              1 | [EFO:0008603](http://www.ebi.ac.uk/efo/EFO_0008603)                                                      |
| `ORDO:Orphanet_46486`  |              1 | [EFO:1000680](http://www.ebi.ac.uk/efo/EFO_1000680)                                                      |
| `ORDO:Orphanet_107`    |              1 | [EFO:1001251](http://www.ebi.ac.uk/efo/EFO_1001251)                                                      |
| `ORDO:Orphanet_1457`   |              1 | [EFO:1001267](http://www.ebi.ac.uk/efo/EFO_1001267)                                                      |
| `ORDO:Orphanet_36205`  |              1 | [EFO:1001293](http://www.ebi.ac.uk/efo/EFO_1001293)                                                      |
| `ORDO:Orphanet_65279`  |              1 | [EFO:1001294](http://www.ebi.ac.uk/efo/EFO_1001294)                                                      |
| `ORDO:Orphanet_58220`  |              1 | [EFO:1001295](http://www.ebi.ac.uk/efo/EFO_1001295)                                                      |
| `ORDO:Orphanet_86864`  |              1 | [EFO:1001341](http://www.ebi.ac.uk/efo/EFO_1001341)                                                      |
| `ORDO:Orphanet_33543`  |              1 | [EFO:1001354](http://www.ebi.ac.uk/efo/EFO_1001354)                                                      |
| `ORDO:Orphanet_158011` |              1 | [EFO:1001376](http://www.ebi.ac.uk/efo/EFO_1001376)                                                      |
| `ORDO:Orphanet_1183`   |              1 | [EFO:1001383](http://www.ebi.ac.uk/efo/EFO_1001383)                                                      |
| `ORDO:Orphanet_3392`   |              1 | [EFO:1001444](http://www.ebi.ac.uk/efo/EFO_1001444)                                                      |
| `ORDO:Orphanet_879`    |              1 | [EFO:1001445](http://www.ebi.ac.uk/efo/EFO_1001445)                                                      |
| `ORDO:Orphanet_662`    |              1 | [EFO:1001452](http://www.ebi.ac.uk/efo/EFO_1001452)                                                      |
| `ORDO:Orphanet_168956` |              1 | [EFO:1001467](http://www.ebi.ac.uk/efo/EFO_1001467)                                                      |
| `ORDO:Orphanet_217720` |              1 | [EFO:1001473](http://www.ebi.ac.uk/efo/EFO_1001473)                                                      |
| `ORDO:Orphanet_188`    |              1 | [EFO:1001477](http://www.ebi.ac.uk/efo/EFO_1001477)                                                      |
| `ORDO:Orphanet_963`    |              1 | [EFO:1001485](http://www.ebi.ac.uk/efo/EFO_1001485)                                                      |
| `ORDO:Orphanet_228119` |              1 | [EFO:1001795](http://www.ebi.ac.uk/efo/EFO_1001795)                                                      |
| `ORDO:Orphanet_158061` |              1 | [EFO:1001806](http://www.ebi.ac.uk/efo/EFO_1001806)                                                      |
| `ORDO:Orphanet_306682` |              1 | [EFO:1001808](http://www.ebi.ac.uk/efo/EFO_1001808)                                                      |
| `ORDO:Orphanet_221074` |              1 | [EFO:1001809](http://www.ebi.ac.uk/efo/EFO_1001809)                                                      |
| `ORDO:Orphanet_137617` |              1 | [EFO:1001814](http://www.ebi.ac.uk/efo/EFO_1001814)                                                      |
| `ORDO:Orphanet_157835` |              1 | [EFO:1001822](http://www.ebi.ac.uk/efo/EFO_1001822)                                                      |
| `ORDO:Orphanet_43116`  |              1 | [EFO:1001842](http://www.ebi.ac.uk/efo/EFO_1001842)                                                      |
| `ORDO:Orphanet_36236`  |              1 | [EFO:1001849](http://www.ebi.ac.uk/efo/EFO_1001849)                                                      |
| `ORDO:Orphanet_838`    |              1 | [EFO:1001856](http://www.ebi.ac.uk/efo/EFO_1001856)                                                      |
| `ORDO:Orphanet_3287`   |              1 | [EFO:1001857](http://www.ebi.ac.uk/efo/EFO_1001857)                                                      |
| `ORDO:Orphanet_83467`  |              1 | [EFO:1001897](http://www.ebi.ac.uk/efo/EFO_1001897)                                                      |
| `ORDO:Orphanet_85414`  |              1 | [EFO:1001999](http://www.ebi.ac.uk/efo/EFO_1001999)                                                      |
| `ORDO:Orphanet_66529`  |              1 | [EFO:1002000](http://www.ebi.ac.uk/efo/EFO_1002000)                                                      |

## `PMID`: PubMed

Overall, there were 18 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref     |   usages_count | usages                                                                                                   |
|-------------------|----------------|----------------------------------------------------------------------------------------------------------|
| `PMID: 26629530`  |              2 | [EFO:0022705](http://www.ebi.ac.uk/efo/EFO_0022705), [EFO:0022706](http://www.ebi.ac.uk/efo/EFO_0022706) |
| `PMID: 11246871`  |              1 | [EFO:0002540](http://www.ebi.ac.uk/efo/EFO_0002540)                                                      |
| `PMID:PMC1531688` |              1 | [EFO:0005725](http://www.ebi.ac.uk/efo/EFO_0005725)                                                      |
| `PMID: 3897439`   |              1 | [EFO:0005910](http://www.ebi.ac.uk/efo/EFO_0005910)                                                      |
| `PMID: 8788275`   |              1 | [EFO:0005913](http://www.ebi.ac.uk/efo/EFO_0005913)                                                      |
| `PMID:27149984 `  |              1 | [EFO:0007836](http://www.ebi.ac.uk/efo/EFO_0007836)                                                      |
| `PMID: 31636452`  |              1 | [EFO:0010605](http://www.ebi.ac.uk/efo/EFO_0010605)                                                      |
| `PMID:25167691 `  |              1 | [EFO:0010695](http://www.ebi.ac.uk/efo/EFO_0010695)                                                      |
| `PMID: 32355309`  |              1 | [EFO:0010749](http://www.ebi.ac.uk/efo/EFO_0010749)                                                      |
| `PMID: 19881539`  |              1 | [EFO:0022445](http://www.ebi.ac.uk/efo/EFO_0022445)                                                      |
| `PMID: 25680274`  |              1 | [EFO:0022593](http://www.ebi.ac.uk/efo/EFO_0022593)                                                      |
| `PMID: 10764661`  |              1 | [EFO:0022696](http://www.ebi.ac.uk/efo/EFO_0022696)                                                      |
| `PMID: 16395697`  |              1 | [EFO:0022699](http://www.ebi.ac.uk/efo/EFO_0022699)                                                      |
| `PMID: 11479214`  |              1 | [EFO:0022701](http://www.ebi.ac.uk/efo/EFO_0022701)                                                      |
| `PMID: 19466639`  |              1 | [EFO:0022708](http://www.ebi.ac.uk/efo/EFO_0022708)                                                      |
| `PMID: 8394948`   |              1 | [EFO:0022718](http://www.ebi.ac.uk/efo/EFO_0022718)                                                      |
| `PMID: 16537381`  |              1 | [EFO:0022786](http://www.ebi.ac.uk/efo/EFO_0022786)                                                      |

## `PRO`: Protein Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `PRO` (standardized to Bioregistry
prefix [`pr`](https://bioregistry.io/pr)) that
did not match the standard pattern `^(?:\d{9}|[OPQ][0-9][A-Z0-9]{3}[0-9](?:-\d+)?|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2}(?:-\d+)?)$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `PRO:DAN`       |              1 | [EFO:0003021](http://www.ebi.ac.uk/efo/EFO_0003021) |

## `Reactome`: Reactome

Overall, there were 3 invalid
xrefs to external prefixed with `Reactome` (standardized to Bioregistry
prefix [`reactome`](https://bioregistry.io/reactome)) that
did not match the standard pattern `^R-[A-Z]{3}-\d+(-\d+)?(\.\d+)?$`.

| external_xref     |   usages_count | usages                                              |
|-------------------|----------------|-----------------------------------------------------|
| `Reactome:Q9HB96` |              1 | [EFO:0009914](http://www.ebi.ac.uk/efo/EFO_0009914) |
| `Reactome:Q9ULP9` |              1 | [EFO:0009915](http://www.ebi.ac.uk/efo/EFO_0009915) |
| `Reactome:Q9NP58` |              1 | [EFO:0009916](http://www.ebi.ac.uk/efo/EFO_0009916) |

## `SNOMEDCT`: SNOMED CT (International Edition)

Overall, there were 3 invalid
xrefs to external prefixed with `SNOMEDCT` (standardized to Bioregistry
prefix [`snomedct`](https://bioregistry.io/snomedct)) that
did not match the standard pattern `^(\w+)?\d+$`.

| external_xref         |   usages_count | usages                                              |
|-----------------------|----------------|-----------------------------------------------------|
| `SNOMEDCT: 266417001` |              1 | [EFO:0010688](http://www.ebi.ac.uk/efo/EFO_0010688) |
| `SNOMEDCT:88039007 `  |              1 | [EFO:0010721](http://www.ebi.ac.uk/efo/EFO_0010721) |
| `SNOMEDCT: 274897005` |              1 | [EFO:1001841](http://www.ebi.ac.uk/efo/EFO_1001841) |

## `TADS`: Tick Anatomy Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `TADS` (standardized to Bioregistry
prefix [`tads`](https://bioregistry.io/tads)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `TADS:000315`   |              1 | [EFO:0000935](http://www.ebi.ac.uk/efo/EFO_0000935) |

## `TGMA`: Mosquito gross anatomy ontology

Overall, there were 1 invalid
xrefs to external prefixed with `TGMA` (standardized to Bioregistry
prefix [`tgma`](https://bioregistry.io/tgma)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `TGMA:000136`   |              1 | [EFO:0000965](http://www.ebi.ac.uk/efo/EFO_0000965) |

## `UMLS`: Unified Medical Language System Concept Unique Identifier

Overall, there were 81 invalid
xrefs to external prefixed with `UMLS` (standardized to Bioregistry
prefix [`umls`](https://bioregistry.io/umls)) that
did not match the standard pattern `^C\d+$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `UMLS:CN242113` |              1 | [EFO:0000350](http://www.ebi.ac.uk/efo/EFO_0000350) |
| `UMLS:CN227279` |              1 | [EFO:0000519](http://www.ebi.ac.uk/efo/EFO_0000519) |
| `UMLS:CN236628` |              1 | [EFO:0000616](http://www.ebi.ac.uk/efo/EFO_0000616) |
| `UMLS:CN205129` |              1 | [EFO:0000640](http://www.ebi.ac.uk/efo/EFO_0000640) |
| `UMLS:CN244903` |              1 | [EFO:0000702](http://www.ebi.ac.uk/efo/EFO_0000702) |
| `UMLS:CN971653` |              1 | [EFO:0000756](http://www.ebi.ac.uk/efo/EFO_0000756) |
| `UMLS:CN204600` |              1 | [EFO:0005717](http://www.ebi.ac.uk/efo/EFO_0005717) |
| `UMLS:CN237663` |              1 | [EFO:0005783](http://www.ebi.ac.uk/efo/EFO_0005783) |
| `UMLS:CN205033` |              1 | [EFO:0006462](http://www.ebi.ac.uk/efo/EFO_0006462) |
| `UMLS:CL520437` |              1 | [EFO:0008614](http://www.ebi.ac.uk/efo/EFO_0008614) |
| `UMLS:CN202862` |              1 | [EFO:0009068](http://www.ebi.ac.uk/efo/EFO_0009068) |
| `UMLS:CN240512` |              1 | [EFO:0009068](http://www.ebi.ac.uk/efo/EFO_0009068) |
| `UMLS:CN237671` |              1 | [EFO:0009553](http://www.ebi.ac.uk/efo/EFO_0009553) |
| `UMLS:CN072436` |              1 | [EFO:0009907](http://www.ebi.ac.uk/efo/EFO_0009907) |
| `UMLS:CN229293` |              1 | [EFO:0700025](http://www.ebi.ac.uk/efo/EFO_0700025) |
| `UMLS:CN226594` |              1 | [EFO:0700026](http://www.ebi.ac.uk/efo/EFO_0700026) |
| `UMLS:CN228909` |              1 | [EFO:0700027](http://www.ebi.ac.uk/efo/EFO_0700027) |
| `UMLS:CN197468` |              1 | [EFO:0700028](http://www.ebi.ac.uk/efo/EFO_0700028) |
| `UMLS:CN197488` |              1 | [EFO:0700029](http://www.ebi.ac.uk/efo/EFO_0700029) |
| `UMLS:CN226645` |              1 | [EFO:0700030](http://www.ebi.ac.uk/efo/EFO_0700030) |
| `UMLS:CN228927` |              1 | [EFO:0700031](http://www.ebi.ac.uk/efo/EFO_0700031) |
| `UMLS:CN228928` |              1 | [EFO:0700032](http://www.ebi.ac.uk/efo/EFO_0700032) |
| `UMLS:CN228932` |              1 | [EFO:0700033](http://www.ebi.ac.uk/efo/EFO_0700033) |
| `UMLS:CN228933` |              1 | [EFO:0700034](http://www.ebi.ac.uk/efo/EFO_0700034) |
| `UMLS:CN199609` |              1 | [EFO:0700036](http://www.ebi.ac.uk/efo/EFO_0700036) |
| `UMLS:CN226709` |              1 | [EFO:0700037](http://www.ebi.ac.uk/efo/EFO_0700037) |
| `UMLS:CN200175` |              1 | [EFO:0700038](http://www.ebi.ac.uk/efo/EFO_0700038) |
| `UMLS:CN226739` |              1 | [EFO:0700040](http://www.ebi.ac.uk/efo/EFO_0700040) |
| `UMLS:CN229044` |              1 | [EFO:0700051](http://www.ebi.ac.uk/efo/EFO_0700051) |
| `UMLS:CN201790` |              1 | [EFO:0700057](http://www.ebi.ac.uk/efo/EFO_0700057) |
| `UMLS:CN201945` |              1 | [EFO:0700058](http://www.ebi.ac.uk/efo/EFO_0700058) |
| `UMLS:CN201974` |              1 | [EFO:0700059](http://www.ebi.ac.uk/efo/EFO_0700059) |
| `UMLS:CN227033` |              1 | [EFO:0700060](http://www.ebi.ac.uk/efo/EFO_0700060) |
| `UMLS:CN202399` |              1 | [EFO:0700061](http://www.ebi.ac.uk/efo/EFO_0700061) |
| `UMLS:CN227073` |              1 | [EFO:0700062](http://www.ebi.ac.uk/efo/EFO_0700062) |
| `UMLS:CN227096` |              1 | [EFO:0700065](http://www.ebi.ac.uk/efo/EFO_0700065) |
| `UMLS:CN202572` |              1 | [EFO:0700066](http://www.ebi.ac.uk/efo/EFO_0700066) |
| `UMLS:CN202602` |              1 | [EFO:0700067](http://www.ebi.ac.uk/efo/EFO_0700067) |
| `UMLS:CN202699` |              1 | [EFO:0700068](http://www.ebi.ac.uk/efo/EFO_0700068) |
| `UMLS:CN202725` |              1 | [EFO:0700069](http://www.ebi.ac.uk/efo/EFO_0700069) |
| `UMLS:CN203384` |              1 | [EFO:0700071](http://www.ebi.ac.uk/efo/EFO_0700071) |
| `UMLS:CN204041` |              1 | [EFO:0700074](http://www.ebi.ac.uk/efo/EFO_0700074) |
| `UMLS:CN437676` |              1 | [EFO:0700075](http://www.ebi.ac.uk/efo/EFO_0700075) |
| `UMLS:CN204780` |              1 | [EFO:0700081](http://www.ebi.ac.uk/efo/EFO_0700081) |
| `UMLS:CN204808` |              1 | [EFO:0700082](http://www.ebi.ac.uk/efo/EFO_0700082) |
| `UMLS:CN225947` |              1 | [EFO:0700088](http://www.ebi.ac.uk/efo/EFO_0700088) |
| `UMLS:CN237587` |              1 | [EFO:0700090](http://www.ebi.ac.uk/efo/EFO_0700090) |
| `UMLS:CN237592` |              1 | [EFO:0700091](http://www.ebi.ac.uk/efo/EFO_0700091) |
| `UMLS:CN242171` |              1 | [EFO:0700093](http://www.ebi.ac.uk/efo/EFO_0700093) |
| `UMLS:CN776854` |              1 | [EFO:0700096](http://www.ebi.ac.uk/efo/EFO_0700096) |
| `UMLS:CN776824` |              1 | [EFO:0700097](http://www.ebi.ac.uk/efo/EFO_0700097) |
| `UMLS:CN205687` |              1 | [EFO:0700102](http://www.ebi.ac.uk/efo/EFO_0700102) |
| `UMLS:CN205736` |              1 | [EFO:0700103](http://www.ebi.ac.uk/efo/EFO_0700103) |
| `UMLS:CN227591` |              1 | [EFO:0700104](http://www.ebi.ac.uk/efo/EFO_0700104) |
| `UMLS:CN206266` |              1 | [EFO:0700105](http://www.ebi.ac.uk/efo/EFO_0700105) |
| `UMLS:CN206304` |              1 | [EFO:0700106](http://www.ebi.ac.uk/efo/EFO_0700106) |
| `UMLS:CN227645` |              1 | [EFO:0700107](http://www.ebi.ac.uk/efo/EFO_0700107) |
| `UMLS:CN227674` |              1 | [EFO:0700110](http://www.ebi.ac.uk/efo/EFO_0700110) |
| `UMLS:CN206692` |              1 | [EFO:0700113](http://www.ebi.ac.uk/efo/EFO_0700113) |
| `UMLS:CN120488` |              1 | [EFO:0700119](http://www.ebi.ac.uk/efo/EFO_0700119) |
| `UMLS:CN227798` |              1 | [EFO:0700120](http://www.ebi.ac.uk/efo/EFO_0700120) |
| `UMLS:CN227834` |              1 | [EFO:0700123](http://www.ebi.ac.uk/efo/EFO_0700123) |
| `UMLS:CN207246` |              1 | [EFO:0700129](http://www.ebi.ac.uk/efo/EFO_0700129) |
| `UMLS:CN043667` |              1 | [EFO:0700137](http://www.ebi.ac.uk/efo/EFO_0700137) |
| `UMLS:CN226945` |              1 | [EFO:1000015](http://www.ebi.ac.uk/efo/EFO_1000015) |
| `UMLS:CN203416` |              1 | [EFO:1000027](http://www.ebi.ac.uk/efo/EFO_1000027) |
| `UMLS:CN201941` |              1 | [EFO:1000028](http://www.ebi.ac.uk/efo/EFO_1000028) |
| `UMLS:CN205034` |              1 | [EFO:1000042](http://www.ebi.ac.uk/efo/EFO_1000042) |
| `UMLS:CL343552` |              1 | [EFO:1000056](http://www.ebi.ac.uk/efo/EFO_1000056) |
| `UMLS:CN202866` |              1 | [EFO:1000129](http://www.ebi.ac.uk/efo/EFO_1000129) |
| `UMLS:CN201056` |              1 | [EFO:1000242](http://www.ebi.ac.uk/efo/EFO_1000242) |
| `UMLS:CN237470` |              1 | [EFO:1000278](http://www.ebi.ac.uk/efo/EFO_1000278) |
| `UMLS:CN206982` |              1 | [EFO:1000297](http://www.ebi.ac.uk/efo/EFO_1000297) |
| `UMLS:CN203938` |              1 | [EFO:1000314](http://www.ebi.ac.uk/efo/EFO_1000314) |
| `UMLS:CN202288` |              1 | [EFO:1000395](http://www.ebi.ac.uk/efo/EFO_1000395) |
| `UMLS:CN204702` |              1 | [EFO:1000570](http://www.ebi.ac.uk/efo/EFO_1000570) |
| `UMLS:CN207411` |              1 | [EFO:1000576](http://www.ebi.ac.uk/efo/EFO_1000576) |
| `UMLS:CN237515` |              1 | [EFO:1001928](http://www.ebi.ac.uk/efo/EFO_1001928) |
| `UMLS:CN221574` |              1 | [EFO:1001951](http://www.ebi.ac.uk/efo/EFO_1001951) |
| `UMLS:CN204398` |              1 | [EFO:1001968](http://www.ebi.ac.uk/efo/EFO_1001968) |
| `UMLS:CN207484` |              1 | [EFO:1002008](http://www.ebi.ac.uk/efo/EFO_1002008) |

## `Wikipedia`: Wikipedia

Overall, there were 2 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^\S+$`.

| external_xref                      |   usages_count | usages                                                                                                   |
|------------------------------------|----------------|----------------------------------------------------------------------------------------------------------|
| `Wikipedia:Single cell sequencing` |              2 | [EFO:0008913](http://www.ebi.ac.uk/efo/EFO_0008913), [EFO:0008913](http://www.ebi.ac.uk/efo/EFO_0008913) |

