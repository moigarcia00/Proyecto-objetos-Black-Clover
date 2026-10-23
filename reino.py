class Reino:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def presentar(self):
        print(f"Son las tierras de {self.nombre}. {self.descripcion}")
