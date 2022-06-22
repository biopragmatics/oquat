# pato

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `pato`. See the [GitHub repository](https://github.com/pato-ontology/pato).


## `ENVO`: Environment Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `ENVO` (standardized to Bioregistry
prefix [`envo`](https://bioregistry.io/envo)) that
did not match the standard pattern `^\d{7,8}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ENVO:pb`       |              3 | [PATO:0015017](http://purl.obolibrary.org/obo/PATO_0015017), [PATO:0015018](http://purl.obolibrary.org/obo/PATO_0015018), [PATO:0015029](http://purl.obolibrary.org/obo/PATO_0015029) |

## `GO`: Gene Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:GO`         |              3 | [PATO:0001440](http://purl.obolibrary.org/obo/PATO_0001440), [PATO:0001441](http://purl.obolibrary.org/obo/PATO_0001441), [PATO:0001720](http://purl.obolibrary.org/obo/PATO_0001720) |

## `ISSN`: International Standard Serial Number

Overall, there were 1 invalid
xrefs to external prefixed with `ISSN` (standardized to Bioregistry
prefix [`issn`](https://bioregistry.io/issn)) that
did not match the standard pattern `^\d{4}-\d{3}[\dX]$`.

| external_xref        |   usages_count | usages                                                      |
|----------------------|----------------|-------------------------------------------------------------|
| `ISSN:9781496335418` |              1 | [PATO:0001744](http://purl.obolibrary.org/obo/PATO_0001744) |

## `Medline`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `Medline` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                                |   usages_count | usages                                                      |
|----------------------------------------------|----------------|-------------------------------------------------------------|
| `Medline:http://www.nlm.nih.gov/medlineplus` |              1 | [PATO:0002048](http://purl.obolibrary.org/obo/PATO_0002048) |

## `neurolex`: NIF Standard Ontology: Neurolex

Overall, there were 2 invalid
xrefs to external prefixed with `neurolex` (standardized to Bioregistry
prefix [`neurolex`](https://bioregistry.io/neurolex)) that
did not match the standard pattern `^\d+$`.

| external_xref                                                           |   usages_count | usages                                                      |
|-------------------------------------------------------------------------|----------------|-------------------------------------------------------------|
| `neurolex:http://neurolex.org/`                                         |              1 | [PATO:0002216](http://purl.obolibrary.org/obo/PATO_0002216) |
| `neurolex:http://neurolex.org/wiki/Category:Nitrated_Molecular_Quality` |              1 | [PATO:0002217](http://purl.obolibrary.org/obo/PATO_0002217) |

## `OBI`: Ontology for Biomedical Investigations

Overall, there were 1 invalid
xrefs to external prefixed with `OBI` (standardized to Bioregistry
prefix [`obi`](https://bioregistry.io/obi)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `OBI:OBI`       |              1 | [PATO:0001985](http://purl.obolibrary.org/obo/PATO_0001985) |

## `OBO_REL`: Relation Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `OBO_REL` (standardized to Bioregistry
prefix [`ro`](https://bioregistry.io/ro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                                      |
|----------------------|----------------|-------------------------------------------------------------|
| `OBO_REL:has_part`   |              1 | [PATO:0001555](http://purl.obolibrary.org/obo/PATO_0001555) |
| `OBO_REL:lacks_part` |              1 | [PATO:0002000](http://purl.obolibrary.org/obo/PATO_0002000) |

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

## `TO`: Plant Trait Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `TO` (standardized to Bioregistry
prefix [`to`](https://bioregistry.io/to)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                   |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------|
| `TO:TO`         |              2 | [PATO:0001540](http://purl.obolibrary.org/obo/PATO_0001540), [PATO:0001541](http://purl.obolibrary.org/obo/PATO_0001541) |

## `Wikipedia`: Wikipedia

Overall, there were 96 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                                      |   usages_count | usages                                                                                                                                                                                |
|--------------------------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Wikipedia:https://en.wikipedia.org/wiki/Drinking_water`           |              3 | [PATO:0025000](http://purl.obolibrary.org/obo/PATO_0025000), [PATO:0025001](http://purl.obolibrary.org/obo/PATO_0025001), [PATO:0025002](http://purl.obolibrary.org/obo/PATO_0025002) |
| `Wikipedia:http://en.wikipedia.org/wiki/Osmolarity`                |              2 | [PATO:0001655](http://purl.obolibrary.org/obo/PATO_0001655), [PATO:0002027](http://purl.obolibrary.org/obo/PATO_0002027)                                                              |
| `Wikipedia:http://en.wikipedia.org/wiki/Velocity`                  |              1 | [PATO:0000008](http://purl.obolibrary.org/obo/PATO_0000008)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/concentration`             |              1 | [PATO:0000033](http://purl.obolibrary.org/obo/PATO_0000033)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/frequency`                 |              1 | [PATO:0000044](http://purl.obolibrary.org/obo/PATO_0000044)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Trophic_level`             |              1 | [PATO:0000056](http://purl.obolibrary.org/obo/PATO_0000056)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Weight`                    |              1 | [PATO:0000128](http://purl.obolibrary.org/obo/PATO_0000128)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Fecundity`                 |              1 | [PATO:0000273](http://purl.obolibrary.org/obo/PATO_0000273)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Magenta`                   |              1 | [PATO:0000321](http://purl.obolibrary.org/obo/PATO_0000321)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Auxotrophic`               |              1 | [PATO:0000422](http://purl.obolibrary.org/obo/PATO_0000422)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Prototrophic`              |              1 | [PATO:0000423](http://purl.obolibrary.org/obo/PATO_0000423)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Hyperplastic`              |              1 | [PATO:0000644](http://purl.obolibrary.org/obo/PATO_0000644)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Necrotic`                  |              1 | [PATO:0000647](http://purl.obolibrary.org/obo/PATO_0000647)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Brown`                     |              1 | [PATO:0000952](http://purl.obolibrary.org/obo/PATO_0000952)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Orange`                    |              1 | [PATO:0000953](http://purl.obolibrary.org/obo/PATO_0000953)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Energy`                    |              1 | [PATO:0001021](http://purl.obolibrary.org/obo/PATO_0001021)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Power`                     |              1 | [PATO:0001024](http://purl.obolibrary.org/obo/PATO_0001024)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Work`                      |              1 | [PATO:0001026](http://purl.obolibrary.org/obo/PATO_0001026)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Acceleration`              |              1 | [PATO:0001028](http://purl.obolibrary.org/obo/PATO_0001028)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Larval`                    |              1 | [PATO:0001185](http://purl.obolibrary.org/obo/PATO_0001185)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Electromagnetic_radiation` |              1 | [PATO:0001291](http://purl.obolibrary.org/obo/PATO_0001291)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Area`                      |              1 | [PATO:0001323](http://purl.obolibrary.org/obo/PATO_0001323)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Bilateral_symmetry`        |              1 | [PATO:0001324](http://purl.obolibrary.org/obo/PATO_0001324)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Diameter`                  |              1 | [PATO:0001334](http://purl.obolibrary.org/obo/PATO_0001334)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Angular_acceleration`      |              1 | [PATO:0001350](http://purl.obolibrary.org/obo/PATO_0001350)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Area_density`              |              1 | [PATO:0001351](http://purl.obolibrary.org/obo/PATO_0001351)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Linear_density`            |              1 | [PATO:0001352](http://purl.obolibrary.org/obo/PATO_0001352)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Mass_density`              |              1 | [PATO:0001353](http://purl.obolibrary.org/obo/PATO_0001353)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Ploidy`                    |              1 | [PATO:0001374](http://purl.obolibrary.org/obo/PATO_0001374)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Haploid`                   |              1 | [PATO:0001375](http://purl.obolibrary.org/obo/PATO_0001375)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Monoploid`                 |              1 | [PATO:0001376](http://purl.obolibrary.org/obo/PATO_0001376)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Polyploid`                 |              1 | [PATO:0001377](http://purl.obolibrary.org/obo/PATO_0001377)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Autopolyploid`             |              1 | [PATO:0001378](http://purl.obolibrary.org/obo/PATO_0001378)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Allopolyploidy`            |              1 | [PATO:0001379](http://purl.obolibrary.org/obo/PATO_0001379)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Paleopolyploid`            |              1 | [PATO:0001380](http://purl.obolibrary.org/obo/PATO_0001380)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Triploid`                  |              1 | [PATO:0001381](http://purl.obolibrary.org/obo/PATO_0001381)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Tetraploid`                |              1 | [PATO:0001382](http://purl.obolibrary.org/obo/PATO_0001382)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Pentaploid`                |              1 | [PATO:0001383](http://purl.obolibrary.org/obo/PATO_0001383)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Hexaploid`                 |              1 | [PATO:0001384](http://purl.obolibrary.org/obo/PATO_0001384)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Aneuploid`                 |              1 | [PATO:0001385](http://purl.obolibrary.org/obo/PATO_0001385)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Monosomy`                  |              1 | [PATO:0001386](http://purl.obolibrary.org/obo/PATO_0001386)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Disomy`                    |              1 | [PATO:0001387](http://purl.obolibrary.org/obo/PATO_0001387)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Uniparental_disomy`        |              1 | [PATO:0001388](http://purl.obolibrary.org/obo/PATO_0001388)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Trisomy`                   |              1 | [PATO:0001389](http://purl.obolibrary.org/obo/PATO_0001389)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Partial_trisomy`           |              1 | [PATO:0001390](http://purl.obolibrary.org/obo/PATO_0001390)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Endopolyploid`             |              1 | [PATO:0001392](http://purl.obolibrary.org/obo/PATO_0001392)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Euploid`                   |              1 | [PATO:0001393](http://purl.obolibrary.org/obo/PATO_0001393)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Diploid`                   |              1 | [PATO:0001394](http://purl.obolibrary.org/obo/PATO_0001394)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Haplodiploid`              |              1 | [PATO:0001395](http://purl.obolibrary.org/obo/PATO_0001395)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Totipotent`                |              1 | [PATO:0001399](http://purl.obolibrary.org/obo/PATO_0001399)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Unipotent`                 |              1 | [PATO:0001400](http://purl.obolibrary.org/obo/PATO_0001400)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Multipotent`               |              1 | [PATO:0001402](http://purl.obolibrary.org/obo/PATO_0001402)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Pluripotent`               |              1 | [PATO:0001403](http://purl.obolibrary.org/obo/PATO_0001403)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Ciliated`                  |              1 | [PATO:0001408](http://purl.obolibrary.org/obo/PATO_0001408)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Angular_velocity`          |              1 | [PATO:0001413](http://purl.obolibrary.org/obo/PATO_0001413)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Violet`                    |              1 | [PATO:0001424](http://purl.obolibrary.org/obo/PATO_0001424)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Maroon`                    |              1 | [PATO:0001426](http://purl.obolibrary.org/obo/PATO_0001426)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Sessility_(botany)`        |              1 | [PATO:0001436](http://purl.obolibrary.org/obo/PATO_0001436)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Sessile_(zoology)`         |              1 | [PATO:0001437](http://purl.obolibrary.org/obo/PATO_0001437)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Cartilaginous`             |              1 | [PATO:0001449](http://purl.obolibrary.org/obo/PATO_0001449)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Surface_tension`           |              1 | [PATO:0001461](http://purl.obolibrary.org/obo/PATO_0001461)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Membrane_potential`        |              1 | [PATO:0001462](http://purl.obolibrary.org/obo/PATO_0001462)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Action_potential`          |              1 | [PATO:0001463](http://purl.obolibrary.org/obo/PATO_0001463)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Electric_potential`        |              1 | [PATO:0001464](http://purl.obolibrary.org/obo/PATO_0001464)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Focus_(optics)`            |              1 | [PATO:0001516](http://purl.obolibrary.org/obo/PATO_0001516)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Sound_quality`             |              1 | [PATO:0001519](http://purl.obolibrary.org/obo/PATO_0001519)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Sound_speed`               |              1 | [PATO:0001522](http://purl.obolibrary.org/obo/PATO_0001522)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Sound_wavelength`          |              1 | [PATO:0001523](http://purl.obolibrary.org/obo/PATO_0001523)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Specific_volume`           |              1 | [PATO:0001679](http://purl.obolibrary.org/obo/PATO_0001679)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Molar_volume`              |              1 | [PATO:0001680](http://purl.obolibrary.org/obo/PATO_0001680)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Molar_mass`                |              1 | [PATO:0001681](http://purl.obolibrary.org/obo/PATO_0001681)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Magnetism`                 |              1 | [PATO:0001682](http://purl.obolibrary.org/obo/PATO_0001682)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Perimeter`                 |              1 | [PATO:0001711](http://purl.obolibrary.org/obo/PATO_0001711)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Luminance`                 |              1 | [PATO:0001718](http://purl.obolibrary.org/obo/PATO_0001718)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Heat_conduction`           |              1 | [PATO:0001756](http://purl.obolibrary.org/obo/PATO_0001756)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Electrical_conduction`     |              1 | [PATO:0001757](http://purl.obolibrary.org/obo/PATO_0001757)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Dehydrated`                |              1 | [PATO:0001801](http://purl.obolibrary.org/obo/PATO_0001801)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Spheroid`                  |              1 | [PATO:0001865](http://purl.obolibrary.org/obo/PATO_0001865)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Prolate`                   |              1 | [PATO:0001866](http://purl.obolibrary.org/obo/PATO_0001866)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Rectangular`               |              1 | [PATO:0001867](http://purl.obolibrary.org/obo/PATO_0001867)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Crescent`                  |              1 | [PATO:0001870](http://purl.obolibrary.org/obo/PATO_0001870)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Cone_(geometry)`           |              1 | [PATO:0002021](http://purl.obolibrary.org/obo/PATO_0002021)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Crystal`                   |              1 | [PATO:0002066](http://purl.obolibrary.org/obo/PATO_0002066)                                                                                                                           |
| `Wikipedia:http://en.wiktionary.org/wiki/hyperphosphorylated`      |              1 | [PATO:0002221](http://purl.obolibrary.org/obo/PATO_0002221)                                                                                                                           |
| `Wikipedia:http://en.wiktionary.org/wiki/hypophosphorylated`       |              1 | [PATO:0002222](http://purl.obolibrary.org/obo/PATO_0002222)                                                                                                                           |
| `Wikipedia:http://en.wiktionary.org/wiki/oxidized`                 |              1 | [PATO:0002223](http://purl.obolibrary.org/obo/PATO_0002223)                                                                                                                           |
| `Wikipedia:https://en.wikipedia.org/wiki/Friability`               |              1 | [PATO:0002405](http://purl.obolibrary.org/obo/PATO_0002405)                                                                                                                           |
| `Wikipedia:https://en.wikipedia.org/wiki/Doubled_haploidy`         |              1 | [PATO:0040027](http://purl.obolibrary.org/obo/PATO_0040027)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Cardinal_direction`        |              1 | [PATO:0045090](http://purl.obolibrary.org/obo/PATO_0045090)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/North`                     |              1 | [PATO:0045091](http://purl.obolibrary.org/obo/PATO_0045091)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/East`                      |              1 | [PATO:0045092](http://purl.obolibrary.org/obo/PATO_0045092)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/South`                     |              1 | [PATO:0045093](http://purl.obolibrary.org/obo/PATO_0045093)                                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/West`                      |              1 | [PATO:0045094](http://purl.obolibrary.org/obo/PATO_0045094)                                                                                                                           |

## `wikipedia`: Wikipedia

Overall, there were 5 invalid
xrefs to external prefixed with `wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                         |   usages_count | usages                                                                                                                   |
|-------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------|
| `wikipedia:https://en.wikipedia.org/wiki/Acinus`      |              2 | [PATO:0002378](http://purl.obolibrary.org/obo/PATO_0002378), [PATO:0002422](http://purl.obolibrary.org/obo/PATO_0002422) |
| `wikipedia:en.wikipedia.org/wiki/Phosphorylated`      |              1 | [PATO:0002220](http://purl.obolibrary.org/obo/PATO_0002220)                                                              |
| `wikipedia:http://en.wiktionary.org/wiki/amphiphilic` |              1 | [PATO:0002420](http://purl.obolibrary.org/obo/PATO_0002420)                                                              |
| `wikipedia:http://en.wikipedia.org/wiki/Brittleness`  |              1 | [PATO:0002477](http://purl.obolibrary.org/obo/PATO_0002477)                                                              |

