from reino import Reino
from personaje import Personaje

reino_trebol = Reino("Reino trebol", "Un reino donde destaca por su individualidad.")

yuno = Personaje(nombre= "Yuno", descripcion= "Joven mago con un potencial enorme.", reino= "reino_trebol", raza= "Humano")
asta = Personaje(nombre= "Asta", descripcion= "Chico sin magia pero nunca se rinde.", reino= "reino_trebol", raza= "Humano")
luck = Personaje(nombre= "Luck", descripcion= "Chico enérgico y bromista.", reino= reino_trebol, raza= "Humano")
litch = Personaje(nombre= "Litch", descripcion= "Lider de los elfos.", reino= reino_trebol, raza= "Elfo")

personajes = [yuno, asta, luck, litch]
Reinos = [reino_trebol]

for personaje in personajes:
    personaje.presentarse()
    personaje.lanzar_hechizo()
    personaje.atacar()
    personaje.descansar()
    print()

for reino in Reinos:
    reino.presentar()