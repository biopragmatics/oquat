# mpath

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `mpath`. See the [GitHub repository](https://github.com/PaulNSchofield/mpath).


## `ICD-O`: International Classification of Diseases for Oncology

Overall, there were 1 invalid
xrefs to external prefixed with `ICD-O` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref    |   usages_count | usages                                        |
|------------------|----------------|-----------------------------------------------|
| `ICD-O:M-8900/0` |              1 | [MPATH:722](https://bioregistry.io/MPATH:722) |

## `ICDO`: International Classification of Diseases for Oncology

Overall, there were 1 invalid
xrefs to external prefixed with `ICDO` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref   |   usages_count | usages                                        |
|-----------------|----------------|-----------------------------------------------|
| `ICDO:M-8822/1` |              1 | [MPATH:723](https://bioregistry.io/MPATH:723) |

## `ISBN`: International Standard Book Number

Overall, there were 1 invalid
xrefs to external prefixed with `ISBN` (standardized to Bioregistry
prefix [`isbn`](https://bioregistry.io/isbn)) that
did not match the standard pattern `^(ISBN)?(-13|-10)?[:]?[ ]?(\d{2,3}[ -]?)?\d{1,5}[ -]?\d{1,7}[ -]?\d{1,6}[ -]?(\d|X)$`.

| external_xref          |   usages_count | usages                                        |
|------------------------|----------------|-----------------------------------------------|
| `ISBN: 0-7216-2921-0.` |              1 | [MPATH:859](https://bioregistry.io/MPATH:859) |

## `MPATH`: Mouse pathology ontology

Overall, there were 143 invalid
xrefs to external prefixed with `MPATH` (standardized to Bioregistry
prefix [`mpath`](https://bioregistry.io/mpath)) that
did not match the standard pattern `^\d+$`.

| external_xref               |   usages_count | usages                                                                                                                                                                                                                                         |
|-----------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MPATH:curation`            |             53 | [MPATH:652](https://bioregistry.io/MPATH:652), [MPATH:811](https://bioregistry.io/MPATH:811), [MPATH:812](https://bioregistry.io/MPATH:812), [MPATH:813](https://bioregistry.io/MPATH:813), [MPATH:814](https://bioregistry.io/MPATH:814), ... |
| `MPATH:Sundberg`            |             51 | [MPATH:670](https://bioregistry.io/MPATH:670), [MPATH:733](https://bioregistry.io/MPATH:733), [MPATH:735](https://bioregistry.io/MPATH:735), [MPATH:739](https://bioregistry.io/MPATH:739), [MPATH:740](https://bioregistry.io/MPATH:740), ... |
| `MPATH:PNS`                 |             17 | [MPATH:764](https://bioregistry.io/MPATH:764), [MPATH:770](https://bioregistry.io/MPATH:770), [MPATH:771](https://bioregistry.io/MPATH:771), [MPATH:772](https://bioregistry.io/MPATH:772), [MPATH:773](https://bioregistry.io/MPATH:773), ... |
| `MPATH:Pathology Committee` |             11 | [MPATH:724](https://bioregistry.io/MPATH:724), [MPATH:874](https://bioregistry.io/MPATH:874), [MPATH:875](https://bioregistry.io/MPATH:875), [MPATH:876](https://bioregistry.io/MPATH:876), [MPATH:878](https://bioregistry.io/MPATH:878), ... |
| `MPATH:JPS`                 |              4 | [MPATH:882](https://bioregistry.io/MPATH:882), [MPATH:883](https://bioregistry.io/MPATH:883), [MPATH:884](https://bioregistry.io/MPATH:884), [MPATH:888](https://bioregistry.io/MPATH:888)                                                     |
| `MPATH:<new dbxref>`        |              3 | [MPATH:770](https://bioregistry.io/MPATH:770), [MPATH:771](https://bioregistry.io/MPATH:771), [MPATH:772](https://bioregistry.io/MPATH:772)                                                                                                    |
| `MPATH:Curation`            |              1 | [MPATH:656](https://bioregistry.io/MPATH:656)                                                                                                                                                                                                  |
| `MPATH::Sundberg`           |              1 | [MPATH:746](https://bioregistry.io/MPATH:746)                                                                                                                                                                                                  |
| `MPATH:Pathology committee` |              1 | [MPATH:809](https://bioregistry.io/MPATH:809)                                                                                                                                                                                                  |
| `MPATH:curationf>`          |              1 | [MPATH:865](https://bioregistry.io/MPATH:865)                                                                                                                                                                                                  |

## `mpath`: Mouse pathology ontology

Overall, there were 2 invalid
xrefs to external prefixed with `mpath` (standardized to Bioregistry
prefix [`mpath`](https://bioregistry.io/mpath)) that
did not match the standard pattern `^\d+$`.

| external_xref        |   usages_count | usages                                        |
|----------------------|----------------|-----------------------------------------------|
| `mpath:<new dbxref>` |              1 | [MPATH:775](https://bioregistry.io/MPATH:775) |
| `mpath:curation`     |              1 | [MPATH:833](https://bioregistry.io/MPATH:833) |

## `PMCID`: Pubmed Central

Overall, there were 1 invalid
xrefs to external prefixed with `PMCID` (standardized to Bioregistry
prefix [`pmc`](https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref    |   usages_count | usages                                        |
|------------------|----------------|-----------------------------------------------|
| `PMCID: 1964945` |              1 | [MPATH:499](https://bioregistry.io/MPATH:499) |

## `PMID`: PubMed

Overall, there were 2 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref       |   usages_count | usages                                        |
|---------------------|----------------|-----------------------------------------------|
| `PMID: 11794381`    |              1 | [MPATH:40](https://bioregistry.io/MPATH:40)   |
| `PMID:    21191096` |              1 | [MPATH:815](https://bioregistry.io/MPATH:815) |

