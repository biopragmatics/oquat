# foodon

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `foodon`. See the [GitHub repository](https://github.com/FoodOntology/foodon).


## `EC`: Enzyme Nomenclature

Overall, there were 5 invalid
xrefs to external prefixed with `EC` (standardized to Bioregistry
prefix [`eccode`](https://bioregistry.io/eccode)) that
did not match the standard pattern `^\d{1,2}(\.\d{0,3}){0,3}$`.

| external_xref                   |   usages_count | usages                                                                                           |
|---------------------------------|----------------|--------------------------------------------------------------------------------------------------|
| `EC:('EC', 'No 216/2009 DCP')`  |              1 | [http://purl.obolibrary.org/obo/FOODON_03411081](http://purl.obolibrary.org/obo/FOODON_03411081) |
| `EC:('EC', 'No 216/2009 MOL')`  |              1 | [http://purl.obolibrary.org/obo/FOODON_03412112](http://purl.obolibrary.org/obo/FOODON_03412112) |
| `EC:('EC', 'No 1637/2001 ECH')` |              1 | [http://purl.obolibrary.org/obo/FOODON_03412115](http://purl.obolibrary.org/obo/FOODON_03412115) |
| `EC:('EC', 'No 216/2009 SAS')`  |              1 | [http://purl.obolibrary.org/obo/FOODON_03413856](http://purl.obolibrary.org/obo/FOODON_03413856) |
| `EC:('EC', 'No 216/2009 RAX')`  |              1 | [http://purl.obolibrary.org/obo/FOODON_03413974](http://purl.obolibrary.org/obo/FOODON_03413974) |

## `EOL`: Environment Ontology for Livestock

Overall, there were 1 invalid
xrefs to external prefixed with `EOL` (standardized to Bioregistry
prefix [`eol`](https://bioregistry.io/eol)) that
did not match the standard pattern `^\d{7}$`.

| external_xref                                          |   usages_count | usages                                                                                           |
|--------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------|
| `EOL:('EOL', 'http://eol.org/pages/4757174/overview')` |              1 | [http://purl.obolibrary.org/obo/FOODON_03414802](http://purl.obolibrary.org/obo/FOODON_03414802) |

## `Wikipedia`: Wikipedia

Overall, there were 3 invalid
xrefs to external prefixed with `Wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^[A-Za-z-0-9_]+$`.

| external_xref                                   |   usages_count | usages                                                                                           |
|-------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------|
| `Wikipedia:('Wikipedia', 'Wort_%28brewing%29')` |              1 | [http://purl.obolibrary.org/obo/FOODON_00001019](http://purl.obolibrary.org/obo/FOODON_00001019) |
| `Wikipedia:('Wikipedia', 'Malt_vinegar#Malt')`  |              1 | [http://purl.obolibrary.org/obo/FOODON_00001074](http://purl.obolibrary.org/obo/FOODON_00001074) |
| `Wikipedia:('Wikipedia', 'Egg_%28food%29')`     |              1 | [http://purl.obolibrary.org/obo/FOODON_00001274](http://purl.obolibrary.org/obo/FOODON_00001274) |

