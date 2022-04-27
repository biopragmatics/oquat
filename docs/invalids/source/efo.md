# efo

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `efo`. See the [GitHub repository](https://github.com/EBISPOT/efo/).


## `ATCC number`: American Type Culture Collection

Overall, there were 1 invalid
xrefs to external prefixed with `ATCC number` (standardized to Bioregistry
prefix [`atcc`](https://bioregistry.io/atcc)) that
did not match the standard pattern `^([A-Z]+-)?\d+$`.

| external_xref                              |   usages_count | usages                                                                                              |
|--------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `ATCC number:('ATCC number', ' CRL-2265')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0001667](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001667) |

## `doi`: Digital Object Identifier

Overall, there were 1 invalid
xrefs to external prefixed with `doi` (standardized to Bioregistry
prefix [`doi`](https://bioregistry.io/doi)) that
did not match the standard pattern `^(doi\:)?\d{2}\.\d{4}.*$`.

| external_xref                       |   usages_count | usages                                                                                              |
|-------------------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `doi:('doi', ' 10.1111/nmo.12871')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0011032](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0011032) |

## `FBdv`: Drosophila development

Overall, there were 1 invalid
xrefs to external prefixed with `FBdv` (standardized to Bioregistry
prefix [`fbdv`](https://bioregistry.io/fbdv)) that
did not match the standard pattern `^\d{8}$`.

| external_xref              |   usages_count | usages                                                                                              |
|----------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `FBdv:('FBdv', '0005333')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0001323](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001323) |

## `ICD10`: International Classification of Diseases, 10th Revision

Overall, there were 297 invalid
xrefs to external prefixed with `ICD10` (standardized to Bioregistry
prefix [`icd10`](https://bioregistry.io/icd10)) that
did not match the standard pattern `^[A-Z]\d+(\.[-\d+])?$`.

| external_xref                |   usages_count | usages                                                                                                                                                                                                   |
|------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ICD10:('ICD10', 'M19.90')`  |              2 | [http://www.ebi.ac.uk/efo/EFO:0005856](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005856), [http://www.ebi.ac.uk/efo/EFO:1000999](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000999) |
| `ICD10:('ICD10', 'E85.4+')`  |              2 | [http://www.ebi.ac.uk/efo/EFO:0006790](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0006790), [http://www.ebi.ac.uk/efo/EFO:1001882](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001882) |
| `ICD10:('ICD10', 'A69.22')`  |              2 | [http://www.ebi.ac.uk/efo/EFO:0007364](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007364), [http://www.ebi.ac.uk/efo/EFO:0009562](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009562) |
| `ICD10:('ICD10', 'K52.89')`  |              2 | [http://www.ebi.ac.uk/efo/EFO:1001293](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001293), [http://www.ebi.ac.uk/efo/EFO:1001294](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001294) |
| `ICD10:('ICD10', 'C91.10')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000095](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000095)                                                                                                      |
| `ICD10:('ICD10', 'E88.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000195](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000195)                                                                                                      |
| `ICD10:('ICD10', 'C91.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000220](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000220)                                                                                                      |
| `ICD10:('ICD10', 'C91.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000220](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000220)                                                                                                      |
| `ICD10:('ICD10', 'C92.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000222](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000222)                                                                                                      |
| `ICD10:('ICD10', 'C92.40')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000224](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000224)                                                                                                      |
| `ICD10:('ICD10', 'L20.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000274](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000274)                                                                                                      |
| `ICD10:('ICD10', 'N46.01')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000279](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000279)                                                                                                      |
| `ICD10:('ICD10', 'K22.70')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000280](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000280)                                                                                                      |
| `ICD10:('ICD10', 'C83.70')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000309](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000309)                                                                                                      |
| `ICD10:('ICD10', 'I00.I99')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000319](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000319)                                                                                                      |
| `ICD10:('ICD10', 'M33.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000398](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000398)                                                                                                      |
| `ICD10:('ICD10', 'E08-E13')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000400](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000400)                                                                                                      |
| `ICD10:('ICD10', 'E10.E14')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000400](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000400)                                                                                                      |
| `ICD10:('ICD10', 'G40.909')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000474](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000474)                                                                                                      |
| `ICD10:('ICD10', 'H40-H42')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000516](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000516)                                                                                                      |
| `ICD10:('ICD10', 'H40.H42')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000516](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000516)                                                                                                      |
| `ICD10:('ICD10', 'I10-I15')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000537](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000537)                                                                                                      |
| `ICD10:('ICD10', 'S00.T98')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000546](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000546)                                                                                                      |
| `ICD10:('ICD10', 'C95.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000565](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000565)                                                                                                      |
| `ICD10:('ICD10', 'E70.E90')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000589](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000589)                                                                                                      |
| `ICD10:('ICD10', 'C00.D48')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000616](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000616)                                                                                                      |
| `ICD10:('ICD10', 'G00-G99')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000618](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000618)                                                                                                      |
| `ICD10:('ICD10', 'G00.G99')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000618](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000618)                                                                                                      |
| `ICD10:('ICD10', 'O14.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000668](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000668)                                                                                                      |
| `ICD10:('ICD10', 'F00.F99')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000677](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000677)                                                                                                      |
| `ICD10:('ICD10', 'H11.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000678](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000678)                                                                                                      |
| `ICD10:('ICD10', 'H11.009')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000678](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000678)                                                                                                      |
| `ICD10:('ICD10', 'J96-J99')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000684](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000684)                                                                                                      |
| `ICD10:('ICD10', 'J12.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000694](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000694)                                                                                                      |
| `ICD10:('ICD10', 'M35.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000699](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000699)                                                                                                      |
| `ICD10:('ICD10', 'B20-B20')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000764](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000764)                                                                                                      |
| `ICD10:('ICD10', 'B20.B24')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000764](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000764)                                                                                                      |
| `ICD10:('ICD10', 'J84.112')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000768](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000768)                                                                                                      |
| `ICD10:('ICD10', 'K90.8+')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000775](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000775)                                                                                                      |
| `ICD10:('ICD10', 'K90.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000775](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000775)                                                                                                      |
| `ICD10:('ICD10', 'M14.8*')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000775](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000775)                                                                                                      |
| `ICD10:('ICD10', 'G72.49')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0000783](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000783)                                                                                                      |
| `ICD10:('ICD10', 'H44.12')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0001067](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001067)                                                                                                      |
| `ICD10:('ICD10', 'C34.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0001071](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001071)                                                                                                      |
| `ICD10:('ICD10', 'F43.10')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0001358](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001358)                                                                                                      |
| `ICD10:('ICD10', 'H35.30')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0001365](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001365)                                                                                                      |
| `ICD10:('ICD10', 'C90.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0001378](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001378)                                                                                                      |
| `ICD10:('ICD10', 'K70-K77')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0001421](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001421)                                                                                                      |
| `ICD10:('ICD10', 'K74.60')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0001422](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001422)                                                                                                      |
| `ICD10:('ICD10', 'I20-I25')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0001645](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001645)                                                                                                      |
| `ICD10:('ICD10', 'I25.10')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0001645](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001645)                                                                                                      |
| `ICD10:('ICD10', 'D10.D36')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0002422](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002422)                                                                                                      |
| `ICD10:('ICD10', 'D75.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0002430](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002430)                                                                                                      |
| `ICD10:('ICD10', 'M08.40')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0002609](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002609)                                                                                                      |
| `ICD10:('ICD10', 'C94.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0003025](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003025)                                                                                                      |
| `ICD10:('ICD10', 'L03.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0003035](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003035)                                                                                                      |
| `ICD10:('ICD10', 'B19.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0003047](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003047)                                                                                                      |
| `ICD10:('ICD10', 'G31.01')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0003096](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003096)                                                                                                      |
| `ICD10:('ICD10', 'I60-I69')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003763](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003763)                                                                                                      |
| `ICD10:('ICD10', 'I60.I69')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003763](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003763)                                                                                                      |
| `ICD10:('ICD10', 'F17.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0003768](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003768)                                                                                                      |
| `ICD10:('ICD10', 'L40.50')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0003778](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003778)                                                                                                      |
| `ICD10:('ICD10', 'G12.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0003782](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003782)                                                                                                      |
| `ICD10:('ICD10', 'G12.22')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0003783](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003783)                                                                                                      |
| `ICD10:('ICD10', 'I26.99')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0003827](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003827)                                                                                                      |
| `ICD10:('ICD10', 'G47.30')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0003918](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003918)                                                                                                      |
| `ICD10:('ICD10', 'G47.33')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0003918](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003918)                                                                                                      |
| `ICD10:('ICD10', 'K91.850')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003921](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003921)                                                                                                      |
| `ICD10:('ICD10', 'E85.1+')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004129](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004129)                                                                                                      |
| `ICD10:('ICD10', 'G63.3*')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004129](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004129)                                                                                                      |
| `ICD10:('ICD10', 'G56.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004143](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004143)                                                                                                      |
| `ICD10:('ICD10', 'M60-M63')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004145](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004145)                                                                                                      |
| `ICD10:('ICD10', 'H40.10')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004190](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004190)                                                                                                      |
| `ICD10:('ICD10', 'H40.13')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004190](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004190)                                                                                                      |
| `ICD10:('ICD10', 'B15.B19')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004196](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004196)                                                                                                      |
| `ICD10:('ICD10', 'H80.80')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004213](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004213)                                                                                                      |
| `ICD10:('ICD10', 'F50.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004215](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004215)                                                                                                      |
| `ICD10:('ICD10', 'A81.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004226](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004226)                                                                                                      |
| `ICD10:('ICD10', 'F30-F39')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004247](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004247)                                                                                                      |
| `ICD10:('ICD10', 'F30.F39')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004247](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004247)                                                                                                      |
| `ICD10:('ICD10', 'G25.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004270](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004270)                                                                                                      |
| `ICD10:('ICD10', 'R53.82')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004540](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004540)                                                                                                      |
| `ICD10:('ICD10', 'H35.32')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004683](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004683)                                                                                                      |
| `ICD10:('ICD10', 'G70.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004991](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004991)                                                                                                      |
| `ICD10:('ICD10', 'H66.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004992](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004992)                                                                                                      |
| `ICD10:('ICD10', 'C62.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0005088](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005088)                                                                                                      |
| `ICD10:('ICD10', 'J09.X')`   |              1 | [http://www.ebi.ac.uk/efo/EFO:0005222](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005222)                                                                                                      |
| `ICD10:('ICD10', 'M31.30')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0005297](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005297)                                                                                                      |
| `ICD10:('ICD10', 'N13.30')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0005562](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005562)                                                                                                      |
| `ICD10:('ICD10', 'H53.54')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0005580](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005580)                                                                                                      |
| `ICD10:('ICD10', 'H53.53')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0005581](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005581)                                                                                                      |
| `ICD10:('ICD10', 'K62.89')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0005628](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005628)                                                                                                      |
| `ICD10:('ICD10', 'M43.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0005649](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005649)                                                                                                      |
| `ICD10:('ICD10', 'A00.B99')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005741](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005741)                                                                                                      |
| `ICD10:('ICD10', 'H52.52')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0005758](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005758)                                                                                                      |
| `ICD10:('ICD10', 'E83.50')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0005769](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005769)                                                                                                      |
| `ICD10:('ICD10', 'G93.40')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0005774](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005774)                                                                                                      |
| `ICD10:('ICD10', 'G47.419')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005855](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005855)                                                                                                      |
| `ICD10:('ICD10', 'C90.10')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0006475](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0006475)                                                                                                      |
| `ICD10:('ICD10', 'C90.30')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0006738](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0006738)                                                                                                      |
| `ICD10:('ICD10', 'A01.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0006789](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0006789)                                                                                                      |
| `ICD10:('ICD10', 'I68.0*')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0006790](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0006790)                                                                                                      |
| `ICD10:('ICD10', 'G31.83')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0006792](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0006792)                                                                                                      |
| `ICD10:('ICD10', 'H81.09')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0006862](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0006862)                                                                                                      |
| `ICD10:('ICD10', 'B60.1+')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007126](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007126)                                                                                                      |
| `ICD10:('ICD10', 'H19.2*')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007126](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007126)                                                                                                      |
| `ICD10:('ICD10', 'B44.1+')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007140](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007140)                                                                                                      |
| `ICD10:('ICD10', 'B44.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007140](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007140)                                                                                                      |
| `ICD10:('ICD10', 'J99.8*')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007140](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007140)                                                                                                      |
| `ICD10:('ICD10', 'H55.01')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007217](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007217)                                                                                                      |
| `ICD10:('ICD10', 'B08.02')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007222](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007222)                                                                                                      |
| `ICD10:('ICD10', 'B08.010')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0007225](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007225)                                                                                                      |
| `ICD10:('ICD10', 'B67.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007245](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007245)                                                                                                      |
| `ICD10:('ICD10', 'J05.10')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007261](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007261)                                                                                                      |
| `ICD10:('ICD10', 'M05.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007269](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007269)                                                                                                      |
| `ICD10:('ICD10', 'B02.21')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007281](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007281)                                                                                                      |
| `ICD10:('ICD10', 'M31.0+')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007290](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007290)                                                                                                      |
| `ICD10:('ICD10', 'N08.5*')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007290](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007290)                                                                                                      |
| `ICD10:('ICD10', 'B33.4+')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007296](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007296)                                                                                                      |
| `ICD10:('ICD10', 'J17.1*')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007296](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007296)                                                                                                      |
| `ICD10:('ICD10', 'B00.5+')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007308](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007308)                                                                                                      |
| `ICD10:('ICD10', 'H19.1*')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007308](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007308)                                                                                                      |
| `ICD10:('ICD10', 'H00.01')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007315](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007315)                                                                                                      |
| `ICD10:('ICD10', 'G72.41')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007323](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007323)                                                                                                      |
| `ICD10:('ICD10', 'A50.40')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007339](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007339)                                                                                                      |
| `ICD10:('ICD10', 'A50.59')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007339](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007339)                                                                                                      |
| `ICD10:('ICD10', 'C60-C63')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0007355](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007355)                                                                                                      |
| `ICD10:('ICD10', 'C94.30')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007359](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007359)                                                                                                      |
| `ICD10:('ICD10', 'B08.04')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007370](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007370)                                                                                                      |
| `ICD10:('ICD10', 'D61.82')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007388](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007388)                                                                                                      |
| `ICD10:('ICD10', 'O41.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007401](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007401)                                                                                                      |
| `ICD10:('ICD10', 'A18.84')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007426](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007426)                                                                                                      |
| `ICD10:('ICD10', 'G47.61')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007428](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007428)                                                                                                      |
| `ICD10:('ICD10', 'O43.21')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007440](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007440)                                                                                                      |
| `ICD10:('ICD10', 'O43.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007441](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007441)                                                                                                      |
| `ICD10:('ICD10', 'B59+')`    |              1 | [http://www.ebi.ac.uk/efo/EFO:0007448](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007448)                                                                                                      |
| `ICD10:('ICD10', 'J17.3*')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007448](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007448)                                                                                                      |
| `ICD10:('ICD10', 'M02.10')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007460](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007460)                                                                                                      |
| `ICD10:('ICD10', 'M02.30')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007460](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007460)                                                                                                      |
| `ICD10:('ICD10', 'G47.52')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007462](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007462)                                                                                                      |
| `ICD10:('ICD10', 'J01.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007486](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007486)                                                                                                      |
| `ICD10:('ICD10', 'M48.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007490](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007490)                                                                                                      |
| `ICD10:('ICD10', 'M48.02')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007490](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007490)                                                                                                      |
| `ICD10:('ICD10', 'M48.06')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007490](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007490)                                                                                                      |
| `ICD10:('ICD10', 'A18.85')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007492](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007492)                                                                                                      |
| `ICD10:('ICD10', 'M43.10')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007493](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007493)                                                                                                      |
| `ICD10:('ICD10', 'G25.82')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007498](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007498)                                                                                                      |
| `ICD10:('ICD10', 'H66.40')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007503](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007503)                                                                                                      |
| `ICD10:('ICD10', 'A52.11')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007505](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007505)                                                                                                      |
| `ICD10:('ICD10', 'A59.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007521](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007521)                                                                                                      |
| `ICD10:('ICD10', 'A18.31')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007529](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007529)                                                                                                      |
| `ICD10:('ICD10', 'A18.10')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007531](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007531)                                                                                                      |
| `ICD10:('ICD10', 'N13.70')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007536](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007536)                                                                                                      |
| `ICD10:('ICD10', 'H81.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007537](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007537)                                                                                                      |
| `ICD10:('ICD10', 'A39.1+')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007544](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007544)                                                                                                      |
| `ICD10:('ICD10', 'E35.1*')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007544](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007544)                                                                                                      |
| `ICD10:('ICD10', 'A92.31')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007545](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007545)                                                                                                      |
| `ICD10:('ICD10', 'A69.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0008510](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008510)                                                                                                      |
| `ICD10:('ICD10', 'Q85.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0008514](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008514)                                                                                                      |
| `ICD10:('ICD10', 'Q85.01')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0008514](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008514)                                                                                                      |
| `ICD10:('ICD10', 'Q85.02')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0008514](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008514)                                                                                                      |
| `ICD10:('ICD10', 'R10.13')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0008533](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008533)                                                                                                      |
| `ICD10:('ICD10', 'L10.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0008602](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008602)                                                                                                      |
| `ICD10:('ICD10', 'E28.31')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009005](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009005)                                                                                                      |
| `ICD10:('ICD10', 'E28.319')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009005](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009005)                                                                                                      |
| `ICD10:('ICD10', 'D68.59')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009315](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009315)                                                                                                      |
| `ICD10:('ICD10', '351.8')`   |              1 | [http://www.ebi.ac.uk/efo/EFO:0009380](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009380)                                                                                                      |
| `ICD10:('ICD10', 'N60-N65')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009483](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009483)                                                                                                      |
| `ICD10:('ICD10', 'H53.30')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009535](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009535)                                                                                                      |
| `ICD10:('ICD10', 'H01.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009536](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009536)                                                                                                      |
| `ICD10:('ICD10', 'I85.01')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009545](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009545)                                                                                                      |
| `ICD10:('ICD10', 'H00.H06')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009546](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009546)                                                                                                      |
| `ICD10:('ICD10', 'N40.N51')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009555](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009555)                                                                                                      |
| `ICD10:('ICD10', 'H73.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009570](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009570)                                                                                                      |
| `ICD10:('ICD10', 'H83.09')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009604](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009604)                                                                                                      |
| `ICD10:('ICD10', 'N00.N99')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009663](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009663)                                                                                                      |
| `ICD10:('ICD10', 'H00.H59')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009664](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009664)                                                                                                      |
| `ICD10:('ICD10', 'H35.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009664](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009664)                                                                                                      |
| `ICD10:('ICD10', 'H60-H62')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009668](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009668)                                                                                                      |
| `ICD10:('ICD10', 'H60.H62')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009668](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009668)                                                                                                      |
| `ICD10:('ICD10', 'H80-H83')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009672](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009672)                                                                                                      |
| `ICD10:('ICD10', 'H80.H83')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009672](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009672)                                                                                                      |
| `ICD10:('ICD10', 'H83.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009672](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009672)                                                                                                      |
| `ICD10:('ICD10', 'H25-H28')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009674](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009674)                                                                                                      |
| `ICD10:('ICD10', 'G82.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009679](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009679)                                                                                                      |
| `ICD10:('ICD10', 'G82.50')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009684](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009684)                                                                                                      |
| `ICD10:('ICD10', 'H81.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009691](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009691)                                                                                                      |
| `ICD10:('ICD10', 'L40.5+')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009733](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009733)                                                                                                      |
| `ICD10:('ICD10', 'M09.0*')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009733](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009733)                                                                                                      |
| `ICD10:('ICD10', 'C95.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000068](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000068)                                                                                                      |
| `ICD10:('ICD10', 'C93.30')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000309](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000309)                                                                                                      |
| `ICD10:('ICD10', 'C64.C68')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000363](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000363)                                                                                                      |
| `ICD10:('ICD10', 'E00-E07')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000627](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000627)                                                                                                      |
| `ICD10:('ICD10', 'E00.E07')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000627](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000627)                                                                                                      |
| `ICD10:('ICD10', 'D18.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000635](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000635)                                                                                                      |
| `ICD10:('ICD10', 'M62.84')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000653](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000653)                                                                                                      |
| `ICD10:('ICD10', 'H71.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000675](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000675)                                                                                                      |
| `ICD10:('ICD10', 'H71.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000676](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000676)                                                                                                      |
| `ICD10:('ICD10', 'H60.40')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000677](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000677)                                                                                                      |
| `ICD10:('ICD10', 'H11.13')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000682](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000682)                                                                                                      |
| `ICD10:('ICD10', 'L12.30')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000691](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000691)                                                                                                      |
| `ICD10:('ICD10', 'O26.40')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000709](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000709)                                                                                                      |
| `ICD10:('ICD10', 'H02.71')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000711](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000711)                                                                                                      |
| `ICD10:('ICD10', 'H02.73')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000713](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000713)                                                                                                      |
| `ICD10:('ICD10', 'H18.06')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000770](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000770)                                                                                                      |
| `ICD10:('ICD10', 'C84.10')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000785](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000785)                                                                                                      |
| `ICD10:('ICD10', 'M76.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000808](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000808)                                                                                                      |
| `ICD10:('ICD10', 'H47.01')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000809](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000809)                                                                                                      |
| `ICD10:('ICD10', 'H18.41')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000818](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000818)                                                                                                      |
| `ICD10:('ICD10', 'T78.41')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000821](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000821)                                                                                                      |
| `ICD10:('ICD10', 'E51.11')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000837](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000837)                                                                                                      |
| `ICD10:('ICD10', 'G61.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000868](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000868)                                                                                                      |
| `ICD10:('ICD10', 'H18.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000879](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000879)                                                                                                      |
| `ICD10:('ICD10', 'H16.40')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000880](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000880)                                                                                                      |
| `ICD10:('ICD10', 'I25.41')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000881](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000881)                                                                                                      |
| `ICD10:('ICD10', 'C72.50')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000884](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000884)                                                                                                      |
| `ICD10:('ICD10', 'A50.06')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000887](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000887)                                                                                                      |
| `ICD10:('ICD10', 'I50.30')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000899](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000899)                                                                                                      |
| `ICD10:('ICD10', 'G25.71')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000903](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000903)                                                                                                      |
| `ICD10:('ICD10', 'H04.12')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000906](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000906)                                                                                                      |
| `ICD10:('ICD10', 'E07.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000931](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000931)                                                                                                      |
| `ICD10:('ICD10', 'G57.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000936](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000936)                                                                                                      |
| `ICD10:('ICD10', 'K31.84')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000948](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000948)                                                                                                      |
| `ICD10:('ICD10', 'C91.40')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000956](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000956)                                                                                                      |
| `ICD10:('ICD10', 'H35.03')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1000977](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000977)                                                                                                      |
| `ICD10:('ICD10', 'M00-M02')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000999](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000999)                                                                                                      |
| `ICD10:('ICD10', 'M15.M19')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000999](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000999)                                                                                                      |
| `ICD10:('ICD10', 'A81.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001008](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001008)                                                                                                      |
| `ICD10:('ICD10', 'D72.823')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001014](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001014)                                                                                                      |
| `ICD10:('ICD10', 'H40.12')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001022](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001022)                                                                                                      |
| `ICD10:('ICD10', 'P24.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001037](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001037)                                                                                                      |
| `ICD10:('ICD10', 'P24.01')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001037](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001037)                                                                                                      |
| `ICD10:('ICD10', 'A39.0+')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001040](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001040)                                                                                                      |
| `ICD10:('ICD10', 'G01*')`    |              1 | [http://www.ebi.ac.uk/efo/EFO:1001040](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001040)                                                                                                      |
| `ICD10:('ICD10', 'C84.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001051](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001051)                                                                                                      |
| `ICD10:('ICD10', 'C92.30')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001052](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001052)                                                                                                      |
| `ICD10:('ICD10', 'E40.E46')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001067](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001067)                                                                                                      |
| `ICD10:('ICD10', 'H40.05')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001069](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001069)                                                                                                      |
| `ICD10:('ICD10', 'N70.92')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001071](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001071)                                                                                                      |
| `ICD10:('ICD10', 'H35.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001074](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001074)                                                                                                      |
| `ICD10:('ICD10', 'H47.10')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001074](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001074)                                                                                                      |
| `ICD10:('ICD10', 'H47.11')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001074](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001074)                                                                                                      |
| `ICD10:('ICD10', 'H05.01')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001076](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001076)                                                                                                      |
| `ICD10:('ICD10', 'H44.11')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001082](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001082)                                                                                                      |
| `ICD10:('ICD10', 'M12.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001106](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001106)                                                                                                      |
| `ICD10:('ICD10', 'R73.09')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001121](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001121)                                                                                                      |
| `ICD10:('ICD10', 'N10-N16')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001141](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001141)                                                                                                      |
| `ICD10:('ICD10', 'G56.30')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001143](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001143)                                                                                                      |
| `ICD10:('ICD10', 'H35.06')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001156](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001156)                                                                                                      |
| `ICD10:('ICD10', 'H35.10')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001158](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001158)                                                                                                      |
| `ICD10:('ICD10', 'H35.17')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001158](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001158)                                                                                                      |
| `ICD10:('ICD10', 'I00-I02')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001160](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001160)                                                                                                      |
| `ICD10:('ICD10', 'I05.I09')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001161](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001161)                                                                                                      |
| `ICD10:('ICD10', 'K11.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001179](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001179)                                                                                                      |
| `ICD10:('ICD10', 'N43.40')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001189](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001189)                                                                                                      |
| `ICD10:('ICD10', 'H44.13')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001205](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001205)                                                                                                      |
| `ICD10:('ICD10', 'A52.02')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001206](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001206)                                                                                                      |
| `ICD10:('ICD10', 'I50.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001207](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001207)                                                                                                      |
| `ICD10:('ICD10', 'G57.50')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001208](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001208)                                                                                                      |
| `ICD10:('ICD10', 'O43.02')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001221](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001221)                                                                                                      |
| `ICD10:('ICD10', 'O43.029')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001221](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001221)                                                                                                      |
| `ICD10:('ICD10', 'D86.89')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001232](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001232)                                                                                                      |
| `ICD10:('ICD10', 'A81.01')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001233](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001233)                                                                                                      |
| `ICD10:('ICD10', 'H43.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001238](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001238)                                                                                                      |
| `ICD10:('ICD10', 'K75.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001249](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001249)                                                                                                      |
| `ICD10:('ICD10', 'H52.32')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001266](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001266)                                                                                                      |
| `ICD10:('ICD10', 'G83.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001279](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001279)                                                                                                      |
| `ICD10:('ICD10', 'K52.831')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001293](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001293)                                                                                                      |
| `ICD10:('ICD10', 'K52.832')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001294](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001294)                                                                                                      |
| `ICD10:('ICD10', 'J84.116')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001300](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001300)                                                                                                      |
| `ICD10:('ICD10', 'B08.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001320](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001320)                                                                                                      |
| `ICD10:('ICD10', 'H47.14')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001330](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001330)                                                                                                      |
| `ICD10:('ICD10', 'C51.C58')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001331](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001331)                                                                                                      |
| `ICD10:('ICD10', 'B65-B83')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001342](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001342)                                                                                                      |
| `ICD10:('ICD10', 'B65.B83')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001342](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001342)                                                                                                      |
| `ICD10:('ICD10', 'K76.81')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001346](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001346)                                                                                                      |
| `ICD10:('ICD10', 'I20.I25')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001375](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001375)                                                                                                      |
| `ICD10:('ICD10', 'E75.24')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001380](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001380)                                                                                                      |
| `ICD10:('ICD10', 'E75.242')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001380](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001380)                                                                                                      |
| `ICD10:('ICD10', 'E75.249')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001380](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001380)                                                                                                      |
| `ICD10:('ICD10', 'N70-N77')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001388](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001388)                                                                                                      |
| `ICD10:('ICD10', 'H93.90')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001455](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001455)                                                                                                      |
| `ICD10:('ICD10', 'H40.20')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001506](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001506)                                                                                                      |
| `ICD10:('ICD10', 'O43.01')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001794](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001794)                                                                                                      |
| `ICD10:('ICD10', 'S52.27')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001811](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001811)                                                                                                      |
| `ICD10:('ICD10', 'H05.12')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001819](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001819)                                                                                                      |
| `ICD10:('ICD10', 'H11.15')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001824](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001824)                                                                                                      |
| `ICD10:('ICD10', 'K68.12')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001832](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001832)                                                                                                      |
| `ICD10:('ICD10', 'F40.00')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001872](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001872)                                                                                                      |
| `ICD10:('ICD10', 'L99.0*')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001882](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001882)                                                                                                      |
| `ICD10:('ICD10', 'D3A.8')`   |              1 | [http://www.ebi.ac.uk/efo/EFO:1001901](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001901)                                                                                                      |
| `ICD10:('ICD10', 'F40.10')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001917](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001917)                                                                                                      |
| `ICD10:('ICD10', 'N00.N08')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1002049](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1002049)                                                                                                      |

