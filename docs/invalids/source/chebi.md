# chebi

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `chebi`. See the [GitHub repository](https://github.com/ebi-chebi/ChEBI).


## `AGR`: Agricultural Online Access

Overall, there were 5 invalid
xrefs to external prefixed with `AGR` (standardized to Bioregistry
prefix [`agricola`](https://bioregistry.io/agricola)) that
did not match the standard pattern `^IND\d+$`.

| external_xref     |   usages_count | usages                                                    |
|-------------------|----------------|-----------------------------------------------------------|
| `AGR:FNI91003265` |              1 | [CHEBI:16409](http://purl.obolibrary.org/obo/CHEBI_16409) |
| `AGR:ADL87012489` |              1 | [CHEBI:17382](http://purl.obolibrary.org/obo/CHEBI_17382) |
| `AGR:GUA85013620` |              1 | [CHEBI:52127](http://purl.obolibrary.org/obo/CHEBI_52127) |
| `AGR:GUA85008832` |              1 | [CHEBI:82052](http://purl.obolibrary.org/obo/CHEBI_82052) |
| `AGR:ADL89034377` |              1 | [CHEBI:82843](http://purl.obolibrary.org/obo/CHEBI_82843) |

## `CAS`: CAS Registry Number

Overall, there were 10 invalid
xrefs to external prefixed with `CAS` (standardized to Bioregistry
prefix [`cas`](https://bioregistry.io/cas)) that
did not match the standard pattern `^\d{1,7}\-\d{2}\-\d$`.

| external_xref    |   usages_count | usages                                                      |
|------------------|----------------|-------------------------------------------------------------|
| `CAS:3/7/4767`   |              1 | [CHEBI:177432](http://purl.obolibrary.org/obo/CHEBI_177432) |
| `CAS:02/08/2547` |              1 | [CHEBI:189017](http://purl.obolibrary.org/obo/CHEBI_189017) |
| `CAS:9/7/2957`   |              1 | [CHEBI:189177](http://purl.obolibrary.org/obo/CHEBI_189177) |
| `CAS:5/9/2016`   |              1 | [CHEBI:189236](http://purl.obolibrary.org/obo/CHEBI_189236) |
| `CAS:5/2/5297`   |              1 | [CHEBI:189931](http://purl.obolibrary.org/obo/CHEBI_189931) |
| `CAS:4/1/5623`   |              1 | [CHEBI:190963](http://purl.obolibrary.org/obo/CHEBI_190963) |
| `CAS:4/8/2004`   |              1 | [CHEBI:191094](http://purl.obolibrary.org/obo/CHEBI_191094) |
| `CAS:03/07/5452` |              1 | [CHEBI:191497](http://purl.obolibrary.org/obo/CHEBI_191497) |
| `CAS:6/5/7780`   |              1 | [CHEBI:191626](http://purl.obolibrary.org/obo/CHEBI_191626) |
| `CAS:03/04/6099` |              1 | [CHEBI:192607](http://purl.obolibrary.org/obo/CHEBI_192607) |

## `ChemIDplus`: ChemIDplus

Overall, there were 33 invalid
xrefs to external prefixed with `ChemIDplus` (standardized to Bioregistry
prefix [`chemidplus`](https://bioregistry.io/chemidplus)) that
did not match the standard pattern `^\d+\-\d+\-\d+$`.

| external_xref           |   usages_count | usages                                                      |
|-------------------------|----------------|-------------------------------------------------------------|
| `ChemIDplus:0035891726` |              1 | [CHEBI:156361](http://purl.obolibrary.org/obo/CHEBI_156361) |
| `ChemIDplus:9589606`    |              1 | [CHEBI:189649](http://purl.obolibrary.org/obo/CHEBI_189649) |
| `ChemIDplus:11981715`   |              1 | [CHEBI:189650](http://purl.obolibrary.org/obo/CHEBI_189650) |
| `ChemIDplus:121427831`  |              1 | [CHEBI:189651](http://purl.obolibrary.org/obo/CHEBI_189651) |
| `ChemIDplus:122201421`  |              1 | [CHEBI:189652](http://purl.obolibrary.org/obo/CHEBI_189652) |
| `ChemIDplus:146047984`  |              1 | [CHEBI:189655](http://purl.obolibrary.org/obo/CHEBI_189655) |
| `ChemIDplus:137076847`  |              1 | [CHEBI:189661](http://purl.obolibrary.org/obo/CHEBI_189661) |
| `ChemIDplus:135048952`  |              1 | [CHEBI:195326](http://purl.obolibrary.org/obo/CHEBI_195326) |
| `ChemIDplus:0142632335` |              1 | [CHEBI:65555](http://purl.obolibrary.org/obo/CHEBI_65555)   |
| `ChemIDplus:0027593233` |              1 | [CHEBI:66729](http://purl.obolibrary.org/obo/CHEBI_66729)   |
| `ChemIDplus:0192214576` |              1 | [CHEBI:67337](http://purl.obolibrary.org/obo/CHEBI_67337)   |
| `ChemIDplus:0006426433` |              1 | [CHEBI:67438](http://purl.obolibrary.org/obo/CHEBI_67438)   |
| `ChemIDplus:0000698102` |              1 | [CHEBI:67940](http://purl.obolibrary.org/obo/CHEBI_67940)   |
| `ChemIDplus:0136565667` |              1 | [CHEBI:67969](http://purl.obolibrary.org/obo/CHEBI_67969)   |
| `ChemIDplus:0001058613` |              1 | [CHEBI:68105](http://purl.obolibrary.org/obo/CHEBI_68105)   |
| `ChemIDplus:0077327050` |              1 | [CHEBI:68856](http://purl.obolibrary.org/obo/CHEBI_68856)   |
| `ChemIDplus:0117710039` |              1 | [CHEBI:68857](http://purl.obolibrary.org/obo/CHEBI_68857)   |
| `ChemIDplus:0143651450` |              1 | [CHEBI:68888](http://purl.obolibrary.org/obo/CHEBI_68888)   |
| `ChemIDplus:0006801407` |              1 | [CHEBI:68906](http://purl.obolibrary.org/obo/CHEBI_68906)   |
| `ChemIDplus:0023778349` |              1 | [CHEBI:69060](http://purl.obolibrary.org/obo/CHEBI_69060)   |
| `ChemIDplus:0000112390` |              1 | [CHEBI:69187](http://purl.obolibrary.org/obo/CHEBI_69187)   |
| `ChemIDplus:0000112618` |              1 | [CHEBI:69188](http://purl.obolibrary.org/obo/CHEBI_69188)   |
| `ChemIDplus:0051103572` |              1 | [CHEBI:69276](http://purl.obolibrary.org/obo/CHEBI_69276)   |
| `ChemIDplus:0157695368` |              1 | [CHEBI:69277](http://purl.obolibrary.org/obo/CHEBI_69277)   |
| `ChemIDplus:0000118718` |              1 | [CHEBI:69438](http://purl.obolibrary.org/obo/CHEBI_69438)   |
| `ChemIDplus:0000150765` |              1 | [CHEBI:69441](http://purl.obolibrary.org/obo/CHEBI_69441)   |
| `ChemIDplus:0001197097` |              1 | [CHEBI:69446](http://purl.obolibrary.org/obo/CHEBI_69446)   |
| `ChemIDplus:0138590600` |              1 | [CHEBI:69599](http://purl.obolibrary.org/obo/CHEBI_69599)   |
| `ChemIDplus:0000102374` |              1 | [CHEBI:69656](http://purl.obolibrary.org/obo/CHEBI_69656)   |
| `ChemIDplus:0001617681` |              1 | [CHEBI:69744](http://purl.obolibrary.org/obo/CHEBI_69744)   |
| `ChemIDplus:0050439684` |              1 | [CHEBI:70074](http://purl.obolibrary.org/obo/CHEBI_70074)   |
| `ChemIDplus:0123871272` |              1 | [CHEBI:70426](http://purl.obolibrary.org/obo/CHEBI_70426)   |
| `ChemIDplus:0006835990` |              1 | [CHEBI:70504](http://purl.obolibrary.org/obo/CHEBI_70504)   |

## `DrugBank`: DrugBank

Overall, there were 83 invalid
xrefs to external prefixed with `DrugBank` (standardized to Bioregistry
prefix [`drugbank`](https://bioregistry.io/drugbank)) that
did not match the standard pattern `^DB\d{5}$`.

| external_xref           |   usages_count | usages                                                      |
|-------------------------|----------------|-------------------------------------------------------------|
| `DrugBank:DBSALT002523` |              1 | [CHEBI:136001](http://purl.obolibrary.org/obo/CHEBI_136001) |
| `DrugBank:DBSALT002417` |              1 | [CHEBI:140115](http://purl.obolibrary.org/obo/CHEBI_140115) |
| `DrugBank:DBSALT002144` |              1 | [CHEBI:145421](http://purl.obolibrary.org/obo/CHEBI_145421) |
| `DrugBank:DBSALT001097` |              1 | [CHEBI:145568](http://purl.obolibrary.org/obo/CHEBI_145568) |
| `DrugBank:DBSALT003375` |              1 | [CHEBI:147356](http://purl.obolibrary.org/obo/CHEBI_147356) |
| `DrugBank:DBSALT002168` |              1 | [CHEBI:149534](http://purl.obolibrary.org/obo/CHEBI_149534) |
| `DrugBank:DBSALT001664` |              1 | [CHEBI:149566](http://purl.obolibrary.org/obo/CHEBI_149566) |
| `DrugBank:DBSALT001310` |              1 | [CHEBI:157785](http://purl.obolibrary.org/obo/CHEBI_157785) |
| `DrugBank:DBSALT002064` |              1 | [CHEBI:172948](http://purl.obolibrary.org/obo/CHEBI_172948) |
| `DrugBank:DBSALT002077` |              1 | [CHEBI:172961](http://purl.obolibrary.org/obo/CHEBI_172961) |
| `DrugBank:DBSALT002581` |              1 | [CHEBI:173081](http://purl.obolibrary.org/obo/CHEBI_173081) |
| `DrugBank:DBSALT000855` |              1 | [CHEBI:17616](http://purl.obolibrary.org/obo/CHEBI_17616)   |
| `DrugBank:DBSALT001293` |              1 | [CHEBI:176786](http://purl.obolibrary.org/obo/CHEBI_176786) |
| `DrugBank:DBSALT002842` |              1 | [CHEBI:176853](http://purl.obolibrary.org/obo/CHEBI_176853) |
| `DrugBank:DBSALT003136` |              1 | [CHEBI:177382](http://purl.obolibrary.org/obo/CHEBI_177382) |
| `DrugBank:DBSALT002498` |              1 | [CHEBI:177871](http://purl.obolibrary.org/obo/CHEBI_177871) |
| `DrugBank:DBSALT000316` |              1 | [CHEBI:180473](http://purl.obolibrary.org/obo/CHEBI_180473) |
| `DrugBank:DBSALT002973` |              1 | [CHEBI:180502](http://purl.obolibrary.org/obo/CHEBI_180502) |
| `DrugBank:DBSALT002497` |              1 | [CHEBI:18290](http://purl.obolibrary.org/obo/CHEBI_18290)   |
| `DrugBank:DBSALT001276` |              1 | [CHEBI:189695](http://purl.obolibrary.org/obo/CHEBI_189695) |
| `DrugBank:DBSALT000142` |              1 | [CHEBI:191940](http://purl.obolibrary.org/obo/CHEBI_191940) |
| `DrugBank:DBSALT003251` |              1 | [CHEBI:194301](http://purl.obolibrary.org/obo/CHEBI_194301) |
| `DrugBank:DBSALT003444` |              1 | [CHEBI:229224](http://purl.obolibrary.org/obo/CHEBI_229224) |
| `DrugBank:DBSALT003430` |              1 | [CHEBI:229231](http://purl.obolibrary.org/obo/CHEBI_229231) |
| `DrugBank:DBSALT003482` |              1 | [CHEBI:229234](http://purl.obolibrary.org/obo/CHEBI_229234) |
| `DrugBank:DBSALT003190` |              1 | [CHEBI:229544](http://purl.obolibrary.org/obo/CHEBI_229544) |
| `DrugBank:DBSALT003479` |              1 | [CHEBI:229644](http://purl.obolibrary.org/obo/CHEBI_229644) |
| `DrugBank:DBSALT002148` |              1 | [CHEBI:229646](http://purl.obolibrary.org/obo/CHEBI_229646) |
| `DrugBank:DBSALT003336` |              1 | [CHEBI:229650](http://purl.obolibrary.org/obo/CHEBI_229650) |
| `DrugBank:DBSALT003493` |              1 | [CHEBI:229654](http://purl.obolibrary.org/obo/CHEBI_229654) |
| `DrugBank:DBSALT000417` |              1 | [CHEBI:230519](http://purl.obolibrary.org/obo/CHEBI_230519) |
| `DrugBank:DBSALT003496` |              1 | [CHEBI:231335](http://purl.obolibrary.org/obo/CHEBI_231335) |
| `DrugBank:DBSALT001499` |              1 | [CHEBI:2911](http://purl.obolibrary.org/obo/CHEBI_2911)     |
| `DrugBank:DBSALT000151` |              1 | [CHEBI:30961](http://purl.obolibrary.org/obo/CHEBI_30961)   |
| `DrugBank:DBSALT002914` |              1 | [CHEBI:31347](http://purl.obolibrary.org/obo/CHEBI_31347)   |
| `DrugBank:DBSALT001147` |              1 | [CHEBI:31398](http://purl.obolibrary.org/obo/CHEBI_31398)   |
| `DrugBank:DBSALT000964` |              1 | [CHEBI:31460](http://purl.obolibrary.org/obo/CHEBI_31460)   |
| `DrugBank:DBSALT002618` |              1 | [CHEBI:31490](http://purl.obolibrary.org/obo/CHEBI_31490)   |
| `DrugBank:DBSALT002399` |              1 | [CHEBI:31593](http://purl.obolibrary.org/obo/CHEBI_31593)   |
| `DrugBank:DBSALT000301` |              1 | [CHEBI:31602](http://purl.obolibrary.org/obo/CHEBI_31602)   |
| `DrugBank:DBSALT001312` |              1 | [CHEBI:31704](http://purl.obolibrary.org/obo/CHEBI_31704)   |
| `DrugBank:DBSALT001240` |              1 | [CHEBI:31795](http://purl.obolibrary.org/obo/CHEBI_31795)   |
| `DrugBank:DBSALT002585` |              1 | [CHEBI:32123](http://purl.obolibrary.org/obo/CHEBI_32123)   |
| `DrugBank:DBSALT001517` |              1 | [CHEBI:32146](http://purl.obolibrary.org/obo/CHEBI_32146)   |
| `DrugBank:DBSALT002505` |              1 | [CHEBI:32150](http://purl.obolibrary.org/obo/CHEBI_32150)   |
| `DrugBank:DBSALT000883` |              1 | [CHEBI:32270](http://purl.obolibrary.org/obo/CHEBI_32270)   |
| `DrugBank:DBSALT002650` |              1 | [CHEBI:33283](http://purl.obolibrary.org/obo/CHEBI_33283)   |
| `DrugBank:DBSALT000891` |              1 | [CHEBI:34850](http://purl.obolibrary.org/obo/CHEBI_34850)   |
| `DrugBank:DBSALT001049` |              1 | [CHEBI:34858](http://purl.obolibrary.org/obo/CHEBI_34858)   |
| `DrugBank:DBSALT001898` |              1 | [CHEBI:4471](http://purl.obolibrary.org/obo/CHEBI_4471)     |
| `DrugBank:DBSALT001948` |              1 | [CHEBI:4709](http://purl.obolibrary.org/obo/CHEBI_4709)     |
| `DrugBank:DBSALT000503` |              1 | [CHEBI:48566](http://purl.obolibrary.org/obo/CHEBI_48566)   |
| `DrugBank:DBSALT001761` |              1 | [CHEBI:48843](http://purl.obolibrary.org/obo/CHEBI_48843)   |
| `DrugBank:DBSALT000205` |              1 | [CHEBI:49105](http://purl.obolibrary.org/obo/CHEBI_49105)   |
| `DrugBank:DBSALT000011` |              1 | [CHEBI:50686](http://purl.obolibrary.org/obo/CHEBI_50686)   |
| `DrugBank:DBSALT000721` |              1 | [CHEBI:50697](http://purl.obolibrary.org/obo/CHEBI_50697)   |
| `DrugBank:DBSALT000776` |              1 | [CHEBI:5124](http://purl.obolibrary.org/obo/CHEBI_5124)     |
| `DrugBank:DBSALT001419` |              1 | [CHEBI:51241](http://purl.obolibrary.org/obo/CHEBI_51241)   |
| `DrugBank:DBSALT000868` |              1 | [CHEBI:51255](http://purl.obolibrary.org/obo/CHEBI_51255)   |
| `DrugBank:DBSALT000064` |              1 | [CHEBI:53509](http://purl.obolibrary.org/obo/CHEBI_53509)   |
| `DrugBank:DBSALT000889` |              1 | [CHEBI:5556](http://purl.obolibrary.org/obo/CHEBI_5556)     |
| `DrugBank:DBSALT000347` |              1 | [CHEBI:58987](http://purl.obolibrary.org/obo/CHEBI_58987)   |
| `DrugBank:DBSALT002877` |              1 | [CHEBI:64103](http://purl.obolibrary.org/obo/CHEBI_64103)   |
| `DrugBank:DBSALT000251` |              1 | [CHEBI:6439](http://purl.obolibrary.org/obo/CHEBI_6439)     |
| `DrugBank:DBSALT002747` |              1 | [CHEBI:65242](http://purl.obolibrary.org/obo/CHEBI_65242)   |
| `DrugBank:DBSALT000019` |              1 | [CHEBI:652822](http://purl.obolibrary.org/obo/CHEBI_652822) |
| `DrugBank:DBSALT000152` |              1 | [CHEBI:68602](http://purl.obolibrary.org/obo/CHEBI_68602)   |
| `DrugBank:DBSALT000016` |              1 | [CHEBI:72295](http://purl.obolibrary.org/obo/CHEBI_72295)   |
| `DrugBank:DBSALT002404` |              1 | [CHEBI:75316](http://purl.obolibrary.org/obo/CHEBI_75316)   |
| `DrugBank:DBSALT000499` |              1 | [CHEBI:7551](http://purl.obolibrary.org/obo/CHEBI_7551)     |
| `DrugBank:DBSALT000641` |              1 | [CHEBI:7641](http://purl.obolibrary.org/obo/CHEBI_7641)     |
| `DrugBank:DBSALT002430` |              1 | [CHEBI:77635](http://purl.obolibrary.org/obo/CHEBI_77635)   |
| `DrugBank:DBSALT000314` |              1 | [CHEBI:79401](http://purl.obolibrary.org/obo/CHEBI_79401)   |
| `DrugBank:DBSALT000132` |              1 | [CHEBI:7944](http://purl.obolibrary.org/obo/CHEBI_7944)     |
| `DrugBank:DBSALT002445` |              1 | [CHEBI:8021](http://purl.obolibrary.org/obo/CHEBI_8021)     |
| `DrugBank:DBSALT001123` |              1 | [CHEBI:81711](http://purl.obolibrary.org/obo/CHEBI_81711)   |
| `DrugBank:DBSALT000785` |              1 | [CHEBI:8379](http://purl.obolibrary.org/obo/CHEBI_8379)     |
| `DrugBank:DBSALT000427` |              1 | [CHEBI:8462](http://purl.obolibrary.org/obo/CHEBI_8462)     |
| `DrugBank:DBSALT000772` |              1 | [CHEBI:86158](http://purl.obolibrary.org/obo/CHEBI_86158)   |
| `DrugBank:DBSALT003069` |              1 | [CHEBI:91243](http://purl.obolibrary.org/obo/CHEBI_91243)   |
| `DrugBank:DBSALT000540` |              1 | [CHEBI:9364](http://purl.obolibrary.org/obo/CHEBI_9364)     |
| `DrugBank:DBSALT001254` |              1 | [CHEBI:9492](http://purl.obolibrary.org/obo/CHEBI_9492)     |
| `DrugBank:DBSALT001257` |              1 | [CHEBI:9925](http://purl.obolibrary.org/obo/CHEBI_9925)     |

## `Gmelin`: Gmelins Handbuch der anorganischen Chemie

Overall, there were 27 invalid
xrefs to external prefixed with `Gmelin` (standardized to Bioregistry
prefix [`gmelin`](https://bioregistry.io/gmelin)) that
did not match the standard pattern `^[1-9][0-9]{2,6}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `Gmelin:79`     |              1 | [CHEBI:16134](http://purl.obolibrary.org/obo/CHEBI_16134) |
| `Gmelin:59`     |              1 | [CHEBI:16183](http://purl.obolibrary.org/obo/CHEBI_16183) |
| `Gmelin:89`     |              1 | [CHEBI:17514](http://purl.obolibrary.org/obo/CHEBI_17514) |
| `Gmelin:3`      |              1 | [CHEBI:18276](http://purl.obolibrary.org/obo/CHEBI_18276) |
| `Gmelin:84`     |              1 | [CHEBI:28938](http://purl.obolibrary.org/obo/CHEBI_28938) |
| `Gmelin:18`     |              1 | [CHEBI:29294](http://purl.obolibrary.org/obo/CHEBI_29294) |
| `Gmelin:16`     |              1 | [CHEBI:29298](http://purl.obolibrary.org/obo/CHEBI_29298) |
| `Gmelin:88`     |              1 | [CHEBI:29306](http://purl.obolibrary.org/obo/CHEBI_29306) |
| `Gmelin:57`     |              1 | [CHEBI:29309](http://purl.obolibrary.org/obo/CHEBI_29309) |
| `Gmelin:66`     |              1 | [CHEBI:29339](http://purl.obolibrary.org/obo/CHEBI_29339) |
| `Gmelin:56`     |              1 | [CHEBI:29357](http://purl.obolibrary.org/obo/CHEBI_29357) |
| `Gmelin:80`     |              1 | [CHEBI:29421](http://purl.obolibrary.org/obo/CHEBI_29421) |
| `Gmelin:44`     |              1 | [CHEBI:30149](http://purl.obolibrary.org/obo/CHEBI_30149) |
| `Gmelin:45`     |              1 | [CHEBI:30153](http://purl.obolibrary.org/obo/CHEBI_30153) |
| `Gmelin:47`     |              1 | [CHEBI:30157](http://purl.obolibrary.org/obo/CHEBI_30157) |
| `Gmelin:40`     |              1 | [CHEBI:33605](http://purl.obolibrary.org/obo/CHEBI_33605) |
| `Gmelin:39`     |              1 | [CHEBI:33606](http://purl.obolibrary.org/obo/CHEBI_33606) |
| `Gmelin:41`     |              1 | [CHEBI:33607](http://purl.obolibrary.org/obo/CHEBI_33607) |
| `Gmelin:49`     |              1 | [CHEBI:33682](http://purl.obolibrary.org/obo/CHEBI_33682) |
| `Gmelin:50`     |              1 | [CHEBI:33684](http://purl.obolibrary.org/obo/CHEBI_33684) |
| `Gmelin:48`     |              1 | [CHEBI:33685](http://purl.obolibrary.org/obo/CHEBI_33685) |
| `Gmelin:2`      |              1 | [CHEBI:33688](http://purl.obolibrary.org/obo/CHEBI_33688) |
| `Gmelin:1`      |              1 | [CHEBI:33689](http://purl.obolibrary.org/obo/CHEBI_33689) |
| `Gmelin:28`     |              1 | [CHEBI:33787](http://purl.obolibrary.org/obo/CHEBI_33787) |
| `Gmelin:29`     |              1 | [CHEBI:33789](http://purl.obolibrary.org/obo/CHEBI_33789) |
| `Gmelin:33`     |              1 | [CHEBI:38983](http://purl.obolibrary.org/obo/CHEBI_38983) |
| `Gmelin:97`     |              1 | [CHEBI:41981](http://purl.obolibrary.org/obo/CHEBI_41981) |

## `LIPID_MAPS_class`: LIPID MAPS

Overall, there were 10 invalid
xrefs to external prefixed with `LIPID_MAPS_class` (standardized to Bioregistry
prefix [`lipidmaps`](https://bioregistry.io/lipidmaps)) that
did not match the standard pattern `^LM(FA|GL|GP|SP|ST|PR|SL|PK)[0-9]{4}([0-9a-zA-Z]{4,6})?$`.

| external_xref             |   usages_count | usages                                                      |
|---------------------------|----------------|-------------------------------------------------------------|
| `LIPID_MAPS_class:LMSL01` |              1 | [CHEBI:157764](http://purl.obolibrary.org/obo/CHEBI_157764) |
| `LIPID_MAPS_class:LMST01` |              1 | [CHEBI:15889](http://purl.obolibrary.org/obo/CHEBI_15889)   |
| `LIPID_MAPS_class:LMSP02` |              1 | [CHEBI:17761](http://purl.obolibrary.org/obo/CHEBI_17761)   |
| `LIPID_MAPS_class:LMFA03` |              1 | [CHEBI:23899](http://purl.obolibrary.org/obo/CHEBI_23899)   |
| `LIPID_MAPS_class:LMFA05` |              1 | [CHEBI:24026](http://purl.obolibrary.org/obo/CHEBI_24026)   |
| `LIPID_MAPS_class:LMPR01` |              1 | [CHEBI:24913](http://purl.obolibrary.org/obo/CHEBI_24913)   |
| `LIPID_MAPS_class:LMFA08` |              1 | [CHEBI:29348](http://purl.obolibrary.org/obo/CHEBI_29348)   |
| `LIPID_MAPS_class:LMSP01` |              1 | [CHEBI:35785](http://purl.obolibrary.org/obo/CHEBI_35785)   |
| `LIPID_MAPS_class:LMST04` |              1 | [CHEBI:36078](http://purl.obolibrary.org/obo/CHEBI_36078)   |
| `LIPID_MAPS_class:LMGP12` |              1 | [CHEBI:76529](http://purl.obolibrary.org/obo/CHEBI_76529)   |

## `MetaCyc`: Metabolic Encyclopedia of metabolic and other pathways

Overall, there were 1 invalid
xrefs to external prefixed with `MetaCyc` (standardized to Bioregistry
prefix [`metacyc.compound`](https://bioregistry.io/metacyc.compound)) that
did not match the standard pattern `^[A-Za-z0-9+_.%-:]+$`.

| external_xref                                                                                 |   usages_count | usages                                                      |
|-----------------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------|
| `MetaCyc:(1<arrow>right</arrow>4)-6-phospho-<stereo>alpha</stereo>-<stereo>D</stereo>-glucan` |              1 | [CHEBI:134068](http://purl.obolibrary.org/obo/CHEBI_134068) |

## `PDBeChem`: Chemical Component Dictionary

Overall, there were 37 invalid
xrefs to external prefixed with `PDBeChem` (standardized to Bioregistry
prefix [`pdb-ccd`](https://bioregistry.io/pdb-ccd)) that
did not match the standard pattern `^\w{1,3}$`.

| external_xref                                                            |   usages_count | usages                                                      |
|--------------------------------------------------------------------------|----------------|-------------------------------------------------------------|
| `PDBeChem:LEU_LFOH`                                                      |              1 | [CHEBI:15603](http://purl.obolibrary.org/obo/CHEBI_15603)   |
| `PDBeChem:DAH_LFOH`                                                      |              1 | [CHEBI:15765](http://purl.obolibrary.org/obo/CHEBI_15765)   |
| `PDBeChem:GLU_LFOH`                                                      |              1 | [CHEBI:16015](http://purl.obolibrary.org/obo/CHEBI_16015)   |
| `PDBeChem:MET_LL`                                                        |              1 | [CHEBI:16044](http://purl.obolibrary.org/obo/CHEBI_16044)   |
| `PDBeChem:ArF00`                                                         |              1 | [CHEBI:16335](http://purl.obolibrary.org/obo/CHEBI_16335)   |
| `PDBeChem:ArS00`                                                         |              1 | [CHEBI:16335](http://purl.obolibrary.org/obo/CHEBI_16335)   |
| `PDBeChem:MET_LFOH`                                                      |              1 | [CHEBI:16643](http://purl.obolibrary.org/obo/CHEBI_16643)   |
| `PDBeChem:U5PrF10`                                                       |              1 | [CHEBI:16695](http://purl.obolibrary.org/obo/CHEBI_16695)   |
| `PDBeChem:UrF10`                                                         |              1 | [CHEBI:16695](http://purl.obolibrary.org/obo/CHEBI_16695)   |
| `PDBeChem:ALA_LFOH`                                                      |              1 | [CHEBI:16977](http://purl.obolibrary.org/obo/CHEBI_16977)   |
| `PDBeChem:TMPdF10`                                                       |              1 | [CHEBI:17013](http://purl.obolibrary.org/obo/CHEBI_17013)   |
| `PDBeChem:TdF10`                                                         |              1 | [CHEBI:17013](http://purl.obolibrary.org/obo/CHEBI_17013)   |
| `PDBeChem:OCS_LFOH`                                                      |              1 | [CHEBI:17285](http://purl.obolibrary.org/obo/CHEBI_17285)   |
| `PDBeChem:https://pubchem.ncbi.nlm.nih.gov/compound/Magnesium-phosphate` |              1 | [CHEBI:190298](http://purl.obolibrary.org/obo/CHEBI_190298) |
| `PDBeChem:https://pubchem.ncbi.nlm.nih.gov/compound/Selenium_-ion_4`     |              1 | [CHEBI:190426](http://purl.obolibrary.org/obo/CHEBI_190426) |
| `PDBeChem:138392202`                                                     |              1 | [CHEBI:190523](http://purl.obolibrary.org/obo/CHEBI_190523) |
| `PDBeChem:102186966`                                                     |              1 | [CHEBI:190524](http://purl.obolibrary.org/obo/CHEBI_190524) |
| `PDBeChem:https://pubchem.ncbi.nlm.nih.gov/substance/163311886`          |              1 | [CHEBI:192503](http://purl.obolibrary.org/obo/CHEBI_192503) |
| `PDBeChem:1501865`                                                       |              1 | [CHEBI:232453](http://purl.obolibrary.org/obo/CHEBI_232453) |
| `PDBeChem:661578`                                                        |              1 | [CHEBI:233083](http://purl.obolibrary.org/obo/CHEBI_233083) |
| `PDBeChem:CID 7210`                                                      |              1 | [CHEBI:233502](http://purl.obolibrary.org/obo/CHEBI_233502) |
| `PDBeChem:GLY_LL`                                                        |              1 | [CHEBI:29947](http://purl.obolibrary.org/obo/CHEBI_29947)   |
| `PDBeChem:ORN_LFOH`                                                      |              1 | [CHEBI:44667](http://purl.obolibrary.org/obo/CHEBI_44667)   |
| `PDBeChem:ALA_LL`                                                        |              1 | [CHEBI:46217](http://purl.obolibrary.org/obo/CHEBI_46217)   |
| `PDBeChem:GLY_LEO2`                                                      |              1 | [CHEBI:46738](http://purl.obolibrary.org/obo/CHEBI_46738)   |
| `PDBeChem:GLY_LSN3`                                                      |              1 | [CHEBI:46740](http://purl.obolibrary.org/obo/CHEBI_46740)   |
| `PDBeChem:GLU_LEO2`                                                      |              1 | [CHEBI:46854](http://purl.obolibrary.org/obo/CHEBI_46854)   |
| `PDBeChem:GLU_LSN3`                                                      |              1 | [CHEBI:46855](http://purl.obolibrary.org/obo/CHEBI_46855)   |
| `PDBeChem:TYR_LEO2`                                                      |              1 | [CHEBI:46857](http://purl.obolibrary.org/obo/CHEBI_46857)   |
| `PDBeChem:TYR_LL`                                                        |              1 | [CHEBI:46858](http://purl.obolibrary.org/obo/CHEBI_46858)   |
| `PDBeChem:MET_LEO2`                                                      |              1 | [CHEBI:49037](http://purl.obolibrary.org/obo/CHEBI_49037)   |
| `PDBeChem:MET_LSN3`                                                      |              1 | [CHEBI:49038](http://purl.obolibrary.org/obo/CHEBI_49038)   |
| `PDBeChem:PRO_LL`                                                        |              1 | [CHEBI:50342](http://purl.obolibrary.org/obo/CHEBI_50342)   |
| `PDBeChem:ASN_LL`                                                        |              1 | [CHEBI:50347](http://purl.obolibrary.org/obo/CHEBI_50347)   |
| `PDBeChem:ASN_LSN3`                                                      |              1 | [CHEBI:50348](http://purl.obolibrary.org/obo/CHEBI_50348)   |
| `PDBeChem:303E`                                                          |              1 | [CHEBI:63871](http://purl.obolibrary.org/obo/CHEBI_63871)   |
| `PDBeChem:triazoxide`                                                    |              1 | [CHEBI:83335](http://purl.obolibrary.org/obo/CHEBI_83335)   |

## `SMID`: C. elegans Small Molecule Identifier Database

Overall, there were 150 invalid
xrefs to external prefixed with `SMID` (standardized to Bioregistry
prefix [`smid`](https://bioregistry.io/smid)) that
did not match the standard pattern `^\d+$`.

| external_xref       |   usages_count | usages                                                    |
|---------------------|----------------|-----------------------------------------------------------|
| `SMID:ascr%2311%0D` |              1 | [CHEBI:78743](http://purl.obolibrary.org/obo/CHEBI_78743) |
| `SMID:icas%2320%0D` |              1 | [CHEBI:78745](http://purl.obolibrary.org/obo/CHEBI_78745) |
| `SMID:ascr%231%0D`  |              1 | [CHEBI:78786](http://purl.obolibrary.org/obo/CHEBI_78786) |
| `SMID:ascr%232%0D`  |              1 | [CHEBI:78812](http://purl.obolibrary.org/obo/CHEBI_78812) |
| `SMID:ascr%233`     |              1 | [CHEBI:78821](http://purl.obolibrary.org/obo/CHEBI_78821) |
| `SMID:ascr%234`     |              1 | [CHEBI:78828](http://purl.obolibrary.org/obo/CHEBI_78828) |
| `SMID:ascr%235%0D`  |              1 | [CHEBI:78829](http://purl.obolibrary.org/obo/CHEBI_78829) |
| `SMID:ascr%237%0D`  |              1 | [CHEBI:78830](http://purl.obolibrary.org/obo/CHEBI_78830) |
| `SMID:ascr%238%0D`  |              1 | [CHEBI:78834](http://purl.obolibrary.org/obo/CHEBI_78834) |
| `SMID:ascr%2310%0D` |              1 | [CHEBI:78838](http://purl.obolibrary.org/obo/CHEBI_78838) |
| `SMID:ascr%2312%0D` |              1 | [CHEBI:78841](http://purl.obolibrary.org/obo/CHEBI_78841) |
| `SMID:ascr%2313%0D` |              1 | [CHEBI:78851](http://purl.obolibrary.org/obo/CHEBI_78851) |
| `SMID:ascr%2315%0D` |              1 | [CHEBI:78852](http://purl.obolibrary.org/obo/CHEBI_78852) |
| `SMID:ascr%2314%0D` |              1 | [CHEBI:78905](http://purl.obolibrary.org/obo/CHEBI_78905) |
| `SMID:ascr%2316%0D` |              1 | [CHEBI:78950](http://purl.obolibrary.org/obo/CHEBI_78950) |
| `SMID:ascr%2317%0D` |              1 | [CHEBI:78952](http://purl.obolibrary.org/obo/CHEBI_78952) |
| `SMID:ascr%2318%0D` |              1 | [CHEBI:78955](http://purl.obolibrary.org/obo/CHEBI_78955) |
| `SMID:ascr%2319%0D` |              1 | [CHEBI:78957](http://purl.obolibrary.org/obo/CHEBI_78957) |
| `SMID:ascr%2320%0D` |              1 | [CHEBI:78958](http://purl.obolibrary.org/obo/CHEBI_78958) |
| `SMID:ascr%2321%0D` |              1 | [CHEBI:78959](http://purl.obolibrary.org/obo/CHEBI_78959) |
| `SMID:ascr%2322%0D` |              1 | [CHEBI:78960](http://purl.obolibrary.org/obo/CHEBI_78960) |
| `SMID:ascr%2323%0D` |              1 | [CHEBI:78961](http://purl.obolibrary.org/obo/CHEBI_78961) |
| `SMID:ascr%2324%0D` |              1 | [CHEBI:78962](http://purl.obolibrary.org/obo/CHEBI_78962) |
| `SMID:ascr%2325%0D` |              1 | [CHEBI:78963](http://purl.obolibrary.org/obo/CHEBI_78963) |
| `SMID:ascr%2326%0D` |              1 | [CHEBI:78964](http://purl.obolibrary.org/obo/CHEBI_78964) |
| `SMID:ascr%2327%0D` |              1 | [CHEBI:78965](http://purl.obolibrary.org/obo/CHEBI_78965) |
| `SMID:ascr%2328%0D` |              1 | [CHEBI:78966](http://purl.obolibrary.org/obo/CHEBI_78966) |
| `SMID:ascr%2329%0D` |              1 | [CHEBI:78967](http://purl.obolibrary.org/obo/CHEBI_78967) |
| `SMID:ascr%2330%0D` |              1 | [CHEBI:78968](http://purl.obolibrary.org/obo/CHEBI_78968) |
| `SMID:ascr%2331%0D` |              1 | [CHEBI:78969](http://purl.obolibrary.org/obo/CHEBI_78969) |
| `SMID:ascr%2332%0D` |              1 | [CHEBI:78970](http://purl.obolibrary.org/obo/CHEBI_78970) |
| `SMID:ascr%2333%0D` |              1 | [CHEBI:78971](http://purl.obolibrary.org/obo/CHEBI_78971) |
| `SMID:ascr%2334%0D` |              1 | [CHEBI:78972](http://purl.obolibrary.org/obo/CHEBI_78972) |
| `SMID:ascr%2335%0D` |              1 | [CHEBI:78973](http://purl.obolibrary.org/obo/CHEBI_78973) |
| `SMID:ascr%2336%0D` |              1 | [CHEBI:78974](http://purl.obolibrary.org/obo/CHEBI_78974) |
| `SMID:ascr%2337%0D` |              1 | [CHEBI:78975](http://purl.obolibrary.org/obo/CHEBI_78975) |
| `SMID:ascr%2338%0D` |              1 | [CHEBI:78976](http://purl.obolibrary.org/obo/CHEBI_78976) |
| `SMID:ascr%239%0D`  |              1 | [CHEBI:79018](http://purl.obolibrary.org/obo/CHEBI_79018) |
| `SMID:icas%237%0D`  |              1 | [CHEBI:79023](http://purl.obolibrary.org/obo/CHEBI_79023) |
| `SMID:icas%239%0D`  |              1 | [CHEBI:79028](http://purl.obolibrary.org/obo/CHEBI_79028) |
| `SMID:icas%2310%0D` |              1 | [CHEBI:79029](http://purl.obolibrary.org/obo/CHEBI_79029) |
| `SMID:icas%231%0D`  |              1 | [CHEBI:79051](http://purl.obolibrary.org/obo/CHEBI_79051) |
| `SMID:icas%233%0D`  |              1 | [CHEBI:79052](http://purl.obolibrary.org/obo/CHEBI_79052) |
| `SMID:icas%2312%0D` |              1 | [CHEBI:79060](http://purl.obolibrary.org/obo/CHEBI_79060) |
| `SMID:icas%2314%0D` |              1 | [CHEBI:79061](http://purl.obolibrary.org/obo/CHEBI_79061) |
| `SMID:icas%2315%0D` |              1 | [CHEBI:79062](http://purl.obolibrary.org/obo/CHEBI_79062) |
| `SMID:icas%2316%0D` |              1 | [CHEBI:79094](http://purl.obolibrary.org/obo/CHEBI_79094) |
| `SMID:icas%2317%0D` |              1 | [CHEBI:79104](http://purl.obolibrary.org/obo/CHEBI_79104) |
| `SMID:icas%2318%0D` |              1 | [CHEBI:79105](http://purl.obolibrary.org/obo/CHEBI_79105) |
| `SMID:icas%2319%0D` |              1 | [CHEBI:79106](http://purl.obolibrary.org/obo/CHEBI_79106) |
| `SMID:icas%2321%0D` |              1 | [CHEBI:79107](http://purl.obolibrary.org/obo/CHEBI_79107) |
| `SMID:icas%2322%0D` |              1 | [CHEBI:79108](http://purl.obolibrary.org/obo/CHEBI_79108) |
| `SMID:icos%231%0D`  |              1 | [CHEBI:79111](http://purl.obolibrary.org/obo/CHEBI_79111) |
| `SMID:icos%233%0D`  |              1 | [CHEBI:79114](http://purl.obolibrary.org/obo/CHEBI_79114) |
| `SMID:icos%239%0D`  |              1 | [CHEBI:79116](http://purl.obolibrary.org/obo/CHEBI_79116) |
| `SMID:icos%2310%0D` |              1 | [CHEBI:79117](http://purl.obolibrary.org/obo/CHEBI_79117) |
| `SMID:icos%2315%0D` |              1 | [CHEBI:79118](http://purl.obolibrary.org/obo/CHEBI_79118) |
| `SMID:icos%2316%0D` |              1 | [CHEBI:79119](http://purl.obolibrary.org/obo/CHEBI_79119) |
| `SMID:icos%2317`    |              1 | [CHEBI:79120](http://purl.obolibrary.org/obo/CHEBI_79120) |
| `SMID:icos%2318`    |              1 | [CHEBI:79124](http://purl.obolibrary.org/obo/CHEBI_79124) |
| `SMID:mbas%233`     |              1 | [CHEBI:79128](http://purl.obolibrary.org/obo/CHEBI_79128) |
| `SMID:mbas%2310`    |              1 | [CHEBI:79129](http://purl.obolibrary.org/obo/CHEBI_79129) |
| `SMID:oscr%231`     |              1 | [CHEBI:79130](http://purl.obolibrary.org/obo/CHEBI_79130) |
| `SMID:oscr%233`     |              1 | [CHEBI:79131](http://purl.obolibrary.org/obo/CHEBI_79131) |
| `SMID:oscr%237`     |              1 | [CHEBI:79132](http://purl.obolibrary.org/obo/CHEBI_79132) |
| `SMID:oscr%239`     |              1 | [CHEBI:79133](http://purl.obolibrary.org/obo/CHEBI_79133) |
| `SMID:oscr%2310`    |              1 | [CHEBI:79134](http://purl.obolibrary.org/obo/CHEBI_79134) |
| `SMID:oscr%2312`    |              1 | [CHEBI:79135](http://purl.obolibrary.org/obo/CHEBI_79135) |
| `SMID:oscr%2314`    |              1 | [CHEBI:79136](http://purl.obolibrary.org/obo/CHEBI_79136) |
| `SMID:oscr%2315`    |              1 | [CHEBI:79137](http://purl.obolibrary.org/obo/CHEBI_79137) |
| `SMID:oscr%2316`    |              1 | [CHEBI:79138](http://purl.obolibrary.org/obo/CHEBI_79138) |
| `SMID:oscr%2317`    |              1 | [CHEBI:79139](http://purl.obolibrary.org/obo/CHEBI_79139) |
| `SMID:oscr%2318`    |              1 | [CHEBI:79140](http://purl.obolibrary.org/obo/CHEBI_79140) |
| `SMID:oscr%2319`    |              1 | [CHEBI:79141](http://purl.obolibrary.org/obo/CHEBI_79141) |
| `SMID:oscr%2320`    |              1 | [CHEBI:79142](http://purl.obolibrary.org/obo/CHEBI_79142) |
| `SMID:oscr%2321%0D` |              1 | [CHEBI:79143](http://purl.obolibrary.org/obo/CHEBI_79143) |
| `SMID:oscr%2322%0D` |              1 | [CHEBI:79144](http://purl.obolibrary.org/obo/CHEBI_79144) |
| `SMID:oscr%2323`    |              1 | [CHEBI:79145](http://purl.obolibrary.org/obo/CHEBI_79145) |
| `SMID:oscr%2324`    |              1 | [CHEBI:79146](http://purl.obolibrary.org/obo/CHEBI_79146) |
| `SMID:oscr%2325`    |              1 | [CHEBI:79147](http://purl.obolibrary.org/obo/CHEBI_79147) |
| `SMID:oscr%2326`    |              1 | [CHEBI:79148](http://purl.obolibrary.org/obo/CHEBI_79148) |
| `SMID:oscr%2327`    |              1 | [CHEBI:79149](http://purl.obolibrary.org/obo/CHEBI_79149) |
| `SMID:oscr%2328`    |              1 | [CHEBI:79150](http://purl.obolibrary.org/obo/CHEBI_79150) |
| `SMID:oscr%2329`    |              1 | [CHEBI:79151](http://purl.obolibrary.org/obo/CHEBI_79151) |
| `SMID:oscr%2330`    |              1 | [CHEBI:79152](http://purl.obolibrary.org/obo/CHEBI_79152) |
| `SMID:oscr%2331`    |              1 | [CHEBI:79153](http://purl.obolibrary.org/obo/CHEBI_79153) |
| `SMID:oscr%2332%0D` |              1 | [CHEBI:79154](http://purl.obolibrary.org/obo/CHEBI_79154) |
| `SMID:oscr%2333`    |              1 | [CHEBI:79155](http://purl.obolibrary.org/obo/CHEBI_79155) |
| `SMID:oscr%2334`    |              1 | [CHEBI:79156](http://purl.obolibrary.org/obo/CHEBI_79156) |
| `SMID:oscr%2335`    |              1 | [CHEBI:79157](http://purl.obolibrary.org/obo/CHEBI_79157) |
| `SMID:oscr%2336`    |              1 | [CHEBI:79158](http://purl.obolibrary.org/obo/CHEBI_79158) |
| `SMID:oscr%2337`    |              1 | [CHEBI:79159](http://purl.obolibrary.org/obo/CHEBI_79159) |
| `SMID:oscr%2338`    |              1 | [CHEBI:79160](http://purl.obolibrary.org/obo/CHEBI_79160) |
| `SMID:glas%231`     |              1 | [CHEBI:79197](http://purl.obolibrary.org/obo/CHEBI_79197) |
| `SMID:bhas%2310%0D` |              1 | [CHEBI:79223](http://purl.obolibrary.org/obo/CHEBI_79223) |
| `SMID:bhas%2316%0D` |              1 | [CHEBI:79227](http://purl.obolibrary.org/obo/CHEBI_79227) |
| `SMID:bhas%2318%0D` |              1 | [CHEBI:79229](http://purl.obolibrary.org/obo/CHEBI_79229) |
| `SMID:bhas%2320%0D` |              1 | [CHEBI:79230](http://purl.obolibrary.org/obo/CHEBI_79230) |
| `SMID:bhas%2322%0D` |              1 | [CHEBI:79231](http://purl.obolibrary.org/obo/CHEBI_79231) |
| `SMID:bhas%2324%0D` |              1 | [CHEBI:79232](http://purl.obolibrary.org/obo/CHEBI_79232) |
| `SMID:bhas%2326%0D` |              1 | [CHEBI:79233](http://purl.obolibrary.org/obo/CHEBI_79233) |
| `SMID:bhas%2328%0D` |              1 | [CHEBI:79234](http://purl.obolibrary.org/obo/CHEBI_79234) |
| `SMID:bhas%2330%0D` |              1 | [CHEBI:79235](http://purl.obolibrary.org/obo/CHEBI_79235) |
| `SMID:bhas%2332%0D` |              1 | [CHEBI:79236](http://purl.obolibrary.org/obo/CHEBI_79236) |
| `SMID:bhas%2334%0D` |              1 | [CHEBI:79237](http://purl.obolibrary.org/obo/CHEBI_79237) |
| `SMID:bhas%2336%0D` |              1 | [CHEBI:79238](http://purl.obolibrary.org/obo/CHEBI_79238) |
| `SMID:bhas%2338%0D` |              1 | [CHEBI:79239](http://purl.obolibrary.org/obo/CHEBI_79239) |
| `SMID:bhas%2340%0D` |              1 | [CHEBI:79240](http://purl.obolibrary.org/obo/CHEBI_79240) |
| `SMID:bhas%2342%0D` |              1 | [CHEBI:79241](http://purl.obolibrary.org/obo/CHEBI_79241) |
| `SMID:bhos%2310%0D` |              1 | [CHEBI:79256](http://purl.obolibrary.org/obo/CHEBI_79256) |
| `SMID:bhos%2316%0D` |              1 | [CHEBI:79258](http://purl.obolibrary.org/obo/CHEBI_79258) |
| `SMID:bhos%2318%0D` |              1 | [CHEBI:79259](http://purl.obolibrary.org/obo/CHEBI_79259) |
| `SMID:bhos%2320%0D` |              1 | [CHEBI:79260](http://purl.obolibrary.org/obo/CHEBI_79260) |
| `SMID:bhos%2322%0D` |              1 | [CHEBI:79261](http://purl.obolibrary.org/obo/CHEBI_79261) |
| `SMID:bhos%2324%0D` |              1 | [CHEBI:79262](http://purl.obolibrary.org/obo/CHEBI_79262) |
| `SMID:bhos%2326%0D` |              1 | [CHEBI:79263](http://purl.obolibrary.org/obo/CHEBI_79263) |
| `SMID:bhos%2328%0D` |              1 | [CHEBI:79264](http://purl.obolibrary.org/obo/CHEBI_79264) |
| `SMID:bhos%2330`    |              1 | [CHEBI:79265](http://purl.obolibrary.org/obo/CHEBI_79265) |
| `SMID:bhos%2332`    |              1 | [CHEBI:79266](http://purl.obolibrary.org/obo/CHEBI_79266) |
| `SMID:bhos%2334`    |              1 | [CHEBI:79267](http://purl.obolibrary.org/obo/CHEBI_79267) |
| `SMID:bhos%2336`    |              1 | [CHEBI:79268](http://purl.obolibrary.org/obo/CHEBI_79268) |
| `SMID:bhos%2338`    |              1 | [CHEBI:79269](http://purl.obolibrary.org/obo/CHEBI_79269) |
| `SMID:bhos%2340`    |              1 | [CHEBI:79270](http://purl.obolibrary.org/obo/CHEBI_79270) |
| `SMID:bhos%2342`    |              1 | [CHEBI:79271](http://purl.obolibrary.org/obo/CHEBI_79271) |
| `SMID:glas%233`     |              1 | [CHEBI:79300](http://purl.obolibrary.org/obo/CHEBI_79300) |
| `SMID:glas%2310`    |              1 | [CHEBI:79301](http://purl.obolibrary.org/obo/CHEBI_79301) |
| `SMID:glas%2316`    |              1 | [CHEBI:79302](http://purl.obolibrary.org/obo/CHEBI_79302) |
| `SMID:glas%2318`    |              1 | [CHEBI:79303](http://purl.obolibrary.org/obo/CHEBI_79303) |
| `SMID:glas%2320`    |              1 | [CHEBI:79304](http://purl.obolibrary.org/obo/CHEBI_79304) |
| `SMID:glas%2322`    |              1 | [CHEBI:79305](http://purl.obolibrary.org/obo/CHEBI_79305) |
| `SMID:glas%2324`    |              1 | [CHEBI:79306](http://purl.obolibrary.org/obo/CHEBI_79306) |
| `SMID:glas%2326`    |              1 | [CHEBI:79307](http://purl.obolibrary.org/obo/CHEBI_79307) |
| `SMID:hbas%233`     |              1 | [CHEBI:79321](http://purl.obolibrary.org/obo/CHEBI_79321) |
| `SMID:hbas%2310`    |              1 | [CHEBI:79330](http://purl.obolibrary.org/obo/CHEBI_79330) |
| `SMID:ibha%2310`    |              1 | [CHEBI:79334](http://purl.obolibrary.org/obo/CHEBI_79334) |
| `SMID:ibha%2316%0D` |              1 | [CHEBI:79353](http://purl.obolibrary.org/obo/CHEBI_79353) |
| `SMID:ibha%2318`    |              1 | [CHEBI:79354](http://purl.obolibrary.org/obo/CHEBI_79354) |
| `SMID:ibha%2320`    |              1 | [CHEBI:79355](http://purl.obolibrary.org/obo/CHEBI_79355) |
| `SMID:ibha%2322`    |              1 | [CHEBI:79356](http://purl.obolibrary.org/obo/CHEBI_79356) |
| `SMID:ibha%2324`    |              1 | [CHEBI:79357](http://purl.obolibrary.org/obo/CHEBI_79357) |
| `SMID:ibha%2326%0D` |              1 | [CHEBI:79358](http://purl.obolibrary.org/obo/CHEBI_79358) |
| `SMID:ibha%2328%0D` |              1 | [CHEBI:79359](http://purl.obolibrary.org/obo/CHEBI_79359) |
| `SMID:ibha%2330`    |              1 | [CHEBI:79360](http://purl.obolibrary.org/obo/CHEBI_79360) |
| `SMID:ibho%2310`    |              1 | [CHEBI:79370](http://purl.obolibrary.org/obo/CHEBI_79370) |
| `SMID:ibho%2316`    |              1 | [CHEBI:79371](http://purl.obolibrary.org/obo/CHEBI_79371) |
| `SMID:ibho%2318`    |              1 | [CHEBI:79372](http://purl.obolibrary.org/obo/CHEBI_79372) |
| `SMID:ibho%2320%0D` |              1 | [CHEBI:79373](http://purl.obolibrary.org/obo/CHEBI_79373) |
| `SMID:ibho%2322`    |              1 | [CHEBI:79374](http://purl.obolibrary.org/obo/CHEBI_79374) |
| `SMID:ibho%2324`    |              1 | [CHEBI:79375](http://purl.obolibrary.org/obo/CHEBI_79375) |
| `SMID:ibho%2326`    |              1 | [CHEBI:79376](http://purl.obolibrary.org/obo/CHEBI_79376) |

