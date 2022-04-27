# ensemblglossary

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `ensemblglossary`.


## `SO`: Sequence types and features ontology

Overall, there were 3 invalid
xrefs to external prefixed with `SO` (standardized to Bioregistry
prefix [`so`](https://bioregistry.io/so)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                                  |   usages_count | usages                                                                                             |
|------------------------------------------------|----------------|----------------------------------------------------------------------------------------------------|
| `SO:('SO', '0002109, SO:0002107, SO:0002108')` |              1 | [http://ensembl.org/glossary/ENSGLOSSARY_0000050](http://ensembl.org/glossary/ENSGLOSSARY_0000050) |
| `SO:('SO', '0002105, SO:0002106')`             |              1 | [http://ensembl.org/glossary/ENSGLOSSARY_0000051](http://ensembl.org/glossary/ENSGLOSSARY_0000051) |
| `SO:('SO', '0000853, FHOM_0000007')`           |              1 | [http://ensembl.org/glossary/ENSGLOSSARY_0000080](http://ensembl.org/glossary/ENSGLOSSARY_0000080) |

