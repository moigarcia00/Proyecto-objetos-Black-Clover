class Reino:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def presentar(self):
        print(f"Bienvenidos al {self.nombre}. {self.descripcion}")
