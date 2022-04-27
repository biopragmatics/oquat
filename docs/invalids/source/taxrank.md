# taxrank

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `taxrank`. See the [GitHub repository](https://github.com/phenoscape/taxrank).


## `NCBITaxon`: NCBI organismal classification

Overall, there were 28 invalid
xrefs to external prefixed with `NCBITaxon` (standardized to Bioregistry
prefix [`ncbitaxon`](https://bioregistry.io/ncbitaxon)) that
did not match the standard pattern `^\d+$`.

| external_xref                                 |   usages_count | usages                                                                                           |
|-----------------------------------------------|----------------|--------------------------------------------------------------------------------------------------|
| `NCBITaxon:('NCBITaxon', 'phylum')`           |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000001](http://purl.obolibrary.org/obo/TAXRANK_0000001) |
| `NCBITaxon:('NCBITaxon', 'class')`            |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000002](http://purl.obolibrary.org/obo/TAXRANK_0000002) |
| `NCBITaxon:('NCBITaxon', 'order')`            |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000003](http://purl.obolibrary.org/obo/TAXRANK_0000003) |
| `NCBITaxon:('NCBITaxon', 'family')`           |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000004](http://purl.obolibrary.org/obo/TAXRANK_0000004) |
| `NCBITaxon:('NCBITaxon', 'genus')`            |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000005](http://purl.obolibrary.org/obo/TAXRANK_0000005) |
| `NCBITaxon:('NCBITaxon', 'species')`          |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000006](http://purl.obolibrary.org/obo/TAXRANK_0000006) |
| `NCBITaxon:('NCBITaxon', 'subclass')`         |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000007](http://purl.obolibrary.org/obo/TAXRANK_0000007) |
| `NCBITaxon:('NCBITaxon', 'subphylum')`        |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000008](http://purl.obolibrary.org/obo/TAXRANK_0000008) |
| `NCBITaxon:('NCBITaxon', 'subgenus')`         |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000009](http://purl.obolibrary.org/obo/TAXRANK_0000009) |
| `NCBITaxon:('NCBITaxon', 'species_group')`    |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000010](http://purl.obolibrary.org/obo/TAXRANK_0000010) |
| `NCBITaxon:('NCBITaxon', 'species_subgroup')` |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000011](http://purl.obolibrary.org/obo/TAXRANK_0000011) |
| `NCBITaxon:('NCBITaxon', 'infraorder')`       |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000013](http://purl.obolibrary.org/obo/TAXRANK_0000013) |
| `NCBITaxon:('NCBITaxon', 'suborder')`         |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000014](http://purl.obolibrary.org/obo/TAXRANK_0000014) |
| `NCBITaxon:('NCBITaxon', 'superclass')`       |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000015](http://purl.obolibrary.org/obo/TAXRANK_0000015) |
| `NCBITaxon:('NCBITaxon', 'varietas')`         |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000016](http://purl.obolibrary.org/obo/TAXRANK_0000016) |
| `NCBITaxon:('NCBITaxon', 'kingdom')`          |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000017](http://purl.obolibrary.org/obo/TAXRANK_0000017) |
| `NCBITaxon:('NCBITaxon', 'superfamily')`      |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000018](http://purl.obolibrary.org/obo/TAXRANK_0000018) |
| `NCBITaxon:('NCBITaxon', 'infraclass')`       |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000019](http://purl.obolibrary.org/obo/TAXRANK_0000019) |
| `NCBITaxon:('NCBITaxon', 'superorder')`       |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000020](http://purl.obolibrary.org/obo/TAXRANK_0000020) |
| `NCBITaxon:('NCBITaxon', 'parvorder')`        |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000021](http://purl.obolibrary.org/obo/TAXRANK_0000021) |
| `NCBITaxon:('NCBITaxon', 'superkingdom')`     |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000022](http://purl.obolibrary.org/obo/TAXRANK_0000022) |
| `NCBITaxon:('NCBITaxon', 'subspecies')`       |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000023](http://purl.obolibrary.org/obo/TAXRANK_0000023) |
| `NCBITaxon:('NCBITaxon', 'subfamily')`        |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000024](http://purl.obolibrary.org/obo/TAXRANK_0000024) |
| `NCBITaxon:('NCBITaxon', 'tribe')`            |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000025](http://purl.obolibrary.org/obo/TAXRANK_0000025) |
| `NCBITaxon:('NCBITaxon', 'forma')`            |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000026](http://purl.obolibrary.org/obo/TAXRANK_0000026) |
| `NCBITaxon:('NCBITaxon', 'superphylum')`      |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000027](http://purl.obolibrary.org/obo/TAXRANK_0000027) |
| `NCBITaxon:('NCBITaxon', 'subtribe')`         |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000028](http://purl.obolibrary.org/obo/TAXRANK_0000028) |
| `NCBITaxon:('NCBITaxon', 'subkingdom')`       |              1 | [http://purl.obolibrary.org/obo/TAXRANK_0000029](http://purl.obolibrary.org/obo/TAXRANK_0000029) |

## `TAXRANK`: Taxonomic rank vocabulary

Overall, there were 2 invalid
xrefs to external prefixed with `TAXRANK` (standardized to Bioregistry
prefix [`taxrank`](https://bioregistry.io/taxrank)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                    |   usages_count | usages                                                                                                                                                                                             |
|----------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TAXRANK:('TAXRANK', 'curator')` |              2 | [http://purl.obolibrary.org/obo/TAXRANK_0000000](http://purl.obolibrary.org/obo/TAXRANK_0000000), [http://purl.obolibrary.org/obo/TAXRANK_0000060](http://purl.obolibrary.org/obo/TAXRANK_0000060) |

