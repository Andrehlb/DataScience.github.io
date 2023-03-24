PostgreSQL

[01Incluindo um registro na tabela08min](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/72574)

Agora que aprendemos a criar uma tabela de

banco de dados, e começamos a entender como funcionam os principais tipos que
vamos utilizar, aprenderemos como incluir os dados nesta tabela.

Começaremos aprendendo
a sintaxe do INSERT. Na tabela de exemplos do site da PostgreSQL,
que você pode ter acesso clicando [aqui](https://www.postgresql.org/docs/8.1/sql-insert.html), observamos a descrição do código que
utilizaremos.

INSERTINTOtable[ ( column [, ...]) ]

    { DEFAULTVALUES| VALUES( { expression| DEFAULT} [, ...]) | query}COPIAR
CÓDIGO

Aviso: Esse é o
código atualizado no site. Na época em que o vídeo estava sendo gravado, haviam
mais opções de comando INSERT.'

Portanto, temos que
escrever o comando INSERT INTO nome_da_tabela e declaramos as colunas e os valores. Olhando os exemplos no final
da página fica mais fácil de entender.

No primeiro exemplo temos a explicação de como
incluir uma linha de dados declarando apenas seus valores. Usamos essa forma
para preencher todos os campos da tabela, porque o programa irá preencher as
colunas na sequência declarada.

INSERTINTOfilms VALUES('UA502', 'Bananas', 105, '1971-07-13', 'Comedy', '82 minutes');COPIAR
CÓDIGO

Então usamos o INSERT INTO, declaramos a coluna, e com VALUES declaramos os valores.

Contudo, o mais comum no dia-a-dia é
utilizarmos o segundo exemplo.

INSERTINTOfilms (code, title, did,
date_prod, kind)

    VALUES('T_601', 'Yojimbo', 106, '1961-06-16', 'Drama');COPIAR
CÓDIGO

Nesse modelo,
colocamos INSERT INTO nome-da-tabela, declaramos os campos que receberão os dados,
a string VALUES e os dados. Por
ser o modelo usado com mais frequência, vamos utilizá-lo na nossa aula.

Já temos a nossa
tabela aluno, então escreveremos no pgAdmin INSERT INTO aluno(). Em seguida declaramos, nos parênteses, os
campos que vamos preencher, lembrando que o campo "id" incrementa automaticamente, então não
vamos nos preocupar com ele agora.

Começaremos pelo campo
"nome", que deve ser declarado nos parâmetros
do INSERT. Por ser um campo de texto, o dado que
colocaremos será uma string. Para adicioná-lo, colocaremos VALUES(''), porque usamos aspas simples para declarar que o dado é uma string,
assim como vimos no exemplo do site. Então colocarei o nome "Diogo".

INSERTINTOaluno (

    nome

) VALUES(

    'Diogo');

COPIAR CÓDIGO

O "cpf" é um char, o que significa que ele também precisa de string, e temos
até 11 caracteres para preencher esse campo. Colocarei 12345678901, ou
seja, 11 caracteres.

O campo tipo text,
que é o "observação", pode ser preenchido com qualquer
texto, então vou utilizar um "Lorem Ipsum", que é um texto gerado automaticamente pelo site [Lorem Ipsum](https://lipsum.com/). Portanto eu vou copiar esse texto e colocar
no nosso código como string, tirando as quebras de linha, e teremos nosso
texto grande.

INSERT
INTOaluno (

    nome,

    cpf,

    observacao

) VALUES (

    'Diogo','12345678901','Lorem ipsum dolor sit amet,
consectetur adipiscing elit. Nulla ac dui et nisl vestibulum consequat. Integer
vitae magna egestas, finibus libero dapibus, maximus magna. Fusce suscipit mi
ut dui vestibulum, non vehicula felis fringilla. Vestibulum eget massa blandit,
viverra quam non, convallis libero. Morbi ut nunc ligula. Duis tristique purus
augue, nec sodales sem scelerisque dignissim. Sed vel rutrum mi. Nunc accumsan
magna quis tempus rhoncus. Duis volutpat nulla a aliquet feugiat. Vestibulum
rhoncus mi diam, eu consectetur sapien eleifend in. Donec sed facilisis velit.
Duis tempus finibus venenatis. Mauris neque nisl, pulvinar eu volutpat eu,
laoreet in massa. Quisque vestibulum eros ac tortor facilisis vulputate. Sed
iaculis purus non sem tempus mollis. Curabitur felis lectus, aliquam id nunc
ut, congue accumsan tellus.');COPIAR CÓDIGO

O próximo é a "idade", que
está como número inteiro. Eu tenho 35 anos, então coloquei aqui 35. Com isso
vemos que, quando estamos falando de números inteiros, não precisamos colocar
aspas.

Agora vamos para o
"dinheiro", um campo numeric (10,2). Quando
colocamos casas decimais, fazemos a separação por ponto ., porque o postgres entende que o ponto é o separador de casas
decimais. Vou colocar 100.50 (cem reais e cinquenta centavos).

No próximo campo
teremos um dado do tipo real para preenchermos a coluna "altura". Nesse campo podemos colocar tanto números inteiros quanto
com casas decimais. Colocaremos então o exemplo de 1.81.

A seguir temos o campo
do tipo boolean, que aceita os valores true, para
verdadeiro, false, para falso, ou null, o equivalente a não passar nenhum valor. Meu status será ativo, então coloco true.

O próximo passo é
preencher a data de nascimento. Para incluir uma data no banco de dados, usamos
o formato YYYY-MM-DD. Nesse formato precisamos colocar, ano, mês
com duas casas de número e dia com duas casas de número. Por exemplo, '1984-08-27', equivalente a data 27 de agosto de 1984.

O campo seguinte é o
da hora da aula. O formato de hora também é uma string, portanto
precisamos usar aspas simples na fórmula 'HH24:MI:SS'.
Dessa forma declaramos o formato de 24 horas, portanto para designarmos o
horário da aula para cinco e meia da tarde, colocamos '17:30:00', zerando os segundos.

Por fim temos o campo
"matriculado
em", do tipo data e hora.
Para separar as duas, primeiro colocamos uma data no mesmo formato anterior.
Hoje é 08 de fevereiro, então vou usar essa data, e são 12h32. Colocarei também
45 segundos. Então esse campo fica '2020-02-08 12:32:45'.

Beleza, já colocamos todos os tipos de campo!

INSERT
INTOaluno (

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

    'Diogo','12345678901','Lorem ipsum dolor sit amet,
consectetur adipiscing elit. Nulla ac dui et nisl vestibulum consequat. Integer
vitae magna egestas, finibus libero dapibus, maximus magna. Fusce suscipit mi
ut dui vestibulum, non vehicula felis fringilla. Vestibulum eget massa blandit,
viverra quam non, convallis libero. Morbi ut nunc ligula. Duis tristique purus
augue, nec sodales sem scelerisque dignissim. Sed vel rutrum mi. Nunc accumsan
magna quis tempus rhoncus. Duis volutpat nulla a aliquet feugiat. Vestibulum
rhoncus mi diam, eu consectetur sapien eleifend in. Donec sed facilisis velit.
Duis tempus finibus venenatis. Mauris neque nisl, pulvinar eu volutpat eu,
laoreet in massa. Quisque vestibulum eros ac tortor facilisis vulputate. Sed
iaculis purus non sem tempus mollis. Curabitur felis lectus, aliquam id nunc
ut, congue accumsan tellus.',35,

    100.50,

    1.81,

    TRUE,

    '1984-08-27','17:30:00','2020-02-08 12:32:45');COPIAR
CÓDIGO

Agora vamos selecionar
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

 [DISCUTIR NO FORUM](https://cursos.alura.com.br/forum/curso-introducao-postgresql-primeiros-passos/exercicio-incluindo-um-registro-na-tabela/72574/novo)[PRÓXIMA ATIVIDADE](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/72574/next)

[PostgreSQL](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos)

15%

Buscar neste curso Pesquisar

AULA02

Executando
operações CRUD

 AULA ATUAL

 ATIVIDADES

* [01Incluindo um registro na tabela08min](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/72574)
* [02Incluindo um
  professor](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/74019)
* [03Atualizando um
  registro na tabela05min](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/72575)
* [04Alterando o
  percentual do INSS](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/74020)
* [05Excluindo um
  registro da tabela04min](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/72576)
* [06Excluindo produtos](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/74021)
* [07Faça como eu fiz](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/74002)
* [08Projeto da aula](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/99437)
* [09O que aprendemos?](https://cursos.alura.com.br/course/introducao-postgresql-primeiros-passos/task/74003)

 OUTROS LINKS
