from impressao import *

def percorreEsquerdaEmOrdem(self, percurso):
  if self.esq != None:
    percorreEsquerdaEmOrdem(self.esq, percurso)
  percurso.append(self)
  percorreDireitaEmOrdem(self, percurso)

def percorreDireitaEmOrdem(self, percurso):
  if self.dir != None:
    percorreEsquerdaEmOrdem(self.dir, percurso)

def buscaData(data1,data2):
    percorreEsquerdaEmOrdem(self, percurso)
    impressaoPercurso(percurso, "emOrdem")


def impressaoData(self, ordem):
  i = 0
  while i < self.__len__() and self != None:
    if (i+1 == self.__len__()) and self[i] != None:
      if(self<=data1 && self>=data2:
        print(self[i].valor, end="\n")
    elif self[i] != None:
      if(self<=data1 && self>=data2:
        print(self[i].valor, end="\n")
    
    i+=1
    return self