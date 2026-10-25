class Personaje:
    def __init__(self, nombre, descripcion, reino, raza, magia):
        self.nombre = nombre
        self.descripcion = descripcion
        self.reino = reino
        self.raza = raza
        self.magia = magia

    def presentarse(self):
        print(f"Soy {self.nombre} del {self.reino}, soy {self.raza} y mi magia es {self.magia}. {self.descripcion}")

    def lanzar_hechizo(self):
        print(f"{self.nombre} lanza un hechizo de {self.magia}")

    def atacar(self):
        print(f"{self.nombre} ataca con su grimorio.")

    def esquivar(self):
        print(f"{self.nombre} esquiva un ataque.")
