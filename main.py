from fazenda import Fazenda
from trator import Trator  
from cultura import Cultura
from safra import Safra
from talhao import Talhao
from plantio import Plantio
faz1 = Fazenda("Fazenda do João", "1000", "Rua das Flores")


#####
trator1= Trator("Trator1","John Deere", "Primeiro", "Azul", 150, 20)
trator2= Trator("Trator2","Masey", "Segundo", "Verde", 150, 20)

faz1.addTratorLista(trator1)
faz1.addTratorLista(trator2)

######################################
cultura1= Cultura("Soja")
cultura2= Cultura("Milho")  
cultura3=Cultura("Algodão")

faz1.addCulturaLista(cultura1)
faz1.addCulturaLista(cultura2)
faz1.addCulturaLista(cultura3)
####################################

safra1= Safra("Safra1","Soja", "2019", "2020")
safra2= Safra("Safra2","Milho", "2020", "2021")
safra3= Safra("Safra3","Algodão", "2021", "2022")

faz1.addSafraLista(safra1)
faz1.addSafraLista(safra2)
faz1.addSafraLista(safra3)

####################################
talhao1= Talhao("Talhao1", "500")  
talhao2= Talhao("Talhao2", "550")
talhao3= Talhao("Talhao3", "600")

faz1.addTalhaoLista(talhao1)
faz1.addTalhaoLista(talhao2)
faz1.addTalhaoLista(talhao3)
####################################
plantio1= Plantio("01/01/2022", "500", "Talhao1", "Safra22/23")
plantio2= Plantio("02/01/2022", "550", "Talhao2", "Safra23/24")
plantio3= Plantio("03/01/2022", "600", "Talhao3", "Safra24/25")

faz1.addPlantioLista(plantio1)
faz1.addPlantioLista(plantio2)
faz1.addPlantioLista(plantio3)

####################################

#faz1.imprimirListaTratores()
#faz1.imprimirListaCulturas()
#faz1.imprimirListaSafras()
#faz1.imprimirListaTalhoes()
#faz1.imprimirListaPlantio()

print(faz1)