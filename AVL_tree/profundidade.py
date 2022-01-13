def profundidade(self):
  if not self: return 0
  profundidade_nodo_esq = 0
  profundidade_nodo_dir = 0
  if self.esq:
    profundidade_nodo_esq = profundidade(self.esq)
  if self.dir:
    profundidade_nodo_dir = profundidade(self.dir)
  return 1 + max(profundidade_nodo_esq, profundidade_nodo_dir)
