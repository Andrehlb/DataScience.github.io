02
Listas e polimorfismo
PRÓXIMA ATIVIDADE

Play Video
Transcrição
[00:00] Vamos estudar outras implicações do uso de objetos com listas ou sequências em geral agora. Eu queria usar agora o conceito de herança e polimorfismo que aprendemos quando trabalhamos com orientação objetos.

[00:15] Vou adicionar uma célula de texto e anotar que estamos falando sobre #Herança e polimorfismo. Na prática, diferente de como eu fiz antes, quando criei a conta com atributos de uma maneira normal: self.código, self.saldo, agora eu vou criar com atributos privados, usando um underline.

[00:45] Para isso, vamos criar uma classe conta simples, class Conta:, com um código e um saldo, usando o underline para deixar privado.

class Conta:

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  def deposita(self, valor):
    self._saldo += valor

  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

Na hora de imprimir também usamos aqui o self._.Essa é a minha classe conta. Se eu quiser, posso imprimir uma conta que tem o ID oitenta e oito e saldo zero, então código 88 e saldo 0.

print(Conta(88))

[>>Codigo 88 Saldo 0<<]
COPIAR CÓDIGO
[01:15] Quero criar agora uma classe de conta corrente. Então a classe ContaCorrente herda da classe “Conta”: class ContaCorrente(Conta):. Toda vez que passa o mês, def passa_o_mes, vamos tirar dessa nossa conta dois reais, logo, self.saldo -= 2.

class ContaCorrente(Conta):

  def passa_o_mes(self):
    self._saldo -= 2

[01:36] Já a classe ContaPoupanca também herda da classe “Conta”, mas quando passa o mês, def passa_o_mes(self):, ela soma um pouquinho de dinheiro e perde um pouco de dinheiro. Primeiro, ela vai somar 1% do dinheiro que ela já tem, então eu estou multiplicando e somando, self._saldo *= 1.01, e depois eu vou tirar o quanto eu tenho que pagar todo mês que, no caso da ContaPoupanca, são 3 reais.

class ContaCorrente(Conta):

  def passa_o_mes(self):
    self._saldo -= 2

class ContaPoupanca(Conta):

  def passa_o_mes(self):
    self._saldo *= 1.01
    self._saldo -= 3

[02:13] Neste nosso exemplo, temos duas classes herdando de "Conta". A primeira tira só dois reais, a outra dá 1% do saldo e depois tira três reais toda vez que passa um mês. Podemos criar duas contas. A conta16,que é uma ContaCorrente de ID “16” e deposita mil reais: conta16.deposita(1000). Agora passamos o mês, passa_o_mes, e depois que passou o mês, imprimimos a conta16.

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

[>>Codigo 16 Saldo 998<<]


[02:50] O resultado é que a conta16 tem 998, porque tirou 2 reais. Agora faremos a mesma coisa com a conta17, só que ela é uma ContaPoupanca que depositou 1000 reais.

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

[>>Codigo 17 Saldo 1007.0<<]

[03:14] Então, a conta17 terminou com 1007 reais. Por enquanto, é o tradicional: você instanciou um objeto e só usou a herança para ter o construtor padrão da classe anterior, o direito ao método deposita, ter os atributos que foram inicializados no __init__, você teve tudo isso de acesso.

[03:35] Onde entra o polimorfismo? Na nossa lista, na nossa sequência. Se eu tenho uma lista de contas, a conta 16 e a 17, contas = [conta16, conta17]. Eu vou reinicializar essas duas contas para que fique claro para nós o que acontece todas as vezes.

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]

[03:57] Agora, eu quero passar por todas as contas (para onde?), então for conta in contas: e eu vou passar o mês, conta.passa_o_mes(). Não importa se dentro da lista eu tenho ContaCorrente ou ContaPoupanca, o que importa é que tenha o passa_o_mes().

for conta in contas:
  conta.passa_o_mes() # duck typing

Na prática, é o duck typing que vemos quando falamos de orientação objeto. Se ele responde como um pato, se ele faz “duck” como um pato, então eu posso pedir para ele fazer "duck".

[04:30] Então, se responde ao passa_o_mes(), então passa o mês, por favor. No meu caso, eu fiz de uma maneira simples que foi definir o método nas duas classes filhas. Quer dizer que a classe mãe não está definida nesse caso. Posso rodar e sempre que eu atualizar eu posso imprimir essa conta. Eu estou utilizando uma lista, poderia ser uma tupla, poderia ser o que for dentro da categoria sequência de contas iterável, e passando por elas para fazer isso.

[05:00] Então repare que temos os benefícios de polimorfismo através do uso de objetos em que podemos iterar, como uma lista, uma tupla ou qualquer outra coisa. Em geral, não vamos usar isso com tuplas dessa maneira, porque lembra que eu falei de tuplas? O uso recomendado em geral utilizado de tuplas é que cada posição tem um significado diferente. Do contrário, a lista passa por todos os elementos, porque eles devem ser tratados da mesma maneira.

