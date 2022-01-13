from impressao import impressaoPercurso

#deve receber a raiz
def defineEncaminhamento(self, ordem):
  percurso = []
  if ordem == "preOrdem":
    percorreEsquerdaPreOrdem(self, percurso)
    impressaoPercurso(percurso, "preOrdem")
  elif ordem == "emOrdem":
    percorreEsquerdaEmOrdem(self, percurso)
    impressaoPercurso(percurso, "emOrdem")
  elif ordem == "posOrdem":
    percorreEsquerdaPosOrdem(self, percurso)
    impressaoPercurso(percurso, "posOrdem")

def percorreEsquerdaPreOrdem(self, percurso):
  percurso.append(self)
  if self.esq != None:
    percorreEsquerdaPreOrdem(self.esq, percurso)
  percorreDireitaPreOrdem(self, percurso)

def percorreEsquerdaEmOrdem(self, percurso):
  if self.esq != None:
    percorreEsquerdaEmOrdem(self.esq, percurso)
  percurso.append(self)
  percorreDireitaEmOrdem(self, percurso)

def percorreEsquerdaPosOrdem(self, percurso):
  if self.esq != None:
    percorreEsquerdaPosOrdem(self.esq, percurso)
  percorreDireitaPosOrdem(self, percurso)
  percurso.append(self)

def percorreDireitaPreOrdem(self, percurso):
  if self.dir != None:
    percorreEsquerdaPreOrdem(self.dir, percurso)
  
def percorreDireitaEmOrdem(self, percurso):
  if self.dir != None:
    percorreEsquerdaEmOrdem(self.dir, percurso)

def percorreDireitaPosOrdem(self, percurso):
  if self.dir != None:
    percorreEsquerdaPosOrdem(self.dir, percurso)

def percorreEsquerdaEmOrdemBuscaPorString(self, percurso, busca):
  if self.esq != None:
    percorreEsquerdaEmOrdemBuscaPorString(self.esq, percurso, busca)
  if self.valor.upper()[0] > busca[0]:
    return
  if self.valor.upper().startswith(busca):
    percurso.append(self)
  percorreDireitaEmOrdemBuscaPorString(self, percurso, busca)

def percorreDireitaEmOrdemBuscaPorString(self, percurso, busca):
  if self.dir != None:
    percorreEsquerdaEmOrdemBuscaPorString(self.dir, percurso, busca)

def percorreEsquerdaEmOrdemData(self, percurso, data1, data2):
  if self.esq != None:
    percorreEsquerdaEmOrdemData(self.esq, percurso, data1, data2)
  if (self.valor >= data1) and (self.valor <= data2):
    percurso.append(self)
  percorreDireitaEmOrdemData(self, percurso, data1, data2) 

def percorreDireitaEmOrdemData(self, percurso, data1, data2):
  if self.dir != None:
    percorreEsquerdaEmOrdemData(self.dir, percurso, data1, data2)
  