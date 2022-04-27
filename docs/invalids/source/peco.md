# peco

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `peco`. See the [GitHub repository](https://github.com/Planteome/plant-experimental-conditions-ontology).


## `CAS`: CAS Chemical Registry

Overall, there were 66 invalid
xrefs to external prefixed with `CAS` (standardized to Bioregistry
prefix [`cas`](https://bioregistry.io/cas)) that
did not match the standard pattern `^\d{1,7}\-\d{2}\-\d$`.

| external_xref                 |   usages_count | usages                                                                                                   |
|-------------------------------|----------------|----------------------------------------------------------------------------------------------------------|
| `CAS:('CAS', '[2514-83-2]')`  |              2 | [PECO:0007506](https://bioregistry.io/PECO:0007506), [PECO:0007510](https://bioregistry.io/PECO:0007510) |
| `CAS:('CAS', '[505-60-2]')`   |              2 | [PECO:0007552](https://bioregistry.io/PECO:0007552), [PECO:0007570](https://bioregistry.io/PECO:0007570) |
| `CAS:('CAS', '[68-87-3]')`    |              1 | [PECO:0007204](https://bioregistry.io/PECO:0007204)                                                      |
| `CAS:('CAS', '[106-93-4]')`   |              1 | [PECO:0007503](https://bioregistry.io/PECO:0007503)                                                      |
| `CAS:('CAS', '[107-06-2]')`   |              1 | [PECO:0007504](https://bioregistry.io/PECO:0007504)                                                      |
| `CAS:('CAS', '[53-70-3]')`    |              1 | [PECO:0007505](https://bioregistry.io/PECO:0007505)                                                      |
| `CAS:('CAS', '[2917-96-6]')`  |              1 | [PECO:0007507](https://bioregistry.io/PECO:0007507)                                                      |
| `CAS:('CAS', '[55-98-1]')`    |              1 | [PECO:0007508](https://bioregistry.io/PECO:0007508)                                                      |
| `CAS:('CAS', '[1187-00-4]')`  |              1 | [PECO:0007509](https://bioregistry.io/PECO:0007509)                                                      |
| `CAS:('CAS', '[116-63-2]')`   |              1 | [PECO:0007511](https://bioregistry.io/PECO:0007511)                                                      |
| `CAS:('CAS', '[107-04-0]')`   |              1 | [PECO:0007512](https://bioregistry.io/PECO:0007512)                                                      |
| `CAS:('CAS', '[479-50-5]')`   |              1 | [PECO:0007513](https://bioregistry.io/PECO:0007513)                                                      |
| `CAS:('CAS', '[526-62-5]')`   |              1 | [PECO:0007514](https://bioregistry.io/PECO:0007514)                                                      |
| `CAS:('CAS', '[3570-58-9]')`  |              1 | [PECO:0007515](https://bioregistry.io/PECO:0007515)                                                      |
| `CAS:('CAS', '[461-31-4]')`   |              1 | [PECO:0007516](https://bioregistry.io/PECO:0007516)                                                      |
| `CAS:('CAS', '[109-86-4]')`   |              1 | [PECO:0007517](https://bioregistry.io/PECO:0007517)                                                      |
| `CAS:('CAS', '[51-20-7]')`    |              1 | [PECO:0007518](https://bioregistry.io/PECO:0007518)                                                      |
| `CAS:('CAS', '[957-75-5]')`   |              1 | [PECO:0007519](https://bioregistry.io/PECO:0007519)                                                      |
| `CAS:('CAS', '[16238-56-5]')` |              1 | [PECO:0007520](https://bioregistry.io/PECO:0007520)                                                      |
| `CAS:('CAS', '[50-76-0]')`    |              1 | [PECO:0007521](https://bioregistry.io/PECO:0007521)                                                      |
| `CAS:('CAS', '[54-62-6]')`    |              1 | [PECO:0007522](https://bioregistry.io/PECO:0007522)                                                      |
| `CAS:('CAS', '[50-32-8]')`    |              1 | [PECO:0007523](https://bioregistry.io/PECO:0007523)                                                      |
| `CAS:('CAS', '[58-08-2]')`    |              1 | [PECO:0007524](https://bioregistry.io/PECO:0007524)                                                      |
| `CAS:('CAS', '[15663-27-1]')` |              1 | [PECO:0007525](https://bioregistry.io/PECO:0007525)                                                      |
| `CAS:('CAS', '[64-86-8]')`    |              1 | [PECO:0007526](https://bioregistry.io/PECO:0007526)                                                      |
| `CAS:('CAS', '[7758-98-7]')`  |              1 | [PECO:0007527](https://bioregistry.io/PECO:0007527)                                                      |
| `CAS:('CAS', '[1464-53-5]')`  |              1 | [PECO:0007528](https://bioregistry.io/PECO:0007528)                                                      |
| `CAS:('CAS', '[2426-07-5]')`  |              1 | [PECO:0007529](https://bioregistry.io/PECO:0007529)                                                      |
| `CAS:('CAS', '[64-67-5]')`    |              1 | [PECO:0007530](https://bioregistry.io/PECO:0007530)                                                      |
| `CAS:('CAS', '[67-68-5]')`    |              1 | [PECO:0007531](https://bioregistry.io/PECO:0007531)                                                      |
| `CAS:('CAS', '[9007-49-2]')`  |              1 | [PECO:0007532](https://bioregistry.io/PECO:0007532)                                                      |
| `CAS:('CAS', '[60-29-7]')`    |              1 | [PECO:0007533](https://bioregistry.io/PECO:0007533)                                                      |
| `CAS:('CAS', '[62-50-0]')`    |              1 | [PECO:0007534](https://bioregistry.io/PECO:0007534)                                                      |
| `CAS:('CAS', '[759-73-9]')`   |              1 | [PECO:0007535](https://bioregistry.io/PECO:0007535)                                                      |
| `CAS:('CAS', '[151-56-4]')`   |              1 | [PECO:0007537](https://bioregistry.io/PECO:0007537)                                                      |
| `CAS:('CAS', '[50-00-0]')`    |              1 | [PECO:0007539](https://bioregistry.io/PECO:0007539)                                                      |
| `CAS:('CAS', '[520-26-3]')`   |              1 | [PECO:0007541](https://bioregistry.io/PECO:0007541)                                                      |
| `CAS:('CAS', '[645-05-6]')`   |              1 | [PECO:0007542](https://bioregistry.io/PECO:0007542)                                                      |
| `CAS:('CAS', '[680-31-9]')`   |              1 | [PECO:0007543](https://bioregistry.io/PECO:0007543)                                                      |
| `CAS:('CAS', '[23255-93-8]')` |              1 | [PECO:0007544](https://bioregistry.io/PECO:0007544)                                                      |
| `CAS:('CAS', '[4213-45-0]')`  |              1 | [PECO:0007545](https://bioregistry.io/PECO:0007545)                                                      |
| `CAS:('CAS', '[146-59-8]')`   |              1 | [PECO:0007546](https://bioregistry.io/PECO:0007546)                                                      |
| `CAS:('CAS', '[7553-56-2]')`  |              1 | [PECO:0007547](https://bioregistry.io/PECO:0007547)                                                      |
| `CAS:('CAS', '[2869-83-2]')`  |              1 | [PECO:0007548](https://bioregistry.io/PECO:0007548)                                                      |
| `CAS:('CAS', '[66-27-3]')`    |              1 | [PECO:0007550](https://bioregistry.io/PECO:0007550)                                                      |
| `CAS:('CAS', '[50-07-7]')`    |              1 | [PECO:0007551](https://bioregistry.io/PECO:0007551)                                                      |
| `CAS:('CAS', '[70-25-7]')`    |              1 | [PECO:0007553](https://bioregistry.io/PECO:0007553)                                                      |
| `CAS:('CAS', '[62-75-9]')`    |              1 | [PECO:0007554](https://bioregistry.io/PECO:0007554)                                                      |
| `CAS:('CAS', '[51-75-2]')`    |              1 | [PECO:0007556](https://bioregistry.io/PECO:0007556)                                                      |
| `CAS:('CAS', '[684-93-5]')`   |              1 | [PECO:0007557](https://bioregistry.io/PECO:0007557)                                                      |
| `CAS:('CAS', '[64508-90-3]')` |              1 | [PECO:0007558](https://bioregistry.io/PECO:0007558)                                                      |
| `CAS:('CAS', '[13045-94-8]')` |              1 | [PECO:0007559](https://bioregistry.io/PECO:0007559)                                                      |
| `CAS:('CAS', '[148-82-3]')`   |              1 | [PECO:0007560](https://bioregistry.io/PECO:0007560)                                                      |
| `CAS:('CAS', '[305-03-3]')`   |              1 | [PECO:0007562](https://bioregistry.io/PECO:0007562)                                                      |
| `CAS:('CAS', '[58880-18-5]')` |              1 | [PECO:0007563](https://bioregistry.io/PECO:0007563)                                                      |
| `CAS:('CAS', '[857-95-4]')`   |              1 | [PECO:0007564](https://bioregistry.io/PECO:0007564)                                                      |
| `CAS:('CAS', '[106-34-3]')`   |              1 | [PECO:0007565](https://bioregistry.io/PECO:0007565)                                                      |
| `CAS:('CAS', '[28361-96-8]')` |              1 | [PECO:0007566](https://bioregistry.io/PECO:0007566)                                                      |
| `CAS:('CAS', '[7631-90-5]')`  |              1 | [PECO:0007567](https://bioregistry.io/PECO:0007567)                                                      |
| `CAS:('CAS', '[7681-49-4]')`  |              1 | [PECO:0007568](https://bioregistry.io/PECO:0007568)                                                      |
| `CAS:('CAS', '[68-76-8]')`    |              1 | [PECO:0007571](https://bioregistry.io/PECO:0007571)                                                      |
| `CAS:('CAS', '[51-18-3]')`    |              1 | [PECO:0007572](https://bioregistry.io/PECO:0007572)                                                      |
| `CAS:('CAS', '[51-79-6]')`    |              1 | [PECO:0007573](https://bioregistry.io/PECO:0007573)                                                      |
| `CAS:('CAS', '[15805-73-9]')` |              1 | [PECO:0007574](https://bioregistry.io/PECO:0007574)                                                      |

## `PECO`: Plant Experimental Conditions Ontology

Overall, there were 103 invalid
xrefs to external prefixed with `PECO` (standardized to Bioregistry
prefix [`peco`](https://bioregistry.io/peco)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                    |   usages_count | usages                                                                                                                                                                                                                                                                       |
|----------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PECO:('PECO', 'cooperl')`       |            100 | [PECO:0001001](https://bioregistry.io/PECO:0001001), [PECO:0001002](https://bioregistry.io/PECO:0001002), [PECO:0001003](https://bioregistry.io/PECO:0001003), [PECO:0001004](https://bioregistry.io/PECO:0001004), [PECO:0001005](https://bioregistry.io/PECO:0001005), ... |
| `PECO:('PECO', 'laura_moore')`   |              2 | [PECO:0001058](https://bioregistry.io/PECO:0001058), [PECO:0001059](https://bioregistry.io/PECO:0001059)                                                                                                                                                                     |
| `PECO:('PECO', 'Laurel_Cooper')` |              1 | [PECO:0001063](https://bioregistry.io/PECO:0001063)                                                                                                                                                                                                                          |

## `PO`: Plant Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `PO` (standardized to Bioregistry
prefix [`po`](https://bioregistry.io/po)) that
did not match the standard pattern `^\d+$`.

| external_xref          |   usages_count | usages                                              |
|------------------------|----------------|-----------------------------------------------------|
| `PO:('PO', 'Cooperl')` |              1 | [PECO:0007407](https://bioregistry.io/PECO:0007407) |

## `TO`: Plant Trait Ontology

Overall, there were 11 invalid
xrefs to external prefixed with `TO` (standardized to Bioregistry
prefix [`to`](https://bioregistry.io/to)) that
did not match the standard pattern `^\d{7}$`.

| external_xref         |   usages_count | usages                                                                                                                                                                                                                                                                       |
|-----------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TO:('TO', 'moorel')` |             11 | [PECO:0007041](https://bioregistry.io/PECO:0007041), [PECO:0007063](https://bioregistry.io/PECO:0007063), [PECO:0007168](https://bioregistry.io/PECO:0007168), [PECO:0007287](https://bioregistry.io/PECO:0007287), [PECO:0007292](https://bioregistry.io/PECO:0007292), ... |

