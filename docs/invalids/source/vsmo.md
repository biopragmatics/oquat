# vsmo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vsmo`.


## `BFO`: Basic Formal Ontology

Overall, there were 6 invalid
xrefs to external prefixed with `BFO` (standardized to Bioregistry
prefix [`bfo`](https://bioregistry.io/bfo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref              |   usages_count | usages                                                                      |
|----------------------------|----------------|-----------------------------------------------------------------------------|
| `BFO:snap:Object`          |              1 | [snap:Object](http://purl.obolibrary.org/obo/snap_Object)                   |
| `BFO:snap:ObjectAggregate` |              1 | [snap:ObjectAggregate](http://purl.obolibrary.org/obo/snap_ObjectAggregate) |
| `BFO:snap:Quality`         |              1 | [snap:Quality](http://purl.obolibrary.org/obo/snap_Quality)                 |
| `BFO:snap:Role`            |              1 | [snap:Role](http://purl.obolibrary.org/obo/snap_Role)                       |
| `BFO:span:Process`         |              1 | [span:Process](http://purl.obolibrary.org/obo/span_Process)                 |
| `BFO:span:TemporalRegion`  |              1 | [span:TemporalRegion](http://purl.obolibrary.org/obo/span_TemporalRegion)   |

## `CAS`: CAS Registry Number

Overall, there were 1 invalid
xrefs to external prefixed with `CAS` (standardized to Bioregistry
prefix [`cas`](https://bioregistry.io/cas)) that
did not match the standard pattern `^\d{1,7}\-\d{2}\-\d$`.

| external_xref                                                                           |   usages_count | usages                                                        |
|-----------------------------------------------------------------------------------------|----------------|---------------------------------------------------------------|
| `CAS:7-(2-chlorophenyl)-4-ethoxy-3,5-dioxa-6-aza-4-phosphaoct-6-ene-8-nitrile4-sulfide` |              1 | [MIRO:10000108](http://purl.obolibrary.org/obo/MIRO_10000108) |

## `ChEBI`: Chemical Entities of Biological Interest

Overall, there were 1 invalid
xrefs to external prefixed with `ChEBI` (standardized to Bioregistry
prefix [`chebi`](https://bioregistry.io/chebi)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `ChEBI:`        |              1 | [CHEBI:23092](http://purl.obolibrary.org/obo/CHEBI_23092) |

## `DOID`: Human Disease Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `DOID` (standardized to Bioregistry
prefix [`doid`](https://bioregistry.io/doid)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `DOID: 2293`    |              1 | [VSMO:0000055](http://purl.obolibrary.org/obo/VSMO_0000055) |

## `ISBN`: International Standard Book Number

Overall, there were 110 invalid
xrefs to external prefixed with `ISBN` (standardized to Bioregistry
prefix [`isbn`](https://bioregistry.io/isbn)) that
did not match the standard pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`.

| external_xref      |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|--------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ISBN:1555812384:` |            110 | [VSMO:0000529](http://purl.obolibrary.org/obo/VSMO_0000529), [VSMO:0000546](http://purl.obolibrary.org/obo/VSMO_0000546), [VSMO:0000578](http://purl.obolibrary.org/obo/VSMO_0000578), [VSMO:0000579](http://purl.obolibrary.org/obo/VSMO_0000579), [VSMO:0000580](http://purl.obolibrary.org/obo/VSMO_0000580), ... |

## `OBI`: Ontology for Biomedical Investigations

Overall, there were 2 invalid
xrefs to external prefixed with `OBI` (standardized to Bioregistry
prefix [`obi`](https://bioregistry.io/obi)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------|
| `OBI:authors`   |              2 | [OBI:0000415](http://purl.obolibrary.org/obo/OBI_0000415), [OBI:0000659](http://purl.obolibrary.org/obo/OBI_0000659) |

## `VO`: Vaccine Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `VO` (standardized to Bioregistry
prefix [`vo`](https://bioregistry.io/vo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                           |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `VO:Authors`    |              2 | [VO:0000002](http://purl.obolibrary.org/obo/VO_0000002), [VO:0003021](http://purl.obolibrary.org/obo/VO_0003021) |

