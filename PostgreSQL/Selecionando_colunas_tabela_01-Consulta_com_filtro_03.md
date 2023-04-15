# 01**Selecionando colunas específicas da tabela**

## Descrição

Olá pessoal, tudo bem? Boas-vindas novamente.

Antes de aprendermos sobre os filtros, precisamos aprender outra coisa importante, que é a seleção de campos específicos do banco de dados.

Até o momento, nossas seleções incluíam todos os campos da tabela. Agora vamos descobrir como filtrar um campo e como atribuir um *alias* para ele.

Começaremos criando um registro no nosso banco de dados, porque na nossa última aula o deixamos vazio. Basta retornar no nosso código de `INSERT` e executá-lo novamente.

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
COPIAR CÓDIGO
```

Usando o `SELECT * FROM aluno;` notamos que os nossos dados foram incluídos na tabela.

Para retornar apenas os dados da coluna "nome", executamos o comando `SELECT nome FROM aluno;`, e assim veremos só os registros de nome. Se quisermos os resultados de mais campos, como "nome", "idade" e "matriculado_em", informamos esses campos, separados por vírgula, após o `SELECT`.

```sql
SELECT nome,
       idade,
       matriculado_em
    FROM aluno;
```

A partir dessa seleção, podemos usar o comando  **`AS`** , ou seja, um  *alias* , para trocar o nome de exibição dos campos na tabela. Se escrevermos `SELECT matriculado_em AS quando_se_matriculou`, essa coluna aparecerá com o nome " **quando_se_matriculou** ".

O *alias* também pode ser usado para atribuir nomes com espaço para os campos, o que pode ser útil, por exemplo, para elaborar um relatório. Nesses casos, os novos nomes precisam estar entre aspas duplas  **`" "`** , ou o programa não irá reconhecê-los e aparecerá uma mensagem de erro de sintaxe.

```vbnet
SELECT nome AS "Nome do Aluno",
       idade,
       matriculado_em AS quando_se_matriculou
    FROM aluno;
```

![Retorno da tabela com os campos selecionados e os nomes alterados com o alias em destaque](https://caelum-online-public.s3.amazonaws.com/1659-postgreSQL-Primeiros-passos-com-SQL/Transcri%C3%A7%C3%A3o/Aula+3/Imagens/alterando_nome_com_as.png)

Essa foi uma dica rápida para aprendermos sobre o  *alias* . Na próxima aula conheceremos os filtros.
