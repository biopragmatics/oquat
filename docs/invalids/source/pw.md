# pw

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `pw`. See the [GitHub repository](https://github.com/rat-genome-database/PW-Pathway-Ontology).


## `KEGG`: Kyoto Encyclopedia of Genes and Genomes

Overall, there were 78 invalid
xrefs to external prefixed with `KEGG` (standardized to Bioregistry
prefix [`kegg`](https://bioregistry.io/kegg)) that
did not match the standard pattern `^([CHDEGTMKR]\d+)|(\w+:[\w\d\.-]*)|([a-z]{3,5})|(\w{2,4}\d{5})$`.

| external_xref   |   usages_count | usages                                                                                                           |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `KEGG:00760`    |              2 | [PW:0000166](http://purl.obolibrary.org/obo/PW_0000166), [PW:0001010](http://purl.obolibrary.org/obo/PW_0001010) |
| `KEGG:04610`    |              2 | [PW:0000474](http://purl.obolibrary.org/obo/PW_0000474), [PW:0000502](http://purl.obolibrary.org/obo/PW_0000502) |
| `KEGG:00010`    |              2 | [PW:0000640](http://purl.obolibrary.org/obo/PW_0000640), [PW:0000641](http://purl.obolibrary.org/obo/PW_0000641) |
| `KEGG:04310`    |              1 | [PW:0000008](http://purl.obolibrary.org/obo/PW_0000008)                                                          |
| `KEGG:00061`    |              1 | [PW:0000029](http://purl.obolibrary.org/obo/PW_0000029)                                                          |
| `KEGG:00230`    |              1 | [PW:0000031](http://purl.obolibrary.org/obo/PW_0000031)                                                          |
| `KEGG:00240`    |              1 | [PW:0000032](http://purl.obolibrary.org/obo/PW_0000032)                                                          |
| `KEGG:00920`    |              1 | [PW:0000037](http://purl.obolibrary.org/obo/PW_0000037)                                                          |
| `KEGG:00120`    |              1 | [PW:0000039](http://purl.obolibrary.org/obo/PW_0000039)                                                          |
| `KEGG:00140`    |              1 | [PW:0000040](http://purl.obolibrary.org/obo/PW_0000040)                                                          |
| `KEGG:00052`    |              1 | [PW:0000042](http://purl.obolibrary.org/obo/PW_0000042)                                                          |
| `KEGG:00620`    |              1 | [PW:0000043](http://purl.obolibrary.org/obo/PW_0000043)                                                          |
| `KEGG:00340`    |              1 | [PW:0000051](http://purl.obolibrary.org/obo/PW_0000051)                                                          |
| `KEGG:00350`    |              1 | [PW:0000052](http://purl.obolibrary.org/obo/PW_0000052)                                                          |
| `KEGG:00360`    |              1 | [PW:0000053](http://purl.obolibrary.org/obo/PW_0000053)                                                          |
| `KEGG:00380`    |              1 | [PW:0000054](http://purl.obolibrary.org/obo/PW_0000054)                                                          |
| `KEGG:00280`    |              1 | [PW:0000071](http://purl.obolibrary.org/obo/PW_0000071)                                                          |
| `KEGG:00310`    |              1 | [PW:0000073](http://purl.obolibrary.org/obo/PW_0000073)                                                          |
| `KEGG:00300`    |              1 | [PW:0000074](http://purl.obolibrary.org/obo/PW_0000074)                                                          |
| `KEGG:00460`    |              1 | [PW:0000078](http://purl.obolibrary.org/obo/PW_0000078)                                                          |
| `KEGG:00480`    |              1 | [PW:0000134](http://purl.obolibrary.org/obo/PW_0000134)                                                          |
| `KEGG:00740`    |              1 | [PW:0000137](http://purl.obolibrary.org/obo/PW_0000137)                                                          |
| `KEGG:00750`    |              1 | [PW:0000138](http://purl.obolibrary.org/obo/PW_0000138)                                                          |
| `KEGG:00780`    |              1 | [PW:0000139](http://purl.obolibrary.org/obo/PW_0000139)                                                          |
| `KEGG:00790`    |              1 | [PW:0000140](http://purl.obolibrary.org/obo/PW_0000140)                                                          |
| `KEGG:00130`    |              1 | [PW:0000142](http://purl.obolibrary.org/obo/PW_0000142)                                                          |
| `KEGG:map4910`  |              1 | [PW:0000143](http://purl.obolibrary.org/obo/PW_0000143)                                                          |
| `KEGG:03050`    |              1 | [PW:0000144](http://purl.obolibrary.org/obo/PW_0000144)                                                          |
| `KEGG:00520`    |              1 | [PW:0000152](http://purl.obolibrary.org/obo/PW_0000152)                                                          |
| `KEGG:00604`    |              1 | [PW:0000164](http://purl.obolibrary.org/obo/PW_0000164)                                                          |
| `KEGG:00770`    |              1 | [PW:0000167](http://purl.obolibrary.org/obo/PW_0000167)                                                          |
| `KEGG:00603`    |              1 | [PW:0000196](http://purl.obolibrary.org/obo/PW_0000196)                                                          |
| `KEGG:00600`    |              1 | [PW:0000197](http://purl.obolibrary.org/obo/PW_0000197)                                                          |
| `KEGG:03440`    |              1 | [PW:0000202](http://purl.obolibrary.org/obo/PW_0000202)                                                          |
| `KEGG:04151`    |              1 | [PW:0000232](http://purl.obolibrary.org/obo/PW_0000232)                                                          |
| `KEGG:04140`    |              1 | [PW:0000278](http://purl.obolibrary.org/obo/PW_0000278)                                                          |
| `KEGG:04144`    |              1 | [PW:0000281](http://purl.obolibrary.org/obo/PW_0000281)                                                          |
| `KEGG:04728`    |              1 | [PW:0000394](http://purl.obolibrary.org/obo/PW_0000394)                                                          |
| `KEGG:04070`    |              1 | [PW:0000595](http://purl.obolibrary.org/obo/PW_0000595)                                                          |
| `KEGG:04141`    |              1 | [PW:0000638](http://purl.obolibrary.org/obo/PW_0000638)                                                          |
| `KEGG:03430`    |              1 | [PW:0000662](http://purl.obolibrary.org/obo/PW_0000662)                                                          |
| `KEGG:04620`    |              1 | [PW:0000814](http://purl.obolibrary.org/obo/PW_0000814)                                                          |
| `KEGG:04622`    |              1 | [PW:0000816](http://purl.obolibrary.org/obo/PW_0000816)                                                          |
| `KEGG:04621`    |              1 | [PW:0000817](http://purl.obolibrary.org/obo/PW_0000817)                                                          |
| `KEGG:04660`    |              1 | [PW:0000821](http://purl.obolibrary.org/obo/PW_0000821)                                                          |
| `KEGG:04662`    |              1 | [PW:0000822](http://purl.obolibrary.org/obo/PW_0000822)                                                          |
| `KEGG:04612`    |              1 | [PW:0000825](http://purl.obolibrary.org/obo/PW_0000825)                                                          |
| `KEGG:04060`    |              1 | [PW:0000828](http://purl.obolibrary.org/obo/PW_0000828)                                                          |
| `KEGG:04062`    |              1 | [PW:0000829](http://purl.obolibrary.org/obo/PW_0000829)                                                          |
| `KEGG:04725`    |              1 | [PW:0000841](http://purl.obolibrary.org/obo/PW_0000841)                                                          |
| `KEGG:04724`    |              1 | [PW:0000844](http://purl.obolibrary.org/obo/PW_0000844)                                                          |
| `KEGG:04727`    |              1 | [PW:0000848](http://purl.obolibrary.org/obo/PW_0000848)                                                          |
| `KEGG:05212`    |              1 | [PW:0000961](http://purl.obolibrary.org/obo/PW_0000961)                                                          |
| `KEGG:04744`    |              1 | [PW:0000962](http://purl.obolibrary.org/obo/PW_0000962)                                                          |
| `KEGG:map5140`  |              1 | [PW:0001047](http://purl.obolibrary.org/obo/PW_0001047)                                                          |
| `KEGG:map5142`  |              1 | [PW:0001048](http://purl.obolibrary.org/obo/PW_0001048)                                                          |
| `KEGG:map5143`  |              1 | [PW:0001049](http://purl.obolibrary.org/obo/PW_0001049)                                                          |
| `KEGG:map5146`  |              1 | [PW:0001053](http://purl.obolibrary.org/obo/PW_0001053)                                                          |
| `KEGG:00190`    |              1 | [PW:0001059](http://purl.obolibrary.org/obo/PW_0001059)                                                          |
| `KEGG:00785`    |              1 | [PW:0001063](http://purl.obolibrary.org/obo/PW_0001063)                                                          |
| `KEGG:03460`    |              1 | [PW:0001065](http://purl.obolibrary.org/obo/PW_0001065)                                                          |
| `KEGG:03008`    |              1 | [PW:0001066](http://purl.obolibrary.org/obo/PW_0001066)                                                          |
| `KEGG:00062`    |              1 | [PW:0001136](http://purl.obolibrary.org/obo/PW_0001136)                                                          |
| `KEGG:00565`    |              1 | [PW:0001138](http://purl.obolibrary.org/obo/PW_0001138)                                                          |
| `KEGG:04145`    |              1 | [PW:0001145](http://purl.obolibrary.org/obo/PW_0001145)                                                          |
| `KEGG:00100`    |              1 | [PW:0001152](http://purl.obolibrary.org/obo/PW_0001152)                                                          |
| `KEGG:00232`    |              1 | [PW:0001153](http://purl.obolibrary.org/obo/PW_0001153)                                                          |
| `KEGG:00531`    |              1 | [PW:0001154](http://purl.obolibrary.org/obo/PW_0001154)                                                          |
| `KEGG:00561`    |              1 | [PW:0001156](http://purl.obolibrary.org/obo/PW_0001156)                                                          |
| `KEGG:00592`    |              1 | [PW:0001158](http://purl.obolibrary.org/obo/PW_0001158)                                                          |
| `KEGG:00970`    |              1 | [PW:0001159](http://purl.obolibrary.org/obo/PW_0001159)                                                          |
| `KEGG:03013`    |              1 | [PW:0001160](http://purl.obolibrary.org/obo/PW_0001160)                                                          |
| `KEGG:03018`    |              1 | [PW:0001161](http://purl.obolibrary.org/obo/PW_0001161)                                                          |
| `KEGG:04723`    |              1 | [PW:0001164](http://purl.obolibrary.org/obo/PW_0001164)                                                          |
| `KEGG:04721`    |              1 | [PW:0002423](http://purl.obolibrary.org/obo/PW_0002423)                                                          |

## `MeSH`: Medical Subject Headings

Overall, there were 6 invalid
xrefs to external prefixed with `MeSH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                   |   usages_count | usages                                                                                                                                                                    |
|---------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MeSH:MeSH`                     |              3 | [PW:0000627](http://purl.obolibrary.org/obo/PW_0000627), [PW:0000631](http://purl.obolibrary.org/obo/PW_0000631), [PW:0000633](http://purl.obolibrary.org/obo/PW_0000633) |
| `MeSH:Medical_Subject_Headings` |              2 | [PW:0000517](http://purl.obolibrary.org/obo/PW_0000517), [PW:0001476](http://purl.obolibrary.org/obo/PW_0001476)                                                          |
| `MeSH:MeSH_descriptor`          |              1 | [PW:0001414](http://purl.obolibrary.org/obo/PW_0001414)                                                                                                                   |

## `NCI`: NCI Thesaurus

Overall, there were 3 invalid
xrefs to external prefixed with `NCI` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref        |   usages_count | usages                                                                                                           |
|----------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `NCI:NCI`            |              2 | [PW:0001211](http://purl.obolibrary.org/obo/PW_0001211), [PW:0001212](http://purl.obolibrary.org/obo/PW_0001212) |
| `NCI:www.cancer.gov` |              1 | [PW:0001217](http://purl.obolibrary.org/obo/PW_0001217)                                                          |

## `OMIM`: Online Mendelian Inheritance in Man

Overall, there were 3 invalid
xrefs to external prefixed with `OMIM` (standardized to Bioregistry
prefix [`omim`](https://bioregistry.io/omim)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                    |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `OMIM:OMIM`     |              3 | [PW:0000625](http://purl.obolibrary.org/obo/PW_0000625), [PW:0000627](http://purl.obolibrary.org/obo/PW_0000627), [PW:0000631](http://purl.obolibrary.org/obo/PW_0000631) |

## `PID`: NCI Pathway Interaction Database: Pathway

Overall, there were 49 invalid
xrefs to external prefixed with `PID` (standardized to Bioregistry
prefix [`pid.pathway`](https://bioregistry.io/pid.pathway)) that
did not match the standard pattern `^\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `PID:200168`    |              1 | [PW:0000122](http://purl.obolibrary.org/obo/PW_0000122) |
| `PID:200172`    |              1 | [PW:0000122](http://purl.obolibrary.org/obo/PW_0000122) |
| `PID:200014`    |              1 | [PW:0000143](http://purl.obolibrary.org/obo/PW_0000143) |
| `PID:200101`    |              1 | [PW:0000170](http://purl.obolibrary.org/obo/PW_0000170) |
| `PID:200159`    |              1 | [PW:0000170](http://purl.obolibrary.org/obo/PW_0000170) |
| `PID:200096`    |              1 | [PW:0000180](http://purl.obolibrary.org/obo/PW_0000180) |
| `PID:200018`    |              1 | [PW:0000198](http://purl.obolibrary.org/obo/PW_0000198) |
| `PID:200077`    |              1 | [PW:0000201](http://purl.obolibrary.org/obo/PW_0000201) |
| `PID:200015`    |              1 | [PW:0000204](http://purl.obolibrary.org/obo/PW_0000204) |
| `PID:200197`    |              1 | [PW:0000232](http://purl.obolibrary.org/obo/PW_0000232) |
| `PID:200102`    |              1 | [PW:0000233](http://purl.obolibrary.org/obo/PW_0000233) |
| `PID:200100`    |              1 | [PW:0000238](http://purl.obolibrary.org/obo/PW_0000238) |
| `PID:200109`    |              1 | [PW:0000243](http://purl.obolibrary.org/obo/PW_0000243) |
| `PID:200188`    |              1 | [PW:0000243](http://purl.obolibrary.org/obo/PW_0000243) |
| `PID:200149`    |              1 | [PW:0000297](http://purl.obolibrary.org/obo/PW_0000297) |
| `PID:200162`    |              1 | [PW:0000297](http://purl.obolibrary.org/obo/PW_0000297) |
| `PID:200201`    |              1 | [PW:0000297](http://purl.obolibrary.org/obo/PW_0000297) |
| `PID:200052`    |              1 | [PW:0000322](http://purl.obolibrary.org/obo/PW_0000322) |
| `PID:200059`    |              1 | [PW:0000322](http://purl.obolibrary.org/obo/PW_0000322) |
| `PID:200142`    |              1 | [PW:0000322](http://purl.obolibrary.org/obo/PW_0000322) |
| `PID:200204`    |              1 | [PW:0000322](http://purl.obolibrary.org/obo/PW_0000322) |
| `PID:200216`    |              1 | [PW:0000322](http://purl.obolibrary.org/obo/PW_0000322) |
| `PID:200220`    |              1 | [PW:0000328](http://purl.obolibrary.org/obo/PW_0000328) |
| `PID:200144`    |              1 | [PW:0000330](http://purl.obolibrary.org/obo/PW_0000330) |
| `PID:200029`    |              1 | [PW:0000331](http://purl.obolibrary.org/obo/PW_0000331) |
| `PID:200036`    |              1 | [PW:0000360](http://purl.obolibrary.org/obo/PW_0000360) |
| `PID:200202`    |              1 | [PW:0000360](http://purl.obolibrary.org/obo/PW_0000360) |
| `PID:200195`    |              1 | [PW:0000387](http://purl.obolibrary.org/obo/PW_0000387) |
| `PID:200062`    |              1 | [PW:0000388](http://purl.obolibrary.org/obo/PW_0000388) |
| `PID:200005`    |              1 | [PW:0000506](http://purl.obolibrary.org/obo/PW_0000506) |
| `PID:200146`    |              1 | [PW:0000516](http://purl.obolibrary.org/obo/PW_0000516) |
| `PID:200020`    |              1 | [PW:0000597](http://purl.obolibrary.org/obo/PW_0000597) |
| `PID:200080`    |              1 | [PW:0000681](http://purl.obolibrary.org/obo/PW_0000681) |
| `PID:200068`    |              1 | [PW:0000682](http://purl.obolibrary.org/obo/PW_0000682) |
| `PID:200089`    |              1 | [PW:0000883](http://purl.obolibrary.org/obo/PW_0000883) |
| `PID:200129`    |              1 | [PW:0000896](http://purl.obolibrary.org/obo/PW_0000896) |
| `PID:200098`    |              1 | [PW:0000907](http://purl.obolibrary.org/obo/PW_0000907) |
| `PID:200022`    |              1 | [PW:0000912](http://purl.obolibrary.org/obo/PW_0000912) |
| `PID:200045`    |              1 | [PW:0000914](http://purl.obolibrary.org/obo/PW_0000914) |
| `PID:200154`    |              1 | [PW:0000915](http://purl.obolibrary.org/obo/PW_0000915) |
| `PID:200028`    |              1 | [PW:0000916](http://purl.obolibrary.org/obo/PW_0000916) |
| `PID:200046`    |              1 | [PW:0000960](http://purl.obolibrary.org/obo/PW_0000960) |
| `PID:200054`    |              1 | [PW:0000960](http://purl.obolibrary.org/obo/PW_0000960) |
| `PID:200076`    |              1 | [PW:0000960](http://purl.obolibrary.org/obo/PW_0000960) |
| `PID:200085`    |              1 | [PW:0000960](http://purl.obolibrary.org/obo/PW_0000960) |
| `PID:200123`    |              1 | [PW:0000960](http://purl.obolibrary.org/obo/PW_0000960) |
| `PID:200211`    |              1 | [PW:0000960](http://purl.obolibrary.org/obo/PW_0000960) |
| `PID:200119`    |              1 | [PW:0000961](http://purl.obolibrary.org/obo/PW_0000961) |
| `PID:200019`    |              1 | [PW:0000970](http://purl.obolibrary.org/obo/PW_0000970) |

## `PMID`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `PMID:9212076;` |              1 | [PW:0000414](http://purl.obolibrary.org/obo/PW_0000414) |

## `PubMed`: PubMed

Overall, there were 14 invalid
xrefs to external prefixed with `PubMed` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                                                                 |   usages_count | usages                                                                                                           |
|-------------------------------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `PubMed:2003,_v._285,_f1-f8.`                                                 |              2 | [PW:0000182](http://purl.obolibrary.org/obo/PW_0000182), [PW:0000183](http://purl.obolibrary.org/obo/PW_0000183) |
| `PubMed:2001,_v.27,_171-179.`                                                 |              1 | [PW:0000144](http://purl.obolibrary.org/obo/PW_0000144)                                                          |
| `PubMed:Neuron,_2004,_v42,_p897-912;_Cellular_Signaling,_2004,_v16,_p127-36.` |              1 | [PW:0000169](http://purl.obolibrary.org/obo/PW_0000169)                                                          |
| `PubMed:2004,_v._17,_38047`                                                   |              1 | [PW:0000174](http://purl.obolibrary.org/obo/PW_0000174)                                                          |
| `PubMed:2004,_v.17,_38-47.`                                                   |              1 | [PW:0000175](http://purl.obolibrary.org/obo/PW_0000175)                                                          |
| `PubMed:2004,_v.29(1),_32-38.`                                                |              1 | [PW:0000179](http://purl.obolibrary.org/obo/PW_0000179)                                                          |
| `PubMed:TIBS,_2004,_v._29(1),_32-38.`                                         |              1 | [PW:0000180](http://purl.obolibrary.org/obo/PW_0000180)                                                          |
| `PubMed:Several_articles_in_PubMed`                                           |              1 | [PW:0000204](http://purl.obolibrary.org/obo/PW_0000204)                                                          |
| `PubMed:TIBS,_2004,_v29_(5),_p265-273`                                        |              1 | [PW:0000206](http://purl.obolibrary.org/obo/PW_0000206)                                                          |
| `PubMed:Science,_2002,_v296,_p1564-7`                                         |              1 | [PW:0000210](http://purl.obolibrary.org/obo/PW_0000210)                                                          |
| `PubMed:Nature_Reviews,_Mol._Cell_Biology,_2001,_v2,_p369-77.`                |              1 | [PW:0000231](http://purl.obolibrary.org/obo/PW_0000231)                                                          |
| `PubMed:Annu._Rev._Neursci._2003,_v26,_701-28.`                               |              1 | [PW:0000274](http://purl.obolibrary.org/obo/PW_0000274)                                                          |
| `PubMed:Several_articles`                                                     |              1 | [PW:0000668](http://purl.obolibrary.org/obo/PW_0000668)                                                          |

## `PW`: Pathway ontology

Overall, there were 8 invalid
xrefs to external prefixed with `PW` (standardized to Bioregistry
prefix [`pw`](https://bioregistry.io/pw)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                      |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PW:InHouse`    |              5 | [PW:0000287](http://purl.obolibrary.org/obo/PW_0000287), [PW:0000288](http://purl.obolibrary.org/obo/PW_0000288), [PW:0000292](http://purl.obolibrary.org/obo/PW_0000292), [PW:0000293](http://purl.obolibrary.org/obo/PW_0000293), [PW:0000300](http://purl.obolibrary.org/obo/PW_0000300) |
| `PW:Inhouse`    |              2 | [PW:0000289](http://purl.obolibrary.org/obo/PW_0000289), [PW:0000290](http://purl.obolibrary.org/obo/PW_0000290)                                                                                                                                                                            |
| `PW:InHouse3`   |              1 | [PW:0000298](http://purl.obolibrary.org/obo/PW_0000298)                                                                                                                                                                                                                                     |

## `Reactome`: Reactome

Overall, there were 8 invalid
xrefs to external prefixed with `Reactome` (standardized to Bioregistry
prefix [`reactome`](https://bioregistry.io/reactome)) that
did not match the standard pattern `^R-[A-Z]{3}-\d+(-\d+)?(\.\d+)?$`.

| external_xref            |   usages_count | usages                                                  |
|--------------------------|----------------|---------------------------------------------------------|
| `Reactome:REACT_11061.4` |              1 | [PW:0000169](http://purl.obolibrary.org/obo/PW_0000169) |
| `Reactome:REACT_15380.1` |              1 | [PW:0000176](http://purl.obolibrary.org/obo/PW_0000176) |
| `Reactome:REACT_11045.1` |              1 | [PW:0000201](http://purl.obolibrary.org/obo/PW_0000201) |
| `Reactome:REACT_14820.1` |              1 | [PW:0000211](http://purl.obolibrary.org/obo/PW_0000211) |
| `Reactome:REACT_1208.1`  |              1 | [PW:0000304](http://purl.obolibrary.org/obo/PW_0000304) |
| `Reactome:REACT_13705.1` |              1 | [PW:0000375](http://purl.obolibrary.org/obo/PW_0000375) |
| `Reactome:REACT_15530.1` |              1 | [PW:0000543](http://purl.obolibrary.org/obo/PW_0000543) |
| `Reactome:REACT_212.3`   |              1 | [PW:0000554](http://purl.obolibrary.org/obo/PW_0000554) |

## `RGD`: Rat Genome Database

Overall, there were 4 invalid
xrefs to external prefixed with `RGD` (standardized to Bioregistry
prefix [`rgd`](https://bioregistry.io/rgd)) that
did not match the standard pattern `^\d{4,}$`.

| external_xref            |   usages_count | usages                                                                                                                                                                    |
|--------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RGD:InHouse_dictionary` |              3 | [PW:0000332](http://purl.obolibrary.org/obo/PW_0000332), [PW:0000646](http://purl.obolibrary.org/obo/PW_0000646), [PW:0000683](http://purl.obolibrary.org/obo/PW_0000683) |
| `RGD:InHouse`            |              1 | [PW:0000684](http://purl.obolibrary.org/obo/PW_0000684)                                                                                                                   |

## `SMP`: Small Molecule Pathway Database

Overall, there were 68 invalid
xrefs to external prefixed with `SMP` (standardized to Bioregistry
prefix [`smpdb`](https://bioregistry.io/smpdb)) that
did not match the standard pattern `^SMP\d+$`.

| external_xref   |   usages_count | usages                                                                                                           |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `SMP:00445`     |              2 | [PW:0000216](http://purl.obolibrary.org/obo/PW_0000216), [PW:0000396](http://purl.obolibrary.org/obo/PW_0000396) |
| `SMP:00018`     |              2 | [PW:0000523](http://purl.obolibrary.org/obo/PW_0000523), [PW:0001158](http://purl.obolibrary.org/obo/PW_0001158) |
| `SMP:00057`     |              1 | [PW:0000026](http://purl.obolibrary.org/obo/PW_0000026)                                                          |
| `SMP:00456`     |              1 | [PW:0000029](http://purl.obolibrary.org/obo/PW_0000029)                                                          |
| `SMP:00050`     |              1 | [PW:0000031](http://purl.obolibrary.org/obo/PW_0000031)                                                          |
| `SMP:00046`     |              1 | [PW:0000032](http://purl.obolibrary.org/obo/PW_0000032)                                                          |
| `SMP:00355`     |              1 | [PW:0000034](http://purl.obolibrary.org/obo/PW_0000034)                                                          |
| `SMP:00035`     |              1 | [PW:0000039](http://purl.obolibrary.org/obo/PW_0000039)                                                          |
| `SMP:00130`     |              1 | [PW:0000040](http://purl.obolibrary.org/obo/PW_0000040)                                                          |
| `SMP:00043`     |              1 | [PW:0000042](http://purl.obolibrary.org/obo/PW_0000042)                                                          |
| `SMP:00060`     |              1 | [PW:0000043](http://purl.obolibrary.org/obo/PW_0000043)                                                          |
| `SMP:00031`     |              1 | [PW:0000045](http://purl.obolibrary.org/obo/PW_0000045)                                                          |
| `SMP:00011`     |              1 | [PW:0000046](http://purl.obolibrary.org/obo/PW_0000046)                                                          |
| `SMP:00013`     |              1 | [PW:0000049](http://purl.obolibrary.org/obo/PW_0000049)                                                          |
| `SMP:00044`     |              1 | [PW:0000051](http://purl.obolibrary.org/obo/PW_0000051)                                                          |
| `SMP:00006`     |              1 | [PW:0000052](http://purl.obolibrary.org/obo/PW_0000052)                                                          |
| `SMP:00063`     |              1 | [PW:0000054](http://purl.obolibrary.org/obo/PW_0000054)                                                          |
| `SMP:00051`     |              1 | [PW:0000058](http://purl.obolibrary.org/obo/PW_0000058)                                                          |
| `SMP:00016`     |              1 | [PW:0000064](http://purl.obolibrary.org/obo/PW_0000064)                                                          |
| `SMP:00073`     |              1 | [PW:0000065](http://purl.obolibrary.org/obo/PW_0000065)                                                          |
| `SMP:00071`     |              1 | [PW:0000069](http://purl.obolibrary.org/obo/PW_0000069)                                                          |
| `SMP:00032`     |              1 | [PW:0000071](http://purl.obolibrary.org/obo/PW_0000071)                                                          |
| `SMP:00037`     |              1 | [PW:0000073](http://purl.obolibrary.org/obo/PW_0000073)                                                          |
| `SMP:00059`     |              1 | [PW:0000076](http://purl.obolibrary.org/obo/PW_0000076)                                                          |
| `SMP:00007`     |              1 | [PW:0000077](http://purl.obolibrary.org/obo/PW_0000077)                                                          |
| `SMP:00478`     |              1 | [PW:0000130](http://purl.obolibrary.org/obo/PW_0000130)                                                          |
| `SMP:00029`     |              1 | [PW:0000133](http://purl.obolibrary.org/obo/PW_0000133)                                                          |
| `SMP:00015`     |              1 | [PW:0000134](http://purl.obolibrary.org/obo/PW_0000134)                                                          |
| `SMP:00070`     |              1 | [PW:0000137](http://purl.obolibrary.org/obo/PW_0000137)                                                          |
| `SMP:00017`     |              1 | [PW:0000138](http://purl.obolibrary.org/obo/PW_0000138)                                                          |
| `SMP:00066`     |              1 | [PW:0000139](http://purl.obolibrary.org/obo/PW_0000139)                                                          |
| `SMP:00053`     |              1 | [PW:0000140](http://purl.obolibrary.org/obo/PW_0000140)                                                          |
| `SMP:00074`     |              1 | [PW:0000141](http://purl.obolibrary.org/obo/PW_0000141)                                                          |
| `SMP:00065`     |              1 | [PW:0000142](http://purl.obolibrary.org/obo/PW_0000142)                                                          |
| `SMP:00391`     |              1 | [PW:0000143](http://purl.obolibrary.org/obo/PW_0000143)                                                          |
| `SMP:00045`     |              1 | [PW:0000152](http://purl.obolibrary.org/obo/PW_0000152)                                                          |
| `SMP:00462`     |              1 | [PW:0000154](http://purl.obolibrary.org/obo/PW_0000154)                                                          |
| `SMP:00027`     |              1 | [PW:0000167](http://purl.obolibrary.org/obo/PW_0000167)                                                          |
| `SMP:00034`     |              1 | [PW:0000197](http://purl.obolibrary.org/obo/PW_0000197)                                                          |
| `SMP:00025`     |              1 | [PW:0000354](http://purl.obolibrary.org/obo/PW_0000354)                                                          |
| `SMP:00055`     |              1 | [PW:0000438](http://purl.obolibrary.org/obo/PW_0000438)                                                          |
| `SMP:00023`     |              1 | [PW:0000454](http://purl.obolibrary.org/obo/PW_0000454)                                                          |
| `SMP:00075`     |              1 | [PW:0000460](http://purl.obolibrary.org/obo/PW_0000460)                                                          |
| `SMP:00040`     |              1 | [PW:0000640](http://purl.obolibrary.org/obo/PW_0000640)                                                          |
| `SMP:00128`     |              1 | [PW:0000641](http://purl.obolibrary.org/obo/PW_0000641)                                                          |
| `SMP:00048`     |              1 | [PW:0001010](http://purl.obolibrary.org/obo/PW_0001010)                                                          |
| `SMP:00464`     |              1 | [PW:0001016](http://purl.obolibrary.org/obo/PW_0001016)                                                          |
| `SMP:00338`     |              1 | [PW:0001070](http://purl.obolibrary.org/obo/PW_0001070)                                                          |
| `SMP:00333`     |              1 | [PW:0001071](http://purl.obolibrary.org/obo/PW_0001071)                                                          |
| `SMP:00054`     |              1 | [PW:0001136](http://purl.obolibrary.org/obo/PW_0001136)                                                          |
| `SMP:00039`     |              1 | [PW:0001156](http://purl.obolibrary.org/obo/PW_0001156)                                                          |
| `SMP:00012`     |              1 | [PW:0001235](http://purl.obolibrary.org/obo/PW_0001235)                                                          |
| `SMP:00467`     |              1 | [PW:0001300](http://purl.obolibrary.org/obo/PW_0001300)                                                          |
| `SMP:00457`     |              1 | [PW:0001364](http://purl.obolibrary.org/obo/PW_0001364)                                                          |
| `SMP:00206`     |              1 | [PW:0001805](http://purl.obolibrary.org/obo/PW_0001805)                                                          |
| `SMP:00479`     |              1 | [PW:0001877](http://purl.obolibrary.org/obo/PW_0001877)                                                          |
| `SMP:00374`     |              1 | [PW:0001992](http://purl.obolibrary.org/obo/PW_0001992)                                                          |
| `SMP:00581`     |              1 | [PW:0001992](http://purl.obolibrary.org/obo/PW_0001992)                                                          |
| `SMP:00573`     |              1 | [PW:0001993](http://purl.obolibrary.org/obo/PW_0001993)                                                          |
| `SMP:00554`     |              1 | [PW:0001995](http://purl.obolibrary.org/obo/PW_0001995)                                                          |
| `SMP:00444`     |              1 | [PW:0002072](http://purl.obolibrary.org/obo/PW_0002072)                                                          |
| `SMP:00182`     |              1 | [PW:0002092](http://purl.obolibrary.org/obo/PW_0002092)                                                          |
| `SMP:00496`     |              1 | [PW:0002093](http://purl.obolibrary.org/obo/PW_0002093)                                                          |
| `SMP:00725`     |              1 | [PW:0002101](http://purl.obolibrary.org/obo/PW_0002101)                                                          |
| `SMP:00024`     |              1 | [PW:0002285](http://purl.obolibrary.org/obo/PW_0002285)                                                          |
| `SMP:00465`     |              1 | [PW:0002292](http://purl.obolibrary.org/obo/PW_0002292)                                                          |

