# xco

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `xco`. See the [GitHub repository](https://github.com/rat-genome-database/XCO-experimental-condition-ontology).


## `CHEBI`: Chemical Entities of Biological Interest

Overall, there were 7 invalid
xrefs to external prefixed with `CHEBI` (standardized to Bioregistry
prefix [`chebi`](https://bioregistry.io/chebi)) that
did not match the standard pattern `^\d+$`.

| external_xref        |   usages_count | usages                                                    |
|----------------------|----------------|-----------------------------------------------------------|
| `CHEBI:CHEBI:2504`   |              1 | [XCO:0000605](http://purl.obolibrary.org/obo/XCO_0000605) |
| `CHEBI:CHEBI: 15366` |              1 | [XCO:0000607](http://purl.obolibrary.org/obo/XCO_0000607) |
| `CHEBI:CHEBI:73224`  |              1 | [XCO:0000608](http://purl.obolibrary.org/obo/XCO_0000608) |
| `CHEBI:CHEBI:17303`  |              1 | [XCO:0000610](http://purl.obolibrary.org/obo/XCO_0000610) |
| `CHEBI:CHEBI:35705`  |              1 | [XCO:0000636](http://purl.obolibrary.org/obo/XCO_0000636) |
| `CHEBI:CHEBI:4031`   |              1 | [XCO:0000637](http://purl.obolibrary.org/obo/XCO_0000637) |
| `CHEBI:CHEBI:70773`  |              1 | [XCO:0000638](http://purl.obolibrary.org/obo/XCO_0000638) |

## `CHEMBL`: ChEMBL

Overall, there were 4 invalid
xrefs to external prefixed with `CHEMBL` (standardized to Bioregistry
prefix [`chembl`](https://bioregistry.io/chembl)) that
did not match the standard pattern `^CHEMBL\d+$`.

| external_xref   |   usages_count | usages                                                                                                                                                                          |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CHEMBL:105608` |              3 | [XCO:0000320](http://purl.obolibrary.org/obo/XCO_0000320), [XCO:0000321](http://purl.obolibrary.org/obo/XCO_0000321), [XCO:0000322](http://purl.obolibrary.org/obo/XCO_0000322) |
| `CHEMBL:297362` |              1 | [XCO:0000131](http://purl.obolibrary.org/obo/XCO_0000131)                                                                                                                       |

## `DrugBank`: DrugBank

Overall, there were 5 invalid
xrefs to external prefixed with `DrugBank` (standardized to Bioregistry
prefix [`drugbank`](https://bioregistry.io/drugbank)) that
did not match the standard pattern `^DB\d{5}$`.

| external_xref                                    |   usages_count | usages                                                    |
|--------------------------------------------------|----------------|-----------------------------------------------------------|
| `DrugBank:https://www.drugbank.ca/drugs/DB00997` |              1 | [XCO:0000539](http://purl.obolibrary.org/obo/XCO_0000539) |
| `DrugBank:https://www.drugbank.ca/drugs/DB00178` |              1 | [XCO:0000548](http://purl.obolibrary.org/obo/XCO_0000548) |
| `DrugBank:https://www.drugbank.ca/drugs/DB00206` |              1 | [XCO:0000550](http://purl.obolibrary.org/obo/XCO_0000550) |
| `DrugBank:https://www.drugbank.ca/drugs/DB01275` |              1 | [XCO:0000551](http://purl.obolibrary.org/obo/XCO_0000551) |
| `DrugBank:https://www.drugbank.ca/drugs/DB00999` |              1 | [XCO:0000552](http://purl.obolibrary.org/obo/XCO_0000552) |

## `Drugbank`: DrugBank

Overall, there were 5 invalid
xrefs to external prefixed with `Drugbank` (standardized to Bioregistry
prefix [`drugbank`](https://bioregistry.io/drugbank)) that
did not match the standard pattern `^DB\d{5}$`.

| external_xref                                             |   usages_count | usages                                                    |
|-----------------------------------------------------------|----------------|-----------------------------------------------------------|
| `Drugbank:https://www.drugbank.ca/drugs/DB01296`          |              1 | [XCO:0000557](http://purl.obolibrary.org/obo/XCO_0000557) |
| `Drugbank:https://www.drugbank.ca/drugs/DB00790`          |              1 | [XCO:0000588](http://purl.obolibrary.org/obo/XCO_0000588) |
| `Drugbank:https://www.drugbank.ca/drugs/DB01094`          |              1 | [XCO:0000603](http://purl.obolibrary.org/obo/XCO_0000603) |
| `Drugbank:https://www.drugbank.ca/drugs/DB06692`          |              1 | [XCO:0000604](http://purl.obolibrary.org/obo/XCO_0000604) |
| `Drugbank:https://www.drugbank.ca/categories/DBCAT000600` |              1 | [XCO:0000618](http://purl.obolibrary.org/obo/XCO_0000618) |

## `DRUGBANK`: DrugBank

Overall, there were 2 invalid
xrefs to external prefixed with `DRUGBANK` (standardized to Bioregistry
prefix [`drugbank`](https://bioregistry.io/drugbank)) that
did not match the standard pattern `^DB\d{5}$`.

| external_xref                                    |   usages_count | usages                                                    |
|--------------------------------------------------|----------------|-----------------------------------------------------------|
| `DRUGBANK:https://www.drugbank.ca/drugs/DB00421` |              1 | [XCO:0000627](http://purl.obolibrary.org/obo/XCO_0000627) |
| `DRUGBANK:https://www.drugbank.ca/drugs/DB00572` |              1 | [XCO:0000631](http://purl.obolibrary.org/obo/XCO_0000631) |

## `drugbank`: DrugBank

Overall, there were 1 invalid
xrefs to external prefixed with `drugbank` (standardized to Bioregistry
prefix [`drugbank`](https://bioregistry.io/drugbank)) that
did not match the standard pattern `^DB\d{5}$`.

| external_xref                                    |   usages_count | usages                                                    |
|--------------------------------------------------|----------------|-----------------------------------------------------------|
| `drugbank:https://www.drugbank.ca/drugs/DB04883` |              1 | [XCO:0000647](http://purl.obolibrary.org/obo/XCO_0000647) |

## `Medline Plus`: MedlinePlus Health Topics

Overall, there were 1 invalid
xrefs to external prefixed with `Medline Plus` (standardized to Bioregistry
prefix [`medlineplus`](https://bioregistry.io/medlineplus)) that
did not match the standard pattern `^\d+$`.

| external_xref                                       |   usages_count | usages                                                    |
|-----------------------------------------------------|----------------|-----------------------------------------------------------|
| `Medline Plus:http\://www.nlm.nih.gov/medlineplus/` |              1 | [XCO:0000563](http://purl.obolibrary.org/obo/XCO_0000563) |

## `MESH`: Medical Subject Headings

Overall, there were 6 invalid
xrefs to external prefixed with `MESH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                                                                                           |   usages_count | usages                                                    |
|---------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------|
| `MESH:https://meshb.nlm.nih.gov/record/ui?ui=D008550`                                                   |              1 | [XCO:0000559](http://purl.obolibrary.org/obo/XCO_0000559) |
| `MESH:https://meshb.nlm.nih.gov/record/ui?ui=D009543`                                                   |              1 | [XCO:0000611](http://purl.obolibrary.org/obo/XCO_0000611) |
| `MESH:https://www.ncbi.nlm.nih.gov/mesh/68020889`                                                       |              1 | [XCO:0000614](http://purl.obolibrary.org/obo/XCO_0000614) |
| `MESH:https://www.ncbi.nlm.nih.gov/mesh?Db=mesh&Cmd=DetailsSearch&Term=%22Verapamil%22%5BMeSH+Terms%5D` |              1 | [XCO:0000616](http://purl.obolibrary.org/obo/XCO_0000616) |
| `MESH:https://www.ncbi.nlm.nih.gov/mesh/68011802`                                                       |              1 | [XCO:0000617](http://purl.obolibrary.org/obo/XCO_0000617) |
| `MESH:https://www.ncbi.nlm.nih.gov/mesh/68016686`                                                       |              1 | [XCO:0000642](http://purl.obolibrary.org/obo/XCO_0000642) |

## `NCI Thesaurus`: NCI Thesaurus

Overall, there were 1 invalid
xrefs to external prefixed with `NCI Thesaurus` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref                                                                                                           |   usages_count | usages                                                    |
|-------------------------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------|
| `NCI Thesaurus:https://ncit-stage.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&code=C930&ns=ncit` |              1 | [XCO:0000620](http://purl.obolibrary.org/obo/XCO_0000620) |

## `PMID`: PubMed

Overall, there were 4 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref        |   usages_count | usages                                                    |
|----------------------|----------------|-----------------------------------------------------------|
| `PMID:PMID:25312437` |              1 | [XCO:0000587](http://purl.obolibrary.org/obo/XCO_0000587) |
| `PMID:PMID: 7609754` |              1 | [XCO:0000612](http://purl.obolibrary.org/obo/XCO_0000612) |
| `PMID:PMID:15894899` |              1 | [XCO:0000635](http://purl.obolibrary.org/obo/XCO_0000635) |
| `PMID:PMID:27671317` |              1 | [XCO:0000639](http://purl.obolibrary.org/obo/XCO_0000639) |

## `PubChem_Compound`: PubChem CID

Overall, there were 5 invalid
xrefs to external prefixed with `PubChem_Compound` (standardized to Bioregistry
prefix [`pubchem.compound`](https://bioregistry.io/pubchem.compound)) that
did not match the standard pattern `^\d+$`.

| external_xref                |   usages_count | usages                                                                                                                                                                          |
|------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PubChem_Compound:CID_13157` |              3 | [XCO:0000344](http://purl.obolibrary.org/obo/XCO_0000344), [XCO:0000436](http://purl.obolibrary.org/obo/XCO_0000436), [XCO:0000437](http://purl.obolibrary.org/obo/XCO_0000437) |
| `PubChem_Compound:CID_12967` |              2 | [XCO:0000345](http://purl.obolibrary.org/obo/XCO_0000345), [XCO:0000346](http://purl.obolibrary.org/obo/XCO_0000346)                                                            |

## `RGD`: Rat Genome Database

Overall, there were 44 invalid
xrefs to external prefixed with `RGD` (standardized to Bioregistry
prefix [`rgd`](https://bioregistry.io/rgd)) that
did not match the standard pattern `^\d{4,}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                     |
|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RGD:MS`        |             27 | [XCO:0000009](http://purl.obolibrary.org/obo/XCO_0000009), [XCO:0000010](http://purl.obolibrary.org/obo/XCO_0000010), [XCO:0000012](http://purl.obolibrary.org/obo/XCO_0000012), [XCO:0000014](http://purl.obolibrary.org/obo/XCO_0000014), [XCO:0000015](http://purl.obolibrary.org/obo/XCO_0000015), ... |
| `RGD:JRS`       |             15 | [XCO:0000120](http://purl.obolibrary.org/obo/XCO_0000120), [XCO:0000133](http://purl.obolibrary.org/obo/XCO_0000133), [XCO:0000152](http://purl.obolibrary.org/obo/XCO_0000152), [XCO:0000153](http://purl.obolibrary.org/obo/XCO_0000153), [XCO:0000158](http://purl.obolibrary.org/obo/XCO_0000158), ... |
| `RGD:SL`        |              1 | [XCO:0000138](http://purl.obolibrary.org/obo/XCO_0000138)                                                                                                                                                                                                                                                  |
| `RGD:MRD`       |              1 | [XCO:0000166](http://purl.obolibrary.org/obo/XCO_0000166)                                                                                                                                                                                                                                                  |

