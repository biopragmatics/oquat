# sibo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `sibo`. See the [GitHub repository](https://github.com/obophenotype/sibo).


## `KEGG COMPOUND`: KEGG Compound

Overall, there were 9 invalid
xrefs to external prefixed with `KEGG COMPOUND` (standardized to Bioregistry
prefix [`kegg.compound`](https://bioregistry.io/kegg.compound)) that
did not match the standard pattern `^C\d+$`.

| external_xref                               |   usages_count | usages                                                                                     |
|---------------------------------------------|----------------|--------------------------------------------------------------------------------------------|
| `KEGG COMPOUND:('KEGG COMPOUND', 'c00180')` |              1 | [http://purl.obolibrary.org/obo/SIBO_0000171](http://purl.obolibrary.org/obo/SIBO_0000171) |
| `KEGG COMPOUND:('KEGG COMPOUND', 'c00711')` |              1 | [http://purl.obolibrary.org/obo/SIBO_0000172](http://purl.obolibrary.org/obo/SIBO_0000172) |
| `KEGG COMPOUND:('KEGG COMPOUND', 'c00383')` |              1 | [http://purl.obolibrary.org/obo/SIBO_0000175](http://purl.obolibrary.org/obo/SIBO_0000175) |
| `KEGG COMPOUND:('KEGG COMPOUND', 'c00366')` |              1 | [http://purl.obolibrary.org/obo/SIBO_0000179](http://purl.obolibrary.org/obo/SIBO_0000179) |
| `KEGG COMPOUND:('KEGG COMPOUND', 'c01530')` |              1 | [http://purl.obolibrary.org/obo/SIBO_0000182](http://purl.obolibrary.org/obo/SIBO_0000182) |
| `KEGG COMPOUND:('KEGG COMPOUND', 'c02226')` |              1 | [http://purl.obolibrary.org/obo/SIBO_0000188](http://purl.obolibrary.org/obo/SIBO_0000188) |
| `KEGG COMPOUND:('KEGG COMPOUND', 'c01432')` |              1 | [http://purl.obolibrary.org/obo/SIBO_0000190](http://purl.obolibrary.org/obo/SIBO_0000190) |
| `KEGG COMPOUND:('KEGG COMPOUND', 'c00303')` |              1 | [http://purl.obolibrary.org/obo/SIBO_0000204](http://purl.obolibrary.org/obo/SIBO_0000204) |
| `KEGG COMPOUND:('KEGG COMPOUND', 'c02057')` |              1 | [http://purl.obolibrary.org/obo/SIBO_0000205](http://purl.obolibrary.org/obo/SIBO_0000205) |

## `SIBO`: Social Insect Behavior Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `SIBO` (standardized to Bioregistry
prefix [`sibo`](https://bioregistry.io/sibo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref             |   usages_count | usages                                                                                     |
|---------------------------|----------------|--------------------------------------------------------------------------------------------|
| `SIBO:('SIBO', 'csmith')` |              1 | [http://purl.obolibrary.org/obo/SIBO_0000079](http://purl.obolibrary.org/obo/SIBO_0000079) |

