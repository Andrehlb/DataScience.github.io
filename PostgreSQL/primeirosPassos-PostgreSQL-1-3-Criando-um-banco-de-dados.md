03 Criando um banco de dados

Olá pessoal! Tudo bem? Boas-vindas novamente.

Agora vamos aprender como criar um banco de dados. É muito simples e podemos fazer de duas formas: usando o pgAdmin ou utilizando o prompt de comando do SQL Shell (psql). Vamos ver como cada uma funciona.

No prompt de comando podemos utilizar o CREATE DATABASE para dizer ao programa que queremos criar um banco. Podemos chamar o nosso banco de teste de "alura", portanto CREATE DATABASE alura;. Quando eu faço isso, consigo criar um banco de dados.

Atenção: Sempre que digitar um comando no prompt de comandos do SQL Shell (psql), você deve finalizar com ; e apertar a tecla "Enter" para confirmar o comando. Só assim ele será executado.

Para visualizar os bancos de dados já estão no nosso postgres, podemos usar o comando \l. Quando apertamos "Enter", aparece a seguinte tabela:

List of databse

| Name      | Owner    | Encoding | Collate                | Ctype                  | Access privileges                           |
| --------- | -------- | -------- | ---------------------- | ---------------------- | ------------------------------------------- |
| alura     | postgres | UTF8     | Portuguese_Brazil.1252 | Portuguese_Brazil.1252 |                                             |
| postgres  | postgres | UTF8     | Portuguese_Brazil.1252 | Portuguese_Brazil.1252 |                                             |
| template0 | postgres | UTF8     | Portuguese_Brazil.1252 | Portuguese_Brazil.1252 | =c/postgres +`<br>` postgres=CTc/postgres |
| template1 | postgres | UTF8     | Portuguese_Brazil.1252 | Portuguese_Brazil.1252 | =c/postgres +`<br>` postgres=CTc/postgres |

Podemos ver que o banco "alura" foi criado e que já tínhamos bancos, chamados "postgres", "template0" e o "template1". Basicamente é assim que criamos um banco de dados. Já definimos o banco "alura" com o Enconding UTF8 e Owner postgres.

E se a gente quiser utilizar o pgAdmin para criar? Seria bem mais simples. Vamos ver como funciona.

Primeiramente, para visualizar o banco que acabamos de criar, clicamos em Database com o botão direito do mouse e selecionamos a opção Refresh. Com isso já podemos ver o banco da "alura" e conseguimos mexer nele.

Antes disso, vamos clicar em Database com o botão direito, passar o mouse sobre a opção create e clicar na pção "Database" que surge em seguida.

![Exemplo de imagem](https://github.com/Andrehlb/dvelopment.github.io/blob/e16f348de35fdc47083a09e3f145e851af649337/PostgreSQL/Assets/Images/criando_database_pgadmin.png "criando_database_pgadmin")

Guia de comandos para abrir a janela de criação do database

Na janela que abre conseguimos digitar o nome da base de dados que a gente quer criar no campo Database. Vou colocar aqui "teste2". Vamos criar esse banco de dados e deixar o "postgres" no campo "Owner".

Mas olha que legal. Se viermos na última guia, chamada "SQL", a gente consegue visualizar qual o comando a gente deveria utilizar para criar.

Janela da criação do Database com a guia do SQL em destaque e o código SQL aberto

Então temos:

CREATE DATABASE teste2
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;COPIAR CÓDIGO
O nosso Database "teste2" WITH(com) OWNER (dono) postgres. Dessa forma estamos declarando que o usuário postgres será o dono do banco de dados, tendo permissões para ele fazer alterações dentro dele. Além disso definimos o Enconding para UTF8 e não colocamos limites de conexão, como podemos ver na linha CONNECTION LIMIT = -1;.

Se colocássemos esse mesmo comando e executássemos no prompt de comando, funcionaria exatamente da mesma forma.

Vou clicar em "salvar" e ele vai criar esse banco de dados chamado "teste 2".

Se você quiser apagar esse banco de dados, basca clicar em cima do nome dele com o botão direito e clicar na opção "Delete/Drop". Uma janela de confirmação vai abrir e você clica no botão "Yes".

Mas o programa não mostrou o comando que vamos utilizar, então vamos ver no prompt.

Vamos começar criando um novo database com o comando CREATE DATABASE teste;. Vou colocar o comand \l para vermos que foi criado o banco "teste" e, se eu quisesse apagar o banco de dados, eu colocaria o comando DROP DATABASE teste;.

Se digitarmos \l novamente, veremos que o banco de dados foi apagado.

Dessa forma conseguimos fazer criação e exlcusão de um banco de dados utilizando postgres.
