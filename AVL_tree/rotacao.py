def rotacionarEsquerda(self):
  self.valor, self.dir.valor = self.dir.valor, self.valor
  self.indexPessoa, self.dir.indexPessoa = self.dir.indexPessoa, self.indexPessoa
  antiga_esq = self.esq
  self.atualizaElementos(self.dir, self.dir.dir)
  self.esq.atualizaElementos(antiga_esq, self.esq.esq)
  return self

def rotacionarDireita(self):
  self.valor, self.esq.valor = self.esq.valor, self.valor
  self.indexPessoa, self.esq.indexPessoa = self.esq.indexPessoa, self.indexPessoa
  antiga_dir = self.dir
  self.atualizaElementos(self.esq.esq, self.esq)
  self.dir.atualizaElementos(self.dir.dir, antiga_dir)
  return self
  