[05:30] Então essa é a grande diferença muito comum de utilizarmos entre tuplas e listas, e por isso que eu estou trabalhando com lista nesse cenário.

03 Arrays e Numpy

[00:00] Eu comentei no passado que, no Python, vamos ter as listas e as tuplas. Naquele momento, na verdade, eu não falei das tuplas, mas eu comentei que às vezes usávamos o termo array como uma maneira genérica de dizer uma sequência de elementos que temos acesso aleatório, a posição 3, posição 5, posição 7. No Python existe o termo array, o tipo array, a diferença é que temos que importar.

[00:33] Eu vou definir aqui: “array, evitaremos usar”. Vamos evitar usar um array padrão do Python, o array padrão do Python é super específico. Então, vamos importar import array as arr e quando eu quero instanciar um array, então, arr.array(), sendo arruma abreviação que eu fiz. Então, eu falo qual o tipo de array que eu quero criar? Eu quero um tipo específico para números com ponto flutuante, que é o tipo d.

import array as arr

arr.array('d', [])

[01:05] E eu passo uma lista com os números, se eu estiver instanciando desta maneira o meu array. Por exemplo, o número um e o três vírgula cinco: [1, 3.5]. Desta maneira, vamos rodar e eu estou instanciando um array de verdade do Python.

import array as arr

arr.array('d', [1, 3.5])

array('d', [1.0. 3.5])
 
Se você procurar o array do Python, pesquisando no google “python documentation array”, você vai encontrar a informação, disponível neste link de que o array serve justamente para você ter uma eficácia maior quando estivermos trabalhando principalmente com números.

[01:40] Então o array do Python tem um tipo específico. Por que tem um tipo específico? Por que eu tive que falar o tipo do meu array? Porque no array do Python, se eu quiser criar um array, eu tenho que falar o tipo e todos os elementos têm que ser desse tipo. Se eu tentar colocar uma string aqui, arr.array('d', [1, 3.5, 'Guilherme']), não vai funcionar.

O motivo é que quando ele cria um array internamente, as arrays do Python - a palavra array que é um tipo de proposta - tipo array vai tentar armazenar os valores de uma maneira eficiente, vai tentar otimizar os processamentos em cima desses valores de uma maneira mais eficiente.

[02:10] Para o dia a dia usual do Python vamos usar as listas. Já em situações específicas, em que temos um conjunto bem pequeno de elementos onde cada posição indica uma coisa, é comum usar as tuplas. E onde costuma ser importante um alto desempenho de funções matemáticas com Python, é muito comum utilizarmos uma biblioteca do Python, a numpy.

[02:50] Portanto costumamos usar a numpy, disponível neste link. Não costumamos usar o array do Python, usamos o numpy Para isso, fazemos import numpy as np. se você não tiver o numpy instalado, precisa instalar, na linha de comando o que você faria seria um !pip install numpy. Eu estou instalando dentro de um Jupiter Notebook, então coloco a exclamação na frente.

[03:25] É comum que essa linha seja a primeira de todas no código, ficando na parte de cima, mas você vai perceber que o numpy, na verdade, já vem instalado no Google Colab, não precisa instalar. Mas, na sua máquina, talvez você queira dar um pip install numpy, ou no seu Jupiter Notebook, você talvez queira dar um !pip install numpy, esse comando mágico com exclamação.

[03:45] Continuando, fizemos import numpy as np, em seguida, faremos np.array() e eu passo a minha lista, [1, 3.5]. Eu tenho a minha lista, que é o meu array, agora do numpy, então isso aqui são os meus números, se eu quiser eu imprimo esses números e o numpy tem uma série de funções, que utilizamos principalmente quando estamos fazendo o Data Science,engenharia cientifica, programação científica, etc.

[04:15] Por exemplo, eu posso somar 3 nesses números, numeros + 3. Se eu somar 3, eu estou somando 3 nos dois elementos, que é uma única dimensão e etc. Então, o Python tem várias funcionalidades super úteis de otimização e de facilidade na escrita e interpretação do código. É muito mais comum que, quando você quer um desempenho alto na parte matemática, em utilização de arrays e matrizes, você vá para o mundo do numpy. Isso é mais comum do que ir para o mundo de arrays do próprio Python.

[04:45] Na prática, o array, em si, acabamos não usando. Vou anotar que # evitaremos usar array puro,se precisamos de trabalho numérico, é costume usar o numpy. Esse é o costume, não significa que é regra, 100% das vezes, mas é o que você vai ver todo mundo utilizando no mundo de Data Science, de ciência de dados é o numpy. Eu queria mostrar para vocês que existe a array nativa, existe a array que é um tipo, mas que chamamos de array e já vem com o Python, só que tem algumas restrições justamente para otimização.

[05:28] Mas quando vamos trabalhar com otimização, é muito mais comum trabalharmos com numpy, cada um tem o seu caso, é muito mais comum o numpy.

CONTINUAR LENDO
