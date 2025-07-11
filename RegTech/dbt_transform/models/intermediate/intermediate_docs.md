# Intermediate docs

{% docs int__cliente_empresa %}
This model joins the `stg__dim_cliente` and `stg__dim_empresa` staging tables to provide a unified view of client details along with their associated company information.  
It is used to simplify access to both client and company metadata, and acts as a shared dimension for downstream mart models such as `dim_clientes_final`.

Key enrichments:

- Joins company name, location, and status with each client
- Used to drive segmentation by company attributes
{% enddocs %}

{% docs int__empresa_geolocation %}
This intermediate model enriches the `stg__dim_empresa` (company) table with geolocation data (latitude and longitude) based on a join with a seed file containing city and state coordinates.

It enables spatial analysis and downstream use cases such as mapping, clustering, and geographic segmentation.

Key features:

- Joins by `cidade` and `estado`
- Adds `latitude` and `longitude` columns
- Acts as a source for any models that require company location information
{% enddocs %}

{% docs int__empresa_pix %}
This model combines data from `stg__dim_empresa` and `stg__dim_pix` to provide a unified view of companies and their PIX participation data.
It is used to analyze how companies are integrated with the PIX ecosystem, their authorization status, participation type, and regulatory compliance.

Key enrichments:

- Joins companies with their corresponding PIX institution data using `cnpj`
- Adds attributes like `autorizada_bcb`, `tipo_participacao_pix`, and `status_producao`
- Used in regulatory, adoption, and institutional analysis
{% enddocs %}

{% docs int__fato_contato_enriched %}
This model enriches the `stg__fato_contato` table (fact table of client contacts) by joining in client and company dimension data.
It is the foundation for funnel analysis and sales performance tracking across clients and companies.

Key features:

- Adds client and company attributes to each contact event
- Enables reporting by job role, company location, funnel stage, and contact method
- Used in conversion tracking and sales segmentation
{% enddocs %}
