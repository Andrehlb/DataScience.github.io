AULA02 | Executando operações CRUD
PostgreSQL

[01Incluindo um registro na tabela08min](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/72574)

Agora que aprendemos a criar uma tabela de

banco de dados, e começamos a entender como funcionam os principais tipos que
vamos utilizar, aprenderemos como incluir os dados nesta tabela.

Começaremos aprendendo a sintaxe do INSERT.

Na tabela de exemplos do site da PostgreSQL, que você pode ter acesso clicando [aqui](https://www.postgresql.org/docs/8.1/sql-insert.html), observamos a descrição do código que
utilizaremos.

```
INSERT INTO table[ ( column [, ...]) ]

    { DEFAULTVALUES| VALUES( { expression| DEFAULT} [, ...]) | query}
```

Portanto, temos que escrever o comando INSERT INTO nome_da_tabela e declaramos as colunas e os valores. Olhando os exemplos no final
da página fica mais fácil de entender.

No primeiro exemplo temos a explicação de como
incluir uma linha de dados declarando apenas seus valores. Usamos essa forma
para preencher todos os campos da tabela, porque o programa irá preencher as
colunas na sequência declarada.

```
INSERT INTO films VALUES('UA502', 'Bananas', 105, '1971-07-13', 'Comedy', '82 minutes');
```

Então usamos o INSERT INTO, declaramos a coluna, e com VALUES declaramos os valores.

Contudo, o mais comum no dia-a-dia é
utilizarmos o segundo exemplo.

```
INSERT INTO films (code, title, did, date_prod, kind)

    VALUES('T_601', 'Yojimbo', 106, '1961-06-16', 'Drama');
```

Nesse modelo, colocamos INSERT INTO nome-da-tabela, declaramos os campos que receberão os dados,
a string VALUES e os dados.

Por ser o modelo usado com mais frequência, vamos utilizá-lo na nossa aula.

Já temos a nossa
tabela aluno, então escreveremos no pgAdmin INSERT INTO aluno(). Em seguida declaramos, nos parênteses, os
campos que vamos preencher, lembrando que o campo "id" incrementa automaticamente, então não
vamos nos preocupar com ele agora.

Começaremos pelo campo
"nome", que deve ser declarado nos parâmetros
do INSERT. Por ser um campo de texto, o dado que
colocaremos será uma string. Para adicioná-lo, colocaremos VALUES(''), porque usamos aspas simples para declarar que o dado é uma string,
assim como vimos no exemplo do site. Então colocarei o nome "Diogo".

```
INSERT INTO aluno (
    nome
) VALUES (
    'Diogo'
);

```

O "cpf" é um char, o que significa que ele também precisa de string, e temos
até 11 caracteres para preencher esse campo. Colocarei 12345678901, ou
seja, 11 caracteres.

O campo tipo text, que é o "observação", pode ser preenchido com qualquer
texto, então vou utilizar um "Lorem Ipsum", que é um texto gerado automaticamente pelo site [Lorem Ipsum](https://lipsum.com/). Portanto eu vou copiar esse texto e colocar
no nosso código como string, tirando as quebras de linha, e teremos nosso
texto grande.

```
INSERT INTO aluno (
    nome,
    cpf,
    observacao
) VALUES (
    'Diogo',
    '12345678901',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dui et nisl vestibulum consequat. Integer vitae magna egestas, finibus libero dapibus, maximus magna. Fusce suscipit mi ut dui vestibulum, non vehicula felis fringilla. Vestibulum eget massa blandit, viverra quam non, convallis libero. Morbi ut nunc ligula. Duis tristique purus augue, nec sodales sem scelerisque dignissim. Sed vel rutrum mi. Nunc accumsan magna quis tempus rhoncus. Duis volutpat nulla a aliquet feugiat. Vestibulum rhoncus mi diam, eu consectetur sapien eleifend in. Donec sed facilisis velit. Duis tempus finibus venenatis. Mauris neque nisl, pulvinar eu volutpat eu, laoreet in massa. Quisque vestibulum eros ac tortor facilisis vulputate. Sed iaculis purus non sem tempus mollis. Curabitur felis lectus, aliquam id nunc ut, congue accumsan tellus.'
);
```

O próximo é a "idade", que

está como número inteiro. Eu tenho 35 anos, então coloquei aqui 35. Com isso
vemos que, quando estamos falando de números inteiros, não precisamos colocar
aspas.

Agora vamos para o
"**dinheiro**", um campo `numeric (10,2)`. Quando
colocamos casas decimais, fazemos a separação por ponto ., porque o postgres entende que o ponto é o separador de casas
decimais. Vou colocar `100.50` (cem reais e cinquenta centavos).

No próximo campo
teremos um dado do tipo real para preenchermos a coluna "**altura**". Nesse campo podemos colocar tanto números inteiros quanto
com casas decimais. Colocaremos então o exemplo de `1.81`.

A seguir temos o campo
do tipo **boolean**, que aceita os valores `true`, para
verdadeiro, `false`, para falso, ou `null`, o equivalente a não passar nenhum valor. Meu status será ativo, então coloco true.

O próximo passo é
preencher a data de nascimento. Para incluir uma data no banco de dados, usamos
o formato `YYYY-MM-DD`. Nesse formato precisamos colocar, ano, mês
com duas casas de número e dia com duas casas de número. Por exemplo, '`1984-08-27`', equivalente a data `27 de agosto de 1984`.

O campo seguinte é o
da hora da aula. O formato de hora também é uma string, portanto
precisamos usar aspas simples na fórmula '`HH24:MI:SS`'.
Dessa forma declaramos o formato de 24 horas, portanto para designarmos o
horário da aula para cinco e meia da tarde, colocamos '`17:30:00`', zerando os segundos.

Por fim temos o campo
"**matriculado** **em**", do tipo data e hora.
Para separar as duas, primeiro colocamos uma data no mesmo formato anterior.
Hoje é 08 de fevereiro, então vou usar essa data, e são 12h32. Colocarei também
45 segundos. Então esse campo fica '`2020-02-08 12:32:45`'.

Beleza, já colocamos todos os tipos de campo!

Agora vamos selecionar

```vbnet
INSERT INTO aluno (
    nome,
    cpf,
    observacao,
    idade,
    dinheiro,
    altura,
    ativo,
    data_nascimento,
    hora_aula,
    matriculado_em
) VALUES (
    'Diogo',
    '12345678901',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dui et nisl vestibulum consequat. Integer vitae magna egestas, finibus libero dapibus, maximus magna. Fusce suscipit mi ut dui vestibulum, non vehicula felis fringilla. Vestibulum eget massa blandit, viverra quam non, convallis libero. Morbi ut nunc ligula. Duis tristique purus augue, nec sodales sem scelerisque dignissim. Sed vel rutrum mi. Nunc accumsan magna quis tempus rhoncus. Duis volutpat nulla a aliquet feugiat. Vestibulum rhoncus mi diam, eu consectetur sapien eleifend in. Donec sed facilisis velit. Duis tempus finibus venenatis. Mauris neque nisl, pulvinar eu volutpat eu, laoreet in massa. Quisque vestibulum eros ac tortor facilisis vulputate. Sed iaculis purus non sem tempus mollis. Curabitur felis lectus, aliquam id nunc ut, congue accumsan tellus.',
    35,
    100.50,
    1.81,
    TRUE,
    '1984-08-27',
    '17:30:00',
    '2020-02-08 12:32:45'
);

```

o código e clicar em executar. Lembrando que precisamos especificar todos os
campos que vamos preencher e a mesma quantidade de dados. E faremos uma nova
busca no banco de dados utilizando SELECT * FROM aluno;,
que serve para trazermos os dados.

Podemos perceber que não
colocamos a informação de "id", mas ele já preencheu. Temos o
nome, CPF, o texto gigante no campo observação, a idade, o dinheiro, o campo do
tipo real, o boleano, a data de nascimento, a hora da aula e o matriculado em.
Ou seja, temos todos os tipos de campo que precisaríamos aprender para
trabalhar no dia-a-dia, porque são os mais utilizados. No seu trabalho serão
basicamente eles que você utilizará para trabalhar no banco de dados.

Na próxima aula aprenderemos como alterar os
dados deste cadastro.

CONTINUAR LENDO

* [~~02Incluindo um
  professor~~](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/74019)
* [03Atualizando um
  registro na tabela05min](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/72575)

# 03**Atualizando um registro na tabela**

## Descrição

Olá pessoal! Tudo bem? Boas-vindas novamente.

Agora que descobrimos como registrar dados na tabela, aprenderemos como alterá-los. Na [documentação do postgres](https://www.postgresql.org/docs/12/sql-update.html) encontramos a sintaxe para realizar um  **update** .

```r
UPDATE [ ONLY ] table_name [ * ] [ [ AS ] alias ]
    SET { column_name = { expression | DEFAULT } |
          ( column_name [, ...] ) = [ ROW ] ( { expression | DEFAULT } [, ...] ) |
          ( column_name [, ...] ) = ( sub-SELECT )
        }
                [ WHERE condition | WHERE CURRENT OF cursor_name ]
```

Na documentação também temos exemplos de como atualizar os dados. No primeiro exemplo, a tabela " **films** " passa pelo update do campo `kind`, cujo valor " **Drama** " é alterado para " **Dramatic** ".

Agora aplicaremos esse conhecimento no nosso banco de dados. Primeiramente selecionamos a nossa tabela com `SELECT * FROM` e utilizar o `WHERE` para filtrar apenas os dados que serão alterados. Isso evita que haja update em todos os registros do banco. No nosso caso, aplicaremos o " **id** " como filtro. Atualmente temos apenas uma entrada, mas quando houver vários registros na tabela, esse comando, ao ser executado, apresentará apenas os dados do " **id** " declarado.

```sql
SELECT *
    FROM aluno
WHERE id = 1
```

Agora que filtramos os dados que queremos alterar, podemos utilizar o `UPDATE nome_da_tabela` para atualizar a tabela, e para informarmos os campos que modificaremos, usamos o `SET`. No nosso exemplo, mudaremos o valor de todos os campos para fixar melhor a sintaxe, sendo a mesma do `INSERT`. Então copiaremos todos os campos para dentro do **`SET`** e atribuiremos novos valores para cada um deles.

```sql
UPDATE aluno
    SET nome = 'Nico',
    cpf = '10987654321',
    observacao = 'Teste',
    idade = 38,
    dinheiro = 15.23,
    altura = 1.90,
    ativo = FALSE,
    data_nascimento = '1980-01-15',
    hora_aula = '13:00:00',
    matriculado_em = '2020-01-02 15:00:00'
WHERE id = 1;
```

> **Atenção:** Não esqueça de colocar um **`=`** antes de atribuir um novo valor.

Selecionando o código do `UPDATE` e clicando no botão de executar, recebemos a mensagem de sucesso na atualização, e com o código `SELECT * FROM aluno;` vemos que a tabela com os novos dados.

Agora que descobrimos como fazer a atualização do banco de dados, aprenderemos como excluir um registro, mas isso fica para próxima aula.

Até a próxima!

 OUTROS LINKS

* [04Alterando o
  percentual do INSS

  ](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/74020)
* 04**Alterando o percentual do INSS**

Ocorreu uma mudança na lei trabalhista, informando que o valor do desconto do INSS sobre o salário dos funcionários deve ser alterado. Esse valor é baseado na faixa de percentual abaixo:

```undefined
até 1.045,00                    7,5%
de 1.045,01 até 2.089,60        9%
de 2.089,61 até 3.134,40        12%
de 3.134,41 até 6.101,06        14%COPIAR CÓDIGO
```

Baseado na tabela `funcionarios`, que possui o campo `percentual_inss` e o campo `salario`, marque a alternativa correta para a atualização do `percentual_inss` para  **14%** :

Selecione uma alternativa*  

* [ ]

```sql
  UPDATE funcionarios 
      SET percentual_inss = 0,14 
  WHERE salario >= 3134,41 
      AND salario <= 6101,06;
```

* [X] X

  ```sql
  UPDATE funcionarios
      SET percentual_inss = 0.14 
  WHERE salario >= 3134.41 
      AND salario <= 6101.06;
  ```
* [ ]

  ```sql
  UPDATE 
      SET percentual_inss = 0.14 
  WHERE salario >= 3134.41 
      AND salario <= 6101.06;
  ```
* [ ]

  ```java
  UPDATE funcionarios
      SET percentual_inss = 0.14 
  WHERE salario => 3134.41 
      AND salario =< 6101.06;
  ```


# [PostgreSQL](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos "Ir para página do curso")

* [05Excluindo um](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/72576)
* [registro da tabela04min](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/72576)

# 05**Excluindo um registro da tabela**

## Descrição

Olá pessoal! Tudo bem? Boas-vindas novamente!

Agora que aprendemos a incluir e a alterar os registros do banco de dados, aprenderemos como excluir os dados da tabela. Na [documentação do postgres](https://www.postgresql.org/docs/current/sql-delete.html) temos a sintaxe do `DELETE`.

```sql
DELETE FROM [ ONLY ] table_name [ * ] [ [ AS ] alias ]
    [ USING from_item [, ...] ]
    [ WHERE condition | WHERE CURRENT OF cursor_name ]COPIAR CÓDIGO
```

Conferindo os exemplos, podemos ver duas aplicações mais comuns desse comando. Na primeira, o `DELETE FROM nome_da_tabela` é aplicado com o filtro `WHERE nome_da_coluna`, que pode ser igual ou diferente a um valor. No outro exemplo, foi utilizado o `DELETE FROM nome_da_tabela`, o campo a ser excluído e o resultado de uma `SELECT` já filtrada.

```sql
DELETE FROM films WHERE kind <> 'Musical';

DELETE FROM films
  WHERE producer_id IN (SELECT id FROM producers WHERE name = 'foo');
```

Vamos aplicar esse comando ao nosso banco de dados, onde temos o registro do " **Nico** " para entendê-lo melhor. Para deletar esse dado, é importante utilizarmos o filtro, como aprendemos na aula passada, evitando a exclusão do registro errado. Dessa vez filtraremos por `nome = 'Nico'`.

```sql
SELECT *
    FROM aluno 
    WHERE nome = 'Nico';
```

Caso utilizássemos outro valor para o nome, não haveria nenhum retorno, porque só temos registro do "Nico". Então sempre que for excluir um dado, utilize o `SELECT` antes para confirmar se o seu filtro está correto. Após confirmado, basta trocar o `SELECT *` por `DELETE` e executar o código para realizarmos a exclusão.

Se utilizarmos novamente o `SELECT * FROM` para pesquisarmos por "Nico", não teremos retorno, já que ele era o único dado inserido na tabela, portanto agora ela ficou vazia. Por isso precisamos de um filtro, porque se apenas executarmos o `DELETE FROM nome_da_tabela`, todos os nossos registros serão apagados, e geralmente você só precisa deletar um registro em específico.

Dessa forma aprendemos como funciona o `DELETE`. Na próxima aula entenderemos mais sobre os filtros.


* [06Excluindo produtos
  ](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/74021)

# 06**Excluindo produtos**

Você recebeu a tarefa de criar um *script* para remover os produtos que não possuíam mais estoque, na tabela `produtos`. Essa tabela possui um campo chamado `estoque`, que armazena a quantidade de itens disponíveis.

Marque a alternativa que representa o *script* de exclusão dos produtos sem estoque.

Selecione uma alternativa*  [ ]

```sql
  DELETE produtos
  WHERE estoque = 0;
```

* [ ]
  ```sql
  DELETE 
      FROM produtos
  WHERE estoque > 0;
  ```
* [ ]
  ```sql
  DELETE estoque 
  WHERE produtos = 0;
  ```
* [ ]
  ```sql
  DELETE 
      FROM produtos
  WHERE estoque = 0;
  ```


* [07Faça como eu fiz](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/74002)
* [08Projeto da aula](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/99437)
* [09O que aprendemos?

  ](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/74003)

Nesta aula, aprendemos:

* Como incluir um registro na tabela, entendendo a sintaxe de inclusão de cada tipo de campo
* A efetuar uma consulta simples, para listar os dados da tabela
* Como alterar um registro na tabela
* Como excluir um registro na tabela
