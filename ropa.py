class Producto:
    def _init_(self, nombre, precio):
        self._nombre = nombre  
        self._precio = precio

    def get_precio(self):
        return self._precio

    def descripcion(self):
        return f"{self._nombre} - {self._precio:,} PYG"


class Camisa(Producto):
    def _init_(self, precio, talla):
        super()._init_("Camisa", precio)
        self.talla = talla

    def descripcion(self):
        return f"Camisa de talla {self.talla} - {self._precio:,} PYG"

class Pantalon(Producto):
    def _init_(self, precio, talla):
        super()._init_("Pantalón", precio)
        self.talla = talla

    def descripcion(self):
        return f"Pantalón de talla {self.talla} - {self._precio:,} PYG"

class Zapato(Producto):
    def _init_(self, precio, talla):
        super()._init_("Zapato", precio)
        self.talla = talla

    def descripcion(self):
        return f"Zapato de talla {self.talla} - {self._precio:,} PYG"


class Tienda:
    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto.descripcion()}")

    def procesar_compra(self, indice):
        producto = self.productos.pop(indice - 1)
        print(f"Has comprado: {producto.descripcion()}\n")

if __name__ == "_main_":
    tienda = Tienda()
    tienda.agregar_producto(Camisa(150000, 'M'))
    tienda.agregar_producto(Pantalon(250000, 'L'))
    tienda.agregar_producto(Zapato(300000, '42'))

    print("Bienvenido a la tienda de ropa:")
    tienda.mostrar_productos()
    
    
    tienda.procesar_compra(1)