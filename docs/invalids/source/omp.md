# omp

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `omp`. See the [GitHub repository](https://github.com/microbialphenotypes/OMP-ontology).


## `APO`: Ascomycete phenotype ontology

Overall, there were 1 invalid
xrefs to external prefixed with `APO` (standardized to Bioregistry
prefix [`apo`](https://bioregistry.io/apo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref             |   usages_count | usages                                            |
|---------------------------|----------------|---------------------------------------------------|
| `APO:('APO', ':0000051')` |              1 | [OMP:0007101](https://bioregistry.io/OMP:0007101) |

## `CHEBI`: Chemical Entities of Biological Interest

Overall, there were 2 invalid
xrefs to external prefixed with `CHEBI` (standardized to Bioregistry
prefix [`chebi`](https://bioregistry.io/chebi)) that
did not match the standard pattern `^\d+$`.

| external_xref                    |   usages_count | usages                                            |
|----------------------------------|----------------|---------------------------------------------------|
| `CHEBI:('CHEBI', 'CHEBI:87649')` |              1 | [OMP:0007481](https://bioregistry.io/OMP:0007481) |
| `CHEBI:('CHEBI', ':4806')`       |              1 | [OMP:0007848](https://bioregistry.io/OMP:0007848) |

## `FYPO`: Fission Yeast Phenotype Ontology

Overall, there were 3 invalid
xrefs to external prefixed with `FYPO` (standardized to Bioregistry
prefix [`fypo`](https://bioregistry.io/fypo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                   |   usages_count | usages                                            |
|---------------------------------|----------------|---------------------------------------------------|
| `FYPO:('FYPO', 'FYPO:0003755')` |              1 | [OMP:0007746](https://bioregistry.io/OMP:0007746) |
| `FYPO:('FYPO', '1178')`         |              1 | [OMP:0007808](https://bioregistry.io/OMP:0007808) |
| `FYPO:('FYPO', '000064')`       |              1 | [OMP:0007701](https://bioregistry.io/OMP:0007701) |

## `GO`: Gene Ontology

Overall, there were 8 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref           |   usages_count | usages                                                                                               |
|-------------------------|----------------|------------------------------------------------------------------------------------------------------|
| `GO:('GO', 'JG')`       |              2 | [OMP:0005181](https://bioregistry.io/OMP:0005181), [OMP:0005200](https://bioregistry.io/OMP:0005200) |
| `GO:('GO', ':0019835')` |              1 | [OMP:0005336](https://bioregistry.io/OMP:0005336)                                                    |
| `GO:('GO', '00140013')` |              1 | [OMP:0007562](https://bioregistry.io/OMP:0007562)                                                    |
| `GO:('GO', ':0032179')` |              1 | [OMP:0007738](https://bioregistry.io/OMP:0007738)                                                    |
| `GO:('GO', '')`         |              1 | [OMP:0008035](https://bioregistry.io/OMP:0008035)                                                    |
| `GO:('GO', ':0007059')` |              1 | [OMP:0005047](https://bioregistry.io/OMP:0005047)                                                    |
| `GO:('GO', '00015629')` |              1 | [OMP:0005182](https://bioregistry.io/OMP:0005182)                                                    |

## `OMP`: Ontology of Microbial Phenotypes

Overall, there were 1,807 invalid
xrefs to external prefixed with `OMP` (standardized to Bioregistry
prefix [`omp`](https://bioregistry.io/omp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                                                                                                                                                                                                                                             |
|----------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `OMP:('OMP', 'DAS')` |            665 | [OMP:0000023](https://bioregistry.io/OMP:0000023), [OMP:0000036](https://bioregistry.io/OMP:0000036), [OMP:0000042](https://bioregistry.io/OMP:0000042), [OMP:0000050](https://bioregistry.io/OMP:0000050), [OMP:0000089](https://bioregistry.io/OMP:0000089), ... |
| `OMP:('OMP', 'JG')`  |            272 | [OMP:0005000](https://bioregistry.io/OMP:0005000), [OMP:0005019](https://bioregistry.io/OMP:0005019), [OMP:0005026](https://bioregistry.io/OMP:0005026), [OMP:0005028](https://bioregistry.io/OMP:0005028), [OMP:0005062](https://bioregistry.io/OMP:0005062), ... |
| `OMP:('OMP', 'WAM')` |            247 | [OMP:0000039](https://bioregistry.io/OMP:0000039), [OMP:0000043](https://bioregistry.io/OMP:0000043), [OMP:0000087](https://bioregistry.io/OMP:0000087), [OMP:0000088](https://bioregistry.io/OMP:0000088), [OMP:0000090](https://bioregistry.io/OMP:0000090), ... |
| `OMP:('OMP', 'das')` |            231 | [OMP:0000044](https://bioregistry.io/OMP:0000044), [OMP:0000193](https://bioregistry.io/OMP:0000193), [OMP:0000223](https://bioregistry.io/OMP:0000223), [OMP:0000226](https://bioregistry.io/OMP:0000226), [OMP:0000250](https://bioregistry.io/OMP:0000250), ... |
| `OMP:('OMP', 'JCH')` |            216 | [OMP:0000013](https://bioregistry.io/OMP:0000013), [OMP:0000014](https://bioregistry.io/OMP:0000014), [OMP:0000026](https://bioregistry.io/OMP:0000026), [OMP:0000101](https://bioregistry.io/OMP:0000101), [OMP:0000106](https://bioregistry.io/OMP:0000106), ... |
| `OMP:('OMP', 'MCC')` |             93 | [OMP:0000000](https://bioregistry.io/OMP:0000000), [OMP:0000001](https://bioregistry.io/OMP:0000001), [OMP:0000002](https://bioregistry.io/OMP:0000002), [OMP:0000003](https://bioregistry.io/OMP:0000003), [OMP:0000004](https://bioregistry.io/OMP:0000004), ... |
| `OMP:('OMP', 'KDA')` |             35 | [OMP:0007224](https://bioregistry.io/OMP:0007224), [OMP:0008000](https://bioregistry.io/OMP:0008000), [OMP:0008001](https://bioregistry.io/OMP:0008001), [OMP:0008002](https://bioregistry.io/OMP:0008002), [OMP:0008003](https://bioregistry.io/OMP:0008003), ... |
| `OMP:('OMP', 'AEZ')` |              9 | [OMP:0000077](https://bioregistry.io/OMP:0000077), [OMP:0000117](https://bioregistry.io/OMP:0000117), [OMP:0000118](https://bioregistry.io/OMP:0000118), [OMP:0000119](https://bioregistry.io/OMP:0000119), [OMP:0000120](https://bioregistry.io/OMP:0000120), ... |
| `OMP:('OMP', 'TZ')`  |              9 | [OMP:0008037](https://bioregistry.io/OMP:0008037), [OMP:0008039](https://bioregistry.io/OMP:0008039), [OMP:0008040](https://bioregistry.io/OMP:0008040), [OMP:0008041](https://bioregistry.io/OMP:0008041), [OMP:0008043](https://bioregistry.io/OMP:0008043), ... |
| `OMP:('OMP', 'TCK')` |              8 | [OMP:0006000](https://bioregistry.io/OMP:0006000), [OMP:0006105](https://bioregistry.io/OMP:0006105), [OMP:0006106](https://bioregistry.io/OMP:0006106), [OMP:0006118](https://bioregistry.io/OMP:0006118), [OMP:0006172](https://bioregistry.io/OMP:0006172), ... |
| `OMP:('OMP', 'AZ')`  |              6 | [OMP:0000140](https://bioregistry.io/OMP:0000140), [OMP:0000141](https://bioregistry.io/OMP:0000141), [OMP:0000142](https://bioregistry.io/OMP:0000142), [OMP:0000148](https://bioregistry.io/OMP:0000148), [OMP:0000256](https://bioregistry.io/OMP:0000256), ... |
| `OMP:('OMP', 'tz')`  |              5 | [OMP:0008035](https://bioregistry.io/OMP:0008035), [OMP:0008036](https://bioregistry.io/OMP:0008036), [OMP:0008038](https://bioregistry.io/OMP:0008038), [OMP:0008052](https://bioregistry.io/OMP:0008052), [OMP:0008060](https://bioregistry.io/OMP:0008060)      |
| `OMP:('OMP', 'dr')`  |              4 | [OMP:0005382](https://bioregistry.io/OMP:0005382), [OMP:0005393](https://bioregistry.io/OMP:0005393), [OMP:0005395](https://bioregistry.io/OMP:0005395), [OMP:0005398](https://bioregistry.io/OMP:0005398)                                                         |
| `OMP:('OMP', 'JHU')` |              2 | [OMP:0005035](https://bioregistry.io/OMP:0005035), [OMP:0005036](https://bioregistry.io/OMP:0005036)                                                                                                                                                               |
| `OMP:('OMP', 'JCh')` |              2 | [OMP:0006141](https://bioregistry.io/OMP:0006141), [OMP:0006143](https://bioregistry.io/OMP:0006143)                                                                                                                                                               |
| `OMP:('OMP', 'DR')`  |              2 | [OMP:0007540](https://bioregistry.io/OMP:0007540), [OMP:0007541](https://bioregistry.io/OMP:0007541)                                                                                                                                                               |
| `OMP:('OMP', 'REF')` |              1 | [OMP:0007267](https://bioregistry.io/OMP:0007267)                                                                                                                                                                                                                  |

## `OMp`: Ontology of Microbial Phenotypes

Overall, there were 2 invalid
xrefs to external prefixed with `OMp` (standardized to Bioregistry
prefix [`omp`](https://bioregistry.io/omp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                                                                               |
|----------------------|----------------|------------------------------------------------------------------------------------------------------|
| `OMp:('OMp', 'JCH')` |              2 | [OMP:0006019](https://bioregistry.io/OMP:0006019), [OMP:0006042](https://bioregistry.io/OMP:0006042) |

## `SNOMED`: SNOMED CT (International Edition)

Overall, there were 6 invalid
xrefs to external prefixed with `SNOMED` (standardized to Bioregistry
prefix [`snomedct`](https://bioregistry.io/snomedct)) that
did not match the standard pattern `^(\w+)?\d+$`.

| external_xref                    |   usages_count | usages                                            |
|----------------------------------|----------------|---------------------------------------------------|
| `SNOMED:('SNOMED', 'P3-51350')`  |              1 | [OMP:0000110](https://bioregistry.io/OMP:0000110) |
| `SNOMED:('SNOMED', 'P3-51370')`  |              1 | [OMP:0000114](https://bioregistry.io/OMP:0000114) |
| `SNOMED:('SNOMED', 'P3-51360')`  |              1 | [OMP:0000115](https://bioregistry.io/OMP:0000115) |
| `SNOMED:('SNOMED', 'P3-513150')` |              1 | [OMP:0000139](https://bioregistry.io/OMP:0000139) |
| `SNOMED:('SNOMED', 'P3-51130')`  |              1 | [OMP:0000160](https://bioregistry.io/OMP:0000160) |
| `SNOMED:('SNOMED', 'P3-51140')`  |              1 | [OMP:0000161](https://bioregistry.io/OMP:0000161) |

