# obci

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `obci`.


## `CARO`: Common Anatomy Reference Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `CARO` (standardized to Bioregistry
prefix [`caro`](https://bioregistry.io/caro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `CARO:mah`      |              1 | [CL:0000000](http://purl.obolibrary.org/obo/CL_0000000) |

## `ICD9CM`: International Classification of Diseases, 9th Revision, Clinical Modification

Overall, there were 3 invalid
xrefs to external prefixed with `ICD9CM` (standardized to Bioregistry
prefix [`icd9cm`](https://bioregistry.io/icd9cm)) that
did not match the standard pattern `^([\dA-Z]\d{2}(\.\d{1,3}|))|(\d{2}(\.\d{1,2}|))$`.

| external_xref       |   usages_count | usages                                              |
|---------------------|----------------|-----------------------------------------------------|
| `ICD9CM:042-042.99` |              1 | [DOID:526](http://purl.obolibrary.org/obo/DOID_526) |
| `ICD9CM:520-579.99` |              1 | [DOID:77](http://purl.obolibrary.org/obo/DOID_77)   |
| `ICD9CM:060-066.99` |              1 | [DOID:934](http://purl.obolibrary.org/obo/DOID_934) |

## `KEGG`: Kyoto Encyclopedia of Genes and Genomes

Overall, there were 2 invalid
xrefs to external prefixed with `KEGG` (standardized to Bioregistry
prefix [`kegg`](https://bioregistry.io/kegg)) that
did not match the standard pattern `^([CHDEGTMKR]\d+)|(\w+:[\w\d\.-]*)|([a-z]{3,5})|(\w{2,4}\d{5})$`.

| external_xref   |   usages_count | usages                                                |
|-----------------|----------------|-------------------------------------------------------|
| `KEGG:05323`    |              1 | [DOID:7148](http://purl.obolibrary.org/obo/DOID_7148) |
| `KEGG:05210`    |              1 | [DOID:9256](http://purl.obolibrary.org/obo/DOID_9256) |

## `MESH`: Medical Subject Headings

Overall, there were 1 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D|M)\d{6,9}$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `MESH:A12.207`  |              1 | [UBERON:0006314](http://purl.obolibrary.org/obo/UBERON_0006314) |

## `MIM`: Online Mendelian Inheritance in Man

Overall, there were 2 invalid
xrefs to external prefixed with `MIM` (standardized to Bioregistry
prefix [`omim`](https://bioregistry.io/omim)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `MIM:PS275200`  |              1 | [DOID:0050328](http://purl.obolibrary.org/obo/DOID_0050328) |
| `MIM:PS210200`  |              1 | [DOID:0050710](http://purl.obolibrary.org/obo/DOID_0050710) |

## `MP`: Mammalian Phenotype Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `MP` (standardized to Bioregistry
prefix [`mp`](https://bioregistry.io/mp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                          |
|-----------------|----------------|-----------------------------------------------------------------|
| `MP:MP`         |              1 | [UBERON:0000173](http://purl.obolibrary.org/obo/UBERON_0000173) |

## `PDBeChem`: Chemical Component Dictionary

Overall, there were 1 invalid
xrefs to external prefixed with `PDBeChem` (standardized to Bioregistry
prefix [`pdb-ccd`](https://bioregistry.io/pdb-ccd)) that
did not match the standard pattern `^\w{1,3}$`.

| external_xref       |   usages_count | usages                                                    |
|---------------------|----------------|-----------------------------------------------------------|
| `PDBeChem:MET_LFOH` |              1 | [CHEBI:16643](http://purl.obolibrary.org/obo/CHEBI_16643) |

## `PRO`: Protein Ontology

Overall, there were 9 invalid
xrefs to external prefixed with `PRO` (standardized to Bioregistry
prefix [`pr`](https://bioregistry.io/pr)) that
did not match the standard pattern `^(?:\d{9}|[OPQ][0-9][A-Z0-9]{3}[0-9](?:-\d+)?|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2}(?:-\d+)?)$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PRO:DAN`       |              6 | [PR:000000001](http://purl.obolibrary.org/obo/PR_000000001), [PR:000000001](http://purl.obolibrary.org/obo/PR_000000001), [PR:000050323](http://purl.obolibrary.org/obo/PR_000050323), [PR:000050323](http://purl.obolibrary.org/obo/PR_000050323), [PR:000050384](http://purl.obolibrary.org/obo/PR_000050384), ... |
| `PRO:DNx`       |              2 | [PR:000003918](http://purl.obolibrary.org/obo/PR_000003918), [PR:000003918](http://purl.obolibrary.org/obo/PR_000003918)                                                                                                                                                                                             |
| `PRO:WCB`       |              1 | [PR:000000001](http://purl.obolibrary.org/obo/PR_000000001)                                                                                                                                                                                                                                                          |

## `SO`: Sequence types and features ontology

Overall, there were 2 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                                                                                           |
|----------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `SO:immuno_workshop` |              2 | [SO:0000704](http://purl.obolibrary.org/obo/SO_0000704), [SO:0001025](http://purl.obolibrary.org/obo/SO_0001025) |

