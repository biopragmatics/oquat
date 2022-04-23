# Invalid Xref Syntax Summary

{% for prefix, result in results %} {% if result.bad_values and not bioregistry.is_deprecated(prefix) %}

<details>
<summary>
{{ bioregistry.get_name(prefix) }}
(<a href="https://bioregistry.io/{{ prefix }}"><code>{{ prefix }}</code></a>; {{ result.bad_values | length }} issues)
</summary>

Improvements can be solicited through
the <a href="{{ bioregistry.get_repository(prefix) }}/issues">issue tracker</a>
on the GitHub repository {{ bioregistry.get_repository(prefix) }}. The
responsible person for this ontology is {{ bioregistry.get_contact_name(prefix) }}
(@{{ bioregistry.get_contact_github(prefix) }}).

{{ result._bad_values_table() }}

</details>

{% endif %} {% endfor %}
