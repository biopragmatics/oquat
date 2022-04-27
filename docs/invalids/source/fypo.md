# fypo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `fypo`. See the [GitHub repository](https://github.com/pombase/fypo).


## `GO`: Gene Ontology

Overall, there were 8 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                      |   usages_count | usages                                                                                                                                                                                                                                                                             |
|------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:('GO', '0036124,PomBase:mah')` |              3 | [http://purl.obolibrary.org/obo/FYPO_0007507](http://purl.obolibrary.org/obo/FYPO_0007507), [http://purl.obolibrary.org/obo/FYPO_0007508](http://purl.obolibrary.org/obo/FYPO_0007508), [http://purl.obolibrary.org/obo/FYPO_0007509](http://purl.obolibrary.org/obo/FYPO_0007509) |
| `GO:('GO', '006355')`              |              2 | [http://purl.obolibrary.org/obo/FYPO_0004526](http://purl.obolibrary.org/obo/FYPO_0004526), [http://purl.obolibrary.org/obo/FYPO_0004527](http://purl.obolibrary.org/obo/FYPO_0004527)                                                                                             |
| `GO:('GO', '001322')`              |              1 | [http://purl.obolibrary.org/obo/FYPO_0003561](http://purl.obolibrary.org/obo/FYPO_0003561)                                                                                                                                                                                         |
| `GO:('GO', '030995')`              |              1 | [http://purl.obolibrary.org/obo/FYPO_0004270](http://purl.obolibrary.org/obo/FYPO_0004270)                                                                                                                                                                                         |
| `GO:('GO', '003118')`              |              1 | [http://purl.obolibrary.org/obo/FYPO_0007501](http://purl.obolibrary.org/obo/FYPO_0007501)                                                                                                                                                                                         |

## `PMID`: PubMed

Overall, there were 2 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                            |   usages_count | usages                                                                                     |
|------------------------------------------|----------------|--------------------------------------------------------------------------------------------|
| `PMID:('PMID', '34805795\nPomBase:val')` |              1 | [http://purl.obolibrary.org/obo/FYPO_0007907](http://purl.obolibrary.org/obo/FYPO_0007907) |
| `PMID:('PMID', ':8247131')`              |              1 | [http://purl.obolibrary.org/obo/FYPO_0001686](http://purl.obolibrary.org/obo/FYPO_0001686) |

## `PomBase`: PomBase

Overall, there were 18,014 invalid
xrefs to external prefixed with `PomBase` (standardized to Bioregistry
prefix [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref                  |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PomBase:('PomBase', 'mah')`   |          14849 | [http://purl.obolibrary.org/obo/FYPO_0000001](http://purl.obolibrary.org/obo/FYPO_0000001), [http://purl.obolibrary.org/obo/FYPO_0000001](http://purl.obolibrary.org/obo/FYPO_0000001), [http://purl.obolibrary.org/obo/FYPO_0000002](http://purl.obolibrary.org/obo/FYPO_0000002), [http://purl.obolibrary.org/obo/FYPO_0000002](http://purl.obolibrary.org/obo/FYPO_0000002), [http://purl.obolibrary.org/obo/FYPO_0000003](http://purl.obolibrary.org/obo/FYPO_0000003), ... |
| `PomBase:('PomBase', 'vw')`    |           1969 | [http://purl.obolibrary.org/obo/FYPO_0000012](http://purl.obolibrary.org/obo/FYPO_0000012), [http://purl.obolibrary.org/obo/FYPO_0000013](http://purl.obolibrary.org/obo/FYPO_0000013), [http://purl.obolibrary.org/obo/FYPO_0000014](http://purl.obolibrary.org/obo/FYPO_0000014), [http://purl.obolibrary.org/obo/FYPO_0000016](http://purl.obolibrary.org/obo/FYPO_0000016), [http://purl.obolibrary.org/obo/FYPO_0000017](http://purl.obolibrary.org/obo/FYPO_0000017), ... |
| `PomBase:('PomBase', 'al')`    |           1076 | [http://purl.obolibrary.org/obo/FYPO_0000006](http://purl.obolibrary.org/obo/FYPO_0000006), [http://purl.obolibrary.org/obo/FYPO_0000061](http://purl.obolibrary.org/obo/FYPO_0000061), [http://purl.obolibrary.org/obo/FYPO_0000090](http://purl.obolibrary.org/obo/FYPO_0000090), [http://purl.obolibrary.org/obo/FYPO_0000102](http://purl.obolibrary.org/obo/FYPO_0000102), [http://purl.obolibrary.org/obo/FYPO_0000108](http://purl.obolibrary.org/obo/FYPO_0000108), ... |
| `PomBase:('PomBase', 'jh')`    |             93 | [http://purl.obolibrary.org/obo/FYPO_0000129](http://purl.obolibrary.org/obo/FYPO_0000129), [http://purl.obolibrary.org/obo/FYPO_0000229](http://purl.obolibrary.org/obo/FYPO_0000229), [http://purl.obolibrary.org/obo/FYPO_0000241](http://purl.obolibrary.org/obo/FYPO_0000241), [http://purl.obolibrary.org/obo/FYPO_0000284](http://purl.obolibrary.org/obo/FYPO_0000284), [http://purl.obolibrary.org/obo/FYPO_0000316](http://purl.obolibrary.org/obo/FYPO_0000316), ... |
| `PomBase:('PomBase', 'val')`   |             16 | [http://purl.obolibrary.org/obo/FYPO_0007902](http://purl.obolibrary.org/obo/FYPO_0007902), [http://purl.obolibrary.org/obo/FYPO_0007903](http://purl.obolibrary.org/obo/FYPO_0007903), [http://purl.obolibrary.org/obo/FYPO_0007906](http://purl.obolibrary.org/obo/FYPO_0007906), [http://purl.obolibrary.org/obo/FYPO_0007908](http://purl.obolibrary.org/obo/FYPO_0007908), [http://purl.obolibrary.org/obo/FYPO_0007909](http://purl.obolibrary.org/obo/FYPO_0007909), ... |
| `PomBase:('PomBase', 'amc')`   |              3 | [http://purl.obolibrary.org/obo/FYPO_0004251](http://purl.obolibrary.org/obo/FYPO_0004251), [http://purl.obolibrary.org/obo/FYPO_0006087](http://purl.obolibrary.org/obo/FYPO_0006087), [http://purl.obolibrary.org/obo/FYPO_0006318](http://purl.obolibrary.org/obo/FYPO_0006318)                                                                                                                                                                                              |
| `PomBase:('PomBase', 'mp')`    |              2 | [http://purl.obolibrary.org/obo/FYPO_0001404](http://purl.obolibrary.org/obo/FYPO_0001404), [http://purl.obolibrary.org/obo/FYPO_0001405](http://purl.obolibrary.org/obo/FYPO_0001405)                                                                                                                                                                                                                                                                                          |
| `PomBase:('PomBase', 'gs')`    |              2 | [http://purl.obolibrary.org/obo/FYPO_0002484](http://purl.obolibrary.org/obo/FYPO_0002484), [http://purl.obolibrary.org/obo/FYPO_0002485](http://purl.obolibrary.org/obo/FYPO_0002485)                                                                                                                                                                                                                                                                                          |
| `PomBase:('PomBase', 'ch')`    |              1 | [http://purl.obolibrary.org/obo/FYPO_0000153](http://purl.obolibrary.org/obo/FYPO_0000153)                                                                                                                                                                                                                                                                                                                                                                                      |
| `PomBase:('PomBase', 'pr')`    |              1 | [http://purl.obolibrary.org/obo/FYPO_0005334](http://purl.obolibrary.org/obo/FYPO_0005334)                                                                                                                                                                                                                                                                                                                                                                                      |
| `PomBase:('PomBase', 'mahle')` |              1 | [http://purl.obolibrary.org/obo/FYPO_0007633](http://purl.obolibrary.org/obo/FYPO_0007633)                                                                                                                                                                                                                                                                                                                                                                                      |
| `PomBase:('PomBase', 'sm')`    |              1 | [http://purl.obolibrary.org/obo/FYPO_0007683](http://purl.obolibrary.org/obo/FYPO_0007683)                                                                                                                                                                                                                                                                                                                                                                                      |

## `Pombase`: PomBase

Overall, there were 39 invalid
xrefs to external prefixed with `Pombase` (standardized to Bioregistry
prefix [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref                |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Pombase:('Pombase', 'vw')`  |             29 | [http://purl.obolibrary.org/obo/FYPO_0002440](http://purl.obolibrary.org/obo/FYPO_0002440), [http://purl.obolibrary.org/obo/FYPO_0003290](http://purl.obolibrary.org/obo/FYPO_0003290), [http://purl.obolibrary.org/obo/FYPO_0004022](http://purl.obolibrary.org/obo/FYPO_0004022), [http://purl.obolibrary.org/obo/FYPO_0004086](http://purl.obolibrary.org/obo/FYPO_0004086), [http://purl.obolibrary.org/obo/FYPO_0004159](http://purl.obolibrary.org/obo/FYPO_0004159), ... |
| `Pombase:('Pombase', 'al')`  |              6 | [http://purl.obolibrary.org/obo/FYPO_0004989](http://purl.obolibrary.org/obo/FYPO_0004989), [http://purl.obolibrary.org/obo/FYPO_0005527](http://purl.obolibrary.org/obo/FYPO_0005527), [http://purl.obolibrary.org/obo/FYPO_0005528](http://purl.obolibrary.org/obo/FYPO_0005528), [http://purl.obolibrary.org/obo/FYPO_0006260](http://purl.obolibrary.org/obo/FYPO_0006260), [http://purl.obolibrary.org/obo/FYPO_0007084](http://purl.obolibrary.org/obo/FYPO_0007084), ... |
| `Pombase:('Pombase', 'mah')` |              4 | [http://purl.obolibrary.org/obo/FYPO_0005385](http://purl.obolibrary.org/obo/FYPO_0005385), [http://purl.obolibrary.org/obo/FYPO_0005396](http://purl.obolibrary.org/obo/FYPO_0005396), [http://purl.obolibrary.org/obo/FYPO_0006770](http://purl.obolibrary.org/obo/FYPO_0006770), [http://purl.obolibrary.org/obo/FYPO_0007288](http://purl.obolibrary.org/obo/FYPO_0007288)                                                                                                  |

## `SGD`: Saccharomyces Genome Database

Overall, there were 293 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
prefix [`sgd`](https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref                         |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:('SGD', 'phenotype_annotation')` |            293 | [http://purl.obolibrary.org/obo/FYPO_0000005](http://purl.obolibrary.org/obo/FYPO_0000005), [http://purl.obolibrary.org/obo/FYPO_0000008](http://purl.obolibrary.org/obo/FYPO_0000008), [http://purl.obolibrary.org/obo/FYPO_0000011](http://purl.obolibrary.org/obo/FYPO_0000011), [http://purl.obolibrary.org/obo/FYPO_0000012](http://purl.obolibrary.org/obo/FYPO_0000012), [http://purl.obolibrary.org/obo/FYPO_0000023](http://purl.obolibrary.org/obo/FYPO_0000023), ... |

## `SO`: Sequence types and features ontology

Overall, there were 1 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref       |   usages_count | usages                                                                                     |
|---------------------|----------------|--------------------------------------------------------------------------------------------|
| `SO:('SO', '1861')` |              1 | [http://purl.obolibrary.org/obo/FYPO_0003251](http://purl.obolibrary.org/obo/FYPO_0003251) |

