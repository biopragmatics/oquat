# to

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `to`. See the [GitHub repository](https://github.com/Planteome/plant-trait-ontology).


## `EC`: Enzyme Nomenclature

Overall, there were 1 invalid
xrefs to external prefixed with `EC` (standardized to Bioregistry
prefix [`eccode`](https://bioregistry.io/eccode)) that
did not match the standard pattern `^\d{1,2}(\.\d{0,3}){0,3}$`.

| external_xref          |   usages_count | usages                                                                                 |
|------------------------|----------------|----------------------------------------------------------------------------------------|
| `EC:('EC', '3.2.1.-')` |              1 | [http://purl.obolibrary.org/obo/TO_0000336](http://purl.obolibrary.org/obo/TO_0000336) |

## `MaizeGDB`: MaizeGDB Locus

Overall, there were 2 invalid
xrefs to external prefixed with `MaizeGDB` (standardized to Bioregistry
prefix [`maizegdb.locus`](https://bioregistry.io/maizegdb.locus)) that
did not match the standard pattern `^\d+$`.

| external_xref                             |   usages_count | usages                                                                                 |
|-------------------------------------------|----------------|----------------------------------------------------------------------------------------|
| `MaizeGDB:('MaizeGDB', 'Mary_Schaeffer')` |              1 | [http://purl.obolibrary.org/obo/TO_0000935](http://purl.obolibrary.org/obo/TO_0000935) |
| `MaizeGDB:('MaizeGDB', '???')`            |              1 | [http://purl.obolibrary.org/obo/TO_0000923](http://purl.obolibrary.org/obo/TO_0000923) |

## `PATO`: Phenotype And Trait Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `PATO` (standardized to Bioregistry
prefix [`pato`](https://bioregistry.io/pato)) that
did not match the standard pattern `^\d{7}$`.

| external_xref             |   usages_count | usages                                                                                 |
|---------------------------|----------------|----------------------------------------------------------------------------------------|
| `PATO:('PATO', '000014')` |              1 | [http://purl.obolibrary.org/obo/TO_0000486](http://purl.obolibrary.org/obo/TO_0000486) |

## `PO`: Plant Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `PO` (standardized to Bioregistry
prefix [`po`](https://bioregistry.io/po)) that
did not match the standard pattern `^\d+$`.

| external_xref          |   usages_count | usages                                                                                                                                                                                                                                                                 |
|------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PO:('PO', 'cooperl')` |              3 | [http://purl.obolibrary.org/obo/TO_0000906](http://purl.obolibrary.org/obo/TO_0000906), [http://purl.obolibrary.org/obo/TO_0000908](http://purl.obolibrary.org/obo/TO_0000908), [http://purl.obolibrary.org/obo/TO_0000909](http://purl.obolibrary.org/obo/TO_0000909) |

## `SGN`: Sol Genomics Network

Overall, there were 1 invalid
xrefs to external prefixed with `SGN` (standardized to Bioregistry
prefix [`sgn`](https://bioregistry.io/sgn)) that
did not match the standard pattern `^\d+$`.

| external_xref       |   usages_count | usages                                                                                 |
|---------------------|----------------|----------------------------------------------------------------------------------------|
| `SGN:('SGN', 'nm')` |              1 | [http://purl.obolibrary.org/obo/TO_0002622](http://purl.obolibrary.org/obo/TO_0002622) |

## `TO`: Plant Trait Ontology

Overall, there were 938 invalid
xrefs to external prefixed with `TO` (standardized to Bioregistry
prefix [`to`](https://bioregistry.io/to)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TO:('TO', 'cooperl')`       |            458 | [http://purl.obolibrary.org/obo/TO_0000017](http://purl.obolibrary.org/obo/TO_0000017), [http://purl.obolibrary.org/obo/TO_0000024](http://purl.obolibrary.org/obo/TO_0000024), [http://purl.obolibrary.org/obo/TO_0000030](http://purl.obolibrary.org/obo/TO_0000030), [http://purl.obolibrary.org/obo/TO_0000043](http://purl.obolibrary.org/obo/TO_0000043), [http://purl.obolibrary.org/obo/TO_0000069](http://purl.obolibrary.org/obo/TO_0000069), ... |
| `TO:('TO', 'moorel')`        |            286 | [http://purl.obolibrary.org/obo/TO_0000003](http://purl.obolibrary.org/obo/TO_0000003), [http://purl.obolibrary.org/obo/TO_0000041](http://purl.obolibrary.org/obo/TO_0000041), [http://purl.obolibrary.org/obo/TO_0000050](http://purl.obolibrary.org/obo/TO_0000050), [http://purl.obolibrary.org/obo/TO_0000051](http://purl.obolibrary.org/obo/TO_0000051), [http://purl.obolibrary.org/obo/TO_0000052](http://purl.obolibrary.org/obo/TO_0000052), ... |
| `TO:('TO', 'malaporte')`     |            103 | [http://purl.obolibrary.org/obo/TO_0000057](http://purl.obolibrary.org/obo/TO_0000057), [http://purl.obolibrary.org/obo/TO_0003000](http://purl.obolibrary.org/obo/TO_0003000), [http://purl.obolibrary.org/obo/TO_0003001](http://purl.obolibrary.org/obo/TO_0003001), [http://purl.obolibrary.org/obo/TO_0003002](http://purl.obolibrary.org/obo/TO_0003002), [http://purl.obolibrary.org/obo/TO_0003003](http://purl.obolibrary.org/obo/TO_0003003), ... |
| `TO:('TO', 'TermGenie')`     |             29 | [http://purl.obolibrary.org/obo/TO_1000001](http://purl.obolibrary.org/obo/TO_1000001), [http://purl.obolibrary.org/obo/TO_1000001](http://purl.obolibrary.org/obo/TO_1000001), [http://purl.obolibrary.org/obo/TO_1000002](http://purl.obolibrary.org/obo/TO_1000002), [http://purl.obolibrary.org/obo/TO_1000002](http://purl.obolibrary.org/obo/TO_1000002), [http://purl.obolibrary.org/obo/TO_1000003](http://purl.obolibrary.org/obo/TO_1000003), ... |
| `TO:('TO', 'contributors')`  |             20 | [http://purl.obolibrary.org/obo/TO_0000396](http://purl.obolibrary.org/obo/TO_0000396), [http://purl.obolibrary.org/obo/TO_0020095](http://purl.obolibrary.org/obo/TO_0020095), [http://purl.obolibrary.org/obo/TO_0020096](http://purl.obolibrary.org/obo/TO_0020096), [http://purl.obolibrary.org/obo/TO_0020097](http://purl.obolibrary.org/obo/TO_0020097), [http://purl.obolibrary.org/obo/TO_0020098](http://purl.obolibrary.org/obo/TO_0020098), ... |
| `TO:('TO', 'austin_meier')`  |             15 | [http://purl.obolibrary.org/obo/TO_0000187](http://purl.obolibrary.org/obo/TO_0000187), [http://purl.obolibrary.org/obo/TO_0000225](http://purl.obolibrary.org/obo/TO_0000225), [http://purl.obolibrary.org/obo/TO_0000227](http://purl.obolibrary.org/obo/TO_0000227), [http://purl.obolibrary.org/obo/TO_0000531](http://purl.obolibrary.org/obo/TO_0000531), [http://purl.obolibrary.org/obo/TO_0000586](http://purl.obolibrary.org/obo/TO_0000586), ... |
| `TO:('TO', 'Ethan_Johnson')` |             12 | [http://purl.obolibrary.org/obo/TO_0000954](http://purl.obolibrary.org/obo/TO_0000954), [http://purl.obolibrary.org/obo/TO_0000963](http://purl.obolibrary.org/obo/TO_0000963), [http://purl.obolibrary.org/obo/TO_0000964](http://purl.obolibrary.org/obo/TO_0000964), [http://purl.obolibrary.org/obo/TO_0000965](http://purl.obolibrary.org/obo/TO_0000965), [http://purl.obolibrary.org/obo/TO_0000966](http://purl.obolibrary.org/obo/TO_0000966), ... |
| `TO:('TO', 'ejohnson')`      |              5 | [http://purl.obolibrary.org/obo/TO_0000958](http://purl.obolibrary.org/obo/TO_0000958), [http://purl.obolibrary.org/obo/TO_0000959](http://purl.obolibrary.org/obo/TO_0000959), [http://purl.obolibrary.org/obo/TO_0000960](http://purl.obolibrary.org/obo/TO_0000960), [http://purl.obolibrary.org/obo/TO_0000961](http://purl.obolibrary.org/obo/TO_0000961), [http://purl.obolibrary.org/obo/TO_0000962](http://purl.obolibrary.org/obo/TO_0000962)      |
| `TO:('TO', 'ethan_johnson')` |              4 | [http://purl.obolibrary.org/obo/TO_0000214](http://purl.obolibrary.org/obo/TO_0000214), [http://purl.obolibrary.org/obo/TO_0000531](http://purl.obolibrary.org/obo/TO_0000531), [http://purl.obolibrary.org/obo/TO_0000947](http://purl.obolibrary.org/obo/TO_0000947), [http://purl.obolibrary.org/obo/TO_0000949](http://purl.obolibrary.org/obo/TO_0000949)                                                                                              |
| `TO:('TO', 'Laurel_Cooper')` |              2 | [http://purl.obolibrary.org/obo/TO_0000515](http://purl.obolibrary.org/obo/TO_0000515), [http://purl.obolibrary.org/obo/TO_0001066](http://purl.obolibrary.org/obo/TO_0001066)                                                                                                                                                                                                                                                                              |
| `TO:('TO', 'seymour_megan')` |              2 | [http://purl.obolibrary.org/obo/TO_0000586](http://purl.obolibrary.org/obo/TO_0000586), [http://purl.obolibrary.org/obo/TO_0001012](http://purl.obolibrary.org/obo/TO_0001012)                                                                                                                                                                                                                                                                              |
| `TO:('TO', 'curators')`      |              1 | [http://purl.obolibrary.org/obo/TO_0000737](http://purl.obolibrary.org/obo/TO_0000737)                                                                                                                                                                                                                                                                                                                                                                      |
| `TO:('TO', 'austinmeier')`   |              1 | [http://purl.obolibrary.org/obo/TO_1000022](http://purl.obolibrary.org/obo/TO_1000022)                                                                                                                                                                                                                                                                                                                                                                      |

