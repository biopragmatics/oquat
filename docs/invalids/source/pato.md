# pato

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `pato`. See the [GitHub repository](https://github.com/pato-ontology/pato)


## `ENVO`: Environment Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `ENVO` (standardized to Bioregistry
entry [`envo`]((https://bioregistry.io/envo)) that
did not match the standard pattern `^\d{7,8}$`.

| external_xref   |   usages_count | usages                                                                                                                                                        |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ENVO:pb`       |              3 | [PATO:0015017](https://bioregistry.io/PATO:0015017), [PATO:0015018](https://bioregistry.io/PATO:0015018), [PATO:0015029](https://bioregistry.io/PATO:0015029) |

## `GO`: Gene Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
entry [`go`]((https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                        |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:GO`         |              3 | [PATO:0001440](https://bioregistry.io/PATO:0001440), [PATO:0001441](https://bioregistry.io/PATO:0001441), [PATO:0001720](https://bioregistry.io/PATO:0001720) |

## `Medline`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `Medline` (standardized to Bioregistry
entry [`pubmed`]((https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                                |   usages_count | usages                                              |
|----------------------------------------------|----------------|-----------------------------------------------------|
| `Medline:http://www.nlm.nih.gov/medlineplus` |              1 | [PATO:0002048](https://bioregistry.io/PATO:0002048) |

## `neurolex`: NeuroLex

Overall, there were 2 invalid
xrefs to external prefixed with `neurolex` (standardized to Bioregistry
entry [`neurolex`]((https://bioregistry.io/neurolex)) that
did not match the standard pattern `^([Bb]irnlex_|Sao|nlx_|GO_|CogPO|HDO|nifext_)\d+$`.

| external_xref                                                           |   usages_count | usages                                              |
|-------------------------------------------------------------------------|----------------|-----------------------------------------------------|
| `neurolex:http://neurolex.org/`                                         |              1 | [PATO:0002216](https://bioregistry.io/PATO:0002216) |
| `neurolex:http://neurolex.org/wiki/Category:Nitrated_Molecular_Quality` |              1 | [PATO:0002217](https://bioregistry.io/PATO:0002217) |

## `OBI`: Ontology for Biomedical Investigations

Overall, there were 1 invalid
xrefs to external prefixed with `OBI` (standardized to Bioregistry
entry [`obi`]((https://bioregistry.io/obi)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `OBI:OBI`       |              1 | [PATO:0001985](https://bioregistry.io/PATO:0001985) |

## `OBO_REL`: Relation Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `OBO_REL` (standardized to Bioregistry
entry [`ro`]((https://bioregistry.io/ro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                              |
|----------------------|----------------|-----------------------------------------------------|
| `OBO_REL:has_part`   |              1 | [PATO:0001555](https://bioregistry.io/PATO:0001555) |
| `OBO_REL:lacks_part` |              1 | [PATO:0002000](https://bioregistry.io/PATO:0002000) |

## `PATO`: Phenotype And Trait Ontology

Overall, there were 69 invalid
xrefs to external prefixed with `PATO` (standardized to Bioregistry
entry [`pato`]((https://bioregistry.io/pato)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                       |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PATO:GVG`      |             54 | [PATO:0001553](https://bioregistry.io/PATO:0001553), [PATO:0001613](https://bioregistry.io/PATO:0001613), [PATO:0001615](https://bioregistry.io/PATO:0001615), [PATO:0001637](https://bioregistry.io/PATO:0001637), [PATO:0002175](https://bioregistry.io/PATO:0002175), ... |
| `PATO:MAH`      |              8 | [PATO:0000428](https://bioregistry.io/PATO:0000428), [PATO:0000428](https://bioregistry.io/PATO:0000428), [PATO:0001624](https://bioregistry.io/PATO:0001624), [PATO:0002629](https://bioregistry.io/PATO:0002629), [PATO:0002631](https://bioregistry.io/PATO:0002631), ... |
| `PATO:LC`       |              2 | [PATO:0000694](https://bioregistry.io/PATO:0000694), [PATO:0002363](https://bioregistry.io/PATO:0002363)                                                                                                                                                                     |
| `PATO:WS`       |              1 | [PATO:0002311](https://bioregistry.io/PATO:0002311)                                                                                                                                                                                                                          |
| `PATO:WC`       |              1 | [PATO:0002320](https://bioregistry.io/PATO:0002320)                                                                                                                                                                                                                          |
| `PATO:PG`       |              1 | [PATO:0002389](https://bioregistry.io/PATO:0002389)                                                                                                                                                                                                                          |
| `PATO:DS`       |              1 | [PATO:0002390](https://bioregistry.io/PATO:0002390)                                                                                                                                                                                                                          |
| `PATO:JL`       |              1 | [PATO:0002454](https://bioregistry.io/PATO:0002454)                                                                                                                                                                                                                          |

## `TO`: Plant Trait Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `TO` (standardized to Bioregistry
entry [`to`]((https://bioregistry.io/to)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                   |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------|
| `TO:TO`         |              2 | [PATO:0001540](https://bioregistry.io/PATO:0001540), [PATO:0001541](https://bioregistry.io/PATO:0001541) |

## `Wikipedia`: Wikipedia

Overall, there were 96 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
entry [`wikipedia.en`]((https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                                      |   usages_count | usages                                                                                                                                                        |
|--------------------------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Wikipedia:https://en.wikipedia.org/wiki/Drinking_water`           |              3 | [PATO:0025000](https://bioregistry.io/PATO:0025000), [PATO:0025001](https://bioregistry.io/PATO:0025001), [PATO:0025002](https://bioregistry.io/PATO:0025002) |
| `Wikipedia:http://en.wikipedia.org/wiki/Osmolarity`                |              2 | [PATO:0001655](https://bioregistry.io/PATO:0001655), [PATO:0002027](https://bioregistry.io/PATO:0002027)                                                      |
| `Wikipedia:http://en.wikipedia.org/wiki/Velocity`                  |              1 | [PATO:0000008](https://bioregistry.io/PATO:0000008)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/concentration`             |              1 | [PATO:0000033](https://bioregistry.io/PATO:0000033)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/frequency`                 |              1 | [PATO:0000044](https://bioregistry.io/PATO:0000044)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Trophic_level`             |              1 | [PATO:0000056](https://bioregistry.io/PATO:0000056)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Weight`                    |              1 | [PATO:0000128](https://bioregistry.io/PATO:0000128)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Fecundity`                 |              1 | [PATO:0000273](https://bioregistry.io/PATO:0000273)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Magenta`                   |              1 | [PATO:0000321](https://bioregistry.io/PATO:0000321)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Auxotrophic`               |              1 | [PATO:0000422](https://bioregistry.io/PATO:0000422)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Prototrophic`              |              1 | [PATO:0000423](https://bioregistry.io/PATO:0000423)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Hyperplastic`              |              1 | [PATO:0000644](https://bioregistry.io/PATO:0000644)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Necrotic`                  |              1 | [PATO:0000647](https://bioregistry.io/PATO:0000647)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Brown`                     |              1 | [PATO:0000952](https://bioregistry.io/PATO:0000952)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Orange`                    |              1 | [PATO:0000953](https://bioregistry.io/PATO:0000953)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Energy`                    |              1 | [PATO:0001021](https://bioregistry.io/PATO:0001021)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Power`                     |              1 | [PATO:0001024](https://bioregistry.io/PATO:0001024)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Work`                      |              1 | [PATO:0001026](https://bioregistry.io/PATO:0001026)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Acceleration`              |              1 | [PATO:0001028](https://bioregistry.io/PATO:0001028)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Larval`                    |              1 | [PATO:0001185](https://bioregistry.io/PATO:0001185)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Electromagnetic_radiation` |              1 | [PATO:0001291](https://bioregistry.io/PATO:0001291)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Area`                      |              1 | [PATO:0001323](https://bioregistry.io/PATO:0001323)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Bilateral_symmetry`        |              1 | [PATO:0001324](https://bioregistry.io/PATO:0001324)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Diameter`                  |              1 | [PATO:0001334](https://bioregistry.io/PATO:0001334)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Angular_acceleration`      |              1 | [PATO:0001350](https://bioregistry.io/PATO:0001350)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Area_density`              |              1 | [PATO:0001351](https://bioregistry.io/PATO:0001351)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Linear_density`            |              1 | [PATO:0001352](https://bioregistry.io/PATO:0001352)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Mass_density`              |              1 | [PATO:0001353](https://bioregistry.io/PATO:0001353)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Ploidy`                    |              1 | [PATO:0001374](https://bioregistry.io/PATO:0001374)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Haploid`                   |              1 | [PATO:0001375](https://bioregistry.io/PATO:0001375)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Monoploid`                 |              1 | [PATO:0001376](https://bioregistry.io/PATO:0001376)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Polyploid`                 |              1 | [PATO:0001377](https://bioregistry.io/PATO:0001377)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Autopolyploid`             |              1 | [PATO:0001378](https://bioregistry.io/PATO:0001378)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Allopolyploidy`            |              1 | [PATO:0001379](https://bioregistry.io/PATO:0001379)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Paleopolyploid`            |              1 | [PATO:0001380](https://bioregistry.io/PATO:0001380)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Triploid`                  |              1 | [PATO:0001381](https://bioregistry.io/PATO:0001381)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Tetraploid`                |              1 | [PATO:0001382](https://bioregistry.io/PATO:0001382)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Pentaploid`                |              1 | [PATO:0001383](https://bioregistry.io/PATO:0001383)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Hexaploid`                 |              1 | [PATO:0001384](https://bioregistry.io/PATO:0001384)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Aneuploid`                 |              1 | [PATO:0001385](https://bioregistry.io/PATO:0001385)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Monosomy`                  |              1 | [PATO:0001386](https://bioregistry.io/PATO:0001386)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Disomy`                    |              1 | [PATO:0001387](https://bioregistry.io/PATO:0001387)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Uniparental_disomy`        |              1 | [PATO:0001388](https://bioregistry.io/PATO:0001388)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Trisomy`                   |              1 | [PATO:0001389](https://bioregistry.io/PATO:0001389)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Partial_trisomy`           |              1 | [PATO:0001390](https://bioregistry.io/PATO:0001390)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Endopolyploid`             |              1 | [PATO:0001392](https://bioregistry.io/PATO:0001392)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Euploid`                   |              1 | [PATO:0001393](https://bioregistry.io/PATO:0001393)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Diploid`                   |              1 | [PATO:0001394](https://bioregistry.io/PATO:0001394)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Haplodiploid`              |              1 | [PATO:0001395](https://bioregistry.io/PATO:0001395)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Totipotent`                |              1 | [PATO:0001399](https://bioregistry.io/PATO:0001399)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Unipotent`                 |              1 | [PATO:0001400](https://bioregistry.io/PATO:0001400)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Multipotent`               |              1 | [PATO:0001402](https://bioregistry.io/PATO:0001402)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Pluripotent`               |              1 | [PATO:0001403](https://bioregistry.io/PATO:0001403)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Ciliated`                  |              1 | [PATO:0001408](https://bioregistry.io/PATO:0001408)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Angular_velocity`          |              1 | [PATO:0001413](https://bioregistry.io/PATO:0001413)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Violet`                    |              1 | [PATO:0001424](https://bioregistry.io/PATO:0001424)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Maroon`                    |              1 | [PATO:0001426](https://bioregistry.io/PATO:0001426)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Sessility_(botany)`        |              1 | [PATO:0001436](https://bioregistry.io/PATO:0001436)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Sessile_(zoology)`         |              1 | [PATO:0001437](https://bioregistry.io/PATO:0001437)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Cartilaginous`             |              1 | [PATO:0001449](https://bioregistry.io/PATO:0001449)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Surface_tension`           |              1 | [PATO:0001461](https://bioregistry.io/PATO:0001461)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Membrane_potential`        |              1 | [PATO:0001462](https://bioregistry.io/PATO:0001462)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Action_potential`          |              1 | [PATO:0001463](https://bioregistry.io/PATO:0001463)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Electric_potential`        |              1 | [PATO:0001464](https://bioregistry.io/PATO:0001464)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Focus_(optics)`            |              1 | [PATO:0001516](https://bioregistry.io/PATO:0001516)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Sound_quality`             |              1 | [PATO:0001519](https://bioregistry.io/PATO:0001519)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Sound_speed`               |              1 | [PATO:0001522](https://bioregistry.io/PATO:0001522)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Sound_wavelength`          |              1 | [PATO:0001523](https://bioregistry.io/PATO:0001523)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Specific_volume`           |              1 | [PATO:0001679](https://bioregistry.io/PATO:0001679)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Molar_volume`              |              1 | [PATO:0001680](https://bioregistry.io/PATO:0001680)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Molar_mass`                |              1 | [PATO:0001681](https://bioregistry.io/PATO:0001681)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Magnetism`                 |              1 | [PATO:0001682](https://bioregistry.io/PATO:0001682)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Perimeter`                 |              1 | [PATO:0001711](https://bioregistry.io/PATO:0001711)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Luminance`                 |              1 | [PATO:0001718](https://bioregistry.io/PATO:0001718)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Heat_conduction`           |              1 | [PATO:0001756](https://bioregistry.io/PATO:0001756)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Electrical_conduction`     |              1 | [PATO:0001757](https://bioregistry.io/PATO:0001757)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Dehydrated`                |              1 | [PATO:0001801](https://bioregistry.io/PATO:0001801)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Spheroid`                  |              1 | [PATO:0001865](https://bioregistry.io/PATO:0001865)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Prolate`                   |              1 | [PATO:0001866](https://bioregistry.io/PATO:0001866)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Rectangular`               |              1 | [PATO:0001867](https://bioregistry.io/PATO:0001867)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Crescent`                  |              1 | [PATO:0001870](https://bioregistry.io/PATO:0001870)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Cone_(geometry)`           |              1 | [PATO:0002021](https://bioregistry.io/PATO:0002021)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Crystal`                   |              1 | [PATO:0002066](https://bioregistry.io/PATO:0002066)                                                                                                           |
| `Wikipedia:http://en.wiktionary.org/wiki/hyperphosphorylated`      |              1 | [PATO:0002221](https://bioregistry.io/PATO:0002221)                                                                                                           |
| `Wikipedia:http://en.wiktionary.org/wiki/hypophosphorylated`       |              1 | [PATO:0002222](https://bioregistry.io/PATO:0002222)                                                                                                           |
| `Wikipedia:http://en.wiktionary.org/wiki/oxidized`                 |              1 | [PATO:0002223](https://bioregistry.io/PATO:0002223)                                                                                                           |
| `Wikipedia:https://en.wikipedia.org/wiki/Friability`               |              1 | [PATO:0002405](https://bioregistry.io/PATO:0002405)                                                                                                           |
| `Wikipedia:https://en.wikipedia.org/wiki/Doubled_haploidy`         |              1 | [PATO:0040027](https://bioregistry.io/PATO:0040027)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/Cardinal_direction`        |              1 | [PATO:0045090](https://bioregistry.io/PATO:0045090)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/North`                     |              1 | [PATO:0045091](https://bioregistry.io/PATO:0045091)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/East`                      |              1 | [PATO:0045092](https://bioregistry.io/PATO:0045092)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/South`                     |              1 | [PATO:0045093](https://bioregistry.io/PATO:0045093)                                                                                                           |
| `Wikipedia:http://en.wikipedia.org/wiki/West`                      |              1 | [PATO:0045094](https://bioregistry.io/PATO:0045094)                                                                                                           |

## `wikipedia`: Wikipedia

Overall, there were 5 invalid
xrefs to external prefixed with `wikipedia` (standardized to Bioregistry
entry [`wikipedia.en`]((https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                         |   usages_count | usages                                                                                                   |
|-------------------------------------------------------|----------------|----------------------------------------------------------------------------------------------------------|
| `wikipedia:https://en.wikipedia.org/wiki/Acinus`      |              2 | [PATO:0002378](https://bioregistry.io/PATO:0002378), [PATO:0002422](https://bioregistry.io/PATO:0002422) |
| `wikipedia:en.wikipedia.org/wiki/Phosphorylated`      |              1 | [PATO:0002220](https://bioregistry.io/PATO:0002220)                                                      |
| `wikipedia:http://en.wiktionary.org/wiki/amphiphilic` |              1 | [PATO:0002420](https://bioregistry.io/PATO:0002420)                                                      |
| `wikipedia:http://en.wikipedia.org/wiki/Brittleness`  |              1 | [PATO:0002477](https://bioregistry.io/PATO:0002477)                                                      |

