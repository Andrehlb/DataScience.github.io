# 05**Criando uma tabela**

## Descrição

Olá pessoal! Tudo bem? Boas-vindas novamente.

Agora vamos aprenderemos como criar uma tabela no banco de dados. Para isso precisamos entender quais são os tipos de dados que as tabelas podem receber.

Começaremos uma simulação baseada no aluno da Alura. Poderíamos ter o nome, RG, telefone, data de nascimento e vários outros dados dessa pessoa para utilizarmos. Porém, precisamos saber como definimos esses  *types* .

Podemos encontrar todos os tipos de campos de dados para o postgres neste [link](https://www.postgresql.org/docs/12/datatype.html). Contudo, são muitos campos então selecionaremos os mais utilizados no dia-a-dia de quando estamos trabalhando com banco de dados.

Os primeiros tipos de campo são referentes a números, e podem ser encontrados [nesta página](https://www.postgresql.org/docs/12/datatype-numeric.html). Vamos copiando a palavra  ***integer*** , que se refere a dados que são números inteiros entre -2147483648 e +2147483647. Depois colamos esse tipo no *Query Editor* do banco de dados "alura".

> **Dica:** Caso tenha dúvidas de como abrir o  *Query Editor* , volta na aula anterior pare relembrar como acessar as *Query Tools* no  **pgAdmin** . Depois disso basta aplicar as mesmas etapas ao banco de dados "alura".

Copiaremos também o  ***real*** , que utilizamos para dados numéricos com casas decimais de até seis dígitos, e colamos na linha abaixo do  *integer* .

Outro campo que utilizamos é o  ***serial*** , para números inteiros positivos com incremento automático, ou seja, não precisamos colocar o valor dele, pois quando incluirmos um novo dado, ele já será incrementado  **+ 1** .

Utilizaremos também o tipo  ***numeric*** , porque, com ele, poderemos definir a precisão, ou seja, a quantidade de casas decimais que queremos no número.

Beleza! Esses são campos numéricos que trabalharemos. Agora vamos para os campos de texto, encontrados [nesta página](https://www.postgresql.org/docs/12/datatype-character.html).

Existem três tipos de campo de texto:

* O  ***varchar(n)*** , utilizado em 90% dos casos. Ele funciona para textos com um número de caracteres pré-determinado. Por exemplo: o **nome** de uma pessoa teria até, aproximadamente, 255 caracteres, portanto poderíamos caracterizá-lo como  *varchar* ;
* O  ***char(n)*** , utilizado quando sabemos exatamente a quantidade de caracteres que será utilizada naquele campo. Por exemplo, o campo de **CPF** sempre vai ter 11 caracteres, então podemos colocá-lo em um campo do tipo  *char* , que já tem o tamanho pré-definido. Porém, se foram definidos 11 caracteres para o campo e a pessoa preencheu apenas 9, os dois caracteres restantes serão preenchidos com espaços em branco, e não queremos isso. Por isso o  **este *type* só deve ser utilizado quando o dado tiver um número exato de caracteres** ;
* O  ***text*** , utilizado quando não temos ideia de qual será o tamanho do texto, mas ainda queremos armazená-lo no banco de dados.

Vamos guardar os três *types* no nosso arquivo.

Outro campo que geralmente utilizamos são os  *boolean types* , que, na verdade, é um único tipo:  ***boolean*** . Ele é definido para ser verdadeiro ou falso, podendo ser utilizado quando só duas opções são possíveis: ativo ou inativo, se uma ação foi executada ou não e exemplos similares.

Temos também os campos de data e hora,que são, sucessivamente, do tipo ***date*** e do tipo  ***time*** . Assim como temos o campo ***timestamp*** que apresenta tanto a data quanto a hora. Estes tipos de campo estão [nesta página](https://www.postgresql.org/docs/12/datatype-datetime.html).

Basicamente são esses tipos de campo que utilizaremos:

```sql
integer
real
serial
numeric

varchar(n)
char(n)
text

boolean

date
time
timestampC
```

Agora na nossa simulação vamos criar uma tabela com os dados de alunos. Para isso precisamos escrever o código **`CREATE TABLE aluno();`** abaixo dessa lista.

Dentro dos parênteses dessa tabela, colocaremos os tipos de dados que queremos registrar. Primeiramente temos o " **id** " do aluno que é do tipo  *serial* , para poder ser incrementado automaticamente.

```scss
CREATE TABLE aluno(
    id SERIAL,

);
```

Colocaremos também o campo para o **nome** do aluno, utilizando  **`nome VARCHAR(255),`** , porque o nome pode ter de zero a 255 caracteres. Podemos colocar também o campo de **CPF** com o tipo  *char* , definindo com 11 caractéres, já que sabemos o tamanho exato do texto, portanto  **`cpf CHAR(11),`** .

Outro campo que podemos criar é o campo **observação** para simular um campo do tipo  *text* , com  **`observação TEXT`** , afinal não sabemos o limite do texto, que poderia ser gigantesco. E para utilizarmos números inteiros, podemos colocar o campo  **idade** , que não tem casa decimal, como  **`idade INTEGER,`** .

O campo do tipo *numeric* pode ser usado para representar quanto dinheiro o aluno tem, então  **`dinhero NUMERIC(10,2),`** , onde o 10 representa o número de caractéres, que são  **1234567890** , e 2 a quantidade de casas decimais, ou seja,  **12345678,90** . E vamos utilizar o tipo *real* para registrarmos a **altura** do aluno,com  **`altura REAL`** , que pode ter entre 1 e 6 casas decimais.

Com isso colocamos todos tipos de campos de numerais e todos os tipos de campos de texto.

```scss
CREATE TABLE aluno(
        id SERIAL,
        nome VARCHAR(255),
        cpf CHAR(11),
        observação TEXT,
        idade INTEGER,
        dinheiro NUMERIC(10,2),
        altura REAL,

);
```

Podemos utilizar o boleano para colocar se o aluno está ativo ou não, ou seja,  **`ativo BOOLEAN,`** . E o tipo *date* pode ser usado em um campo para data de nascimento,  **`data_nascimento DATE,`** .

Vamos colocar também o horário da aula para usar o  *time* , com  **`hora_aula TIME,`** , e para registrar a matrícula do aluno, utilizaremos o  *timestamp* , ou seja, **`matriculado_em TIMESTAMP`**

Temos, então, uma tabela com todos os tipos de dados que poderemos utilizar para aprender como eles funcionam.

```sql
CREATE TABLE aluno(
    id SERIAL,
        nome VARCHAR(255),
        cpf CHAR(11),
        observação TEXT,
        idade INTEGER,
        dinheiro NUMERIC(10,2),
        altura REAL,
        ativo BOOLEAN,
        data_nascimento DATE,
        hora_aula TIME,
        matriculado_em TIMESTAMP
);
```

Para criar essa tabela no banco de dados, selecionamos o código e clicamos no botão de execução.

![Código selecionado e o botão executar em destaque. Uma seta vermelha aponta para mensagem de sucesso abaixo do editor de códigos](https://caelum-online-public.s3.amazonaws.com/1659-postgreSQL-Primeiros-passos-com-SQL/Transcri%C3%A7%C3%A3o/Aula+1/Imagens/executando_tabela_com_sucesso.png)

Vamos fazer um teste rápido para saber se a tabela está funcionando digitando o código `SELECT * FROM aluno`, já que "aluno" é o nome da tabela. Mais uma vez selecionamos o código que queremos executar e clicamos no botão de execução para trazer os dados.

Com isso veremos a tabela, que agora está vazia, na guia *Data output* abaixo do editor de código.

![Tabela vazia na guia Data output, abaixo do editor de códigos, indicada por uma seta vermelha](https://caelum-online-public.s3.amazonaws.com/1659-postgreSQL-Primeiros-passos-com-SQL/Transcri%C3%A7%C3%A3o/Aula+1/Imagens/tabela_no_banco_de_dados.png)

# 06**Tabela de empresa**

Você está trabalhando em um projeto em que seus clientes precisam cadastrar alguns dados das empresas que são suas parceiras. Em uma reunião para definir quais dados os seus clientes precisam, ficou acordado as seguintes colunas:

* Um identificador numérico, sem casas decimais, que deve ser incrementado automaticamente
* O CNPJ
* A razão social
* O nome fantasia
* A data de abertura da empresa

Quais das alternativas abaixo representa o comando SQL para criar a tabela que armazenará os dados das empresas?

Selecione uma alternativa*  [ ]

```sql
  CREATE TABLE empresas (
      id INTEGER,
      cnpj INTEGER,
      razao_social VARCHAR(255),
      nome_fantasia VARCHAR(255),
      data_abertura DATE
  );
```

* [ ]
  ```sql
  CREATE TABLE empresas (
      id SERIAL,
      cnpj INTEGER,
      razao_social VARCHAR(255),
      nome_fantasia VARCHAR(255),
      data_abertura DATA
  );
  ```
* [ ]
  ```sql
  CREATE TABLE empresas (
      id SERIAL,
      cnpj CHAR(14),
      razao_social VARCHAR(255),
      nome_fantasia VARCHAR(255),
      data_abertura DATE
  );
  ```
* [ ]
  ```sql
  CREATE TABLE empresas (
      id SERIAL,
      cnpj CHAR(14),
      razao_social REAL,
      nome_fantasia BOOLEAN,
      data_abertura DATE
  );
  ```
