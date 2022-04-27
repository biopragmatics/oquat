# fypo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `fypo`. See the [GitHub repository](https://github.com/pombase/fypo)


## `GO`: Gene Ontology

- Normalized prefix: `go`
- [https://bioregistry.io/go](https://bioregistry.io/go)
- Pattern:`^\d{7}$`

| identifier               |   appearances | examples                                                                                                                                                      |
|--------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:0036124,PomBase:mah` |             3 | [FYPO:0007507](https://bioregistry.io/FYPO:0007507), [FYPO:0007508](https://bioregistry.io/FYPO:0007508), [FYPO:0007509](https://bioregistry.io/FYPO:0007509) |
| `GO:006355`              |             2 | [FYPO:0004526](https://bioregistry.io/FYPO:0004526), [FYPO:0004527](https://bioregistry.io/FYPO:0004527)                                                      |
| `GO:001322`              |             1 | [FYPO:0003561](https://bioregistry.io/FYPO:0003561)                                                                                                           |
| `GO:030995`              |             1 | [FYPO:0004270](https://bioregistry.io/FYPO:0004270)                                                                                                           |
| `GO:003118`              |             1 | [FYPO:0007501](https://bioregistry.io/FYPO:0007501)                                                                                                           |

## `PMID`: PubMed

- Normalized prefix: `pubmed`
- [https://bioregistry.io/pubmed](https://bioregistry.io/pubmed)
- Pattern:`^\d+$`

| identifier      |   appearances | examples                                            |
|-----------------|---------------|-----------------------------------------------------|
| `PMID:34805795
PomBase:val`                 |             1 | [FYPO:0007907](https://bioregistry.io/FYPO:0007907) |
| `PMID::8247131` |             1 | [FYPO:0001686](https://bioregistry.io/FYPO:0001686) |

## `PomBase`: PomBase

- Normalized prefix: `pombase`
- [https://bioregistry.io/pombase](https://bioregistry.io/pombase)
- Pattern:`^S\w+(\.)?\w+(\.)?$`

| identifier      |   appearances | examples                                                                                                                                                                                                                                                                     |
|-----------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PomBase:mah`   |         14849 | [FYPO:0002528](https://bioregistry.io/FYPO:0002528), [FYPO:0003615](https://bioregistry.io/FYPO:0003615), [FYPO:0005973](https://bioregistry.io/FYPO:0005973), [FYPO:0006165](https://bioregistry.io/FYPO:0006165), [FYPO:0006884](https://bioregistry.io/FYPO:0006884), ... |
| `PomBase:vw`    |          1969 | [FYPO:0000365](https://bioregistry.io/FYPO:0000365), [FYPO:0000877](https://bioregistry.io/FYPO:0000877), [FYPO:0006912](https://bioregistry.io/FYPO:0006912), [FYPO:0006988](https://bioregistry.io/FYPO:0006988), [FYPO:0007310](https://bioregistry.io/FYPO:0007310), ... |
| `PomBase:al`    |          1076 | [FYPO:0001306](https://bioregistry.io/FYPO:0001306), [FYPO:0001795](https://bioregistry.io/FYPO:0001795), [FYPO:0001901](https://bioregistry.io/FYPO:0001901), [FYPO:0002829](https://bioregistry.io/FYPO:0002829), [FYPO:0003545](https://bioregistry.io/FYPO:0003545), ... |
| `PomBase:jh`    |            93 | [FYPO:0002179](https://bioregistry.io/FYPO:0002179), [FYPO:0005855](https://bioregistry.io/FYPO:0005855), [FYPO:0006768](https://bioregistry.io/FYPO:0006768), [FYPO:0006848](https://bioregistry.io/FYPO:0006848), [FYPO:0007659](https://bioregistry.io/FYPO:0007659), ... |
| `PomBase:val`   |            16 | [FYPO:0007908](https://bioregistry.io/FYPO:0007908), [FYPO:0007909](https://bioregistry.io/FYPO:0007909), [FYPO:0007944](https://bioregistry.io/FYPO:0007944), [FYPO:0007945](https://bioregistry.io/FYPO:0007945), [FYPO:0007947](https://bioregistry.io/FYPO:0007947), ... |
| `PomBase:amc`   |             3 | [FYPO:0004251](https://bioregistry.io/FYPO:0004251), [FYPO:0006087](https://bioregistry.io/FYPO:0006087), [FYPO:0006318](https://bioregistry.io/FYPO:0006318)                                                                                                                |
| `PomBase:mp`    |             2 | [FYPO:0001404](https://bioregistry.io/FYPO:0001404), [FYPO:0001405](https://bioregistry.io/FYPO:0001405)                                                                                                                                                                     |
| `PomBase:gs`    |             2 | [FYPO:0002484](https://bioregistry.io/FYPO:0002484), [FYPO:0002485](https://bioregistry.io/FYPO:0002485)                                                                                                                                                                     |
| `PomBase:ch`    |             1 | [FYPO:0000153](https://bioregistry.io/FYPO:0000153)                                                                                                                                                                                                                          |
| `PomBase:pr`    |             1 | [FYPO:0005334](https://bioregistry.io/FYPO:0005334)                                                                                                                                                                                                                          |
| `PomBase:mahle` |             1 | [FYPO:0007633](https://bioregistry.io/FYPO:0007633)                                                                                                                                                                                                                          |
| `PomBase:sm`    |             1 | [FYPO:0007683](https://bioregistry.io/FYPO:0007683)                                                                                                                                                                                                                          |

## `Pombase`: PomBase

- Normalized prefix: `pombase`
- [https://bioregistry.io/pombase](https://bioregistry.io/pombase)
- Pattern:`^S\w+(\.)?\w+(\.)?$`

| identifier    |   appearances | examples                                                                                                                                                                                                                                                                     |
|---------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Pombase:vw`  |            29 | [FYPO:0002440](https://bioregistry.io/FYPO:0002440), [FYPO:0006277](https://bioregistry.io/FYPO:0006277), [FYPO:0007044](https://bioregistry.io/FYPO:0007044), [FYPO:0007048](https://bioregistry.io/FYPO:0007048), [FYPO:0007109](https://bioregistry.io/FYPO:0007109), ... |
| `Pombase:al`  |             6 | [FYPO:0004989](https://bioregistry.io/FYPO:0004989), [FYPO:0004989](https://bioregistry.io/FYPO:0004989), [FYPO:0004989](https://bioregistry.io/FYPO:0004989), [FYPO:0006260](https://bioregistry.io/FYPO:0006260), [FYPO:0007084](https://bioregistry.io/FYPO:0007084), ... |
| `Pombase:mah` |             4 | [FYPO:0005385](https://bioregistry.io/FYPO:0005385), [FYPO:0005396](https://bioregistry.io/FYPO:0005396), [FYPO:0006770](https://bioregistry.io/FYPO:0006770), [FYPO:0007288](https://bioregistry.io/FYPO:0007288)                                                           |

## `SGD`: Saccharomyces Genome Database

- Normalized prefix: `sgd`
- [https://bioregistry.io/sgd](https://bioregistry.io/sgd)
- Pattern:`^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`

| identifier                 |   appearances | examples                                                                                                                                                                                                                                                                     |
|----------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:phenotype_annotation` |           293 | [FYPO:0000397](https://bioregistry.io/FYPO:0000397), [FYPO:0000619](https://bioregistry.io/FYPO:0000619), [FYPO:0000726](https://bioregistry.io/FYPO:0000726), [FYPO:0001043](https://bioregistry.io/FYPO:0001043), [FYPO:0002498](https://bioregistry.io/FYPO:0002498), ... |

## `SO`: Sequence types and features ontology

- Normalized prefix: `so`
- [https://bioregistry.io/so](https://bioregistry.io/so)
- Pattern:`^\d{7}$`

| identifier   |   appearances | examples                                            |
|--------------|---------------|-----------------------------------------------------|
| `SO:1861`    |             1 | [FYPO:0003251](https://bioregistry.io/FYPO:0003251) |

