class Trator:
  #criando o construtor da classe
  def __init__(self, nome, marca, modelo, cor, potencia_cv, torque):
    self.nome=nome
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.potencia_cv = potencia_cv
    self.torque = torque
    #self.andando = False

  def print(self):
    print(f'\n----------------')
    print(f"Nome..........: {self.nome}")
    print(f"Marca.........: {self.marca}")
    print(f'Modelo........: {self.modelo}')
    print(f'Cor...........: {self.cor}')
    print(f'Potencia em CV: {self.potencia_cv}')
    print(f'Torque........: {self.torque}')
    print(f'\n----------------')



  #def andar(self):
    #self.andando = True
    #pass

  #def parar(self):
    #self.andando = False
    #pass
  