# mmo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `mmo`. See the [GitHub repository](https://github.com/rat-genome-database/MMO-Measurement-Method-Ontology)


## `ECO`: Evidence ontology

- Normalized prefix: `eco`
- [https://bioregistry.io/eco](https://bioregistry.io/eco)
- Pattern:`^\d{7}$`

| identifier        |   appearances | examples                                          |
|-------------------|---------------|---------------------------------------------------|
| `ECO:ECO:0001010` |             1 | [MMO:0000678](https://bioregistry.io/MMO:0000678) |
| `ECO:ECO:0000004` |             1 | [MMO:0000679](https://bioregistry.io/MMO:0000679) |
| `ECO:ECO:0000230` |             1 | [MMO:0000680](https://bioregistry.io/MMO:0000680) |
| `ECO:ECO:0000102` |             1 | [MMO:0000681](https://bioregistry.io/MMO:0000681) |
| `ECO:ECO:0000085` |             1 | [MMO:0000682](https://bioregistry.io/MMO:0000682) |
| `ECO:ECO:0000070` |             1 | [MMO:0000683](https://bioregistry.io/MMO:0000683) |
| `ECO:ECO:0001049` |             1 | [MMO:0000684](https://bioregistry.io/MMO:0000684) |
| `ECO:ECO:0005587` |             1 | [MMO:0000685](https://bioregistry.io/MMO:0000685) |
| `ECO:ECO:0005600` |             1 | [MMO:0000686](https://bioregistry.io/MMO:0000686) |

## `efo`: Experimental Factor Ontology

- Normalized prefix: `efo`
- [https://bioregistry.io/efo](https://bioregistry.io/efo)
- Pattern:`^\d{7}$`

| identifier        |   appearances | examples                                          |
|-------------------|---------------|---------------------------------------------------|
| `efo:EFO_0001458` |             1 | [MMO:0000642](https://bioregistry.io/MMO:0000642) |
| `efo:EFO_0002768` |             1 | [MMO:0000648](https://bioregistry.io/MMO:0000648) |
| `efo:EFO_0002943` |             1 | [MMO:0000655](https://bioregistry.io/MMO:0000655) |
| `efo:EFO_0002770` |             1 | [MMO:0000659](https://bioregistry.io/MMO:0000659) |
| `efo:EFO_0008896` |             1 | [MMO:0000659](https://bioregistry.io/MMO:0000659) |
| `efo:EFO_0002941` |             1 | [MMO:0000660](https://bioregistry.io/MMO:0000660) |
| `efo:EFO_0000561` |             1 | [MMO:0000672](https://bioregistry.io/MMO:0000672) |

## `MESH`: Medical Subject Headings

- Normalized prefix: `mesh`
- [https://bioregistry.io/mesh](https://bioregistry.io/mesh)
- Pattern:`^(C|D)\d{6,9}$`

| identifier                                            |   appearances | examples                                          |
|-------------------------------------------------------|---------------|---------------------------------------------------|
| `MESH:https://meshb.nlm.nih.gov/record/ui?ui=D009543` |             1 | [MMO:0000697](https://bioregistry.io/MMO:0000697) |

## `PMID`: PubMed

- Normalized prefix: `pubmed`
- [https://bioregistry.io/pubmed](https://bioregistry.io/pubmed)
- Pattern:`^\d+$`

| identifier          |   appearances | examples                                          |
|---------------------|---------------|---------------------------------------------------|
| `PMID:PMID:3411196` |             1 | [MMO:0000695](https://bioregistry.io/MMO:0000695) |

## `RGD`: Rat Genome Database

- Normalized prefix: `rgd`
- [https://bioregistry.io/rgd](https://bioregistry.io/rgd)
- Pattern:`^\d{4,}$`

| identifier   |   appearances | examples                                                                                                                                                                                                                                                           |
|--------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RGD:JRS`    |            29 | [MMO:0000223](https://bioregistry.io/MMO:0000223), [MMO:0000257](https://bioregistry.io/MMO:0000257), [MMO:0000260](https://bioregistry.io/MMO:0000260), [MMO:0000276](https://bioregistry.io/MMO:0000276), [MMO:0000502](https://bioregistry.io/MMO:0000502), ... |
| `RGD:MS`     |             5 | [MMO:0000081](https://bioregistry.io/MMO:0000081), [MMO:0000097](https://bioregistry.io/MMO:0000097), [MMO:0000104](https://bioregistry.io/MMO:0000104), [MMO:0000137](https://bioregistry.io/MMO:0000137), [MMO:0000160](https://bioregistry.io/MMO:0000160)      |
| `RGD:SL`     |             1 | [MMO:0000132](https://bioregistry.io/MMO:0000132)                                                                                                                                                                                                                  |
| `RGD:SJL`    |             1 | [MMO:0000448](https://bioregistry.io/MMO:0000448)                                                                                                                                                                                                                  |
| `RGD:GTH`    |             1 | [MMO:0000497](https://bioregistry.io/MMO:0000497)                                                                                                                                                                                                                  |

## `Wikipedia`: Wikipedia

- Normalized prefix: `wikipedia.en`
- [https://bioregistry.io/wikipedia.en](https://bioregistry.io/wikipedia.en)
- Pattern:`^[A-Za-z-0-9_]+$`

| identifier                                                                                    |   appearances | examples                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Wikipedia:http://en.wikipedia.org/wiki/Lipoprotein`                                          |            10 | [MMO:0000478](https://bioregistry.io/MMO:0000478), [MMO:0000485](https://bioregistry.io/MMO:0000485), [MMO:0000486](https://bioregistry.io/MMO:0000486), [MMO:0000488](https://bioregistry.io/MMO:0000488), [MMO:0000488](https://bioregistry.io/MMO:0000488), ... |
| `Wikipedia:http://en.wikipedia.org/wiki/`                                                     |             9 | [MMO:0000023](https://bioregistry.io/MMO:0000023), [MMO:0000079](https://bioregistry.io/MMO:0000079), [MMO:0000113](https://bioregistry.io/MMO:0000113), [MMO:0000164](https://bioregistry.io/MMO:0000164), [MMO:0000204](https://bioregistry.io/MMO:0000204), ... |
| `Wikipedia:http://en.wikipedia.org/wiki/Urine_test_strip`                                     |             9 | [MMO:0000153](https://bioregistry.io/MMO:0000153), [MMO:0000171](https://bioregistry.io/MMO:0000171), [MMO:0000187](https://bioregistry.io/MMO:0000187), [MMO:0000464](https://bioregistry.io/MMO:0000464), [MMO:0000464](https://bioregistry.io/MMO:0000464), ... |
| `Wikipedia:http://en.wikipedia.org/wiki/Visible_spectrum`                                     |             7 | [MMO:0000111](https://bioregistry.io/MMO:0000111), [MMO:0000220](https://bioregistry.io/MMO:0000220), [MMO:0000419](https://bioregistry.io/MMO:0000419), [MMO:0000420](https://bioregistry.io/MMO:0000420), [MMO:0000422](https://bioregistry.io/MMO:0000422), ... |
| `Wikipedia:http://en.wikipedia.org/wiki/Intermediate-density_lipoprotein`                     |             6 | [MMO:0000473](https://bioregistry.io/MMO:0000473), [MMO:0000474](https://bioregistry.io/MMO:0000474), [MMO:0000474](https://bioregistry.io/MMO:0000474), [MMO:0000476](https://bioregistry.io/MMO:0000476), [MMO:0000484](https://bioregistry.io/MMO:0000484), ... |
| `Wikipedia:http://en.wikipedia.org/wiki/Jaffe_reaction`                                       |             5 | [MMO:0000542](https://bioregistry.io/MMO:0000542), [MMO:0000543](https://bioregistry.io/MMO:0000543), [MMO:0000544](https://bioregistry.io/MMO:0000544), [MMO:0000545](https://bioregistry.io/MMO:0000545), [MMO:0000546](https://bioregistry.io/MMO:0000546)      |
| `Wikipedia:http://en.wikipedia.org/wiki/Quantitative_computed_tomography`                     |             4 | [MMO:0000364](https://bioregistry.io/MMO:0000364), [MMO:0000365](https://bioregistry.io/MMO:0000365), [MMO:0000367](https://bioregistry.io/MMO:0000367), [MMO:0000508](https://bioregistry.io/MMO:0000508)                                                         |
| `Wikipedia:http://en.wikipedia.org/wiki/Ion_selective_electrode`                              |             4 | [MMO:0000450](https://bioregistry.io/MMO:0000450), [MMO:0000451](https://bioregistry.io/MMO:0000451), [MMO:0000452](https://bioregistry.io/MMO:0000452), [MMO:0000453](https://bioregistry.io/MMO:0000453)                                                         |
| `Wikipedia:http://en.wikipedia.org/wiki/Calipers`                                             |             4 | [MMO:0000514](https://bioregistry.io/MMO:0000514), [MMO:0000515](https://bioregistry.io/MMO:0000515), [MMO:0000516](https://bioregistry.io/MMO:0000516), [MMO:0000517](https://bioregistry.io/MMO:0000517)                                                         |
| `Wikipedia:http://en.wikipedia.org/wiki/Campesterol`                                          |             4 | [MMO:0000520](https://bioregistry.io/MMO:0000520), [MMO:0000524](https://bioregistry.io/MMO:0000524), [MMO:0000525](https://bioregistry.io/MMO:0000525), [MMO:0000531](https://bioregistry.io/MMO:0000531)                                                         |
| `Wikipedia:http://en.wikipedia.org/wiki/Sitosterol`                                           |             4 | [MMO:0000521](https://bioregistry.io/MMO:0000521), [MMO:0000522](https://bioregistry.io/MMO:0000522), [MMO:0000523](https://bioregistry.io/MMO:0000523), [MMO:0000532](https://bioregistry.io/MMO:0000532)                                                         |
| `Wikipedia:https://en.wikipedia.org/wiki/High_throughput_biology`                             |             3 | [MMO:0000644](https://bioregistry.io/MMO:0000644), [MMO:0000664](https://bioregistry.io/MMO:0000664), [MMO:0000665](https://bioregistry.io/MMO:0000665)                                                                                                            |
| `Wikipedia:http://en.wikipedia.org/wiki/Atomic_absorption_spectroscopy`                       |             2 | [MMO:0000232](https://bioregistry.io/MMO:0000232), [MMO:0000379](https://bioregistry.io/MMO:0000379)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Hemocytometer`                                        |             2 | [MMO:0000368](https://bioregistry.io/MMO:0000368), [MMO:0000447](https://bioregistry.io/MMO:0000447)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Radial_immunodiffusion`                               |             2 | [MMO:0000439](https://bioregistry.io/MMO:0000439), [MMO:0000440](https://bioregistry.io/MMO:0000440)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Polymerase_Chain_Reaction`                            |             2 | [MMO:0000461](https://bioregistry.io/MMO:0000461), [MMO:0000462](https://bioregistry.io/MMO:0000462)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Colony-forming_unit#Tools_for_counting_colonies`      |             2 | [MMO:0000563](https://bioregistry.io/MMO:0000563), [MMO:0000564](https://bioregistry.io/MMO:0000564)                                                                                                                                                               |
| `Wikipedia:https://en.wikipedia.org/wiki/SHIRPA`                                              |             2 | [MMO:0000598](https://bioregistry.io/MMO:0000598), [MMO:0000599](https://bioregistry.io/MMO:0000599)                                                                                                                                                               |
| `Wikipedia:https://en.wikipedia.org/wiki/Gene_expression`                                     |             2 | [MMO:0000640](https://bioregistry.io/MMO:0000640), [MMO:0000643](https://bioregistry.io/MMO:0000643)                                                                                                                                                               |
| `Wikipedia:https://en.wikipedia.org/wiki/Microarray`                                          |             2 | [MMO:0000648](https://bioregistry.io/MMO:0000648), [MMO:0000649](https://bioregistry.io/MMO:0000649)                                                                                                                                                               |
| `Wikipedia:https://en.wikipedia.org/wiki/Nuclease_protection_assay`                           |             2 | [MMO:0000651](https://bioregistry.io/MMO:0000651), [MMO:0000652](https://bioregistry.io/MMO:0000652)                                                                                                                                                               |
| `Wikipedia:http://en.wikipedia.org/wiki/Hydrostatic_weighing`                                 |             1 | [MMO:0000091](https://bioregistry.io/MMO:0000091)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Thromboelastometry`                                   |             1 | [MMO:0000099](https://bioregistry.io/MMO:0000099)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Caliper`                                              |             1 | [MMO:0000159](https://bioregistry.io/MMO:0000159)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Sphygmomanometry`                                     |             1 | [MMO:0000201](https://bioregistry.io/MMO:0000201)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Ultrasonic_flow_meter`                                |             1 | [MMO:0000228](https://bioregistry.io/MMO:0000228)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Inductively_coupled_plasma`                           |             1 | [MMO:0000231](https://bioregistry.io/MMO:0000231)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Liquid_scintillation_counting`                        |             1 | [MMO:0000238](https://bioregistry.io/MMO:0000238)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Chromatography#Thin_layer_chromatography`             |             1 | [MMO:0000289](https://bioregistry.io/MMO:0000289)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Electrophysiology`                                    |             1 | [MMO:0000291](https://bioregistry.io/MMO:0000291)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Patch_clamp`                                          |             1 | [MMO:0000292](https://bioregistry.io/MMO:0000292)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Patch_clamp#Whole-cell_recording_or_whole-cell_patch` |             1 | [MMO:0000293](https://bioregistry.io/MMO:0000293)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Glucose_tolerance_test`                               |             1 | [MMO:0000326](https://bioregistry.io/MMO:0000326)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Solid_%28state_of_matter%29`                          |             1 | [MMO:0000328](https://bioregistry.io/MMO:0000328)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Western_blot`                                         |             1 | [MMO:0000338](https://bioregistry.io/MMO:0000338)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Southern_blot`                                        |             1 | [MMO:0000340](https://bioregistry.io/MMO:0000340)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Graphite_furnace_atomic_absorption`                   |             1 | [MMO:0000380](https://bioregistry.io/MMO:0000380)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Gadolinium`                                           |             1 | [MMO:0000384](https://bioregistry.io/MMO:0000384)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Electroanalytical_Methods`                            |             1 | [MMO:0000386](https://bioregistry.io/MMO:0000386)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Clark_electrode`                                      |             1 | [MMO:0000387](https://bioregistry.io/MMO:0000387)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Mohr_pipette`                                         |             1 | [MMO:0000393](https://bioregistry.io/MMO:0000393)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Morris_water_maze`                                    |             1 | [MMO:0000402](https://bioregistry.io/MMO:0000402)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Bicinchoninic_acid_assay`                             |             1 | [MMO:0000424](https://bioregistry.io/MMO:0000424)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Lowry_protein_assay`                                  |             1 | [MMO:0000425](https://bioregistry.io/MMO:0000425)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Bradford_protein_assay`                               |             1 | [MMO:0000426](https://bioregistry.io/MMO:0000426)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Bromocresol_green`                                    |             1 | [MMO:0000436](https://bioregistry.io/MMO:0000436)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Ouchterlony_double_immunodiffusion`                   |             1 | [MMO:0000438](https://bioregistry.io/MMO:0000438)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Transducer`                                           |             1 | [MMO:0000454](https://bioregistry.io/MMO:0000454)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Piezoelectric_accelerometer`                          |             1 | [MMO:0000455](https://bioregistry.io/MMO:0000455)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/ELISPOT`                                              |             1 | [MMO:0000458](https://bioregistry.io/MMO:0000458)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Phytosterol`                                          |             1 | [MMO:0000530](https://bioregistry.io/MMO:0000530)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Histology#Staining`                                   |             1 | [MMO:0000561](https://bioregistry.io/MMO:0000561)                                                                                                                                                                                                                  |
| `Wikipedia:http://en.wikipedia.org/wiki/Growth_medium#Selective_media`                        |             1 | [MMO:0000564](https://bioregistry.io/MMO:0000564)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Rotarod_performance_test`                            |             1 | [MMO:0000567](https://bioregistry.io/MMO:0000567)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Common_carotid_artery`                               |             1 | [MMO:0000582](https://bioregistry.io/MMO:0000582)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Electroretinography`                                 |             1 | [MMO:0000616](https://bioregistry.io/MMO:0000616)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Flow_cytometry`                                      |             1 | [MMO:0000617](https://bioregistry.io/MMO:0000617)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Pressure_measurement#Liquid_column_(manometer)`      |             1 | [MMO:0000622](https://bioregistry.io/MMO:0000622)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Tympanometry`                                        |             1 | [MMO:0000624](https://bioregistry.io/MMO:0000624)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Bronchoalveolar_lavage`                              |             1 | [MMO:0000633](https://bioregistry.io/MMO:0000633)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Primary_transcript`                                  |             1 | [MMO:0000641](https://bioregistry.io/MMO:0000641)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/In_situ#Biology_and_biomedical_engineering`          |             1 | [MMO:0000643](https://bioregistry.io/MMO:0000643)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Tiling_array`                                        |             1 | [MMO:0000650](https://bioregistry.io/MMO:0000650)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Polymerase_chain_reaction`                           |             1 | [MMO:0000655](https://bioregistry.io/MMO:0000655)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Reverse_transcription_polymerase_chain_reaction`     |             1 | [MMO:0000655](https://bioregistry.io/MMO:0000655)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Real-time_polymerase_chain_reaction`                 |             1 | [MMO:0000656](https://bioregistry.io/MMO:0000656)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/In_situ_hybridization`                               |             1 | [MMO:0000658](https://bioregistry.io/MMO:0000658)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Serial_analysis_of_gene_expression`                  |             1 | [MMO:0000660](https://bioregistry.io/MMO:0000660)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Immunofluorescence`                                  |             1 | [MMO:0000662](https://bioregistry.io/MMO:0000662)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Proteomics#High-throughput_proteomic_technologies`   |             1 | [MMO:0000664](https://bioregistry.io/MMO:0000664)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Proteomics`                                          |             1 | [MMO:0000665](https://bioregistry.io/MMO:0000665)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Protein_microarray`                                  |             1 | [MMO:0000666](https://bioregistry.io/MMO:0000666)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Tissue_microarray`                                   |             1 | [MMO:0000667](https://bioregistry.io/MMO:0000667)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Antibody_microarray`                                 |             1 | [MMO:0000668](https://bioregistry.io/MMO:0000668)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Western_blot`                                        |             1 | [MMO:0000669](https://bioregistry.io/MMO:0000669)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Vapor_pressure_osmometry`                            |             1 | [MMO:0000675](https://bioregistry.io/MMO:0000675)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Optical_coherence_tomography`                        |             1 | [MMO:0000696](https://bioregistry.io/MMO:0000696)                                                                                                                                                                                                                  |
| `Wikipedia:https://en.wikipedia.org/wiki/Comprehensive_metabolic_panel`                       |             1 | [MMO:0000698](https://bioregistry.io/MMO:0000698)                                                                                                                                                                                                                  |
