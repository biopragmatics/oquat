# aeon

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `aeon`. See the [GitHub repository](https://github.com/tibonto/aeon).


## `Geonames`: GeoNames

Overall, there were 8 invalid
xrefs to external prefixed with `Geonames` (standardized to Bioregistry
prefix [`geonames`](https://bioregistry.io/geonames)) that
did not match the standard pattern `^\d+$`.

| external_xref                                        |   usages_count | usages                                                                                                                                                                                      |
|------------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Geonames:feature`                                   |              3 | [ENVO:00000005](http://purl.obolibrary.org/obo/ENVO_00000005), [ENVO:00000062](http://purl.obolibrary.org/obo/ENVO_00000062), [ENVO:00000123](http://purl.obolibrary.org/obo/ENVO_00000123) |
| `Geonames:http://www.geonames.org/export/codes.html` |              1 | [ENVO:00000005](http://purl.obolibrary.org/obo/ENVO_00000005)                                                                                                                               |
| `Geonames:A.ADM1`                                    |              1 | [ENVO:00000005](http://purl.obolibrary.org/obo/ENVO_00000005)                                                                                                                               |
| `Geonames:P.PPL`                                     |              1 | [ENVO:00000062](http://purl.obolibrary.org/obo/ENVO_00000062)                                                                                                                               |
| `Geonames:P.PPLS`                                    |              1 | [ENVO:00000062](http://purl.obolibrary.org/obo/ENVO_00000062)                                                                                                                               |
| `Geonames:A.PCL`                                     |              1 | [ENVO:00000123](http://purl.obolibrary.org/obo/ENVO_00000123)                                                                                                                               |

## `MA`: Mouse adult gross anatomy

Overall, there were 1 invalid
xrefs to external prefixed with `MA` (standardized to Bioregistry
prefix [`ma`](https://bioregistry.io/ma)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `MA:ma`         |              1 | [ENVO:00000123](http://purl.obolibrary.org/obo/ENVO_00000123) |

