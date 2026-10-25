class orden:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def presentar(self):
        print(f"Bienvenidos a la orden{self.nombre}. {self.descripcion}")