# fypo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `fypo`. See the [GitHub repository](https://github.com/pombase/fypo).


## `GO`: Gene Ontology

Overall, there were 8 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref            |   usages_count | usages                                                                                                                                                                                |
|--------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:0036124,PomBase:mah` |              3 | [FYPO:0007507](http://purl.obolibrary.org/obo/FYPO_0007507), [FYPO:0007508](http://purl.obolibrary.org/obo/FYPO_0007508), [FYPO:0007509](http://purl.obolibrary.org/obo/FYPO_0007509) |
| `GO:006355`              |              2 | [FYPO:0004526](http://purl.obolibrary.org/obo/FYPO_0004526), [FYPO:0004527](http://purl.obolibrary.org/obo/FYPO_0004527)                                                              |
| `GO:001322`              |              1 | [FYPO:0003561](http://purl.obolibrary.org/obo/FYPO_0003561)                                                                                                                           |
| `GO:030995`              |              1 | [FYPO:0004270](http://purl.obolibrary.org/obo/FYPO_0004270)                                                                                                                           |
| `GO:003118`              |              1 | [FYPO:0007501](http://purl.obolibrary.org/obo/FYPO_0007501)                                                                                                                           |

## `PMID`: PubMed

Overall, there were 2 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `PMID:34805795
PomBase:val`                 |              1 | [FYPO:0007907](http://purl.obolibrary.org/obo/FYPO_0007907) |
| `PMID::8247131` |              1 | [FYPO:0001686](http://purl.obolibrary.org/obo/FYPO_0001686) |

## `PomBase`: PomBase

Overall, there were 18,025 invalid
xrefs to external prefixed with `PomBase` (standardized to Bioregistry
prefix [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PomBase:mah`   |          14845 | [FYPO:0000001](http://purl.obolibrary.org/obo/FYPO_0000001), [FYPO:0000001](http://purl.obolibrary.org/obo/FYPO_0000001), [FYPO:0000002](http://purl.obolibrary.org/obo/FYPO_0000002), [FYPO:0000002](http://purl.obolibrary.org/obo/FYPO_0000002), [FYPO:0000003](http://purl.obolibrary.org/obo/FYPO_0000003), ... |
| `PomBase:vw`    |           1969 | [FYPO:0000012](http://purl.obolibrary.org/obo/FYPO_0000012), [FYPO:0000013](http://purl.obolibrary.org/obo/FYPO_0000013), [FYPO:0000014](http://purl.obolibrary.org/obo/FYPO_0000014), [FYPO:0000016](http://purl.obolibrary.org/obo/FYPO_0000016), [FYPO:0000017](http://purl.obolibrary.org/obo/FYPO_0000017), ... |
| `PomBase:al`    |           1076 | [FYPO:0000006](http://purl.obolibrary.org/obo/FYPO_0000006), [FYPO:0000061](http://purl.obolibrary.org/obo/FYPO_0000061), [FYPO:0000090](http://purl.obolibrary.org/obo/FYPO_0000090), [FYPO:0000102](http://purl.obolibrary.org/obo/FYPO_0000102), [FYPO:0000108](http://purl.obolibrary.org/obo/FYPO_0000108), ... |
| `PomBase:jh`    |             93 | [FYPO:0000129](http://purl.obolibrary.org/obo/FYPO_0000129), [FYPO:0000229](http://purl.obolibrary.org/obo/FYPO_0000229), [FYPO:0000241](http://purl.obolibrary.org/obo/FYPO_0000241), [FYPO:0000284](http://purl.obolibrary.org/obo/FYPO_0000284), [FYPO:0000316](http://purl.obolibrary.org/obo/FYPO_0000316), ... |
| `PomBase:val`   |             22 | [FYPO:0000901](http://purl.obolibrary.org/obo/FYPO_0000901), [FYPO:0000901](http://purl.obolibrary.org/obo/FYPO_0000901), [FYPO:0007902](http://purl.obolibrary.org/obo/FYPO_0007902), [FYPO:0007903](http://purl.obolibrary.org/obo/FYPO_0007903), [FYPO:0007906](http://purl.obolibrary.org/obo/FYPO_0007906), ... |
| `PomBase:mlr`   |              9 | [FYPO:0007955](http://purl.obolibrary.org/obo/FYPO_0007955), [FYPO:0007957](http://purl.obolibrary.org/obo/FYPO_0007957), [FYPO:0007957](http://purl.obolibrary.org/obo/FYPO_0007957), [FYPO:0007959](http://purl.obolibrary.org/obo/FYPO_0007959), [FYPO:0007960](http://purl.obolibrary.org/obo/FYPO_0007960), ... |
| `PomBase:amc`   |              3 | [FYPO:0004251](http://purl.obolibrary.org/obo/FYPO_0004251), [FYPO:0006087](http://purl.obolibrary.org/obo/FYPO_0006087), [FYPO:0006318](http://purl.obolibrary.org/obo/FYPO_0006318)                                                                                                                                |
| `PomBase:mp`    |              2 | [FYPO:0001404](http://purl.obolibrary.org/obo/FYPO_0001404), [FYPO:0001405](http://purl.obolibrary.org/obo/FYPO_0001405)                                                                                                                                                                                             |
| `PomBase:gs`    |              2 | [FYPO:0002484](http://purl.obolibrary.org/obo/FYPO_0002484), [FYPO:0002485](http://purl.obolibrary.org/obo/FYPO_0002485)                                                                                                                                                                                             |
| `PomBase:ch`    |              1 | [FYPO:0000153](http://purl.obolibrary.org/obo/FYPO_0000153)                                                                                                                                                                                                                                                          |
| `PomBase:pr`    |              1 | [FYPO:0005334](http://purl.obolibrary.org/obo/FYPO_0005334)                                                                                                                                                                                                                                                          |
| `PomBase:mahle` |              1 | [FYPO:0007633](http://purl.obolibrary.org/obo/FYPO_0007633)                                                                                                                                                                                                                                                          |
| `PomBase:sm`    |              1 | [FYPO:0007683](http://purl.obolibrary.org/obo/FYPO_0007683)                                                                                                                                                                                                                                                          |

## `Pombase`: PomBase

Overall, there were 39 invalid
xrefs to external prefixed with `Pombase` (standardized to Bioregistry
prefix [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Pombase:vw`    |             29 | [FYPO:0002440](http://purl.obolibrary.org/obo/FYPO_0002440), [FYPO:0003290](http://purl.obolibrary.org/obo/FYPO_0003290), [FYPO:0004022](http://purl.obolibrary.org/obo/FYPO_0004022), [FYPO:0004086](http://purl.obolibrary.org/obo/FYPO_0004086), [FYPO:0004159](http://purl.obolibrary.org/obo/FYPO_0004159), ... |
| `Pombase:al`    |              6 | [FYPO:0004989](http://purl.obolibrary.org/obo/FYPO_0004989), [FYPO:0005527](http://purl.obolibrary.org/obo/FYPO_0005527), [FYPO:0005528](http://purl.obolibrary.org/obo/FYPO_0005528), [FYPO:0006260](http://purl.obolibrary.org/obo/FYPO_0006260), [FYPO:0007084](http://purl.obolibrary.org/obo/FYPO_0007084), ... |
| `Pombase:mah`   |              4 | [FYPO:0005385](http://purl.obolibrary.org/obo/FYPO_0005385), [FYPO:0005396](http://purl.obolibrary.org/obo/FYPO_0005396), [FYPO:0006770](http://purl.obolibrary.org/obo/FYPO_0006770), [FYPO:0007288](http://purl.obolibrary.org/obo/FYPO_0007288)                                                                   |

## `SGD`: Saccharomyces Genome Database

Overall, there were 292 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
prefix [`sgd`](https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref              |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|----------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:phenotype_annotation` |            292 | [FYPO:0000005](http://purl.obolibrary.org/obo/FYPO_0000005), [FYPO:0000008](http://purl.obolibrary.org/obo/FYPO_0000008), [FYPO:0000011](http://purl.obolibrary.org/obo/FYPO_0000011), [FYPO:0000012](http://purl.obolibrary.org/obo/FYPO_0000012), [FYPO:0000023](http://purl.obolibrary.org/obo/FYPO_0000023), ... |

## `SO`: Sequence types and features ontology

Overall, there were 1 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `SO:1861`       |              1 | [FYPO:0003251](http://purl.obolibrary.org/obo/FYPO_0003251) |

