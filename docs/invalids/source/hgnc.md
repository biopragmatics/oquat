# hgnc

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `hgnc`.


## `RefSeq`: Reference Sequence Collection

Overall, there were 2 invalid
xrefs to external prefixed with `RefSeq` (standardized to Bioregistry
prefix [`refseq`](https://bioregistry.io/refseq)) that
did not match the standard pattern `^(((AC|AP|NC|NG|NM|NP|NR|NT|NW|WP|XM|XP|XR|YP|ZP)_\d+)|(NZ_[A-Z]{2,4}\d+))(\.\d+)?$`.

| external_xref       |   usages_count | usages                                                                                                                                             |
|---------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `RefSeq:XR_016092.` |              1 | [https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37909) |
| `RefSeq:NM_021728.` |              1 | [https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8522)   |

