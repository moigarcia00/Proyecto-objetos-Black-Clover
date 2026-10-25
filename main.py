from ordenes import orden
from reino import Reino
from personaje import Personaje

reino_trebol = Reino("Reino trebol", "Un reino donde destaca por su individualidad.")
reino_corazon = Reino("Reino Corazón", "Un reino donde destaca su conexión mágica con la naturaleza")
reino_diamante = Reino ("Reino Diamante", "Un reino donde destaca por su gran poder militar")
reino_pica = Reino ("Reino Pica", "Un reino que destaca por su frío extremo y por ser reinado por demonios")


toros_negros = orden(" de los Toros Negros", "Una orden que destaca por su individualidad de sus integrantes y valorar a cada miembro por sus logros y no por su linaje ni su magia")
amanecer_dorado = orden (" del Amanecer Dorado", "Una orden que destaca por ser la mejor oden del reino trebol y sus miembtros ser los más fuertes del reino")

yuno = Personaje(nombre= "Yuno", descripcion= " Un huérfano con un un gran talento mágico que sueña con ser el rey mago junto con su rival y amigo Asta.", reino= "reino_trebol", raza= "Humano", magia= "magia de viento")
asta = Personaje(nombre= "Asta", descripcion= " Un huerfano sin poder mágico que aspira ser rey mago junto con su rival y amigo Yuno.", reino= "reino_trebol", raza= "Humano", magia= "la antimagia")
luck = Personaje(nombre= "Luck", descripcion= " El Hijo bastardo de una noble al que le obsesiona y emociona los combates.", reino= "reino_trebol", raza= "Humano", magia= "magia de rayo")
litch = Personaje(nombre= "Litch", descripcion= "El lider de los elfos y traicionado por los humanos con el objetivo de vengarse de ellos tras haber resucitado después de haber muerto hace más de 500 años.", reino= "reino_trebol", raza= "Elfo", magia= "magia de espadas")

personajes = [yuno, asta, luck, litch]
Reinos = [reino_trebol, reino_corazon, reino_diamante, reino_pica]
ordenes = [toros_negros, amanecer_dorado]

for personaje in personajes:
    personaje.presentarse()
    personaje.lanzar_hechizo()
    personaje.atacar()
    personaje.esquivar()
    print()

for reino in Reinos:
    reino.presentar()
    print()

for orden in ordenes:
    orden.presentar()
    print()