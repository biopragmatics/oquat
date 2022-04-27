# xco

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `xco`. See the [GitHub repository](https://github.com/rat-genome-database/XCO-experimental-condition-ontology).


## `CHEBI`: Chemical Entities of Biological Interest

Overall, there were 7 invalid
xrefs to external prefixed with `CHEBI` (standardized to Bioregistry
entry [`chebi`]((https://bioregistry.io/chebi)) that
did not match the standard pattern `^\d+$`.

| external_xref        |   usages_count | usages                                            |
|----------------------|----------------|---------------------------------------------------|
| `CHEBI:CHEBI:2504`   |              1 | [XCO:0000605](https://bioregistry.io/XCO:0000605) |
| `CHEBI:CHEBI: 15366` |              1 | [XCO:0000607](https://bioregistry.io/XCO:0000607) |
| `CHEBI:CHEBI:73224`  |              1 | [XCO:0000608](https://bioregistry.io/XCO:0000608) |
| `CHEBI:CHEBI:17303`  |              1 | [XCO:0000610](https://bioregistry.io/XCO:0000610) |
| `CHEBI:CHEBI:35705`  |              1 | [XCO:0000636](https://bioregistry.io/XCO:0000636) |
| `CHEBI:CHEBI:4031`   |              1 | [XCO:0000637](https://bioregistry.io/XCO:0000637) |
| `CHEBI:CHEBI:70773`  |              1 | [XCO:0000638](https://bioregistry.io/XCO:0000638) |

## `CHEMBL`: ChEMBL

Overall, there were 4 invalid
xrefs to external prefixed with `CHEMBL` (standardized to Bioregistry
entry [`chembl`]((https://bioregistry.io/chembl)) that
did not match the standard pattern `^CHEMBL\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                  |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CHEMBL:105608` |              3 | [XCO:0000320](https://bioregistry.io/XCO:0000320), [XCO:0000321](https://bioregistry.io/XCO:0000321), [XCO:0000322](https://bioregistry.io/XCO:0000322) |
| `CHEMBL:297362` |              1 | [XCO:0000131](https://bioregistry.io/XCO:0000131)                                                                                                       |

## `DrugBank`: DrugBank

Overall, there were 5 invalid
xrefs to external prefixed with `DrugBank` (standardized to Bioregistry
entry [`drugbank`]((https://bioregistry.io/drugbank)) that
did not match the standard pattern `^DB\d{5}$`.

| external_xref                                    |   usages_count | usages                                            |
|--------------------------------------------------|----------------|---------------------------------------------------|
| `DrugBank:https://www.drugbank.ca/drugs/DB00997` |              1 | [XCO:0000539](https://bioregistry.io/XCO:0000539) |
| `DrugBank:https://www.drugbank.ca/drugs/DB00178` |              1 | [XCO:0000548](https://bioregistry.io/XCO:0000548) |
| `DrugBank:https://www.drugbank.ca/drugs/DB00206` |              1 | [XCO:0000550](https://bioregistry.io/XCO:0000550) |
| `DrugBank:https://www.drugbank.ca/drugs/DB01275` |              1 | [XCO:0000551](https://bioregistry.io/XCO:0000551) |
| `DrugBank:https://www.drugbank.ca/drugs/DB00999` |              1 | [XCO:0000552](https://bioregistry.io/XCO:0000552) |

## `Drugbank`: DrugBank

Overall, there were 5 invalid
xrefs to external prefixed with `Drugbank` (standardized to Bioregistry
entry [`drugbank`]((https://bioregistry.io/drugbank)) that
did not match the standard pattern `^DB\d{5}$`.

| external_xref                                             |   usages_count | usages                                            |
|-----------------------------------------------------------|----------------|---------------------------------------------------|
| `Drugbank:https://www.drugbank.ca/drugs/DB01296`          |              1 | [XCO:0000557](https://bioregistry.io/XCO:0000557) |
| `Drugbank:https://www.drugbank.ca/drugs/DB00790`          |              1 | [XCO:0000588](https://bioregistry.io/XCO:0000588) |
| `Drugbank:https://www.drugbank.ca/drugs/DB01094`          |              1 | [XCO:0000603](https://bioregistry.io/XCO:0000603) |
| `Drugbank:https://www.drugbank.ca/drugs/DB06692`          |              1 | [XCO:0000604](https://bioregistry.io/XCO:0000604) |
| `Drugbank:https://www.drugbank.ca/categories/DBCAT000600` |              1 | [XCO:0000618](https://bioregistry.io/XCO:0000618) |

## `DRUGBANK`: DrugBank

Overall, there were 2 invalid
xrefs to external prefixed with `DRUGBANK` (standardized to Bioregistry
entry [`drugbank`]((https://bioregistry.io/drugbank)) that
did not match the standard pattern `^DB\d{5}$`.

| external_xref                                    |   usages_count | usages                                            |
|--------------------------------------------------|----------------|---------------------------------------------------|
| `DRUGBANK:https://www.drugbank.ca/drugs/DB00421` |              1 | [XCO:0000627](https://bioregistry.io/XCO:0000627) |
| `DRUGBANK:https://www.drugbank.ca/drugs/DB00572` |              1 | [XCO:0000631](https://bioregistry.io/XCO:0000631) |

## `drugbank`: DrugBank

Overall, there were 1 invalid
xrefs to external prefixed with `drugbank` (standardized to Bioregistry
entry [`drugbank`]((https://bioregistry.io/drugbank)) that
did not match the standard pattern `^DB\d{5}$`.

| external_xref                                    |   usages_count | usages                                            |
|--------------------------------------------------|----------------|---------------------------------------------------|
| `drugbank:https://www.drugbank.ca/drugs/DB04883` |              1 | [XCO:0000647](https://bioregistry.io/XCO:0000647) |

## `Medline Plus`: MedlinePlus Health Topics

Overall, there were 1 invalid
xrefs to external prefixed with `Medline Plus` (standardized to Bioregistry
entry [`medlineplus`]((https://bioregistry.io/medlineplus)) that
did not match the standard pattern `^\d+$`.

| external_xref                                       |   usages_count | usages                                            |
|-----------------------------------------------------|----------------|---------------------------------------------------|
| `Medline Plus:http\://www.nlm.nih.gov/medlineplus/` |              1 | [XCO:0000563](https://bioregistry.io/XCO:0000563) |

## `MESH`: Medical Subject Headings

Overall, there were 6 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
entry [`mesh`]((https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                                                                                           |   usages_count | usages                                            |
|---------------------------------------------------------------------------------------------------------|----------------|---------------------------------------------------|
| `MESH:https://meshb.nlm.nih.gov/record/ui?ui=D008550`                                                   |              1 | [XCO:0000559](https://bioregistry.io/XCO:0000559) |
| `MESH:https://meshb.nlm.nih.gov/record/ui?ui=D009543`                                                   |              1 | [XCO:0000611](https://bioregistry.io/XCO:0000611) |
| `MESH:https://www.ncbi.nlm.nih.gov/mesh/68020889`                                                       |              1 | [XCO:0000614](https://bioregistry.io/XCO:0000614) |
| `MESH:https://www.ncbi.nlm.nih.gov/mesh?Db=mesh&Cmd=DetailsSearch&Term=%22Verapamil%22%5BMeSH+Terms%5D` |              1 | [XCO:0000616](https://bioregistry.io/XCO:0000616) |
| `MESH:https://www.ncbi.nlm.nih.gov/mesh/68011802`                                                       |              1 | [XCO:0000617](https://bioregistry.io/XCO:0000617) |
| `MESH:https://www.ncbi.nlm.nih.gov/mesh/68016686`                                                       |              1 | [XCO:0000642](https://bioregistry.io/XCO:0000642) |

## `NCI Thesaurus`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCI Thesaurus` (standardized to Bioregistry
entry [`ncit`]((https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                                                                                                           |   usages_count | usages                                            |
|-------------------------------------------------------------------------------------------------------------------------|----------------|---------------------------------------------------|
| `NCI Thesaurus:https://ncit-stage.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&code=C930&ns=ncit` |              1 | [XCO:0000620](https://bioregistry.io/XCO:0000620) |

## `PMID`: PubMed

Overall, there were 4 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
entry [`pubmed`]((https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref        |   usages_count | usages                                            |
|----------------------|----------------|---------------------------------------------------|
| `PMID:PMID:25312437` |              1 | [XCO:0000587](https://bioregistry.io/XCO:0000587) |
| `PMID:PMID: 7609754` |              1 | [XCO:0000612](https://bioregistry.io/XCO:0000612) |
| `PMID:PMID:15894899` |              1 | [XCO:0000635](https://bioregistry.io/XCO:0000635) |
| `PMID:PMID:27671317` |              1 | [XCO:0000639](https://bioregistry.io/XCO:0000639) |

## `PubChem_Compound`: PubChem CID

Overall, there were 5 invalid
xrefs to external prefixed with `PubChem_Compound` (standardized to Bioregistry
entry [`pubchem.compound`]((https://bioregistry.io/pubchem.compound)) that
did not match the standard pattern `^\d+$`.

| external_xref                |   usages_count | usages                                                                                                                                                  |
|------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PubChem_Compound:CID_13157` |              3 | [XCO:0000344](https://bioregistry.io/XCO:0000344), [XCO:0000436](https://bioregistry.io/XCO:0000436), [XCO:0000437](https://bioregistry.io/XCO:0000437) |
| `PubChem_Compound:CID_12967` |              2 | [XCO:0000345](https://bioregistry.io/XCO:0000345), [XCO:0000346](https://bioregistry.io/XCO:0000346)                                                    |

## `RGD`: Rat Genome Database

Overall, there were 44 invalid
xrefs to external prefixed with `RGD` (standardized to Bioregistry
entry [`rgd`]((https://bioregistry.io/rgd)) that
did not match the standard pattern `^\d{4,}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                             |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RGD:MS`        |             27 | [XCO:0000009](https://bioregistry.io/XCO:0000009), [XCO:0000010](https://bioregistry.io/XCO:0000010), [XCO:0000012](https://bioregistry.io/XCO:0000012), [XCO:0000014](https://bioregistry.io/XCO:0000014), [XCO:0000015](https://bioregistry.io/XCO:0000015), ... |
| `RGD:JRS`       |             15 | [XCO:0000120](https://bioregistry.io/XCO:0000120), [XCO:0000133](https://bioregistry.io/XCO:0000133), [XCO:0000152](https://bioregistry.io/XCO:0000152), [XCO:0000153](https://bioregistry.io/XCO:0000153), [XCO:0000158](https://bioregistry.io/XCO:0000158), ... |
| `RGD:SL`        |              1 | [XCO:0000138](https://bioregistry.io/XCO:0000138)                                                                                                                                                                                                                  |
| `RGD:MRD`       |              1 | [XCO:0000166](https://bioregistry.io/XCO:0000166)                                                                                                                                                                                                                  |

## `Wikipedia`: Wikipedia

Overall, there were 176 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
entry [`wikipedia.en`]((https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                                                                      |   usages_count | usages                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Wikipedia:http://en.wikipedia.org/wiki/Electromagnetic_Radiation`                                 |              6 | [XCO:0000042](https://bioregistry.io/XCO:0000042), [XCO:0000043](https://bioregistry.io/XCO:0000043), [XCO:0000045](https://bioregistry.io/XCO:0000045), [XCO:0000046](https://bioregistry.io/XCO:0000046), [XCO:0000179](https://bioregistry.io/XCO:0000179), ... |
| `Wikipedia:http://en.wikipedia.org/wiki/Nitrosourea`                                               |              6 | [XCO:0000343](https://bioregistry.io/XCO:0000343), [XCO:0000344](https://bioregistry.io/XCO:0000344), [XCO:0000345](https://bioregistry.io/XCO:0000345), [XCO:0000346](https://bioregistry.io/XCO:0000346), [XCO:0000436](https://bioregistry.io/XCO:0000436), ... |
| `Wikipedia:http://en.wikipedia.org/wiki/11-Deoxycorticosterone`                                    |              4 | [XCO:0000192](https://bioregistry.io/XCO:0000192), [XCO:0000328](https://bioregistry.io/XCO:0000328), [XCO:0000329](https://bioregistry.io/XCO:0000329), [XCO:0000330](https://bioregistry.io/XCO:0000330)                                                         |
| `Wikipedia:http://en.wikipedia.org/wiki/Ionizing_radiation`                                        |              3 | [XCO:0000039](https://bioregistry.io/XCO:0000039), [XCO:0000041](https://bioregistry.io/XCO:0000041), [XCO:0000179](https://bioregistry.io/XCO:0000179)                                                                                                            |
| `Wikipedia:http://en.eikipedia.org/wiki/`                                                          |              3 | [XCO:0000119](https://bioregistry.io/XCO:0000119), [XCO:0000123](https://bioregistry.io/XCO:0000123), [XCO:0000124](https://bioregistry.io/XCO:0000124)                                                                                                            |
| `Wikipedia:http://en.wikipedia.org/wiki/Saline_%28medicine%29#Normal`                              |              3 | [XCO:0000147](https://bioregistry.io/XCO:0000147), [XCO:0000148](https://bioregistry.io/XCO:0000148), [XCO:0000215](https://bioregistry.io/XCO:0000215)                                                                                                            |
| `Wikipedia:http://en.wikipedia.org/wiki/Acetylaminofluorene`                                       |              3 | [XCO:0000208](https://bioregistry.io/XCO:0000208), [XCO:0000441](https://bioregistry.io/XCO:0000441), [XCO:0000442](https://bioregistry.io/XCO:0000442)                                                                                                            |
| `Wikipedia:http://en.wikipedia.org/wiki/Hexamethonium`                                             |              3 | [XCO:0000320](https://bioregistry.io/XCO:0000320), [XCO:0000321](https://bioregistry.io/XCO:0000321), [XCO:0000322](https://bioregistry.io/XCO:0000322)                                                                                                            |
| `Wikipedia:http://en.wikipedia.org/wiki/RU28362`                                                   |              3 | [XCO:0000331](https://bioregistry.io/XCO:0000331), [XCO:0000332](https://bioregistry.io/XCO:0000332), [XCO:0000333](https://bioregistry.io/XCO:0000333)                                                                                                            |
| `Wikipedia:http://en.wikipedia.org/wiki/Dexamethasone`                                             |              3 | [XCO:0000372](https://bioregistry.io/XCO:0000372), [XCO:0000443](https://bioregistry.io/XCO:0000443), [XCO:0000444](https://bioregistry.io/XCO:0000444)                                                                                                            |
| `Wikipedia:http://en.wikipedia.org/wiki/Bisphenol_A`                                               |              3 | [XCO:0000397](https://bioregistry.io/XCO:0000397), [XCO:0000404](https://bioregistry.io/XCO:0000404), [XCO:0000406](https://bioregistry.io/XCO:0000406)                                                                                                            |
| `Wikipedia:http://en.wikipedia.org/wiki/Metformin`                                                 |              3 | [XCO:0000408](https://bioregistry.io/XCO:0000408), [XCO:0000409](https://bioregistry.io/XCO:0000409), [XCO:0000410](https://bioregistry.io/XCO:0000410)                                                                                                            |
| `Wikipedia:http://en.wikipedia.org/wiki/Streptococcus_pneumoniae`                                  |              3 | [XCO:0000476](https://bioregistry.io/XCO:0000476), [XCO:0000477](https://bioregistry.io/XCO:0000477), [XCO:0000478](https://bioregistry.io/XCO:0000478)                                                                                                            |
| `Wikipedia:http://en.wikipedia.org/wiki/Haemophilus_influenzae`                                    |              3 | [XCO:0000479](https://bioregistry.io/XCO:0000479), [XCO:0000480](https://bioregistry.io/XCO:0000480), [XCO:0000481](https://bioregistry.io/XCO:0000481)                                                                                                            |
| `Wikipedia:https://en.wikipedia.org/wiki/Metoprolol`                                               |              3 | [XCO:0000514](https://bioregistry.io/XCO:0000514), [XCO:0000515](https://bioregistry.io/XCO:0000515), [XCO:0000516](https://bioregistry.io/XCO:0000516)                                                                                                            |
| `Wikipedia:http://en.wikipedia.org/wiki/Surgery`                                                   |              2 | [XCO:0000165](https://bioregistry.io/XCO:0000165), [XCO:0000318](https://bioregistry.io/XCO:0000318)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Calcium`                                                   |              2 | [XCO:0000184](https://bioregistry.io/XCO:0000184), [XCO:0000185](https://bioregistry.io/XCO:0000185)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Captopril`                                                 |              2 | [XCO:0000270](https://bioregistry.io/XCO:0000270), [XCO:0000382](https://bioregistry.io/XCO:0000382)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Adrenal_gland`                                             |              2 | [XCO:0000334](https://bioregistry.io/XCO:0000334), [XCO:0000335](https://bioregistry.io/XCO:0000335)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Nanoparticle`                                              |              2 | [XCO:0000338](https://bioregistry.io/XCO:0000338), [XCO:0000339](https://bioregistry.io/XCO:0000339)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/4-Nitroquinoline_1-oxide`                                  |              2 | [XCO:0000351](https://bioregistry.io/XCO:0000351), [XCO:0000395](https://bioregistry.io/XCO:0000395)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Methylnitronitrosoguanidine`                               |              2 | [XCO:0000354](https://bioregistry.io/XCO:0000354), [XCO:0000355](https://bioregistry.io/XCO:0000355)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Trichinella_spiralis`                                      |              2 | [XCO:0000370](https://bioregistry.io/XCO:0000370), [XCO:0000371](https://bioregistry.io/XCO:0000371)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Cisplatin`                                                 |              2 | [XCO:0000398](https://bioregistry.io/XCO:0000398), [XCO:0000405](https://bioregistry.io/XCO:0000405)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Fructose`                                                  |              2 | [XCO:0000428](https://bioregistry.io/XCO:0000428), [XCO:0000429](https://bioregistry.io/XCO:0000429)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Retinyl_palmitate`                                         |              2 | [XCO:0000456](https://bioregistry.io/XCO:0000456), [XCO:0000458](https://bioregistry.io/XCO:0000458)                                                                                                                                                               |
| `Wikipedia:https://en.wikipedia.org/wiki/Neurostimulation`                                         |              2 | [XCO:0000521](https://bioregistry.io/XCO:0000521), [XCO:0000522](https://bioregistry.io/XCO:0000522)                                                                                                                                                               |
| `Wikipedia:https://en.wikipedia.org/wiki/Enalapril`                                                |              2 | [XCO:0000542](https://bioregistry.io/XCO:0000542), [XCO:0000677](https://bioregistry.io/XCO:0000677)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Gamma_ray`                                                 |              1 | [XCO:0000040](https://bioregistry.io/XCO:0000040)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Non-ionizing_radiation`                                    |              1 | [XCO:0000044](https://bioregistry.io/XCO:0000044)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Caffeine`                                                  |              1 | [XCO:0000074](https://bioregistry.io/XCO:0000074)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Steroid`                                                   |              1 | [XCO:0000091](https://bioregistry.io/XCO:0000091)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Estradiol`                                                 |              1 | [XCO:0000092](https://bioregistry.io/XCO:0000092)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Ketamine`                                                  |              1 | [XCO:0000130](https://bioregistry.io/XCO:0000130)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Xylazine`                                                  |              1 | [XCO:0000131](https://bioregistry.io/XCO:0000131)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Acepromazine`                                              |              1 | [XCO:0000132](https://bioregistry.io/XCO:0000132)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Methacholine`                                              |              1 | [XCO:0000134](https://bioregistry.io/XCO:0000134)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Sodium_nitroprusside`                                      |              1 | [XCO:0000142](https://bioregistry.io/XCO:0000142)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Acetylcholine`                                             |              1 | [XCO:0000143](https://bioregistry.io/XCO:0000143)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Phenylephrine`                                             |              1 | [XCO:0000145](https://bioregistry.io/XCO:0000145)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Saline_%28medicine%29`                                     |              1 | [XCO:0000156](https://bioregistry.io/XCO:0000156)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Thrombin`                                                  |              1 | [XCO:0000177](https://bioregistry.io/XCO:0000177)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Thapsigargin`                                              |              1 | [XCO:0000178](https://bioregistry.io/XCO:0000178)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Ultraviolet`                                               |              1 | [XCO:0000180](https://bioregistry.io/XCO:0000180)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Trimethaphan_camsylate`                                    |              1 | [XCO:0000187](https://bioregistry.io/XCO:0000187)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Darodipine`                                                |              1 | [XCO:0000188](https://bioregistry.io/XCO:0000188)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Glibenclamide`                                             |              1 | [XCO:0000196](https://bioregistry.io/XCO:0000196)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Alpha-Ketoisocaproic_acid`                                 |              1 | [XCO:0000200](https://bioregistry.io/XCO:0000200)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Ruthenium_red`                                             |              1 | [XCO:0000224](https://bioregistry.io/XCO:0000224)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Potassium_channel`                                         |              1 | [XCO:0000225](https://bioregistry.io/XCO:0000225)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Apamin`                                                    |              1 | [XCO:0000226](https://bioregistry.io/XCO:0000226)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Charybdotoxin`                                             |              1 | [XCO:0000227](https://bioregistry.io/XCO:0000227)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Streptozotocin`                                            |              1 | [XCO:0000241](https://bioregistry.io/XCO:0000241)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Alloxan`                                                   |              1 | [XCO:0000242](https://bioregistry.io/XCO:0000242)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Tolbutamide`                                               |              1 | [XCO:0000252](https://bioregistry.io/XCO:0000252)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Isoprenaline#Chemistry`                                    |              1 | [XCO:0000256](https://bioregistry.io/XCO:0000256)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Balloon_angioplasty`                                       |              1 | [XCO:0000268](https://bioregistry.io/XCO:0000268)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/4-Hydroxy-TEMPO`                                           |              1 | [XCO:0000272](https://bioregistry.io/XCO:0000272)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Carrageenan`                                               |              1 | [XCO:0000273](https://bioregistry.io/XCO:0000273)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Terpene`                                                   |              1 | [XCO:0000279](https://bioregistry.io/XCO:0000279)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Squalene`                                                  |              1 | [XCO:0000280](https://bioregistry.io/XCO:0000280)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Collagen`                                                  |              1 | [XCO:0000281](https://bioregistry.io/XCO:0000281)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/CD90`                                                      |              1 | [XCO:0000282](https://bioregistry.io/XCO:0000282)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Technetium_%2899mTc%29_sestamibi`                          |              1 | [XCO:0000293](https://bioregistry.io/XCO:0000293)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Estrogen`                                                  |              1 | [XCO:0000294](https://bioregistry.io/XCO:0000294)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Diethylstilbestrol`                                        |              1 | [XCO:0000295](https://bioregistry.io/XCO:0000295)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Adrenergic_receptors`                                      |              1 | [XCO:0000336](https://bioregistry.io/XCO:0000336)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Titanium_dioxide`                                          |              1 | [XCO:0000339](https://bioregistry.io/XCO:0000339)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Propyl`                                                    |              1 | [XCO:0000344](https://bioregistry.io/XCO:0000344)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Ethyl_group`                                               |              1 | [XCO:0000345](https://bioregistry.io/XCO:0000345)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Methyl_group`                                              |              1 | [XCO:0000346](https://bioregistry.io/XCO:0000346)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/N-Methyl-N-nitrosourea`                                    |              1 | [XCO:0000346](https://bioregistry.io/XCO:0000346)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Middle_Cerebral_Artery`                                    |              1 | [XCO:0000348](https://bioregistry.io/XCO:0000348)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Streptococcus`                                             |              1 | [XCO:0000350](https://bioregistry.io/XCO:0000350)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Quinoline`                                                 |              1 | [XCO:0000351](https://bioregistry.io/XCO:0000351)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Aminohippuric_acid`                                        |              1 | [XCO:0000359](https://bioregistry.io/XCO:0000359)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Losartan`                                                  |              1 | [XCO:0000383](https://bioregistry.io/XCO:0000383)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/TEMPOL`                                                    |              1 | [XCO:0000384](https://bioregistry.io/XCO:0000384)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Antimetabolite`                                            |              1 | [XCO:0000390](https://bioregistry.io/XCO:0000390)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Bromodeoxyuridine`                                         |              1 | [XCO:0000391](https://bioregistry.io/XCO:0000391)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Nucleotide`                                                |              1 | [XCO:0000392](https://bioregistry.io/XCO:0000392)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/1,2-dimethylhydrazine`                                     |              1 | [XCO:0000393](https://bioregistry.io/XCO:0000393)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Habituation`                                               |              1 | [XCO:0000402](https://bioregistry.io/XCO:0000402)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Thymoquinone`                                              |              1 | [XCO:0000423](https://bioregistry.io/XCO:0000423)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Benfotiamine`                                              |              1 | [XCO:0000424](https://bioregistry.io/XCO:0000424)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Lactoferrin`                                               |              1 | [XCO:0000425](https://bioregistry.io/XCO:0000425)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Pyrazole`                                                  |              1 | [XCO:0000426](https://bioregistry.io/XCO:0000426)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Lycopene`                                                  |              1 | [XCO:0000427](https://bioregistry.io/XCO:0000427)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Candesartan`                                               |              1 | [XCO:0000438](https://bioregistry.io/XCO:0000438)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Phosphate_buffered_saline`                                 |              1 | [XCO:0000445](https://bioregistry.io/XCO:0000445)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Herpes_simplex_virus`                                      |              1 | [XCO:0000451](https://bioregistry.io/XCO:0000451)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Vitamin_A`                                                 |              1 | [XCO:0000468](https://bioregistry.io/XCO:0000468)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Retinoid`                                                  |              1 | [XCO:0000469](https://bioregistry.io/XCO:0000469)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Flavonoid`                                                 |              1 | [XCO:0000470](https://bioregistry.io/XCO:0000470)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Naringenin`                                                |              1 | [XCO:0000473](https://bioregistry.io/XCO:0000473)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Alendronic_acid`                                           |              1 | [XCO:0000474](https://bioregistry.io/XCO:0000474)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Ceftriaxone`                                               |              1 | [XCO:0000484](https://bioregistry.io/XCO:0000484)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Carprofen`                                                |              1 | [XCO:0000507](https://bioregistry.io/XCO:0000507)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Ester`                                                    |              1 | [XCO:0000511](https://bioregistry.io/XCO:0000511)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Teratology`                                               |              1 | [XCO:0000512](https://bioregistry.io/XCO:0000512)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Dibutyl_phthalate`                                        |              1 | [XCO:0000513](https://bioregistry.io/XCO:0000513)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Neuromodulation_(medicine)`                               |              1 | [XCO:0000520](https://bioregistry.io/XCO:0000520)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Common_peroneal_nerve`                                    |              1 | [XCO:0000522](https://bioregistry.io/XCO:0000522)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/ACE_inhibitor`                                            |              1 | [XCO:0000524](https://bioregistry.io/XCO:0000524)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Benazepril`                                               |              1 | [XCO:0000525](https://bioregistry.io/XCO:0000525)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Protein_synthesis_inhibitor`                              |              1 | [XCO:0000532](https://bioregistry.io/XCO:0000532)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Puromycin`                                                |              1 | [XCO:0000533](https://bioregistry.io/XCO:0000533)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Sunitinib`                                                |              1 | [XCO:0000534](https://bioregistry.io/XCO:0000534)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Angiotensin_II_receptor_blocker`                          |              1 | [XCO:0000536](https://bioregistry.io/XCO:0000536)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Olmesartan`                                               |              1 | [XCO:0000537](https://bioregistry.io/XCO:0000537)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Temocapril`                                               |              1 | [XCO:0000538](https://bioregistry.io/XCO:0000538)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Doxorubicin`                                              |              1 | [XCO:0000539](https://bioregistry.io/XCO:0000539)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Delapril`                                                 |              1 | [XCO:0000540](https://bioregistry.io/XCO:0000540)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Bosentan`                                                 |              1 | [XCO:0000541](https://bioregistry.io/XCO:0000541)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Vitamin_D`                                                |              1 | [XCO:0000543](https://bioregistry.io/XCO:0000543)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Ergocalciferol`                                           |              1 | [XCO:0000544](https://bioregistry.io/XCO:0000544)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Cholecalciferol`                                          |              1 | [XCO:0000545](https://bioregistry.io/XCO:0000545)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Analog`                                                   |              1 | [XCO:0000546](https://bioregistry.io/XCO:0000546)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Paricalcitol`                                             |              1 | [XCO:0000547](https://bioregistry.io/XCO:0000547)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Anterior_interventricular_branch_of_left_coronary_artery` |              1 | [XCO:0000549](https://bioregistry.io/XCO:0000549)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Reserpine`                                                |              1 | [XCO:0000550](https://bioregistry.io/XCO:0000550)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Everolimus`                                               |              1 | [XCO:0000553](https://bioregistry.io/XCO:0000553)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Meclofenamic_acid`                                        |              1 | [XCO:0000564](https://bioregistry.io/XCO:0000564)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Ipragliflozin`                                            |              1 | [XCO:0000565](https://bioregistry.io/XCO:0000565)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Meropenem`                                                |              1 | [XCO:0000575](https://bioregistry.io/XCO:0000575)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Thiobutabarbital`                                         |              1 | [XCO:0000624](https://bioregistry.io/XCO:0000624)                                                                                                                                                                                                                  |

## `wikipedia`: Wikipedia

Overall, there were 1 invalid
xrefs to external prefixed with `wikipedia` (standardized to Bioregistry
entry [`wikipedia.en`]((https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                      |   usages_count | usages                                            |
|----------------------------------------------------|----------------|---------------------------------------------------|
| `wikipedia:https://en.wikipedia.org/wiki/Cortisol` |              1 | [XCO:0000633](https://bioregistry.io/XCO:0000633) |

