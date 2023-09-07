# cmo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `cmo`. See the [GitHub repository](https://github.com/rat-genome-database/CMO-Clinical-Measurement-Ontology).


## `BRENDA`: BRENDA Enzyme

Overall, there were 1 invalid
xrefs to external prefixed with `BRENDA` (standardized to Bioregistry
prefix [`brenda`](https://bioregistry.io/brenda)) that
did not match the standard pattern `^((\d+\.-\.-\.-)|(\d+\.\d+\.-\.-)|(\d+\.\d+\.\d+\.-)|(\d+\.\d+\.\d+\.\d+))$`.

| external_xref      |   usages_count | usages                                                    |
|--------------------|----------------|-----------------------------------------------------------|
| `BRENDA:EC2.3.2.2` |              1 | [CMO:0001921](http://purl.obolibrary.org/obo/CMO_0001921) |

## `ECGOntology`: Electrocardiogram Ontology

Overall, there were 5 invalid
xrefs to external prefixed with `ECGOntology` (standardized to Bioregistry
prefix [`ecg`](https://bioregistry.io/ecg)) that
did not match the standard pattern `^\d+$`.

| external_xref              |   usages_count | usages                                                                                                                                                                                                                                                                                                |
|----------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ECGOntology:<new dbxref>` |              5 | [CMO:0000232](http://purl.obolibrary.org/obo/CMO_0000232), [CMO:0000233](http://purl.obolibrary.org/obo/CMO_0000233), [CMO:0000234](http://purl.obolibrary.org/obo/CMO_0000234), [CMO:0000235](http://purl.obolibrary.org/obo/CMO_0000235), [CMO:0000278](http://purl.obolibrary.org/obo/CMO_0000278) |

## `QTLdb`: Animal Genome QTL

Overall, there were 38 invalid
xrefs to external prefixed with `QTLdb` (standardized to Bioregistry
prefix [`qtldb`](https://bioregistry.io/qtldb)) that
did not match the standard pattern `^\d+$`.

| external_xref           |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `QTLdb:animal_QTL_data` |             19 | [CMO:0000396](http://purl.obolibrary.org/obo/CMO_0000396), [CMO:0000399](http://purl.obolibrary.org/obo/CMO_0000399), [CMO:0000403](http://purl.obolibrary.org/obo/CMO_0000403), [CMO:0000408](http://purl.obolibrary.org/obo/CMO_0000408), [CMO:0000415](http://purl.obolibrary.org/obo/CMO_0000415), ... |
| `QTLdb:CAP`             |             19 | [CMO:0000402](http://purl.obolibrary.org/obo/CMO_0000402), [CMO:0000453](http://purl.obolibrary.org/obo/CMO_0000453), [CMO:0001306](http://purl.obolibrary.org/obo/CMO_0001306), [CMO:0001307](http://purl.obolibrary.org/obo/CMO_0001307), [CMO:0001308](http://purl.obolibrary.org/obo/CMO_0001308), ... |

## `RGD`: Rat Genome Database

Overall, there were 192 invalid
xrefs to external prefixed with `RGD` (standardized to Bioregistry
prefix [`rgd`](https://bioregistry.io/rgd)) that
did not match the standard pattern `^\d{4,}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RGD:JRS`       |            114 | [CMO:0000068](http://purl.obolibrary.org/obo/CMO_0000068), [CMO:0000069](http://purl.obolibrary.org/obo/CMO_0000069), [CMO:0000070](http://purl.obolibrary.org/obo/CMO_0000070), [CMO:0000075](http://purl.obolibrary.org/obo/CMO_0000075), [CMO:0000179](http://purl.obolibrary.org/obo/CMO_0000179), ... |
| `RGD:MS`        |             75 | [CMO:0000011](http://purl.obolibrary.org/obo/CMO_0000011), [CMO:0000019](http://purl.obolibrary.org/obo/CMO_0000019), [CMO:0000035](http://purl.obolibrary.org/obo/CMO_0000035), [CMO:0000039](http://purl.obolibrary.org/obo/CMO_0000039), [CMO:0000040](http://purl.obolibrary.org/obo/CMO_0000040), ... |
| `RGD:SL`        |              3 | [CMO:0001037](http://purl.obolibrary.org/obo/CMO_0001037), [CMO:0001210](http://purl.obolibrary.org/obo/CMO_0001210), [CMO:0001492](http://purl.obolibrary.org/obo/CMO_0001492)                                                                                                                            |

