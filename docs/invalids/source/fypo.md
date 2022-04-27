# fypo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `fypo`. See the [GitHub repository](https://github.com/pombase/fypo)


## `GO`: Gene Ontology

Overall, there were 8 invalid
xrefs to external terms in `go` that did not match the standard
pattern `^\d{7}$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/go).

| external_xref            |   usages_count | usages                                                                                                                                                        |
|--------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:0036124,PomBase:mah` |              3 | [FYPO:0007507](https://bioregistry.io/FYPO:0007507), [FYPO:0007508](https://bioregistry.io/FYPO:0007508), [FYPO:0007509](https://bioregistry.io/FYPO:0007509) |
| `GO:006355`              |              2 | [FYPO:0004526](https://bioregistry.io/FYPO:0004526), [FYPO:0004527](https://bioregistry.io/FYPO:0004527)                                                      |
| `GO:001322`              |              1 | [FYPO:0003561](https://bioregistry.io/FYPO:0003561)                                                                                                           |
| `GO:030995`              |              1 | [FYPO:0004270](https://bioregistry.io/FYPO:0004270)                                                                                                           |
| `GO:003118`              |              1 | [FYPO:0007501](https://bioregistry.io/FYPO:0007501)                                                                                                           |

## `PMID`: PubMed

Overall, there were 2 invalid
xrefs to external terms in `pubmed` that did not match the standard
pattern `^\d+$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/pubmed).

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `PMID:34805795
PomBase:val`                 |              1 | [FYPO:0007907](https://bioregistry.io/FYPO:0007907) |
| `PMID::8247131` |              1 | [FYPO:0001686](https://bioregistry.io/FYPO:0001686) |

## `PomBase`: PomBase

Overall, there were 18,014 invalid
xrefs to external terms in `pombase` that did not match the standard
pattern `^S\w+(\.)?\w+(\.)?$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/pombase).

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                       |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PomBase:mah`   |          14849 | [FYPO:0000522](https://bioregistry.io/FYPO:0000522), [FYPO:0001624](https://bioregistry.io/FYPO:0001624), [FYPO:0002425](https://bioregistry.io/FYPO:0002425), [FYPO:0004100](https://bioregistry.io/FYPO:0004100), [FYPO:0006941](https://bioregistry.io/FYPO:0006941), ... |
| `PomBase:vw`    |           1969 | [FYPO:0001391](https://bioregistry.io/FYPO:0001391), [FYPO:0001511](https://bioregistry.io/FYPO:0001511), [FYPO:0001891](https://bioregistry.io/FYPO:0001891), [FYPO:0005655](https://bioregistry.io/FYPO:0005655), [FYPO:0007403](https://bioregistry.io/FYPO:0007403), ... |
| `PomBase:al`    |           1076 | [FYPO:0001072](https://bioregistry.io/FYPO:0001072), [FYPO:0002238](https://bioregistry.io/FYPO:0002238), [FYPO:0005317](https://bioregistry.io/FYPO:0005317), [FYPO:0005917](https://bioregistry.io/FYPO:0005917), [FYPO:0006830](https://bioregistry.io/FYPO:0006830), ... |
| `PomBase:jh`    |             93 | [FYPO:0000229](https://bioregistry.io/FYPO:0000229), [FYPO:0002178](https://bioregistry.io/FYPO:0002178), [FYPO:0006167](https://bioregistry.io/FYPO:0006167), [FYPO:0007785](https://bioregistry.io/FYPO:0007785), [FYPO:0007862](https://bioregistry.io/FYPO:0007862), ... |
| `PomBase:val`   |             16 | [FYPO:0007902](https://bioregistry.io/FYPO:0007902), [FYPO:0007909](https://bioregistry.io/FYPO:0007909), [FYPO:0007943](https://bioregistry.io/FYPO:0007943), [FYPO:0007949](https://bioregistry.io/FYPO:0007949), [FYPO:0007951](https://bioregistry.io/FYPO:0007951), ... |
| `PomBase:amc`   |              3 | [FYPO:0004251](https://bioregistry.io/FYPO:0004251), [FYPO:0006087](https://bioregistry.io/FYPO:0006087), [FYPO:0006318](https://bioregistry.io/FYPO:0006318)                                                                                                                |
| `PomBase:mp`    |              2 | [FYPO:0001404](https://bioregistry.io/FYPO:0001404), [FYPO:0001405](https://bioregistry.io/FYPO:0001405)                                                                                                                                                                     |
| `PomBase:gs`    |              2 | [FYPO:0002484](https://bioregistry.io/FYPO:0002484), [FYPO:0002485](https://bioregistry.io/FYPO:0002485)                                                                                                                                                                     |
| `PomBase:ch`    |              1 | [FYPO:0000153](https://bioregistry.io/FYPO:0000153)                                                                                                                                                                                                                          |
| `PomBase:pr`    |              1 | [FYPO:0005334](https://bioregistry.io/FYPO:0005334)                                                                                                                                                                                                                          |
| `PomBase:mahle` |              1 | [FYPO:0007633](https://bioregistry.io/FYPO:0007633)                                                                                                                                                                                                                          |
| `PomBase:sm`    |              1 | [FYPO:0007683](https://bioregistry.io/FYPO:0007683)                                                                                                                                                                                                                          |

## `Pombase`: PomBase

Overall, there were 39 invalid
xrefs to external terms in `pombase` that did not match the standard
pattern `^S\w+(\.)?\w+(\.)?$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/pombase).

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                       |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Pombase:vw`    |             29 | [FYPO:0004159](https://bioregistry.io/FYPO:0004159), [FYPO:0004532](https://bioregistry.io/FYPO:0004532), [FYPO:0006273](https://bioregistry.io/FYPO:0006273), [FYPO:0007051](https://bioregistry.io/FYPO:0007051), [FYPO:0007067](https://bioregistry.io/FYPO:0007067), ... |
| `Pombase:al`    |              6 | [FYPO:0004989](https://bioregistry.io/FYPO:0004989), [FYPO:0006260](https://bioregistry.io/FYPO:0006260), [FYPO:0006260](https://bioregistry.io/FYPO:0006260), [FYPO:0007084](https://bioregistry.io/FYPO:0007084), [FYPO:0007144](https://bioregistry.io/FYPO:0007144), ... |
| `Pombase:mah`   |              4 | [FYPO:0005385](https://bioregistry.io/FYPO:0005385), [FYPO:0005396](https://bioregistry.io/FYPO:0005396), [FYPO:0006770](https://bioregistry.io/FYPO:0006770), [FYPO:0007288](https://bioregistry.io/FYPO:0007288)                                                           |

## `SGD`: Saccharomyces Genome Database

Overall, there were 293 invalid
xrefs to external terms in `sgd` that did not match the standard
pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/sgd).

| external_xref              |   usages_count | usages                                                                                                                                                                                                                                                                       |
|----------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:phenotype_annotation` |            293 | [FYPO:0000422](https://bioregistry.io/FYPO:0000422), [FYPO:0000478](https://bioregistry.io/FYPO:0000478), [FYPO:0000528](https://bioregistry.io/FYPO:0000528), [FYPO:0000620](https://bioregistry.io/FYPO:0000620), [FYPO:0003449](https://bioregistry.io/FYPO:0003449), ... |

## `SO`: Sequence types and features ontology

Overall, there were 1 invalid
xrefs to external terms in `so` that did not match the standard
pattern `^\d{7}$`. More information on this
external resource can be found on the
[Bioregistry](https://bioregistry.io/so).

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `SO:1861`       |              1 | [FYPO:0003251](https://bioregistry.io/FYPO:0003251) |

