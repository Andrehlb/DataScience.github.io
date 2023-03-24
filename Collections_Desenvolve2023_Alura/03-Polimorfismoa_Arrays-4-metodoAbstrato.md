04
Método abstrato
PRÓXIMA ATIVIDADE

Play Video
Transcrição
[00:00] Eu queria só terminar com um refinamento pequeno do código que fizemos. Da mesma maneira que utilizamos o underline para fazer uma forçada de um atributo privado, na medida do possível, eu queria dar também uma olhada de quando forçamos aquela questão - não forçamos, na verdade, ainda - de que as classes filhas tivessem o passa_o_mes.

[00:20] Eu posso criar um tipo novo de conta, por exemplo, uma class ContaInvestimento(conta) que herda de “Conta” e que não tem o passa_o_mes. Não tem nada, só passa, não vai fazer nada, não tem código nenhum aqui dentro. Isso aqui funciona, não só funciona, como, se eu adicionar um código no meio, eu consigo criar uma ContaInvestimento(764), mesmo sem ter o passa_o_mes().

class ContaCorrente(Conta):

  def passa_o_mes(self):
    self._saldo -= 2

class ContaPoupanca(Conta):

  def passa_o_mes(self):
    self._saldo *= 1.01
    self._saldo -= 3

class ContaInvestimento(Conta):
  pass

ContaInvestimento(764)
COPIAR CÓDIGO
[00:50] Que seria estranho, porque eu gostaria, como criador da classe Conta, que todo mundo que herda da classe Conta tivesse o método passa_o_mes(). Portanto, o que eu queria era colocar o método passa_o_mes() e, de alguma maneira, jogar um erro do tipo NotImplementedError, caso você chame esse método.

class Conta:

  def __init__(self, codigo):
    self.codigo = codigo
    self.saldo = 0

  def deposita(self, valor):
      raise NotImplementedError 

  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)
COPIAR CÓDIGO
Então se você chamar esse método, eu vou dar um erro. Mas você só vai descobrir esse erro se chamar o método. Através de uma classe que não sobrescreveu o método.

[01:25] Só nesse instante você descobriria. O que podemos fazer? Nas últimas versões do Python, podemos dizer que eu não implemento esse método, dar um pass e podemos decorar com uma anotação, um decorator, dizendo que é um método abstrato, um @abstractmethod. Então, eu não estou implementando.

class Conta:

  def __init__(self, codigo):
    self.codigo = codigo
    self.saldo = 0

  def deposita(self, valor):
      self._saldo += valor

    @abstractmethod
    def passa_o_mes(sef)
      pass

  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)
COPIAR CÓDIGO
[01:45] Faltou importar o que eu tenho que importar. Para isso, eu faço from abc import ABCMeta, abstractmethod. Usamos o ABCmeta como uma meta classe, metaclass. É uma configuração que precisamos colocar: class Conta(metaclass=ABCMeta):. O abstractmethod já está no nosso código, mais abaixo.

from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):

  def __init__(self, codigo):
    self.codigo = codigo
    self.saldo = 0

  def deposita(self, valor):
      self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
      pass

  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)
COPIAR CÓDIGO
[02:15] Agora vou rodar o código, interpretou e vou tentar criar uma conta normal. Já deu erro, porque a classe Conta virou uma classe abstrata. Ela tem um método abstrato e não pode ser instanciada, porque ainda não implementaram todos os métodos abstratos, o método passa_o_mês().

[02:30] Agora, se eu criar essas 3 classes, tudo bem.

class ContaCorrente(Conta):

  def passa_o_mes(self):
    self._saldo -= 2

class ContaPoupanca(Conta):

  def passa_o_mes(self):
    self._saldo *= 1.01
    self._saldo -= 3

class ContaInvestimento(Conta):
  pass
COPIAR CÓDIGO
Porém, na hora que eu tentar instanciar uma ContaInvestimento, já dá erro. As outras classes funcionam, o que não funciona é aquilo que criamos sem implementar o método abstrato, esse é o único que não funciona.

[02:56] Então, a sacada é: se você tem um método que você quer definir na sua classe mãe e que todo mundo seja forçado a implementar, coloque um @abstractmethod nela, defina ela como uma classe abstrata através da meta classe ABCmeta.

[03:12] Então dessa maneira, forçamos para que o erro apareça na hora que você tem que instanciar, que é muito mais cedo do que o momento que você tenta chamar o método, porque você instancia em algum momento e os métodos só são chamados bem depois, não sabemos quando.

[03:30] Agora, se o erro acontecendo logo que você tentou instanciar, você consegue pegar mais cedo esse erro. Essa é a vantagem, quando eu tente instanciar eu já descobri que a classe não está completa. Então, eu queria refinar esse ponto do nosso código.

[03:46] Por fim, eu queria dizer se você tem interesse e quer aprender mais sobre o numpy, que usamos quando fazemos ciência de dados, temos os nosso cursos. Diversos cursos na área de ciência de dados em que vamos utilizar o numpy, só dar uma olhadinha e continuar os estudos por lá.

CONTINUAR LENDO
