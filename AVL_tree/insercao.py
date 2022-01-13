from nodo import *
from profundidade import profundidade
from balanceamento import balancearArvore

def insere(raiz, nodo): 
  if not raiz:
    return nodo
  elif nodo.valor < raiz.valor:
    raiz.esq = insere(raiz.esq, nodo)
  else:
    raiz.dir = insere(raiz.dir, nodo)
  raiz = balancearArvore(raiz)
  return raiz
