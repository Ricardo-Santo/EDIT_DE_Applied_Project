# Staging docs

{% docs stg__dim_cliente %}
Staging dim table with **client** information. Contains a unique identifier for each client(**id_cliente**), the id of the company the client belongs to, the clients **nome** (name), **e-mail** address and it's **cargo** (position) in the company.
{% enddocs %}

{% docs stg__dim_empresa %}
Staging dim Table with **company** information. Contains a unique identifier for each company (**id_empresa**), the **cnpj** (*Cadastro Nacional de Pessoas Jurídicas*), which is the company's registry id for the government, the name of the company (**nome_empresa**), the state (**estado**) where the company is located, the city (**cidade**) where the company is located, the country (**pais**) where the company is located and contains a column **situacao** that describes if the company is authorized to carry out it's activity.
{% enddocs %}

{% docs stg__dim_pix %}
Staging dim table with Pix information. Contains the company name (**nome_reduzido**), the **ispb** which is the bank code ID for that company, the **cnpj** (*Cadastro Nacional de Pessoas Jurídicas*), which is the company's registry id for the government, the type of institution of the company (**tipo_de_instituicao**), the **autorizada_bcb** column explains if the company is authorized by the Brazillian Central Bank, the **tipo_participacao_spi** explains the type of participation the company has in the SPI (*Sistema de Pagamentos Instantâneos*), the **tipo_participacao_pix** explains the type of participation the company has in the PIX (*Sistema de pagamentos instatâneos*), the **modo_participacao_pix**, which explains what type of company are they registered as in the PIX, the **status_producao**, which explains the status of production the company's in, the **inic_transacao_pagamento** which explains if the company has started any transactions, the **facilitador_saque_troco** which explains if the company facilitates withdrawals or change to it's customers.
{% enddocs %}

{% docs stg__fato_contato %}
Staging Fact Table with information of the contact with the client. Contains **id_contato** which is a Unique Identifier for each contact made with the companies, the **id_cliente** which is the client's identification number, **id_empresa** which is the identification number of the corresponding company, the **data_contato** which is the date the contact was made with the client, the **etapa_funil** which is the status of the funnel stage the client is at the moment of the contact, the **canal** which is the how the sales contact was made and **responsavel** which is the person responsible for the corresponding contact with the client at a given time.
{% enddocs %}
