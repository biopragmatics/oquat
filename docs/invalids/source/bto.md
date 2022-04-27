# bto

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `bto`. See the [GitHub repository](https://github.com/BRENDA-Enzymes/BTO).


## `Flybase`: FlyBase Gene

Overall, there were 1 invalid
xrefs to external prefixed with `Flybase` (standardized to Bioregistry
prefix [`flybase`](https://bioregistry.io/flybase)) that
did not match the standard pattern `^FB\w{2}\d{7}$`.

| external_xref                                                                                              |   usages_count | usages                                                    |
|------------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------|
| `Flybase:('Flybase', 'http://flybase.bio.indiana.edu/allied-data/lk/interactive-fly/lewheld/preface.htm')` |              1 | [BTO:0001464](http://purl.obolibrary.org/obo/BTO_0001464) |

## `ISSN`: International Standard Serial Number

Overall, there were 1 invalid
xrefs to external prefixed with `ISSN` (standardized to Bioregistry
prefix [`issn`](https://bioregistry.io/issn)) that
did not match the standard pattern `^\d{4}-\d{3}[\dX]$`.

| external_xref                                                                      |   usages_count | usages                                                    |
|------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------|
| `ISSN:('ISSN', '0302-766X_(printed_version)_ISSN_1432-0878_(electronic_version)')` |              1 | [BTO:0001198](http://purl.obolibrary.org/obo/BTO_0001198) |

## `MedlinePlus`: MedlinePlus Health Topics

Overall, there were 1 invalid
xrefs to external prefixed with `MedlinePlus` (standardized to Bioregistry
prefix [`medlineplus`](https://bioregistry.io/medlineplus)) that
did not match the standard pattern `^\d+$`.

| external_xref                                                                                                              |   usages_count | usages                                                    |
|----------------------------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------|
| `MedlinePlus:('MedlinePlus', 'A_service_of_the_U.S._National_Library_of_Medicine_From_the_National_Institutes_of_Health')` |              1 | [BTO:0005035](http://purl.obolibrary.org/obo/BTO_0005035) |

## `MGI`: Mouse Genome Informatics

Overall, there were 1 invalid
xrefs to external prefixed with `MGI` (standardized to Bioregistry
prefix [`mgi`](https://bioregistry.io/mgi)) that
did not match the standard pattern `^\d+$`.

| external_xref                                                         |   usages_count | usages                                                    |
|-----------------------------------------------------------------------|----------------|-----------------------------------------------------------|
| `MGI:('MGI', 'http://www.mousedb.net/searches/GO.cgi?id=GO:0060935')` |              1 | [BTO:0003093](http://purl.obolibrary.org/obo/BTO_0003093) |

## `NASC`: NASC code

Overall, there were 1 invalid
xrefs to external prefixed with `NASC` (standardized to Bioregistry
prefix [`nasc`](https://bioregistry.io/nasc)) that
did not match the standard pattern `^(\w+)?\d+$`.

| external_xref                                            |   usages_count | usages                                                    |
|----------------------------------------------------------|----------------|-----------------------------------------------------------|
| `NASC:('NASC', 'The_European_Arabidopsis_Stock_Centre')` |              1 | [BTO:0003086](http://purl.obolibrary.org/obo/BTO_0003086) |

## `Patent`: Google Patents

Overall, there were 2 invalid
xrefs to external prefixed with `Patent` (standardized to Bioregistry
prefix [`google.patent`](https://bioregistry.io/google.patent)) that
did not match the standard pattern `^[A-Z]{2}\d+([A-Z])?$`.

| external_xref                            |   usages_count | usages                                                                                                               |
|------------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------|
| `Patent:('Patent', 'CA_Patent_2469027')` |              2 | [BTO:0004841](http://purl.obolibrary.org/obo/BTO_0004841), [BTO:0004952](http://purl.obolibrary.org/obo/BTO_0004952) |

## `PMID`: PubMed

Overall, there were 7 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                 |   usages_count | usages                                                    |
|-------------------------------|----------------|-----------------------------------------------------------|
| `PMID:('PMID', '_17179233')`  |              1 | [BTO:0004783](http://purl.obolibrary.org/obo/BTO_0004783) |
| `PMID:('PMID', '_8635507')`   |              1 | [BTO:0005332](http://purl.obolibrary.org/obo/BTO_0005332) |
| `PMID:('PMID', '_21552385')`  |              1 | [BTO:0005353](http://purl.obolibrary.org/obo/BTO_0005353) |
| `PMID:('PMID', '_6178358')`   |              1 | [BTO:0005386](http://purl.obolibrary.org/obo/BTO_0005386) |
| `PMID:('PMID', ':8305734')`   |              1 | [BTO:0005634](http://purl.obolibrary.org/obo/BTO_0005634) |
| `PMID:('PMID', '  29991048')` |              1 | [BTO:0006394](http://purl.obolibrary.org/obo/BTO_0006394) |
| `PMID:('PMID', ' 9522462')`   |              1 | [BTO:0006473](http://purl.obolibrary.org/obo/BTO_0006473) |

## `WormBase`: WormBase database of nematode biology

Overall, there were 1 invalid
xrefs to external prefixed with `WormBase` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref                                       |   usages_count | usages                                                    |
|-----------------------------------------------------|----------------|-----------------------------------------------------------|
| `WormBase:('WormBase', 'http://www.wormbase.org/')` |              1 | [BTO:0003039](http://purl.obolibrary.org/obo/BTO_0003039) |

## `Wormbase`: WormBase database of nematode biology

Overall, there were 1 invalid
xrefs to external prefixed with `Wormbase` (standardized to Bioregistry
prefix [`wormbase`](https://bioregistry.io/wormbase)) that
did not match the standard pattern `^WB[A-Z][a-z]+\d+$`.

| external_xref                                                              |   usages_count | usages                                                    |
|----------------------------------------------------------------------------|----------------|-----------------------------------------------------------|
| `Wormbase:('Wormbase', 'https://wormbase.org//species/all/anatomy_term/')` |              1 | [BTO:0006342](http://purl.obolibrary.org/obo/BTO_0006342) |

