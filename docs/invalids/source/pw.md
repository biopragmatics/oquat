# pw

This document details the invalid local unique identifiers used in CURIEs
for node, synonym, and definition cross-references in `pw`. See the [GitHub repository](https://github.com/rat-genome-database/PW-Pathway-Ontology).


## `BioCyc`: BioCyc collection of metabolic pathway databases

Overall, there were 12 invalid
xrefs to external prefixed with `BioCyc` (standardized to Bioregistry
prefix [`biocyc`](https://bioregistry.io/biocyc)) that
did not match the standard pattern `^[A-Z-0-9]+(\:)?[A-Za-z0-9+_.%-:]+$`.

| external_xref                                                                    |   usages_count | usages                                                                                                                                                                    |
|----------------------------------------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BioCyc:http://www.biocyc.org/META/NEW-IMAGE?type=PATHWAY&object=PWY-1861`       |              3 | [PW:0001376](http://purl.obolibrary.org/obo/PW_0001376), [PW:0001377](http://purl.obolibrary.org/obo/PW_0001377), [PW:0001378](http://purl.obolibrary.org/obo/PW_0001378) |
| `BioCyc:http://biocyc.org/META/NEW-IMAGE?type=PATHWAY&object=GLUTDEG-PWY`        |              2 | [PW:0001381](http://purl.obolibrary.org/obo/PW_0001381), [PW:0001382](http://purl.obolibrary.org/obo/PW_0001382)                                                          |
| `BioCyc:http://biocyc.org/META/NEW-IMAGE?type=PATHWAY&object=P221-PWY`           |              1 | [PW:0001379](http://purl.obolibrary.org/obo/PW_0001379)                                                                                                                   |
| `BioCyc:http://biocyc.org/META/NEW-IMAGE?type=PATHWAY&object=GLUTAMATE-DEG1-PWY` |              1 | [PW:0001380](http://purl.obolibrary.org/obo/PW_0001380)                                                                                                                   |
| `BioCyc:http://biocyc.org/META/NEW-IMAGE?type=PATHWAY&object=PWY-4321`           |              1 | [PW:0001383](http://purl.obolibrary.org/obo/PW_0001383)                                                                                                                   |
| `BioCyc:http://biocyc.org/META/NEW-IMAGE?type=PATHWAY&object=P162-PWY`           |              1 | [PW:0001384](http://purl.obolibrary.org/obo/PW_0001384)                                                                                                                   |
| `BioCyc:http://biocyc.org/META/NEW-IMAGE?type=PATHWAY&object=GLUDEG-II-PWY`      |              1 | [PW:0001386](http://purl.obolibrary.org/obo/PW_0001386)                                                                                                                   |
| `BioCyc:http://biocyc.org/META/NEW-IMAGE?type=PATHWAY&object=PWY-5087`           |              1 | [PW:0001387](http://purl.obolibrary.org/obo/PW_0001387)                                                                                                                   |
| `BioCyc:http://biocyc.org/META/NEW-IMAGE?type=PATHWAY&object=PWY-5088`           |              1 | [PW:0001388](http://purl.obolibrary.org/obo/PW_0001388)                                                                                                                   |

## `GO`: Gene Ontology

Overall, there were 4 invalid
xrefs to external prefixed with `GO` (standardized to Bioregistry
prefix [`go`](https://bioregistry.io/go)) that
did not match the standard pattern `^\d{7}$`.

| external_xref        |   usages_count | usages                                                  |
|----------------------|----------------|---------------------------------------------------------|
| `GO:006071`          |              1 | [PW:0000200](http://purl.obolibrary.org/obo/PW_0000200) |
| `GO:0070527, PubMed` |              1 | [PW:0000508](http://purl.obolibrary.org/obo/PW_0000508) |
| `GO:00005978`        |              1 | [PW:0000532](http://purl.obolibrary.org/obo/PW_0000532) |
| `GO:0016132, KEGG`   |              1 | [PW:0000552](http://purl.obolibrary.org/obo/PW_0000552) |

## `KEGG`: Kyoto Encyclopedia of Genes and Genomes

Overall, there were 27 invalid
xrefs to external prefixed with `KEGG` (standardized to Bioregistry
prefix [`kegg`](https://bioregistry.io/kegg)) that
did not match the standard pattern `^([CHDEGTMKR]\d+)|(\w+:[\w\d\.-]*)|([a-z]{3,5})|(\w{2,4}\d{5})$`.

| external_xref                                                 |   usages_count | usages                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `KEGG:http://www.genome.jp/kegg-bin/get_htext?br08303.keg`    |             10 | [PW:0000919](http://purl.obolibrary.org/obo/PW_0000919), [PW:0000920](http://purl.obolibrary.org/obo/PW_0000920), [PW:0000921](http://purl.obolibrary.org/obo/PW_0000921), [PW:0000922](http://purl.obolibrary.org/obo/PW_0000922), [PW:0000923](http://purl.obolibrary.org/obo/PW_0000923), ... |
| `KEGG:http://www.genome.jp/kegg/`                             |              3 | [PW:0000011](http://purl.obolibrary.org/obo/PW_0000011), [PW:0000754](http://purl.obolibrary.org/obo/PW_0000754), [PW:0001077](http://purl.obolibrary.org/obo/PW_0001077)                                                                                                                        |
| `KEGG:00620`                                                  |              1 | [PW:0000043](http://purl.obolibrary.org/obo/PW_0000043)                                                                                                                                                                                                                                          |
| `KEGG:http://www.genome.jp/kegg/pathway.html#xenobiotics`     |              1 | [PW:0000107](http://purl.obolibrary.org/obo/PW_0000107)                                                                                                                                                                                                                                          |
| `KEGG:map4910`                                                |              1 | [PW:0000143](http://purl.obolibrary.org/obo/PW_0000143)                                                                                                                                                                                                                                          |
| `KEGG:http://www.genome.ad.jp/kegg/pathway/map/map00040.html` |              1 | [PW:0000188](http://purl.obolibrary.org/obo/PW_0000188)                                                                                                                                                                                                                                          |
| `KEGG:http://umbbd.msi.umn.edu/ddt/ddt_map.html`              |              1 | [PW:0000519](http://purl.obolibrary.org/obo/PW_0000519)                                                                                                                                                                                                                                          |
| `KEGG:http://umbbd.msi.umn.edu/dcb/dcb_map.html`              |              1 | [PW:0000520](http://purl.obolibrary.org/obo/PW_0000520)                                                                                                                                                                                                                                          |
| `KEGG:http://umbbd.msi.umn.edu/dce/dce_map.html`              |              1 | [PW:0000521](http://purl.obolibrary.org/obo/PW_0000521)                                                                                                                                                                                                                                          |
| `KEGG:map5140`                                                |              1 | [PW:0001047](http://purl.obolibrary.org/obo/PW_0001047)                                                                                                                                                                                                                                          |
| `KEGG:map5142`                                                |              1 | [PW:0001048](http://purl.obolibrary.org/obo/PW_0001048)                                                                                                                                                                                                                                          |
| `KEGG:map5143`                                                |              1 | [PW:0001049](http://purl.obolibrary.org/obo/PW_0001049)                                                                                                                                                                                                                                          |
| `KEGG:map5146`                                                |              1 | [PW:0001053](http://purl.obolibrary.org/obo/PW_0001053)                                                                                                                                                                                                                                          |
| `KEGG:00232`                                                  |              1 | [PW:0001153](http://purl.obolibrary.org/obo/PW_0001153)                                                                                                                                                                                                                                          |
| `KEGG:00531`                                                  |              1 | [PW:0001154](http://purl.obolibrary.org/obo/PW_0001154)                                                                                                                                                                                                                                          |
| `KEGG:http://www.genome.jp/dbget-bin/www_bget?cpd:C09747`     |              1 | [PW:0001322](http://purl.obolibrary.org/obo/PW_0001322)                                                                                                                                                                                                                                          |

## `MeSH`: Medical Subject Headings

Overall, there were 10 invalid
xrefs to external prefixed with `MeSH` (standardized to Bioregistry
prefix [`mesh`](https://bioregistry.io/mesh)) that
did not match the standard pattern `^(C|D)\d{6,9}$`.

| external_xref                                                                                                     |   usages_count | usages                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `MeSH:http://www.nlm.nih.gov/cgi/mesh/2014/MB_cgi`                                                                |              3 | [PW:0000625](http://purl.obolibrary.org/obo/PW_0000625), [PW:0000700](http://purl.obolibrary.org/obo/PW_0000700), [PW:0000701](http://purl.obolibrary.org/obo/PW_0000701) |
| `MeSH:MeSH`                                                                                                       |              3 | [PW:0000627](http://purl.obolibrary.org/obo/PW_0000627), [PW:0000631](http://purl.obolibrary.org/obo/PW_0000631), [PW:0000633](http://purl.obolibrary.org/obo/PW_0000633) |
| `MeSH:Medical Subject Headings`                                                                                   |              2 | [PW:0000517](http://purl.obolibrary.org/obo/PW_0000517), [PW:0001476](http://purl.obolibrary.org/obo/PW_0001476)                                                          |
| `MeSH:MeSH descriptor`                                                                                            |              1 | [PW:0001414](http://purl.obolibrary.org/obo/PW_0001414)                                                                                                                   |
| `MeSH:http://www.nlm.nih.gov/cgi/mesh/2014/MB_cgi?mode=&term=Neoplasms,+Nerve+Tissue&field=entry#TreeC04.557.580` |              1 | [PW:0001550](http://purl.obolibrary.org/obo/PW_0001550)                                                                                                                   |

## `MetaCyc`: Metabolic Encyclopedia of metabolic and other pathways

Overall, there were 3 invalid
xrefs to external prefixed with `MetaCyc` (standardized to Bioregistry
prefix [`metacyc.compound`](https://bioregistry.io/metacyc.compound)) that
did not match the standard pattern `^[A-Za-z0-9+_.%-:]+$`.

| external_xref                                                              |   usages_count | usages                                                  |
|----------------------------------------------------------------------------|----------------|---------------------------------------------------------|
| `MetaCyc:http://www.biocyc.org/META/NEW-IMAGE?type=PATHWAY&object=AST-PWY` |              1 | [PW:0001261](http://purl.obolibrary.org/obo/PW_0001261) |
| `MetaCyc:http://biocyc.org/META/NEW-IMAGE?object=Lycopene-Biosynthesis`    |              1 | [PW:0001291](http://purl.obolibrary.org/obo/PW_0001291) |
| `MetaCyc:http://biocyc.org/META/NEW-IMAGE?object=METHIONINE-DEG`           |              1 | [PW:0001302](http://purl.obolibrary.org/obo/PW_0001302) |

## `NCI`: NCI Thesaurus

Overall, there were 4 invalid
xrefs to external prefixed with `NCI` (standardized to Bioregistry
prefix [`ncit`](https://bioregistry.io/ncit)) that
did not match the standard pattern `^C\d+$`.

| external_xref               |   usages_count | usages                                                                                                           |
|-----------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `NCI:NCI`                   |              2 | [PW:0001211](http://purl.obolibrary.org/obo/PW_0001211), [PW:0001212](http://purl.obolibrary.org/obo/PW_0001212) |
| `NCI:http://www.cancer.gov` |              1 | [PW:0001210](http://purl.obolibrary.org/obo/PW_0001210)                                                          |
| `NCI:www.cancer.gov`        |              1 | [PW:0001217](http://purl.obolibrary.org/obo/PW_0001217)                                                          |

## `OMIM`: Online Mendelian Inheritance in Man

Overall, there were 4 invalid
xrefs to external prefixed with `OMIM` (standardized to Bioregistry
prefix [`omim`](https://bioregistry.io/omim)) that
did not match the standard pattern `^\d+$`.

| external_xref                            |   usages_count | usages                                                                                                                                                                    |
|------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `OMIM:OMIM`                              |              3 | [PW:0000625](http://purl.obolibrary.org/obo/PW_0000625), [PW:0000627](http://purl.obolibrary.org/obo/PW_0000627), [PW:0000631](http://purl.obolibrary.org/obo/PW_0000631) |
| `OMIM:https://www.omim.org/entry/201710` |              1 | [PW:0001479](http://purl.obolibrary.org/obo/PW_0001479)                                                                                                                   |

## `PMID`: PubMed

Overall, there were 3 invalid
xrefs to external prefixed with `PMID` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref    |   usages_count | usages                                                  |
|------------------|----------------|---------------------------------------------------------|
| `PMID:9212076;`  |              1 | [PW:0000414](http://purl.obolibrary.org/obo/PW_0000414) |
| `PMID:1 7976918` |              1 | [PW:0001062](http://purl.obolibrary.org/obo/PW_0001062) |
| `PMID:22594892:` |              1 | [PW:0001121](http://purl.obolibrary.org/obo/PW_0001121) |

## `PubChem`: PubChem CID

Overall, there were 3 invalid
xrefs to external prefixed with `PubChem` (standardized to Bioregistry
prefix [`pubchem.compound`](https://bioregistry.io/pubchem.compound)) that
did not match the standard pattern `^\d+$`.

| external_xref                                                          |   usages_count | usages                                                                                                                                                                    |
|------------------------------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PubChem:https://pubchem.ncbi.nlm.nih.gov/compound/hydroflumethiazide` |              3 | [PW:0002377](http://purl.obolibrary.org/obo/PW_0002377), [PW:0002378](http://purl.obolibrary.org/obo/PW_0002378), [PW:0002379](http://purl.obolibrary.org/obo/PW_0002379) |

## `PubMed`: PubMed

Overall, there were 16 invalid
xrefs to external prefixed with `PubMed` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                                                                 |   usages_count | usages                                                                                                           |
|-------------------------------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `PubMed:2003, v. 285, f1-f8.`                                                 |              2 | [PW:0000182](http://purl.obolibrary.org/obo/PW_0000182), [PW:0000183](http://purl.obolibrary.org/obo/PW_0000183) |
| `PubMed:http://www.ncbi.nlm.nih.gov/sites/entrez`                             |              2 | [PW:0000573](http://purl.obolibrary.org/obo/PW_0000573), [PW:0000574](http://purl.obolibrary.org/obo/PW_0000574) |
| `PubMed:2001, v.27, 171-179.`                                                 |              1 | [PW:0000144](http://purl.obolibrary.org/obo/PW_0000144)                                                          |
| `PubMed:Neuron, 2004, v42, p897-912; Cellular Signaling, 2004, v16, p127-36.` |              1 | [PW:0000169](http://purl.obolibrary.org/obo/PW_0000169)                                                          |
| `PubMed:2004, v. 17, 38047`                                                   |              1 | [PW:0000174](http://purl.obolibrary.org/obo/PW_0000174)                                                          |
| `PubMed:2004, v.17, 38-47.`                                                   |              1 | [PW:0000175](http://purl.obolibrary.org/obo/PW_0000175)                                                          |
| `PubMed:2004, v.29(1), 32-38.`                                                |              1 | [PW:0000179](http://purl.obolibrary.org/obo/PW_0000179)                                                          |
| `PubMed:TIBS, 2004, v. 29(1), 32-38.`                                         |              1 | [PW:0000180](http://purl.obolibrary.org/obo/PW_0000180)                                                          |
| `PubMed:Several articles in PubMed`                                           |              1 | [PW:0000204](http://purl.obolibrary.org/obo/PW_0000204)                                                          |
| `PubMed:TIBS, 2004, v29 (5), p265-273`                                        |              1 | [PW:0000206](http://purl.obolibrary.org/obo/PW_0000206)                                                          |
| `PubMed:Science, 2002, v296, p1564-7`                                         |              1 | [PW:0000210](http://purl.obolibrary.org/obo/PW_0000210)                                                          |
| `PubMed:Nature Reviews, Mol. Cell Biology, 2001, v2, p369-77.`                |              1 | [PW:0000231](http://purl.obolibrary.org/obo/PW_0000231)                                                          |
| `PubMed:Annu. Rev. Neursci. 2003, v26, 701-28.`                               |              1 | [PW:0000274](http://purl.obolibrary.org/obo/PW_0000274)                                                          |
| `PubMed:Several articles`                                                     |              1 | [PW:0000668](http://purl.obolibrary.org/obo/PW_0000668)                                                          |

## `Pubmed`: PubMed

Overall, there were 1 invalid
xrefs to external prefixed with `Pubmed` (standardized to Bioregistry
prefix [`pubmed`](https://bioregistry.io/pubmed)) that
did not match the standard pattern `^\d+$`.

| external_xref                         |   usages_count | usages                                                  |
|---------------------------------------|----------------|---------------------------------------------------------|
| `Pubmed:http://www.ncbi.nlm.nih.gov/` |              1 | [PW:0000575](http://purl.obolibrary.org/obo/PW_0000575) |

## `PW`: Pathway ontology

Overall, there were 8 invalid
xrefs to external prefixed with `PW` (standardized to Bioregistry
prefix [`pw`](https://bioregistry.io/pw)) that
did not match the standard pattern `^\d{7}$`.

| external_xref   |   usages_count | usages                                                                                                                                                                                                                                                                                      |
|-----------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PW:InHouse`    |              5 | [PW:0000287](http://purl.obolibrary.org/obo/PW_0000287), [PW:0000288](http://purl.obolibrary.org/obo/PW_0000288), [PW:0000292](http://purl.obolibrary.org/obo/PW_0000292), [PW:0000293](http://purl.obolibrary.org/obo/PW_0000293), [PW:0000300](http://purl.obolibrary.org/obo/PW_0000300) |
| `PW:Inhouse`    |              2 | [PW:0000289](http://purl.obolibrary.org/obo/PW_0000289), [PW:0000290](http://purl.obolibrary.org/obo/PW_0000290)                                                                                                                                                                            |
| `PW:InHouse3`   |              1 | [PW:0000298](http://purl.obolibrary.org/obo/PW_0000298)                                                                                                                                                                                                                                     |

## `Reactome`: Reactome

Overall, there were 67 invalid
xrefs to external prefixed with `Reactome` (standardized to Bioregistry
prefix [`reactome`](https://bioregistry.io/reactome)) that
did not match the standard pattern `^R-[A-Z]{3}-\d+(-\d+)?(\.\d+)?$`.

| external_xref               |   usages_count | usages                                                                                                                                                                                                                                                                                      |
|-----------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Reactome:www.reactome.org` |              5 | [PW:0000089](http://purl.obolibrary.org/obo/PW_0000089), [PW:0000090](http://purl.obolibrary.org/obo/PW_0000090), [PW:0000091](http://purl.obolibrary.org/obo/PW_0000091), [PW:0000092](http://purl.obolibrary.org/obo/PW_0000092), [PW:0000093](http://purl.obolibrary.org/obo/PW_0000093) |
| `Reactome:REACT_1538.1`     |              2 | [PW:0000094](http://purl.obolibrary.org/obo/PW_0000094), [PW:0000095](http://purl.obolibrary.org/obo/PW_0000095)                                                                                                                                                                            |
| `Reactome:REACT_634.5`      |              1 | [PW:0000007](http://purl.obolibrary.org/obo/PW_0000007)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1046.3`     |              1 | [PW:0000026](http://purl.obolibrary.org/obo/PW_0000026)                                                                                                                                                                                                                                     |
| `Reactome:REACT_2071.3`     |              1 | [PW:0000043](http://purl.obolibrary.org/obo/PW_0000043)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1859.1`     |              1 | [PW:0000045](http://purl.obolibrary.org/obo/PW_0000045)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1861.3`     |              1 | [PW:0000069](http://purl.obolibrary.org/obo/PW_0000069)                                                                                                                                                                                                                                     |
| `Reactome:REACT_152.3`      |              1 | [PW:0000086](http://purl.obolibrary.org/obo/PW_0000086)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1590.1`     |              1 | [PW:0000087](http://purl.obolibrary.org/obo/PW_0000087)                                                                                                                                                                                                                                     |
| `Reactome:REACT_899.3`      |              1 | [PW:0000089](http://purl.obolibrary.org/obo/PW_0000089)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1915.2`     |              1 | [PW:0000090](http://purl.obolibrary.org/obo/PW_0000090)                                                                                                                                                                                                                                     |
| `Reactome:REACT_2203.2`     |              1 | [PW:0000091](http://purl.obolibrary.org/obo/PW_0000091)                                                                                                                                                                                                                                     |
| `Reactome:REACT_910.1`      |              1 | [PW:0000092](http://purl.obolibrary.org/obo/PW_0000092)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1725.1`     |              1 | [PW:0000093](http://purl.obolibrary.org/obo/PW_0000093)                                                                                                                                                                                                                                     |
| `Reactome:REACT_828.2`      |              1 | [PW:0000096](http://purl.obolibrary.org/obo/PW_0000096)                                                                                                                                                                                                                                     |
| `Reactome:REACT_2137.2`     |              1 | [PW:0000097](http://purl.obolibrary.org/obo/PW_0000097)                                                                                                                                                                                                                                     |
| `Reactome:REACT_216.1`      |              1 | [PW:0000099](http://purl.obolibrary.org/obo/PW_0000099)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1482.4`     |              1 | [PW:0000102](http://purl.obolibrary.org/obo/PW_0000102)                                                                                                                                                                                                                                     |
| `Reactome:REACT_962.4`      |              1 | [PW:0000102](http://purl.obolibrary.org/obo/PW_0000102)                                                                                                                                                                                                                                     |
| `Reactome:REACT_964.1`      |              1 | [PW:0000104](http://purl.obolibrary.org/obo/PW_0000104)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1059.1`     |              1 | [PW:0000106](http://purl.obolibrary.org/obo/PW_0000106)                                                                                                                                                                                                                                     |
| `Reactome:REACT_14797.1`    |              1 | [PW:0000125](http://purl.obolibrary.org/obo/PW_0000125)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1309.1`     |              1 | [PW:0000126](http://purl.obolibrary.org/obo/PW_0000126)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1366.1`     |              1 | [PW:0000127](http://purl.obolibrary.org/obo/PW_0000127)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1371.1`     |              1 | [PW:0000128](http://purl.obolibrary.org/obo/PW_0000128)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1104.1`     |              1 | [PW:0000129](http://purl.obolibrary.org/obo/PW_0000129)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1826.2`     |              1 | [PW:0000130](http://purl.obolibrary.org/obo/PW_0000130)                                                                                                                                                                                                                                     |
| `Reactome:REACT_498.5`      |              1 | [PW:0000143](http://purl.obolibrary.org/obo/PW_0000143)                                                                                                                                                                                                                                     |
| `Reactome:REACT_11061.4`    |              1 | [PW:0000169](http://purl.obolibrary.org/obo/PW_0000169)                                                                                                                                                                                                                                     |
| `Reactome:REACT_9417.3`     |              1 | [PW:0000170](http://purl.obolibrary.org/obo/PW_0000170)                                                                                                                                                                                                                                     |
| `Reactome:REACT_15380.1`    |              1 | [PW:0000176](http://purl.obolibrary.org/obo/PW_0000176)                                                                                                                                                                                                                                     |
| `Reactome:REACT_6838.1`     |              1 | [PW:0000180](http://purl.obolibrary.org/obo/PW_0000180)                                                                                                                                                                                                                                     |
| `Reactome:REACT_12065.1`    |              1 | [PW:0000198](http://purl.obolibrary.org/obo/PW_0000198)                                                                                                                                                                                                                                     |
| `Reactome:REACT_11045.1`    |              1 | [PW:0000201](http://purl.obolibrary.org/obo/PW_0000201)                                                                                                                                                                                                                                     |
| `Reactome:REACT_299.2`      |              1 | [PW:0000204](http://purl.obolibrary.org/obo/PW_0000204)                                                                                                                                                                                                                                     |
| `Reactome:REACT_6844.5`     |              1 | [PW:0000206](http://purl.obolibrary.org/obo/PW_0000206)                                                                                                                                                                                                                                     |
| `Reactome:REACT_14820.1`    |              1 | [PW:0000211](http://purl.obolibrary.org/obo/PW_0000211)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1432.1`     |              1 | [PW:0000233](http://purl.obolibrary.org/obo/PW_0000233)                                                                                                                                                                                                                                     |
| `Reactome:REACT_12529.1`    |              1 | [PW:0000243](http://purl.obolibrary.org/obo/PW_0000243)                                                                                                                                                                                                                                     |
| `Reactome:REACT_13477.2`    |              1 | [PW:0000274](http://purl.obolibrary.org/obo/PW_0000274)                                                                                                                                                                                                                                     |
| `Reactome:REACT_13552.1`    |              1 | [PW:0000286](http://purl.obolibrary.org/obo/PW_0000286)                                                                                                                                                                                                                                     |
| `Reactome:REACT_16888.1`    |              1 | [PW:0000297](http://purl.obolibrary.org/obo/PW_0000297)                                                                                                                                                                                                                                     |
| `Reactome:REACT_85.1`       |              1 | [PW:0000303](http://purl.obolibrary.org/obo/PW_0000303)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1208.1`     |              1 | [PW:0000304](http://purl.obolibrary.org/obo/PW_0000304)                                                                                                                                                                                                                                     |
| `Reactome:REACT_9470.2`     |              1 | [PW:0000328](http://purl.obolibrary.org/obo/PW_0000328)                                                                                                                                                                                                                                     |
| `Reactome:REACT_12034.1`    |              1 | [PW:0000330](http://purl.obolibrary.org/obo/PW_0000330)                                                                                                                                                                                                                                     |
| `Reactome:REACT_6959.3`     |              1 | [PW:0000373](http://purl.obolibrary.org/obo/PW_0000373)                                                                                                                                                                                                                                     |
| `Reactome:REACT_13705.1`    |              1 | [PW:0000375](http://purl.obolibrary.org/obo/PW_0000375)                                                                                                                                                                                                                                     |
| `Reactome:REACT_897.2`      |              1 | [PW:0000384](http://purl.obolibrary.org/obo/PW_0000384)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1846.2`     |              1 | [PW:0000385](http://purl.obolibrary.org/obo/PW_0000385)                                                                                                                                                                                                                                     |
| `Reactome:REACT_813.2`      |              1 | [PW:0000404](http://purl.obolibrary.org/obo/PW_0000404)                                                                                                                                                                                                                                     |
| `Reactome:REACT_9405.2`     |              1 | [PW:0000454](http://purl.obolibrary.org/obo/PW_0000454)                                                                                                                                                                                                                                     |
| `Reactome:REACT_6823.1`     |              1 | [PW:0000482](http://purl.obolibrary.org/obo/PW_0000482)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1736.2`     |              1 | [PW:0000532](http://purl.obolibrary.org/obo/PW_0000532)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1008.1`     |              1 | [PW:0000534](http://purl.obolibrary.org/obo/PW_0000534)                                                                                                                                                                                                                                     |
| `Reactome:REACT_15530.1`    |              1 | [PW:0000543](http://purl.obolibrary.org/obo/PW_0000543)                                                                                                                                                                                                                                     |
| `Reactome:REACT_212.3`      |              1 | [PW:0000554](http://purl.obolibrary.org/obo/PW_0000554)                                                                                                                                                                                                                                     |
| `Reactome:REACT_12020.1`    |              1 | [PW:0000603](http://purl.obolibrary.org/obo/PW_0000603)                                                                                                                                                                                                                                     |
| `Reactome:REACT_18325.2`    |              1 | [PW:0000674](http://purl.obolibrary.org/obo/PW_0000674)                                                                                                                                                                                                                                     |
| `Reactome:REACT_900.1`      |              1 | [PW:0000681](http://purl.obolibrary.org/obo/PW_0000681)                                                                                                                                                                                                                                     |
| `Reactome:REACT_402.1`      |              1 | [PW:0000682](http://purl.obolibrary.org/obo/PW_0000682)                                                                                                                                                                                                                                     |
| `Reactome:REACT_1464.3`     |              1 | [PW:0000776](http://purl.obolibrary.org/obo/PW_0000776)                                                                                                                                                                                                                                     |

## `RGD`: Rat Genome Database

Overall, there were 4 invalid
xrefs to external prefixed with `RGD` (standardized to Bioregistry
prefix [`rgd`](https://bioregistry.io/rgd)) that
did not match the standard pattern `^\d{4,}$`.

| external_xref            |   usages_count | usages                                                                                                                                                                    |
|--------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `RGD:InHouse dictionary` |              3 | [PW:0000332](http://purl.obolibrary.org/obo/PW_0000332), [PW:0000646](http://purl.obolibrary.org/obo/PW_0000646), [PW:0000683](http://purl.obolibrary.org/obo/PW_0000683) |
| `RGD:InHouse`            |              1 | [PW:0000684](http://purl.obolibrary.org/obo/PW_0000684)                                                                                                                   |

## `SMPDB`: Small Molecule Pathway Database

Overall, there were 6 invalid
xrefs to external prefixed with `SMPDB` (standardized to Bioregistry
prefix [`smpdb`](https://bioregistry.io/smpdb)) that
did not match the standard pattern `^SMP\d+$`.

| external_xref                                             |   usages_count | usages                                                                                                           |
|-----------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| `SMPDB:http://pathman.smpdb.ca/pathways/SMP00448/pathway` |              2 | [PW:0000764](http://purl.obolibrary.org/obo/PW_0000764), [PW:0000766](http://purl.obolibrary.org/obo/PW_0000766) |
| `SMPDB:http://pathman.smpdb.ca/pathways/SMP00029/pathway` |              1 | [PW:0000133](http://purl.obolibrary.org/obo/PW_0000133)                                                          |
| `SMPDB:http://pathman.smpdb.ca/pathways/SMP00446/pathway` |              1 | [PW:0000759](http://purl.obolibrary.org/obo/PW_0000759)                                                          |
| `SMPDB:http://pathman.smpdb.ca/pathways/SMP00096/pathway` |              1 | [PW:0000762](http://purl.obolibrary.org/obo/PW_0000762)                                                          |
| `SMPDB:http://pathman.smpdb.ca/pathways/SMP00467/pathway` |              1 | [PW:0001300](http://purl.obolibrary.org/obo/PW_0001300)                                                          |

## `wikipedia`: Wikipedia

Overall, there were 3 invalid
xrefs to external prefixed with `wikipedia` (standardized to Bioregistry
prefix [`wikipedia.en`](https://bioregistry.io/wikipedia.en)) that
did not match the standard pattern `^\S+$`.

| external_xref                                                          |   usages_count | usages                                                  |
|------------------------------------------------------------------------|----------------|---------------------------------------------------------|
| `wikipedia:<new dbxrefhttps://en.wikipedia.org/wiki/Aminocaproic_acid` |              1 | [PW:0001653](http://purl.obolibrary.org/obo/PW_0001653) |
| `wikipedia:<new dbxrefhttps://en.wikipedia.org/wiki/Nitrendipine`      |              1 | [PW:0001903](http://purl.obolibrary.org/obo/PW_0001903) |
| `wikipedia:<new dbxrefhttps://en.wikipedia.org/wiki/Atenolol`          |              1 | [PW:0002232](http://purl.obolibrary.org/obo/PW_0002232) |

