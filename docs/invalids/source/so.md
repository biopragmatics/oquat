# so

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `so`. See the [GitHub repository](https://github.com/The-Sequence-Ontology/SO-Ontologies).


## `BioRXiv`: bioRxiv

Overall, there were 1 invalid
xrefs to external prefixed with `BioRXiv` (standardized to Bioregistry
prefix [`biorxiv`](https://bioregistry.io/biorxiv)) that
did not match the standard pattern `^(\d{4}\.\d{2}\.\d{2}\.)?\d{6,8}(v\d{1,3})?$`.

| external_xref                                           |   usages_count | usages                                          |
|---------------------------------------------------------|----------------|-------------------------------------------------|
| `BioRXiv:('BioRXiv', 'https://doi.org/10.1101/584664')` |              1 | [SO:0002223](https://bioregistry.io/SO:0002223) |

## `FB`: FlyBase Gene

Overall, there were 42 invalid
xrefs to external prefixed with `FB` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref                   |   usages_count | usages                                                                                                                                                                                                                                                   |
|---------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FB:('FB', 'reference_manual')` |             24 | [SO:0000062](https://bioregistry.io/SO:0000062), [SO:0000453](https://bioregistry.io/SO:0000453), [SO:0001784](https://bioregistry.io/SO:0001784), [SO:1000044](https://bioregistry.io/SO:1000044), [SO:1000046](https://bioregistry.io/SO:1000046), ... |
| `FB:('FB', 'km')`               |              6 | [SO:0000461](https://bioregistry.io/SO:0000461), [SO:0000465](https://bioregistry.io/SO:0000465), [SO:0000512](https://bioregistry.io/SO:0000512), [SO:0000547](https://bioregistry.io/SO:0000547), [SO:0000549](https://bioregistry.io/SO:0000549), ... |
| `FB:('FB', 'mc')`               |              4 | [SO:0000796](https://bioregistry.io/SO:0000796), [SO:0000797](https://bioregistry.io/SO:0000797), [SO:0000798](https://bioregistry.io/SO:0000798), [SO:0000799](https://bioregistry.io/SO:0000799)                                                       |
| `FB:('FB', 'gm')`               |              4 | [SO:0000800](https://bioregistry.io/SO:0000800), [SO:0000801](https://bioregistry.io/SO:0000801), [SO:0000802](https://bioregistry.io/SO:0000802), [SO:0000803](https://bioregistry.io/SO:0000803)                                                       |
| `FB:('FB', 'manual')`           |              2 | [SO:1000142](https://bioregistry.io/SO:1000142), [SO:1000143](https://bioregistry.io/SO:1000143)                                                                                                                                                         |
| `FB:('FB', 'WG')`               |              1 | [SO:0000719](https://bioregistry.io/SO:0000719)                                                                                                                                                                                                          |
| `FB:('FB', 'cds')`              |              1 | [SO:0000934](https://bioregistry.io/SO:0000934)                                                                                                                                                                                                          |

## `GO`: Gene Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref      |   usages_count | usages                                                                                                                                            |
|--------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:('GO', 'mah')` |              3 | [SO:0001861](https://bioregistry.io/SO:0001861), [SO:0001861](https://bioregistry.io/SO:0001861), [SO:0001871](https://bioregistry.io/SO:0001871) |

## `HGNC`: HUGO Gene Nomenclature Committee

Overall, there were 1 invalid
xrefs to external prefixed with `HGNC` (standardized to Bioregistry
prefix [`hgnc`](https://bioregistry.io/hgnc)) that
did not match the standard pattern `^((HGNC|hgnc):)?\d{1,5}$`.

| external_xref         |   usages_count | usages                                          |
|-----------------------|----------------|-------------------------------------------------|
| `HGNC:('HGNC', 'mw')` |              1 | [SO:0001877](https://bioregistry.io/SO:0001877) |

## `MGD`: Mouse Genome Informatics

Overall, there were 1 invalid
xrefs to external prefixed with `MGD` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref       |   usages_count | usages                                          |
|---------------------|----------------|-------------------------------------------------|
| `MGD:('MGD', 'tm')` |              1 | [SO:0001644](https://bioregistry.io/SO:0001644) |

## `MGI`: Mouse Genome Informatics

Overall, there were 1 invalid
xrefs to external prefixed with `MGI` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref          |   usages_count | usages                                          |
|------------------------|----------------|-------------------------------------------------|
| `MGI:('MGI', 'hdeen')` |              1 | [SO:0001503](https://bioregistry.io/SO:0001503) |

## `PMC`: Pubmed Central

Overall, there were 1 invalid
xrefs to external prefixed with `PMC` (standardized to Bioregistry
prefix [`pmc`](https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref           |   usages_count | usages                                          |
|-------------------------|----------------|-------------------------------------------------|
| `PMC:('PMC', '126017')` |              1 | [SO:0002095](https://bioregistry.io/SO:0002095) |

## `PMID`: PubMed

Overall, there were 22 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                             |   usages_count | usages                                                                                                                                                                                                                                              |
|-------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PMID:('PMID', ' 24572720')`              |              5 | [SO:0002344](https://bioregistry.io/SO:0002344), [SO:0002345](https://bioregistry.io/SO:0002345), [SO:0002346](https://bioregistry.io/SO:0002346), [SO:0002347](https://bioregistry.io/SO:0002347), [SO:0002348](https://bioregistry.io/SO:0002348) |
| `PMID:('PMID', '12537576:16827941')`      |              4 | [SO:0001158](https://bioregistry.io/SO:0001158), [SO:0001159](https://bioregistry.io/SO:0001159), [SO:0001160](https://bioregistry.io/SO:0001160), [SO:0001161](https://bioregistry.io/SO:0001161)                                                  |
| `PMID:('PMID', ' 118436')`                |              2 | [SO:0002336](https://bioregistry.io/SO:0002336), [SO:0002337](https://bioregistry.io/SO:0002337)                                                                                                                                                    |
| `PMID:('PMID', ' 29474379')`              |              2 | [SO:0002336](https://bioregistry.io/SO:0002336), [SO:0002337](https://bioregistry.io/SO:0002337)                                                                                                                                                    |
| `PMID:('PMID', ' 3136294')`               |              2 | [SO:0002336](https://bioregistry.io/SO:0002336), [SO:0002337](https://bioregistry.io/SO:0002337)                                                                                                                                                    |
| `PMID:('PMID', '=12409455')`              |              1 | [SO:0000394](https://bioregistry.io/SO:0000394)                                                                                                                                                                                                     |
| `PMID:('PMID', '16827941:12537576')`      |              1 | [SO:0001157](https://bioregistry.io/SO:0001157)                                                                                                                                                                                                     |
| `PMID:('PMID', '12537576:15231738')`      |              1 | [SO:0001162](https://bioregistry.io/SO:0001162)                                                                                                                                                                                                     |
| `PMID:('PMID', '15388847,PMID:16524884')` |              1 | [SO:0002235](https://bioregistry.io/SO:0002235)                                                                                                                                                                                                     |
| `PMID:('PMID', ' 19407924')`              |              1 | [SO:0002293](https://bioregistry.io/SO:0002293)                                                                                                                                                                                                     |
| `PMID:('PMID', ' 16236432')`              |              1 | [SO:0002350](https://bioregistry.io/SO:0002350)                                                                                                                                                                                                     |
| `PMID:('PMID', ' 17608616')`              |              1 | [SO:0002350](https://bioregistry.io/SO:0002350)                                                                                                                                                                                                     |

## `PomBase`: PomBase

Overall, there were 12 invalid
xrefs to external prefixed with `PomBase` (standardized to Bioregistry
prefix [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref                |   usages_count | usages                                                                                                                                                                                                                                                   |
|------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PomBase:('PomBase', 'mah')` |              6 | [SO:0001808](https://bioregistry.io/SO:0001808), [SO:0001811](https://bioregistry.io/SO:0001811), [SO:0001812](https://bioregistry.io/SO:0001812), [SO:0001813](https://bioregistry.io/SO:0001813), [SO:0001905](https://bioregistry.io/SO:0001905), ... |
| `PomBase:('PomBase', 'al')`  |              3 | [SO:0000370](https://bioregistry.io/SO:0000370), [SO:0002022](https://bioregistry.io/SO:0002022), [SO:0002207](https://bioregistry.io/SO:0002207)                                                                                                        |
| `PomBase:('PomBase', 'vw')`  |              2 | [SO:0002025](https://bioregistry.io/SO:0002025), [SO:0002215](https://bioregistry.io/SO:0002215)                                                                                                                                                         |
| `PomBase:('PomBase', 'mh')`  |              1 | [SO:0002208](https://bioregistry.io/SO:0002208)                                                                                                                                                                                                          |

## `POMBASE`: PomBase

Overall, there were 3 invalid
xrefs to external prefixed with `POMBASE` (standardized to Bioregistry
prefix [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref                |   usages_count | usages                                                                                           |
|------------------------------|----------------|--------------------------------------------------------------------------------------------------|
| `POMBASE:('POMBASE', 'mah')` |              2 | [SO:0002027](https://bioregistry.io/SO:0002027), [SO:0002028](https://bioregistry.io/SO:0002028) |
| `POMBASE:('POMBASE', 'vw')`  |              1 | [SO:0002029](https://bioregistry.io/SO:0002029)                                                  |

## `RFAM`: Rfam database of RNA families

Overall, there were 2 invalid
xrefs to external prefixed with `RFAM` (standardized to Bioregistry
prefix [`rfam`](https://bioregistry.io/rfam)) that
did not match the standard pattern `^RF\d{5}$`.

| external_xref         |   usages_count | usages                                                                                           |
|-----------------------|----------------|--------------------------------------------------------------------------------------------------|
| `RFAM:('RFAM', 'jd')` |              2 | [SO:0001427](https://bioregistry.io/SO:0001427), [SO:0001459](https://bioregistry.io/SO:0001459) |

## `SGD`: Saccharomyces Genome Database

Overall, there were 12 invalid
xrefs to external prefixed with `SGD` (standardized to Bioregistry
prefix [`sgd`](https://bioregistry.io/sgd)) that
did not match the standard pattern `^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`.

| external_xref       |   usages_count | usages                                                                                                                                                                                                                                                   |
|---------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:('SGD', 'jd')` |              6 | [SO:0002001](https://bioregistry.io/SO:0002001), [SO:0002002](https://bioregistry.io/SO:0002002), [SO:0002003](https://bioregistry.io/SO:0002003), [SO:0002004](https://bioregistry.io/SO:0002004), [SO:0002024](https://bioregistry.io/SO:0002024), ... |
| `SGD:('SGD', 'rb')` |              3 | [SO:0000236](https://bioregistry.io/SO:0000236), [SO:0000717](https://bioregistry.io/SO:0000717), [SO:0000718](https://bioregistry.io/SO:0000718)                                                                                                        |
| `SGD:('SGD', 'se')` |              3 | [SO:0002048](https://bioregistry.io/SO:0002048), [SO:0002059](https://bioregistry.io/SO:0002059), [SO:0005853](https://bioregistry.io/SO:0005853)                                                                                                        |

## `SO`: Sequence types and features ontology

Overall, there were 1,224 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                  |   usages_count | usages                                                                                                                                                                                                                                                   |
|--------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SO:('SO', 'ke')`              |            885 | [SO:0000001](https://bioregistry.io/SO:0000001), [SO:0000002](https://bioregistry.io/SO:0000002), [SO:0000006](https://bioregistry.io/SO:0000006), [SO:0000013](https://bioregistry.io/SO:0000013), [SO:0000020](https://bioregistry.io/SO:0000020), ... |
| `SO:('SO', 'xp')`              |            109 | [SO:0000078](https://bioregistry.io/SO:0000078), [SO:0000087](https://bioregistry.io/SO:0000087), [SO:0000088](https://bioregistry.io/SO:0000088), [SO:0000089](https://bioregistry.io/SO:0000089), [SO:0000090](https://bioregistry.io/SO:0000090), ... |
| `SO:('SO', 'ma')`              |             76 | [SO:0000036](https://bioregistry.io/SO:0000036), [SO:0000037](https://bioregistry.io/SO:0000037), [SO:0000040](https://bioregistry.io/SO:0000040), [SO:0000042](https://bioregistry.io/SO:0000042), [SO:0000051](https://bioregistry.io/SO:0000051), ... |
| `SO:('SO', 'cb')`              |             41 | [SO:0000059](https://bioregistry.io/SO:0000059), [SO:0000061](https://bioregistry.io/SO:0000061), [SO:0000419](https://bioregistry.io/SO:0000419), [SO:0000694](https://bioregistry.io/SO:0000694), [SO:0000836](https://bioregistry.io/SO:0000836), ... |
| `SO:('SO', 'nlw')`             |             21 | [SO:0000708](https://bioregistry.io/SO:0000708), [SO:0000709](https://bioregistry.io/SO:0000709), [SO:0001464](https://bioregistry.io/SO:0001464), [SO:0001465](https://bioregistry.io/SO:0001465), [SO:0001466](https://bioregistry.io/SO:0001466), ... |
| `SO:('SO', 'as')`              |             14 | [SO:0000140](https://bioregistry.io/SO:0000140), [SO:0000365](https://bioregistry.io/SO:0000365), [SO:0000367](https://bioregistry.io/SO:0000367), [SO:0000942](https://bioregistry.io/SO:0000942), [SO:0000943](https://bioregistry.io/SO:0000943), ... |
| `SO:('SO', 'cjm')`             |             11 | [SO:0000162](https://bioregistry.io/SO:0000162), [SO:0000163](https://bioregistry.io/SO:0000163), [SO:0000164](https://bioregistry.io/SO:0000164), [SO:0000196](https://bioregistry.io/SO:0000196), [SO:0000197](https://bioregistry.io/SO:0000197), ... |
| `SO:('SO', 'immuno_workshop')` |              8 | [SO:0000704](https://bioregistry.io/SO:0000704), [SO:0001023](https://bioregistry.io/SO:0001023), [SO:0001024](https://bioregistry.io/SO:0001024), [SO:0001025](https://bioregistry.io/SO:0001025), [SO:0001026](https://bioregistry.io/SO:0001026), ... |
| `SO:('SO', 'rd')`              |              7 | [SO:0000150](https://bioregistry.io/SO:0000150), [SO:0000307](https://bioregistry.io/SO:0000307), [SO:0000337](https://bioregistry.io/SO:0000337), [SO:0000339](https://bioregistry.io/SO:0000339), [SO:0000468](https://bioregistry.io/SO:0000468), ... |
| `SO:('SO', 'vw')`              |              7 | [SO:0001794](https://bioregistry.io/SO:0001794), [SO:0001795](https://bioregistry.io/SO:0001795), [SO:0001796](https://bioregistry.io/SO:0001796), [SO:0001798](https://bioregistry.io/SO:0001798), [SO:0001799](https://bioregistry.io/SO:0001799), ... |
| `SO:('SO', 'bm')`              |              6 | [SO:0001218](https://bioregistry.io/SO:0001218), [SO:0001483](https://bioregistry.io/SO:0001483), [SO:0001745](https://bioregistry.io/SO:0001745), [SO:0001746](https://bioregistry.io/SO:0001746), [SO:0001902](https://bioregistry.io/SO:0001902), ... |
| `SO:('SO', 'ls')`              |              4 | [SO:0000007](https://bioregistry.io/SO:0000007), [SO:0000148](https://bioregistry.io/SO:0000148), [SO:0000149](https://bioregistry.io/SO:0000149), [SO:0000688](https://bioregistry.io/SO:0000688)                                                       |
| `SO:('SO', 'regcreative')`     |              4 | [SO:0000167](https://bioregistry.io/SO:0000167), [SO:0000627](https://bioregistry.io/SO:0000627), [SO:0001055](https://bioregistry.io/SO:0001055), [SO:0001058](https://bioregistry.io/SO:0001058)                                                       |
| `SO:('SO', 'ml')`              |              4 | [SO:0001668](https://bioregistry.io/SO:0001668), [SO:0001980](https://bioregistry.io/SO:0001980), [SO:0001981](https://bioregistry.io/SO:0001981), [SO:0001982](https://bioregistry.io/SO:0001982)                                                       |
| `SO:('SO', 'ds')`              |              4 | [SO:0002329](https://bioregistry.io/SO:0002329), [SO:0002330](https://bioregistry.io/SO:0002330), [SO:0002331](https://bioregistry.io/SO:0002331), [SO:0002332](https://bioregistry.io/SO:0002332)                                                       |
| `SO:('SO', 'andrewgibson')`    |              3 | [SO:0001915](https://bioregistry.io/SO:0001915), [SO:0001916](https://bioregistry.io/SO:0001916), [SO:0001917](https://bioregistry.io/SO:0001917)                                                                                                        |
| `SO:('SO', 'rtapella')`        |              3 | [SO:0001918](https://bioregistry.io/SO:0001918), [SO:0001919](https://bioregistry.io/SO:0001919), [SO:0001920](https://bioregistry.io/SO:0001920)                                                                                                        |
| `SO:('SO', 'jk')`              |              2 | [SO:0000931](https://bioregistry.io/SO:0000931), [SO:0000978](https://bioregistry.io/SO:0000978)                                                                                                                                                         |
| `SO:('SO', 'chado')`           |              2 | [SO:0001416](https://bioregistry.io/SO:0001416), [SO:0001417](https://bioregistry.io/SO:0001417)                                                                                                                                                         |
| `SO:('SO', 'jh')`              |              1 | [SO:0000552](https://bioregistry.io/SO:0000552)                                                                                                                                                                                                          |
| `SO:('SO', 'SG')`              |              1 | [SO:0000727](https://bioregistry.io/SO:0000727)                                                                                                                                                                                                          |
| `SO:('SO', 'GAR')`             |              1 | [SO:0000839](https://bioregistry.io/SO:0000839)                                                                                                                                                                                                          |
| `SO:('SO', 'jestill')`         |              1 | [SO:0001642](https://bioregistry.io/SO:0001642)                                                                                                                                                                                                          |
| `SO:('SO', 'db')`              |              1 | [SO:0001645](https://bioregistry.io/SO:0001645)                                                                                                                                                                                                          |
| `SO:('SO', 'AF')`              |              1 | [SO:0001658](https://bioregistry.io/SO:0001658)                                                                                                                                                                                                          |
| `SO:('SO', 'KE')`              |              1 | [SO:0001731](https://bioregistry.io/SO:0001731)                                                                                                                                                                                                          |
| `SO:('SO', 'mc')`              |              1 | [SO:0001740](https://bioregistry.io/SO:0001740)                                                                                                                                                                                                          |
| `SO:('SO', 'hd')`              |              1 | [SO:0001741](https://bioregistry.io/SO:0001741)                                                                                                                                                                                                          |
| `SO:('SO', 'BM')`              |              1 | [SO:0001744](https://bioregistry.io/SO:0001744)                                                                                                                                                                                                          |
| `SO:('SO', 'myl')`             |              1 | [SO:0001959](https://bioregistry.io/SO:0001959)                                                                                                                                                                                                          |
| `SO:('SO', 'rs')`              |              1 | [SO:0002049](https://bioregistry.io/SO:0002049)                                                                                                                                                                                                          |
| `SO:('SO', 'nrs')`             |              1 | [SO:0002095](https://bioregistry.io/SO:0002095)                                                                                                                                                                                                          |

## `UniProt`: UniProt Protein

Overall, there were 21 invalid
xrefs to external prefixed with `UniProt` (standardized to Bioregistry
prefix [`uniprot`](https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref                            |   usages_count | usages                                                                                                                                                                                                                                                   |
|------------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UniProt:('UniProt', 'curation_manual')` |             19 | [SO:0001064](https://bioregistry.io/SO:0001064), [SO:0001066](https://bioregistry.io/SO:0001066), [SO:0001067](https://bioregistry.io/SO:0001067), [SO:0001080](https://bioregistry.io/SO:0001080), [SO:0001083](https://bioregistry.io/SO:0001083), ... |
| `UniProt:('UniProt', 'curator_manual')`  |              1 | [SO:0001077](https://bioregistry.io/SO:0001077)                                                                                                                                                                                                          |
| `UniProt:('UniProt', 'Curation_manual')` |              1 | [SO:0001093](https://bioregistry.io/SO:0001093)                                                                                                                                                                                                          |

## `uniprot`: UniProt Protein

Overall, there were 31 invalid
xrefs to external prefixed with `uniprot` (standardized to Bioregistry
prefix [`uniprot`](https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref                         |   usages_count | usages                                                                                                                                                                                                                                                   |
|---------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uniprot:('uniprot', 'feature_type')` |             28 | [SO:0000417](https://bioregistry.io/SO:0000417), [SO:0000418](https://bioregistry.io/SO:0000418), [SO:0000419](https://bioregistry.io/SO:0000419), [SO:0000691](https://bioregistry.io/SO:0000691), [SO:0000725](https://bioregistry.io/SO:0000725), ... |
| `uniprot:('uniprot', 'feature')`      |              2 | [SO:0001655](https://bioregistry.io/SO:0001655), [SO:0100020](https://bioregistry.io/SO:0100020)                                                                                                                                                         |
| `uniprot:('uniprot', 'curation')`     |              1 | [SO:0001091](https://bioregistry.io/SO:0001091)                                                                                                                                                                                                          |

## `WB`: WormBase database of nematode biology

Overall, there were 1 invalid
xrefs to external prefixed with `WB` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref      |   usages_count | usages                                          |
|--------------------|----------------|-------------------------------------------------|
| `WB:('WB', 'ems')` |              1 | [SO:0000274](https://bioregistry.io/SO:0000274) |

## `xenbase`: Xenbase

Overall, there were 5 invalid
xrefs to external prefixed with `xenbase` (standardized to Bioregistry
prefix [`xenbase`](https://bioregistry.io/xenbase)) that
did not match the standard pattern `^XB\-\w+\-\d+$`.

| external_xref               |   usages_count | usages                                                                                                                                                                                                                                              |
|-----------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `xenbase:('xenbase', 'jb')` |              5 | [SO:0001203](https://bioregistry.io/SO:0001203), [SO:0001204](https://bioregistry.io/SO:0001204), [SO:0001205](https://bioregistry.io/SO:0001205), [SO:0001206](https://bioregistry.io/SO:0001206), [SO:0001207](https://bioregistry.io/SO:0001207) |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 6 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref         |   usages_count | usages                                                                                                                                            |
|-----------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:('ZFIN', 'dh')` |              3 | [SO:0001477](https://bioregistry.io/SO:0001477), [SO:0001478](https://bioregistry.io/SO:0001478), [SO:0001479](https://bioregistry.io/SO:0001479) |
| `ZFIN:('ZFIN', 'mh')` |              2 | [SO:0001480](https://bioregistry.io/SO:0001480), [SO:0001481](https://bioregistry.io/SO:0001481)                                                  |
| `ZFIN:('ZFIN', 'st')` |              1 | [SO:0002217](https://bioregistry.io/SO:0002217)                                                                                                   |

