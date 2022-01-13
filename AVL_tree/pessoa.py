class Pessoa:
  #codData vai ser adicionado como parâmetro do construtor
  def __init__(self, cpf, rg, nome, dataNasc, cidade,codData):
    self.nome = nome
    self.cpf = cpf
    self.dataNasc = dataNasc
    self.rg = rg
    self.cidade = cidade
    self.codData = int(codData) 

  def imprime(self):
    pessoaString = '\n**' + str(self.nome) + '**\nCPF: ' + str(self.cpf) + '\nRG: ' + str(self.rg) + '\nDATA DE NASCIMENTO: ' + str(self.dataNasc) + '\nCIDADE DE NASCIMENTO: ' + str(self.cidade)
    print(pessoaString)