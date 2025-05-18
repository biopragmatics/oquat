# Ontology Quality Assessment Toolkit

This website shows various large-scale analyses of ontology quality across the
OBO Foundry ontologies and others in the Bioregistry.

- Analysis on [unknown prefixes](unknowns/)
- Analysis on [invalid local unique identifiers](invalids/)
- Analysis on [versions](versions/)
- List of failures during parsing [here](failures.md)


```shell
$ docker run --rm --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:4.2.0 jekyll serve
```
