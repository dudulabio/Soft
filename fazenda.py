class Fazenda:
  def __init__(self, nome, area_ha, endereco):
   self.nome=nome
   self.area_ha=area_ha
   self.endereco=endereco
   self.tratores=[]
   self.culturas=[]
   self.safras=[]
   self.talhoes=[]
   self.plantios=[]
####Lista de tratores####    
  def imprimirListaTratores(self):
    for t in self.tratores:
      t.print()

  def addTratorLista(self, Trator):
    self.tratores.append(Trator)

  def remListaTratores(self, Trator):
    self.tratores.remove(Trator)
####Lista de Culturas####
  def imprimirListaCulturas(self):
    for t in self.culturas:
      t.print()

  def addCulturaLista(self, Cultura):
    self.culturas.append(Cultura)

  def remListaCulturas(self, Cultura): 
    self.culturas.remove(Cultura)
####Lista de Safras####    
  def imprimirListaSafras(self):
     for t in self.safras:
       t.print()

  def addSafraLista(self, Safra):
     self.safras.append(Safra)

  def remListaSafra(self, Safra): 
     self.safras.remove(Safra)
####Lista de Talhões####
  def imprimirListaTalhoes(self):
     for t in self.talhoes:
       t.print()

  def addTalhaoLista(self, Talhao):
     self.talhoes.append(Talhao)

  def remListaTalhao(self, Talhao): 
     self.talhoes.remove(Talhao)

####Lista de Plantio####
  def imprimirListaPlantio(self):
    for t in self.plantios:
      t.print()

  def addPlantioLista(self, Plantio):
     self.plantios.append(Plantio)

  def remListaPlantio(self, Plantio): 
     self.plantios.remove(Plantio)