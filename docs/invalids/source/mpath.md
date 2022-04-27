# mpath

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `mpath`. See the [GitHub repository](https://github.com/PaulNSchofield/mpath).


## `ICD-O`: International Classification of Diseases for Oncology

Overall, there were 1 invalid
xrefs to external prefixed with `ICD-O` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref                 |   usages_count | usages                                                                               |
|-------------------------------|----------------|--------------------------------------------------------------------------------------|
| `ICD-O:('ICD-O', 'M-8900/0')` |              1 | [http://purl.obolibrary.org/obo/MPATH_722](http://purl.obolibrary.org/obo/MPATH_722) |

## `ICDO`: International Classification of Diseases for Oncology

Overall, there were 1 invalid
xrefs to external prefixed with `ICDO` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref               |   usages_count | usages                                                                               |
|-----------------------------|----------------|--------------------------------------------------------------------------------------|
| `ICDO:('ICDO', 'M-8822/1')` |              1 | [http://purl.obolibrary.org/obo/MPATH_723](http://purl.obolibrary.org/obo/MPATH_723) |

## `ISBN`: International Standard Book Number

Overall, there were 1 invalid
xrefs to external prefixed with `ISBN` (standardized to Bioregistry
prefix [`isbn`](https://bioregistry.io/isbn)) that
did not match the standard pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`.

| external_xref                      |   usages_count | usages                                                                               |
|------------------------------------|----------------|--------------------------------------------------------------------------------------|
| `ISBN:('ISBN', ' 0-7216-2921-0.')` |              1 | [http://purl.obolibrary.org/obo/MPATH_859](http://purl.obolibrary.org/obo/MPATH_859) |

## `MPATH`: Mouse pathology ontology

Overall, there were 143 invalid
xrefs to external prefixed with `MPATH` (standardized to Bioregistry
prefix [`mpath`](https://bioregistry.io/mpath)) that
did not match the standard pattern `^\d+$`.

| external_xref                            |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MPATH:('MPATH', 'curation')`            |             53 | [http://purl.obolibrary.org/obo/MPATH_652](http://purl.obolibrary.org/obo/MPATH_652), [http://purl.obolibrary.org/obo/MPATH_811](http://purl.obolibrary.org/obo/MPATH_811), [http://purl.obolibrary.org/obo/MPATH_812](http://purl.obolibrary.org/obo/MPATH_812), [http://purl.obolibrary.org/obo/MPATH_813](http://purl.obolibrary.org/obo/MPATH_813), [http://purl.obolibrary.org/obo/MPATH_814](http://purl.obolibrary.org/obo/MPATH_814), ... |
| `MPATH:('MPATH', 'Sundberg')`            |             51 | [http://purl.obolibrary.org/obo/MPATH_670](http://purl.obolibrary.org/obo/MPATH_670), [http://purl.obolibrary.org/obo/MPATH_733](http://purl.obolibrary.org/obo/MPATH_733), [http://purl.obolibrary.org/obo/MPATH_735](http://purl.obolibrary.org/obo/MPATH_735), [http://purl.obolibrary.org/obo/MPATH_739](http://purl.obolibrary.org/obo/MPATH_739), [http://purl.obolibrary.org/obo/MPATH_740](http://purl.obolibrary.org/obo/MPATH_740), ... |
| `MPATH:('MPATH', 'PNS')`                 |             17 | [http://purl.obolibrary.org/obo/MPATH_764](http://purl.obolibrary.org/obo/MPATH_764), [http://purl.obolibrary.org/obo/MPATH_770](http://purl.obolibrary.org/obo/MPATH_770), [http://purl.obolibrary.org/obo/MPATH_771](http://purl.obolibrary.org/obo/MPATH_771), [http://purl.obolibrary.org/obo/MPATH_772](http://purl.obolibrary.org/obo/MPATH_772), [http://purl.obolibrary.org/obo/MPATH_773](http://purl.obolibrary.org/obo/MPATH_773), ... |
| `MPATH:('MPATH', 'Pathology Committee')` |             11 | [http://purl.obolibrary.org/obo/MPATH_724](http://purl.obolibrary.org/obo/MPATH_724), [http://purl.obolibrary.org/obo/MPATH_874](http://purl.obolibrary.org/obo/MPATH_874), [http://purl.obolibrary.org/obo/MPATH_875](http://purl.obolibrary.org/obo/MPATH_875), [http://purl.obolibrary.org/obo/MPATH_876](http://purl.obolibrary.org/obo/MPATH_876), [http://purl.obolibrary.org/obo/MPATH_878](http://purl.obolibrary.org/obo/MPATH_878), ... |
| `MPATH:('MPATH', 'JPS')`                 |              4 | [http://purl.obolibrary.org/obo/MPATH_882](http://purl.obolibrary.org/obo/MPATH_882), [http://purl.obolibrary.org/obo/MPATH_883](http://purl.obolibrary.org/obo/MPATH_883), [http://purl.obolibrary.org/obo/MPATH_884](http://purl.obolibrary.org/obo/MPATH_884), [http://purl.obolibrary.org/obo/MPATH_888](http://purl.obolibrary.org/obo/MPATH_888)                                                                                            |
| `MPATH:('MPATH', '<new dbxref>')`        |              3 | [http://purl.obolibrary.org/obo/MPATH_770](http://purl.obolibrary.org/obo/MPATH_770), [http://purl.obolibrary.org/obo/MPATH_771](http://purl.obolibrary.org/obo/MPATH_771), [http://purl.obolibrary.org/obo/MPATH_772](http://purl.obolibrary.org/obo/MPATH_772)                                                                                                                                                                                  |
| `MPATH:('MPATH', 'Curation')`            |              1 | [http://purl.obolibrary.org/obo/MPATH_656](http://purl.obolibrary.org/obo/MPATH_656)                                                                                                                                                                                                                                                                                                                                                              |
| `MPATH:('MPATH', ':Sundberg')`           |              1 | [http://purl.obolibrary.org/obo/MPATH_746](http://purl.obolibrary.org/obo/MPATH_746)                                                                                                                                                                                                                                                                                                                                                              |
| `MPATH:('MPATH', 'Pathology committee')` |              1 | [http://purl.obolibrary.org/obo/MPATH_809](http://purl.obolibrary.org/obo/MPATH_809)                                                                                                                                                                                                                                                                                                                                                              |
| `MPATH:('MPATH', 'curationf>')`          |              1 | [http://purl.obolibrary.org/obo/MPATH_865](http://purl.obolibrary.org/obo/MPATH_865)                                                                                                                                                                                                                                                                                                                                                              |

## `mpath`: Mouse pathology ontology

Overall, there were 2 invalid
xrefs to external prefixed with `mpath` (standardized to Bioregistry
prefix [`mpath`](https://bioregistry.io/mpath)) that
did not match the standard pattern `^\d+$`.

| external_xref                     |   usages_count | usages                                                                               |
|-----------------------------------|----------------|--------------------------------------------------------------------------------------|
| `mpath:('mpath', '<new dbxref>')` |              1 | [http://purl.obolibrary.org/obo/MPATH_775](http://purl.obolibrary.org/obo/MPATH_775) |
| `mpath:('mpath', 'curation')`     |              1 | [http://purl.obolibrary.org/obo/MPATH_833](http://purl.obolibrary.org/obo/MPATH_833) |

## `PMCID`: Pubmed Central

Overall, there were 1 invalid
xrefs to external prefixed with `PMCID` (standardized to Bioregistry
prefix [`pmc`](https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref                 |   usages_count | usages                                                                               |
|-------------------------------|----------------|--------------------------------------------------------------------------------------|
| `PMCID:('PMCID', ' 1964945')` |              1 | [http://purl.obolibrary.org/obo/MPATH_499](http://purl.obolibrary.org/obo/MPATH_499) |

## `PMID`: PubMed

Overall, there were 2 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                   |   usages_count | usages                                                                               |
|---------------------------------|----------------|--------------------------------------------------------------------------------------|
| `PMID:('PMID', ' 11794381')`    |              1 | [http://purl.obolibrary.org/obo/MPATH_40](http://purl.obolibrary.org/obo/MPATH_40)   |
| `PMID:('PMID', '    21191096')` |              1 | [http://purl.obolibrary.org/obo/MPATH_815](http://purl.obolibrary.org/obo/MPATH_815) |

