# tao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `tao`.


## `CL`: Cell Ontology

Overall, there were 154 invalid
xrefs to external prefixed with `CL` (standardized to Bioregistry
prefix [`cl`](https://bioregistry.io/cl)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CL:curator`    |            153 | [TAO:0002148](http://purl.obolibrary.org/obo/TAO_0002148), [TAO:0002182](http://purl.obolibrary.org/obo/TAO_0002182), [TAO:0002211](http://purl.obolibrary.org/obo/TAO_0002211), [TAO:0005243](http://purl.obolibrary.org/obo/TAO_0005243), [TAO:0005322](http://purl.obolibrary.org/obo/TAO_0005322), ... |
| `CL:Curator`    |              1 | [TAO:0005242](http://purl.obolibrary.org/obo/TAO_0005242)                                                                                                                                                                                                                                                  |

## `TAO`: Teleost Anatomy Ontology

Overall, there were 670 invalid
xrefs to external prefixed with `TAO` (standardized to Bioregistry
prefix [`tao`](https://bioregistry.io/tao)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                              |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TAO:wd`                                   |            546 | [TAO:0000027](http://purl.obolibrary.org/obo/TAO_0000027), [TAO:0000037](http://purl.obolibrary.org/obo/TAO_0000037), [TAO:0000052](http://purl.obolibrary.org/obo/TAO_0000052), [TAO:0000078](http://purl.obolibrary.org/obo/TAO_0000078), [TAO:0000107](http://purl.obolibrary.org/obo/TAO_0000107), ... |
| `TAO:GA_TG`                                |             80 | [TAO:0000015](http://purl.obolibrary.org/obo/TAO_0000015), [TAO:0000104](http://purl.obolibrary.org/obo/TAO_0000104), [TAO:0000127](http://purl.obolibrary.org/obo/TAO_0000127), [TAO:0000191](http://purl.obolibrary.org/obo/TAO_0000191), [TAO:0000250](http://purl.obolibrary.org/obo/TAO_0000250), ... |
| `TAO:pem`                                  |              8 | [TAO:0000367](http://purl.obolibrary.org/obo/TAO_0000367), [TAO:0001675](http://purl.obolibrary.org/obo/TAO_0001675), [TAO:0001676](http://purl.obolibrary.org/obo/TAO_0001676), [TAO:0001677](http://purl.obolibrary.org/obo/TAO_0001677), [TAO:0001678](http://purl.obolibrary.org/obo/TAO_0001678), ... |
| `TAO:MAH`                                  |              6 | [TAO:0000189](http://purl.obolibrary.org/obo/TAO_0000189), [TAO:0000290](http://purl.obolibrary.org/obo/TAO_0000290), [TAO:0000351](http://purl.obolibrary.org/obo/TAO_0000351), [TAO:0001410](http://purl.obolibrary.org/obo/TAO_0001410), [TAO:0001414](http://purl.obolibrary.org/obo/TAO_0001414), ... |
| `TAO:ga_tg`                                |              4 | [TAO:0000103](http://purl.obolibrary.org/obo/TAO_0000103), [TAO:0000656](http://purl.obolibrary.org/obo/TAO_0000656), [TAO:0002020](http://purl.obolibrary.org/obo/TAO_0002020), [TAO:0002089](http://purl.obolibrary.org/obo/TAO_0002089)                                                                 |
| `TAO:curator`                              |              4 | [TAO:0000258](http://purl.obolibrary.org/obo/TAO_0000258), [TAO:0002149](http://purl.obolibrary.org/obo/TAO_0002149), [TAO:0002150](http://purl.obolibrary.org/obo/TAO_0002150), [TAO:0005225](http://purl.obolibrary.org/obo/TAO_0005225)                                                                 |
| `TAO:Arratia_2008`                         |              4 | [TAO:0001584](http://purl.obolibrary.org/obo/TAO_0001584), [TAO:0001829](http://purl.obolibrary.org/obo/TAO_0001829), [TAO:0001830](http://purl.obolibrary.org/obo/TAO_0001830), [TAO:0002165](http://purl.obolibrary.org/obo/TAO_0002165)                                                                 |
| `TAO:doi:10.1046/j.1096-3642.2002.00014.x` |              2 | [TAO:0001191](http://purl.obolibrary.org/obo/TAO_0001191), [TAO:0001192](http://purl.obolibrary.org/obo/TAO_0001192)                                                                                                                                                                                       |
| `TAO:Arratia_Schultze_1992`                |              1 | [TAO:0000602](http://purl.obolibrary.org/obo/TAO_0000602)                                                                                                                                                                                                                                                  |
| `TAO:Patterson_1968`                       |              1 | [TAO:0000602](http://purl.obolibrary.org/obo/TAO_0000602)                                                                                                                                                                                                                                                  |
| `TAO:Arratia and Schultze_1992`            |              1 | [TAO:0000660](http://purl.obolibrary.org/obo/TAO_0000660)                                                                                                                                                                                                                                                  |
| `TAO:je`                                   |              1 | [TAO:0001275](http://purl.obolibrary.org/obo/TAO_0001275)                                                                                                                                                                                                                                                  |
| `TAO:VSAO_workshop`                        |              1 | [TAO:0001890](http://purl.obolibrary.org/obo/TAO_0001890)                                                                                                                                                                                                                                                  |
| `TAO:w`                                    |              1 | [TAO:0001957](http://purl.obolibrary.org/obo/TAO_0001957)                                                                                                                                                                                                                                                  |
| `TAO:Bridge_1877`                          |              1 | [TAO:0000127](http://purl.obolibrary.org/obo/TAO_0000127)                                                                                                                                                                                                                                                  |
| `TAO:Goodrich_1930`                        |              1 | [TAO:0000127](http://purl.obolibrary.org/obo/TAO_0000127)                                                                                                                                                                                                                                                  |
| `TAO:Jollie_1984`                          |              1 | [TAO:0000127](http://purl.obolibrary.org/obo/TAO_0000127)                                                                                                                                                                                                                                                  |
| `TAO:Regan_1923`                           |              1 | [TAO:0000127](http://purl.obolibrary.org/obo/TAO_0000127)                                                                                                                                                                                                                                                  |
| `TAO:Arratia_Schultze_1990`                |              1 | [TAO:0000452](http://purl.obolibrary.org/obo/TAO_0000452)                                                                                                                                                                                                                                                  |
| `TAO:Harrington_1955`                      |              1 | [TAO:0000663](http://purl.obolibrary.org/obo/TAO_0000663)                                                                                                                                                                                                                                                  |
| `TAO:Weitzman_1962`                        |              1 | [TAO:0000663](http://purl.obolibrary.org/obo/TAO_0000663)                                                                                                                                                                                                                                                  |
| `TAO:Bird 2003`                            |              1 | [TAO:0001553](http://purl.obolibrary.org/obo/TAO_0001553)                                                                                                                                                                                                                                                  |
| `TAO:Bird and Mabee 2003`                  |              1 | [TAO:0001553](http://purl.obolibrary.org/obo/TAO_0001553)                                                                                                                                                                                                                                                  |
| `TAO:Fink and Fink 1981`                   |              1 | [TAO:0001553](http://purl.obolibrary.org/obo/TAO_0001553)                                                                                                                                                                                                                                                  |

## `ZFA`: Zebrafish anatomy and development ontology

Overall, there were 4 invalid
xrefs to external prefixed with `ZFA` (standardized to Bioregistry
prefix [`zfa`](https://bioregistry.io/zfa)) that
did not match the standard pattern `^\d{7}$`.

| external_xref           |   usages_count | usages                                                                                                                                                                          |
|-------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFA:curator`           |              3 | [TAO:0002135](http://purl.obolibrary.org/obo/TAO_0002135), [TAO:0002136](http://purl.obolibrary.org/obo/TAO_0002136), [TAO:0002141](http://purl.obolibrary.org/obo/TAO_0002141) |
| `ZFA:ZDB-PUB-060323-12` |              1 | [TAO:0005245](http://purl.obolibrary.org/obo/TAO_0005245)                                                                                                                       |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 811 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref    |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:curator`   |            805 | [TAO:0000000](http://purl.obolibrary.org/obo/TAO_0000000), [TAO:0000001](http://purl.obolibrary.org/obo/TAO_0000001), [TAO:0000006](http://purl.obolibrary.org/obo/TAO_0000006), [TAO:0000007](http://purl.obolibrary.org/obo/TAO_0000007), [TAO:0000008](http://purl.obolibrary.org/obo/TAO_0000008), ... |
| `ZFIN:Curator`   |              4 | [TAO:0005153](http://purl.obolibrary.org/obo/TAO_0005153), [TAO:0005165](http://purl.obolibrary.org/obo/TAO_0005165), [TAO:0005166](http://purl.obolibrary.org/obo/TAO_0005166), [TAO:0005210](http://purl.obolibrary.org/obo/TAO_0005210)                                                                 |
| `ZFIN:090511-18` |              1 | [TAO:0002145](http://purl.obolibrary.org/obo/TAO_0002145)                                                                                                                                                                                                                                                  |
| `ZFIN:CVS`       |              1 | [TAO:0005265](http://purl.obolibrary.org/obo/TAO_0005265)                                                                                                                                                                                                                                                  |

