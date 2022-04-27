# enm

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `enm`.


## `AGR`: Agricultural Online Access

Overall, there were 6 invalid
xrefs to external prefixed with `AGR` (standardized to Bioregistry
prefix [`agricola`](https://bioregistry.io/agricola)) that
did not match the standard pattern `^\d+$`.

| external_xref                |   usages_count | usages                                                      |
|------------------------------|----------------|-------------------------------------------------------------|
| `AGR:('AGR', 'IND84086009')` |              1 | [CHEBI:136643](http://purl.obolibrary.org/obo/CHEBI_136643) |
| `AGR:('AGR', 'IND20386178')` |              1 | [CHEBI:136644](http://purl.obolibrary.org/obo/CHEBI_136644) |
| `AGR:('AGR', 'IND84086011')` |              1 | [CHEBI:136644](http://purl.obolibrary.org/obo/CHEBI_136644) |
| `AGR:('AGR', 'IND89021681')` |              1 | [CHEBI:136644](http://purl.obolibrary.org/obo/CHEBI_136644) |
| `AGR:('AGR', 'IND92003154')` |              1 | [CHEBI:136644](http://purl.obolibrary.org/obo/CHEBI_136644) |
| `AGR:('AGR', 'IND43789627')` |              1 | [CHEBI:136646](http://purl.obolibrary.org/obo/CHEBI_136646) |

## `BSPO`: Biological Spatial Ontology

Overall, there were 17 invalid
xrefs to external prefixed with `BSPO` (standardized to Bioregistry
prefix [`bspo`](https://bioregistry.io/bspo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                    |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|----------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BSPO:('BSPO', 'cjm')`           |             11 | [BSPO:0000096](http://purl.obolibrary.org/obo/BSPO_0000096), [BSPO:0000097](http://purl.obolibrary.org/obo/BSPO_0000097), [BSPO:0000098](http://purl.obolibrary.org/obo/BSPO_0000098), [BSPO:0000099](http://purl.obolibrary.org/obo/BSPO_0000099), [BSPO:0000100](http://purl.obolibrary.org/obo/BSPO_0000100), ... |
| `BSPO:('BSPO', 'PATO_mtg_2009')` |              6 | [BSPO:0000120](http://purl.obolibrary.org/obo/BSPO_0000120), [BSPO:0000121](http://purl.obolibrary.org/obo/BSPO_0000121), [BSPO:0000122](http://purl.obolibrary.org/obo/BSPO_0000122), [BSPO:0000123](http://purl.obolibrary.org/obo/BSPO_0000123), [BSPO:0000124](http://purl.obolibrary.org/obo/BSPO_0000124), ... |

## `ENVO`: Environment Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `ENVO` (standardized to Bioregistry
prefix [`envo`](https://bioregistry.io/envo)) that
did not match the standard pattern `^\d{7,8}$`.

| external_xref          |   usages_count | usages                                                        |
|------------------------|----------------|---------------------------------------------------------------|
| `ENVO:('ENVO', 'cjm')` |              1 | [ENVO:00005774](http://purl.obolibrary.org/obo/ENVO_00005774) |

## `FAO`: Fungal gross anatomy

Overall, there were 27 invalid
xrefs to external prefixed with `FAO` (standardized to Bioregistry
prefix [`fao`](https://bioregistry.io/fao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                                                        |   usages_count | usages                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FAO:('FAO', 'http://fao.org/ag/agl/agll/wrb/doc/wrb2006final.pdf')` |             27 | [ENVO:00002229](http://purl.obolibrary.org/obo/ENVO_00002229), [ENVO:00002231](http://purl.obolibrary.org/obo/ENVO_00002231), [ENVO:00002233](http://purl.obolibrary.org/obo/ENVO_00002233), [ENVO:00002234](http://purl.obolibrary.org/obo/ENVO_00002234), [ENVO:00002235](http://purl.obolibrary.org/obo/ENVO_00002235), ... |

## `Gmelin`: Gmelins Handbuch der anorganischen Chemie

Overall, there were 1 invalid
xrefs to external prefixed with `Gmelin` (standardized to Bioregistry
prefix [`gmelin`](https://bioregistry.io/gmelin)) that
did not match the standard pattern `^[1-9][0-9]{3,6}$`.

| external_xref              |   usages_count | usages                                                    |
|----------------------------|----------------|-----------------------------------------------------------|
| `Gmelin:('Gmelin', '485')` |              1 | [CHEBI:15379](http://purl.obolibrary.org/obo/CHEBI_15379) |

## `HPA`: Human Protein Atlas tissue profile information

Overall, there were 1 invalid
xrefs to external prefixed with `HPA` (standardized to Bioregistry
prefix [`hpa`](https://bioregistry.io/hpa)) that
did not match the standard pattern `^ENSG\d{11}$`.

| external_xref        |   usages_count | usages                                                  |
|----------------------|----------------|---------------------------------------------------------|
| `HPA:('HPA', 'HPA')` |              1 | [CL:1001603](http://purl.obolibrary.org/obo/CL_1001603) |

## `HPO`: Human Phenotype Ontology

Overall, there were 5 invalid
xrefs to external prefixed with `HPO` (standardized to Bioregistry
prefix [`hp`](https://bioregistry.io/hp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref              |   usages_count | usages                                                                                                                                                                                                                                                                                      |
|----------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HPO:('HPO', 'probinson')` |              5 | [HP:0001522](http://purl.obolibrary.org/obo/HP_0001522), [HP:0003674](http://purl.obolibrary.org/obo/HP_0003674), [HP:0003811](http://purl.obolibrary.org/obo/HP_0003811), [HP:0003826](http://purl.obolibrary.org/obo/HP_0003826), [HP:0100613](http://purl.obolibrary.org/obo/HP_0100613) |

## `MA`: Mouse adult gross anatomy

Overall, there were 13 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
prefix [`ma`](https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref     |   usages_count | usages                                                                                                                                                                                                                                                                                                                         |
|-------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MA:('MA', 'ma')` |             11 | [ENVO:00000447](http://purl.obolibrary.org/obo/ENVO_00000447), [ENVO:00000873](http://purl.obolibrary.org/obo/ENVO_00000873), [ENVO:00001995](http://purl.obolibrary.org/obo/ENVO_00001995), [ENVO:00002006](http://purl.obolibrary.org/obo/ENVO_00002006), [ENVO:00002047](http://purl.obolibrary.org/obo/ENVO_00002047), ... |
| `MA:('MA', 'th')` |              2 | [BSPO:0001114](http://purl.obolibrary.org/obo/BSPO_0001114), [BSPO:1000000](http://purl.obolibrary.org/obo/BSPO_1000000)                                                                                                                                                                                                       |

## `MGI`: Mouse Genome Informatics

Overall, there were 1 invalid
xrefs to external prefixed with `MGI` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref           |   usages_count | usages                                                          |
|-------------------------|----------------|-----------------------------------------------------------------|
| `MGI:('MGI', 'csmith')` |              1 | [UBERON:0002530](http://purl.obolibrary.org/obo/UBERON_0002530) |

## `MSH`: Medical Subject Headings

Overall, there were 1 invalid
xrefs to external prefixed with `MSH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref            |   usages_count | usages                                              |
|--------------------------|----------------|-----------------------------------------------------|
| `MSH:('MSH', 'Q000401')` |              1 | [EFO:0004352](http://www.ebi.ac.uk/efo/EFO_0004352) |

## `obi`: Ontology for Biomedical Investigations

Overall, there were 1 invalid
xrefs to external prefixed with `obi` (standardized to Bioregistry
prefix [`obi`](https://bioregistry.io/obi)) that
did not match the standard pattern `^\d{7}$`.

| external_xref         |   usages_count | usages                                                    |
|-----------------------|----------------|-----------------------------------------------------------|
| `obi:('obi', 'pppb')` |              1 | [OBI:0000070](http://purl.obolibrary.org/obo/OBI_0000070) |

## `OBO_REL`: Relation Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `OBO_REL` (standardized to Bioregistry
prefix [`ro`](https://bioregistry.io/ro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                     |   usages_count | usages                                                      |
|-----------------------------------|----------------|-------------------------------------------------------------|
| `OBO_REL:('OBO_REL', 'has_part')` |              1 | [PATO:0001555](http://purl.obolibrary.org/obo/PATO_0001555) |

## `PATO`: Phenotype And Trait Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `PATO` (standardized to Bioregistry
prefix [`pato`](https://bioregistry.io/pato)) that
did not match the standard pattern `^\d{7}$`.

| external_xref          |   usages_count | usages                                                                                                                                                                                                                                                                                                          |
|------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PATO:('PATO', 'GVG')` |              5 | [PATO:0000911](http://purl.obolibrary.org/obo/PATO_0000911), [PATO:0000912](http://purl.obolibrary.org/obo/PATO_0000912), [PATO:0001596](http://purl.obolibrary.org/obo/PATO_0001596), [PATO:0001663](http://purl.obolibrary.org/obo/PATO_0001663), [PATO:0001664](http://purl.obolibrary.org/obo/PATO_0001664) |
| `PATO:('PATO', 'DS')`  |              1 | [PATO:0002390](http://purl.obolibrary.org/obo/PATO_0002390)                                                                                                                                                                                                                                                     |
| `PATO:('PATO', 'MAH')` |              1 | [PATO:0002632](http://purl.obolibrary.org/obo/PATO_0002632)                                                                                                                                                                                                                                                     |

## `PMID`: PubMed

Overall, there were 3 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                |   usages_count | usages                                              |
|------------------------------|----------------|-----------------------------------------------------|
| `PMID:('PMID', '27149984 ')` |              1 | [EFO:0007836](http://www.ebi.ac.uk/efo/EFO_0007836) |
| `PMID:('PMID', ' 31636452')` |              1 | [EFO:0010605](http://www.ebi.ac.uk/efo/EFO_0010605) |
| `PMID:('PMID', ' 32355309')` |              1 | [EFO:0010749](http://www.ebi.ac.uk/efo/EFO_0010749) |

## `SO`: Sequence types and features ontology

Overall, there were 2 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref      |   usages_count | usages                                                                                                                                                                           |
|--------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SO:('SO', 'cjm')` |              2 | [envo#disconnected:from](http://purl.obolibrary.org/obo/envo#disconnected_from), [uberon#spatially:disjoint:from](http://purl.obolibrary.org/obo/uberon#spatially_disjoint_from) |

## `UBERON`: Uber Anatomy Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `UBERON` (standardized to Bioregistry
prefix [`uberon`](https://bioregistry.io/uberon)) that
did not match the standard pattern `^\d+$`.

| external_xref              |   usages_count | usages                                                          |
|----------------------------|----------------|-----------------------------------------------------------------|
| `UBERON:('UBERON', 'cjm')` |              1 | [UBERON:0006925](http://purl.obolibrary.org/obo/UBERON_0006925) |

## `Wikipedia`: Wikipedia

Overall, there were 22 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                                                   |   usages_count | usages                                                                                      |
|---------------------------------------------------------------------------------|----------------|---------------------------------------------------------------------------------------------|
| `Wikipedia:('Wikipedia', 'https://en.wikipedia.org/wiki/Gas')`                  |              1 | [CHEBI:138675](http://purl.obolibrary.org/obo/CHEBI_138675)                                 |
| `Wikipedia:('Wikipedia', 'Glycoprotein_IIb/IIIa_inhibitors')`                   |              1 | [CHEBI:50433](http://purl.obolibrary.org/obo/CHEBI_50433)                                   |
| `Wikipedia:('Wikipedia', 'Matrix-assisted_laser_desorption/ionization#Matrix')` |              1 | [CHEBI:64345](http://purl.obolibrary.org/obo/CHEBI_64345)                                   |
| `Wikipedia:('Wikipedia', 'Stabiliser_(food)')`                                  |              1 | [CHEBI:77966](http://purl.obolibrary.org/obo/CHEBI_77966)                                   |
| `Wikipedia:('Wikipedia', 'Insertion_(anatomy)#Muscles')`                        |              1 | [RO:0002372](http://purl.obolibrary.org/obo/RO_0002372)                                     |
| `Wikipedia:('Wikipedia', 'Insertion_(anatomy)')`                                |              1 | [RO:0002373](http://purl.obolibrary.org/obo/RO_0002373)                                     |
| `Wikipedia:('Wikipedia', 'Antagonist_(muscle)')`                                |              1 | [uberon#has:muscle:antagonist](http://purl.obolibrary.org/obo/uberon#has_muscle_antagonist) |
| `Wikipedia:('Wikipedia', 'Dissociation_(psychology)')`                          |              1 | [EFO:0009750](http://www.ebi.ac.uk/efo/EFO_0009750)                                         |
| `Wikipedia:('Wikipedia', '17α-Hydroxyprogesterone')`                            |              1 | [EFO:0010220](http://www.ebi.ac.uk/efo/EFO_0010220)                                         |
| `Wikipedia:('Wikipedia', 'Transduction_(genetics)')`                            |              1 | [GO:0009293](http://purl.obolibrary.org/obo/GO_0009293)                                     |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/concentration')`         |              1 | [PATO:0000033](http://purl.obolibrary.org/obo/PATO_0000033)                                 |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/frequency')`             |              1 | [PATO:0000044](http://purl.obolibrary.org/obo/PATO_0000044)                                 |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Hyperplastic')`          |              1 | [PATO:0000644](http://purl.obolibrary.org/obo/PATO_0000644)                                 |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Area')`                  |              1 | [PATO:0001323](http://purl.obolibrary.org/obo/PATO_0001323)                                 |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Diameter')`              |              1 | [PATO:0001334](http://purl.obolibrary.org/obo/PATO_0001334)                                 |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Area_density')`          |              1 | [PATO:0001351](http://purl.obolibrary.org/obo/PATO_0001351)                                 |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Linear_density')`        |              1 | [PATO:0001352](http://purl.obolibrary.org/obo/PATO_0001352)                                 |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Mass_density')`          |              1 | [PATO:0001353](http://purl.obolibrary.org/obo/PATO_0001353)                                 |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Electric_potential')`    |              1 | [PATO:0001464](http://purl.obolibrary.org/obo/PATO_0001464)                                 |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Specific_volume')`       |              1 | [PATO:0001679](http://purl.obolibrary.org/obo/PATO_0001679)                                 |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Molar_volume')`          |              1 | [PATO:0001680](http://purl.obolibrary.org/obo/PATO_0001680)                                 |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Perimeter')`             |              1 | [PATO:0001711](http://purl.obolibrary.org/obo/PATO_0001711)                                 |

## `WWF`: World Wildlife Fund Ecoregion

Overall, there were 13 invalid
xrefs to external prefixed with `WWF` (standardized to Bioregistry
prefix [`wwf.ecoregion`](https://bioregistry.io/wwf.ecoregion)) that
did not match the standard pattern `^AT\d+$`.

| external_xref           |   usages_count | usages                                                        |
|-------------------------|----------------|---------------------------------------------------------------|
| `WWF:('WWF', 'Biome')`  |              1 | [ENVO:00000428](http://purl.obolibrary.org/obo/ENVO_00000428) |
| `WWF:('WWF', 'AA1310')` |              1 | [ENVO:01001569](http://purl.obolibrary.org/obo/ENVO_01001569) |
| `WWF:('WWF', 'AA1309')` |              1 | [ENVO:01001572](http://purl.obolibrary.org/obo/ENVO_01001572) |
| `WWF:('WWF', 'AA1308')` |              1 | [ENVO:01001573](http://purl.obolibrary.org/obo/ENVO_01001573) |
| `WWF:('WWF', 'AA1307')` |              1 | [ENVO:01001574](http://purl.obolibrary.org/obo/ENVO_01001574) |
| `WWF:('WWF', 'AA1301')` |              1 | [ENVO:01001575](http://purl.obolibrary.org/obo/ENVO_01001575) |
| `WWF:('WWF', 'AA1302')` |              1 | [ENVO:01001576](http://purl.obolibrary.org/obo/ENVO_01001576) |
| `WWF:('WWF', 'AA1303')` |              1 | [ENVO:01001577](http://purl.obolibrary.org/obo/ENVO_01001577) |
| `WWF:('WWF', 'AA1304')` |              1 | [ENVO:01001578](http://purl.obolibrary.org/obo/ENVO_01001578) |
| `WWF:('WWF', 'AA1305')` |              1 | [ENVO:01001579](http://purl.obolibrary.org/obo/ENVO_01001579) |
| `WWF:('WWF', 'AA1306')` |              1 | [ENVO:01001580](http://purl.obolibrary.org/obo/ENVO_01001580) |
| `WWF:('WWF', 'IM1304')` |              1 | [ENVO:01001627](http://purl.obolibrary.org/obo/ENVO_01001627) |
| `WWF:('WWF', 'IM1303')` |              1 | [ENVO:01001628](http://purl.obolibrary.org/obo/ENVO_01001628) |

## `ZFS`: Zebrafish developmental stages ontology

Overall, there were 1 invalid
xrefs to external prefixed with `ZFS` (standardized to Bioregistry
prefix [`zfs`](https://bioregistry.io/zfs)) that
did not match the standard pattern `^\d{7}$`.

| external_xref             |   usages_count | usages                                                  |
|---------------------------|----------------|---------------------------------------------------------|
| `ZFS:('ZFS', 'finishes')` |              1 | [RO:0002229](http://purl.obolibrary.org/obo/RO_0002229) |

