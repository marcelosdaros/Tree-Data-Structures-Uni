from encaminhamento import percorreEsquerdaEmOrdemBuscaPorString
from encaminhamento import percorreEsquerdaEmOrdemData
from impressao import impressaoPercurso
from convert_data import *

def buscaNodo(raiz, valor):
  if raiz == None:
    return "Valor não encontra-se na árvore"
  num = valor
  if raiz.valor == num:
    return raiz
  elif num < raiz.valor:
    return buscaNodo(raiz.esq, valor)
  elif num > raiz.valor:
    return buscaNodo(raiz.dir, valor)

def buscaPessoaPorCPF(raiz, valor, gerenciadorListaPessoas):
  teste = buscaNodo(raiz, valor)
  if teste != "Valor não encontra-se na árvore":
    gerenciadorListaPessoas.listaGeral[teste.indexPessoa].imprime()
  else:
    print("Não foi encontrada nenhuma pessoa com o CPF inserido.")

def buscaPessoasPorString(self, busca):
  pessoas = []
  percorreEsquerdaEmOrdemBuscaPorString(self, pessoas, busca)
  if len(pessoas) > 0:
    impressaoPercurso(pessoas, "emOrdemBuscaPorString")
  else:
    print("Não foram encontradas pessoas cujos nomes iniciam com os caracteres inseridos.")
  return pessoas

def buscaIntervaloPorData(self,data1,data2):
  pessoas = []
  data1 = convertData(data1)
  data2 = convertData(data2)
  if data1 > data2:
    aux = data1
    data1 =int (data2)
    data2 =int (aux)
  percorreEsquerdaEmOrdemData(self, pessoas, data1, data2)
  if len(pessoas)== 0:
    print ("Não foram encontradas pessoas que nasceram no intervalo de data inserido.")

  return pessoas