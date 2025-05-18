# xco

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `xco`. See the [GitHub repository](https://github.com/rat-genome-database/XCO-experimental-condition-ontology).


## `Cellosaurus`: Cellosaurus

Overall, there were 2 invalid
xrefs to external prefixed with `Cellosaurus` (standardized to Bioregistry
prefix [`cellosaurus`](https://bioregistry.io/cellosaurus)) that
did not match the standard pattern `^[A-Z0-9]{4}$`.

| external_xref           |   usages_count | usages                                                    |
|-------------------------|----------------|-----------------------------------------------------------|
| `Cellosaurus:CVCL_5712` |              1 | [XCO:0000835](http://purl.obolibrary.org/obo/XCO_0000835) |
| `Cellosaurus:CVCL_3537` |              1 | [XCO:0001045](http://purl.obolibrary.org/obo/XCO_0001045) |

## `CHEBI`: Chemical Entities of Biological Interest

Overall, there were 1 invalid
xrefs to external prefixed with `CHEBI` (standardized to Bioregistry
prefix [`chebi`](https://bioregistry.io/chebi)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `CHEBI:25698he` |              1 | [XCO:0000799](http://purl.obolibrary.org/obo/XCO_0000799) |

## `CHEMBL`: ChEMBL

Overall, there were 1 invalid
xrefs to external prefixed with `CHEMBL` (standardized to Bioregistry
prefix [`chembl`](https://bioregistry.io/chembl)) that
did not match the standard pattern `^CHEMBL\d+$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `CHEMBL:105608` |              1 | [XCO:0000322](http://purl.obolibrary.org/obo/XCO_0000322) |

## `MESH`: Medical Subject Headings

Overall, there were 2 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D|M)\d{6,9}$`.

| external_xref   |   usages_count | usages                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------|
| `MESH:68011802` |              2 | [XCO:0000617](http://purl.obolibrary.org/obo/XCO_0000617), [XCO:0000617](http://purl.obolibrary.org/obo/XCO_0000617) |

## `PMID`: PubMed

Overall, there were 3 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref    |   usages_count | usages                                                    |
|------------------|----------------|-----------------------------------------------------------|
| `PMID:_21543068` |              1 | [XCO:0001532](http://purl.obolibrary.org/obo/XCO_0001532) |
| `PMID:_33008419` |              1 | [XCO:0001535](http://purl.obolibrary.org/obo/XCO_0001535) |
| `PMID:_28143577` |              1 | [XCO:0001576](http://purl.obolibrary.org/obo/XCO_0001576) |

## `RGD`: Rat Genome Database

Overall, there were 41 invalid
xrefs to external prefixed with `RGD` (standardized to Bioregistry
prefix [`rgd`](https://bioregistry.io/rgd)) that
did not match the standard pattern `^\d{4,}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RGD:MS`        |             24 | [XCO:0000010](http://purl.obolibrary.org/obo/XCO_0000010), [XCO:0000012](http://purl.obolibrary.org/obo/XCO_0000012), [XCO:0000014](http://purl.obolibrary.org/obo/XCO_0000014), [XCO:0000015](http://purl.obolibrary.org/obo/XCO_0000015), [XCO:0000017](http://purl.obolibrary.org/obo/XCO_0000017), ... |
| `RGD:JRS`       |             15 | [XCO:0000120](http://purl.obolibrary.org/obo/XCO_0000120), [XCO:0000133](http://purl.obolibrary.org/obo/XCO_0000133), [XCO:0000152](http://purl.obolibrary.org/obo/XCO_0000152), [XCO:0000153](http://purl.obolibrary.org/obo/XCO_0000153), [XCO:0000158](http://purl.obolibrary.org/obo/XCO_0000158), ... |
| `RGD:SL`        |              1 | [XCO:0000138](http://purl.obolibrary.org/obo/XCO_0000138)                                                                                                                                                                                                                                                  |
| `RGD:MRD`       |              1 | [XCO:0000166](http://purl.obolibrary.org/obo/XCO_0000166)                                                                                                                                                                                                                                                  |

## `UniProt`: UniProt Protein

Overall, there were 1 invalid
xrefs to external prefixed with `UniProt` (standardized to Bioregistry
prefix [`uniprot`](https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref    |   usages_count | usages                                                    |
|------------------|----------------|-----------------------------------------------------------|
| `UniProt:419947` |              1 | [XCO:0001037](http://purl.obolibrary.org/obo/XCO_0001037) |

