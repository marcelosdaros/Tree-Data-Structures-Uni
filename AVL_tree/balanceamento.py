from profundidade import profundidade
from rotacao import *

def balancoAtual(self):
  if not self: return 0
  profundidade_nodo_esq = 0
  profundidade_nodo_dir = 0
  if self.esq:
    profundidade_nodo_esq = profundidade(self.esq)
  if self.dir:
    profundidade_nodo_dir = profundidade(self.dir)
  return profundidade_nodo_esq - profundidade_nodo_dir

def balancearArvore(self):
  balanco = balancoAtual(self)
  if balanco > 1 and balancoAtual(self.esq) >= 0:
    return rotacionarDireita(self)
  if balanco < -1 and balancoAtual(self.dir) <= 0:
    return rotacionarEsquerda(self)
  if balanco > 1 and balancoAtual(self.esq) < 0:
    self.esq = rotacionarEsquerda(self.esq)
    return rotacionarDireita(self)
  if balanco < -1 and balancoAtual(self.dir) > 0:
    self.dir = rotacionarDireita(self.dir)
    return rotacionarEsquerda(self)
  return self
  