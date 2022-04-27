# idomal

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `idomal`. See the [GitHub repository](https://github.com/VEuPathDB-ontology/IDOMAL).


## `BFO`: Basic Formal Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `BFO` (standardized to Bioregistry
prefix [`bfo`](https://bioregistry.io/bfo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref         |   usages_count | usages                                                                                         |
|-----------------------|----------------|------------------------------------------------------------------------------------------------|
| `BFO:('BFO', 'SNAP')` |              1 | [http://purl.obolibrary.org/obo/IDOMAL_0000002](http://purl.obolibrary.org/obo/IDOMAL_0000002) |

## `ISBN`: International Standard Book Number

Overall, there were 2 invalid
xrefs to external prefixed with `ISBN` (standardized to Bioregistry
prefix [`isbn`](https://bioregistry.io/isbn)) that
did not match the standard pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`.

| external_xref                     |   usages_count | usages                                                                                         |
|-----------------------------------|----------------|------------------------------------------------------------------------------------------------|
| `ISBN:('ISBN', '0-8493-15-67-0')` |              1 | [http://purl.obolibrary.org/obo/IDOMAL_0000783](http://purl.obolibrary.org/obo/IDOMAL_0000783) |
| `ISBN:('ISBN', '0-412-40180-0:')` |              1 | [http://purl.obolibrary.org/obo/IDOMAL_0002188](http://purl.obolibrary.org/obo/IDOMAL_0002188) |

## `NCI`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCI` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref              |   usages_count | usages                                                                                           |
|----------------------------|----------------|--------------------------------------------------------------------------------------------------|
| `NCI:('NCI', 'Thesaurus')` |              1 | [http://purl.obolibrary.org/obo/IDOMAL_50000048](http://purl.obolibrary.org/obo/IDOMAL_50000048) |

## `Wikipedia`: Wikipedia

Overall, there were 1 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                             |   usages_count | usages                                                                                         |
|-------------------------------------------|----------------|------------------------------------------------------------------------------------------------|
| `Wikipedia:('Wikipedia', "Field'sstain")` |              1 | [http://purl.obolibrary.org/obo/IDOMAL_0000553](http://purl.obolibrary.org/obo/IDOMAL_0000553) |

