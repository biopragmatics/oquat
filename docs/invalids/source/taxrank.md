# taxrank

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `taxrank`. See the [GitHub repository](https://github.com/phenoscape/taxrank).


## `NCBITaxon`: NCBI organismal classification

Overall, there were 28 invalid
xrefs to external prefixed with `NCBITaxon` (standardized to Bioregistry
prefix [`ncbitaxon`](https://bioregistry.io/ncbitaxon)) that
did not match the standard pattern `^\d+$`.

| external_xref                                 |   usages_count | usages                                                    |
|-----------------------------------------------|----------------|-----------------------------------------------------------|
| `NCBITaxon:('NCBITaxon', 'phylum')`           |              1 | [TAXRANK:0000001](https://bioregistry.io/TAXRANK:0000001) |
| `NCBITaxon:('NCBITaxon', 'class')`            |              1 | [TAXRANK:0000002](https://bioregistry.io/TAXRANK:0000002) |
| `NCBITaxon:('NCBITaxon', 'order')`            |              1 | [TAXRANK:0000003](https://bioregistry.io/TAXRANK:0000003) |
| `NCBITaxon:('NCBITaxon', 'family')`           |              1 | [TAXRANK:0000004](https://bioregistry.io/TAXRANK:0000004) |
| `NCBITaxon:('NCBITaxon', 'genus')`            |              1 | [TAXRANK:0000005](https://bioregistry.io/TAXRANK:0000005) |
| `NCBITaxon:('NCBITaxon', 'species')`          |              1 | [TAXRANK:0000006](https://bioregistry.io/TAXRANK:0000006) |
| `NCBITaxon:('NCBITaxon', 'subclass')`         |              1 | [TAXRANK:0000007](https://bioregistry.io/TAXRANK:0000007) |
| `NCBITaxon:('NCBITaxon', 'subphylum')`        |              1 | [TAXRANK:0000008](https://bioregistry.io/TAXRANK:0000008) |
| `NCBITaxon:('NCBITaxon', 'subgenus')`         |              1 | [TAXRANK:0000009](https://bioregistry.io/TAXRANK:0000009) |
| `NCBITaxon:('NCBITaxon', 'species_group')`    |              1 | [TAXRANK:0000010](https://bioregistry.io/TAXRANK:0000010) |
| `NCBITaxon:('NCBITaxon', 'species_subgroup')` |              1 | [TAXRANK:0000011](https://bioregistry.io/TAXRANK:0000011) |
| `NCBITaxon:('NCBITaxon', 'infraorder')`       |              1 | [TAXRANK:0000013](https://bioregistry.io/TAXRANK:0000013) |
| `NCBITaxon:('NCBITaxon', 'suborder')`         |              1 | [TAXRANK:0000014](https://bioregistry.io/TAXRANK:0000014) |
| `NCBITaxon:('NCBITaxon', 'superclass')`       |              1 | [TAXRANK:0000015](https://bioregistry.io/TAXRANK:0000015) |
| `NCBITaxon:('NCBITaxon', 'varietas')`         |              1 | [TAXRANK:0000016](https://bioregistry.io/TAXRANK:0000016) |
| `NCBITaxon:('NCBITaxon', 'kingdom')`          |              1 | [TAXRANK:0000017](https://bioregistry.io/TAXRANK:0000017) |
| `NCBITaxon:('NCBITaxon', 'superfamily')`      |              1 | [TAXRANK:0000018](https://bioregistry.io/TAXRANK:0000018) |
| `NCBITaxon:('NCBITaxon', 'infraclass')`       |              1 | [TAXRANK:0000019](https://bioregistry.io/TAXRANK:0000019) |
| `NCBITaxon:('NCBITaxon', 'superorder')`       |              1 | [TAXRANK:0000020](https://bioregistry.io/TAXRANK:0000020) |
| `NCBITaxon:('NCBITaxon', 'parvorder')`        |              1 | [TAXRANK:0000021](https://bioregistry.io/TAXRANK:0000021) |
| `NCBITaxon:('NCBITaxon', 'superkingdom')`     |              1 | [TAXRANK:0000022](https://bioregistry.io/TAXRANK:0000022) |
| `NCBITaxon:('NCBITaxon', 'subspecies')`       |              1 | [TAXRANK:0000023](https://bioregistry.io/TAXRANK:0000023) |
| `NCBITaxon:('NCBITaxon', 'subfamily')`        |              1 | [TAXRANK:0000024](https://bioregistry.io/TAXRANK:0000024) |
| `NCBITaxon:('NCBITaxon', 'tribe')`            |              1 | [TAXRANK:0000025](https://bioregistry.io/TAXRANK:0000025) |
| `NCBITaxon:('NCBITaxon', 'forma')`            |              1 | [TAXRANK:0000026](https://bioregistry.io/TAXRANK:0000026) |
| `NCBITaxon:('NCBITaxon', 'superphylum')`      |              1 | [TAXRANK:0000027](https://bioregistry.io/TAXRANK:0000027) |
| `NCBITaxon:('NCBITaxon', 'subtribe')`         |              1 | [TAXRANK:0000028](https://bioregistry.io/TAXRANK:0000028) |
| `NCBITaxon:('NCBITaxon', 'subkingdom')`       |              1 | [TAXRANK:0000029](https://bioregistry.io/TAXRANK:0000029) |

## `TAXRANK`: Taxonomic rank vocabulary

Overall, there were 2 invalid
xrefs to external prefixed with `TAXRANK` (standardized to Bioregistry
prefix [`taxrank`](https://bioregistry.io/taxrank)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                    |   usages_count | usages                                                                                                               |
|----------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------|
| `TAXRANK:('TAXRANK', 'curator')` |              2 | [TAXRANK:0000000](https://bioregistry.io/TAXRANK:0000000), [TAXRANK:0000060](https://bioregistry.io/TAXRANK:0000060) |

