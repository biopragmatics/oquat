# eco

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `eco`. See the [GitHub repository](https://github.com/evidenceontology/evidenceontology).


## `DisProt`: DisProt

Overall, there were 7 invalid
xrefs to external prefixed with `DisProt` (standardized to Bioregistry
prefix [`disprot`](https://bioregistry.io/disprot)) that
did not match the standard pattern `^DP\d{5}$`.

| external_xref                           |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DisProt:('DisProt', 'BalintMeszaros')` |              7 | [http://purl.obolibrary.org/obo/ECO_0006183](http://purl.obolibrary.org/obo/ECO_0006183), [http://purl.obolibrary.org/obo/ECO_0006185](http://purl.obolibrary.org/obo/ECO_0006185), [http://purl.obolibrary.org/obo/ECO_0006187](http://purl.obolibrary.org/obo/ECO_0006187), [http://purl.obolibrary.org/obo/ECO_0006188](http://purl.obolibrary.org/obo/ECO_0006188), [http://purl.obolibrary.org/obo/ECO_0006189](http://purl.obolibrary.org/obo/ECO_0006189), ... |

## `ECO`: Evidence ontology

Overall, there were 1,411 invalid
xrefs to external prefixed with `ECO` (standardized to Bioregistry
prefix [`eco`](https://bioregistry.io/eco)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ECO:('ECO', 'RCT')` |            718 | [http://purl.obolibrary.org/obo/ECO_0000009](http://purl.obolibrary.org/obo/ECO_0000009), [http://purl.obolibrary.org/obo/ECO_0000011](http://purl.obolibrary.org/obo/ECO_0000011), [http://purl.obolibrary.org/obo/ECO_0000033](http://purl.obolibrary.org/obo/ECO_0000033), [http://purl.obolibrary.org/obo/ECO_0000053](http://purl.obolibrary.org/obo/ECO_0000053), [http://purl.obolibrary.org/obo/ECO_0000054](http://purl.obolibrary.org/obo/ECO_0000054), ... |
| `ECO:('ECO', 'SN')`  |            328 | [http://purl.obolibrary.org/obo/ECO_0000001](http://purl.obolibrary.org/obo/ECO_0000001), [http://purl.obolibrary.org/obo/ECO_0000002](http://purl.obolibrary.org/obo/ECO_0000002), [http://purl.obolibrary.org/obo/ECO_0000018](http://purl.obolibrary.org/obo/ECO_0000018), [http://purl.obolibrary.org/obo/ECO_0000021](http://purl.obolibrary.org/obo/ECO_0000021), [http://purl.obolibrary.org/obo/ECO_0000028](http://purl.obolibrary.org/obo/ECO_0000028), ... |
| `ECO:('ECO', 'MCC')` |            297 | [http://purl.obolibrary.org/obo/ECO_0000000](http://purl.obolibrary.org/obo/ECO_0000000), [http://purl.obolibrary.org/obo/ECO_0000007](http://purl.obolibrary.org/obo/ECO_0000007), [http://purl.obolibrary.org/obo/ECO_0000008](http://purl.obolibrary.org/obo/ECO_0000008), [http://purl.obolibrary.org/obo/ECO_0000019](http://purl.obolibrary.org/obo/ECO_0000019), [http://purl.obolibrary.org/obo/ECO_0000020](http://purl.obolibrary.org/obo/ECO_0000020), ... |
| `ECO:('ECO', 'SW')`  |             58 | [http://purl.obolibrary.org/obo/ECO_0000085](http://purl.obolibrary.org/obo/ECO_0000085), [http://purl.obolibrary.org/obo/ECO_0000095](http://purl.obolibrary.org/obo/ECO_0000095), [http://purl.obolibrary.org/obo/ECO_0000096](http://purl.obolibrary.org/obo/ECO_0000096), [http://purl.obolibrary.org/obo/ECO_0000106](http://purl.obolibrary.org/obo/ECO_0000106), [http://purl.obolibrary.org/obo/ECO_0000109](http://purl.obolibrary.org/obo/ECO_0000109), ... |
| `ECO:('ECO', 'KAV')` |              3 | [http://purl.obolibrary.org/obo/ECO_0000003](http://purl.obolibrary.org/obo/ECO_0000003), [http://purl.obolibrary.org/obo/ECO_0000154](http://purl.obolibrary.org/obo/ECO_0000154), [http://purl.obolibrary.org/obo/ECO_0000164](http://purl.obolibrary.org/obo/ECO_0000164)                                                                                                                                                                                          |
| `ECO:('ECO', 'KIM')` |              2 | [http://purl.obolibrary.org/obo/ECO_0000004](http://purl.obolibrary.org/obo/ECO_0000004), [http://purl.obolibrary.org/obo/ECO_0000096](http://purl.obolibrary.org/obo/ECO_0000096)                                                                                                                                                                                                                                                                                    |
| `ECO:('ECO', 'RCJ')` |              2 | [http://purl.obolibrary.org/obo/ECO_0001828](http://purl.obolibrary.org/obo/ECO_0001828), [http://purl.obolibrary.org/obo/ECO_0007850](http://purl.obolibrary.org/obo/ECO_0007850)                                                                                                                                                                                                                                                                                    |
| `ECO:('ECO', 'MG')`  |              2 | [http://purl.obolibrary.org/obo/ECO_0006186](http://purl.obolibrary.org/obo/ECO_0006186), [http://purl.obolibrary.org/obo/ECO_0006252](http://purl.obolibrary.org/obo/ECO_0006252)                                                                                                                                                                                                                                                                                    |
| `ECO:('ECO', 'cjm')` |              1 | [http://purl.obolibrary.org/obo/ECO_0000501](http://purl.obolibrary.org/obo/ECO_0000501)                                                                                                                                                                                                                                                                                                                                                                              |

## `EDAM`: Bioinformatics operations, data types, formats, identifiers and topics

Overall, there were 1 invalid
xrefs to external prefixed with `EDAM` (standardized to Bioregistry
prefix [`edam`](https://bioregistry.io/edam)) that
did not match the standard pattern `^(data|topic|operation|format)\_\d{4}$`.

| external_xref                 |   usages_count | usages                                                                                   |
|-------------------------------|----------------|------------------------------------------------------------------------------------------|
| `EDAM:('EDAM', 'topic:3298')` |              1 | [http://purl.obolibrary.org/obo/ECO_0007075](http://purl.obolibrary.org/obo/ECO_0007075) |

## `GO`: Gene Ontology

Overall, there were 7 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref      |   usages_count | usages                                                                                                                                                                                                                                                                       |
|--------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:('GO', 'IEP')` |              3 | [http://purl.obolibrary.org/obo/ECO_0000008](http://purl.obolibrary.org/obo/ECO_0000008), [http://purl.obolibrary.org/obo/ECO_0007006](http://purl.obolibrary.org/obo/ECO_0007006), [http://purl.obolibrary.org/obo/ECO_0007007](http://purl.obolibrary.org/obo/ECO_0007007) |
| `GO:('GO', 'IMP')` |              3 | [http://purl.obolibrary.org/obo/ECO_0000015](http://purl.obolibrary.org/obo/ECO_0000015), [http://purl.obolibrary.org/obo/ECO_0007000](http://purl.obolibrary.org/obo/ECO_0007000), [http://purl.obolibrary.org/obo/ECO_0007001](http://purl.obolibrary.org/obo/ECO_0007001) |
| `GO:('GO', 'TAS')` |              1 | [http://purl.obolibrary.org/obo/ECO_0000033](http://purl.obolibrary.org/obo/ECO_0000033)                                                                                                                                                                                     |

## `HPO`: Human Phenotype Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `HPO` (standardized to Bioregistry
prefix [`hp`](https://bioregistry.io/hp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                                                                   |
|----------------------|----------------|------------------------------------------------------------------------------------------|
| `HPO:('HPO', 'PCS')` |              1 | [http://purl.obolibrary.org/obo/ECO_0006017](http://purl.obolibrary.org/obo/ECO_0006017) |
| `HPO:('HPO', 'ICE')` |              1 | [http://purl.obolibrary.org/obo/ECO_0006019](http://purl.obolibrary.org/obo/ECO_0006019) |

## `PMC`: Pubmed Central

Overall, there were 22 invalid
xrefs to external prefixed with `PMC` (standardized to Bioregistry
prefix [`pmc`](https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref            |   usages_count | usages                                                                                                                                                                             |
|--------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PMC:('PMC', '102612')`  |              2 | [http://purl.obolibrary.org/obo/ECO_0000138](http://purl.obolibrary.org/obo/ECO_0000138), [http://purl.obolibrary.org/obo/ECO_0006084](http://purl.obolibrary.org/obo/ECO_0006084) |
| `PMC:('PMC', '4029002')` |              1 | [http://purl.obolibrary.org/obo/ECO_0000010](http://purl.obolibrary.org/obo/ECO_0000010)                                                                                           |
| `PMC:('PMC', '2686546')` |              1 | [http://purl.obolibrary.org/obo/ECO_0000029](http://purl.obolibrary.org/obo/ECO_0000029)                                                                                           |
| `PMC:('PMC', '38513')`   |              1 | [http://purl.obolibrary.org/obo/ECO_0000077](http://purl.obolibrary.org/obo/ECO_0000077)                                                                                           |
| `PMC:('PMC', '2881125')` |              1 | [http://purl.obolibrary.org/obo/ECO_0000359](http://purl.obolibrary.org/obo/ECO_0000359)                                                                                           |
| `PMC:('PMC', '3929704')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001004](http://purl.obolibrary.org/obo/ECO_0001004)                                                                                           |
| `PMC:('PMC', '3478843')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001008](http://purl.obolibrary.org/obo/ECO_0001008)                                                                                           |
| `PMC:('PMC', '3169266')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001011](http://purl.obolibrary.org/obo/ECO_0001011)                                                                                           |
| `PMC:('PMC', '3185625')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001022](http://purl.obolibrary.org/obo/ECO_0001022)                                                                                           |
| `PMC:('PMC', '3074624')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001026](http://purl.obolibrary.org/obo/ECO_0001026)                                                                                           |
| `PMC:('PMC', '3572410')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001030](http://purl.obolibrary.org/obo/ECO_0001030)                                                                                           |
| `PMC:('PMC', '4401164')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001039](http://purl.obolibrary.org/obo/ECO_0001039)                                                                                           |
| `PMC:('PMC', '2217636')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001042](http://purl.obolibrary.org/obo/ECO_0001042)                                                                                           |
| `PMC:('PMC', '346675')`  |              1 | [http://purl.obolibrary.org/obo/ECO_0001047](http://purl.obolibrary.org/obo/ECO_0001047)                                                                                           |
| `PMC:('PMC', '2782548')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001091](http://purl.obolibrary.org/obo/ECO_0001091)                                                                                           |
| `PMC:('PMC', '1534009')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001102](http://purl.obolibrary.org/obo/ECO_0001102)                                                                                           |
| `PMC:('PMC', '3149870')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001107](http://purl.obolibrary.org/obo/ECO_0001107)                                                                                           |
| `PMC:('PMC', '1828913')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001117](http://purl.obolibrary.org/obo/ECO_0001117)                                                                                           |
| `PMC:('PMC', '1808921')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001129](http://purl.obolibrary.org/obo/ECO_0001129)                                                                                           |
| `PMC:('PMC', '3908118')` |              1 | [http://purl.obolibrary.org/obo/ECO_0005008](http://purl.obolibrary.org/obo/ECO_0005008)                                                                                           |
| `PMC:('PMC', '3667641')` |              1 | [http://purl.obolibrary.org/obo/ECO_0005021](http://purl.obolibrary.org/obo/ECO_0005021)                                                                                           |

## `PMCID`: Pubmed Central

Overall, there were 1 invalid
xrefs to external prefixed with `PMCID` (standardized to Bioregistry
prefix [`pmc`](https://bioregistry.io/pmc)) that
did not match the standard pattern `^PMC\d+$`.

| external_xref                |   usages_count | usages                                                                                   |
|------------------------------|----------------|------------------------------------------------------------------------------------------|
| `PMCID:('PMCID', '3277431')` |              1 | [http://purl.obolibrary.org/obo/ECO_0001811](http://purl.obolibrary.org/obo/ECO_0001811) |

## `PMID`: PubMed

Overall, there were 2 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                |   usages_count | usages                                                                                   |
|------------------------------|----------------|------------------------------------------------------------------------------------------|
| `PMID:('PMID', ' 16428685')` |              1 | [http://purl.obolibrary.org/obo/ECO_0006163](http://purl.obolibrary.org/obo/ECO_0006163) |
| `PMID:('PMID', ' 23036848')` |              1 | [http://purl.obolibrary.org/obo/ECO_0006163](http://purl.obolibrary.org/obo/ECO_0006163) |

## `PomBase`: PomBase

Overall, there were 1 invalid
xrefs to external prefixed with `PomBase` (standardized to Bioregistry
prefix [`pombase`](https://bioregistry.io/pombase)) that
did not match the standard pattern `^S\w+(\.)?\w+(\.)?$`.

| external_xref                |   usages_count | usages                                                                                   |
|------------------------------|----------------|------------------------------------------------------------------------------------------|
| `PomBase:('PomBase', 'MAH')` |              1 | [http://purl.obolibrary.org/obo/ECO_0000095](http://purl.obolibrary.org/obo/ECO_0000095) |

## `PSI-MI`: Molecular Interactions Controlled Vocabulary

Overall, there were 3 invalid
xrefs to external prefixed with `PSI-MI` (standardized to Bioregistry
prefix [`mi`](https://bioregistry.io/mi)) that
did not match the standard pattern `^\d{4}$`.

| external_xref                  |   usages_count | usages                                                                                   |
|--------------------------------|----------------|------------------------------------------------------------------------------------------|
| `PSI-MI:('PSI-MI', 'MI:0400')` |              1 | [http://purl.obolibrary.org/obo/ECO_0000023](http://purl.obolibrary.org/obo/ECO_0000023) |
| `PSI-MI:('PSI-MI', 'MI:0090')` |              1 | [http://purl.obolibrary.org/obo/ECO_0000025](http://purl.obolibrary.org/obo/ECO_0000025) |
| `PSI-MI:('PSI-MI', 'MI:0432')` |              1 | [http://purl.obolibrary.org/obo/ECO_0000066](http://purl.obolibrary.org/obo/ECO_0000066) |

