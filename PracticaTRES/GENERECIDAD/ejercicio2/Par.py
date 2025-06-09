class Par:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor

    def mostrar_par(self):
        print(f"({self.clave}, {self.valor})")


# Estudiante
par_estudiante = Par("202012345", "Juan Pérez")
par_estudiante.mostrar_par()

# Producto
par_producto = Par("A123", 50.75)
par_producto.mostrar_par()