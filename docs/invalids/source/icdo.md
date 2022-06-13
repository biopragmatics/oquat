# icdo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `icdo`.


## `MESH`: Medical Subject Headings

Overall, there were 10 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                  |   usages_count | usages                                                          |
|--------------------------------|----------------|-----------------------------------------------------------------|
| `MESH:A03.492.411`             |              1 | [UBERON:0000160](http://purl.obolibrary.org/obo/UBERON_0000160) |
| `MESH:A03.492.766`             |              1 | [UBERON:0000945](http://purl.obolibrary.org/obo/UBERON_0000945) |
| `MESH:A03.365`                 |              1 | [UBERON:0001043](http://purl.obolibrary.org/obo/UBERON_0001043) |
| `MESH:A01.176`                 |              1 | [UBERON:0001137](http://purl.obolibrary.org/obo/UBERON_0001137) |
| `MESH:A05.810.161`             |              1 | [UBERON:0001255](http://purl.obolibrary.org/obo/UBERON_0001255) |
| `MESH:A05.360.444.849.286`     |              1 | [UBERON:0001301](http://purl.obolibrary.org/obo/UBERON_0001301) |
| `MESH:A01.911`                 |              1 | [UBERON:0001443](http://purl.obolibrary.org/obo/UBERON_0001443) |
| `MESH:A03.492.411.620`         |              1 | [UBERON:0002108](http://purl.obolibrary.org/obo/UBERON_0002108) |
| `MESH:A03.492`                 |              1 | [UBERON:0005409](http://purl.obolibrary.org/obo/UBERON_0005409) |
| `MESH:A02.835.232.500.247.510` |              1 | [UBERON:0007119](http://purl.obolibrary.org/obo/UBERON_0007119) |

## `ncithesaurus`: NCI Thesaurus

Overall, there were 2 invalid
xrefs to external prefixed with `ncithesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                   |   usages_count | usages                                                          |
|---------------------------------|----------------|-----------------------------------------------------------------|
| `ncithesaurus:Whole_Organism`   |              1 | [UBERON:0000468](http://purl.obolibrary.org/obo/UBERON_0000468) |
| `ncithesaurus:Digestive_System` |              1 | [UBERON:0001007](http://purl.obolibrary.org/obo/UBERON_0001007) |

## `SO`: Sequence types and features ontology

Overall, there were 1 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `SO:similar_to` |              1 | [RO:HOM0000000](http://purl.obolibrary.org/obo/RO_HOM0000000) |

