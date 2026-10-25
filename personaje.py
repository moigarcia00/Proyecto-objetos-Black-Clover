class Personaje:
    def __init__(self, nombre, descripcion, reino, raza, magia, orden=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.reino = reino
        self.raza = raza
        self.magia = magia
        self.orden = orden

    def presentarse(self):
        if hasattr(self.reino, "nombre"):
            reino_nombre = self.reino.nombre
        else:
            reino_nombre = self.reino

        texto = f"Soy {self.nombre} del {reino_nombre}, soy {self.raza} y mi magia es {self.magia}."
        if self.orden is not None:
            if hasattr(self.orden, "nombre"):
                texto = texto + f" Pertenezco a la orden{self.orden.nombre}."
            else:
                texto = texto + f" Pertenezco a la orden{self.orden}."
        texto = texto + f" {self.descripcion}"
        print(texto)

    def lanzar_hechizo(self):
        print(f"{self.nombre} lanza un hechizo de {self.magia}")

    def atacar(self):
        print(f"{self.nombre} ataca con su grimorio.")

    def esquivar(self):
        print(f"{self.nombre} esquiva un ataque.")
