class Clientes:
  
    def __init__(self, idcliente, nombre, apellido, correo, fecha_registro, saldo):
        self.idcliente=idcliente
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.fecha_registro=fecha_registro
        self.__saldo=saldo

    def mostrar_saldo(self):
        agregar=int(input("monto para agregar: "))
        print(f"el nuevo saldo de {self.nombre + self.apellido} tras haber agregado {agregar} es de {agregar + self.__saldo}")
    
    def get_saldo(self):
        return self.__saldo

juan=Clientes(1, "juan", "rojas","gmail",25-5-1992, 20000)
juan.mostrar_saldo()





class Producto:
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, impuesto):
        self.sku=sku
        self.nombre=nombre
        self.categoria=categoria
        self.proveedor=proveedor
        self.stock=stock
        self.valor_neto=valor_neto
        self.__impuesto=1.19

    def mostrar_producto(self):
        print(f" producto categoria {self.categoria} costó en total {self.valor_neto * self.__impuesto}")   
    
    def get_impuesto(self):
        return self.__impuesto

cat=Producto("sku1","j","zapatilla", "nike", 10, 5000, 1.19)
neto=5000
cat.mostrar_producto()


class Vendedor:
    def __init__(self, run, nombre, apellido, sección, comision):
        self.run=run
        self.nombre=nombre
        self.apellido=apellido
        self.seccion=sección
        self.comision=0
        






    