# 04**Tupla de objetos e lista de tuplas**

## Descrição

[00:00] No mundo real, acabamos trabalhando com uma mistura de tudo: tuplas, listas, objetos, tudo misturado à medida do necessário. Então eu poderia ter a representação de usuários através de tuplas. Nós fizemos a variável guilherme e daniela. Eu poderia falar que "usuários" é uma lista de guilherme e daniela, isto é, uma lista de tuplas.

```bash
usuarios = [guilherme, daniela]
usuarios

[('Guilherme', 37, 1981), ('Daniela', 31, 1987)]
COPIAR CÓDIGO
```

Vai ocorrer erro na sintaxe, porque as strings 'Andrhelb' e 'Rafa' precisam estar entre aspas, caso contrário o Python irá interpretá-las como variáveis.

```

usuarios = ['Andrhelb', 'Rafa']

usuarios

[('Andrhelb', 37, 1981), ('Rafa', 31, 1987)]
```

```
[('Andrhelb', 37, 1981), ('Rafa', 31, 1987)]
```

Se eu quiser criar essa lista a partir da lista original `usuarios`, posso fazer uso de uma **compreensão de lista**, onde a cada elemento da lista original é adicionada uma tupla contendo o nome do usuário, sua idade (calculada subtraindo seu ano de nascimento do ano atual) e o ano de nascimento:

```
from datetime import dateusuarios = ['Andrhelb', 'Rafa']
ano_atual = date.today().year
usuarios = [(u, ano_atual - 1981 if u == 'Andrhelb' else ano_atual - 1987, 1981 if u == 'Andrhelb' else 1987) for u in usuarios]
```

A compreensão de lista acima, usei a biblioteca `datetime` para obter o ano atual. 

Além disso, assumi que o ano de nascimento da pessoa com o nome 'Andrhelb' era 1981 e da pessoa com o nome 'Rafa' era 1987. Esses valores podem ser atualizados conforme necessário.

[00:30] Eu estou misturando as duas coisas, o “usuario” é uma tupla, que é o nome, idade, ano de nascimento. Então, eu tenho uma lista com todos os meus usuários. Usei uma lista para representar todos os meus usuários, porque eu decidi que, com o passar do tempo do meu sistema, eu vou ter usuários novos.

[00:50] Por exemplo, `usuarios.append()` o Paulo. Como eu representaria o Paulo? Estamos usando tupla para representar o usuário de uma maneira curta, rápida e que faz sentido nesse contexto.

[01:02] Portanto, nesse contexto, eu representaria com o nome do Paulo, a idade dele e o ano de nascimento dele, `usuarios.append(('Paulo', 39, 1979))`. Ao rodar, teremos o novo usuário.

```go
usuarios.append(('Paulo', 39, 1979))
usuarios
COPIAR CÓDIGO
```

A lista "usuários" é mutável, significa que eu posso adicionar elementos novos dentro, portanto, faz sentido que o "usuários" seja uma lista. Se o meu usuário é imutável, ou se em determinado contexto fez sentido que eu o representasse através de uma tupla por qualquer outro motivo, então, ele está aqui representado através de uma tupla.

```css
usuarios 

[('Guilherme',37,1981), ('Daniela',31,1987), ('Paulo',39,1979)]
COPIAR CÓDIGO
```

[01:35] Nesse cenário, repare que em `usuarios[0]`, o zero é o valor da tupla `(Guilherme, 37, 1981)`. Como é uma tupla, eu não consigo alterar o valor. Se eu quiser pegar a posição 0, que é o Guilherme, e alterar para “Guilherme Silveira”, `usuarios[0][0] = 'Guilherme Silveira'`, eu não posso, porque é uma tupla e tupla não altera valor.

[02:10] Ou seja, não podemos alterar o valor de dentro de uma tupla, a referência que a tupla está fazendo. Portanto, eu mostrei uma lista de tuplas, será que o contrário também acaba aparecendo? Sim, em algumas situações. Temos, por exemplo, a `conta_do_gui`, que é uma `ContaCorrente` e a conta do Gui tem 500 reais, `conta_do_gui.deposita(500)`, e tínhamos a `conta_da_dani`.

