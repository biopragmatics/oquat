# fypo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `fypo`. See the [GitHub repository](https://github.com/pombase/fypo).


## `GO`: Gene Ontology

Overall, there were 8 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
entry [`go`]((https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref            |   usages_count | usages                                                                                                                                                        |
|--------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:0036124,PomBase:mah` |              3 | [FYPO:0007507](https://bioregistry.io/FYPO:0007507), [FYPO:0007508](https://bioregistry.io/FYPO:0007508), [FYPO:0007509](https://bioregistry.io/FYPO:0007509) |
| `GO:006355`              |              2 | [FYPO:0004526](https://bioregistry.io/FYPO:0004526), [FYPO:0004527](https://bioregistry.io/FYPO:0004527)                                                      |
| `GO:001322`              |              1 | [FYPO:0003561](https://bioregistry.io/FYPO:0003561)                                                                                                           |
| `GO:030995`              |              1 | [FYPO:0004270](https://bioregistry.io/FYPO:0004270)                                                                                                           |
| `GO:003118`              |              1 | [FYPO:0007501](https://bioregistry.io/FYPO:0007501)                                                                                                           |

## `PMID`: PubMed

Overall, there were 2 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
entry [`pubmed`]((https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `PMID:34805795
PomBase:val`                 |              1 | [FYPO:0007907](https://bioregistry.io/FYPO:0007907) |
| `PMID::8247131` |              1 | [FYPO:0001686](https://bioregistry.io/FYPO:0001686) |

## `PomBase`: PomBase

Overall, there were 18,014 invalid
xrefs to external prefixed with `PomBase` (standardized to Bioregistry
entry [`pombase`]((https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                       |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PomBase:mah`   |          14849 | [FYPO:0000001](https://bioregistry.io/FYPO:0000001), [FYPO:0000001](https://bioregistry.io/FYPO:0000001), [FYPO:0000002](https://bioregistry.io/FYPO:0000002), [FYPO:0000002](https://bioregistry.io/FYPO:0000002), [FYPO:0000003](https://bioregistry.io/FYPO:0000003), ... |
| `PomBase:vw`    |           1969 | [FYPO:0000012](https://bioregistry.io/FYPO:0000012), [FYPO:0000013](https://bioregistry.io/FYPO:0000013), [FYPO:0000014](https://bioregistry.io/FYPO:0000014), [FYPO:0000016](https://bioregistry.io/FYPO:0000016), [FYPO:0000017](https://bioregistry.io/FYPO:0000017), ... |
| `PomBase:al`    |           1076 | [FYPO:0000006](https://bioregistry.io/FYPO:0000006), [FYPO:0000061](https://bioregistry.io/FYPO:0000061), [FYPO:0000090](https://bioregistry.io/FYPO:0000090), [FYPO:0000102](https://bioregistry.io/FYPO:0000102), [FYPO:0000108](https://bioregistry.io/FYPO:0000108), ... |
| `PomBase:jh`    |             93 | [FYPO:0000129](https://bioregistry.io/FYPO:0000129), [FYPO:0000229](https://bioregistry.io/FYPO:0000229), [FYPO:0000241](https://bioregistry.io/FYPO:0000241), [FYPO:0000284](https://bioregistry.io/FYPO:0000284), [FYPO:0000316](https://bioregistry.io/FYPO:0000316), ... |
| `PomBase:val`   |             16 | [FYPO:0007902](https://bioregistry.io/FYPO:0007902), [FYPO:0007903](https://bioregistry.io/FYPO:0007903), [FYPO:0007906](https://bioregistry.io/FYPO:0007906), [FYPO:0007908](https://bioregistry.io/FYPO:0007908), [FYPO:0007909](https://bioregistry.io/FYPO:0007909), ... |
| `PomBase:amc`   |              3 | [FYPO:0004251](https://bioregistry.io/FYPO:0004251), [FYPO:0006087](https://bioregistry.io/FYPO:0006087), [FYPO:0006318](https://bioregistry.io/FYPO:0006318)                                                                                                                |
| `PomBase:mp`    |              2 | [FYPO:0001404](https://bioregistry.io/FYPO:0001404), [FYPO:0001405](https://bioregistry.io/FYPO:0001405)                                                                                                                                                                     |
| `PomBase:gs`    |              2 | [FYPO:0002484](https://bioregistry.io/FYPO:0002484), [FYPO:0002485](https://bioregistry.io/FYPO:0002485)                                                                                                                                                                     |
| `PomBase:ch`    |              1 | [FYPO:0000153](https://bioregistry.io/FYPO:0000153)                                                                                                                                                                                                                          |
| `PomBase:pr`    |              1 | [FYPO:0005334](https://bioregistry.io/FYPO:0005334)                                                                                                                                                                                                                          |
| `PomBase:mahle` |              1 | [FYPO:0007633](https://bioregistry.io/FYPO:0007633)                                                                                                                                                                                                                          |
| `PomBase:sm`    |              1 | [FYPO:0007683](https://bioregistry.io/FYPO:0007683)                                                                                                                                                                                                                          |

## `Pombase`: PomBase

Overall, there were 39 invalid
xrefs to external prefixed with `Pombase` (standardized to Bioregistry
entry [`pombase`]((https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                       |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Pombase:vw`    |             29 | [FYPO:0002440](https://bioregistry.io/FYPO:0002440), [FYPO:0003290](https://bioregistry.io/FYPO:0003290), [FYPO:0004022](https://bioregistry.io/FYPO:0004022), [FYPO:0004086](https://bioregistry.io/FYPO:0004086), [FYPO:0004159](https://bioregistry.io/FYPO:0004159), ... |
| `Pombase:al`    |              6 | [FYPO:0004989](https://bioregistry.io/FYPO:0004989), [FYPO:0005527](https://bioregistry.io/FYPO:0005527), [FYPO:0005528](https://bioregistry.io/FYPO:0005528), [FYPO:0006260](https://bioregistry.io/FYPO:0006260), [FYPO:0007084](https://bioregistry.io/FYPO:0007084), ... |
| `Pombase:mah`   |              4 | [FYPO:0005385](https://bioregistry.io/FYPO:0005385), [FYPO:0005396](https://bioregistry.io/FYPO:0005396), [FYPO:0006770](https://bioregistry.io/FYPO:0006770), [FYPO:0007288](https://bioregistry.io/FYPO:0007288)                                                           |

## `SGD`: Saccharomyces Genome Database

Overall, there were 293 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
entry [`sgd`]((https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref              |   usages_count | usages                                                                                                                                                                                                                                                                       |
|----------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:phenotype_annotation` |            293 | [FYPO:0000005](https://bioregistry.io/FYPO:0000005), [FYPO:0000008](https://bioregistry.io/FYPO:0000008), [FYPO:0000011](https://bioregistry.io/FYPO:0000011), [FYPO:0000012](https://bioregistry.io/FYPO:0000012), [FYPO:0000023](https://bioregistry.io/FYPO:0000023), ... |

## `SO`: Sequence types and features ontology

Overall, there were 1 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
entry [`so`]((https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `SO:1861`       |              1 | [FYPO:0003251](https://bioregistry.io/FYPO:0003251) |

