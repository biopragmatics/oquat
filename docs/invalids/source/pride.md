# pride

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `pride`. See the [GitHub repository](https://github.com/PRIDE-Utilities/pride-ontology).


## `CHEBI`: Chemical Entities of Biological Interest

Overall, there were 1 invalid
xrefs to external prefixed with `CHEBI` (standardized to Bioregistry
prefix [`chebi`](https://bioregistry.io/chebi)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `CHEBI:`        |              1 | [CHMO:0002374](http://purl.obolibrary.org/obo/CHMO_0002374) |

## `FIX`: Physico-chemical methods and properties

Overall, there were 7 invalid
xrefs to external prefixed with `FIX` (standardized to Bioregistry
prefix [`fix`](https://bioregistry.io/fix)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `FIX:000760`    |              1 | [CHMO:0002141](http://purl.obolibrary.org/obo/CHMO_0002141) |
| `FIX:000762`    |              1 | [CHMO:0002142](http://purl.obolibrary.org/obo/CHMO_0002142) |
| `FIX:000771`    |              1 | [CHMO:0002143](http://purl.obolibrary.org/obo/CHMO_0002143) |
| `FIX:000774`    |              1 | [CHMO:0002144](http://purl.obolibrary.org/obo/CHMO_0002144) |
| `FIX:00001158`  |              1 | [CHMO:0002708](http://purl.obolibrary.org/obo/CHMO_0002708) |
| `FIX:00001157`  |              1 | [CHMO:0002709](http://purl.obolibrary.org/obo/CHMO_0002709) |
| `FIX:000125`    |              1 | [CHMO:0002713](http://purl.obolibrary.org/obo/CHMO_0002713) |

## `OBCS`: Ontology of Biological and Clinical Statistics

Overall, there were 2 invalid
xrefs to external prefixed with `OBCS` (standardized to Bioregistry
prefix [`obcs`](https://bioregistry.io/obcs)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                   |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------|
| `OBCS:YQH`      |              2 | [OBCS:0000058](http://purl.obolibrary.org/obo/OBCS_0000058), [OBCS:0000059](http://purl.obolibrary.org/obo/OBCS_0000059) |

## `obi`: Ontology for Biomedical Investigations

Overall, there were 32 invalid
xrefs to external prefixed with `obi` (standardized to Bioregistry
prefix [`obi`](https://bioregistry.io/obi)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `obi:bp`        |              6 | [OBI:0000094](http://purl.obolibrary.org/obo/OBI_0000094), [OBI:0000417](http://purl.obolibrary.org/obo/OBI_0000417), [OBI:0000443](http://purl.obolibrary.org/obo/OBI_0000443), [OBI:0000796](http://purl.obolibrary.org/obo/OBI_0000796), [OBI:0000838](http://purl.obolibrary.org/obo/OBI_0000838), ... |
| `obi:prs`       |              6 | [OBI:0000094](http://purl.obolibrary.org/obo/OBI_0000094), [OBI:0000443](http://purl.obolibrary.org/obo/OBI_0000443), [OBI:0302886](http://purl.obolibrary.org/obo/OBI_0302886), [OBI:0302888](http://purl.obolibrary.org/obo/OBI_0302888), [OBI:0302893](http://purl.obolibrary.org/obo/OBI_0302893), ... |
| `obi:pppb`      |              2 | [OBI:0000070](http://purl.obolibrary.org/obo/OBI_0000070), [OBI:0000185](http://purl.obolibrary.org/obo/OBI_0000185)                                                                                                                                                                                       |
| `obi:mc`        |              2 | [OBI:0000094](http://purl.obolibrary.org/obo/OBI_0000094), [OBI:0200051](http://purl.obolibrary.org/obo/OBI_0200051)                                                                                                                                                                                       |
| `obi:ar`        |              2 | [OBI:0000417](http://purl.obolibrary.org/obo/OBI_0000417), [OBI:0000443](http://purl.obolibrary.org/obo/OBI_0000443)                                                                                                                                                                                       |
| `obi:hp`        |              2 | [OBI:0000443](http://purl.obolibrary.org/obo/OBI_0000443), [OBI:0001032](http://purl.obolibrary.org/obo/OBI_0001032)                                                                                                                                                                                       |
| `obi:es`        |              2 | [OBI:0001061](http://purl.obolibrary.org/obo/OBI_0001061), [OBI:0001138](http://purl.obolibrary.org/obo/OBI_0001138)                                                                                                                                                                                       |
| `obi:jq`        |              2 | [OBI:0400064](http://purl.obolibrary.org/obo/OBI_0400064), [OBI:0400065](http://purl.obolibrary.org/obo/OBI_0400065)                                                                                                                                                                                       |
| `obi:fg`        |              1 | [OBI:0000094](http://purl.obolibrary.org/obo/OBI_0000094)                                                                                                                                                                                                                                                  |
| `obi:jf`        |              1 | [OBI:0000094](http://purl.obolibrary.org/obo/OBI_0000094)                                                                                                                                                                                                                                                  |
| `obi:ppb`       |              1 | [OBI:0000443](http://purl.obolibrary.org/obo/OBI_0000443)                                                                                                                                                                                                                                                  |
| `obi:IEDB`      |              1 | [OBI:0000661](http://purl.obolibrary.org/obo/OBI_0000661)                                                                                                                                                                                                                                                  |
| `obi:obi`       |              1 | [OBI:0000968](http://purl.obolibrary.org/obo/OBI_0000968)                                                                                                                                                                                                                                                  |
| `obi:EAGLE-I`   |              1 | [OBI:0001042](http://purl.obolibrary.org/obo/OBI_0001042)                                                                                                                                                                                                                                                  |
| `obi:em`        |              1 | [OBI:0200051](http://purl.obolibrary.org/obo/OBI_0200051)                                                                                                                                                                                                                                                  |
| `obi:jm`        |              1 | [OBI:0200051](http://purl.obolibrary.org/obo/OBI_0200051)                                                                                                                                                                                                                                                  |

## `PRIDE`: PRIDE Controlled Vocabulary

Overall, there were 3 invalid
xrefs to external prefixed with `PRIDE` (standardized to Bioregistry
prefix [`pride`](https://bioregistry.io/pride)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                      |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PRIDE:PRIDE`   |              3 | [PRIDE:0000099](http://purl.obolibrary.org/obo/PRIDE_0000099), [PRIDE:0000100](http://purl.obolibrary.org/obo/PRIDE_0000100), [PRIDE:0000104](http://purl.obolibrary.org/obo/PRIDE_0000104) |