```makefile
conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
conta_da_dani = ContaCorrente(234876)
conta_da_dani.deposita(1000)
COPIAR CÓDIGO
```

[02:55] A `conta_da_dani` é uma `ContaCorrente` que eu tinha colocado um número aleatório, vou ser sincero. Nós temos duas contas, mas imagine que eu estou fazendo o processamento de um relatório onde as contas, não é que estão adicionando e removendo contas, não! As contas são essas e acabou, ninguém toca na quantidade de contas bancárias que eu tenho no meu relatório.

[03:22] Se ninguém toca nisso, ninguém pode adicionar, ninguém pode remover conta nova da minha lista de contas - e eu estou usando o termo lista de uma maneira genérica, que utilizamos no dia a dia, de lista de mercado - não posso adicionar nem remover nada, então, eu posso representar as minhas contas com uma tupla: `contas = (conta_do_gui, conta_da_dani)`. Eu posso fazer isso. E, desta maneira, terei uma tupla de objetos.

```makefile
conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
conta_da_dani = ContaCorrente(234876)
conta_da_dani.deposita(1000)

contas = (conta_do_gui, conta_da_dani)

contas

(<--main__.ContaCorrente at 0x7fabla56908>,
 <__main__.ContaCorrente at 0x7fabla56240>,
COPIAR CÓDIGO
```

[03:50] O `contas` apresentará dois objetos com a representação que mostra o possível endereço de memória, ou uma variável similar e mostra que são dois objetos diferentes. Será que eu consigo alterar esses valores?

Para isso, faremos `for conta in contas:`. Na linha seguinte, `print(conta)`. Repare que a primeira conta tem saldo 500 e a segunda 1000, e contas é uma tupla. Se é uma tupla, eu não consigo " *appendar* " qualquer coisa, `contas.append(423768)`, porque não existe um método que é um atributo `append()`.

```csharp
AttributeError: 'tuple' object has no attribute 'append'
COPIAR CÓDIGO
```

[04:38] Então, não dá para " *appendar* " nada, não dá para alterar a tupla. Mas repare que a tupla está referenciando dois objetos e o objeto da tupla, o `contas[0]` (que é a `conta_do_guilherme`) é um objeto mutável. Por mais que a tupla não possa ser mudada, e considerando que ela começou referenciando dois objetos, ela vai continuar referenciando esses dois, não importa o que aconteça, ela está referenciando eles.

[05:10] O que pode acontecer é alguém, manualmente, alterar o valor do objeto. A tupla continua referenciando o valor dos dois objetos. Se alguém alterou um valor que era referenciado pela referência da tupla, ela não tem nada a ver com isso. Ela só não deixa você adicionar ou remover elementos dela, nessa situação específica que eu estou dizendo, diferenciando o nosso uso.

[05:45] Então se eu fizer agora aquele mesmo `for`, você perceberá que o valor da primeira conta foi alterado, mas a tupla continua a mesma, ela continua referenciando os mesmos dois lugares.

```less
for conta in contas: 
  print(conta)

[>>Codigo 15 Saldo 800<<]
[>>Codigo 234876 Saldo 1000<<]
COPIAR CÓDIGO
```

Note que eu só usei a tupla com a característica de ser imutável. Foi o único motivo para usar a tupla aqui.

[06:10] A tupla não costuma ser usada nesses cenários. É mais comum que ela seja usada naquele cenário que eu tinha dito antes, quando você tem uma sequência em que cada posição quer dizer uma coisa diferente, isto é, as posições têm significado. Aqui, da maneira que eu usei, não tem significado, poderia ser `(conta_da_dani, conta_do_gui)`, `(conta_do_gui, conta_da_dani)`, quantas contas fossem, em uma ordem ou outra, de ponta cabeça, são as contas do banco.

[06:37] Eu usei a tupla só para ter a imutabilidade, ela não costuma ser usada dessa maneira, mas eu queria mostrar que existe a mistura, você pode colocar objeto dentro de tupla, lista dentro de tupla, tupla dentro de lista, objeto dentro de lista, pode fazer um mix e esse mix traz consequências. Precisamos sempre pensar que: a tupla não vai mudar de tamanho, mas quem está dentro pode mudar as referências de dentro. É isso que precisamos considerar quando pensamos sobre as tuplas.
