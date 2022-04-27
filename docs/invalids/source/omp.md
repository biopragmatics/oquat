# omp

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `omp`. See the [GitHub repository](https://github.com/microbialphenotypes/OMP-ontology).


## `APO`: Ascomycete phenotype ontology

Overall, there were 1 invalid
xrefs to external prefixed with `APO` (standardized to Bioregistry
prefix [`apo`](https://bioregistry.io/apo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref             |   usages_count | usages                                                                                   |
|---------------------------|----------------|------------------------------------------------------------------------------------------|
| `APO:('APO', ':0000051')` |              1 | [http://purl.obolibrary.org/obo/OMP_0007101](http://purl.obolibrary.org/obo/OMP_0007101) |

## `CHEBI`: Chemical Entities of Biological Interest

Overall, there were 2 invalid
xrefs to external prefixed with `CHEBI` (standardized to Bioregistry
prefix [`chebi`](https://bioregistry.io/chebi)) that
did not match the standard pattern `^\d+$`.

| external_xref                    |   usages_count | usages                                                                                   |
|----------------------------------|----------------|------------------------------------------------------------------------------------------|
| `CHEBI:('CHEBI', 'CHEBI:87649')` |              1 | [http://purl.obolibrary.org/obo/OMP_0007481](http://purl.obolibrary.org/obo/OMP_0007481) |
| `CHEBI:('CHEBI', ':4806')`       |              1 | [http://purl.obolibrary.org/obo/OMP_0007848](http://purl.obolibrary.org/obo/OMP_0007848) |

## `FYPO`: Fission Yeast Phenotype Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `FYPO` (standardized to Bioregistry
prefix [`fypo`](https://bioregistry.io/fypo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                   |   usages_count | usages                                                                                   |
|---------------------------------|----------------|------------------------------------------------------------------------------------------|
| `FYPO:('FYPO', 'FYPO:0003755')` |              1 | [http://purl.obolibrary.org/obo/OMP_0007746](http://purl.obolibrary.org/obo/OMP_0007746) |
| `FYPO:('FYPO', '1178')`         |              1 | [http://purl.obolibrary.org/obo/OMP_0007808](http://purl.obolibrary.org/obo/OMP_0007808) |
| `FYPO:('FYPO', '000064')`       |              1 | [http://purl.obolibrary.org/obo/OMP_0007701](http://purl.obolibrary.org/obo/OMP_0007701) |

## `GO`: Gene Ontology

Overall, there were 8 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref           |   usages_count | usages                                                                                                                                                                             |
|-------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GO:('GO', 'JG')`       |              2 | [http://purl.obolibrary.org/obo/OMP_0005181](http://purl.obolibrary.org/obo/OMP_0005181), [http://purl.obolibrary.org/obo/OMP_0005200](http://purl.obolibrary.org/obo/OMP_0005200) |
| `GO:('GO', ':0019835')` |              1 | [http://purl.obolibrary.org/obo/OMP_0005336](http://purl.obolibrary.org/obo/OMP_0005336)                                                                                           |
| `GO:('GO', '00140013')` |              1 | [http://purl.obolibrary.org/obo/OMP_0007562](http://purl.obolibrary.org/obo/OMP_0007562)                                                                                           |
| `GO:('GO', ':0032179')` |              1 | [http://purl.obolibrary.org/obo/OMP_0007738](http://purl.obolibrary.org/obo/OMP_0007738)                                                                                           |
| `GO:('GO', '')`         |              1 | [http://purl.obolibrary.org/obo/OMP_0008035](http://purl.obolibrary.org/obo/OMP_0008035)                                                                                           |
| `GO:('GO', ':0007059')` |              1 | [http://purl.obolibrary.org/obo/OMP_0005047](http://purl.obolibrary.org/obo/OMP_0005047)                                                                                           |
| `GO:('GO', '00015629')` |              1 | [http://purl.obolibrary.org/obo/OMP_0005182](http://purl.obolibrary.org/obo/OMP_0005182)                                                                                           |

## `OMP`: Ontology of Microbial Phenotypes

Overall, there were 1,807 invalid
xrefs to external prefixed with `OMP` (standardized to Bioregistry
prefix [`omp`](https://bioregistry.io/omp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `OMP:('OMP', 'DAS')` |            665 | [http://purl.obolibrary.org/obo/OMP_0000023](http://purl.obolibrary.org/obo/OMP_0000023), [http://purl.obolibrary.org/obo/OMP_0000036](http://purl.obolibrary.org/obo/OMP_0000036), [http://purl.obolibrary.org/obo/OMP_0000042](http://purl.obolibrary.org/obo/OMP_0000042), [http://purl.obolibrary.org/obo/OMP_0000050](http://purl.obolibrary.org/obo/OMP_0000050), [http://purl.obolibrary.org/obo/OMP_0000089](http://purl.obolibrary.org/obo/OMP_0000089), ... |
| `OMP:('OMP', 'JG')`  |            272 | [http://purl.obolibrary.org/obo/OMP_0005000](http://purl.obolibrary.org/obo/OMP_0005000), [http://purl.obolibrary.org/obo/OMP_0005019](http://purl.obolibrary.org/obo/OMP_0005019), [http://purl.obolibrary.org/obo/OMP_0005026](http://purl.obolibrary.org/obo/OMP_0005026), [http://purl.obolibrary.org/obo/OMP_0005028](http://purl.obolibrary.org/obo/OMP_0005028), [http://purl.obolibrary.org/obo/OMP_0005062](http://purl.obolibrary.org/obo/OMP_0005062), ... |
| `OMP:('OMP', 'WAM')` |            247 | [http://purl.obolibrary.org/obo/OMP_0000039](http://purl.obolibrary.org/obo/OMP_0000039), [http://purl.obolibrary.org/obo/OMP_0000043](http://purl.obolibrary.org/obo/OMP_0000043), [http://purl.obolibrary.org/obo/OMP_0000087](http://purl.obolibrary.org/obo/OMP_0000087), [http://purl.obolibrary.org/obo/OMP_0000088](http://purl.obolibrary.org/obo/OMP_0000088), [http://purl.obolibrary.org/obo/OMP_0000090](http://purl.obolibrary.org/obo/OMP_0000090), ... |
| `OMP:('OMP', 'das')` |            231 | [http://purl.obolibrary.org/obo/OMP_0000044](http://purl.obolibrary.org/obo/OMP_0000044), [http://purl.obolibrary.org/obo/OMP_0000193](http://purl.obolibrary.org/obo/OMP_0000193), [http://purl.obolibrary.org/obo/OMP_0000223](http://purl.obolibrary.org/obo/OMP_0000223), [http://purl.obolibrary.org/obo/OMP_0000226](http://purl.obolibrary.org/obo/OMP_0000226), [http://purl.obolibrary.org/obo/OMP_0000250](http://purl.obolibrary.org/obo/OMP_0000250), ... |
| `OMP:('OMP', 'JCH')` |            216 | [http://purl.obolibrary.org/obo/OMP_0000013](http://purl.obolibrary.org/obo/OMP_0000013), [http://purl.obolibrary.org/obo/OMP_0000014](http://purl.obolibrary.org/obo/OMP_0000014), [http://purl.obolibrary.org/obo/OMP_0000026](http://purl.obolibrary.org/obo/OMP_0000026), [http://purl.obolibrary.org/obo/OMP_0000101](http://purl.obolibrary.org/obo/OMP_0000101), [http://purl.obolibrary.org/obo/OMP_0000106](http://purl.obolibrary.org/obo/OMP_0000106), ... |
| `OMP:('OMP', 'MCC')` |             93 | [http://purl.obolibrary.org/obo/OMP_0000000](http://purl.obolibrary.org/obo/OMP_0000000), [http://purl.obolibrary.org/obo/OMP_0000001](http://purl.obolibrary.org/obo/OMP_0000001), [http://purl.obolibrary.org/obo/OMP_0000002](http://purl.obolibrary.org/obo/OMP_0000002), [http://purl.obolibrary.org/obo/OMP_0000003](http://purl.obolibrary.org/obo/OMP_0000003), [http://purl.obolibrary.org/obo/OMP_0000004](http://purl.obolibrary.org/obo/OMP_0000004), ... |
| `OMP:('OMP', 'KDA')` |             35 | [http://purl.obolibrary.org/obo/OMP_0007224](http://purl.obolibrary.org/obo/OMP_0007224), [http://purl.obolibrary.org/obo/OMP_0008000](http://purl.obolibrary.org/obo/OMP_0008000), [http://purl.obolibrary.org/obo/OMP_0008001](http://purl.obolibrary.org/obo/OMP_0008001), [http://purl.obolibrary.org/obo/OMP_0008002](http://purl.obolibrary.org/obo/OMP_0008002), [http://purl.obolibrary.org/obo/OMP_0008003](http://purl.obolibrary.org/obo/OMP_0008003), ... |
| `OMP:('OMP', 'AEZ')` |              9 | [http://purl.obolibrary.org/obo/OMP_0000077](http://purl.obolibrary.org/obo/OMP_0000077), [http://purl.obolibrary.org/obo/OMP_0000117](http://purl.obolibrary.org/obo/OMP_0000117), [http://purl.obolibrary.org/obo/OMP_0000118](http://purl.obolibrary.org/obo/OMP_0000118), [http://purl.obolibrary.org/obo/OMP_0000119](http://purl.obolibrary.org/obo/OMP_0000119), [http://purl.obolibrary.org/obo/OMP_0000120](http://purl.obolibrary.org/obo/OMP_0000120), ... |
| `OMP:('OMP', 'TZ')`  |              9 | [http://purl.obolibrary.org/obo/OMP_0008037](http://purl.obolibrary.org/obo/OMP_0008037), [http://purl.obolibrary.org/obo/OMP_0008039](http://purl.obolibrary.org/obo/OMP_0008039), [http://purl.obolibrary.org/obo/OMP_0008040](http://purl.obolibrary.org/obo/OMP_0008040), [http://purl.obolibrary.org/obo/OMP_0008041](http://purl.obolibrary.org/obo/OMP_0008041), [http://purl.obolibrary.org/obo/OMP_0008043](http://purl.obolibrary.org/obo/OMP_0008043), ... |
| `OMP:('OMP', 'TCK')` |              8 | [http://purl.obolibrary.org/obo/OMP_0006000](http://purl.obolibrary.org/obo/OMP_0006000), [http://purl.obolibrary.org/obo/OMP_0006105](http://purl.obolibrary.org/obo/OMP_0006105), [http://purl.obolibrary.org/obo/OMP_0006106](http://purl.obolibrary.org/obo/OMP_0006106), [http://purl.obolibrary.org/obo/OMP_0006118](http://purl.obolibrary.org/obo/OMP_0006118), [http://purl.obolibrary.org/obo/OMP_0006172](http://purl.obolibrary.org/obo/OMP_0006172), ... |
| `OMP:('OMP', 'AZ')`  |              6 | [http://purl.obolibrary.org/obo/OMP_0000140](http://purl.obolibrary.org/obo/OMP_0000140), [http://purl.obolibrary.org/obo/OMP_0000141](http://purl.obolibrary.org/obo/OMP_0000141), [http://purl.obolibrary.org/obo/OMP_0000142](http://purl.obolibrary.org/obo/OMP_0000142), [http://purl.obolibrary.org/obo/OMP_0000148](http://purl.obolibrary.org/obo/OMP_0000148), [http://purl.obolibrary.org/obo/OMP_0000256](http://purl.obolibrary.org/obo/OMP_0000256), ... |
| `OMP:('OMP', 'tz')`  |              5 | [http://purl.obolibrary.org/obo/OMP_0008035](http://purl.obolibrary.org/obo/OMP_0008035), [http://purl.obolibrary.org/obo/OMP_0008036](http://purl.obolibrary.org/obo/OMP_0008036), [http://purl.obolibrary.org/obo/OMP_0008038](http://purl.obolibrary.org/obo/OMP_0008038), [http://purl.obolibrary.org/obo/OMP_0008052](http://purl.obolibrary.org/obo/OMP_0008052), [http://purl.obolibrary.org/obo/OMP_0008060](http://purl.obolibrary.org/obo/OMP_0008060)      |
| `OMP:('OMP', 'dr')`  |              4 | [http://purl.obolibrary.org/obo/OMP_0005382](http://purl.obolibrary.org/obo/OMP_0005382), [http://purl.obolibrary.org/obo/OMP_0005393](http://purl.obolibrary.org/obo/OMP_0005393), [http://purl.obolibrary.org/obo/OMP_0005395](http://purl.obolibrary.org/obo/OMP_0005395), [http://purl.obolibrary.org/obo/OMP_0005398](http://purl.obolibrary.org/obo/OMP_0005398)                                                                                                |
| `OMP:('OMP', 'JHU')` |              2 | [http://purl.obolibrary.org/obo/OMP_0005035](http://purl.obolibrary.org/obo/OMP_0005035), [http://purl.obolibrary.org/obo/OMP_0005036](http://purl.obolibrary.org/obo/OMP_0005036)                                                                                                                                                                                                                                                                                    |
| `OMP:('OMP', 'JCh')` |              2 | [http://purl.obolibrary.org/obo/OMP_0006141](http://purl.obolibrary.org/obo/OMP_0006141), [http://purl.obolibrary.org/obo/OMP_0006143](http://purl.obolibrary.org/obo/OMP_0006143)                                                                                                                                                                                                                                                                                    |
| `OMP:('OMP', 'DR')`  |              2 | [http://purl.obolibrary.org/obo/OMP_0007540](http://purl.obolibrary.org/obo/OMP_0007540), [http://purl.obolibrary.org/obo/OMP_0007541](http://purl.obolibrary.org/obo/OMP_0007541)                                                                                                                                                                                                                                                                                    |
| `OMP:('OMP', 'REF')` |              1 | [http://purl.obolibrary.org/obo/OMP_0007267](http://purl.obolibrary.org/obo/OMP_0007267)                                                                                                                                                                                                                                                                                                                                                                              |

## `OMp`: Ontology of Microbial Phenotypes

Overall, there were 2 invalid
xrefs to external prefixed with `OMp` (standardized to Bioregistry
prefix [`omp`](https://bioregistry.io/omp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                                                                                                                                                             |
|----------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `OMp:('OMp', 'JCH')` |              2 | [http://purl.obolibrary.org/obo/OMP_0006019](http://purl.obolibrary.org/obo/OMP_0006019), [http://purl.obolibrary.org/obo/OMP_0006042](http://purl.obolibrary.org/obo/OMP_0006042) |

## `SNOMED`: SNOMED CT (International Edition)

Overall, there were 6 invalid
xrefs to external prefixed with `SNOMED` (standardized to Bioregistry
prefix [`snomedct`](https://bioregistry.io/snomedct)) that
did not match the standard pattern `^(\w+)?\d+$`.

| external_xref                    |   usages_count | usages                                                                                   |
|----------------------------------|----------------|------------------------------------------------------------------------------------------|
| `SNOMED:('SNOMED', 'P3-51350')`  |              1 | [http://purl.obolibrary.org/obo/OMP_0000110](http://purl.obolibrary.org/obo/OMP_0000110) |
| `SNOMED:('SNOMED', 'P3-51370')`  |              1 | [http://purl.obolibrary.org/obo/OMP_0000114](http://purl.obolibrary.org/obo/OMP_0000114) |
| `SNOMED:('SNOMED', 'P3-51360')`  |              1 | [http://purl.obolibrary.org/obo/OMP_0000115](http://purl.obolibrary.org/obo/OMP_0000115) |
| `SNOMED:('SNOMED', 'P3-513150')` |              1 | [http://purl.obolibrary.org/obo/OMP_0000139](http://purl.obolibrary.org/obo/OMP_0000139) |
| `SNOMED:('SNOMED', 'P3-51130')`  |              1 | [http://purl.obolibrary.org/obo/OMP_0000160](http://purl.obolibrary.org/obo/OMP_0000160) |
| `SNOMED:('SNOMED', 'P3-51140')`  |              1 | [http://purl.obolibrary.org/obo/OMP_0000161](http://purl.obolibrary.org/obo/OMP_0000161) |

