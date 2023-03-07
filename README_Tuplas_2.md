[Python Collections parte 1: listas e tuplas](https://cursos.alura.com.br/course/python-collections-listas-e-tuplas)

AULA02 - Tuplas

* 2. Listas com objetos de classes | 10min

  ## Transcrição

  [00:00] Continuando o trabalho das nossas listas, eu vou separar agora, na verdade, uma seção de textos, em que vamos trabalhar agora com objetos próprios, isto é `#Objetos próprios`. Eu digo próprios de classes que nós mesmos vamos construir, então eu quero criar uma classe para que trabalhemos com ela de exemplo nessa próxima utilização de uma lista.

  [00:26] Então vou criar uma classe que representa uma “Conta Corrente”: `class ContaCorrente:`. Essa classe, quando eu inicializo uma `ContaCorrente`, na construção da nossa `ContaCorrente`, recebemos o `self`, como quando criamos uma classe em Python.


  ```Python
  class ContaCorrente: 

    def__init__(self, )
  ```

  A função `__init__`, a palavra " **init** " é o nome correto do método especial que é chamado automaticamente quando um objeto é criado a partir de uma classe, para inicializar seus atributos.

  o método `__init__` deve ter parênteses vazios após o nome "init"

  Vamos receber também o código da conta, `codigo` para descobrirmos, por exemplo, se essa conta é a conta 15, a 37, seja qual for. Logo, `self.codigo = codigo`.

  ```python
  class ContaCorrente: 

    def__init__(self, codigo):
        self.codigo = codigo
  ```

  Eu também vou inicializar o saldo da conta, isto é, quanto eu tenho de dinheiro: `self.saldo = 0`.

  ```python
  class ContaCorrente: 

    def__init__(self, codigo):
        self.codigo = codigo
          self.saldo = 0
  ```

  [01:02] O que mais eu vou ter na minha conta? A minha conta vai permitir que eu deposite, então, `def deposita(self, valor):`, recebe o `self` e o `valor`. Mas o que o deposita vai fazer? Vai aumentar o saldo: `self.saldo += valor`.

  ```Python
  class ContaCorrente: 

    def__init__(self, codigo):
        self.codigo = codigo
          self.saldo = 0

      def deposita(self, valor):
        self.saldo += valor
  ```

  Então, podemos utilizar a `ContaCorrente` para adicionar algum saldo e testar o resultado. Eu vou definir também um método com a representação em forma de *string* dessa nossa classe, ou, no caso, de um objeto dessa classe.

  [01:32] A representação de string é: `def__str__(self):`. Em seguida, vou devolver essa  *string* , `return ""`, e dentro dos parênteses vou colocar `[Codigo {} Saldo {}]` ("código" e vou substituir pelo código; "saldo" e vou substituir pelo saldo).

  ```Python
  class ContaCorrente: 

    def__init__(self, codigo):
        self.codigo = codigo
          self.saldo = 0

      def deposita(self, valor):
        self.saldo += valor

      def__str__(self):
        return "[codigo {} saldo {}]"

  ```

  Para sinalizar que isso é o nosso objeto, vou colocar uns símbolos de maior `>>` e menor `<<` para ficar bem claro que isso é o nosso objeto. Vou formatar essa *string* com as variáveis `self.codigo` e `self.saldo`.

  ```Python
  def__str__(self):
    return "[>>codigo {} saldo {}<<]".format(self.codigo, self.saldo)

  ```

  [02:05] Portanto, vamos substituir as duas chaves pelo código e pelo saldo. Estamos utilizando a **introdução de orientação objetos**, que nós estudamos nos cursos de Python - nos dois cursos iniciais de orientação a objetos. Aprendemos **o que define uma classe, um construtor, um método e uma representação de  *string*** . Se eu não errei nada no código, ele vai rodar, interpretar e definir a classe e podemos criar a `conta_do_gui`.

  [02:31] A `conta_do_gui` é uma `ContaCorrente()`, cujo código é `15`. Se eu quiser imprimir a `conta_do_gui`, eu deveria imprimir um saldo 0. Portanto, “Shift + Enter”, e não deveria ter saldo, só que a impressão aqui vai mostrar: código 15, saldo 0, e o motivo é ter pego a representação de *string* deste objeto.

  ```Python
  conta_do_gui = ContaCorrente(15)
  print(conta_do_gui)

  [>>Codigo 15 Saldo 0<<]

  ```

  [02:55] Agora eu poderia depositar alguma coisa nessa conta, então, `conta_do_gui.deposita(500)`, e, de novo, `print(conta_do_gui)`. Vamos conferir quanto imprime agora. Estamos chamando a representação de  *string* , vai imprimir código 15, saldo 500.

  ```Python
  conta_do_gui.deposita(500)
  print(conta_do_gui)

  [>>Codigo 15 Saldo 500<<]

  ```

  Está funcionando. Até aí, temos a orientação a objetos. O que eu queria, é: trabalhar com contas dentro de uma lista.

  [03:20] Então, vamos criar também a `conta_da_dani`. A Dani tem uma `ContaCorrente()`. A conta dela é o número `47685`. E a conta da Dani deposita mil reais, `conta_da_dani.deposita(1000)`. Se eu imprimir a `conta_da_dani`, não teremos surpresas: mil reais e conta 47.685.

  ```bash
  conta_da_dani = ContaCorrente(47685)
  conta_da_dani.deposita(1000)
  print(conta_da_dani)
  Python
  [>>Codigo 47685 Saldo 1000<<]

  ```

  O que eu posso fazer agora é criar uma lista. Essa minha lista de contas tem a referência para essas duas contas, para esses dois objetos: uma para a `conta_do_gui` e a outra para a `conta_da_dani`. Isto é, `contas = [conta_do_gui, conta_da_dani]`.

  [03:52] Vamos imprimir as contas usando `print(contas)`. Ao imprimir, vamos ver que funciona uma lista com as contas, o problema é que na hora de imprimir a representação da minha lista, ele não chama, por padrão, o método `str`.

  ```Python
  contas = [conta_do_gui, conta_da_dani]
  print(contas)

  [<__main__.ContaCorrente object at 0x7fabla6d40>, <__main__.ContaCorrente object at 07fabfla6db70>]

  ```

  O que eu queria fazer aqui era apenas explicar que temos duas contas e o interessante do valor padrão é que ele mostra que são objetos distintos, porque dá para notar que um objeto está na posição de memória `7fabf1a6d940`, e outro na `7fab1f1`, ou seja, em outra posição de memória.

  [04:32] De fato, são dois objetos distintos nessa representação. Continuando, podemos fazer `for conta in contas:`, e na linha seguinte `print(conta)`. Lembre-se que o print de um objeto específico vai chamar representação de *string* dele. A representação de *string* da `conta_do_gui` é `15` e `500`, da Dani é `47685` e `1.000`.

  ```shell
  contas = [conta_do_gui, conta_da_dani]
  for conta in contas:
    print(conta)

  [>>Codigo 15 Saldo 500<<]
  [>>Codigo 47685 Saldo 1000<<]
  COPIAR CÓDIGO
  ```

  [04:55] Então, listas de objetos funcionam normalmente, assim como esperávamos quando estávamos trabalhando com as listas de valores do tipo inteiro. Poderia ser ponto flutuante ou string, lista de listas, enfim, trabalhamos com a lista que quisermos. Qual é o cuidado que precisamos tomar? Com a mutabilidade.

  [05:20] O que acontece se eu criar uma nova lista de contas, onde eu coloco a `conta_do_gui`, a `conta_da_dani` e a `conta_do_gui` de novo? Agora eu tenho 3 contas, e eu tenho que a `contas[0]` é a referência da primeira posição da nossa lista, que referencia quem referenciava a `conta_do_gui`, que é aquela conta de código `15` e saldo `500`.

  ```bash
  contas = [conta_do_gui, conta_da_dani, conta_do_gui]

  print(contas[0])

  [>>Codigo 15 Saldo 500<<]
  COPIAR CÓDIGO
  ```

  [05:49] O que acontece se eu depositar 100 reais na `conta_do_gui`? Vamos fazer aquele nosso `print(contas[0])` de novo e vamos ter como resultado que o `contas[0]` aumentou para 600 reais, Assim como a `conta_do_gui`.

  ```scss
  conta_do_gui.deposita(100)

  print(contas[0])

  [>>Codigo 15 Saldo 600<<]

  print(conta_do_gui)
  COPIAR CÓDIGO
  ```

  [06:11] Nós só criamos um objeto - na verdade criamos dois. Criamos um objeto quando instanciamos, quando chamamos o construtor. Quantas vezes eu chamei o construtor de ContaCorrente? Somente duas contas existem na memória, eu não criei várias contas, eu criei só duas, a do Gui e a da Dani.

  [06:45] A do Gui é referenciado pela variável `conta_do_gui`. Já a da Dani é referenciada pela variável `conta_da_dani`. No momento em que eu crio uma lista, uma array - uma sequência, essa minha lista - em que a casa 0 referencia quem referenciava a `conta_do_gui`, eu não estou criando objetos novos, eu só estou referenciando aquele objeto que já existia. Portanto, aquele objeto que já existia agora tem duas referências, tanto o `contas[0]`, quanto `conta_do_gui`.

  [07:22] A `conta_da_dani` está referenciando um objeto que tem duas referências: a `conta_da_dani` e a `contas[1]`, ambas referenciando o mesmo objeto. Quer dizer que eu tenho duas referências para um e duas para outro.

  Porém, encontramos outro `conta_do_gui`.

  ```ini
  contas = [conta_do_gui, conta_da_dani, conta_do_gui]
  COPIAR CÓDIGO
  ```

  Então o `contas[2]`, quer dizer, `print(contas[2])`, também é uma referência para `conta_do_gui`, para o mesmo objeto que está sendo referenciado pela `conta_do_gui`, portanto, seu saldo também é 600, já que eu só tenho dois objetos na memória.

  ```scss
    print(conta_do_gui)

  [>>Codigo 15 Saldo 600<<]

    print(contas[2])

  [>>Codigo 15 Saldo 600<<]
  COPIAR CÓDIGO
  ```

  [07:55] Então a maneira de interpretarmos deve ser sempre: ao colocarmos objetos numa lista, não devemos instanciar esses objetos. Assim como passar parâmetros para métodos, não instância objetos. Só instanciamos um objeto novo de verdade quando chamamos o "construção" dele, a "instanciação". Quando construimos com `ContaCorrente()`, então, criamos uma conta corrente.

  [08:15] Então eu só criei duas, mas eu posso ter quantas referências eu quiser. O perigo de ter muitas referências é que você pode, de novo, perder o controle se o objeto é mutável. Alguém pode chegar e falar `contas[2].deposita(300)`. No momento em que a pessoa fez `contas[2].deposita(300)`, o nosso `print(conta_do_gui)` reflete isso, porque é uma referência para o mesmo objeto, então, temos 900 reais agora dentro desse objeto.

  ```scss
  print(conta_do_gui)

  [>>Codigo 15 Saldo 900<<]
  COPIAR CÓDIGO
  ```

  [08:45] Esses são cuidados que precisamos tomar quando trabalhamos com listas por causa da mutabilidade dos objetos. Devemos lembrar sempre que temos referência para os objetos, se estes objetos são mutáveis, podem mudar ali dentro, existem alguns cuidados que precisamos tomar. Às vezes é exatamente isso que queremos, às vezes não queremos que sejam mutáveis, que possam mudar o valor lá dentro, vai depender do que você quer.
* [03Tuplas, objetos e
  anemia16min](https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/52940)
* [04Tupla de objetos
  e lista de tuplas08min](https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/52941)
* [05Diferenciando
  tupla e lista](https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/54401)
* [06Faça como eu fiz
  na aula](https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/54403)
* [07O que aprendemos?](https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/54402)

 OUTROS LINKS

 [Discord Alura](https://discord.gg/SK9bj7hEYD) [Fórum do curso](https://cursos.alura.com.br/forum/curso-python-collections-listas-e-tuplas/todos)[Voltar para
 Dashboard](https://cursos.alura.com.br/dashboard)

MODO NOTURNO

[![Gravatar de André Luiz Barbosa]()](https://cursos.alura.com.br/user/andrehlbarbosa)

[André Luiz Barbosa22.3k xp](https://cursos.alura.com.br/user/andrehlbarbosa)

From
 [[https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/54529](https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/54529)](%5Bhttps://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/54529%5D(https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/54529))
