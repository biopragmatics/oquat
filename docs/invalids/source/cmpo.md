# cmpo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `cmpo`.


## `EC`: Enzyme Nomenclature

Overall, there were 2 invalid
xrefs to external prefixed with `EC` (standardized to Bioregistry
prefix [`eccode`](https://bioregistry.io/eccode)) that
did not match the standard pattern `^\d{1,2}(\.\d{0,3}){0,3}$`.

| external_xref          |   usages_count | usages                                                  |
|------------------------|----------------|---------------------------------------------------------|
| `EC:('EC', '2.7.7.-')` |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720) |
| `EC:('EC', '3.1.-.-')` |              1 | [GO:0004518](http://purl.obolibrary.org/obo/GO_0004518) |

## `GO`: Gene Ontology

Overall, there were 4 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref     |   usages_count | usages                                                                                                                                                                                                                             |
|-------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:('GO', 'jl')` |              4 | [GO:0044092](http://purl.obolibrary.org/obo/GO_0044092), [GO:0044093](http://purl.obolibrary.org/obo/GO_0044093), [GO:1902679](http://purl.obolibrary.org/obo/GO_1902679), [GO:1902680](http://purl.obolibrary.org/obo/GO_1902680) |

## `OBO_REL`: Relation Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `OBO_REL` (standardized to Bioregistry
prefix [`ro`](https://bioregistry.io/ro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                       |   usages_count | usages                                                      |
|-------------------------------------|----------------|-------------------------------------------------------------|
| `OBO_REL:('OBO_REL', 'part_of')`    |              1 | [BFO:0000050](http://purl.obolibrary.org/obo/BFO_0000050)   |
| `OBO_REL:('OBO_REL', 'has_part')`   |              1 | [PATO:0001555](http://purl.obolibrary.org/obo/PATO_0001555) |
| `OBO_REL:('OBO_REL', 'lacks_part')` |              1 | [PATO:0002000](http://purl.obolibrary.org/obo/PATO_0002000) |

## `PATO`: Phenotype And Trait Ontology

Overall, there were 4 invalid
xrefs to external prefixed with `PATO` (standardized to Bioregistry
prefix [`pato`](https://bioregistry.io/pato)) that
did not match the standard pattern `^\d{7}$`.

| external_xref          |   usages_count | usages                                                                                                                                                                                                                                             |
|------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PATO:('PATO', 'GVG')` |              4 | [PATO:0000911](http://purl.obolibrary.org/obo/PATO_0000911), [PATO:0000912](http://purl.obolibrary.org/obo/PATO_0000912), [PATO:0001562](http://purl.obolibrary.org/obo/PATO_0001562), [PATO:0001563](http://purl.obolibrary.org/obo/PATO_0001563) |

## `PomBase`: PomBase

Overall, there were 1 invalid
xrefs to external prefixed with `PomBase` (standardized to Bioregistry
prefix [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref                |   usages_count | usages                                                                           |
|------------------------------|----------------|----------------------------------------------------------------------------------|
| `PomBase:('PomBase', 'mah')` |              1 | [http://www.ebi.ac.uk/cmpo/CMPO_0000430](http://www.ebi.ac.uk/cmpo/CMPO_0000430) |

## `Reactome`: Reactome

Overall, there were 620 invalid
xrefs to external prefixed with `Reactome` (standardized to Bioregistry
prefix [`reactome`](https://bioregistry.io/reactome)) that
did not match the standard pattern `^R-[A-Z]{3}-\d+(-\d+)?(\.\d+)?$`.

| external_xref                            |   usages_count | usages                                                                                                           |
|------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `Reactome:('Reactome', 'REACT_13696.1')` |              2 | [GO:0007249](http://purl.obolibrary.org/obo/GO_0007249), [GO:0007249](http://purl.obolibrary.org/obo/GO_0007249) |
| `Reactome:('Reactome', '69278')`         |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_101162')`  |              1 | [GO:0000080](http://purl.obolibrary.org/obo/GO_0000080)                                                          |
| `Reactome:('Reactome', 'REACT_1590')`    |              1 | [GO:0000080](http://purl.obolibrary.org/obo/GO_0000080)                                                          |
| `Reactome:('Reactome', 'REACT_29795')`   |              1 | [GO:0000080](http://purl.obolibrary.org/obo/GO_0000080)                                                          |
| `Reactome:('Reactome', 'REACT_34060')`   |              1 | [GO:0000080](http://purl.obolibrary.org/obo/GO_0000080)                                                          |
| `Reactome:('Reactome', 'REACT_78665')`   |              1 | [GO:0000080](http://purl.obolibrary.org/obo/GO_0000080)                                                          |
| `Reactome:('Reactome', 'REACT_78866')`   |              1 | [GO:0000080](http://purl.obolibrary.org/obo/GO_0000080)                                                          |
| `Reactome:('Reactome', 'REACT_83686')`   |              1 | [GO:0000080](http://purl.obolibrary.org/obo/GO_0000080)                                                          |
| `Reactome:('Reactome', 'REACT_91654')`   |              1 | [GO:0000080](http://purl.obolibrary.org/obo/GO_0000080)                                                          |
| `Reactome:('Reactome', 'REACT_93384')`   |              1 | [GO:0000080](http://purl.obolibrary.org/obo/GO_0000080)                                                          |
| `Reactome:('Reactome', 'REACT_93574')`   |              1 | [GO:0000080](http://purl.obolibrary.org/obo/GO_0000080)                                                          |
| `Reactome:('Reactome', 'REACT_105829')`  |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_108550')`  |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_110039')`  |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_28988')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_32013')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_34043')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_78838')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_78845')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_81914')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_82813')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_85811')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_89318')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_899')`     |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_92500')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_92759')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_95174')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_96081')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_97603')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_99645')`   |              1 | [GO:0000084](http://purl.obolibrary.org/obo/GO_0000084)                                                          |
| `Reactome:('Reactome', 'REACT_105223')`  |              1 | [GO:0000085](http://purl.obolibrary.org/obo/GO_0000085)                                                          |
| `Reactome:('Reactome', 'REACT_105307')`  |              1 | [GO:0000085](http://purl.obolibrary.org/obo/GO_0000085)                                                          |
| `Reactome:('Reactome', 'REACT_106415')`  |              1 | [GO:0000085](http://purl.obolibrary.org/obo/GO_0000085)                                                          |
| `Reactome:('Reactome', 'REACT_106836')`  |              1 | [GO:0000085](http://purl.obolibrary.org/obo/GO_0000085)                                                          |
| `Reactome:('Reactome', 'REACT_1915')`    |              1 | [GO:0000085](http://purl.obolibrary.org/obo/GO_0000085)                                                          |
| `Reactome:('Reactome', 'REACT_28975')`   |              1 | [GO:0000085](http://purl.obolibrary.org/obo/GO_0000085)                                                          |
| `Reactome:('Reactome', 'REACT_85928')`   |              1 | [GO:0000085](http://purl.obolibrary.org/obo/GO_0000085)                                                          |
| `Reactome:('Reactome', 'REACT_96332')`   |              1 | [GO:0000085](http://purl.obolibrary.org/obo/GO_0000085)                                                          |
| `Reactome:('Reactome', 'REACT_100942')`  |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_103766')`  |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_107882')`  |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_114616')`  |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_2203')`    |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_28929')`   |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_30388')`   |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_34062')`   |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_77778')`   |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_83880')`   |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_87036')`   |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_87230')`   |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_87807')`   |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_88018')`   |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_88369')`   |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_92702')`   |              1 | [GO:0000086](http://purl.obolibrary.org/obo/GO_0000086)                                                          |
| `Reactome:('Reactome', 'REACT_105412')`  |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_107095')`  |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_109059')`  |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_29488')`   |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_33490')`   |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_82055')`   |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_87132')`   |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_88263')`   |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_910')`     |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_92998')`   |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_93131')`   |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_93566')`   |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_93720')`   |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_94536')`   |              1 | [GO:0000087](http://purl.obolibrary.org/obo/GO_0000087)                                                          |
| `Reactome:('Reactome', 'REACT_100605')`  |              1 | [GO:0000088](http://purl.obolibrary.org/obo/GO_0000088)                                                          |
| `Reactome:('Reactome', 'REACT_102122')`  |              1 | [GO:0000088](http://purl.obolibrary.org/obo/GO_0000088)                                                          |
| `Reactome:('Reactome', 'REACT_105127')`  |              1 | [GO:0000088](http://purl.obolibrary.org/obo/GO_0000088)                                                          |
| `Reactome:('Reactome', 'REACT_106058')`  |              1 | [GO:0000088](http://purl.obolibrary.org/obo/GO_0000088)                                                          |
| `Reactome:('Reactome', 'REACT_28443')`   |              1 | [GO:0000088](http://purl.obolibrary.org/obo/GO_0000088)                                                          |
| `Reactome:('Reactome', 'REACT_28607')`   |              1 | [GO:0000088](http://purl.obolibrary.org/obo/GO_0000088)                                                          |
| `Reactome:('Reactome', 'REACT_32677')`   |              1 | [GO:0000088](http://purl.obolibrary.org/obo/GO_0000088)                                                          |
| `Reactome:('Reactome', 'REACT_765')`     |              1 | [GO:0000088](http://purl.obolibrary.org/obo/GO_0000088)                                                          |
| `Reactome:('Reactome', 'REACT_79474')`   |              1 | [GO:0000088](http://purl.obolibrary.org/obo/GO_0000088)                                                          |
| `Reactome:('Reactome', 'REACT_80300')`   |              1 | [GO:0000088](http://purl.obolibrary.org/obo/GO_0000088)                                                          |
| `Reactome:('Reactome', 'REACT_83888')`   |              1 | [GO:0000088](http://purl.obolibrary.org/obo/GO_0000088)                                                          |
| `Reactome:('Reactome', 'REACT_90347')`   |              1 | [GO:0000088](http://purl.obolibrary.org/obo/GO_0000088)                                                          |
| `Reactome:('Reactome', 'REACT_90481')`   |              1 | [GO:0000088](http://purl.obolibrary.org/obo/GO_0000088)                                                          |
| `Reactome:('Reactome', 'REACT_434')`     |              1 | [GO:0000089](http://purl.obolibrary.org/obo/GO_0000089)                                                          |
| `Reactome:('Reactome', 'REACT_102823')`  |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_104270')`  |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_105082')`  |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_114704')`  |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_118069')`  |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_118526')`  |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_118539')`  |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_31336')`   |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_31385')`   |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_682')`     |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_79351')`   |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_83126')`   |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_98905')`   |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_99376')`   |              1 | [GO:0000236](http://purl.obolibrary.org/obo/GO_0000236)                                                          |
| `Reactome:('Reactome', 'REACT_100451')`  |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_104035')`  |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_104195')`  |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_105856')`  |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_108233')`  |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_152')`     |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_28464')`   |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_28953')`   |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_33388')`   |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_53493')`   |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_79085')`   |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_84794')`   |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_85137')`   |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_85950')`   |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_90332')`   |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_90846')`   |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_96281')`   |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_97744')`   |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_98208')`   |              1 | [GO:0000278](http://purl.obolibrary.org/obo/GO_0000278)                                                          |
| `Reactome:('Reactome', 'REACT_101918')`  |              1 | [GO:0000910](http://purl.obolibrary.org/obo/GO_0000910)                                                          |
| `Reactome:('Reactome', 'REACT_108805')`  |              1 | [GO:0000910](http://purl.obolibrary.org/obo/GO_0000910)                                                          |
| `Reactome:('Reactome', 'REACT_1932')`    |              1 | [GO:0000910](http://purl.obolibrary.org/obo/GO_0000910)                                                          |
| `Reactome:('Reactome', 'REACT_30667')`   |              1 | [GO:0000910](http://purl.obolibrary.org/obo/GO_0000910)                                                          |
| `Reactome:('Reactome', 'REACT_32636')`   |              1 | [GO:0000910](http://purl.obolibrary.org/obo/GO_0000910)                                                          |
| `Reactome:('Reactome', 'REACT_78494')`   |              1 | [GO:0000910](http://purl.obolibrary.org/obo/GO_0000910)                                                          |
| `Reactome:('Reactome', 'REACT_84722')`   |              1 | [GO:0000910](http://purl.obolibrary.org/obo/GO_0000910)                                                          |
| `Reactome:('Reactome', 'REACT_87726')`   |              1 | [GO:0000910](http://purl.obolibrary.org/obo/GO_0000910)                                                          |
| `Reactome:('Reactome', 'REACT_92849')`   |              1 | [GO:0000910](http://purl.obolibrary.org/obo/GO_0000910)                                                          |
| `Reactome:('Reactome', 'REACT_93374')`   |              1 | [GO:0000910](http://purl.obolibrary.org/obo/GO_0000910)                                                          |
| `Reactome:('Reactome', 'REACT_94382')`   |              1 | [GO:0000910](http://purl.obolibrary.org/obo/GO_0000910)                                                          |
| `Reactome:('Reactome', 'REACT_98952')`   |              1 | [GO:0000910](http://purl.obolibrary.org/obo/GO_0000910)                                                          |
| `Reactome:('Reactome', 'REACT_99118')`   |              1 | [GO:0000910](http://purl.obolibrary.org/obo/GO_0000910)                                                          |
| `Reactome:('Reactome', 'REACT_104705')`  |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_106476')`  |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_108407')`  |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_109443')`  |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_113385')`  |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_114466')`  |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_115824')`  |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_116122')`  |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_28249')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_30494')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_30995')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_31549')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_33436')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_77280')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_7985')`    |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_8019')`    |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_80834')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_81691')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_83982')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_85286')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_86666')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_90823')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_93232')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_94534')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_94768')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_95176')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_96912')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_97770')`   |              1 | [GO:0003720](http://purl.obolibrary.org/obo/GO_0003720)                                                          |
| `Reactome:('Reactome', 'REACT_9039')`    |              1 | [GO:0003964](http://purl.obolibrary.org/obo/GO_0003964)                                                          |
| `Reactome:('Reactome', 'REACT_9049')`    |              1 | [GO:0003964](http://purl.obolibrary.org/obo/GO_0003964)                                                          |
| `Reactome:('Reactome', 'REACT_100654')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_101397')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_103600')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_106502')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_108614')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_110731')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_112366')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_1124')`    |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_112509')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_112615')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_112782')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_113127')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_113480')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_113819')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_114931')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_115221')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_115226')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_115382')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_115937')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_116011')`  |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_1914')`    |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_34610')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_6746')`    |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_6774')`    |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_77706')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_78624')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_79198')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_80387')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_80628')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_80681')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_80797')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_81714')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_87541')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_89800')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_90034')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_90935')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_92894')`   |              1 | [GO:0004519](http://purl.obolibrary.org/obo/GO_0004519)                                                          |
| `Reactome:('Reactome', 'REACT_101184')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_101250')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_101987')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_103441')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_103771')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_104010')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_104673')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_104703')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_104968')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_106756')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_109040')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_109537')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_109692')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_110386')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_112122')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_112152')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_115154')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_115463')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_115479')`  |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_1274')`    |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_1311')`    |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_1964')`    |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_27164')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_27209')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_28610')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_28960')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_30718')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_31162')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_31548')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_31660')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_31823')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_32833')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_33043')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_78421')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_79265')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_80173')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_80298')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_80967')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_811')`     |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_81197')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_82925')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_83838')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_85019')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_88339')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_90087')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_92741')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_94592')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_94820')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_95903')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_97114')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_98405')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_98417')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_99783')`   |              1 | [GO:0004520](http://purl.obolibrary.org/obo/GO_0004520)                                                          |
| `Reactome:('Reactome', 'REACT_100642')`  |              1 | [GO:0004536](http://purl.obolibrary.org/obo/GO_0004536)                                                          |
| `Reactome:('Reactome', 'REACT_101208')`  |              1 | [GO:0004536](http://purl.obolibrary.org/obo/GO_0004536)                                                          |
| `Reactome:('Reactome', 'REACT_110575')`  |              1 | [GO:0004536](http://purl.obolibrary.org/obo/GO_0004536)                                                          |
| `Reactome:('Reactome', 'REACT_13702')`   |              1 | [GO:0004536](http://purl.obolibrary.org/obo/GO_0004536)                                                          |
| `Reactome:('Reactome', 'REACT_29722')`   |              1 | [GO:0004536](http://purl.obolibrary.org/obo/GO_0004536)                                                          |
| `Reactome:('Reactome', 'REACT_31853')`   |              1 | [GO:0004536](http://purl.obolibrary.org/obo/GO_0004536)                                                          |
| `Reactome:('Reactome', 'REACT_90424')`   |              1 | [GO:0004536](http://purl.obolibrary.org/obo/GO_0004536)                                                          |
| `Reactome:('Reactome', 'REACT_95359')`   |              1 | [GO:0004536](http://purl.obolibrary.org/obo/GO_0004536)                                                          |
| `Reactome:('Reactome', 'REACT_98682')`   |              1 | [GO:0004536](http://purl.obolibrary.org/obo/GO_0004536)                                                          |
| `Reactome:('Reactome', 'REACT_100559')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_101280')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_101497')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_102679')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_103614')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_104547')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_105292')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_105467')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_105835')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_106018')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_106104')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_106382')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_106434')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_106732')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_107075')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_107423')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_108461')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_108634')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_108739')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_108768')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_108929')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_109137')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_112472')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_113703')`  |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_29423')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_29444')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_29691')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_29764')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_30149')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_31024')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_31919')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_32546')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_32932')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_33572')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_33874')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_50018')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_53588')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_6729')`    |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_6738')`    |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_6750')`    |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_6769')`    |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_6798')`    |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_6869')`    |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_6936')`    |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_6939')`    |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_77532')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_79188')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_79450')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_80432')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_80571')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_80896')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_80988')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_81803')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_83095')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_84829')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_85561')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_86410')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_86739')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_87233')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_87449')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_87590')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_88085')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_88384')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_88529')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_89355')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_89439')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_89725')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_90512')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_90809')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_90838')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_91184')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_91302')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_92527')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_92644')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_92706')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_94983')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_95253')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_95329')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_96115')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_96804')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_96998')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_97204')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_97726')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_99948')`   |              1 | [GO:0006260](http://purl.obolibrary.org/obo/GO_0006260)                                                          |
| `Reactome:('Reactome', 'REACT_6880')`    |              1 | [GO:0006278](http://purl.obolibrary.org/obo/GO_0006278)                                                          |
| `Reactome:('Reactome', 'REACT_9037')`    |              1 | [GO:0006278](http://purl.obolibrary.org/obo/GO_0006278)                                                          |
| `Reactome:('Reactome', 'REACT_9055')`    |              1 | [GO:0006278](http://purl.obolibrary.org/obo/GO_0006278)                                                          |
| `Reactome:('Reactome', 'REACT_102783')`  |              1 | [GO:0006309](http://purl.obolibrary.org/obo/GO_0006309)                                                          |
| `Reactome:('Reactome', 'REACT_105342')`  |              1 | [GO:0006309](http://purl.obolibrary.org/obo/GO_0006309)                                                          |
| `Reactome:('Reactome', 'REACT_110358')`  |              1 | [GO:0006309](http://purl.obolibrary.org/obo/GO_0006309)                                                          |
| `Reactome:('Reactome', 'REACT_113418')`  |              1 | [GO:0006309](http://purl.obolibrary.org/obo/GO_0006309)                                                          |
| `Reactome:('Reactome', 'REACT_1213')`    |              1 | [GO:0006309](http://purl.obolibrary.org/obo/GO_0006309)                                                          |
| `Reactome:('Reactome', 'REACT_28808')`   |              1 | [GO:0006309](http://purl.obolibrary.org/obo/GO_0006309)                                                          |
| `Reactome:('Reactome', 'REACT_33113')`   |              1 | [GO:0006309](http://purl.obolibrary.org/obo/GO_0006309)                                                          |
| `Reactome:('Reactome', 'REACT_92967')`   |              1 | [GO:0006309](http://purl.obolibrary.org/obo/GO_0006309)                                                          |
| `Reactome:('Reactome', 'REACT_94135')`   |              1 | [GO:0006309](http://purl.obolibrary.org/obo/GO_0006309)                                                          |
| `Reactome:('Reactome', 'REACT_98713')`   |              1 | [GO:0006309](http://purl.obolibrary.org/obo/GO_0006309)                                                          |
| `Reactome:('Reactome', 'REACT_99275')`   |              1 | [GO:0006309](http://purl.obolibrary.org/obo/GO_0006309)                                                          |
| `Reactome:('Reactome', 'REACT_99925')`   |              1 | [GO:0006309](http://purl.obolibrary.org/obo/GO_0006309)                                                          |
| `Reactome:('Reactome', 'REACT_100045')`  |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_100962')`  |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_101249')`  |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_104187')`  |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_105149')`  |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_106405')`  |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_106672')`  |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_107264')`  |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_108651')`  |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_109165')`  |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_110081')`  |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_111964')`  |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_13526')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_13638')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_13643')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_28087')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_28795')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_28816')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_30266')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_30361')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_30371')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_30548')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_30763')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_31349')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_34139')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_578')`     |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_77132')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_77313')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_77415')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_78287')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_78802')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_79809')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_82724')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_83328')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_85877')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_86749')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_86873')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_87570')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_88740')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_88784')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_89196')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_90267')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_91011')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_91243')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_93937')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_94099')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_95069')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_95675')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_97627')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_99784')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_99799')`   |              1 | [GO:0006915](http://purl.obolibrary.org/obo/GO_0006915)                                                          |
| `Reactome:('Reactome', 'REACT_100800')`  |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_108463')`  |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_29660')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_77151')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_78666')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_79472')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_79859')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_80493')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_81021')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_81052')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_84120')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_89424')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_90988')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_92689')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_93576')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_94230')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_97703')`   |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_995')`     |              1 | [GO:0006921](http://purl.obolibrary.org/obo/GO_0006921)                                                          |
| `Reactome:('Reactome', 'REACT_100624')`  |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_102354')`  |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_112130')`  |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_112549')`  |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_113151')`  |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_113601')`  |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_113964')`  |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_114657')`  |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_114690')`  |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_114820')`  |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_114910')`  |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_115037')`  |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_115147')`  |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_12478')`   |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_31232')`   |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_78535')`   |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_89740')`   |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_93680')`   |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_98872')`   |              1 | [GO:0007165](http://purl.obolibrary.org/obo/GO_0007165)                                                          |
| `Reactome:('Reactome', 'REACT_25351')`   |              1 | [GO:0007249](http://purl.obolibrary.org/obo/GO_0007249)                                                          |
| `Reactome:('Reactome', 'REACT_6227')`    |              1 | [GO:0009967](http://purl.obolibrary.org/obo/GO_0009967)                                                          |
| `Reactome:('Reactome', 'REACT_6334')`    |              1 | [GO:0009968](http://purl.obolibrary.org/obo/GO_0009968)                                                          |
| `Reactome:('Reactome', 'REACT_100537')`  |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_101147')`  |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_101952')`  |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_105649')`  |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_108313')`  |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_29068')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_34240')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_71')`      |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_78136')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_78959')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_79662')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_85241')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_85359')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_86357')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_89816')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_91657')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_91965')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_93586')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_93968')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_94814')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_98256')`   |              1 | [GO:0010467](http://purl.obolibrary.org/obo/GO_0010467)                                                          |
| `Reactome:('Reactome', 'REACT_107259')`  |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_107652')`  |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_110289')`  |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_21257')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_30579')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_31367')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_33720')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_80071')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_83630')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_84169')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_85788')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_88316')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_89992')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_91556')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_92152')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_94876')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_99403')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_99885')`   |              1 | [GO:0016070](http://purl.obolibrary.org/obo/GO_0016070)                                                          |
| `Reactome:('Reactome', 'REACT_25050')`   |              1 | [GO:0016740](http://purl.obolibrary.org/obo/GO_0016740)                                                          |
| `Reactome:('Reactome', 'REACT_110436')`  |              1 | [GO:0016787](http://purl.obolibrary.org/obo/GO_0016787)                                                          |
| `Reactome:('Reactome', 'REACT_111159')`  |              1 | [GO:0016787](http://purl.obolibrary.org/obo/GO_0016787)                                                          |
| `Reactome:('Reactome', 'REACT_15331')`   |              1 | [GO:0016787](http://purl.obolibrary.org/obo/GO_0016787)                                                          |
| `Reactome:('Reactome', 'REACT_83734')`   |              1 | [GO:0016787](http://purl.obolibrary.org/obo/GO_0016787)                                                          |
| `Reactome:('Reactome', 'REACT_84047')`   |              1 | [GO:0016787](http://purl.obolibrary.org/obo/GO_0016787)                                                          |
| `Reactome:('Reactome', 'REACT_87959')`   |              1 | [GO:0016787](http://purl.obolibrary.org/obo/GO_0016787)                                                          |
| `Reactome:('Reactome', 'REACT_88159')`   |              1 | [GO:0016787](http://purl.obolibrary.org/obo/GO_0016787)                                                          |
| `Reactome:('Reactome', 'REACT_90118')`   |              1 | [GO:0016787](http://purl.obolibrary.org/obo/GO_0016787)                                                          |
| `Reactome:('Reactome', 'REACT_91045')`   |              1 | [GO:0016787](http://purl.obolibrary.org/obo/GO_0016787)                                                          |
| `Reactome:('Reactome', 'REACT_98572')`   |              1 | [GO:0016787](http://purl.obolibrary.org/obo/GO_0016787)                                                          |
| `Reactome:('Reactome', 'REACT_106563')`  |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_109748')`  |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_112177')`  |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_19294')`   |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_1978')`    |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_45174')`   |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_77112')`   |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_81282')`   |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_83347')`   |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_88228')`   |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_88314')`   |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_89615')`   |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_92446')`   |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_94475')`   |              1 | [GO:0016788](http://purl.obolibrary.org/obo/GO_0016788)                                                          |
| `Reactome:('Reactome', 'REACT_101225')`  |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_102187')`  |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_102331')`  |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_105293')`  |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_108571')`  |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_109170')`  |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_2122')`    |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_28360')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_31270')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_79603')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_80902')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_83058')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_84314')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_86633')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_87840')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_88060')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_91293')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_91429')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_91906')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_92487')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_99393')`   |              1 | [GO:0031325](http://purl.obolibrary.org/obo/GO_0031325)                                                          |
| `Reactome:('Reactome', 'REACT_115680')`  |              1 | [GO:0034061](http://purl.obolibrary.org/obo/GO_0034061)                                                          |
| `Reactome:('Reactome', 'REACT_115778')`  |              1 | [GO:0034061](http://purl.obolibrary.org/obo/GO_0034061)                                                          |
| `Reactome:('Reactome', 'REACT_115899')`  |              1 | [GO:0034061](http://purl.obolibrary.org/obo/GO_0034061)                                                          |
| `Reactome:('Reactome', 'REACT_115932')`  |              1 | [GO:0034061](http://purl.obolibrary.org/obo/GO_0034061)                                                          |
| `Reactome:('Reactome', 'REACT_116106')`  |              1 | [GO:0034061](http://purl.obolibrary.org/obo/GO_0034061)                                                          |
| `Reactome:('Reactome', 'REACT_116167')`  |              1 | [GO:0034061](http://purl.obolibrary.org/obo/GO_0034061)                                                          |
| `Reactome:('Reactome', 'REACT_102000')`  |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_103710')`  |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_107293')`  |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_108179')`  |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_109042')`  |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_13')`      |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_28699')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_29108')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_32429')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_33347')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_34326')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_55564')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_77741')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_82379')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_86268')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_90299')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_91959')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_93580')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_95666')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_98086')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_99241')`   |              1 | [GO:0034641](http://purl.obolibrary.org/obo/GO_0034641)                                                          |
| `Reactome:('Reactome', 'REACT_100795')`  |              1 | [GO:0035556](http://purl.obolibrary.org/obo/GO_0035556)                                                          |
| `Reactome:('Reactome', 'REACT_102462')`  |              1 | [GO:0035556](http://purl.obolibrary.org/obo/GO_0035556)                                                          |
| `Reactome:('Reactome', 'REACT_104200')`  |              1 | [GO:0035556](http://purl.obolibrary.org/obo/GO_0035556)                                                          |
| `Reactome:('Reactome', 'REACT_108216')`  |              1 | [GO:0035556](http://purl.obolibrary.org/obo/GO_0035556)                                                          |
| `Reactome:('Reactome', 'REACT_1525')`    |              1 | [GO:0035556](http://purl.obolibrary.org/obo/GO_0035556)                                                          |
| `Reactome:('Reactome', 'REACT_80030')`   |              1 | [GO:0035556](http://purl.obolibrary.org/obo/GO_0035556)                                                          |
| `Reactome:('Reactome', 'REACT_83068')`   |              1 | [GO:0035556](http://purl.obolibrary.org/obo/GO_0035556)                                                          |
| `Reactome:('Reactome', 'REACT_83869')`   |              1 | [GO:0035556](http://purl.obolibrary.org/obo/GO_0035556)                                                          |
| `Reactome:('Reactome', 'REACT_87453')`   |              1 | [GO:0035556](http://purl.obolibrary.org/obo/GO_0035556)                                                          |
| `Reactome:('Reactome', 'REACT_89085')`   |              1 | [GO:0035556](http://purl.obolibrary.org/obo/GO_0035556)                                                          |
| `Reactome:('Reactome', 'REACT_89983')`   |              1 | [GO:0035556](http://purl.obolibrary.org/obo/GO_0035556)                                                          |
| `Reactome:('Reactome', 'REACT_90740')`   |              1 | [GO:0035556](http://purl.obolibrary.org/obo/GO_0035556)                                                          |
| `Reactome:('Reactome', 'REACT_99938')`   |              1 | [GO:0035556](http://purl.obolibrary.org/obo/GO_0035556)                                                          |
| `Reactome:('Reactome', 'REACT_24918')`   |              1 | [GO:0043123](http://purl.obolibrary.org/obo/GO_0043123)                                                          |
| `Reactome:('Reactome', 'REACT_104536')`  |              1 | [GO:0051090](http://purl.obolibrary.org/obo/GO_0051090)                                                          |
| `Reactome:('Reactome', 'REACT_107559')`  |              1 | [GO:0051090](http://purl.obolibrary.org/obo/GO_0051090)                                                          |
| `Reactome:('Reactome', 'REACT_109535')`  |              1 | [GO:0051090](http://purl.obolibrary.org/obo/GO_0051090)                                                          |
| `Reactome:('Reactome', 'REACT_110257')`  |              1 | [GO:0051090](http://purl.obolibrary.org/obo/GO_0051090)                                                          |
| `Reactome:('Reactome', 'REACT_110693')`  |              1 | [GO:0051090](http://purl.obolibrary.org/obo/GO_0051090)                                                          |
| `Reactome:('Reactome', 'REACT_21326')`   |              1 | [GO:0051090](http://purl.obolibrary.org/obo/GO_0051090)                                                          |
| `Reactome:('Reactome', 'REACT_82719')`   |              1 | [GO:0051090](http://purl.obolibrary.org/obo/GO_0051090)                                                          |
| `Reactome:('Reactome', 'REACT_83365')`   |              1 | [GO:0051090](http://purl.obolibrary.org/obo/GO_0051090)                                                          |
| `Reactome:('Reactome', 'REACT_90659')`   |              1 | [GO:0051090](http://purl.obolibrary.org/obo/GO_0051090)                                                          |
| `Reactome:('Reactome', 'REACT_92725')`   |              1 | [GO:0051090](http://purl.obolibrary.org/obo/GO_0051090)                                                          |
| `Reactome:('Reactome', 'REACT_96476')`   |              1 | [GO:0051090](http://purl.obolibrary.org/obo/GO_0051090)                                                          |
| `Reactome:('Reactome', 'REACT_99415')`   |              1 | [GO:0051090](http://purl.obolibrary.org/obo/GO_0051090)                                                          |
| `Reactome:('Reactome', 'REACT_107873')`  |              1 | [GO:0051092](http://purl.obolibrary.org/obo/GO_0051092)                                                          |
| `Reactome:('Reactome', 'REACT_113398')`  |              1 | [GO:0051092](http://purl.obolibrary.org/obo/GO_0051092)                                                          |
| `Reactome:('Reactome', 'REACT_113766')`  |              1 | [GO:0051092](http://purl.obolibrary.org/obo/GO_0051092)                                                          |
| `Reactome:('Reactome', 'REACT_21281')`   |              1 | [GO:0051092](http://purl.obolibrary.org/obo/GO_0051092)                                                          |
| `Reactome:('Reactome', 'REACT_31084')`   |              1 | [GO:0051092](http://purl.obolibrary.org/obo/GO_0051092)                                                          |
| `Reactome:('Reactome', 'REACT_33907')`   |              1 | [GO:0051092](http://purl.obolibrary.org/obo/GO_0051092)                                                          |
| `Reactome:('Reactome', 'REACT_34168')`   |              1 | [GO:0051092](http://purl.obolibrary.org/obo/GO_0051092)                                                          |
| `Reactome:('Reactome', 'REACT_34256')`   |              1 | [GO:0051092](http://purl.obolibrary.org/obo/GO_0051092)                                                          |
| `Reactome:('Reactome', 'REACT_87914')`   |              1 | [GO:0051092](http://purl.obolibrary.org/obo/GO_0051092)                                                          |
| `Reactome:('Reactome', 'REACT_95400')`   |              1 | [GO:0051092](http://purl.obolibrary.org/obo/GO_0051092)                                                          |
| `Reactome:('Reactome', 'REACT_9004')`    |              1 | [GO:0051169](http://purl.obolibrary.org/obo/GO_0051169)                                                          |
| `Reactome:('Reactome', 'REACT_10010')`   |              1 | [GO:0051170](http://purl.obolibrary.org/obo/GO_0051170)                                                          |
| `Reactome:('Reactome', 'REACT_32050')`   |              1 | [GO:0051170](http://purl.obolibrary.org/obo/GO_0051170)                                                          |
| `Reactome:('Reactome', 'REACT_91459')`   |              1 | [GO:0051170](http://purl.obolibrary.org/obo/GO_0051170)                                                          |
| `Reactome:('Reactome', 'REACT_97007')`   |              1 | [GO:0051170](http://purl.obolibrary.org/obo/GO_0051170)                                                          |
| `Reactome:('Reactome', 'REACT_101524')`  |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_103082')`  |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_11123')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_29278')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_32337')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_33741')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_34084')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_78213')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_78288')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_83546')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_86557')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_87431')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_88307')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_91154')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_93714')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_95586')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_96516')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |
| `Reactome:('Reactome', 'REACT_97881')`   |              1 | [GO:0061024](http://purl.obolibrary.org/obo/GO_0061024)                                                          |

## `Wikipedia`: Wikipedia

Overall, there were 14 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                                                       |   usages_count | usages                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Wikipedia:('Wikipedia', 'Association_(statistics)')`                               |              2 | [pato#directly:associated:with](http://purl.obolibrary.org/obo/pato#directly_associated_with), [pato#inversely:associated:with](http://purl.obolibrary.org/obo/pato#inversely_associated_with) |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Velocity')`                  |              1 | [PATO:0000008](http://purl.obolibrary.org/obo/PATO_0000008)                                                                                                                                    |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/concentration')`             |              1 | [PATO:0000033](http://purl.obolibrary.org/obo/PATO_0000033)                                                                                                                                    |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/frequency')`                 |              1 | [PATO:0000044](http://purl.obolibrary.org/obo/PATO_0000044)                                                                                                                                    |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Electromagnetic_radiation')` |              1 | [PATO:0001291](http://purl.obolibrary.org/obo/PATO_0001291)                                                                                                                                    |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Area')`                      |              1 | [PATO:0001323](http://purl.obolibrary.org/obo/PATO_0001323)                                                                                                                                    |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Ploidy')`                    |              1 | [PATO:0001374](http://purl.obolibrary.org/obo/PATO_0001374)                                                                                                                                    |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Polyploid')`                 |              1 | [PATO:0001377](http://purl.obolibrary.org/obo/PATO_0001377)                                                                                                                                    |
| `Wikipedia:('Wikipedia', 'http://en.wikipedia.org/wiki/Euploid')`                   |              1 | [PATO:0001393](http://purl.obolibrary.org/obo/PATO_0001393)                                                                                                                                    |
| `Wikipedia:('Wikipedia', 'Binding_(molecular)')`                                    |              1 | [GO:0005488](http://purl.obolibrary.org/obo/GO_0005488)                                                                                                                                        |
| `Wikipedia:('Wikipedia', 'Cell_(biology)')`                                         |              1 | [GO:0005623](http://purl.obolibrary.org/obo/GO_0005623)                                                                                                                                        |
| `Wikipedia:('Wikipedia', 'Transcription_(genetics)')`                               |              1 | [GO:0006351](http://purl.obolibrary.org/obo/GO_0006351)                                                                                                                                        |
| `Wikipedia:('Wikipedia', 'Vesicle_(biology)')`                                      |              1 | [GO:0031982](http://purl.obolibrary.org/obo/GO_0031982)                                                                                                                                        |

## `wikipedia`: Wikipedia

Overall, there were 1 invalid
xrefs to external prefixed with `wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                                     |   usages_count | usages                                                      |
|-------------------------------------------------------------------|----------------|-------------------------------------------------------------|
| `wikipedia:('wikipedia', 'https://en.wikipedia.org/wiki/Acinus')` |              1 | [PATO:0002378](http://purl.obolibrary.org/obo/PATO_0002378) |

