# Marts docs

{% docs dim_clientes_final %}
This dimension table combines client information with enriched company and geolocation data.

It is designed for use in client segmentation, demographic analysis, and location-based reporting.

Key features:

- Built from `int__cliente_empresa`
- Enriched with `latitude` and `longitude` from `int__empresa_geolocation`
- Includes client name, contact info, job role, and company metadata

Use cases:

- Analyzing client distribution by region
- Filtering clients by company attributes
- Mapping clients using geospatial tools
{% enddocs %}

{% docs empresa_pix_analysis %}
This mart filters companies that are authorized by the Central Bank of Brazil (BCB) to operate in the PIX system.

It provides a clean dataset of active, authorized companies with their PIX-related attributes for regulatory and institutional analysis.

Key features:

- Derived from `int__empresa_pix`
- Filters only `autorizada_bcb = 'Sim'`
- Useful for compliance, participation tracking, and fintech analysis

Includes:

- Joins between `stg__dim_empresa` and `stg__dim_pix`
- Attributes like `autorizada_bcb`, `tipo_participacao_pix`, and `status_producao`
- Optional geolocation for spatial analysis
{% enddocs %}

{% docs fato_contato_final %}
This fact table includes all enriched contact events with clients, along with a calculated metric for total contact count per client.

It supports funnel analysis, conversion metrics, and client engagement tracking.

Key features:

- Based on `int__fato_contato_enriched`
- Adds a window function for `total_contatos_cliente`
- Can be used to analyze frequency, stages, and channels of contact across clients

Use cases:

- Identify highly contacted clients
- Funnel drop-off by stage or region
- Sales rep performance analysis
{% enddocs %}
