class Personaje:
    def __init__(self, nombre, descripcion, reino, raza):
        self.nombre = nombre
        self.descripcion = descripcion
        self.reino = reino
        self.raza = raza

    def presentarse(self):
        print(f"Soy {self.nombre} del {self.reino} y soy {self.raza}. {self.descripcion}")

    def lanzar_hechizo(self):
        print(f"{self.nombre} lanza un hechizo.")

    def atacar(self):
        print(f"{self.nombre} ataca con su grimorio.")

    def descansar(self):
        print(f"{self.nombre} descansa un momento.")
