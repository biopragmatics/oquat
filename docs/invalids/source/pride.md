# pride

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `pride`.


## `CHEBI`: Chemical Entities of Biological Interest

Overall, there were 1 invalid
xrefs to external prefixed with `CHEBI` (standardized to Bioregistry
prefix [`chebi`](https://bioregistry.io/chebi)) that
did not match the standard pattern `^\d+$`.

| external_xref         |   usages_count | usages                                                                                     |
|-----------------------|----------------|--------------------------------------------------------------------------------------------|
| `CHEBI:('CHEBI', '')` |              1 | [http://purl.obolibrary.org/obo/CHMO_0002374](http://purl.obolibrary.org/obo/CHMO_0002374) |

## `FIX`: Physico-chemical methods and properties

Overall, there were 7 invalid
xrefs to external prefixed with `FIX` (standardized to Bioregistry
prefix [`fix`](https://bioregistry.io/fix)) that
did not match the standard pattern `^\d{7}$`.

| external_xref             |   usages_count | usages                                                                                     |
|---------------------------|----------------|--------------------------------------------------------------------------------------------|
| `FIX:('FIX', '000760')`   |              1 | [http://purl.obolibrary.org/obo/CHMO_0002141](http://purl.obolibrary.org/obo/CHMO_0002141) |
| `FIX:('FIX', '000762')`   |              1 | [http://purl.obolibrary.org/obo/CHMO_0002142](http://purl.obolibrary.org/obo/CHMO_0002142) |
| `FIX:('FIX', '000771')`   |              1 | [http://purl.obolibrary.org/obo/CHMO_0002143](http://purl.obolibrary.org/obo/CHMO_0002143) |
| `FIX:('FIX', '000774')`   |              1 | [http://purl.obolibrary.org/obo/CHMO_0002144](http://purl.obolibrary.org/obo/CHMO_0002144) |
| `FIX:('FIX', '00001158')` |              1 | [http://purl.obolibrary.org/obo/CHMO_0002708](http://purl.obolibrary.org/obo/CHMO_0002708) |
| `FIX:('FIX', '00001157')` |              1 | [http://purl.obolibrary.org/obo/CHMO_0002709](http://purl.obolibrary.org/obo/CHMO_0002709) |
| `FIX:('FIX', '000125')`   |              1 | [http://purl.obolibrary.org/obo/CHMO_0002713](http://purl.obolibrary.org/obo/CHMO_0002713) |

## `obi`: Ontology for Biomedical Investigations

Overall, there were 32 invalid
xrefs to external prefixed with `obi` (standardized to Bioregistry
prefix [`obi`](https://bioregistry.io/obi)) that
did not match the standard pattern `^\d{7}$`.

| external_xref            |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `obi:('obi', 'bp')`      |              6 | [http://purl.obolibrary.org/obo/OBI_0000094](http://purl.obolibrary.org/obo/OBI_0000094), [http://purl.obolibrary.org/obo/OBI_0000417](http://purl.obolibrary.org/obo/OBI_0000417), [http://purl.obolibrary.org/obo/OBI_0000443](http://purl.obolibrary.org/obo/OBI_0000443), [http://purl.obolibrary.org/obo/OBI_0000796](http://purl.obolibrary.org/obo/OBI_0000796), [http://purl.obolibrary.org/obo/OBI_0000838](http://purl.obolibrary.org/obo/OBI_0000838), ... |
| `obi:('obi', 'prs')`     |              6 | [http://purl.obolibrary.org/obo/OBI_0000094](http://purl.obolibrary.org/obo/OBI_0000094), [http://purl.obolibrary.org/obo/OBI_0000443](http://purl.obolibrary.org/obo/OBI_0000443), [http://purl.obolibrary.org/obo/OBI_0302886](http://purl.obolibrary.org/obo/OBI_0302886), [http://purl.obolibrary.org/obo/OBI_0302888](http://purl.obolibrary.org/obo/OBI_0302888), [http://purl.obolibrary.org/obo/OBI_0302893](http://purl.obolibrary.org/obo/OBI_0302893), ... |
| `obi:('obi', 'pppb')`    |              2 | [http://purl.obolibrary.org/obo/OBI_0000070](http://purl.obolibrary.org/obo/OBI_0000070), [http://purl.obolibrary.org/obo/OBI_0000185](http://purl.obolibrary.org/obo/OBI_0000185)                                                                                                                                                                                                                                                                                    |
| `obi:('obi', 'mc')`      |              2 | [http://purl.obolibrary.org/obo/OBI_0000094](http://purl.obolibrary.org/obo/OBI_0000094), [http://purl.obolibrary.org/obo/OBI_0200051](http://purl.obolibrary.org/obo/OBI_0200051)                                                                                                                                                                                                                                                                                    |
| `obi:('obi', 'ar')`      |              2 | [http://purl.obolibrary.org/obo/OBI_0000417](http://purl.obolibrary.org/obo/OBI_0000417), [http://purl.obolibrary.org/obo/OBI_0000443](http://purl.obolibrary.org/obo/OBI_0000443)                                                                                                                                                                                                                                                                                    |
| `obi:('obi', 'hp')`      |              2 | [http://purl.obolibrary.org/obo/OBI_0000443](http://purl.obolibrary.org/obo/OBI_0000443), [http://purl.obolibrary.org/obo/OBI_0001032](http://purl.obolibrary.org/obo/OBI_0001032)                                                                                                                                                                                                                                                                                    |
| `obi:('obi', 'es')`      |              2 | [http://purl.obolibrary.org/obo/OBI_0001061](http://purl.obolibrary.org/obo/OBI_0001061), [http://purl.obolibrary.org/obo/OBI_0001138](http://purl.obolibrary.org/obo/OBI_0001138)                                                                                                                                                                                                                                                                                    |
| `obi:('obi', 'jq')`      |              2 | [http://purl.obolibrary.org/obo/OBI_0400064](http://purl.obolibrary.org/obo/OBI_0400064), [http://purl.obolibrary.org/obo/OBI_0400065](http://purl.obolibrary.org/obo/OBI_0400065)                                                                                                                                                                                                                                                                                    |
| `obi:('obi', 'fg')`      |              1 | [http://purl.obolibrary.org/obo/OBI_0000094](http://purl.obolibrary.org/obo/OBI_0000094)                                                                                                                                                                                                                                                                                                                                                                              |
| `obi:('obi', 'jf')`      |              1 | [http://purl.obolibrary.org/obo/OBI_0000094](http://purl.obolibrary.org/obo/OBI_0000094)                                                                                                                                                                                                                                                                                                                                                                              |
| `obi:('obi', 'ppb')`     |              1 | [http://purl.obolibrary.org/obo/OBI_0000443](http://purl.obolibrary.org/obo/OBI_0000443)                                                                                                                                                                                                                                                                                                                                                                              |
| `obi:('obi', 'IEDB')`    |              1 | [http://purl.obolibrary.org/obo/OBI_0000661](http://purl.obolibrary.org/obo/OBI_0000661)                                                                                                                                                                                                                                                                                                                                                                              |
| `obi:('obi', 'obi')`     |              1 | [http://purl.obolibrary.org/obo/OBI_0000968](http://purl.obolibrary.org/obo/OBI_0000968)                                                                                                                                                                                                                                                                                                                                                                              |
| `obi:('obi', 'EAGLE-I')` |              1 | [http://purl.obolibrary.org/obo/OBI_0001042](http://purl.obolibrary.org/obo/OBI_0001042)                                                                                                                                                                                                                                                                                                                                                                              |
| `obi:('obi', 'em')`      |              1 | [http://purl.obolibrary.org/obo/OBI_0200051](http://purl.obolibrary.org/obo/OBI_0200051)                                                                                                                                                                                                                                                                                                                                                                              |
| `obi:('obi', 'jm')`      |              1 | [http://purl.obolibrary.org/obo/OBI_0200051](http://purl.obolibrary.org/obo/OBI_0200051)                                                                                                                                                                                                                                                                                                                                                                              |

## `PRIDE`: PRIDE Controlled Vocabulary

Overall, there were 3 invalid
xrefs to external prefixed with `PRIDE` (standardized to Bioregistry
prefix [`pride`](https://bioregistry.io/pride)) that
did not match the standard pattern `^\d+$`.

| external_xref              |   usages_count | usages                                                                                                                                                                                                                                                                                   |
|----------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PRIDE:('PRIDE', 'PRIDE')` |              3 | [http://purl.obolibrary.org/obo/PRIDE_0000099](http://purl.obolibrary.org/obo/PRIDE_0000099), [http://purl.obolibrary.org/obo/PRIDE_0000100](http://purl.obolibrary.org/obo/PRIDE_0000100), [http://purl.obolibrary.org/obo/PRIDE_0000104](http://purl.obolibrary.org/obo/PRIDE_0000104) |

