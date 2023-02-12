# [`goa`](https://bioregistry.io/goa): Gene Ontology Annotation Database

This page summarize the different resources that reference `goa`
but use local unique identifiers that do not match the standard pattern of
`^(([A-N,R-Z][0-9][A-Z][A-Z, 0-9][A-Z, 0-9][0-9])|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9]))|(URS[0-9A-F]{10}(_[0-9]+){0,1})|(EBI-[0-9]+)$`. Of the 3 resources,
1 variants on the standard prefix were found: ['GOA'].

## `go`: Gene Ontology

Identifiers for this prefix are given incorrectly in `go`. See the [GitHub repository](https://github.com/geneontology/go-ontology).

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `GOA:als`       |              1 | [GO:1903985](http://purl.obolibrary.org/obo/GO_1903985) |

## `nif`: None

Identifiers for this prefix are given incorrectly in `nif`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GOA:UniProtKB` |             19 | [PR:000026262](http://purl.obolibrary.org/obo/PR_000026262), [PR:000026264](http://purl.obolibrary.org/obo/PR_000026264), [PR:000026266](http://purl.obolibrary.org/obo/PR_000026266), [PR:000026268](http://purl.obolibrary.org/obo/PR_000026268), [PR:000026281](http://purl.obolibrary.org/obo/PR_000026281), ... |
| `GOA:IntAct`    |             15 | [PR:000026246](http://purl.obolibrary.org/obo/PR_000026246), [PR:000026256](http://purl.obolibrary.org/obo/PR_000026256), [PR:000026258](http://purl.obolibrary.org/obo/PR_000026258), [PR:000026260](http://purl.obolibrary.org/obo/PR_000026260), [PR:000026277](http://purl.obolibrary.org/obo/PR_000026277), ... |
| `GOA:BHF-UCL`   |              3 | [PR:000026248](http://purl.obolibrary.org/obo/PR_000026248), [PR:000026250](http://purl.obolibrary.org/obo/PR_000026250), [PR:000026252](http://purl.obolibrary.org/obo/PR_000026252)                                                                                                                                |
| `GOA:als`       |              1 | [GO:1903985](http://purl.obolibrary.org/obo/GO_1903985)                                                                                                                                                                                                                                                              |

## `pr`: Protein Ontology

Identifiers for this prefix are given incorrectly in `pr`. See the [GitHub repository](https://github.com/PROconsortium/PRoteinOntology).

| external_xref   |   usages_count | usages                                                                                                                                                                          |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GOA:BHF-UCL`   |              3 | [PR:P51636-1](http://purl.obolibrary.org/obo/PR_P51636-1), [PR:P51636-2](http://purl.obolibrary.org/obo/PR_P51636-2), [PR:P51636-3](http://purl.obolibrary.org/obo/PR_P51636-3) |

