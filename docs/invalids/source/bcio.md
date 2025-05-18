# bcio

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `bcio`.


## `Geonames`: GeoNames

Overall, there were 11 invalid
xrefs to external prefixed with `Geonames` (standardized to Bioregistry
prefix [`geonames`](https://bioregistry.io/geonames)) that
did not match the standard pattern `^\d+$`.

| external_xref      |   usages_count | usages                                                                                                                                                                                                                                                     |
|--------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Geonames:feature` |              4 | [ENVO:00000064](http://purl.obolibrary.org/obo/ENVO_00000064), [ENVO:00000091](http://purl.obolibrary.org/obo/ENVO_00000091), [ENVO:00000109](http://purl.obolibrary.org/obo/ENVO_00000109), [ENVO:00000111](http://purl.obolibrary.org/obo/ENVO_00000111) |
| `Geonames:R`       |              1 | [ENVO:00000064](http://purl.obolibrary.org/obo/ENVO_00000064)                                                                                                                                                                                              |
| `Geonames:R.RD`    |              1 | [ENVO:00000064](http://purl.obolibrary.org/obo/ENVO_00000064)                                                                                                                                                                                              |
| `Geonames:R.ST`    |              1 | [ENVO:00000064](http://purl.obolibrary.org/obo/ENVO_00000064)                                                                                                                                                                                              |
| `Geonames:T.BCH`   |              1 | [ENVO:00000091](http://purl.obolibrary.org/obo/ENVO_00000091)                                                                                                                                                                                              |
| `Geonames:T.BCHS`  |              1 | [ENVO:00000091](http://purl.obolibrary.org/obo/ENVO_00000091)                                                                                                                                                                                              |
| `Geonames:V.GRVPN` |              1 | [ENVO:00000109](http://purl.obolibrary.org/obo/ENVO_00000109)                                                                                                                                                                                              |
| `Geonames:V.FRST`  |              1 | [ENVO:00000111](http://purl.obolibrary.org/obo/ENVO_00000111)                                                                                                                                                                                              |

## `MA`: Mouse adult gross anatomy

Overall, there were 2 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
prefix [`ma`](https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                       |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------|
| `MA:ma`         |              2 | [ENVO:00000010](http://purl.obolibrary.org/obo/ENVO_00000010), [ENVO:00000070](http://purl.obolibrary.org/obo/ENVO_00000070) |

