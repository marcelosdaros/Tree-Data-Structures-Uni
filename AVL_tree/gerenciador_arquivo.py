import os

def montaCaminhoArquivo(nomeArquivo):
  diretorioArquivo = os.path.dirname(os.path.realpath('__file__'))
  return os.path.join(diretorioArquivo, nomeArquivo)

def buscaConteudoArquivo(nomeArquivo):
  caminhoRelativo = montaCaminhoArquivo(nomeArquivo)
  gerenciadorArquivo = open(caminhoRelativo)
  if gerenciadorArquivo == None: return gerenciadorArquivo
  conteudoArquivo = gerenciadorArquivo.read().split('\n')
  gerenciadorArquivo.close()
  return conteudoArquivo