## `ICDO`: International Classification of Diseases for Oncology

Overall, there were 5 invalid
xrefs to external prefixed with `ICDO` (standardized to Bioregistry
prefix [`icdo`](https://bioregistry.io/icdo)) that
did not match the standard pattern `^[8-9]\d{3}(/[0-3])?$`.

| external_xref              |   usages_count | usages                                                                                                                                                                                                   |
|----------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ICDO:('ICDO', '0000/0')`  |              2 | [http://www.ebi.ac.uk/efo/EFO:1000159](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000159), [http://www.ebi.ac.uk/efo/EFO:1000508](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000508) |
| `ICDO:('ICDO', 'M9861/3')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000330](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000330)                                                                                                      |
| `ICDO:('ICDO', '981-983')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004289](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004289)                                                                                                      |
| `ICDO:('ICDO', '8000/6')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0009709](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009709)                                                                                                      |

## `IDO`: Infectious Disease Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `IDO` (standardized to Bioregistry
prefix [`ido`](https://bioregistry.io/ido)) that
did not match the standard pattern `^[0-9]+$`.

| external_xref                |   usages_count | usages                                                                                              |
|------------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `IDO:('IDO', 'IDO_0000436')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005741](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005741) |

## `KEGG`: Kyoto Encyclopedia of Genes and Genomes

Overall, there were 18 invalid
xrefs to external prefixed with `KEGG` (standardized to Bioregistry
prefix [`kegg`](https://bioregistry.io/kegg)) that
did not match the standard pattern `^([CHDEGTMKR]\d+)|(\w+:[\w\d\.-]*)|([a-z]{3,5})|(\w{2,4}\d{5})$`.

| external_xref            |   usages_count | usages                                                                                              |
|--------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `KEGG:('KEGG', '05221')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000222](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000222) |
| `KEGG:('KEGG', '05220')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000339](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000339) |
| `KEGG:('KEGG', '05414')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000407](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000407) |
| `KEGG:('KEGG', '05410')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000538](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000538) |
| `KEGG:('KEGG', '05133')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000650](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000650) |
| `KEGG:('KEGG', '05323')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000685](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000685) |
| `KEGG:('KEGG', '05222')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000702](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000702) |
| `KEGG:('KEGG', '05218')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000756](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000756) |
| `KEGG:('KEGG', '05215')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0001663](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001663) |
| `KEGG:('KEGG', '05322')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0002690](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002690) |
| `KEGG:('KEGG', '05223')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003060](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003060) |
| `KEGG:('KEGG', '05321')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003767](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003767) |
| `KEGG:('KEGG', '05020')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004720](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004720) |
| `KEGG:('KEGG', '05143')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005225](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005225) |
| `KEGG:('KEGG', '05131')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005585](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005585) |
| `KEGG:('KEGG', '05210')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005842](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005842) |
| `KEGG:('KEGG', '05416')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009609](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009609) |
| `KEGG:('KEGG', '05212')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000359](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000359) |

## `MedDRA`: Medical Dictionary for Regulatory Activities Terminology

Overall, there were 9 invalid
xrefs to external prefixed with `MedDRA` (standardized to Bioregistry
prefix [`meddra`](https://bioregistry.io/meddra)) that
did not match the standard pattern `^\d+$`.

| external_xref                          |   usages_count | usages                                                                                              |
|----------------------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `MedDRA:('MedDRA', 'C0023462')`        |              1 | [http://www.ebi.ac.uk/efo/EFO:0003025](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003025) |
| `MedDRA:('MedDRA', '10020MedDRA:100')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003964](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003964) |
| `MedDRA:('MedDRA', '100MedDRA:10022')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0007213](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007213) |
| `MedDRA:('MedDRA', '10045MedDRA:100')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0007529](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007529) |
| `MedDRA:('MedDRA', '1005MedDRA:1006')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009248](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009248) |
| `MedDRA:('MedDRA', '1000MedDRA:1002')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009657](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009657) |
| `MedDRA:('MedDRA', '1001MedDRA:1007')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000879](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000879) |
| `MedDRA:('MedDRA', '1001MedDRA:1009')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000879](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000879) |
| `MedDRA:('MedDRA', '10049MedDRA:100')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001835](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001835) |

## `MedlinePlus`: MedlinePlus Health Topics

Overall, there were 1 invalid
xrefs to external prefixed with `MedlinePlus` (standardized to Bioregistry
prefix [`medlineplus`](https://bioregistry.io/medlineplus)) that
did not match the standard pattern `^\d+$`.

| external_xref                            |   usages_count | usages                                                                                              |
|------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `MedlinePlus:('MedlinePlus', ' 001381')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000777](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000777) |

