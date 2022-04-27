# vsao

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `vsao`.


## `GO`: Gene Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                                   |   usages_count | usages                                                                                     |
|-------------------------------------------------|----------------|--------------------------------------------------------------------------------------------|
| `GO:('GO', '[GOC:mtg_sensu, ISBN:0198547684]')` |              1 | [http://purl.obolibrary.org/obo/VSAO_0000021](http://purl.obolibrary.org/obo/VSAO_0000021) |
| `GO:('GO', 'curator')`                          |              1 | [http://purl.obolibrary.org/obo/VSAO_0000092](http://purl.obolibrary.org/obo/VSAO_0000092) |

## `UBERON`: Uber Anatomy Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `UBERON` (standardized to Bioregistry
prefix [`uberon`](https://bioregistry.io/uberon)) that
did not match the standard pattern `^\d+$`.

| external_xref              |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UBERON:('UBERON', 'cjm')` |              7 | [http://purl.obolibrary.org/obo/VSAO_0000076](http://purl.obolibrary.org/obo/VSAO_0000076), [http://purl.obolibrary.org/obo/VSAO_0000155](http://purl.obolibrary.org/obo/VSAO_0000155), [http://purl.obolibrary.org/obo/VSAO_0000156](http://purl.obolibrary.org/obo/VSAO_0000156), [http://purl.obolibrary.org/obo/VSAO_0000303](http://purl.obolibrary.org/obo/VSAO_0000303), [http://purl.obolibrary.org/obo/VSAO_0000304](http://purl.obolibrary.org/obo/VSAO_0000304), ... |

## `ZFIN`: Zebrafish Information Network Gene

Overall, there were 3 invalid
xrefs to external prefixed with `ZFIN` (standardized to Bioregistry
prefix [`zfin`](https://bioregistry.io/zfin)) that
did not match the standard pattern `^ZDB\-\w+\-\d+\-\d+$`.

| external_xref              |   usages_count | usages                                                                                                                                                                                                                                                                             |
|----------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ZFIN:('ZFIN', 'curator')` |              3 | [http://purl.obolibrary.org/obo/VSAO_0000001](http://purl.obolibrary.org/obo/VSAO_0000001), [http://purl.obolibrary.org/obo/VSAO_0000164](http://purl.obolibrary.org/obo/VSAO_0000164), [http://purl.obolibrary.org/obo/VSAO_0000178](http://purl.obolibrary.org/obo/VSAO_0000178) |

