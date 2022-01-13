from typing import Counter
from nodo import *
from consulta import buscaPessoaPorCPF
from consulta import buscaPessoasPorString
from consulta import buscaIntervaloPorData
from encaminhamento import defineEncaminhamento
from remocao import removeNodo
from impressao import *
from insercao import insere
from pessoa import *
from gerenciador_arquivo import buscaConteudoArquivo
from gerenciador_lista_pessoas import *
from convert_data import *

global raizCPF
global raizNome
global raizDataNasc
raizCPF = None
raizNome = None
raizDataNasc = None

global gerenciadorPessoas
gerenciadorPessoas = GerenciadorListaPessoas()

conteudo = buscaConteudoArquivo('dados_pessoas.csv')

if not conteudo: print('Não foram encontrados dados no arquivo informado')

for linha in conteudo:
  dadosPessoa = linha.split(';')
  index = gerenciadorPessoas.inserePessoa(dadosPessoa)

  nodoCPF = Nodo(dadosPessoa[0], index)
  raizCPF = insere(raizCPF, nodoCPF)

  nodoNome = Nodo(str(dadosPessoa[2]) + " " + str(index), index)
  raizNome = insere(raizNome, nodoNome)

  nodoDataNasc = Nodo(int(convertData(dadosPessoa[3])), index)
  raizDataNasc = insere(raizDataNasc, nodoDataNasc)

print("* AVL por CPF *\n")
imprimeArvore(raizCPF)
print("\n* AVL por nome *\n")
imprimeArvore(raizNome)
print("\n* AVL por data de nascimento *\n")
imprimeArvore(raizDataNasc)
print("")

textoMenu = "Informe a função desejada no seguinte formato <inicial da funcao>:\nFunções:\n[c] Busca pessoa por CPF\n[n] Busca pessoas por nome (completo ou parcial)\n[d] Busca pessoas por intervalo de data de nascimento\n[s] Sair\n---------------------------------------------------------------------------\n"

while True:
  escolha = input(textoMenu)

  if escolha == 's':
    break

  elif escolha == 'c':
    buscaCPF = input("Insira o CPF da pessoa desejada: (sem pontuação)\n")
    buscaPessoaPorCPF(raizCPF, buscaCPF, gerenciadorPessoas)
    print('---------------------------------------------------------------------------\n')

  elif escolha == 'n':
    buscaNomes = input("Insira um nome ou parte inicial de um nome: ").upper()
    pessoas = buscaPessoasPorString(raizNome, buscaNomes)
    if len(pessoas) > 0:
      gerenciadorPessoas.imprimeListaSelecionados(pessoas)
    print('---------------------------------------------------------------------------\n')

  elif escolha == 'd':
    buscaData1 = input("Insira a primeira data no seguinte formato: '20/08/2000'\n")
    buscaData2 = input("Insira a segunda data no seguinte formato: '20/08/2000'\n") 
    buscaDATA = buscaIntervaloPorData(raizDataNasc, buscaData1, buscaData2)
    if len(buscaDATA) > 0:
      gerenciadorPessoas.imprimeListaSelecionados(buscaDATA)
    print('---------------------------------------------------------------------------\n')