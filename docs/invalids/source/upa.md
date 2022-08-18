# upa

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `upa`. See the [GitHub repository](https://github.com/geneontology/unipathway).


## `KEGG`: Kyoto Encyclopedia of Genes and Genomes

Overall, there were 1,008 invalid
xrefs to external prefixed with `KEGG` (standardized to Bioregistry
prefix [`kegg`](https://bioregistry.io/kegg)) that
did not match the standard pattern `^([CHDEGTMKR]\d+)|(\w+:[\w\d\.-]*)|([a-z]{3,5})|(\w{2,4}\d{5})$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `KEGG:COMPOUND` |           1008 | [UPa:UPC00001](http://purl.obolibrary.org/obo/UPa_UPC00001), [UPa:UPC00002](http://purl.obolibrary.org/obo/UPa_UPC00002), [UPa:UPC00003](http://purl.obolibrary.org/obo/UPa_UPC00003), [UPa:UPC00004](http://purl.obolibrary.org/obo/UPa_UPC00004), [UPa:UPC00005](http://purl.obolibrary.org/obo/UPa_UPC00005), ... |

## `PMID`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref            |   usages_count | usages                                                      |
|--------------------------|----------------|-------------------------------------------------------------|
| `PMID:SBN:0-13-144329-1` |              1 | [UPa:UPA00219](http://purl.obolibrary.org/obo/UPa_UPA00219) |

## `UPa`: Unipathway

Overall, there were 1,008 invalid
xrefs to external prefixed with `UPa` (standardized to Bioregistry
prefix [`upa`](https://bioregistry.io/upa)) that
did not match the standard pattern `^(UCR|UCY|UER|ULS|UPA|UPC|UPX)\d{5}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                                               |
|-----------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `UPa:`          |           1008 | [UPa:UPC00001](http://purl.obolibrary.org/obo/UPa_UPC00001), [UPa:UPC00002](http://purl.obolibrary.org/obo/UPa_UPC00002), [UPa:UPC00003](http://purl.obolibrary.org/obo/UPa_UPC00003), [UPa:UPC00004](http://purl.obolibrary.org/obo/UPa_UPC00004), [UPa:UPC00005](http://purl.obolibrary.org/obo/UPa_UPC00005), ... |

