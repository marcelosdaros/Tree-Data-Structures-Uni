def impressaoPercurso(self, ordem):
  if ordem == "preOrdem":
    print("Percurso em pré ordem:", end=" ")
  elif ordem == "emOrdem":
    print("Percurso em ordem:", end=" ")
  elif ordem == "posOrdem":
    print("Percurso em pós ordem:", end=" ")
  elif ordem == "emOrdemBuscaPorString":
    print("Nomes que começam com os caracteres inseridos:", end=" ")
    impressaoBuscaPessoasPorString(self)
    return
  elif ordem == "emOrdemBuscaData":
    print("As pessoas que nasceram no intervalo de data inserido:", end=" ")
    impressaoIntervaloData(self)
    return
  i = 0
  while i < self.__len__() and self != None:
    if (i+1 == self.__len__()) and self[i] != None:
      print(self[i].valor, end="\n")
    elif self[i] != None:
      print(self[i].valor, end=", ")
    i+=1

def impressaoBuscaPessoasPorString(self):
  i = 0
  while i < self.__len__() and self != None:
    if (i+1 == self.__len__()) and self[i] != None:
      aux = self[i].valor.split(" ")
      aux.pop()
      aux = ' '.join(aux)
      print(aux, end="\n")
    elif self[i] != None:
      aux = self[i].valor.split(" ")
      aux.pop()
      aux = ' '.join(aux)
      print(aux, end=", ")
    i+=1

def impressaoIntervaloData(self):
  i = 0
  while i < self.__len__() and self != None:
    if (i+1 == self.__len__()) and self[i] != None:
      aux = self[i].valor.split(" ")
      aux.pop()
      aux = ' '.join(aux)
      print(aux, end="\n")
    elif self[i] != None:
      aux = self[i].valor.split(" ")
      aux.pop()
      aux = ' '.join(aux)
      print(aux, end=", ")
    i+=1

def impressaoBuscaNodo(self):
  impressao = ""
  if self.esq == None and self.dir == None:
    impressao += "O número procurado encontra-se na árvore e é um nó folha, valor = " + str(self.valor)
  else:
    impressao += "O número procurado encontra-se na árvore: valor = " + str(self.valor)
  if self.esq != None:
    impressao += ", filho sub-árvore esquerda = " + str(self.esq.valor)
  else:
    impressao += ", não possui sub-árvore à esquerda"
  if self.dir != None:
    impressao += ", filho sub-árvore direita = " + str(self.dir.valor)
  else:
    impressao += ", não possui sub-árvore à direita"
  return impressao

def imprimeArvore(raiz, nivel=0) :
  if raiz == None: return
  if raiz.dir:
    imprimeArvore(raiz.dir, nivel+1)
  identacao = ''
  for x in range(nivel):
    identacao += '  '
  print (identacao + str(raiz.valor))
  if raiz.esq:
    imprimeArvore(raiz.esq, nivel+1)

