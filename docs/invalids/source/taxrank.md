# taxrank

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `taxrank`. See the [GitHub repository](https://github.com/phenoscape/taxrank).


## `NCBITaxon`: NCBI organismal classification

Overall, there were 28 invalid
xrefs to external prefixed with `NCBITaxon` (standardized to Bioregistry
prefix [`ncbitaxon`](https://bioregistry.io/ncbitaxon)) that
did not match the standard pattern `^\d+$`.

| external_xref                |   usages_count | usages                                                            |
|------------------------------|----------------|-------------------------------------------------------------------|
| `NCBITaxon:phylum`           |              1 | [TAXRANK:0000001](http://purl.obolibrary.org/obo/TAXRANK_0000001) |
| `NCBITaxon:class`            |              1 | [TAXRANK:0000002](http://purl.obolibrary.org/obo/TAXRANK_0000002) |
| `NCBITaxon:order`            |              1 | [TAXRANK:0000003](http://purl.obolibrary.org/obo/TAXRANK_0000003) |
| `NCBITaxon:family`           |              1 | [TAXRANK:0000004](http://purl.obolibrary.org/obo/TAXRANK_0000004) |
| `NCBITaxon:genus`            |              1 | [TAXRANK:0000005](http://purl.obolibrary.org/obo/TAXRANK_0000005) |
| `NCBITaxon:species`          |              1 | [TAXRANK:0000006](http://purl.obolibrary.org/obo/TAXRANK_0000006) |
| `NCBITaxon:subclass`         |              1 | [TAXRANK:0000007](http://purl.obolibrary.org/obo/TAXRANK_0000007) |
| `NCBITaxon:subphylum`        |              1 | [TAXRANK:0000008](http://purl.obolibrary.org/obo/TAXRANK_0000008) |
| `NCBITaxon:subgenus`         |              1 | [TAXRANK:0000009](http://purl.obolibrary.org/obo/TAXRANK_0000009) |
| `NCBITaxon:species_group`    |              1 | [TAXRANK:0000010](http://purl.obolibrary.org/obo/TAXRANK_0000010) |
| `NCBITaxon:species_subgroup` |              1 | [TAXRANK:0000011](http://purl.obolibrary.org/obo/TAXRANK_0000011) |
| `NCBITaxon:infraorder`       |              1 | [TAXRANK:0000013](http://purl.obolibrary.org/obo/TAXRANK_0000013) |
| `NCBITaxon:suborder`         |              1 | [TAXRANK:0000014](http://purl.obolibrary.org/obo/TAXRANK_0000014) |
| `NCBITaxon:superclass`       |              1 | [TAXRANK:0000015](http://purl.obolibrary.org/obo/TAXRANK_0000015) |
| `NCBITaxon:varietas`         |              1 | [TAXRANK:0000016](http://purl.obolibrary.org/obo/TAXRANK_0000016) |
| `NCBITaxon:kingdom`          |              1 | [TAXRANK:0000017](http://purl.obolibrary.org/obo/TAXRANK_0000017) |
| `NCBITaxon:superfamily`      |              1 | [TAXRANK:0000018](http://purl.obolibrary.org/obo/TAXRANK_0000018) |
| `NCBITaxon:infraclass`       |              1 | [TAXRANK:0000019](http://purl.obolibrary.org/obo/TAXRANK_0000019) |
| `NCBITaxon:superorder`       |              1 | [TAXRANK:0000020](http://purl.obolibrary.org/obo/TAXRANK_0000020) |
| `NCBITaxon:parvorder`        |              1 | [TAXRANK:0000021](http://purl.obolibrary.org/obo/TAXRANK_0000021) |
| `NCBITaxon:superkingdom`     |              1 | [TAXRANK:0000022](http://purl.obolibrary.org/obo/TAXRANK_0000022) |
| `NCBITaxon:subspecies`       |              1 | [TAXRANK:0000023](http://purl.obolibrary.org/obo/TAXRANK_0000023) |
| `NCBITaxon:subfamily`        |              1 | [TAXRANK:0000024](http://purl.obolibrary.org/obo/TAXRANK_0000024) |
| `NCBITaxon:tribe`            |              1 | [TAXRANK:0000025](http://purl.obolibrary.org/obo/TAXRANK_0000025) |
| `NCBITaxon:forma`            |              1 | [TAXRANK:0000026](http://purl.obolibrary.org/obo/TAXRANK_0000026) |
| `NCBITaxon:superphylum`      |              1 | [TAXRANK:0000027](http://purl.obolibrary.org/obo/TAXRANK_0000027) |
| `NCBITaxon:subtribe`         |              1 | [TAXRANK:0000028](http://purl.obolibrary.org/obo/TAXRANK_0000028) |
| `NCBITaxon:subkingdom`       |              1 | [TAXRANK:0000029](http://purl.obolibrary.org/obo/TAXRANK_0000029) |

## `TAXRANK`: Taxonomic rank vocabulary

Overall, there were 2 invalid
xrefs to external prefixed with `TAXRANK` (standardized to Bioregistry
prefix [`taxrank`](https://bioregistry.io/taxrank)) that
did not match the standard pattern `^\d{7}$`.

| external_xref     |   usages_count | usages                                                                                                                               |
|-------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `TAXRANK:curator` |              2 | [TAXRANK:0000000](http://purl.obolibrary.org/obo/TAXRANK_0000000), [TAXRANK:0000060](http://purl.obolibrary.org/obo/TAXRANK_0000060) |

