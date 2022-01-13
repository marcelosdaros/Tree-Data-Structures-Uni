class Nodo:
  def __init__(self, valor, indexPessoa):
    self.valor = valor
    self.indexPessoa = indexPessoa
    self.esq = None
    self.dir = None

  def atualizaElementos(self, esquerda, direita):
    self.esq = esquerda
    self.dir = direita
