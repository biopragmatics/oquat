# peco

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `peco`. See the [GitHub repository](https://github.com/Planteome/plant-experimental-conditions-ontology).


## `CAS`: CAS Chemical Registry

Overall, there were 66 invalid
xrefs to external prefixed with `CAS` (standardized to Bioregistry
prefix [`cas`](https://bioregistry.io/cas)) that
did not match the standard pattern `^\d{1,7}\-\d{2}\-\d$`.

| external_xref                 |   usages_count | usages                                                                                                                                                                                 |
|-------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CAS:('CAS', '[2514-83-2]')`  |              2 | [http://purl.obolibrary.org/obo/PECO_0007506](http://purl.obolibrary.org/obo/PECO_0007506), [http://purl.obolibrary.org/obo/PECO_0007510](http://purl.obolibrary.org/obo/PECO_0007510) |
| `CAS:('CAS', '[505-60-2]')`   |              2 | [http://purl.obolibrary.org/obo/PECO_0007552](http://purl.obolibrary.org/obo/PECO_0007552), [http://purl.obolibrary.org/obo/PECO_0007570](http://purl.obolibrary.org/obo/PECO_0007570) |
| `CAS:('CAS', '[68-87-3]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007204](http://purl.obolibrary.org/obo/PECO_0007204)                                                                                             |
| `CAS:('CAS', '[106-93-4]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007503](http://purl.obolibrary.org/obo/PECO_0007503)                                                                                             |
| `CAS:('CAS', '[107-06-2]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007504](http://purl.obolibrary.org/obo/PECO_0007504)                                                                                             |
| `CAS:('CAS', '[53-70-3]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007505](http://purl.obolibrary.org/obo/PECO_0007505)                                                                                             |
| `CAS:('CAS', '[2917-96-6]')`  |              1 | [http://purl.obolibrary.org/obo/PECO_0007507](http://purl.obolibrary.org/obo/PECO_0007507)                                                                                             |
| `CAS:('CAS', '[55-98-1]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007508](http://purl.obolibrary.org/obo/PECO_0007508)                                                                                             |
| `CAS:('CAS', '[1187-00-4]')`  |              1 | [http://purl.obolibrary.org/obo/PECO_0007509](http://purl.obolibrary.org/obo/PECO_0007509)                                                                                             |
| `CAS:('CAS', '[116-63-2]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007511](http://purl.obolibrary.org/obo/PECO_0007511)                                                                                             |
| `CAS:('CAS', '[107-04-0]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007512](http://purl.obolibrary.org/obo/PECO_0007512)                                                                                             |
| `CAS:('CAS', '[479-50-5]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007513](http://purl.obolibrary.org/obo/PECO_0007513)                                                                                             |
| `CAS:('CAS', '[526-62-5]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007514](http://purl.obolibrary.org/obo/PECO_0007514)                                                                                             |
| `CAS:('CAS', '[3570-58-9]')`  |              1 | [http://purl.obolibrary.org/obo/PECO_0007515](http://purl.obolibrary.org/obo/PECO_0007515)                                                                                             |
| `CAS:('CAS', '[461-31-4]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007516](http://purl.obolibrary.org/obo/PECO_0007516)                                                                                             |
| `CAS:('CAS', '[109-86-4]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007517](http://purl.obolibrary.org/obo/PECO_0007517)                                                                                             |
| `CAS:('CAS', '[51-20-7]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007518](http://purl.obolibrary.org/obo/PECO_0007518)                                                                                             |
| `CAS:('CAS', '[957-75-5]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007519](http://purl.obolibrary.org/obo/PECO_0007519)                                                                                             |
| `CAS:('CAS', '[16238-56-5]')` |              1 | [http://purl.obolibrary.org/obo/PECO_0007520](http://purl.obolibrary.org/obo/PECO_0007520)                                                                                             |
| `CAS:('CAS', '[50-76-0]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007521](http://purl.obolibrary.org/obo/PECO_0007521)                                                                                             |
| `CAS:('CAS', '[54-62-6]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007522](http://purl.obolibrary.org/obo/PECO_0007522)                                                                                             |
| `CAS:('CAS', '[50-32-8]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007523](http://purl.obolibrary.org/obo/PECO_0007523)                                                                                             |
| `CAS:('CAS', '[58-08-2]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007524](http://purl.obolibrary.org/obo/PECO_0007524)                                                                                             |
| `CAS:('CAS', '[15663-27-1]')` |              1 | [http://purl.obolibrary.org/obo/PECO_0007525](http://purl.obolibrary.org/obo/PECO_0007525)                                                                                             |
| `CAS:('CAS', '[64-86-8]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007526](http://purl.obolibrary.org/obo/PECO_0007526)                                                                                             |
| `CAS:('CAS', '[7758-98-7]')`  |              1 | [http://purl.obolibrary.org/obo/PECO_0007527](http://purl.obolibrary.org/obo/PECO_0007527)                                                                                             |
| `CAS:('CAS', '[1464-53-5]')`  |              1 | [http://purl.obolibrary.org/obo/PECO_0007528](http://purl.obolibrary.org/obo/PECO_0007528)                                                                                             |
| `CAS:('CAS', '[2426-07-5]')`  |              1 | [http://purl.obolibrary.org/obo/PECO_0007529](http://purl.obolibrary.org/obo/PECO_0007529)                                                                                             |
| `CAS:('CAS', '[64-67-5]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007530](http://purl.obolibrary.org/obo/PECO_0007530)                                                                                             |
| `CAS:('CAS', '[67-68-5]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007531](http://purl.obolibrary.org/obo/PECO_0007531)                                                                                             |
| `CAS:('CAS', '[9007-49-2]')`  |              1 | [http://purl.obolibrary.org/obo/PECO_0007532](http://purl.obolibrary.org/obo/PECO_0007532)                                                                                             |
| `CAS:('CAS', '[60-29-7]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007533](http://purl.obolibrary.org/obo/PECO_0007533)                                                                                             |
| `CAS:('CAS', '[62-50-0]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007534](http://purl.obolibrary.org/obo/PECO_0007534)                                                                                             |
| `CAS:('CAS', '[759-73-9]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007535](http://purl.obolibrary.org/obo/PECO_0007535)                                                                                             |
| `CAS:('CAS', '[151-56-4]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007537](http://purl.obolibrary.org/obo/PECO_0007537)                                                                                             |
| `CAS:('CAS', '[50-00-0]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007539](http://purl.obolibrary.org/obo/PECO_0007539)                                                                                             |
| `CAS:('CAS', '[520-26-3]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007541](http://purl.obolibrary.org/obo/PECO_0007541)                                                                                             |
| `CAS:('CAS', '[645-05-6]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007542](http://purl.obolibrary.org/obo/PECO_0007542)                                                                                             |
| `CAS:('CAS', '[680-31-9]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007543](http://purl.obolibrary.org/obo/PECO_0007543)                                                                                             |
| `CAS:('CAS', '[23255-93-8]')` |              1 | [http://purl.obolibrary.org/obo/PECO_0007544](http://purl.obolibrary.org/obo/PECO_0007544)                                                                                             |
| `CAS:('CAS', '[4213-45-0]')`  |              1 | [http://purl.obolibrary.org/obo/PECO_0007545](http://purl.obolibrary.org/obo/PECO_0007545)                                                                                             |
| `CAS:('CAS', '[146-59-8]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007546](http://purl.obolibrary.org/obo/PECO_0007546)                                                                                             |
| `CAS:('CAS', '[7553-56-2]')`  |              1 | [http://purl.obolibrary.org/obo/PECO_0007547](http://purl.obolibrary.org/obo/PECO_0007547)                                                                                             |
| `CAS:('CAS', '[2869-83-2]')`  |              1 | [http://purl.obolibrary.org/obo/PECO_0007548](http://purl.obolibrary.org/obo/PECO_0007548)                                                                                             |
| `CAS:('CAS', '[66-27-3]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007550](http://purl.obolibrary.org/obo/PECO_0007550)                                                                                             |
| `CAS:('CAS', '[50-07-7]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007551](http://purl.obolibrary.org/obo/PECO_0007551)                                                                                             |
| `CAS:('CAS', '[70-25-7]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007553](http://purl.obolibrary.org/obo/PECO_0007553)                                                                                             |
| `CAS:('CAS', '[62-75-9]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007554](http://purl.obolibrary.org/obo/PECO_0007554)                                                                                             |
| `CAS:('CAS', '[51-75-2]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007556](http://purl.obolibrary.org/obo/PECO_0007556)                                                                                             |
| `CAS:('CAS', '[684-93-5]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007557](http://purl.obolibrary.org/obo/PECO_0007557)                                                                                             |
| `CAS:('CAS', '[64508-90-3]')` |              1 | [http://purl.obolibrary.org/obo/PECO_0007558](http://purl.obolibrary.org/obo/PECO_0007558)                                                                                             |
| `CAS:('CAS', '[13045-94-8]')` |              1 | [http://purl.obolibrary.org/obo/PECO_0007559](http://purl.obolibrary.org/obo/PECO_0007559)                                                                                             |
| `CAS:('CAS', '[148-82-3]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007560](http://purl.obolibrary.org/obo/PECO_0007560)                                                                                             |
| `CAS:('CAS', '[305-03-3]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007562](http://purl.obolibrary.org/obo/PECO_0007562)                                                                                             |
| `CAS:('CAS', '[58880-18-5]')` |              1 | [http://purl.obolibrary.org/obo/PECO_0007563](http://purl.obolibrary.org/obo/PECO_0007563)                                                                                             |
| `CAS:('CAS', '[857-95-4]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007564](http://purl.obolibrary.org/obo/PECO_0007564)                                                                                             |
| `CAS:('CAS', '[106-34-3]')`   |              1 | [http://purl.obolibrary.org/obo/PECO_0007565](http://purl.obolibrary.org/obo/PECO_0007565)                                                                                             |
| `CAS:('CAS', '[28361-96-8]')` |              1 | [http://purl.obolibrary.org/obo/PECO_0007566](http://purl.obolibrary.org/obo/PECO_0007566)                                                                                             |
| `CAS:('CAS', '[7631-90-5]')`  |              1 | [http://purl.obolibrary.org/obo/PECO_0007567](http://purl.obolibrary.org/obo/PECO_0007567)                                                                                             |
| `CAS:('CAS', '[7681-49-4]')`  |              1 | [http://purl.obolibrary.org/obo/PECO_0007568](http://purl.obolibrary.org/obo/PECO_0007568)                                                                                             |
| `CAS:('CAS', '[68-76-8]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007571](http://purl.obolibrary.org/obo/PECO_0007571)                                                                                             |
| `CAS:('CAS', '[51-18-3]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007572](http://purl.obolibrary.org/obo/PECO_0007572)                                                                                             |
| `CAS:('CAS', '[51-79-6]')`    |              1 | [http://purl.obolibrary.org/obo/PECO_0007573](http://purl.obolibrary.org/obo/PECO_0007573)                                                                                             |
| `CAS:('CAS', '[15805-73-9]')` |              1 | [http://purl.obolibrary.org/obo/PECO_0007574](http://purl.obolibrary.org/obo/PECO_0007574)                                                                                             |

## `PECO`: Plant Experimental Conditions Ontology

Overall, there were 103 invalid
xrefs to external prefixed with `PECO` (standardized to Bioregistry
prefix [`peco`](https://bioregistry.io/peco)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                    |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PECO:('PECO', 'cooperl')`       |            100 | [http://purl.obolibrary.org/obo/PECO_0001001](http://purl.obolibrary.org/obo/PECO_0001001), [http://purl.obolibrary.org/obo/PECO_0001002](http://purl.obolibrary.org/obo/PECO_0001002), [http://purl.obolibrary.org/obo/PECO_0001003](http://purl.obolibrary.org/obo/PECO_0001003), [http://purl.obolibrary.org/obo/PECO_0001004](http://purl.obolibrary.org/obo/PECO_0001004), [http://purl.obolibrary.org/obo/PECO_0001005](http://purl.obolibrary.org/obo/PECO_0001005), ... |
| `PECO:('PECO', 'laura_moore')`   |              2 | [http://purl.obolibrary.org/obo/PECO_0001058](http://purl.obolibrary.org/obo/PECO_0001058), [http://purl.obolibrary.org/obo/PECO_0001059](http://purl.obolibrary.org/obo/PECO_0001059)                                                                                                                                                                                                                                                                                          |
| `PECO:('PECO', 'Laurel_Cooper')` |              1 | [http://purl.obolibrary.org/obo/PECO_0001063](http://purl.obolibrary.org/obo/PECO_0001063)                                                                                                                                                                                                                                                                                                                                                                                      |

## `PO`: Plant Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `PO` (standardized to Bioregistry
prefix [`po`](https://bioregistry.io/po)) that
did not match the standard pattern `^\d+$`.

| external_xref          |   usages_count | usages                                                                                     |
|------------------------|----------------|--------------------------------------------------------------------------------------------|
| `PO:('PO', 'Cooperl')` |              1 | [http://purl.obolibrary.org/obo/PECO_0007407](http://purl.obolibrary.org/obo/PECO_0007407) |

## `TO`: Plant Trait Ontology

Overall, there were 11 invalid
xrefs to external prefixed with `TO` (standardized to Bioregistry
prefix [`to`](https://bioregistry.io/to)) that
did not match the standard pattern `^\d{7}$`.

| external_xref         |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TO:('TO', 'moorel')` |             11 | [http://purl.obolibrary.org/obo/PECO_0007041](http://purl.obolibrary.org/obo/PECO_0007041), [http://purl.obolibrary.org/obo/PECO_0007063](http://purl.obolibrary.org/obo/PECO_0007063), [http://purl.obolibrary.org/obo/PECO_0007168](http://purl.obolibrary.org/obo/PECO_0007168), [http://purl.obolibrary.org/obo/PECO_0007287](http://purl.obolibrary.org/obo/PECO_0007287), [http://purl.obolibrary.org/obo/PECO_0007292](http://purl.obolibrary.org/obo/PECO_0007292), ... |

