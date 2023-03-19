# mpath

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `mpath`. See the [GitHub repository](https://github.com/PaulNSchofield/mpath).


## `ICD-O`: International Classification of Diseases for Oncology

Overall, there were 1 invalid
xrefs to external prefixed with `ICD-O` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref    |   usages_count | usages                                                |
|------------------|----------------|-------------------------------------------------------|
| `ICD-O:M-8900/0` |              1 | [MPATH:722](http://purl.obolibrary.org/obo/MPATH_722) |

## `ICDO`: International Classification of Diseases for Oncology

Overall, there were 1 invalid
xrefs to external prefixed with `ICDO` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref   |   usages_count | usages                                                |
|-----------------|----------------|-------------------------------------------------------|
| `ICDO:M-8822/1` |              1 | [MPATH:723](http://purl.obolibrary.org/obo/MPATH_723) |

## `ISBN`: International Standard Book Number

Overall, there were 1 invalid
xrefs to external prefixed with `ISBN` (standardized to Bioregistry
prefix [`isbn`](https://bioregistry.io/isbn)) that
did not match the standard pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`.

| external_xref          |   usages_count | usages                                                |
|------------------------|----------------|-------------------------------------------------------|
| `ISBN: 0-7216-2921-0.` |              1 | [MPATH:859](http://purl.obolibrary.org/obo/MPATH_859) |

## `MPATH`: Mouse pathology ontology

Overall, there were 143 invalid
xrefs to external prefixed with `MPATH` (standardized to Bioregistry
prefix [`mpath`](https://bioregistry.io/mpath)) that
did not match the standard pattern `^\d+$`.

| external_xref               |   usages_count | usages                                                                                                                                                                                                                                                                                 |
|-----------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MPATH:curation`            |             53 | [MPATH:652](http://purl.obolibrary.org/obo/MPATH_652), [MPATH:811](http://purl.obolibrary.org/obo/MPATH_811), [MPATH:812](http://purl.obolibrary.org/obo/MPATH_812), [MPATH:813](http://purl.obolibrary.org/obo/MPATH_813), [MPATH:814](http://purl.obolibrary.org/obo/MPATH_814), ... |
| `MPATH:Sundberg`            |             51 | [MPATH:670](http://purl.obolibrary.org/obo/MPATH_670), [MPATH:733](http://purl.obolibrary.org/obo/MPATH_733), [MPATH:735](http://purl.obolibrary.org/obo/MPATH_735), [MPATH:739](http://purl.obolibrary.org/obo/MPATH_739), [MPATH:740](http://purl.obolibrary.org/obo/MPATH_740), ... |
| `MPATH:PNS`                 |             17 | [MPATH:764](http://purl.obolibrary.org/obo/MPATH_764), [MPATH:770](http://purl.obolibrary.org/obo/MPATH_770), [MPATH:771](http://purl.obolibrary.org/obo/MPATH_771), [MPATH:772](http://purl.obolibrary.org/obo/MPATH_772), [MPATH:773](http://purl.obolibrary.org/obo/MPATH_773), ... |
| `MPATH:Pathology Committee` |             11 | [MPATH:724](http://purl.obolibrary.org/obo/MPATH_724), [MPATH:874](http://purl.obolibrary.org/obo/MPATH_874), [MPATH:875](http://purl.obolibrary.org/obo/MPATH_875), [MPATH:876](http://purl.obolibrary.org/obo/MPATH_876), [MPATH:878](http://purl.obolibrary.org/obo/MPATH_878), ... |
| `MPATH:JPS`                 |              4 | [MPATH:882](http://purl.obolibrary.org/obo/MPATH_882), [MPATH:883](http://purl.obolibrary.org/obo/MPATH_883), [MPATH:884](http://purl.obolibrary.org/obo/MPATH_884), [MPATH:888](http://purl.obolibrary.org/obo/MPATH_888)                                                             |
| `MPATH:<new dbxref>`        |              3 | [MPATH:770](http://purl.obolibrary.org/obo/MPATH_770), [MPATH:771](http://purl.obolibrary.org/obo/MPATH_771), [MPATH:772](http://purl.obolibrary.org/obo/MPATH_772)                                                                                                                    |
| `MPATH:Curation`            |              1 | [MPATH:656](http://purl.obolibrary.org/obo/MPATH_656)                                                                                                                                                                                                                                  |
| `MPATH::Sundberg`           |              1 | [MPATH:746](http://purl.obolibrary.org/obo/MPATH_746)                                                                                                                                                                                                                                  |
| `MPATH:Pathology committee` |              1 | [MPATH:809](http://purl.obolibrary.org/obo/MPATH_809)                                                                                                                                                                                                                                  |
| `MPATH:curationf>`          |              1 | [MPATH:865](http://purl.obolibrary.org/obo/MPATH_865)                                                                                                                                                                                                                                  |

## `mpath`: Mouse pathology ontology

Overall, there were 2 invalid
xrefs to external prefixed with `mpath` (standardized to Bioregistry
prefix [`mpath`](https://bioregistry.io/mpath)) that
did not match the standard pattern `^\d+$`.

| external_xref        |   usages_count | usages                                                |
|----------------------|----------------|-------------------------------------------------------|
| `mpath:<new dbxref>` |              1 | [MPATH:775](http://purl.obolibrary.org/obo/MPATH_775) |
| `mpath:curation`     |              1 | [MPATH:833](http://purl.obolibrary.org/obo/MPATH_833) |

## `PMCID`: PubMed Central

Overall, there were 1 invalid
xrefs to external prefixed with `PMCID` (standardized to Bioregistry
prefix [`pmc`](https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref    |   usages_count | usages                                                |
|------------------|----------------|-------------------------------------------------------|
| `PMCID: 1964945` |              1 | [MPATH:499](http://purl.obolibrary.org/obo/MPATH_499) |

## `PMID`: PubMed

Overall, there were 2 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref       |   usages_count | usages                                                |
|---------------------|----------------|-------------------------------------------------------|
| `PMID: 11794381`    |              1 | [MPATH:40](http://purl.obolibrary.org/obo/MPATH_40)   |
| `PMID:    21191096` |              1 | [MPATH:815](http://purl.obolibrary.org/obo/MPATH_815) |

