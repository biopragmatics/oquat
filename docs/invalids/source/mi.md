# mi

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `mi`. See the [GitHub repository](https://github.com/HUPO-PSI/psi-mi-CV).


## `GO`: Gene Ontology

Overall, there were 6 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref             |   usages_count | usages                                                                                                                                                             |
|---------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:('GO', 'GO:0044093')` |              2 | [http://purl.obolibrary.org/obo/MI_2236](http://purl.obolibrary.org/obo/MI_2236), [http://purl.obolibrary.org/obo/MI_2241](http://purl.obolibrary.org/obo/MI_2241) |
| `GO:('GO', 'GO:0016491')` |              1 | [http://purl.obolibrary.org/obo/MI_0945](http://purl.obolibrary.org/obo/MI_0945)                                                                                   |
| `GO:('GO', 'GO:0016783')` |              1 | [http://purl.obolibrary.org/obo/MI_1327](http://purl.obolibrary.org/obo/MI_1327)                                                                                   |
| `GO:('GO', 'GO:0018322')` |              1 | [http://purl.obolibrary.org/obo/MI_2272](http://purl.obolibrary.org/obo/MI_2272)                                                                                   |
| `GO:('GO', 'GO:0018166')` |              1 | [http://purl.obolibrary.org/obo/MI_2273](http://purl.obolibrary.org/obo/MI_2273)                                                                                   |

## `PMID`: PubMed

Overall, there were 3 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                  |   usages_count | usages                                                                           |
|--------------------------------|----------------|----------------------------------------------------------------------------------|
| `PMID:('PMID', ':17072308')`   |              1 | [http://purl.obolibrary.org/obo/MI_0813](http://purl.obolibrary.org/obo/MI_0813) |
| `PMID:('PMID', 'ID:11604014')` |              1 | [http://purl.obolibrary.org/obo/MI_1075](http://purl.obolibrary.org/obo/MI_1075) |
| `PMID:('PMID', '13846364.')`   |              1 | [http://purl.obolibrary.org/obo/MI_1197](http://purl.obolibrary.org/obo/MI_1197) |

## `psi-mi`: Molecular Interactions Controlled Vocabulary

Overall, there were 1 invalid
xrefs to external prefixed with `psi-mi` (standardized to Bioregistry
prefix [`mi`](https://bioregistry.io/mi)) that
did not match the standard pattern `^\d{4}$`.

| external_xref                  |   usages_count | usages                                                                           |
|--------------------------------|----------------|----------------------------------------------------------------------------------|
| `psi-mi:('psi-mi', 'MI:1285')` |              1 | [http://purl.obolibrary.org/obo/MI_1276](http://purl.obolibrary.org/obo/MI_1276) |

