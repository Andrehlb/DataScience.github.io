PASSO 2: HIGIENIZAÇÃO DE DADO
Nome da tabela: prata_netflix
Inserir os dados na tabela acima com as seguintes regras:

- a tabela deve conter as mesmas colunas da camada bronze;
- Campos que possuem valores vazios devem ter esses valores substituídos pela string: “Desconhecido”;
- O campo description pode ter somente 120 caracteres, portanto, caso haja mais, considerar somente os primeiros 120
- O campo show_id precisa ser do tipo integer na nova tabela, para isso antes da inserção na tabela a string: “s” deve ser removida;
- O campo release_year deve ser inteiro, caso o campo esteja vazio, considerar o valor 9999

Entendi. Vamos seguir os passos para realizar a higienização dos dados e inserção na tabela `prata_netflix`:

1. Criar a tabela `prata_netflix` com as mesmas colunas da tabela `bronze_netflix`, exceto pelo campo `show_id` que será alterado para `integer`:

```
CREATE TABLE prata_netflix(
   show_id      INTEGER NOT NULL PRIMARY KEY,
   type         VARCHAR(7) NOT NULL,
   title        VARCHAR(104) NOT NULL,
   director     VARCHAR(208),
   desc_cast    VARCHAR(771),
   country      VARCHAR(123),
   date_added   VARCHAR(19),
   release_year INTEGER NOT NULL,
   rating       VARCHAR(8),
   duration     VARCHAR(10),
   listed_in    VARCHAR(79) NOT NULL,
   description  VARCHAR(120) NOT NULL
);

```




2. Inserir os dados na tabela `prata_netflix` com as devidas transformações e ajustes:

```
SELECT
    CAST(REPLACE(show_id, 's', '') AS INTEGER) AS show_id,
    COALESCE(type, 'Desconhecido') AS type,
    COALESCE(title, 'Desconhecido') AS title,
    COALESCE(director, 'Desconhecido') AS director,
    COALESCE(desc_cast, 'Desconhecido') AS desc_cast,
    COALESCE(country, 'Desconhecido') AS country,
    COALESCE(date_added, 'Desconhecido') AS date_added,
    COALESCE(CAST(release_year AS INTEGER), 9999) AS release_year,
    COALESCE(rating, 'Desconhecido') AS rating,
    COALESCE(duration, 'Desconhecido') AS duration,
    COALESCE(listed_in, 'Desconhecido') AS listed_in,
    CASE
        WHEN LENGTH(description) <= 120 THEN COALESCE(description, 'Desconhecido')
        ELSE LEFT(description, 120)
    END AS description
FROM bronze_netflix;
```

Explicando o código acima:

* No comando `INSERT INTO`, estamos inserindo os dados na tabela `prata_netflix`, especificando as colunas que receberão os valores;
* No comando `SELECT`, estamos selecionando as colunas que precisamos das tabelas `bronze_netflix` e aplicando as devidas transformações e ajustes;
* Usamos a função `REPLACE` para remover a letra "s" do campo `show_id` e depois converter o valor para inteiro com `CAST`;
* Usamos a função `COALESCE` para substituir os valores vazios pela string "Desconhecido";
* No campo `description`, usamos a função `LEFT` para pegar apenas os primeiros 120 caracteres e a função `LENGTH` para contar o número de caracteres;
* Para o campo `release_year`, usamos a função `CAST` para converter para inteiro e a função `COALESCE` para substituir o valor vazio por 9999.

  para verificar tabelas que tem no schema:

  ```
  SELECT table_name FROM information_schema.tables WHERE table_schema='public'
  ```
