from balanceamento import balancearArvore

def removeNodo(raiz, valor):
  if not raiz:
    return raiz
  elif valor < raiz.valor:
    raiz.esq = removeNodo(raiz.esq, valor)
  elif valor > raiz.valor:
    raiz.dir = removeNodo(raiz.dir, valor)
  else:
    if not raiz.esq:
      auxiliar = raiz.dir
      raiz = None
      return auxiliar
    elif not raiz.dir:
      auxiliar = raiz.esq
      raiz = None
      return auxiliar
    auxiliar = achaMaiorValor(raiz.esq)
    raiz.valor = auxiliar.valor
    raiz.indexPessoa = auxiliar.indexPessoa
    raiz.esq = removeNodo(raiz.esq, auxiliar.valor)
  if not raiz:
    return raiz
  return balancearArvore(raiz)

def achaMaiorValor(raiz):
  if raiz == None or raiz.dir == None:
    return raiz
  return achaMaiorValor(raiz.dir)