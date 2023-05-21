# dto

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `dto`. See the [GitHub repository](https://github.com/DrugTargetOntology/DTO).


## `ChEBI`: Chemical Entities of Biological Interest

Overall, there were 1 invalid
xrefs to external prefixed with `ChEBI` (standardized to Bioregistry
prefix [`chebi`](https://bioregistry.io/chebi)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `ChEBI:C00209`  |              1 | [CHEBI:30623](http://purl.obolibrary.org/obo/CHEBI_30623) |

## `ChemIDplus`: ChemIDplus

Overall, there were 1 invalid
xrefs to external prefixed with `ChemIDplus` (standardized to Bioregistry
prefix [`chemidplus`](https://bioregistry.io/chemidplus)) that
did not match the standard pattern `^\d+\-\d+\-\d+$`.

| external_xref        |   usages_count | usages                                                    |
|----------------------|----------------|-----------------------------------------------------------|
| `ChemIDplus:1764436` |              1 | [CHEBI:15355](http://purl.obolibrary.org/obo/CHEBI_15355) |

## `KEGG COMPOUND`: KEGG Compound

Overall, there were 39 invalid
xrefs to external prefixed with `KEGG COMPOUND` (standardized to Bioregistry
prefix [`kegg.compound`](https://bioregistry.io/kegg.compound)) that
did not match the standard pattern `^C\d+$`.

| external_xref               |   usages_count | usages                                                    |
|-----------------------------|----------------|-----------------------------------------------------------|
| `KEGG COMPOUND:51-84-3`     |              1 | [CHEBI:15355](http://purl.obolibrary.org/obo/CHEBI_15355) |
| `KEGG COMPOUND:56-65-5`     |              1 | [CHEBI:15422](http://purl.obolibrary.org/obo/CHEBI_15422) |
| `KEGG COMPOUND:56-40-6`     |              1 | [CHEBI:15428](http://purl.obolibrary.org/obo/CHEBI_15428) |
| `KEGG COMPOUND:41598-07-6`  |              1 | [CHEBI:15555](http://purl.obolibrary.org/obo/CHEBI_15555) |
| `KEGG COMPOUND:63-39-8`     |              1 | [CHEBI:15713](http://purl.obolibrary.org/obo/CHEBI_15713) |
| `KEGG COMPOUND:110-15-6`    |              1 | [CHEBI:15741](http://purl.obolibrary.org/obo/CHEBI_15741) |
| `KEGG COMPOUND:56-86-0`     |              1 | [CHEBI:16015](http://purl.obolibrary.org/obo/CHEBI_16015) |
| `KEGG COMPOUND:58-61-7`     |              1 | [CHEBI:16335](http://purl.obolibrary.org/obo/CHEBI_16335) |
| `KEGG COMPOUND:474-25-9`    |              1 | [CHEBI:16755](http://purl.obolibrary.org/obo/CHEBI_16755) |
| `KEGG COMPOUND:20398-34-9`  |              1 | [CHEBI:16761](http://purl.obolibrary.org/obo/CHEBI_16761) |
| `KEGG COMPOUND:58-64-0`     |              1 | [CHEBI:16761](http://purl.obolibrary.org/obo/CHEBI_16761) |
| `KEGG COMPOUND:73-31-4`     |              1 | [CHEBI:16796](http://purl.obolibrary.org/obo/CHEBI_16796) |
| `KEGG COMPOUND:19794-97-9`  |              1 | [CHEBI:16893](http://purl.obolibrary.org/obo/CHEBI_16893) |
| `KEGG COMPOUND:72025-60-6`  |              1 | [CHEBI:16978](http://purl.obolibrary.org/obo/CHEBI_16978) |
| `KEGG COMPOUND:58-98-0`     |              1 | [CHEBI:17659](http://purl.obolibrary.org/obo/CHEBI_17659) |
| `KEGG COMPOUND:16887-00-6`  |              1 | [CHEBI:17996](http://purl.obolibrary.org/obo/CHEBI_17996) |
| `KEGG COMPOUND:62-31-7`     |              1 | [CHEBI:18243](http://purl.obolibrary.org/obo/CHEBI_18243) |
| `KEGG COMPOUND:51-45-6`     |              1 | [CHEBI:18295](http://purl.obolibrary.org/obo/CHEBI_18295) |
| `KEGG COMPOUND:64-04-0`     |              1 | [CHEBI:18397](http://purl.obolibrary.org/obo/CHEBI_18397) |
| `KEGG COMPOUND:94421-68-8`  |              1 | [CHEBI:2700](http://purl.obolibrary.org/obo/CHEBI_2700)   |
| `KEGG COMPOUND:50-67-9`     |              1 | [CHEBI:28790](http://purl.obolibrary.org/obo/CHEBI_28790) |
| `KEGG COMPOUND:51-43-4`     |              1 | [CHEBI:28918](http://purl.obolibrary.org/obo/CHEBI_28918) |
| `KEGG COMPOUND:1393-25-5`   |              1 | [CHEBI:34972](http://purl.obolibrary.org/obo/CHEBI_34972) |
| `KEGG COMPOUND:17034-35-4`  |              1 | [CHEBI:34972](http://purl.obolibrary.org/obo/CHEBI_34972) |
| `KEGG COMPOUND:26993-30-6`  |              1 | [CHEBI:37550](http://purl.obolibrary.org/obo/CHEBI_37550) |
| `KEGG COMPOUND:7439-93-2`   |              1 | [CHEBI:49713](http://purl.obolibrary.org/obo/CHEBI_49713) |
| `KEGG COMPOUND:53847-30-6`  |              1 | [CHEBI:52392](http://purl.obolibrary.org/obo/CHEBI_52392) |
| `KEGG COMPOUND:9007-92-5`   |              1 | [CHEBI:5391](http://purl.obolibrary.org/obo/CHEBI_5391)   |
| `KEGG COMPOUND:54397-84-1`  |              1 | [CHEBI:63977](http://purl.obolibrary.org/obo/CHEBI_63977) |
| `KEGG COMPOUND:89663-86-5`  |              1 | [CHEBI:6498](http://purl.obolibrary.org/obo/CHEBI_6498)   |
| `KEGG COMPOUND:2956-16-3`   |              1 | [CHEBI:67119](http://purl.obolibrary.org/obo/CHEBI_67119) |
| `KEGG COMPOUND:39379-15-2`  |              1 | [CHEBI:7542](http://purl.obolibrary.org/obo/CHEBI_7542)   |
| `KEGG COMPOUND:55508-42-4`  |              1 | [CHEBI:7542](http://purl.obolibrary.org/obo/CHEBI_7542)   |
| `KEGG COMPOUND:60748-06-3`  |              1 | [CHEBI:75441](http://purl.obolibrary.org/obo/CHEBI_75441) |
| `KEGG COMPOUND:123626-67-5` |              1 | [CHEBI:80240](http://purl.obolibrary.org/obo/CHEBI_80240) |
| `KEGG COMPOUND:125692-40-2` |              1 | [CHEBI:80243](http://purl.obolibrary.org/obo/CHEBI_80243) |
| `KEGG COMPOUND:67382-96-1`  |              1 | [CHEBI:80254](http://purl.obolibrary.org/obo/CHEBI_80254) |
| `KEGG COMPOUND:148498-78-6` |              1 | [CHEBI:80339](http://purl.obolibrary.org/obo/CHEBI_80339) |
| `KEGG COMPOUND:9002-04-4`   |              1 | [CHEBI:9574](http://purl.obolibrary.org/obo/CHEBI_9574)   |

## `MESH`: Medical Subject Headings

Overall, there were 25 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref              |   usages_count | usages                                                          |
|----------------------------|----------------|-----------------------------------------------------------------|
| `MESH:A05.360.319.679.256` |              1 | [UBERON:0000002](http://purl.obolibrary.org/obo/UBERON_0000002) |
| `MESH:A05.810.776`         |              1 | [UBERON:0000056](http://purl.obolibrary.org/obo/UBERON_0000056) |
| `MESH:A03.492.411`         |              1 | [UBERON:0000160](http://purl.obolibrary.org/obo/UBERON_0000160) |
| `MESH:A01.236`             |              1 | [UBERON:0000310](http://purl.obolibrary.org/obo/UBERON_0000310) |
| `MESH:A05.360.444.849`     |              1 | [UBERON:0000473](http://purl.obolibrary.org/obo/UBERON_0000473) |
| `MESH:A03.492.766`         |              1 | [UBERON:0000945](http://purl.obolibrary.org/obo/UBERON_0000945) |
| `MESH:A08.186.211`         |              1 | [UBERON:0000955](http://purl.obolibrary.org/obo/UBERON_0000955) |
| `MESH:A05.360.319.114.630` |              1 | [UBERON:0000992](http://purl.obolibrary.org/obo/UBERON_0000992) |
| `MESH:A05.360.319.679`     |              1 | [UBERON:0000995](http://purl.obolibrary.org/obo/UBERON_0000995) |
| `MESH:A05.360.319.887`     |              1 | [UBERON:0000997](http://purl.obolibrary.org/obo/UBERON_0000997) |
| `MESH:A08`                 |              1 | [UBERON:0001016](http://purl.obolibrary.org/obo/UBERON_0001016) |
| `MESH:A03.365`             |              1 | [UBERON:0001043](http://purl.obolibrary.org/obo/UBERON_0001043) |
| `MESH:A05.810.161`         |              1 | [UBERON:0001255](http://purl.obolibrary.org/obo/UBERON_0001255) |
| `MESH:A03.734`             |              1 | [UBERON:0001264](http://purl.obolibrary.org/obo/UBERON_0001264) |
| `MESH:A12.207.152.693`     |              1 | [UBERON:0001969](http://purl.obolibrary.org/obo/UBERON_0001969) |
| `MESH:A06.407.900`         |              1 | [UBERON:0002046](http://purl.obolibrary.org/obo/UBERON_0002046) |
| `MESH:A04.411`             |              1 | [UBERON:0002048](http://purl.obolibrary.org/obo/UBERON_0002048) |
| `MESH:A17.815`             |              1 | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) |
| `MESH:A03.620`             |              1 | [UBERON:0002107](http://purl.obolibrary.org/obo/UBERON_0002107) |
| `MESH:A03.159.439`         |              1 | [UBERON:0002110](http://purl.obolibrary.org/obo/UBERON_0002110) |
| `MESH:A05.810.453`         |              1 | [UBERON:0002113](http://purl.obolibrary.org/obo/UBERON_0002113) |
| `MESH:A03.492.411.620.270` |              1 | [UBERON:0002114](http://purl.obolibrary.org/obo/UBERON_0002114) |
| `MESH:A05.360.444.575`     |              1 | [UBERON:0002367](http://purl.obolibrary.org/obo/UBERON_0002367) |
| `MESH:A06.407.071`         |              1 | [UBERON:0002369](http://purl.obolibrary.org/obo/UBERON_0002369) |
| `MESH:A02.633`             |              1 | [UBERON:0002385](http://purl.obolibrary.org/obo/UBERON_0002385) |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 28 invalid
xrefs to external prefixed with `ncithesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                                         |   usages_count | usages                                                          |
|-------------------------------------------------------|----------------|-----------------------------------------------------------------|
| `ncithesaurus:Cervix`                                 |              1 | [UBERON:0000002](http://purl.obolibrary.org/obo/UBERON_0000002) |
| `ncithesaurus:Ureter`                                 |              1 | [UBERON:0000056](http://purl.obolibrary.org/obo/UBERON_0000056) |
| `ncithesaurus:Intestine`                              |              1 | [UBERON:0000160](http://purl.obolibrary.org/obo/UBERON_0000160) |
| `ncithesaurus:Breast`                                 |              1 | [UBERON:0000310](http://purl.obolibrary.org/obo/UBERON_0000310) |
| `ncithesaurus:Testis`                                 |              1 | [UBERON:0000473](http://purl.obolibrary.org/obo/UBERON_0000473) |
| `ncithesaurus:Stomach`                                |              1 | [UBERON:0000945](http://purl.obolibrary.org/obo/UBERON_0000945) |
| `ncithesaurus:Brain`                                  |              1 | [UBERON:0000955](http://purl.obolibrary.org/obo/UBERON_0000955) |
| `ncithesaurus:Ovary`                                  |              1 | [UBERON:0000992](http://purl.obolibrary.org/obo/UBERON_0000992) |
| `ncithesaurus:Uterus`                                 |              1 | [UBERON:0000995](http://purl.obolibrary.org/obo/UBERON_0000995) |
| `ncithesaurus:Vulva`                                  |              1 | [UBERON:0000997](http://purl.obolibrary.org/obo/UBERON_0000997) |
| `ncithesaurus:Nervous_System`                         |              1 | [UBERON:0001016](http://purl.obolibrary.org/obo/UBERON_0001016) |
| `ncithesaurus:Esophagus`                              |              1 | [UBERON:0001043](http://purl.obolibrary.org/obo/UBERON_0001043) |
| `ncithesaurus:Anatomic_Structure_System_or_Substance` |              1 | [UBERON:0001062](http://purl.obolibrary.org/obo/UBERON_0001062) |
| `ncithesaurus:Bladder`                                |              1 | [UBERON:0001255](http://purl.obolibrary.org/obo/UBERON_0001255) |
| `ncithesaurus:Pancreas`                               |              1 | [UBERON:0001264](http://purl.obolibrary.org/obo/UBERON_0001264) |
| `ncithesaurus:Bone`                                   |              1 | [UBERON:0001474](http://purl.obolibrary.org/obo/UBERON_0001474) |
| `ncithesaurus:Plasma`                                 |              1 | [UBERON:0001969](http://purl.obolibrary.org/obo/UBERON_0001969) |
| `ncithesaurus:Thyroid_Gland`                          |              1 | [UBERON:0002046](http://purl.obolibrary.org/obo/UBERON_0002046) |
| `ncithesaurus:Lung`                                   |              1 | [UBERON:0002048](http://purl.obolibrary.org/obo/UBERON_0002048) |
| `ncithesaurus:Skin`                                   |              1 | [UBERON:0002097](http://purl.obolibrary.org/obo/UBERON_0002097) |
| `ncithesaurus:Liver`                                  |              1 | [UBERON:0002107](http://purl.obolibrary.org/obo/UBERON_0002107) |
| `ncithesaurus:Gallbladder`                            |              1 | [UBERON:0002110](http://purl.obolibrary.org/obo/UBERON_0002110) |
| `ncithesaurus:Kidney`                                 |              1 | [UBERON:0002113](http://purl.obolibrary.org/obo/UBERON_0002113) |
| `ncithesaurus:Duodenum`                               |              1 | [UBERON:0002114](http://purl.obolibrary.org/obo/UBERON_0002114) |
| `ncithesaurus:Prostate_Gland`                         |              1 | [UBERON:0002367](http://purl.obolibrary.org/obo/UBERON_0002367) |
| `ncithesaurus:Adrenal_Gland`                          |              1 | [UBERON:0002369](http://purl.obolibrary.org/obo/UBERON_0002369) |
| `ncithesaurus:Muscle_Tissue`                          |              1 | [UBERON:0002385](http://purl.obolibrary.org/obo/UBERON_0002385) |
| `ncithesaurus:Head_and_Neck`                          |              1 | [UBERON:0007811](http://purl.obolibrary.org/obo/UBERON_0007811) |

## `PDBeChem`: Chemical Component Dictionary

Overall, there were 2 invalid
xrefs to external prefixed with `PDBeChem` (standardized to Bioregistry
prefix [`pdb-ccd`](https://bioregistry.io/pdb-ccd)) that
did not match the standard pattern `^\w{1,3}$`.

| external_xref       |   usages_count | usages                                                    |
|---------------------|----------------|-----------------------------------------------------------|
| `PDBeChem:GLU_LFOH` |              1 | [CHEBI:16015](http://purl.obolibrary.org/obo/CHEBI_16015) |
| `PDBeChem:ALA_LFOH` |              1 | [CHEBI:16977](http://purl.obolibrary.org/obo/CHEBI_16977) |

## `Reaxys`: Reaxys

Overall, there were 1 invalid
xrefs to external prefixed with `Reaxys` (standardized to Bioregistry
prefix [`reaxys`](https://bioregistry.io/reaxys)) that
did not match the standard pattern `^\d+$`.

| external_xref       |   usages_count | usages                                                    |
|---------------------|----------------|-----------------------------------------------------------|
| `Reaxys:82337-46-0` |              1 | [CHEBI:34144](http://purl.obolibrary.org/obo/CHEBI_34144) |

## `Wikipedia`: Wikipedia

Overall, there were 9 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^\S+$`.

| external_xref                       |   usages_count | usages                                                    |
|-------------------------------------|----------------|-----------------------------------------------------------|
| `Wikipedia:Adenosine triphosphate`  |              1 | [CHEBI:15422](http://purl.obolibrary.org/obo/CHEBI_15422) |
| `Wikipedia:Prostaglandin D2`        |              1 | [CHEBI:15555](http://purl.obolibrary.org/obo/CHEBI_15555) |
| `Wikipedia:Uridine triphosphate`    |              1 | [CHEBI:15713](http://purl.obolibrary.org/obo/CHEBI_15713) |
| `Wikipedia:Succinic acid`           |              1 | [CHEBI:15741](http://purl.obolibrary.org/obo/CHEBI_15741) |
| `Wikipedia:Chenodeoxycholic acid`   |              1 | [CHEBI:16755](http://purl.obolibrary.org/obo/CHEBI_16755) |
| `Wikipedia:Leukotriene C4`          |              1 | [CHEBI:16978](http://purl.obolibrary.org/obo/CHEBI_16978) |
| `Wikipedia:3-Hydroxybutyric acid`   |              1 | [CHEBI:20067](http://purl.obolibrary.org/obo/CHEBI_20067) |
| `Wikipedia:Sphingosine 1-phosphate` |              1 | [CHEBI:37550](http://purl.obolibrary.org/obo/CHEBI_37550) |
| `Wikipedia:Angiotensin II`          |              1 | [CHEBI:48432](http://purl.obolibrary.org/obo/CHEBI_48432) |

