# foodon

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `foodon`. See the [GitHub repository](https://github.com/FoodOntology/foodon).


## `EC`: Enzyme Nomenclature

Overall, there were 5 invalid
xrefs to external prefixed with `EC` (standardized to Bioregistry
entry [`eccode`](https://bioregistry.io/eccode)) that
did not match the standard pattern `^\d{1,2}(\.\d{0,3}){0,3}$`.

| external_xref         |   usages_count | usages                                                    |
|-----------------------|----------------|-----------------------------------------------------------|
| `EC:No 216/2009 DCP`  |              1 | [FOODON:03411081](https://bioregistry.io/FOODON:03411081) |
| `EC:No 216/2009 MOL`  |              1 | [FOODON:03412112](https://bioregistry.io/FOODON:03412112) |
| `EC:No 1637/2001 ECH` |              1 | [FOODON:03412115](https://bioregistry.io/FOODON:03412115) |
| `EC:No 216/2009 SAS`  |              1 | [FOODON:03413856](https://bioregistry.io/FOODON:03413856) |
| `EC:No 216/2009 RAX`  |              1 | [FOODON:03413974](https://bioregistry.io/FOODON:03413974) |

## `EOL`: Environment Ontology for Livestock

Overall, there were 1 invalid
xrefs to external prefixed with `EOL` (standardized to Bioregistry
entry [`eol`](https://bioregistry.io/eol)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                               |   usages_count | usages                                                    |
|---------------------------------------------|----------------|-----------------------------------------------------------|
| `EOL:http://eol.org/pages/4757174/overview` |              1 | [FOODON:03414802](https://bioregistry.io/FOODON:03414802) |

## `Wikipedia`: Wikipedia

Overall, there were 3 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
entry [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                  |   usages_count | usages                                                    |
|--------------------------------|----------------|-----------------------------------------------------------|
| `Wikipedia:Wort_%28brewing%29` |              1 | [FOODON:00001019](https://bioregistry.io/FOODON:00001019) |
| `Wikipedia:Malt_vinegar#Malt`  |              1 | [FOODON:00001074](https://bioregistry.io/FOODON:00001074) |
| `Wikipedia:Egg_%28food%29`     |              1 | [FOODON:00001274](https://bioregistry.io/FOODON:00001274) |

