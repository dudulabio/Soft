class Plantio:
  def __init__(self, data_plantio, ha_plantados, talhao_plantio, safra_plantio):
    self.data_plantio = data_plantio
    self.ha_plantados = ha_plantados
    self.talhao_plantio = talhao_plantio
    self.safra_plantio = safra_plantio


  def print(self):
    print(f'\n----------------')
    print(f'Data do Plantio: {self.data_plantio}')
    print(f'Hectares Plantados: {self.ha_plantados}')
    print(f'Talhão Plantio: {self.talhao_plantio}')
    print(f'Safra Plantio: {self.safra_plantio}')
    print(f'\n----------------')

