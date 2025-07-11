SELECT
  e.id_empresa,
  e.nome_empresa,
  e.cnpj,
  p.tipo_de_instituicao,
  p.autorizada_bcb,
  p.tipo_participacao_pix,
  p.mod_participacao_pix,
  p.status_producao,
  p.inic_transacao_pagamento,
  p.facilitador_saque_troco
FROM {{ ref('stg__dim_empresa') }} e
RIGHT JOIN {{ ref('stg__dim_pix') }} p
  ON e.cnpj = p.cnpj
