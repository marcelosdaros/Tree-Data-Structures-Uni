from convert_data import *
from pessoa import *

class GerenciadorListaPessoas:
  def __init__(self):
    self.listaGeral = []

  def inserePessoa(self, dadosPessoa):
    codData = convertData(dadosPessoa[3])
    novaPessoa = Pessoa(dadosPessoa[0], dadosPessoa[1], dadosPessoa[2], dadosPessoa[3], dadosPessoa[4],codData)
    self.listaGeral.append(novaPessoa)
    return self.listaGeral.__len__() - 1
  
  def imprimeLista(self):
    for pessoa in self.listaGeral:
      pessoa.imprime()
  
  def imprimeListaSelecionados(self, listaSelecionados):
    print("\nDados de cada pessoa:")
    for pessoa in listaSelecionados:
      self.listaGeral[pessoa.indexPessoa].imprime()