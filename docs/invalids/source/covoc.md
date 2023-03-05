# covoc

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `covoc`. See the [GitHub repository](https://github.com/EBISPOT/covoc).


## `ATC`: Anatomical Therapeutic Chemical Classification System

Overall, there were 3 invalid
xrefs to external prefixed with `ATC` (standardized to Bioregistry
prefix [`atc`](https://bioregistry.io/atc)) that
did not match the standard pattern `^[A-Z](\d+([A-Z]{1,2}(\d+)?)?)?$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `ATC: D11AX22`  |              1 | [CHEBI:6078](http://purl.obolibrary.org/obo/CHEBI_6078)   |
| `ATC: N02BB02`  |              1 | [CHEBI:62088](http://purl.obolibrary.org/obo/CHEBI_62088) |
| `ATC: C09BA13`  |              1 | [CHEBI:6960](http://purl.obolibrary.org/obo/CHEBI_6960)   |

## `CARO`: Common Anatomy Reference Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `CARO` (standardized to Bioregistry
prefix [`caro`](https://bioregistry.io/caro)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `CARO:mah`      |              1 | [CL:0000000](http://purl.obolibrary.org/obo/CL_0000000) |

## `ChEMBL`: ChEMBL

Overall, there were 4 invalid
xrefs to external prefixed with `ChEMBL` (standardized to Bioregistry
prefix [`chembl`](https://bioregistry.io/chembl)) that
did not match the standard pattern `^CHEMBL\d+$`.

| external_xref    |   usages_count | usages                                                        |
|------------------|----------------|---------------------------------------------------------------|
| `ChEMBL:477164`  |              1 | [COVOC:0030001](http://purl.obolibrary.org/obo/COVOC_0030001) |
| `ChEMBL:1201580` |              1 | [COVOC:0030002](http://purl.obolibrary.org/obo/COVOC_0030002) |
| `ChEMBL:2106041` |              1 | [COVOC:0030004](http://purl.obolibrary.org/obo/COVOC_0030004) |
| `ChEMBL:519846`  |              1 | [COVOC:0030005](http://purl.obolibrary.org/obo/COVOC_0030005) |

## `FB`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `FB` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `FB:ma`         |              1 | [CL:0000134](http://purl.obolibrary.org/obo/CL_0000134) |

## `GenPept`: GenPept

Overall, there were 24 invalid
xrefs to external prefixed with `GenPept` (standardized to Bioregistry
prefix [`genpept`](https://bioregistry.io/genpept)) that
did not match the standard pattern `^\w{3}\d{5}(\.\d+)?$`.

| external_xref          |   usages_count | usages                                                                                                                                                              |
|------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GenPept:YP_009724390` |              3 | [PR:P0DTC2](http://purl.obolibrary.org/obo/PR_P0DTC2), [PR:P0DTC2](http://purl.obolibrary.org/obo/PR_P0DTC2), [PR:P0DTC2](http://purl.obolibrary.org/obo/PR_P0DTC2) |
| `GenPept:YP_009724391` |              3 | [PR:P0DTC3](http://purl.obolibrary.org/obo/PR_P0DTC3), [PR:P0DTC3](http://purl.obolibrary.org/obo/PR_P0DTC3), [PR:P0DTC3](http://purl.obolibrary.org/obo/PR_P0DTC3) |
| `GenPept:YP_009724392` |              3 | [PR:P0DTC4](http://purl.obolibrary.org/obo/PR_P0DTC4), [PR:P0DTC4](http://purl.obolibrary.org/obo/PR_P0DTC4), [PR:P0DTC4](http://purl.obolibrary.org/obo/PR_P0DTC4) |
| `GenPept:YP_009724393` |              3 | [PR:P0DTC5](http://purl.obolibrary.org/obo/PR_P0DTC5), [PR:P0DTC5](http://purl.obolibrary.org/obo/PR_P0DTC5), [PR:P0DTC5](http://purl.obolibrary.org/obo/PR_P0DTC5) |
| `GenPept:YP_009724395` |              3 | [PR:P0DTC7](http://purl.obolibrary.org/obo/PR_P0DTC7), [PR:P0DTC7](http://purl.obolibrary.org/obo/PR_P0DTC7), [PR:P0DTC7](http://purl.obolibrary.org/obo/PR_P0DTC7) |
| `GenPept:YP_009725299` |              2 | [PR:000050272](http://purl.obolibrary.org/obo/PR_000050272), [PR:000050272](http://purl.obolibrary.org/obo/PR_000050272)                                            |
| `GenPept:YP_009725295` |              2 | [PR:P0DTC1-1](http://purl.obolibrary.org/obo/PR_P0DTC1-1), [PR:P0DTC1-1](http://purl.obolibrary.org/obo/PR_P0DTC1-1)                                                |
| `GenPept:YP_009724397` |              2 | [PR:P0DTC9](http://purl.obolibrary.org/obo/PR_P0DTC9), [PR:P0DTC9](http://purl.obolibrary.org/obo/PR_P0DTC9)                                                        |
| `GenPept:YP_009724389` |              2 | [PR:P0DTD1-1](http://purl.obolibrary.org/obo/PR_P0DTD1-1), [PR:P0DTD1-1](http://purl.obolibrary.org/obo/PR_P0DTD1-1)                                                |
| `GenPept:YP_009742610` |              1 | [PR:000050272](http://purl.obolibrary.org/obo/PR_000050272)                                                                                                         |

## `GEO`: NCBI Gene Expression Omnibus

Overall, there were 1 invalid
xrefs to external prefixed with `GEO` (standardized to Bioregistry
prefix [`geo`](https://bioregistry.io/geo)) that
did not match the standard pattern `^G(PL|SM|SE|DS)\d+$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `GEO:000000374` |              1 | [COVOC:0070006](http://purl.obolibrary.org/obo/COVOC_0070006) |

## `Gmelin`: Gmelins Handbuch der anorganischen Chemie

Overall, there were 2 invalid
xrefs to external prefixed with `Gmelin` (standardized to Bioregistry
prefix [`gmelin`](https://bioregistry.io/gmelin)) that
did not match the standard pattern `^[1-9][0-9]{3,6}$`.

| external_xref   |   usages_count | usages                                                    |
|-----------------|----------------|-----------------------------------------------------------|
| `Gmelin:485`    |              1 | [CHEBI:15379](http://purl.obolibrary.org/obo/CHEBI_15379) |
| `Gmelin:509`    |              1 | [CHEBI:16240](http://purl.obolibrary.org/obo/CHEBI_16240) |

## `HPO`: Human Phenotype Ontology

Overall, there were 20 invalid
xrefs to external prefixed with `HPO` (standardized to Bioregistry
prefix [`hp`](https://bioregistry.io/hp)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HPO:probinson` |             18 | [HP:0000822](http://purl.obolibrary.org/obo/HP_0000822), [HP:0000969](http://purl.obolibrary.org/obo/HP_0000969), [HP:0000988](http://purl.obolibrary.org/obo/HP_0000988), [HP:0000989](http://purl.obolibrary.org/obo/HP_0000989), [HP:0001025](http://purl.obolibrary.org/obo/HP_0001025), ... |
| `HPO:sdoelken`  |              1 | [HP:0001945](http://purl.obolibrary.org/obo/HP_0001945)                                                                                                                                                                                                                                          |
| `HPO:skoehler`  |              1 | [HP:0003326](http://purl.obolibrary.org/obo/HP_0003326)                                                                                                                                                                                                                                          |

## `ICD11`: International Classification of Diseases, 11th Revision

Overall, there were 2 invalid
xrefs to external prefixed with `ICD11` (standardized to Bioregistry
prefix [`icd11`](https://bioregistry.io/icd11)) that
did not match the standard pattern `^[1-9]\d*$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `ICD11:RA01.0`  |              1 | [MONDO:0100096](http://purl.obolibrary.org/obo/MONDO_0100096) |
| `ICD11:RA01.2`  |              1 | [MONDO:0100096](http://purl.obolibrary.org/obo/MONDO_0100096) |

## `ICD9`: International Classification of Diseases, 9th Revision

Overall, there were 7 invalid
xrefs to external prefixed with `ICD9` (standardized to Bioregistry
prefix [`icd9`](https://bioregistry.io/icd9)) that
did not match the standard pattern `^(\d\d\d|V\d\d|E[8-9]\d\d)(\.\d{1,2})?$`.

| external_xref     |   usages_count | usages                                                        |
|-------------------|----------------|---------------------------------------------------------------|
| `ICD9:390-459.99` |              1 | [MONDO:0004995](http://purl.obolibrary.org/obo/MONDO_0004995) |
| `ICD9:420-429.99` |              1 | [MONDO:0004995](http://purl.obolibrary.org/obo/MONDO_0004995) |
| `ICD9:490-496.99` |              1 | [MONDO:0005002](http://purl.obolibrary.org/obo/MONDO_0005002) |
| `ICD9:060-066.99` |              1 | [MONDO:0005108](http://purl.obolibrary.org/obo/MONDO_0005108) |
| `ICD9:460-519.99` |              1 | [EFO:0000684](http://www.ebi.ac.uk/efo/EFO_0000684)           |
| `ICD9:500-508.99` |              1 | [EFO:0000684](http://www.ebi.ac.uk/efo/EFO_0000684)           |
| `ICD9:510-519.99` |              1 | [EFO:0000684](http://www.ebi.ac.uk/efo/EFO_0000684)           |

## `IEDB`: Immune Epitope Database

Overall, there were 1 invalid
xrefs to external prefixed with `IEDB` (standardized to Bioregistry
prefix [`iedb`](https://bioregistry.io/iedb)) that
did not match the standard pattern `^[0-9]+$`.

| external_xref   |   usages_count | usages                                                      |
|-----------------|----------------|-------------------------------------------------------------|
| `IEDB:BP`       |              1 | [PR:000000001](http://purl.obolibrary.org/obo/PR_000000001) |

## `KEGG`: Kyoto Encyclopedia of Genes and Genomes

Overall, there were 1 invalid
xrefs to external prefixed with `KEGG` (standardized to Bioregistry
prefix [`kegg`](https://bioregistry.io/kegg)) that
did not match the standard pattern `^([CHDEGTMKR]\d+)|(\w+:[\w\d\.-]*)|([a-z]{3,5})|(\w{2,4}\d{5})$`.

| external_xref   |   usages_count | usages                                                        |
|-----------------|----------------|---------------------------------------------------------------|
| `KEGG:05310`    |              1 | [MONDO:0004979](http://purl.obolibrary.org/obo/MONDO_0004979) |

## `MeSH`: Medical Subject Headings

Overall, there were 1 invalid
xrefs to external prefixed with `MeSH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref   |   usages_count | usages                                              |
|-----------------|----------------|-----------------------------------------------------|
| `MeSH:Q000401`  |              1 | [EFO:0004352](http://www.ebi.ac.uk/efo/EFO_0004352) |

## `MONDO`: Monarch Disease Ontology

Overall, there were 18 invalid
xrefs to external prefixed with `MONDO` (standardized to Bioregistry
prefix [`mondo`](https://bioregistry.io/mondo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                                         |   usages_count | usages                                                                                                                                                                                      |
|-------------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MONDO:patterns/infectious_disease_by_agent`          |              3 | [MONDO:0005108](http://purl.obolibrary.org/obo/MONDO_0005108), [MONDO:0100096](http://purl.obolibrary.org/obo/MONDO_0100096), [MONDO:0100096](http://purl.obolibrary.org/obo/MONDO_0100096) |
| `MONDO:patterns/specific_infectious_disease_by_agent` |              3 | [MONDO:0005091](http://purl.obolibrary.org/obo/MONDO_0005091), [MONDO:0005108](http://purl.obolibrary.org/obo/MONDO_0005108), [MONDO:0005812](http://purl.obolibrary.org/obo/MONDO_0005812) |
| `MONDO:ambiguous`                                     |              2 | [MONDO:0002280](http://purl.obolibrary.org/obo/MONDO_0002280), [MONDO:0005015](http://purl.obolibrary.org/obo/MONDO_0005015)                                                                |
| `MONDO:design_pattern`                                |              2 | [MONDO:0004995](http://purl.obolibrary.org/obo/MONDO_0004995), [EFO:0000684](http://www.ebi.ac.uk/efo/EFO_0000684)                                                                          |
| `MONDO:patterns/location`                             |              2 | [MONDO:0004995](http://purl.obolibrary.org/obo/MONDO_0004995), [EFO:0000684](http://www.ebi.ac.uk/efo/EFO_0000684)                                                                          |
| `MONDO:patterns/location_top`                         |              2 | [MONDO:0004995](http://purl.obolibrary.org/obo/MONDO_0004995), [EFO:0000684](http://www.ebi.ac.uk/efo/EFO_0000684)                                                                          |
| `MONDO:patterns/inflammatory_disease_by_site`         |              1 | [MONDO:0002258](http://purl.obolibrary.org/obo/MONDO_0002258)                                                                                                                               |
| `MONDO:cjm`                                           |              1 | [MONDO:0004995](http://purl.obolibrary.org/obo/MONDO_0004995)                                                                                                                               |
| `MONDO:patterns/chronic`                              |              1 | [MONDO:0005002](http://purl.obolibrary.org/obo/MONDO_0005002)                                                                                                                               |
| `MONDO:Lexical`                                       |              1 | [MONDO:0007186](http://purl.obolibrary.org/obo/MONDO_0007186)                                                                                                                               |

## `NCIT`: NCI Thesaurus

Overall, there were 6 invalid
xrefs to external prefixed with `NCIT` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                                         |
|-----------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `NCIT:P378`     |              6 | [MONDO:0005002](http://purl.obolibrary.org/obo/MONDO_0005002), [MONDO:0005015](http://purl.obolibrary.org/obo/MONDO_0005015), [MONDO:0005091](http://purl.obolibrary.org/obo/MONDO_0005091), [MONDO:0005108](http://purl.obolibrary.org/obo/MONDO_0005108), [MONDO:0005249](http://purl.obolibrary.org/obo/MONDO_0005249), ... |

## `NIF_Subcellular`: NIF Standard Ontology: Subcellular Entities

Overall, there were 4 invalid
xrefs to external prefixed with `NIF_Subcellular` (standardized to Bioregistry
prefix [`nlx.sub`](https://bioregistry.io/nlx.sub)) that
did not match the standard pattern `^\d+$`.

| external_xref                        |   usages_count | usages                                                                                                           |
|--------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `NIF_Subcellular:sao1337158144`      |              2 | [GO:0005575](http://purl.obolibrary.org/obo/GO_0005575), [GO:0005575](http://purl.obolibrary.org/obo/GO_0005575) |
| `NIF_Subcellular:nlx_subcell_100315` |              1 | [GO:0005575](http://purl.obolibrary.org/obo/GO_0005575)                                                          |
| `NIF_Subcellular:sao1820400233`      |              1 | [GO:0005730](http://purl.obolibrary.org/obo/GO_0005730)                                                          |

## `NIFSTD`: NIF Standard Ontology

Overall, there were 2 invalid
xrefs to external prefixed with `NIFSTD` (standardized to Bioregistry
prefix [`nif.std`](https://bioregistry.io/nif.std)) that
did not match the standard pattern `^BAMSC\d+$`.

| external_xref         |   usages_count | usages                                              |
|-----------------------|----------------|-----------------------------------------------------|
| `NIFSTD:birnlex_2110` |              1 | [EFO:0000264](http://www.ebi.ac.uk/efo/EFO_0000264) |
| `NIFSTD:birnlex_2087` |              1 | [EFO:0000651](http://www.ebi.ac.uk/efo/EFO_0000651) |

## `PRO`: Protein Ontology

Overall, there were 42 invalid
xrefs to external prefixed with `PRO` (standardized to Bioregistry
prefix [`pr`](https://bioregistry.io/pr)) that
did not match the standard pattern `^\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PRO:DAN`       |             22 | [PR:000000001](http://purl.obolibrary.org/obo/PR_000000001), [PR:000000001](http://purl.obolibrary.org/obo/PR_000000001), [PR:000050252](http://purl.obolibrary.org/obo/PR_000050252), [PR:000050252](http://purl.obolibrary.org/obo/PR_000050252), [PR:000050272](http://purl.obolibrary.org/obo/PR_000050272), ... |
| `PRO:DNx`       |             12 | [PR:000001341](http://purl.obolibrary.org/obo/PR_000001341), [PR:000001471](http://purl.obolibrary.org/obo/PR_000001471), [PR:000003137](http://purl.obolibrary.org/obo/PR_000003137), [PR:000018931](http://purl.obolibrary.org/obo/PR_000018931), [PR:000018931](http://purl.obolibrary.org/obo/PR_000018931), ... |
| `PRO:WCB`       |              4 | [PR:000000001](http://purl.obolibrary.org/obo/PR_000000001), [PR:000001341](http://purl.obolibrary.org/obo/PR_000001341), [PR:P12821](http://purl.obolibrary.org/obo/PR_P12821), [PR:Q9H2X3](http://purl.obolibrary.org/obo/PR_Q9H2X3)                                                                               |
| `PRO:JAN`       |              2 | [PR:000001471](http://purl.obolibrary.org/obo/PR_000001471), [PR:P22301](http://purl.obolibrary.org/obo/PR_P22301)                                                                                                                                                                                                   |
| `PRO:CNA`       |              1 | [PR:000003137](http://purl.obolibrary.org/obo/PR_000003137)                                                                                                                                                                                                                                                          |
| `PRO:YC`        |              1 | [PR:P0DTC9](http://purl.obolibrary.org/obo/PR_P0DTC9)                                                                                                                                                                                                                                                                |

## `ReO`: Reagent Ontology

Overall, there were 1 invalid
xrefs to external prefixed with `ReO` (standardized to Bioregistry
prefix [`reo`](https://bioregistry.io/reo)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                  |
|-----------------|----------------|---------------------------------------------------------|
| `ReO:mhb`       |              1 | [CL:0000010](http://purl.obolibrary.org/obo/CL_0000010) |

## `UMLS`: Unified Medical Language System Concept Unique Identifier

Overall, there were 2 invalid
xrefs to external prefixed with `UMLS` (standardized to Bioregistry
prefix [`umls`](https://bioregistry.io/umls)) that
did not match the standard pattern `^C\d+$`.

| external_xref                   |   usages_count | usages                                                        |
|---------------------------------|----------------|---------------------------------------------------------------|
| `UMLS:CN236658`                 |              1 | [MONDO:0002050](http://purl.obolibrary.org/obo/MONDO_0002050) |
| `UMLS:C0026565 | UMLS:C0026566` |              1 | [EFO:0004352](http://www.ebi.ac.uk/efo/EFO_0004352)           |

## `UniProtKB`: UniProt Protein

Overall, there were 2 invalid
xrefs to external prefixed with `UniProtKB` (standardized to Bioregistry
prefix [`uniprot`](https://bioregistry.io/uniprot)) that
did not match the standard pattern `^([A-N,R-Z][0-9]([A-Z][A-Z, 0-9][A-Z, 0-9][0-9]){1,2})|([O,P,Q][0-9][A-Z, 0-9][A-Z, 0-9][A-Z, 0-9][0-9])(\.\d+)?$`.

| external_xref        |   usages_count | usages                                                    |
|----------------------|----------------|-----------------------------------------------------------|
| `UniProtKB:P0DTC1-1` |              1 | [PR:P0DTC1-1](http://purl.obolibrary.org/obo/PR_P0DTC1-1) |
| `UniProtKB:P0DTD1-1` |              1 | [PR:P0DTD1-1](http://purl.obolibrary.org/obo/PR_P0DTD1-1) |

## `Wikipedia`: Wikipedia

Overall, there were 8 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                                              |   usages_count | usages                                                                                                                       |
|----------------------------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------|
| `Wikipedia:Vector_(epidemiology)`                                          |              2 | [MONDO:0100120](http://purl.obolibrary.org/obo/MONDO_0100120), [MONDO:0100120](http://purl.obolibrary.org/obo/MONDO_0100120) |
| `Wikipedia:Sulfonamide_(medicine)`                                         |              1 | [CHEBI:87228](http://purl.obolibrary.org/obo/CHEBI_87228)                                                                    |
| `Wikipedia:Neutralizing_antibody#Virus_evasion_of_neutralizing_antibodies` |              1 | [COVOC:0010007](http://purl.obolibrary.org/obo/COVOC_0010007)                                                                |
| `Wikipedia:Epitope#T_cell_epitopes`                                        |              1 | [COVOC:0010034](http://purl.obolibrary.org/obo/COVOC_0010034)                                                                |
| `Wikipedia:Cannabis_(drug)`                                                |              1 | [COVOC:0030019](http://purl.obolibrary.org/obo/COVOC_0030019)                                                                |
| `Wikipedia:Translation_(genetics)`                                         |              1 | [GO:0006412](http://purl.obolibrary.org/obo/GO_0006412)                                                                      |
| `Wikipedia:Autophagy_(cellular)`                                           |              1 | [GO:0006914](http://purl.obolibrary.org/obo/GO_0006914)                                                                      |