## `MeSH`: Medical Subject Headings

Overall, there were 8 invalid
xrefs to external prefixed with `MeSH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref               |   usages_count | usages                                                                                                                                                                                                                                                                                                        |
|-----------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MeSH:('MeSH', 'NoID')`     |              3 | [http://www.ebi.ac.uk/efo/EFO:0007233](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007233), [http://www.ebi.ac.uk/efo/EFO:0007422](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007422), [http://www.ebi.ac.uk/efo/EFO:0007441](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007441) |
| `MeSH:('MeSH', 'DO16518')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004122](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004122)                                                                                                                                                                                                           |
| `MeSH:('MeSH', 'Q000401')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0004352](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004352)                                                                                                                                                                                                           |
| `MeSH:('MeSH', '68062025')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0010581](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0010581)                                                                                                                                                                                                           |
| `MeSH:('MeSH', 'Q000633')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0011061](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0011061)                                                                                                                                                                                                           |
| `MeSH:('MeSH', 'DO14076')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001216](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001216)                                                                                                                                                                                                           |

## `MONDO`: Monarch Disease Ontology

Overall, there were 1,758 invalid
xrefs to external prefixed with `MONDO` (standardized to Bioregistry
prefix [`mondo`](https://bioregistry.io/mondo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                                                       |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MONDO:('MONDO', 'patterns/location')`                              |            618 | [http://www.ebi.ac.uk/efo/EFO:0000178](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000178), [http://www.ebi.ac.uk/efo/EFO:0000181](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000181), [http://www.ebi.ac.uk/efo/EFO:0000182](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000182), [http://www.ebi.ac.uk/efo/EFO:0000191](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000191), [http://www.ebi.ac.uk/efo/EFO:0000199](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000199), ... |
| `MONDO:('MONDO', 'design_pattern')`                                 |            208 | [http://www.ebi.ac.uk/efo/EFO:0000191](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000191), [http://www.ebi.ac.uk/efo/EFO:0000319](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000319), [http://www.ebi.ac.uk/efo/EFO:0000330](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000330), [http://www.ebi.ac.uk/efo/EFO:0000405](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000405), [http://www.ebi.ac.uk/efo/EFO:0000405](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000405), ... |
| `MONDO:('MONDO', 'patterns/specific_infectious_disease_by_agent')`  |            168 | [http://www.ebi.ac.uk/efo/EFO:0000650](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000650), [http://www.ebi.ac.uk/efo/EFO:0000694](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000694), [http://www.ebi.ac.uk/efo/EFO:0000763](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000763), [http://www.ebi.ac.uk/efo/EFO:0000764](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000764), [http://www.ebi.ac.uk/efo/EFO:0000769](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000769), ... |
| `MONDO:('MONDO', 'ambiguous')`                                      |            160 | [http://www.ebi.ac.uk/efo/EFO:0000217](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000217), [http://www.ebi.ac.uk/efo/EFO:0000220](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000220), [http://www.ebi.ac.uk/efo/EFO:0000248](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000248), [http://www.ebi.ac.uk/efo/EFO:0000275](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000275), [http://www.ebi.ac.uk/efo/EFO:0000284](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000284), ... |
| `MONDO:('MONDO', 'patterns/location_top')`                          |            115 | [http://www.ebi.ac.uk/efo/EFO:0000319](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000319), [http://www.ebi.ac.uk/efo/EFO:0000405](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000405), [http://www.ebi.ac.uk/efo/EFO:0000512](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000512), [http://www.ebi.ac.uk/efo/EFO:0000524](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000524), [http://www.ebi.ac.uk/efo/EFO:0000540](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000540), ... |
| `MONDO:('MONDO', 'Lexical')`                                        |             76 | [http://www.ebi.ac.uk/efo/EFO:0000095](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000095), [http://www.ebi.ac.uk/efo/EFO:0000174](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000174), [http://www.ebi.ac.uk/efo/EFO:0000181](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000181), [http://www.ebi.ac.uk/efo/EFO:0000198](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000198), [http://www.ebi.ac.uk/efo/EFO:0000222](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000222), ... |
| `MONDO:('MONDO', 'patterns/neoplasm')`                              |             69 | [http://www.ebi.ac.uk/efo/EFO:0000294](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000294), [http://www.ebi.ac.uk/efo/EFO:0002431](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002431), [http://www.ebi.ac.uk/efo/EFO:0002626](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002626), [http://www.ebi.ac.uk/efo/EFO:0003769](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003769), [http://www.ebi.ac.uk/efo/EFO:0003817](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003817), ... |
| `MONDO:('MONDO', 'patterns/inflammatory_disease_by_site')`          |             62 | [http://www.ebi.ac.uk/efo/EFO:0000217](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000217), [http://www.ebi.ac.uk/efo/EFO:0000278](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000278), [http://www.ebi.ac.uk/efo/EFO:0000465](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000465), [http://www.ebi.ac.uk/efo/EFO:0000557](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000557), [http://www.ebi.ac.uk/efo/EFO:0000649](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000649), ... |
| `MONDO:('MONDO', 'patterns/carcinoma')`                             |             50 | [http://www.ebi.ac.uk/efo/EFO:0000178](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000178), [http://www.ebi.ac.uk/efo/EFO:0000182](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000182), [http://www.ebi.ac.uk/efo/EFO:0000216](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000216), [http://www.ebi.ac.uk/efo/EFO:0000305](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000305), [http://www.ebi.ac.uk/efo/EFO:0000501](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000501), ... |
| `MONDO:('MONDO', 'patterns/cancer')`                                |             41 | [http://www.ebi.ac.uk/efo/EFO:0000178](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000178), [http://www.ebi.ac.uk/efo/EFO:0000326](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000326), [http://www.ebi.ac.uk/efo/EFO:0005088](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005088), [http://www.ebi.ac.uk/efo/EFO:0005553](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005553), [http://www.ebi.ac.uk/efo/EFO:0005557](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005557), ... |
| `MONDO:('MONDO', 'cjm')`                                            |             28 | [http://www.ebi.ac.uk/efo/EFO:0000182](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000182), [http://www.ebi.ac.uk/efo/EFO:0000319](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000319), [http://www.ebi.ac.uk/efo/EFO:0000405](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000405), [http://www.ebi.ac.uk/efo/EFO:0000508](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000508), [http://www.ebi.ac.uk/efo/EFO:0000574](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000574), ... |
| `MONDO:('MONDO', 'DesignPattern')`                                  |             22 | [http://www.ebi.ac.uk/efo/EFO:0000216](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000216), [http://www.ebi.ac.uk/efo/EFO:0000294](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000294), [http://www.ebi.ac.uk/efo/EFO:0000305](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000305), [http://www.ebi.ac.uk/efo/EFO:0000326](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000326), [http://www.ebi.ac.uk/efo/EFO:0000673](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000673), ... |
| `MONDO:('MONDO', 'patterns/chronic')`                               |             16 | [http://www.ebi.ac.uk/efo/EFO:0000337](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000337), [http://www.ebi.ac.uk/efo/EFO:0000339](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000339), [http://www.ebi.ac.uk/efo/EFO:0000341](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000341), [http://www.ebi.ac.uk/efo/EFO:0000342](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000342), [http://www.ebi.ac.uk/efo/EFO:0002428](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002428), ... |
| `MONDO:('MONDO', 'patterns/infectious_disease_by_agent')`           |             12 | [http://www.ebi.ac.uk/efo/EFO:0000763](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000763), [http://www.ebi.ac.uk/efo/EFO:0004249](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004249), [http://www.ebi.ac.uk/efo/EFO:0007128](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007128), [http://www.ebi.ac.uk/efo/EFO:0007146](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007146), [http://www.ebi.ac.uk/efo/EFO:0007173](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007173), ... |
| `MONDO:('MONDO', 'LexicalVariant')`                                 |             12 | [http://www.ebi.ac.uk/efo/EFO:0000384](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000384), [http://www.ebi.ac.uk/efo/EFO:0003780](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003780), [http://www.ebi.ac.uk/efo/EFO:0005625](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005625), [http://www.ebi.ac.uk/efo/EFO:0005627](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005627), [http://www.ebi.ac.uk/efo/EFO:0005629](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005629), ... |
| `MONDO:('MONDO', 'patterns/malignant')`                             |             11 | [http://www.ebi.ac.uk/efo/EFO:0000311](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000311), [http://www.ebi.ac.uk/efo/EFO:0005567](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005567), [http://www.ebi.ac.uk/efo/EFO:0008545](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008545), [http://www.ebi.ac.uk/efo/EFO:1000124](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000124), [http://www.ebi.ac.uk/efo/EFO:1000348](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000348), ... |
| `MONDO:('MONDO', 'patterns/sarcoma')`                               |             10 | [http://www.ebi.ac.uk/efo/EFO:0000569](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000569), [http://www.ebi.ac.uk/efo/EFO:0000637](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000637), [http://www.ebi.ac.uk/efo/EFO:0002914](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002914), [http://www.ebi.ac.uk/efo/EFO:0002920](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002920), [http://www.ebi.ac.uk/efo/EFO:0003968](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003968), ... |
| `MONDO:('MONDO', 'patterns/basis_in_disruption_of_process')`        |              9 | [http://www.ebi.ac.uk/efo/EFO:0000589](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000589), [http://www.ebi.ac.uk/efo/EFO:0000677](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000677), [http://www.ebi.ac.uk/efo/EFO:0005269](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005269), [http://www.ebi.ac.uk/efo/EFO:0005269](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005269), [http://www.ebi.ac.uk/efo/EFO:0008499](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008499), ... |
| `MONDO:('MONDO', 'patterns/disease_series_by_gene')`                |              9 | [http://www.ebi.ac.uk/efo/EFO:0009301](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009301), [http://www.ebi.ac.uk/efo/EFO:0009301](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009301), [http://www.ebi.ac.uk/efo/EFO:1001333](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001333), [http://www.ebi.ac.uk/efo/EFO:1001501](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001501), [http://www.ebi.ac.uk/efo/EFO:1001977](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001977), ... |
| `MONDO:('MONDO', 'patterns/hereditary')`                            |              8 | [http://www.ebi.ac.uk/efo/EFO:0000508](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000508), [http://www.ebi.ac.uk/efo/EFO:0001356](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001356), [http://www.ebi.ac.uk/efo/EFO:0002945](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002945), [http://www.ebi.ac.uk/efo/EFO:0002945](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002945), [http://www.ebi.ac.uk/efo/EFO:0004128](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004128), ... |
| `MONDO:('MONDO', 'patterns/neuroendocrine_neoplasm_grade1')`        |              8 | [http://www.ebi.ac.uk/efo/EFO:1000092](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000092), [http://www.ebi.ac.uk/efo/EFO:1000094](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000094), [http://www.ebi.ac.uk/efo/EFO:1000154](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000154), [http://www.ebi.ac.uk/efo/EFO:1000188](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000188), [http://www.ebi.ac.uk/efo/EFO:1000195](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000195), ... |
| `MONDO:('MONDO', 'patterns/acute')`                                 |              7 | [http://www.ebi.ac.uk/efo/EFO:0000220](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000220), [http://www.ebi.ac.uk/efo/EFO:0000221](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000221), [http://www.ebi.ac.uk/efo/EFO:0000222](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000222), [http://www.ebi.ac.uk/efo/EFO:0002497](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002497), [http://www.ebi.ac.uk/efo/EFO:0008583](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008583), ... |
| `MONDO:('MONDO', 'patterns/allergic_form_of_disease')`              |              6 | [http://www.ebi.ac.uk/efo/EFO:0000274](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000274), [http://www.ebi.ac.uk/efo/EFO:0005854](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005854), [http://www.ebi.ac.uk/efo/EFO:0007141](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007141), [http://www.ebi.ac.uk/efo/EFO:1000668](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000668), [http://www.ebi.ac.uk/efo/EFO:1000669](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000669), ... |
| `MONDO:('MONDO', 'patterns/benign')`                                |              5 | [http://www.ebi.ac.uk/efo/EFO:0002422](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002422), [http://www.ebi.ac.uk/efo/EFO:1000028](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000028), [http://www.ebi.ac.uk/efo/EFO:1000106](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000106), [http://www.ebi.ac.uk/efo/EFO:1000108](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000108), [http://www.ebi.ac.uk/efo/EFO:1000485](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000485)      |
| `MONDO:('MONDO', 'patterns/environmental_stimulus')`                |              4 | [http://www.ebi.ac.uk/efo/EFO:0004712](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004712), [http://www.ebi.ac.uk/efo/EFO:0007153](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007153), [http://www.ebi.ac.uk/efo/EFO:1000814](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000814), [http://www.ebi.ac.uk/efo/EFO:1000851](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000851)                                                                                                           |
| `MONDO:('MONDO', 'patterns/congenital')`                            |              4 | [http://www.ebi.ac.uk/efo/EFO:0007217](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007217), [http://www.ebi.ac.uk/efo/EFO:0007218](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007218), [http://www.ebi.ac.uk/efo/EFO:0007219](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007219), [http://www.ebi.ac.uk/efo/EFO:0007220](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007220)                                                                                                           |
| `MONDO:('MONDO', 'patterns/inborn_metabolic')`                      |              3 | [http://www.ebi.ac.uk/efo/EFO:0005596](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005596), [http://www.ebi.ac.uk/efo/EFO:0005596](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005596), [http://www.ebi.ac.uk/efo/EFO:0007287](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007287)                                                                                                                                                                                                                |
| `MONDO:('MONDO', 'patterns/acquired')`                              |              3 | [http://www.ebi.ac.uk/efo/EFO:1000639](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000639), [http://www.ebi.ac.uk/efo/EFO:1000663](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000663), [http://www.ebi.ac.uk/efo/EFO:1000691](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000691)                                                                                                                                                                                                                |
| `MONDO:('MONDO', 'patterns/autosomal_recessive')`                   |              2 | [http://www.ebi.ac.uk/efo/EFO:1000017](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000017), [http://www.ebi.ac.uk/efo/EFO:1000017](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000017)                                                                                                                                                                                                                                                                                                                     |
| `MONDO:('MONDO', 'patterns/childhood')`                             |              2 | [http://www.ebi.ac.uk/efo/EFO:0000330](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000330), [http://www.ebi.ac.uk/efo/EFO:0004594](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004594)                                                                                                                                                                                                                                                                                                                     |
| `MONDO:('MONDO', 'patterns/carcinoma_in_situ')`                     |              2 | [http://www.ebi.ac.uk/efo/EFO:0000432](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000432), [http://www.ebi.ac.uk/efo/EFO:1000283](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000283)                                                                                                                                                                                                                                                                                                                     |
| `MONDO:('MONDO', 'patterns/neuroendocrine_neoplasm')`               |              2 | [http://www.ebi.ac.uk/efo/EFO:0005220](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005220), [http://www.ebi.ac.uk/efo/EFO:1001928](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001928)                                                                                                                                                                                                                                                                                                                     |
| `MONDO:('MONDO', 'patterns/adult')`                                 |              2 | [http://www.ebi.ac.uk/efo/EFO:1001933](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001933), [http://www.ebi.ac.uk/efo/EFO:1001935](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001935)                                                                                                                                                                                                                                                                                                                     |
| `MONDO:('MONDO', 'patterns/specific_inflammatory_disease_by_site')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005751](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005751)                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `MONDO:('MONDO', 'design_patterns')`                                |              1 | [http://www.ebi.ac.uk/efo/EFO:0000182](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000182)                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `MONDO:('MONDO', 'patterns/allergy')`                               |              1 | [http://www.ebi.ac.uk/efo/EFO:0009482](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009482)                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `MONDO:('MONDO', 'patterns/autosomal_dominant')`                    |              1 | [http://www.ebi.ac.uk/efo/EFO:1001496](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001496)                                                                                                                                                                                                                                                                                                                                                                                                                          |

## `NCIm`: NCI Metathesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCIm` (standardized to Bioregistry
prefix [`ncim`](https://bioregistry.io/ncim)) that
did not match the standard pattern `^C\d+$`.

| external_xref               |   usages_count | usages                                                                                              |
|-----------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `NCIm:('NCIm', 'CL455363')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003918](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003918) |

## `NCIT`: NCI Thesaurus

Overall, there were 360 invalid
xrefs to external prefixed with `NCIT` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                     |   usages_count | usages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `NCIT:('NCIT', 'P378')`           |            359 | [http://www.ebi.ac.uk/efo/EFO:0000096](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000096), [http://www.ebi.ac.uk/efo/EFO:0000186](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000186), [http://www.ebi.ac.uk/efo/EFO:0000248](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000248), [http://www.ebi.ac.uk/efo/EFO:0000266](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000266), [http://www.ebi.ac.uk/efo/EFO:0000275](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000275), ... |
| `NCIT:('NCIT', 'C92189-variant')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001417](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001417)                                                                                                                                                                                                                                                                                                                                                                                                                          |

## `NCIt`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCIt` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref              |   usages_count | usages                                                                                              |
|----------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `NCIt:('NCIt', ' C12511')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0001394](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001394) |

## `OBI`: Ontology for Biomedical Investigations

Overall, there were 1 invalid
xrefs to external prefixed with `OBI` (standardized to Bioregistry
prefix [`obi`](https://bioregistry.io/obi)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                |   usages_count | usages                                                                                              |
|------------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `OBI:('OBI', 'OBI_1110054')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005140](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005140) |

## `OMIMPS`: OMIM Phenotypic Series

Overall, there were 56 invalid
xrefs to external prefixed with `OMIMPS` (standardized to Bioregistry
prefix [`omim.ps`](https://bioregistry.io/omim.ps)) that
did not match the standard pattern `^PS\d+$`.

| external_xref                 |   usages_count | usages                                                                                                                                                                                                   |
|-------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `OMIMPS:('OMIMPS', '600512')` |              2 | [http://www.ebi.ac.uk/efo/EFO:0000773](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000773), [http://www.ebi.ac.uk/efo/EFO:0000773](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000773) |
| `OMIMPS:('OMIMPS', '603075')` |              2 | [http://www.ebi.ac.uk/efo/EFO:0001365](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001365), [http://www.ebi.ac.uk/efo/EFO:0001365](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001365) |
| `OMIMPS:('OMIMPS', '190300')` |              2 | [http://www.ebi.ac.uk/efo/EFO:0003108](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003108), [http://www.ebi.ac.uk/efo/EFO:0003108](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003108) |
| `OMIMPS:('OMIMPS', '608638')` |              2 | [http://www.ebi.ac.uk/efo/EFO:0003757](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003757), [http://www.ebi.ac.uk/efo/EFO:0003757](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003757) |
| `OMIMPS:('OMIMPS', '608207')` |              2 | [http://www.ebi.ac.uk/efo/EFO:0005045](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005045), [http://www.ebi.ac.uk/efo/EFO:0005045](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005045) |
| `OMIMPS:('OMIMPS', '106600')` |              2 | [http://www.ebi.ac.uk/efo/EFO:0005410](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005410), [http://www.ebi.ac.uk/efo/EFO:0005410](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005410) |
| `OMIMPS:('OMIMPS', '212065')` |              2 | [http://www.ebi.ac.uk/efo/EFO:0005545](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005545), [http://www.ebi.ac.uk/efo/EFO:0005545](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005545) |
| `OMIMPS:('OMIMPS', '212066')` |              2 | [http://www.ebi.ac.uk/efo/EFO:0005546](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005546), [http://www.ebi.ac.uk/efo/EFO:0005546](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005546) |
| `OMIMPS:('OMIMPS', '310700')` |              2 | [http://www.ebi.ac.uk/efo/EFO:0007217](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007217), [http://www.ebi.ac.uk/efo/EFO:0007217](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007217) |
| `OMIMPS:('OMIMPS', '256450')` |              2 | [http://www.ebi.ac.uk/efo/EFO:0007318](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007318), [http://www.ebi.ac.uk/efo/EFO:0007318](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007318) |
| `OMIMPS:('OMIMPS', '607765')` |              2 | [http://www.ebi.ac.uk/efo/EFO:0009039](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009039), [http://www.ebi.ac.uk/efo/EFO:0009039](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009039) |
| `OMIMPS:('OMIMPS', '231090')` |              2 | [http://www.ebi.ac.uk/efo/EFO:1000298](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000298), [http://www.ebi.ac.uk/efo/EFO:1000298](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000298) |
| `OMIMPS:('OMIMPS', '168000')` |              2 | [http://www.ebi.ac.uk/efo/EFO:1000453](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000453), [http://www.ebi.ac.uk/efo/EFO:1000453](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000453) |
| `OMIMPS:('OMIMPS', '608594')` |              2 | [http://www.ebi.ac.uk/efo/EFO:1000681](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000681), [http://www.ebi.ac.uk/efo/EFO:1000681](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000681) |
| `OMIMPS:('OMIMPS', '109720')` |              2 | [http://www.ebi.ac.uk/efo/EFO:1001486](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001486), [http://www.ebi.ac.uk/efo/EFO:1001486](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001486) |
| `OMIMPS:('OMIMPS', '209850')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003758](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003758)                                                                                                      |
| `OMIMPS:('OMIMPS', '603165')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000274](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000274)                                                                                                      |
| `OMIMPS:('OMIMPS', '258150')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000279](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000279)                                                                                                      |
| `OMIMPS:('OMIMPS', '192600')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000538](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000538)                                                                                                      |
| `OMIMPS:('OMIMPS', '189800')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000668](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000668)                                                                                                      |
| `OMIMPS:('OMIMPS', '177900')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000676](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000676)                                                                                                      |
| `OMIMPS:('OMIMPS', '212750')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0001060](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001060)                                                                                                      |
| `OMIMPS:('OMIMPS', '105400')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0001356](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001356)                                                                                                      |
| `OMIMPS:('OMIMPS', '266600')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003767](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003767)                                                                                                      |
| `OMIMPS:('OMIMPS', '600803')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003832](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003832)                                                                                                      |
| `OMIMPS:('OMIMPS', '115430')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004143](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004143)                                                                                                      |
| `OMIMPS:('OMIMPS', '161950')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004194](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004194)                                                                                                      |
| `OMIMPS:('OMIMPS', '300633')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004209](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004209)                                                                                                      |
| `OMIMPS:('OMIMPS', '166800')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004213](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004213)                                                                                                      |
| `OMIMPS:('OMIMPS', '603278')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004236](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004236)                                                                                                      |
| `OMIMPS:('OMIMPS', '167250')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004261](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004261)                                                                                                      |
| `OMIMPS:('OMIMPS', '102300')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004270](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004270)                                                                                                      |
| `OMIMPS:('OMIMPS', '143890')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004911](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004911)                                                                                                      |
| `OMIMPS:('OMIMPS', '600165')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005569](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005569)                                                                                                      |
| `OMIMPS:('OMIMPS', '600669')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005917](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005917)                                                                                                      |
| `OMIMPS:('OMIMPS', '305400')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009297](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009297)                                                                                                      |
| `OMIMPS:('OMIMPS', '153600')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009441](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009441)                                                                                                      |
| `OMIMPS:('OMIMPS', '142700')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000648](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000648)                                                                                                      |
| `OMIMPS:('OMIMPS', '175800')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000757](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000757)                                                                                                      |
| `OMIMPS:('OMIMPS', '108800')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000825](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000825)                                                                                                      |
| `OMIMPS:('OMIMPS', '606711')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001510](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001510)                                                                                                      |

## `ORDO`: Orphanet Rare Disease Ontology

Overall, there were 13 invalid
xrefs to external prefixed with `ORDO` (standardized to Bioregistry
prefix [`orphanet.ordo`](https://bioregistry.io/orphanet.ordo)) that
did not match the standard pattern `^Orphanet(_|:)C?\d+$`.

| external_xref             |   usages_count | usages                                                                                              |
|---------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `ORDO:('ORDO', '183')`    |              1 | [http://www.ebi.ac.uk/efo/EFO:0007208](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007208) |
| `ORDO:('ORDO', '99879')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0008506](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008506) |
| `ORDO:('ORDO', '99878')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0008519](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008519) |
| `ORDO:('ORDO', '767')`    |              1 | [http://www.ebi.ac.uk/efo/EFO:0009012](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009012) |
| `ORDO:('ORDO', '178493')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009201](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009201) |
| `ORDO:('ORDO', '137810')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001882](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001882) |
| `ORDO:('ORDO', '81')`     |              1 | [http://www.ebi.ac.uk/efo/EFO:1001982](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001982) |
| `ORDO:('ORDO', '466775')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001983](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001983) |
| `ORDO:('ORDO', '45358')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001985](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001985) |
| `ORDO:('ORDO', '447881')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001987](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001987) |
| `ORDO:('ORDO', '65684')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:1001989](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001989) |
| `ORDO:('ORDO', '431255')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001992](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001992) |
| `ORDO:('ORDO', '869')`    |              1 | [http://www.ebi.ac.uk/efo/EFO:1001997](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001997) |

## `PMID`: PubMed

Overall, there were 8 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                 |   usages_count | usages                                                                                              |
|-------------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `PMID:('PMID', ' 11246871')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0002540](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0002540) |
| `PMID:('PMID', 'PMC1531688')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005725](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005725) |
| `PMID:('PMID', ' 3897439')`   |              1 | [http://www.ebi.ac.uk/efo/EFO:0005910](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005910) |
| `PMID:('PMID', ' 8788275')`   |              1 | [http://www.ebi.ac.uk/efo/EFO:0005913](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005913) |
| `PMID:('PMID', '27149984 ')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0007836](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007836) |
| `PMID:('PMID', ' 31636452')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0010605](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0010605) |
| `PMID:('PMID', '25167691 ')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0010695](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0010695) |
| `PMID:('PMID', ' 32355309')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0010749](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0010749) |

## `PR`: Protein Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `PR` (standardized to Bioregistry
prefix [`pr`](https://bioregistry.io/pr)) that
did not match the standard pattern `^\d+$`.

| external_xref         |   usages_count | usages                                                                                              |
|-----------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `PR:('PR', 'Q92496')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0600091](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0600091) |

## `Reactome`: Reactome

Overall, there were 3 invalid
xrefs to external prefixed with `Reactome` (standardized to Bioregistry
prefix [`reactome`](https://bioregistry.io/reactome)) that
did not match the standard pattern `^R-[A-Z]{3}-\d+(-\d+)?(\.\d+)?$`.

| external_xref                     |   usages_count | usages                                                                                              |
|-----------------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `Reactome:('Reactome', 'Q9HB96')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009914](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009914) |
| `Reactome:('Reactome', 'Q9ULP9')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009915](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009915) |
| `Reactome:('Reactome', 'Q9NP58')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009916](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009916) |

## `SNOMEDCT`: SNOMED CT (International Edition)

Overall, there were 3 invalid
xrefs to external prefixed with `SNOMEDCT` (standardized to Bioregistry
prefix [`snomedct`](https://bioregistry.io/snomedct)) that
did not match the standard pattern `^(\w+)?\d+$`.

| external_xref                         |   usages_count | usages                                                                                              |
|---------------------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `SNOMEDCT:('SNOMEDCT', ' 266417001')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0010688](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0010688) |
| `SNOMEDCT:('SNOMEDCT', '88039007 ')`  |              1 | [http://www.ebi.ac.uk/efo/EFO:0010721](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0010721) |
| `SNOMEDCT:('SNOMEDCT', ' 274897005')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001841](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001841) |

## `TADS`: Tick Anatomy Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `TADS` (standardized to Bioregistry
prefix [`tads`](https://bioregistry.io/tads)) that
did not match the standard pattern `^\d{7}$`.

| external_xref             |   usages_count | usages                                                                                              |
|---------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `TADS:('TADS', '000315')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000935](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000935) |

## `TGMA`: Mosquito gross anatomy ontology

Overall, there were 1 invalid
xrefs to external prefixed with `TGMA` (standardized to Bioregistry
prefix [`tgma`](https://bioregistry.io/tgma)) that
did not match the standard pattern `^\d{7}$`.

| external_xref             |   usages_count | usages                                                                                              |
|---------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `TGMA:('TGMA', '000136')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000965](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000965) |

## `UMLS`: Unified Medical Language System Concept Unique Identifier

Overall, there were 88 invalid
xrefs to external prefixed with `UMLS` (standardized to Bioregistry
prefix [`umls`](https://bioregistry.io/umls)) that
did not match the standard pattern `^C\d+$`.

| external_xref               |   usages_count | usages                                                                                              |
|-----------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| `UMLS:('UMLS', 'CN242113')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000350](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000350) |
| `UMLS:('UMLS', 'CN043071')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000384](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000384) |
| `UMLS:('UMLS', 'CN227279')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000519](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000519) |
| `UMLS:('UMLS', 'CN236663')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000551](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000551) |
| `UMLS:('UMLS', 'CN236628')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000616](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000616) |
| `UMLS:('UMLS', 'CN205405')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000621](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000621) |
| `UMLS:('UMLS', 'CN205129')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000640](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000640) |
| `UMLS:('UMLS', 'CN240636')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000677](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000677) |
| `UMLS:('UMLS', 'CN202001')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000693](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000693) |
| `UMLS:('UMLS', 'CN244903')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000702](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000702) |
| `UMLS:('UMLS', 'CN206012')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000717](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000717) |
| `UMLS:('UMLS', 'CN971653')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000756](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000756) |
| `UMLS:('UMLS', 'CN204440')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0000775](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0000775) |
| `UMLS:('UMLS', 'CN200519')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0001361](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0001361) |
| `UMLS:('UMLS', 'CN236639')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003144](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003144) |
| `UMLS:('UMLS', 'CN236661')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003777](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003777) |
| `UMLS:('UMLS', 'CN239852')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003777](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003777) |
| `UMLS:('UMLS', 'CN236627')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003869](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003869) |
| `UMLS:('UMLS', 'CN236629')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003893](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003893) |
| `UMLS:('UMLS', 'CN580792')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0003900](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003900) |
| `UMLS:('UMLS', 'CN205090')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004209](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004209) |
| `UMLS:('UMLS', 'CN043606')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004236](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004236) |
| `UMLS:('UMLS', 'CN236651')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004240](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004240) |
| `UMLS:('UMLS', 'CN236678')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004247](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004247) |
| `UMLS:('UMLS', 'CN204768')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004260](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004260) |
| `UMLS:('UMLS', 'CN240645')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004262](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004262) |
| `UMLS:('UMLS', 'CN118841')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0004911](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004911) |
| `UMLS:('UMLS', 'CN169364')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005207](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005207) |
| `UMLS:('UMLS', 'CN237762')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005222](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005222) |
| `UMLS:('UMLS', 'CN169366')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005410](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005410) |
| `UMLS:('UMLS', 'CN204600')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005717](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005717) |
| `UMLS:('UMLS', 'CN237663')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005783](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005783) |
| `UMLS:('UMLS', 'CN206939')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005803](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005803) |
| `UMLS:('UMLS', 'CN882913')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005803](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005803) |
| `UMLS:('UMLS', 'CN206062')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0005855](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0005855) |
| `UMLS:('UMLS', 'CN205033')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0006462](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0006462) |
| `UMLS:('UMLS', 'CN242134')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0006513](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0006513) |
| `UMLS:('UMLS', 'CN206037')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0007135](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007135) |
| `UMLS:('UMLS', 'CN199179')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0007183](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007183) |
| `UMLS:('UMLS', 'CN205187')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0007195](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007195) |
| `UMLS:('UMLS', 'CN201384')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0007211](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007211) |
| `UMLS:('UMLS', 'CN205282')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0007342](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007342) |
| `UMLS:('UMLS', 'CN203069')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0007460](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0007460) |
| `UMLS:('UMLS', 'CN776941')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0008493](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008493) |
| `UMLS:('UMLS', 'CN204884')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0008507](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008507) |
| `UMLS:('UMLS', 'CN237754')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0008597](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008597) |
| `UMLS:('UMLS', 'CN206006')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0008598](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008598) |
| `UMLS:('UMLS', 'CN205981')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0008613](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008613) |
| `UMLS:('UMLS', 'CL520437')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0008614](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008614) |
| `UMLS:('UMLS', 'CN239183')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009039](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009039) |
| `UMLS:('UMLS', 'CN202862')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009068](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009068) |
| `UMLS:('UMLS', 'CN240512')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009068](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009068) |
| `UMLS:('UMLS', 'CN237682')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009160](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009160) |
| `UMLS:('UMLS', 'CN237555')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009199](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009199) |
| `UMLS:('UMLS', 'CN226092')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009266](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009266) |
| `UMLS:('UMLS', 'CN737161')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009300](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009300) |
| `UMLS:('UMLS', 'CN237671')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009553](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009553) |
| `UMLS:('UMLS', 'CN072436')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0009907](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009907) |
| `UMLS:('UMLS', 'CN206246')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0010580](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0010580) |
| `UMLS:('UMLS', 'CN226945')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000015](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000015) |
| `UMLS:('UMLS', 'CN203416')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000027](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000027) |
| `UMLS:('UMLS', 'CN201941')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000028](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000028) |
| `UMLS:('UMLS', 'CN205034')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000042](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000042) |
| `UMLS:('UMLS', 'CL343552')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000056](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000056) |
| `UMLS:('UMLS', 'CN202866')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000129](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000129) |
| `UMLS:('UMLS', 'CN201056')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000242](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000242) |
| `UMLS:('UMLS', 'CN237470')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000278](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000278) |
| `UMLS:('UMLS', 'CN206982')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000297](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000297) |
| `UMLS:('UMLS', 'CN203938')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000314](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000314) |
| `UMLS:('UMLS', 'CN202288')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000395](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000395) |
| `UMLS:('UMLS', 'CN204702')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000570](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000570) |
| `UMLS:('UMLS', 'CN207411')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000576](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000576) |
| `UMLS:('UMLS', 'CN201658')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000737](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000737) |
| `UMLS:('UMLS', 'CN202712')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000780](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000780) |
| `UMLS:('UMLS', 'CN205287')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000797](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000797) |
| `UMLS:('UMLS', 'CN242089')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1000850](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000850) |
| `UMLS:('UMLS', 'CN203409')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001142](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001142) |
| `UMLS:('UMLS', 'CN206761')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001221](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001221) |
| `UMLS:('UMLS', 'CN226908')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001473](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001473) |
| `UMLS:('UMLS', 'CN119611')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001496](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001496) |
| `UMLS:('UMLS', 'CN206284')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001901](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001901) |
| `UMLS:('UMLS', 'CN237515')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001928](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001928) |
| `UMLS:('UMLS', 'CN221574')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001951](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001951) |
| `UMLS:('UMLS', 'CN204398')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001968](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001968) |
| `UMLS:('UMLS', 'CN237712')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1001987](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001987) |
| `UMLS:('UMLS', 'CN205479')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1002000](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1002000) |
| `UMLS:('UMLS', 'CN207484')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1002008](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1002008) |
| `UMLS:('UMLS', 'CN580795')` |              1 | [http://www.ebi.ac.uk/efo/EFO:1002049](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1002049) |

## `Wikipedia`: Wikipedia

Overall, there were 17 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                                                          |   usages_count | usages                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Wikipedia:('Wikipedia', 'Single cell sequencing')`                                    |              2 | [http://www.ebi.ac.uk/efo/EFO:0008913](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008913), [http://www.ebi.ac.uk/efo/EFO:0008913](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008913) |
| `Wikipedia:('Wikipedia', 'Multiple_displacement_amplification#Phi_29_DNA_polymerase')` |              1 | [http://www.ebi.ac.uk/efo/EFO:0008864](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0008864)                                                                                                      |
| `Wikipedia:('Wikipedia', "Hashimoto's_thyroiditis")`                                   |              1 | [http://www.ebi.ac.uk/efo/EFO:0003779](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0003779)                                                                                                      |
| `Wikipedia:('Wikipedia', 'Darier%27s_disease')`                                        |              1 | [http://www.ebi.ac.uk/efo/EFO:0004124](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0004124)                                                                                                      |
| `Wikipedia:('Wikipedia', 'Iodine-131#Treatment_of_thyroid_cancer')`                    |              1 | [http://www.ebi.ac.uk/efo/EFO:0009600](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009600)                                                                                                      |
| `Wikipedia:('Wikipedia', 'Ataxia#Hereditary_ataxias')`                                 |              1 | [http://www.ebi.ac.uk/efo/EFO:0009671](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009671)                                                                                                      |
| `Wikipedia:('Wikipedia', 'Dissociation_(psychology)')`                                 |              1 | [http://www.ebi.ac.uk/efo/EFO:0009750](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0009750)                                                                                                      |
| `Wikipedia:('Wikipedia', '17α-Hydroxyprogesterone')`                                   |              1 | [http://www.ebi.ac.uk/efo/EFO:0010220](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:0010220)                                                                                                      |
| `Wikipedia:('Wikipedia', "Prinzmetal's_angina")`                                       |              1 | [http://www.ebi.ac.uk/efo/EFO:1000013](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000013)                                                                                                      |
| `Wikipedia:('Wikipedia', 'Urticaria#Allergic_urticaria')`                              |              1 | [http://www.ebi.ac.uk/efo/EFO:1000669](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000669)                                                                                                      |
| `Wikipedia:('Wikipedia', "Kimura's_disease")`                                          |              1 | [http://www.ebi.ac.uk/efo/EFO:1000722](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000722)                                                                                                      |
| `Wikipedia:('Wikipedia', "Ludwig's_angina")`                                           |              1 | [http://www.ebi.ac.uk/efo/EFO:1000730](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000730)                                                                                                      |
| `Wikipedia:('Wikipedia', 'Urticaria#Vibratory_angioedema')`                            |              1 | [http://www.ebi.ac.uk/efo/EFO:1000775](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1000775)                                                                                                      |
| `Wikipedia:('Wikipedia', 'Niemann–Pick_disease')`                                      |              1 | [http://www.ebi.ac.uk/efo/EFO:1001380](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001380)                                                                                                      |
| `Wikipedia:('Wikipedia', "Susac's_syndrome")`                                          |              1 | [http://www.ebi.ac.uk/efo/EFO:1001856](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001856)                                                                                                      |
| `Wikipedia:('Wikipedia', 'Morvan%27s_syndrome')`                                       |              1 | [http://www.ebi.ac.uk/efo/EFO:1001897](https://bioregistry.io/http://www.ebi.ac.uk/efo/EFO:1001897)                                                                                                      |

