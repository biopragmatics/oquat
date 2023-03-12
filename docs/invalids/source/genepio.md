# genepio

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `genepio`. See the [GitHub repository](https://github.com/GenEpiO/genepio).


## `INSDC`: Nucleotide Sequence Database

Overall, there were 2 invalid
xrefs to external prefixed with `INSDC` (standardized to Bioregistry
prefix [`insdc`](https://bioregistry.io/insdc)) that
did not match the standard pattern `^([A-Z]\d{5}|[A-Z]{2}\d{6}|[A-Z]{4,6}\d{8,10}|[A-J][A-Z]{2}\d{5})(\.\d+)?$`.

| external_xref                |   usages_count | usages                                                            |
|------------------------------|----------------|-------------------------------------------------------------------|
| `INSDC:institution_code:BRS` |              1 | [GENEPIO:0001643](http://purl.obolibrary.org/obo/GENEPIO_0001643) |
| `INSDC:specimen_voucher`     |              1 | [GENEPIO:0001722](http://purl.obolibrary.org/obo/GENEPIO_0001722) |

## `Snomed`: SNOMED CT (International Edition)

Overall, there were 2 invalid
xrefs to external prefixed with `Snomed` (standardized to Bioregistry
prefix [`snomedct`](https://bioregistry.io/snomedct)) that
did not match the standard pattern `^(\w+)?\d+$`.

| external_xref               |   usages_count | usages                                                            |
|-----------------------------|----------------|-------------------------------------------------------------------|
| `Snomed: Concept 260827009` |              1 | [GENEPIO:0001076](http://purl.obolibrary.org/obo/GENEPIO_0001076) |
| `Snomed: Concept 260823008` |              1 | [GENEPIO:0001077](http://purl.obolibrary.org/obo/GENEPIO_0001077) |

## `SNOMED`: SNOMED CT (International Edition)

Overall, there were 1 invalid
xrefs to external prefixed with `SNOMED` (standardized to Bioregistry
prefix [`snomedct`](https://bioregistry.io/snomedct)) that
did not match the standard pattern `^(\w+)?\d+$`.

| external_xref                                                  |   usages_count | usages                                                            |
|----------------------------------------------------------------|----------------|-------------------------------------------------------------------|
| `SNOMED: http://www.snomedbrowser.com/Codes/Details/272405002` |              1 | [GENEPIO:0001719](http://purl.obolibrary.org/obo/GENEPIO_0001719) |

