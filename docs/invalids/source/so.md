# so

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `so`. See the [GitHub repository](https://github.com/The-Sequence-Ontology/SO-Ontologies)


## `BioRXiv`: bioRxiv

- Normalized prefix: `biorxiv`
- [https://bioregistry.io/biorxiv](https://bioregistry.io/biorxiv)
- Pattern:`^(\d{4}\.\d{2}\.\d{2}\.)?\d{6,8}(v\d{1,3})?$`

| identifier                               |   appearances | examples                                        |
|------------------------------------------|---------------|-------------------------------------------------|
| `BioRXiv:https://doi.org/10.1101/584664` |             1 | [SO:0002223](https://bioregistry.io/SO:0002223) |

## `FB`: FlyBase Gene

- Normalized prefix: `flybase`
- [https://bioregistry.io/flybase](https://bioregistry.io/flybase)
- Pattern:`^FB\w{2}\d{7}$`

| identifier            |   appearances | examples                                                                                                                                                                                                                                                 |
|-----------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FB:reference_manual` |            24 | [SO:1000144](https://bioregistry.io/SO:1000144), [SO:1000159](https://bioregistry.io/SO:1000159), [SO:1000160](https://bioregistry.io/SO:1000160), [SO:1000160](https://bioregistry.io/SO:1000160), [SO:1000171](https://bioregistry.io/SO:1000171), ... |
| `FB:km`               |             6 | [SO:0000461](https://bioregistry.io/SO:0000461), [SO:0000461](https://bioregistry.io/SO:0000461), [SO:0000512](https://bioregistry.io/SO:0000512), [SO:0000549](https://bioregistry.io/SO:0000549), [SO:0000567](https://bioregistry.io/SO:0000567), ... |
| `FB:mc`               |             4 | [SO:0000796](https://bioregistry.io/SO:0000796), [SO:0000797](https://bioregistry.io/SO:0000797), [SO:0000798](https://bioregistry.io/SO:0000798), [SO:0000799](https://bioregistry.io/SO:0000799)                                                       |
| `FB:gm`               |             4 | [SO:0000800](https://bioregistry.io/SO:0000800), [SO:0000801](https://bioregistry.io/SO:0000801), [SO:0000802](https://bioregistry.io/SO:0000802), [SO:0000803](https://bioregistry.io/SO:0000803)                                                       |
| `FB:manual`           |             2 | [SO:1000142](https://bioregistry.io/SO:1000142), [SO:1000143](https://bioregistry.io/SO:1000143)                                                                                                                                                         |
| `FB:WG`               |             1 | [SO:0000719](https://bioregistry.io/SO:0000719)                                                                                                                                                                                                          |
| `FB:cds`              |             1 | [SO:0000934](https://bioregistry.io/SO:0000934)                                                                                                                                                                                                          |

## `GO`: Gene Ontology

- Normalized prefix: `go`
- [https://bioregistry.io/go](https://bioregistry.io/go)
- Pattern:`^\d{7}$`

| identifier   |   appearances | examples                                                                                                                                          |
|--------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:mah`     |             3 | [SO:0001861](https://bioregistry.io/SO:0001861), [SO:0001861](https://bioregistry.io/SO:0001861), [SO:0001871](https://bioregistry.io/SO:0001871) |

## `HGNC`: HUGO Gene Nomenclature Committee

- Normalized prefix: `hgnc`
- [https://bioregistry.io/hgnc](https://bioregistry.io/hgnc)
- Pattern:`^((HGNC|hgnc):)?\d{1,5}$`

| identifier   |   appearances | examples                                        |
|--------------|---------------|-------------------------------------------------|
| `HGNC:mw`    |             1 | [SO:0001877](https://bioregistry.io/SO:0001877) |

## `MGD`: Mouse Genome Informatics

- Normalized prefix: `mgi`
- [https://bioregistry.io/mgi](https://bioregistry.io/mgi)
- Pattern:`^\d+$`

| identifier   |   appearances | examples                                        |
|--------------|---------------|-------------------------------------------------|
| `MGD:tm`     |             1 | [SO:0001644](https://bioregistry.io/SO:0001644) |

## `MGI`: Mouse Genome Informatics

- Normalized prefix: `mgi`
- [https://bioregistry.io/mgi](https://bioregistry.io/mgi)
- Pattern:`^\d+$`

| identifier   |   appearances | examples                                        |
|--------------|---------------|-------------------------------------------------|
| `MGI:hdeen`  |             1 | [SO:0001503](https://bioregistry.io/SO:0001503) |

## `PMC`: Pubmed Central

- Normalized prefix: `pmc`
- [https://bioregistry.io/pmc](https://bioregistry.io/pmc)
- Pattern:`^PMC\d+$`

| identifier   |   appearances | examples                                        |
|--------------|---------------|-------------------------------------------------|
| `PMC:126017` |             1 | [SO:0002095](https://bioregistry.io/SO:0002095) |

## `PMID`: PubMed

- Normalized prefix: `pubmed`
- [https://bioregistry.io/pubmed](https://bioregistry.io/pubmed)
- Pattern:`^\d+$`

| identifier                    |   appearances | examples                                                                                                                                                                                                                                            |
|-------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PMID: 24572720`              |             5 | [SO:0002344](https://bioregistry.io/SO:0002344), [SO:0002345](https://bioregistry.io/SO:0002345), [SO:0002346](https://bioregistry.io/SO:0002346), [SO:0002347](https://bioregistry.io/SO:0002347), [SO:0002348](https://bioregistry.io/SO:0002348) |
| `PMID:12537576:16827941`      |             4 | [SO:0001158](https://bioregistry.io/SO:0001158), [SO:0001159](https://bioregistry.io/SO:0001159), [SO:0001160](https://bioregistry.io/SO:0001160), [SO:0001161](https://bioregistry.io/SO:0001161)                                                  |
| `PMID: 118436`                |             2 | [SO:0002336](https://bioregistry.io/SO:0002336), [SO:0002337](https://bioregistry.io/SO:0002337)                                                                                                                                                    |
| `PMID: 29474379`              |             2 | [SO:0002336](https://bioregistry.io/SO:0002336), [SO:0002337](https://bioregistry.io/SO:0002337)                                                                                                                                                    |
| `PMID: 3136294`               |             2 | [SO:0002336](https://bioregistry.io/SO:0002336), [SO:0002337](https://bioregistry.io/SO:0002337)                                                                                                                                                    |
| `PMID:=12409455`              |             1 | [SO:0000394](https://bioregistry.io/SO:0000394)                                                                                                                                                                                                     |
| `PMID:16827941:12537576`      |             1 | [SO:0001157](https://bioregistry.io/SO:0001157)                                                                                                                                                                                                     |
| `PMID:12537576:15231738`      |             1 | [SO:0001162](https://bioregistry.io/SO:0001162)                                                                                                                                                                                                     |
| `PMID:15388847,PMID:16524884` |             1 | [SO:0002235](https://bioregistry.io/SO:0002235)                                                                                                                                                                                                     |
| `PMID: 19407924`              |             1 | [SO:0002293](https://bioregistry.io/SO:0002293)                                                                                                                                                                                                     |
| `PMID: 16236432`              |             1 | [SO:0002350](https://bioregistry.io/SO:0002350)                                                                                                                                                                                                     |
| `PMID: 17608616`              |             1 | [SO:0002350](https://bioregistry.io/SO:0002350)                                                                                                                                                                                                     |

## `PomBase`: PomBase

- Normalized prefix: `pombase`
- [https://bioregistry.io/pombase](https://bioregistry.io/pombase)
- Pattern:`^S\w+(\.)?\w+(\.)?$`

| identifier    |   appearances | examples                                                                                                                                                                                                                                                 |
|---------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PomBase:mah` |             6 | [SO:0001811](https://bioregistry.io/SO:0001811), [SO:0001813](https://bioregistry.io/SO:0001813), [SO:0001813](https://bioregistry.io/SO:0001813), [SO:0001813](https://bioregistry.io/SO:0001813), [SO:0001984](https://bioregistry.io/SO:0001984), ... |
| `PomBase:al`  |             3 | [SO:0000370](https://bioregistry.io/SO:0000370), [SO:0002022](https://bioregistry.io/SO:0002022), [SO:0002207](https://bioregistry.io/SO:0002207)                                                                                                        |
| `PomBase:vw`  |             2 | [SO:0002025](https://bioregistry.io/SO:0002025), [SO:0002215](https://bioregistry.io/SO:0002215)                                                                                                                                                         |
| `PomBase:mh`  |             1 | [SO:0002208](https://bioregistry.io/SO:0002208)                                                                                                                                                                                                          |

## `POMBASE`: PomBase

- Normalized prefix: `pombase`
- [https://bioregistry.io/pombase](https://bioregistry.io/pombase)
- Pattern:`^S\w+(\.)?\w+(\.)?$`

| identifier    |   appearances | examples                                                                                         |
|---------------|---------------|--------------------------------------------------------------------------------------------------|
| `POMBASE:mah` |             2 | [SO:0002027](https://bioregistry.io/SO:0002027), [SO:0002028](https://bioregistry.io/SO:0002028) |
| `POMBASE:vw`  |             1 | [SO:0002029](https://bioregistry.io/SO:0002029)                                                  |

## `RFAM`: Rfam database of RNA families

- Normalized prefix: `rfam`
- [https://bioregistry.io/rfam](https://bioregistry.io/rfam)
- Pattern:`^RF\d{5}$`

| identifier   |   appearances | examples                                                                                         |
|--------------|---------------|--------------------------------------------------------------------------------------------------|
| `RFAM:jd`    |             2 | [SO:0001427](https://bioregistry.io/SO:0001427), [SO:0001459](https://bioregistry.io/SO:0001459) |

## `SGD`: Saccharomyces Genome Database

- Normalized prefix: `sgd`
- [https://bioregistry.io/sgd](https://bioregistry.io/sgd)
- Pattern:`^((S\d+$)|(Y[A-Z]{2}\d{3}[a-zA-Z](\-[A-Z])?))$`

| identifier   |   appearances | examples                                                                                                                                                                                                                                                 |
|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SGD:jd`     |             6 | [SO:0002002](https://bioregistry.io/SO:0002002), [SO:0002002](https://bioregistry.io/SO:0002002), [SO:0002003](https://bioregistry.io/SO:0002003), [SO:0002004](https://bioregistry.io/SO:0002004), [SO:0002030](https://bioregistry.io/SO:0002030), ... |
| `SGD:rb`     |             3 | [SO:0000236](https://bioregistry.io/SO:0000236), [SO:0000717](https://bioregistry.io/SO:0000717), [SO:0000718](https://bioregistry.io/SO:0000718)                                                                                                        |
| `SGD:se`     |             3 | [SO:0002048](https://bioregistry.io/SO:0002048), [SO:0002059](https://bioregistry.io/SO:0002059), [SO:0005853](https://bioregistry.io/SO:0005853)                                                                                                        |

## `SO`: Sequence types and features ontology

- Normalized prefix: `so`
- [https://bioregistry.io/so](https://bioregistry.io/so)
- Pattern:`^\d{7}$`

| identifier           |   appearances | examples                                                                                                                                                                                                                                                 |
|----------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SO:ke`              |           885 | [SO:0000267](https://bioregistry.io/SO:0000267), [SO:0001474](https://bioregistry.io/SO:0001474), [SO:0001641](https://bioregistry.io/SO:0001641), [SO:0002050](https://bioregistry.io/SO:0002050), [SO:1000132](https://bioregistry.io/SO:1000132), ... |
| `SO:xp`              |           109 | [SO:0000637](https://bioregistry.io/SO:0000637), [SO:0000711](https://bioregistry.io/SO:0000711), [SO:0000808](https://bioregistry.io/SO:0000808), [SO:0000872](https://bioregistry.io/SO:0000872), [SO:0000902](https://bioregistry.io/SO:0000902), ... |
| `SO:ma`              |            76 | [SO:0000157](https://bioregistry.io/SO:0000157), [SO:0000671](https://bioregistry.io/SO:0000671), [SO:0000930](https://bioregistry.io/SO:0000930), [SO:0000954](https://bioregistry.io/SO:0000954), [SO:0000960](https://bioregistry.io/SO:0000960), ... |
| `SO:cb`              |            41 | [SO:0000851](https://bioregistry.io/SO:0000851), [SO:0001151](https://bioregistry.io/SO:0001151), [SO:0001409](https://bioregistry.io/SO:0001409), [SO:0001410](https://bioregistry.io/SO:0001410), [SO:0001411](https://bioregistry.io/SO:0001411), ... |
| `SO:nlw`             |            21 | [SO:0000708](https://bioregistry.io/SO:0000708), [SO:0001471](https://bioregistry.io/SO:0001471), [SO:0001471](https://bioregistry.io/SO:0001471), [SO:0001751](https://bioregistry.io/SO:0001751), [SO:0001755](https://bioregistry.io/SO:0001755), ... |
| `SO:as`              |            14 | [SO:0000944](https://bioregistry.io/SO:0000944), [SO:0000945](https://bioregistry.io/SO:0000945), [SO:0000949](https://bioregistry.io/SO:0000949), [SO:0000953](https://bioregistry.io/SO:0000953), [SO:0000953](https://bioregistry.io/SO:0000953), ... |
| `SO:cjm`             |            11 | [SO:0000162](https://bioregistry.io/SO:0000162), [SO:0000163](https://bioregistry.io/SO:0000163), [SO:0000241](https://bioregistry.io/SO:0000241), [SO:0000462](https://bioregistry.io/SO:0000462), [SO:0000605](https://bioregistry.io/SO:0000605), ... |
| `SO:immuno_workshop` |             8 | [SO:0000704](https://bioregistry.io/SO:0000704), [SO:0000704](https://bioregistry.io/SO:0000704), [SO:0001026](https://bioregistry.io/SO:0001026), [SO:0001026](https://bioregistry.io/SO:0001026), [SO:0001027](https://bioregistry.io/SO:0001027), ... |
| `SO:rd`              |             7 | [SO:0000150](https://bioregistry.io/SO:0000150), [SO:0000307](https://bioregistry.io/SO:0000307), [SO:0000307](https://bioregistry.io/SO:0000307), [SO:0000337](https://bioregistry.io/SO:0000337), [SO:0000339](https://bioregistry.io/SO:0000339), ... |
| `SO:vw`              |             7 | [SO:0001794](https://bioregistry.io/SO:0001794), [SO:0001796](https://bioregistry.io/SO:0001796), [SO:0001796](https://bioregistry.io/SO:0001796), [SO:0001799](https://bioregistry.io/SO:0001799), [SO:0001899](https://bioregistry.io/SO:0001899), ... |
| `SO:bm`              |             6 | [SO:0001483](https://bioregistry.io/SO:0001483), [SO:0001745](https://bioregistry.io/SO:0001745), [SO:0001746](https://bioregistry.io/SO:0001746), [SO:0001902](https://bioregistry.io/SO:0001902), [SO:0001928](https://bioregistry.io/SO:0001928), ... |
| `SO:ls`              |             4 | [SO:0000007](https://bioregistry.io/SO:0000007), [SO:0000148](https://bioregistry.io/SO:0000148), [SO:0000149](https://bioregistry.io/SO:0000149), [SO:0000688](https://bioregistry.io/SO:0000688)                                                       |
| `SO:regcreative`     |             4 | [SO:0000167](https://bioregistry.io/SO:0000167), [SO:0000627](https://bioregistry.io/SO:0000627), [SO:0001055](https://bioregistry.io/SO:0001055), [SO:0001058](https://bioregistry.io/SO:0001058)                                                       |
| `SO:ml`              |             4 | [SO:0001668](https://bioregistry.io/SO:0001668), [SO:0001980](https://bioregistry.io/SO:0001980), [SO:0001981](https://bioregistry.io/SO:0001981), [SO:0001982](https://bioregistry.io/SO:0001982)                                                       |
| `SO:ds`              |             4 | [SO:0002329](https://bioregistry.io/SO:0002329), [SO:0002330](https://bioregistry.io/SO:0002330), [SO:0002331](https://bioregistry.io/SO:0002331), [SO:0002332](https://bioregistry.io/SO:0002332)                                                       |
| `SO:andrewgibson`    |             3 | [SO:0001915](https://bioregistry.io/SO:0001915), [SO:0001916](https://bioregistry.io/SO:0001916), [SO:0001917](https://bioregistry.io/SO:0001917)                                                                                                        |
| `SO:rtapella`        |             3 | [SO:0001918](https://bioregistry.io/SO:0001918), [SO:0001919](https://bioregistry.io/SO:0001919), [SO:0001920](https://bioregistry.io/SO:0001920)                                                                                                        |
| `SO:jk`              |             2 | [SO:0000931](https://bioregistry.io/SO:0000931), [SO:0000978](https://bioregistry.io/SO:0000978)                                                                                                                                                         |
| `SO:chado`           |             2 | [SO:0001416](https://bioregistry.io/SO:0001416), [SO:0001417](https://bioregistry.io/SO:0001417)                                                                                                                                                         |
| `SO:jh`              |             1 | [SO:0000552](https://bioregistry.io/SO:0000552)                                                                                                                                                                                                          |
| `SO:SG`              |             1 | [SO:0000727](https://bioregistry.io/SO:0000727)                                                                                                                                                                                                          |
| `SO:GAR`             |             1 | [SO:0000839](https://bioregistry.io/SO:0000839)                                                                                                                                                                                                          |
| `SO:jestill`         |             1 | [SO:0001642](https://bioregistry.io/SO:0001642)                                                                                                                                                                                                          |
| `SO:db`              |             1 | [SO:0001645](https://bioregistry.io/SO:0001645)                                                                                                                                                                                                          |
| `SO:AF`              |             1 | [SO:0001658](https://bioregistry.io/SO:0001658)                                                                                                                                                                                                          |
| `SO:KE`              |             1 | [SO:0001731](https://bioregistry.io/SO:0001731)                                                                                                                                                                                                          |
| `SO:mc`              |             1 | [SO:0001740](https://bioregistry.io/SO:0001740)                                                                                                                                                                                                          |
| `SO:hd`              |             1 | [SO:0001741](https://bioregistry.io/SO:0001741)                                                                                                                                                                                                          |
| `SO:BM`              |             1 | [SO:0001744](https://bioregistry.io/SO:0001744)                                                                                                                                                                                                          |
| `SO:myl`             |             1 | [SO:0001959](https://bioregistry.io/SO:0001959)                                                                                                                                                                                                          |
| `SO:rs`              |             1 | [SO:0002049](https://bioregistry.io/SO:0002049)                                                                                                                                                                                                          |
| `SO:nrs`             |             1 | [SO:0002095](https://bioregistry.io/SO:0002095)                                                                                                                                                                                                          |

## `UniProt`: UniProt Protein

- Normalized prefix: `uniprot`
- [https://bioregistry.io/uniprot](https://bioregistry.io/uniprot)
- Pattern:`^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`

| identifier                |   appearances | examples                                                                                                                                                                                                                                                 |
|---------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UniProt:curation_manual` |            19 | [SO:0001083](https://bioregistry.io/SO:0001083), [SO:0001085](https://bioregistry.io/SO:0001085), [SO:0001085](https://bioregistry.io/SO:0001085), [SO:0001088](https://bioregistry.io/SO:0001088), [SO:0001113](https://bioregistry.io/SO:0001113), ... |
| `UniProt:curator_manual`  |             1 | [SO:0001077](https://bioregistry.io/SO:0001077)                                                                                                                                                                                                          |
| `UniProt:Curation_manual` |             1 | [SO:0001093](https://bioregistry.io/SO:0001093)                                                                                                                                                                                                          |

## `uniprot`: UniProt Protein

- Normalized prefix: `uniprot`
- [https://bioregistry.io/uniprot](https://bioregistry.io/uniprot)
- Pattern:`^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`

| identifier             |   appearances | examples                                                                                                                                                                                                                                                 |
|------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uniprot:feature_type` |            28 | [SO:0000725](https://bioregistry.io/SO:0000725), [SO:0001066](https://bioregistry.io/SO:0001066), [SO:0001067](https://bioregistry.io/SO:0001067), [SO:0001077](https://bioregistry.io/SO:0001077), [SO:0001083](https://bioregistry.io/SO:0001083), ... |
| `uniprot:feature`      |             2 | [SO:0001655](https://bioregistry.io/SO:0001655), [SO:0100020](https://bioregistry.io/SO:0100020)                                                                                                                                                         |
| `uniprot:curation`     |             1 | [SO:0001091](https://bioregistry.io/SO:0001091)                                                                                                                                                                                                          |

## `WB`: WormBase database of nematode biology

- Normalized prefix: `wormbase`
- [https://bioregistry.io/wormbase](https://bioregistry.io/wormbase)
- Pattern:`^WB[A-Z][a-z]+\d+$`

| identifier   |   appearances | examples                                        |
|--------------|---------------|-------------------------------------------------|
| `WB:ems`     |             1 | [SO:0000274](https://bioregistry.io/SO:0000274) |

## `xenbase`: Xenbase

- Normalized prefix: `xenbase`
- [https://bioregistry.io/xenbase](https://bioregistry.io/xenbase)
- Pattern:`^XB\-\w+\-\d+$`

| identifier   |   appearances | examples                                                                                                                                                                                                                                            |
|--------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `xenbase:jb` |             5 | [SO:0001203](https://bioregistry.io/SO:0001203), [SO:0001204](https://bioregistry.io/SO:0001204), [SO:0001205](https://bioregistry.io/SO:0001205), [SO:0001206](https://bioregistry.io/SO:0001206), [SO:0001207](https://bioregistry.io/SO:0001207) |

## `ZFIN`: Zebrafish Information Network Gene

- Normalized prefix: `zfin`
- [https://bioregistry.io/zfin](https://bioregistry.io/zfin)
- Pattern:`^ZDB\-\w+\-\d+\-\d+$`

| identifier   |   appearances | examples                                                                                                                                          |
|--------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:dh`    |             3 | [SO:0001477](https://bioregistry.io/SO:0001477), [SO:0001478](https://bioregistry.io/SO:0001478), [SO:0001479](https://bioregistry.io/SO:0001479) |
| `ZFIN:mh`    |             2 | [SO:0001480](https://bioregistry.io/SO:0001480), [SO:0001481](https://bioregistry.io/SO:0001481)                                                  |
| `ZFIN:st`    |             1 | [SO:0002217](https://bioregistry.io/SO:0002217)                                                                                                   |

