class Safra:
  def __init__(self, nome, cultura, ano_inicio, ano_fim):
    self.nome=nome
    self.cultura=cultura
    self.ano_inicio=ano_inicio
    self.ano_fim=ano_fim
  def print (self):  
      print(f'\n----------------')
      print(f"Nome: ########## : {self.nome}")
      print(f"Cultura..........: {self.cultura}")
      print(f"Ano de Inicio....: {self.ano_inicio}")
      print(f"Ano de término...: {self.ano_fim}")




