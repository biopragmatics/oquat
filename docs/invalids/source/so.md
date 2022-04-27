# so

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `so`. See the [GitHub repository](https://github.com/The-Sequence-Ontology/SO-Ontologies).


## `BioRXiv`: bioRxiv

Overall, there were 1 invalid
xrefs to external prefixed with `BioRXiv` (standardized to Bioregistry
prefix [`biorxiv`](https://bioregistry.io/biorxiv)) that
did not match the standard pattern `^(\d{4}\.\d{2}\.\d{2}\.)?\d{6,8}(v\d{1,3})?$`.

| external_xref                                           |   usages_count | usages                                                                                 |
|---------------------------------------------------------|----------------|----------------------------------------------------------------------------------------|
| `BioRXiv:('BioRXiv', 'https://doi.org/10.1101/584664')` |              1 | [http://purl.obolibrary.org/obo/SO_0002223](http://purl.obolibrary.org/obo/SO_0002223) |

## `FB`: FlyBase Gene

Overall, there were 42 invalid
xrefs to external prefixed with `FB` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref                   |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FB:('FB', 'reference_manual')` |             24 | [http://purl.obolibrary.org/obo/SO_0000062](http://purl.obolibrary.org/obo/SO_0000062), [http://purl.obolibrary.org/obo/SO_0000453](http://purl.obolibrary.org/obo/SO_0000453), [http://purl.obolibrary.org/obo/SO_0001784](http://purl.obolibrary.org/obo/SO_0001784), [http://purl.obolibrary.org/obo/SO_1000044](http://purl.obolibrary.org/obo/SO_1000044), [http://purl.obolibrary.org/obo/SO_1000046](http://purl.obolibrary.org/obo/SO_1000046), ... |
| `FB:('FB', 'km')`               |              6 | [http://purl.obolibrary.org/obo/SO_0000461](http://purl.obolibrary.org/obo/SO_0000461), [http://purl.obolibrary.org/obo/SO_0000465](http://purl.obolibrary.org/obo/SO_0000465), [http://purl.obolibrary.org/obo/SO_0000512](http://purl.obolibrary.org/obo/SO_0000512), [http://purl.obolibrary.org/obo/SO_0000547](http://purl.obolibrary.org/obo/SO_0000547), [http://purl.obolibrary.org/obo/SO_0000549](http://purl.obolibrary.org/obo/SO_0000549), ... |
| `FB:('FB', 'mc')`               |              4 | [http://purl.obolibrary.org/obo/SO_0000796](http://purl.obolibrary.org/obo/SO_0000796), [http://purl.obolibrary.org/obo/SO_0000797](http://purl.obolibrary.org/obo/SO_0000797), [http://purl.obolibrary.org/obo/SO_0000798](http://purl.obolibrary.org/obo/SO_0000798), [http://purl.obolibrary.org/obo/SO_0000799](http://purl.obolibrary.org/obo/SO_0000799)                                                                                              |
| `FB:('FB', 'gm')`               |              4 | [http://purl.obolibrary.org/obo/SO_0000800](http://purl.obolibrary.org/obo/SO_0000800), [http://purl.obolibrary.org/obo/SO_0000801](http://purl.obolibrary.org/obo/SO_0000801), [http://purl.obolibrary.org/obo/SO_0000802](http://purl.obolibrary.org/obo/SO_0000802), [http://purl.obolibrary.org/obo/SO_0000803](http://purl.obolibrary.org/obo/SO_0000803)                                                                                              |
| `FB:('FB', 'manual')`           |              2 | [http://purl.obolibrary.org/obo/SO_1000142](http://purl.obolibrary.org/obo/SO_1000142), [http://purl.obolibrary.org/obo/SO_1000143](http://purl.obolibrary.org/obo/SO_1000143)                                                                                                                                                                                                                                                                              |
| `FB:('FB', 'WG')`               |              1 | [http://purl.obolibrary.org/obo/SO_0000719](http://purl.obolibrary.org/obo/SO_0000719)                                                                                                                                                                                                                                                                                                                                                                      |
| `FB:('FB', 'cds')`              |              1 | [http://purl.obolibrary.org/obo/SO_0000934](http://purl.obolibrary.org/obo/SO_0000934)                                                                                                                                                                                                                                                                                                                                                                      |

## `GO`: Gene Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref      |   usages_count | usages                                                                                                                                                                                                                                                                 |
|--------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:('GO', 'mah')` |              3 | [http://purl.obolibrary.org/obo/SO_0001861](http://purl.obolibrary.org/obo/SO_0001861), [http://purl.obolibrary.org/obo/SO_0001861](http://purl.obolibrary.org/obo/SO_0001861), [http://purl.obolibrary.org/obo/SO_0001871](http://purl.obolibrary.org/obo/SO_0001871) |

## `HGNC`: HUGO Gene Nomenclature Committee

Overall, there were 1 invalid
xrefs to external prefixed with `HGNC` (standardized to Bioregistry
prefix [`hgnc`](https://bioregistry.io/hgnc)) that
did not match the standard pattern `^((HGNC|hgnc):)?\d{1,5}$`.

| external_xref         |   usages_count | usages                                                                                 |
|-----------------------|----------------|----------------------------------------------------------------------------------------|
| `HGNC:('HGNC', 'mw')` |              1 | [http://purl.obolibrary.org/obo/SO_0001877](http://purl.obolibrary.org/obo/SO_0001877) |

## `MGD`: Mouse Genome Informatics

Overall, there were 1 invalid
xrefs to external prefixed with `MGD` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref       |   usages_count | usages                                                                                 |
|---------------------|----------------|----------------------------------------------------------------------------------------|
| `MGD:('MGD', 'tm')` |              1 | [http://purl.obolibrary.org/obo/SO_0001644](http://purl.obolibrary.org/obo/SO_0001644) |

## `MGI`: Mouse Genome Informatics

Overall, there were 1 invalid
xrefs to external prefixed with `MGI` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref          |   usages_count | usages                                                                                 |
|------------------------|----------------|----------------------------------------------------------------------------------------|
| `MGI:('MGI', 'hdeen')` |              1 | [http://purl.obolibrary.org/obo/SO_0001503](http://purl.obolibrary.org/obo/SO_0001503) |

## `PMC`: Pubmed Central

Overall, there were 1 invalid
xrefs to external prefixed with `PMC` (standardized to Bioregistry
prefix [`pmc`](https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref           |   usages_count | usages                                                                                 |
|-------------------------|----------------|----------------------------------------------------------------------------------------|
| `PMC:('PMC', '126017')` |              1 | [http://purl.obolibrary.org/obo/SO_0002095](http://purl.obolibrary.org/obo/SO_0002095) |

## `PMID`: PubMed

Overall, there were 22 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                             |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PMID:('PMID', ' 24572720')`              |              5 | [http://purl.obolibrary.org/obo/SO_0002344](http://purl.obolibrary.org/obo/SO_0002344), [http://purl.obolibrary.org/obo/SO_0002345](http://purl.obolibrary.org/obo/SO_0002345), [http://purl.obolibrary.org/obo/SO_0002346](http://purl.obolibrary.org/obo/SO_0002346), [http://purl.obolibrary.org/obo/SO_0002347](http://purl.obolibrary.org/obo/SO_0002347), [http://purl.obolibrary.org/obo/SO_0002348](http://purl.obolibrary.org/obo/SO_0002348) |
| `PMID:('PMID', '12537576:16827941')`      |              4 | [http://purl.obolibrary.org/obo/SO_0001158](http://purl.obolibrary.org/obo/SO_0001158), [http://purl.obolibrary.org/obo/SO_0001159](http://purl.obolibrary.org/obo/SO_0001159), [http://purl.obolibrary.org/obo/SO_0001160](http://purl.obolibrary.org/obo/SO_0001160), [http://purl.obolibrary.org/obo/SO_0001161](http://purl.obolibrary.org/obo/SO_0001161)                                                                                         |
| `PMID:('PMID', ' 118436')`                |              2 | [http://purl.obolibrary.org/obo/SO_0002336](http://purl.obolibrary.org/obo/SO_0002336), [http://purl.obolibrary.org/obo/SO_0002337](http://purl.obolibrary.org/obo/SO_0002337)                                                                                                                                                                                                                                                                         |
| `PMID:('PMID', ' 29474379')`              |              2 | [http://purl.obolibrary.org/obo/SO_0002336](http://purl.obolibrary.org/obo/SO_0002336), [http://purl.obolibrary.org/obo/SO_0002337](http://purl.obolibrary.org/obo/SO_0002337)                                                                                                                                                                                                                                                                         |
| `PMID:('PMID', ' 3136294')`               |              2 | [http://purl.obolibrary.org/obo/SO_0002336](http://purl.obolibrary.org/obo/SO_0002336), [http://purl.obolibrary.org/obo/SO_0002337](http://purl.obolibrary.org/obo/SO_0002337)                                                                                                                                                                                                                                                                         |
| `PMID:('PMID', '=12409455')`              |              1 | [http://purl.obolibrary.org/obo/SO_0000394](http://purl.obolibrary.org/obo/SO_0000394)                                                                                                                                                                                                                                                                                                                                                                 |
| `PMID:('PMID', '16827941:12537576')`      |              1 | [http://purl.obolibrary.org/obo/SO_0001157](http://purl.obolibrary.org/obo/SO_0001157)                                                                                                                                                                                                                                                                                                                                                                 |
| `PMID:('PMID', '12537576:15231738')`      |              1 | [http://purl.obolibrary.org/obo/SO_0001162](http://purl.obolibrary.org/obo/SO_0001162)                                                                                                                                                                                                                                                                                                                                                                 |
| `PMID:('PMID', '15388847,PMID:16524884')` |              1 | [http://purl.obolibrary.org/obo/SO_0002235](http://purl.obolibrary.org/obo/SO_0002235)                                                                                                                                                                                                                                                                                                                                                                 |
| `PMID:('PMID', ' 19407924')`              |              1 | [http://purl.obolibrary.org/obo/SO_0002293](http://purl.obolibrary.org/obo/SO_0002293)                                                                                                                                                                                                                                                                                                                                                                 |
| `PMID:('PMID', ' 16236432')`              |              1 | [http://purl.obolibrary.org/obo/SO_0002350](http://purl.obolibrary.org/obo/SO_0002350)                                                                                                                                                                                                                                                                                                                                                                 |
| `PMID:('PMID', ' 17608616')`              |              1 | [http://purl.obolibrary.org/obo/SO_0002350](http://purl.obolibrary.org/obo/SO_0002350)                                                                                                                                                                                                                                                                                                                                                                 |

## `PomBase`: PomBase

Overall, there were 12 invalid
xrefs to external prefixed with `PomBase` (standardized to Bioregistry
prefix [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref                |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PomBase:('PomBase', 'mah')` |              6 | [http://purl.obolibrary.org/obo/SO_0001808](http://purl.obolibrary.org/obo/SO_0001808), [http://purl.obolibrary.org/obo/SO_0001811](http://purl.obolibrary.org/obo/SO_0001811), [http://purl.obolibrary.org/obo/SO_0001812](http://purl.obolibrary.org/obo/SO_0001812), [http://purl.obolibrary.org/obo/SO_0001813](http://purl.obolibrary.org/obo/SO_0001813), [http://purl.obolibrary.org/obo/SO_0001905](http://purl.obolibrary.org/obo/SO_0001905), ... |
| `PomBase:('PomBase', 'al')`  |              3 | [http://purl.obolibrary.org/obo/SO_0000370](http://purl.obolibrary.org/obo/SO_0000370), [http://purl.obolibrary.org/obo/SO_0002022](http://purl.obolibrary.org/obo/SO_0002022), [http://purl.obolibrary.org/obo/SO_0002207](http://purl.obolibrary.org/obo/SO_0002207)                                                                                                                                                                                      |
| `PomBase:('PomBase', 'vw')`  |              2 | [http://purl.obolibrary.org/obo/SO_0002025](http://purl.obolibrary.org/obo/SO_0002025), [http://purl.obolibrary.org/obo/SO_0002215](http://purl.obolibrary.org/obo/SO_0002215)                                                                                                                                                                                                                                                                              |
| `PomBase:('PomBase', 'mh')`  |              1 | [http://purl.obolibrary.org/obo/SO_0002208](http://purl.obolibrary.org/obo/SO_0002208)                                                                                                                                                                                                                                                                                                                                                                      |

## `POMBASE`: PomBase

Overall, there were 3 invalid
xrefs to external prefixed with `POMBASE` (standardized to Bioregistry
prefix [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref                |   usages_count | usages                                                                                                                                                                         |
|------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `POMBASE:('POMBASE', 'mah')` |              2 | [http://purl.obolibrary.org/obo/SO_0002027](http://purl.obolibrary.org/obo/SO_0002027), [http://purl.obolibrary.org/obo/SO_0002028](http://purl.obolibrary.org/obo/SO_0002028) |
| `POMBASE:('POMBASE', 'vw')`  |              1 | [http://purl.obolibrary.org/obo/SO_0002029](http://purl.obolibrary.org/obo/SO_0002029)                                                                                         |

## `RFAM`: Rfam database of RNA families

Overall, there were 2 invalid
xrefs to external prefixed with `RFAM` (standardized to Bioregistry
prefix [`rfam`](https://bioregistry.io/rfam)) that
did not match the standard pattern `^RF\d{5}$`.

| external_xref         |   usages_count | usages                                                                                                                                                                         |
|-----------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RFAM:('RFAM', 'jd')` |              2 | [http://purl.obolibrary.org/obo/SO_0001427](http://purl.obolibrary.org/obo/SO_0001427), [http://purl.obolibrary.org/obo/SO_0001459](http://purl.obolibrary.org/obo/SO_0001459) |

## `SGD`: Saccharomyces Genome Database

Overall, there were 12 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
prefix [`sgd`](https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref       |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:('SGD', 'jd')` |              6 | [http://purl.obolibrary.org/obo/SO_0002001](http://purl.obolibrary.org/obo/SO_0002001), [http://purl.obolibrary.org/obo/SO_0002002](http://purl.obolibrary.org/obo/SO_0002002), [http://purl.obolibrary.org/obo/SO_0002003](http://purl.obolibrary.org/obo/SO_0002003), [http://purl.obolibrary.org/obo/SO_0002004](http://purl.obolibrary.org/obo/SO_0002004), [http://purl.obolibrary.org/obo/SO_0002024](http://purl.obolibrary.org/obo/SO_0002024), ... |
| `SGD:('SGD', 'rb')` |              3 | [http://purl.obolibrary.org/obo/SO_0000236](http://purl.obolibrary.org/obo/SO_0000236), [http://purl.obolibrary.org/obo/SO_0000717](http://purl.obolibrary.org/obo/SO_0000717), [http://purl.obolibrary.org/obo/SO_0000718](http://purl.obolibrary.org/obo/SO_0000718)                                                                                                                                                                                      |
| `SGD:('SGD', 'se')` |              3 | [http://purl.obolibrary.org/obo/SO_0002048](http://purl.obolibrary.org/obo/SO_0002048), [http://purl.obolibrary.org/obo/SO_0002059](http://purl.obolibrary.org/obo/SO_0002059), [http://purl.obolibrary.org/obo/SO_0005853](http://purl.obolibrary.org/obo/SO_0005853)                                                                                                                                                                                      |

## `SO`: Sequence types and features ontology

Overall, there were 1,224 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                  |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SO:('SO', 'ke')`              |            885 | [http://purl.obolibrary.org/obo/SO_0000001](http://purl.obolibrary.org/obo/SO_0000001), [http://purl.obolibrary.org/obo/SO_0000002](http://purl.obolibrary.org/obo/SO_0000002), [http://purl.obolibrary.org/obo/SO_0000006](http://purl.obolibrary.org/obo/SO_0000006), [http://purl.obolibrary.org/obo/SO_0000013](http://purl.obolibrary.org/obo/SO_0000013), [http://purl.obolibrary.org/obo/SO_0000020](http://purl.obolibrary.org/obo/SO_0000020), ... |
| `SO:('SO', 'xp')`              |            109 | [http://purl.obolibrary.org/obo/SO_0000078](http://purl.obolibrary.org/obo/SO_0000078), [http://purl.obolibrary.org/obo/SO_0000087](http://purl.obolibrary.org/obo/SO_0000087), [http://purl.obolibrary.org/obo/SO_0000088](http://purl.obolibrary.org/obo/SO_0000088), [http://purl.obolibrary.org/obo/SO_0000089](http://purl.obolibrary.org/obo/SO_0000089), [http://purl.obolibrary.org/obo/SO_0000090](http://purl.obolibrary.org/obo/SO_0000090), ... |
| `SO:('SO', 'ma')`              |             76 | [http://purl.obolibrary.org/obo/SO_0000036](http://purl.obolibrary.org/obo/SO_0000036), [http://purl.obolibrary.org/obo/SO_0000037](http://purl.obolibrary.org/obo/SO_0000037), [http://purl.obolibrary.org/obo/SO_0000040](http://purl.obolibrary.org/obo/SO_0000040), [http://purl.obolibrary.org/obo/SO_0000042](http://purl.obolibrary.org/obo/SO_0000042), [http://purl.obolibrary.org/obo/SO_0000051](http://purl.obolibrary.org/obo/SO_0000051), ... |
| `SO:('SO', 'cb')`              |             41 | [http://purl.obolibrary.org/obo/SO_0000059](http://purl.obolibrary.org/obo/SO_0000059), [http://purl.obolibrary.org/obo/SO_0000061](http://purl.obolibrary.org/obo/SO_0000061), [http://purl.obolibrary.org/obo/SO_0000419](http://purl.obolibrary.org/obo/SO_0000419), [http://purl.obolibrary.org/obo/SO_0000694](http://purl.obolibrary.org/obo/SO_0000694), [http://purl.obolibrary.org/obo/SO_0000836](http://purl.obolibrary.org/obo/SO_0000836), ... |
| `SO:('SO', 'nlw')`             |             21 | [http://purl.obolibrary.org/obo/SO_0000708](http://purl.obolibrary.org/obo/SO_0000708), [http://purl.obolibrary.org/obo/SO_0000709](http://purl.obolibrary.org/obo/SO_0000709), [http://purl.obolibrary.org/obo/SO_0001464](http://purl.obolibrary.org/obo/SO_0001464), [http://purl.obolibrary.org/obo/SO_0001465](http://purl.obolibrary.org/obo/SO_0001465), [http://purl.obolibrary.org/obo/SO_0001466](http://purl.obolibrary.org/obo/SO_0001466), ... |
| `SO:('SO', 'as')`              |             14 | [http://purl.obolibrary.org/obo/SO_0000140](http://purl.obolibrary.org/obo/SO_0000140), [http://purl.obolibrary.org/obo/SO_0000365](http://purl.obolibrary.org/obo/SO_0000365), [http://purl.obolibrary.org/obo/SO_0000367](http://purl.obolibrary.org/obo/SO_0000367), [http://purl.obolibrary.org/obo/SO_0000942](http://purl.obolibrary.org/obo/SO_0000942), [http://purl.obolibrary.org/obo/SO_0000943](http://purl.obolibrary.org/obo/SO_0000943), ... |
| `SO:('SO', 'cjm')`             |             11 | [http://purl.obolibrary.org/obo/SO_0000162](http://purl.obolibrary.org/obo/SO_0000162), [http://purl.obolibrary.org/obo/SO_0000163](http://purl.obolibrary.org/obo/SO_0000163), [http://purl.obolibrary.org/obo/SO_0000164](http://purl.obolibrary.org/obo/SO_0000164), [http://purl.obolibrary.org/obo/SO_0000196](http://purl.obolibrary.org/obo/SO_0000196), [http://purl.obolibrary.org/obo/SO_0000197](http://purl.obolibrary.org/obo/SO_0000197), ... |
| `SO:('SO', 'immuno_workshop')` |              8 | [http://purl.obolibrary.org/obo/SO_0000704](http://purl.obolibrary.org/obo/SO_0000704), [http://purl.obolibrary.org/obo/SO_0001023](http://purl.obolibrary.org/obo/SO_0001023), [http://purl.obolibrary.org/obo/SO_0001024](http://purl.obolibrary.org/obo/SO_0001024), [http://purl.obolibrary.org/obo/SO_0001025](http://purl.obolibrary.org/obo/SO_0001025), [http://purl.obolibrary.org/obo/SO_0001026](http://purl.obolibrary.org/obo/SO_0001026), ... |
| `SO:('SO', 'rd')`              |              7 | [http://purl.obolibrary.org/obo/SO_0000150](http://purl.obolibrary.org/obo/SO_0000150), [http://purl.obolibrary.org/obo/SO_0000307](http://purl.obolibrary.org/obo/SO_0000307), [http://purl.obolibrary.org/obo/SO_0000337](http://purl.obolibrary.org/obo/SO_0000337), [http://purl.obolibrary.org/obo/SO_0000339](http://purl.obolibrary.org/obo/SO_0000339), [http://purl.obolibrary.org/obo/SO_0000468](http://purl.obolibrary.org/obo/SO_0000468), ... |
| `SO:('SO', 'vw')`              |              7 | [http://purl.obolibrary.org/obo/SO_0001794](http://purl.obolibrary.org/obo/SO_0001794), [http://purl.obolibrary.org/obo/SO_0001795](http://purl.obolibrary.org/obo/SO_0001795), [http://purl.obolibrary.org/obo/SO_0001796](http://purl.obolibrary.org/obo/SO_0001796), [http://purl.obolibrary.org/obo/SO_0001798](http://purl.obolibrary.org/obo/SO_0001798), [http://purl.obolibrary.org/obo/SO_0001799](http://purl.obolibrary.org/obo/SO_0001799), ... |
| `SO:('SO', 'bm')`              |              6 | [http://purl.obolibrary.org/obo/SO_0001218](http://purl.obolibrary.org/obo/SO_0001218), [http://purl.obolibrary.org/obo/SO_0001483](http://purl.obolibrary.org/obo/SO_0001483), [http://purl.obolibrary.org/obo/SO_0001745](http://purl.obolibrary.org/obo/SO_0001745), [http://purl.obolibrary.org/obo/SO_0001746](http://purl.obolibrary.org/obo/SO_0001746), [http://purl.obolibrary.org/obo/SO_0001902](http://purl.obolibrary.org/obo/SO_0001902), ... |
| `SO:('SO', 'ls')`              |              4 | [http://purl.obolibrary.org/obo/SO_0000007](http://purl.obolibrary.org/obo/SO_0000007), [http://purl.obolibrary.org/obo/SO_0000148](http://purl.obolibrary.org/obo/SO_0000148), [http://purl.obolibrary.org/obo/SO_0000149](http://purl.obolibrary.org/obo/SO_0000149), [http://purl.obolibrary.org/obo/SO_0000688](http://purl.obolibrary.org/obo/SO_0000688)                                                                                              |
| `SO:('SO', 'regcreative')`     |              4 | [http://purl.obolibrary.org/obo/SO_0000167](http://purl.obolibrary.org/obo/SO_0000167), [http://purl.obolibrary.org/obo/SO_0000627](http://purl.obolibrary.org/obo/SO_0000627), [http://purl.obolibrary.org/obo/SO_0001055](http://purl.obolibrary.org/obo/SO_0001055), [http://purl.obolibrary.org/obo/SO_0001058](http://purl.obolibrary.org/obo/SO_0001058)                                                                                              |
| `SO:('SO', 'ml')`              |              4 | [http://purl.obolibrary.org/obo/SO_0001668](http://purl.obolibrary.org/obo/SO_0001668), [http://purl.obolibrary.org/obo/SO_0001980](http://purl.obolibrary.org/obo/SO_0001980), [http://purl.obolibrary.org/obo/SO_0001981](http://purl.obolibrary.org/obo/SO_0001981), [http://purl.obolibrary.org/obo/SO_0001982](http://purl.obolibrary.org/obo/SO_0001982)                                                                                              |
| `SO:('SO', 'ds')`              |              4 | [http://purl.obolibrary.org/obo/SO_0002329](http://purl.obolibrary.org/obo/SO_0002329), [http://purl.obolibrary.org/obo/SO_0002330](http://purl.obolibrary.org/obo/SO_0002330), [http://purl.obolibrary.org/obo/SO_0002331](http://purl.obolibrary.org/obo/SO_0002331), [http://purl.obolibrary.org/obo/SO_0002332](http://purl.obolibrary.org/obo/SO_0002332)                                                                                              |
| `SO:('SO', 'andrewgibson')`    |              3 | [http://purl.obolibrary.org/obo/SO_0001915](http://purl.obolibrary.org/obo/SO_0001915), [http://purl.obolibrary.org/obo/SO_0001916](http://purl.obolibrary.org/obo/SO_0001916), [http://purl.obolibrary.org/obo/SO_0001917](http://purl.obolibrary.org/obo/SO_0001917)                                                                                                                                                                                      |
| `SO:('SO', 'rtapella')`        |              3 | [http://purl.obolibrary.org/obo/SO_0001918](http://purl.obolibrary.org/obo/SO_0001918), [http://purl.obolibrary.org/obo/SO_0001919](http://purl.obolibrary.org/obo/SO_0001919), [http://purl.obolibrary.org/obo/SO_0001920](http://purl.obolibrary.org/obo/SO_0001920)                                                                                                                                                                                      |
| `SO:('SO', 'jk')`              |              2 | [http://purl.obolibrary.org/obo/SO_0000931](http://purl.obolibrary.org/obo/SO_0000931), [http://purl.obolibrary.org/obo/SO_0000978](http://purl.obolibrary.org/obo/SO_0000978)                                                                                                                                                                                                                                                                              |
| `SO:('SO', 'chado')`           |              2 | [http://purl.obolibrary.org/obo/SO_0001416](http://purl.obolibrary.org/obo/SO_0001416), [http://purl.obolibrary.org/obo/SO_0001417](http://purl.obolibrary.org/obo/SO_0001417)                                                                                                                                                                                                                                                                              |
| `SO:('SO', 'jh')`              |              1 | [http://purl.obolibrary.org/obo/SO_0000552](http://purl.obolibrary.org/obo/SO_0000552)                                                                                                                                                                                                                                                                                                                                                                      |
| `SO:('SO', 'SG')`              |              1 | [http://purl.obolibrary.org/obo/SO_0000727](http://purl.obolibrary.org/obo/SO_0000727)                                                                                                                                                                                                                                                                                                                                                                      |
| `SO:('SO', 'GAR')`             |              1 | [http://purl.obolibrary.org/obo/SO_0000839](http://purl.obolibrary.org/obo/SO_0000839)                                                                                                                                                                                                                                                                                                                                                                      |
| `SO:('SO', 'jestill')`         |              1 | [http://purl.obolibrary.org/obo/SO_0001642](http://purl.obolibrary.org/obo/SO_0001642)                                                                                                                                                                                                                                                                                                                                                                      |
| `SO:('SO', 'db')`              |              1 | [http://purl.obolibrary.org/obo/SO_0001645](http://purl.obolibrary.org/obo/SO_0001645)                                                                                                                                                                                                                                                                                                                                                                      |
| `SO:('SO', 'AF')`              |              1 | [http://purl.obolibrary.org/obo/SO_0001658](http://purl.obolibrary.org/obo/SO_0001658)                                                                                                                                                                                                                                                                                                                                                                      |
| `SO:('SO', 'KE')`              |              1 | [http://purl.obolibrary.org/obo/SO_0001731](http://purl.obolibrary.org/obo/SO_0001731)                                                                                                                                                                                                                                                                                                                                                                      |
| `SO:('SO', 'mc')`              |              1 | [http://purl.obolibrary.org/obo/SO_0001740](http://purl.obolibrary.org/obo/SO_0001740)                                                                                                                                                                                                                                                                                                                                                                      |
| `SO:('SO', 'hd')`              |              1 | [http://purl.obolibrary.org/obo/SO_0001741](http://purl.obolibrary.org/obo/SO_0001741)                                                                                                                                                                                                                                                                                                                                                                      |
| `SO:('SO', 'BM')`              |              1 | [http://purl.obolibrary.org/obo/SO_0001744](http://purl.obolibrary.org/obo/SO_0001744)                                                                                                                                                                                                                                                                                                                                                                      |
| `SO:('SO', 'myl')`             |              1 | [http://purl.obolibrary.org/obo/SO_0001959](http://purl.obolibrary.org/obo/SO_0001959)                                                                                                                                                                                                                                                                                                                                                                      |
| `SO:('SO', 'rs')`              |              1 | [http://purl.obolibrary.org/obo/SO_0002049](http://purl.obolibrary.org/obo/SO_0002049)                                                                                                                                                                                                                                                                                                                                                                      |
| `SO:('SO', 'nrs')`             |              1 | [http://purl.obolibrary.org/obo/SO_0002095](http://purl.obolibrary.org/obo/SO_0002095)                                                                                                                                                                                                                                                                                                                                                                      |

## `UniProt`: UniProt Protein

Overall, there were 21 invalid
xrefs to external prefixed with `UniProt` (standardized to Bioregistry
prefix [`uniprot`](https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref                            |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UniProt:('UniProt', 'curation_manual')` |             19 | [http://purl.obolibrary.org/obo/SO_0001064](http://purl.obolibrary.org/obo/SO_0001064), [http://purl.obolibrary.org/obo/SO_0001066](http://purl.obolibrary.org/obo/SO_0001066), [http://purl.obolibrary.org/obo/SO_0001067](http://purl.obolibrary.org/obo/SO_0001067), [http://purl.obolibrary.org/obo/SO_0001080](http://purl.obolibrary.org/obo/SO_0001080), [http://purl.obolibrary.org/obo/SO_0001083](http://purl.obolibrary.org/obo/SO_0001083), ... |
| `UniProt:('UniProt', 'curator_manual')`  |              1 | [http://purl.obolibrary.org/obo/SO_0001077](http://purl.obolibrary.org/obo/SO_0001077)                                                                                                                                                                                                                                                                                                                                                                      |
| `UniProt:('UniProt', 'Curation_manual')` |              1 | [http://purl.obolibrary.org/obo/SO_0001093](http://purl.obolibrary.org/obo/SO_0001093)                                                                                                                                                                                                                                                                                                                                                                      |

## `uniprot`: UniProt Protein

Overall, there were 31 invalid
xrefs to external prefixed with `uniprot` (standardized to Bioregistry
prefix [`uniprot`](https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref                         |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uniprot:('uniprot', 'feature_type')` |             28 | [http://purl.obolibrary.org/obo/SO_0000417](http://purl.obolibrary.org/obo/SO_0000417), [http://purl.obolibrary.org/obo/SO_0000418](http://purl.obolibrary.org/obo/SO_0000418), [http://purl.obolibrary.org/obo/SO_0000419](http://purl.obolibrary.org/obo/SO_0000419), [http://purl.obolibrary.org/obo/SO_0000691](http://purl.obolibrary.org/obo/SO_0000691), [http://purl.obolibrary.org/obo/SO_0000725](http://purl.obolibrary.org/obo/SO_0000725), ... |
| `uniprot:('uniprot', 'feature')`      |              2 | [http://purl.obolibrary.org/obo/SO_0001655](http://purl.obolibrary.org/obo/SO_0001655), [http://purl.obolibrary.org/obo/SO_0100020](http://purl.obolibrary.org/obo/SO_0100020)                                                                                                                                                                                                                                                                              |
| `uniprot:('uniprot', 'curation')`     |              1 | [http://purl.obolibrary.org/obo/SO_0001091](http://purl.obolibrary.org/obo/SO_0001091)                                                                                                                                                                                                                                                                                                                                                                      |

## `WB`: WormBase database of nematode biology

Overall, there were 1 invalid
xrefs to external prefixed with `WB` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref      |   usages_count | usages                                                                                 |
|--------------------|----------------|----------------------------------------------------------------------------------------|
| `WB:('WB', 'ems')` |              1 | [http://purl.obolibrary.org/obo/SO_0000274](http://purl.obolibrary.org/obo/SO_0000274) |

## `xenbase`: Xenbase

Overall, there were 5 invalid
xrefs to external prefixed with `xenbase` (standardized to Bioregistry
prefix [`xenbase`](https://bioregistry.io/xenbase)) that
did not match the standard pattern `^XB\-\w+\-\d+$`.

| external_xref               |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `xenbase:('xenbase', 'jb')` |              5 | [http://purl.obolibrary.org/obo/SO_0001203](http://purl.obolibrary.org/obo/SO_0001203), [http://purl.obolibrary.org/obo/SO_0001204](http://purl.obolibrary.org/obo/SO_0001204), [http://purl.obolibrary.org/obo/SO_0001205](http://purl.obolibrary.org/obo/SO_0001205), [http://purl.obolibrary.org/obo/SO_0001206](http://purl.obolibrary.org/obo/SO_0001206), [http://purl.obolibrary.org/obo/SO_0001207](http://purl.obolibrary.org/obo/SO_0001207) |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 6 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref         |   usages_count | usages                                                                                                                                                                                                                                                                 |
|-----------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:('ZFIN', 'dh')` |              3 | [http://purl.obolibrary.org/obo/SO_0001477](http://purl.obolibrary.org/obo/SO_0001477), [http://purl.obolibrary.org/obo/SO_0001478](http://purl.obolibrary.org/obo/SO_0001478), [http://purl.obolibrary.org/obo/SO_0001479](http://purl.obolibrary.org/obo/SO_0001479) |
| `ZFIN:('ZFIN', 'mh')` |              2 | [http://purl.obolibrary.org/obo/SO_0001480](http://purl.obolibrary.org/obo/SO_0001480), [http://purl.obolibrary.org/obo/SO_0001481](http://purl.obolibrary.org/obo/SO_0001481)                                                                                         |
| `ZFIN:('ZFIN', 'st')` |              1 | [http://purl.obolibrary.org/obo/SO_0002217](http://purl.obolibrary.org/obo/SO_0002217)                                                                                                                                                                                 |

