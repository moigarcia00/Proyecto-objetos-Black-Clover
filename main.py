from ordenes import orden
from reino import Reino
from personaje import Personaje

reino_trebol = Reino("Reino trebol", "Un reino donde destaca por su individualidad.")
reino_corazon = Reino("Reino Corazón", "Un reino donde destaca su conexión mágica con la naturaleza.")
reino_diamante = Reino("Reino Diamante", "Un reino donde destaca por su gran poder militar.")
reino_pica = Reino("Reino Pica", "Un reino que destaca por su frío extremo y por ser reinado por demonios.")


toros_negros = orden(" de los Toros Negros", "Una orden que destaca por su individualidad de sus integrantes y valorar a cada miembro por sus logros y no por su linaje ni su magia.")
amanecer_dorado = orden(" del Amanecer Dorado", "Una orden que destaca por ser la mejor oden del reino trebol y sus miembtros ser los más fuertes del reino.")
leones_carmesi = orden(" de los Leones Carmsí", "Una orden que destaca por su gran pasión y lealtad al reino Trebol")
rosas_azules = orden(" de las Rosas Azules", "Orden exclusivamente para mujeres que destaca por su orgullo de sí mismas y demostrando que son superiores a los hombres")


yuno = Personaje(nombre="Yuno", descripcion="Un huérfano con un un gran talento mágico que sueña con ser el rey mago junto con su rival y amigo Asta.", reino= reino_trebol, raza="Humano", magia="magia de viento", orden = amanecer_dorado)
asta = Personaje(nombre="Asta", descripcion="Un huerfano sin poder mágico que aspira ser rey mago junto con su rival y amigo Yuno.", reino= reino_trebol, raza="Humano", magia="la antimagia", orden = toros_negros)
luck = Personaje(nombre="Luck", descripcion="El Hijo bastardo de una noble al que le obsesiona y emociona los combates.", reino= reino_trebol, raza="Humano", magia="magia de rayo")
litch = Personaje(nombre="Litch", descripcion="El lider de los elfos y traicionado por los humanos con el objetivo de vengarse de ellos tras haber resucitado después de haber muerto hace más de 500 años.", reino= reino_trebol, raza="Elfo", magia="magia de espadas")
mars = Personaje(nombre="Mars", descripcion="Uno de los Ocho Generales Brillantes del Reino Diamante.", reino= reino_diamante, raza="Humano", magia="magia de mineral")
zenon = Personaje(nombre="Zenon", descripcion="Miembro de la Tríada Oscura del Reino Pica y el anfitrión del diablo Beelzebub.", reino= reino_pica, raza="Humano", magia="magia de huesos")

personajes = [yuno, asta, luck, litch,mars,zenon]
Reinos = [reino_trebol, reino_corazon, reino_diamante, reino_pica]
ordenes = [toros_negros, amanecer_dorado,leones_carmesi,rosas_azules]

print("Bienvenido al mundo de Black Clover")
print("¿Qué quieres ver?")
print("1) Personajes")
print("2) Reinos")
print("3) Órdenes")

opcion = input("Elige un número: ")

if opcion == "1":
    for personaje in personajes:
        personaje.presentarse()
        personaje.lanzar_hechizo()
        personaje.atacar()
        personaje.esquivar()
        print()
elif opcion == "2":
    for reino in Reinos:
        reino.presentar()
        print()
elif opcion == "3":
    for orden in ordenes:
        orden.presentar()
        print()
else:
    print("Opción no válida. Elige 1, 2 o 3.")