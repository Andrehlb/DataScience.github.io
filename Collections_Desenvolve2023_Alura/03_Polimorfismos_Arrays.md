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