# 01**Apresentação**

## Descrição

> **Observação:** ***PostgreSQL: Primeiros passos com SQL***  ou   ***Introdução ao Banco de dados: PostgreSQL***  se trata do mesmo conteudo.

Tópico de Diogo Mascarenhas | Alura
Curso de  **Introdução ao Banco de Dados: PostgreSQL** .
O nosso objetivo neste curso é apresentar uma introdução às principais funções que você pode utilizar nesse poderoso banco de dados relacional  *open source* .

O **pré-requisito** para esse curso é ter uma noção básica sobre o que é um banco de dados, porque focaremos na prática através do PostgreSQL, o banco de dados relacional mais avançado do mundo, segundo a autodeclaração no [site oficial](https://www.postgresql.org/).

![Página inicial do PostgreeSQL na qual há um banner com a imagem de uma família de elefantes na savana em escala de cinza e, sobre ela, a frase ](https://caelum-online-public.s3.amazonaws.com/1659-postgreSQL-Primeiros-passos-com-SQL/Transcri%C3%A7%C3%A3o/Aula+1/Imagens/home+postgreSQL.png)

Os tópicos que iremos abordar nesse curso serão:

* Instalação do **PostgreeSQL (versão 12)** e  **pgAdmin (versão 4)** ;
* Como criar e excluir um banco de dados;
* Criação de tabelas dentro do banco de dados;
* Inclusão, alteração e exclusão de registros dentro das tabelas;
* Como fazer consultas em um banco de dados;
* Quais são os tipos de dados;
* Filtragem de dados com os operadores ***e***  e ***ou*** ;
* Junção nas consultas de dados ( *Joins* ,  *Left* ,  *Right* ,  *Full* <  *Cross* );
* Chaves primárias e chaves estrangeiras;
* Restrições usando ***restrict*** e deleção de dados de outras tabelas com  ***cascade*** ;
* Como ordenar ou limitar as consultas;
* Agrupamento de dados;
* Análise e operações de dados;
* Elaboração de filtros para os agrupamentos.

Não precisa se preocupar caso não tenha entendido alguns termos dessa introdução, porque ao longo do curso você aprenderá o significado de todos eles.

# 02 **Ambiente e versões**

## Descrição

Olá pessoal, tudo bem? Boas-vindas novamente!

Nosso primeiro passo para utilizar o **PostgreSQL** é fazer a instalação dele na nossa máquina. Para isso, pesquise "PostgreSQL" no Google e clique no primeiro link. Ele leva para para o [site oficial](http://https//www.postgresql.org/) do  **PostgreSQL** , onde você deve clicar no botão de download dentro do banner no topo da página.

![Página inicial do PostgreSQL com o botão de download destacado com um retângulo vermelho](https://caelum-online-public.s3.amazonaws.com/1659-postgreSQL-Primeiros-passos-com-SQL/Transcri%C3%A7%C3%A3o/Aula+1/Imagens/home+postgreSQL+com+bot%C3%A3o+de+download+em+destaque.png)

Eu farei o download do Windows porque é o sistema operacional da nossa máquina, mas você deve baixar na opção de Linux ou Mac OS de acordo com o seu sistema operacional que você estiver utilizando.

Depois vou clicar em  *Download the installer* .

![Página de instalação do software PostgreSQL para Windows com uma seta vermelha apontando para o link ](https://caelum-online-public.s3.amazonaws.com/1659-postgreSQL-Primeiros-passos-com-SQL/Transcri%C3%A7%C3%A3o/Aula+1/Imagens/download_the_instaler.png)

Vai aparecer uma tabela com as opções de download de todas as versões disponíveis para cada sistema operacional. A versão que vamos utilizar é a 12.1, então vou clicar no botão de download dela na coluna do Windows.

![Tabela com os links para download do PostgreSQL com uma seta vermelha apontado para a versão 12.9 e destacando o botão de download](https://caelum-online-public.s3.amazonaws.com/1659-postgreSQL-Primeiros-passos-com-SQL/Transcri%C3%A7%C3%A3o/Aula+1/Imagens/tabela_download_versoes_postgre.png)

> **Atenção:** O PostgreSQL lançou novas versões após a gravação do curso. Para uma experiência mais próxima às demonstrações do intrutor, recomendamos que baixe a  ***versão 12.9*** .

Beleza! Vai abrir uma pasta para você iniciar o download do instalador. Eu já tenho aqui o arquivo, mas você pode baixar. Ele tem aproximadamente 200Mb e vai demorar um pouco para ser baixado, mas quando terminar a instalação, basta continuar seguindo o nosso tutorial.

Após baixar o instalador, vou na pasta de download e dou dois cliques no arquivo para começar a instalação. Ele fará o carregamento e, quando aparecer a tela inicial da instalação do programa, clique no botão " *Next* " (próximo) no canto inferior direito da janela para continuar a instalação.

No próximo eu vou instalar a versão 12 nesse diretório que já aparece na caixa de texto e clicar em " *Next* ."

Nessa janela aparecem marcadas todas as caixas de seleção com os componentes que podem ser instalados. O **PostgreSQL Server** e o **pgAdmin4** serão utilizados para fazermos as *queries* no banco de dados. O **Stack Builder** que nem é necessário, mas eu vou deixar aqui intalado porque ele facilita quaisquer instalações a mais que desejar fazer. E o **Command Line Tools** que é para fazer as execuções do sistema via linhas de comando. Mais uma vez clica em " *Next* ".

Essa janela mostra a pasta onde ficarão guardados os bancos de dados que criarmos. Mais uma vez clique em " *Next* ".

E vamos criar uma senha para o usuário postgre. Eu vou colocar " **postgres** " mesmo mas você pode colocar qualquer senha que escolher,  **só lembra de guardá-la** . Preencher as duas caixas de texto com a mesma senha e clique em " *Next* ".

A seguir aparece o pedido para selecionar o número da porta. A porta padrão que o postgre vai utilizar é a  **"5432"** , que já estará digitada no campo, então apenas clique em " *Next* ".

Aqui você deve colocar o *Default locale* (local padrão). Selecione **Portuguese, Brazil** e clique em " *Next* ".

Beleza! Agora é somente confirmar os dados, então clique em *Next* nesta janela e na próxima e ele já está fazendo a instalação. Esse processo também demora um pouco porque ele precisa extrair os dados do instalador e copiar todos eles para pasta de destino. Então vamos aguardar um pouco.

Quando ele terminou de instalar, ele vai para uma nova janela com uma caixa de seleção marcada para iniciar o  *Stack Builder* . Você pode desmarcar ela porque a gente não vai utilizar o  *Stack Bulder* , e clique em *Finish* (finalizar).

Tudo bem aqui. Terminamos a instalação e precisamos verificar se está tudo OK. Para isso abriremos o  *psql* , que é a linha de comando do  **PostgreSQL** .

Colocamos na barra de pesquisa do computador *psql* e o programa **SQL Shell (psql)** irá aparecer, então a gente clica para abrí-lo.

Assim que o **SQL Shell (psql)** abre, na primeira linha estará escrito  **Server [localhost]** . Você deve apertar "Enter" sequencialmente para navegar entre as pastas a seguir:

"Server [localhost]: > Database [postgres]: > Port [5432]: > Username [postgres]: > Password for user postgres:"

Ele vai pedir a senha, que no meu caso também é "postgres", mas você deve escrever a senha que você escolheu e apertar enter.

![Janela do SQL Shell (psql) com o caminho percorrido e algumas mensagens que aparecem após colocar a senha. São elas: a versão do psql, um aviso de erro em inglês, o comando para pedir ajuda, também em inglês, e, no final, ](https://caelum-online-public.s3.amazonaws.com/1659-postgreSQL-Primeiros-passos-com-SQL/Transcri%C3%A7%C3%A3o/Aula+1/Imagens/sql_shell.png)

Beleza! Estou conectado no banco. Já conseguimos fazer essa parte, esntão também vamos verificar como o **pgAdmin** está instalado. Vou digitar no buscador do computador "pgAdmin" e clicar para abrir o programa.

Ele vai carregar e abrir no seu navegador. Ele vai pedir para você colocar uma senha, que vou colocar novamente "postgres", mas poderia ser qualquer outra senha, e dar "OK".

Na coluna da esquerda ele tem os  *servers* . Geralmente clicando sobre a palavra " *Servers* " você verá carregado o "PostgreSQL 12" e, clicando sobre ele, você poderá ter acesso aos bancos já cadastrados.

![Janela com o pgAdmin aberta com um destaque na coluna da esquerda, onde tem os servers e o ](https://caelum-online-public.s3.amazonaws.com/1659-postgreSQL-Primeiros-passos-com-SQL/Transcri%C3%A7%C3%A3o/Aula+1/Imagens/pgAdmin.png)

Mas se não aparecer, clique com o botão direito em "*Servers* siga o caminho:

"Server > Create > Server... >"

Irá abrir uma nova janela onde, no campo "Name" você coloca um nome para o servidor. Vou colocar "PostgreSQL 12 Teste" porque é o que vai aparecer no meu caso, que já tem o "PostgreSQL 12". Depois você vai na aba " *Connection* " (Conexão) e, na opção " *Host name/address* ", coloca " *localhost* ", que é sua máquina padrão.

Na opção " *Port* " basta manter o "5432", assim como nas opções " *Maintenance database* " e em " *Username* " basta manter "postgres".

Já em " *Password* " você coloca a senha que escolheu. Aqui também é "postgres". E vou marcar a caixa de seleção para salvar a senha. Em seguida, vou clicar no botão " *Save* " no canto inferior direito da janela.

"![Janela de criação do servidor com a aba ](https://caelum-online-public.s3.amazonaws.com/1659-postgreSQL-Primeiros-passos-com-SQL/Transcri%C3%A7%C3%A3o/Aula+1/Imagens/janela_criacao_server.png)

Da mesma forma que conseguimos nos conectar ao *server* "12", conseguimos nos conectar também ao "12 teste". Então caso o de cima não apareça para você, basta criar um *server* para utilizar. No meu caso, eu vou excluir o que eu criei, porque não vou utilizar, e vou manter apenas o "PostgreSQL 12".

Para me conectar ao banco de dado, clique seguindo o caminho:

"Servers > PostgreSQL 12 > Databases > postgres"

Ao selecionar "postgres", clique em " ***Tools*** " na barra de comando no alto da janela e, em seguida, clique em "*Query Tool".

![Janela do pgAdmin com o mouse sobre a opção Query Tools](https://caelum-online-public.s3.amazonaws.com/1659-postgreSQL-Primeiros-passos-com-SQL/Transcri%C3%A7%C3%A3o/Aula+1/Imagens/janela_querytools.png)

Na coluna da esqueda irá carrgar um um arquivo com o nome "postgres/postgres@PostgreSQL 12" para informar que estou conectado ao banco de dados postgres.

No campo para escrever os códigos, eu posso digitar `SELECT NOW();` e depois clicar no botão "▶" na barra acima do nome do arquivo para executar o comando. abaixo da área em que o código é digitado.

![Arquivo com o código SELECT NOW() executado com o mouse sobre o botão executar. Uma seta vermelha aponta para o retorno do código](https://caelum-online-public.s3.amazonaws.com/1659-postgreSQL-Primeiros-passos-com-SQL/Transcri%C3%A7%C3%A3o/Aula+1/Imagens/resultado_selectnow_pgadmin.png)

É só um teste, ainda vamos aprender muito como isso funciona, mas é só para validar se você está no banco de dados. Esse comando mostra o horário em que estamos executando a  *query* .

A mesma coisa acontece se digitar `SELECT NOW();` na janela do **SQL Shell** e apertar "Enter" e ele vai mostrar o horário, provando que estamos conectados ao banco de dados.

![Janela do SQL Shell (psql) com o código SELECT NOW() executado e o resultado apontado por uma seta vermelha](https://caelum-online-public.s3.amazonaws.com/1659-postgreSQL-Primeiros-passos-com-SQL/Transcri%C3%A7%C3%A3o/Aula+1/Imagens/slectnow_shell.png)

Então estamos com o Postgre instalado e com o pgAdmin 4 instalado. Na próxima aula veremos como todos esses comando e itens funcionam. Até a próxima.

CONTINUAR LENDO
