
class Bebidas:
    
    def __init__(self, id, nombre, precio, clasificacion, marca):
        
        self._id = id
        self._nombre = nombre
        self._precio = precio
        self._clasificacion = clasificacion
        self._marca = marca
        
    #creacion de los metodos getter a setter
    
    @property
    def id(self):
        return self._id
    
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def clasificacion(self):
        return self._clasificacion

    @clasificacion.setter
    def clasificacion(self, clasificacion):
        self._clasificacion = clasificacion


    @property
    def marca(self):
        return self._marca

    @marca.setter 
    def marca(self, marca):
        self._marca = marca



class AlmacenBebidas:
    def __init__(self):
        self.bebidas = []
        
        
    def DarAlta(self):
        
        id = int(input("Ingrese el ID de la bebida: "))
        nombre = input("Ingrese el nombre de la bebida: ")
        precio = float(input("Ingrese el precio de la bebida: "))
        clasificacion = input("Ingrese la clasificación de la bebida: ")
        marca = input("Ingrese la marca de la bebida: ")
    
        bebida = Bebidas(id, nombre, precio, clasificacion, marca,)
        self.bebidas.append(bebida)
        print("Bebida agregada correctamente.")
        
    
    def DarBaja(self, id):
        for bebida in self.bebidas:
            if bebida.id == id:
                self.bebidas.remove(bebida)
                print("Se elimino correctamente la bebida.")
                return
        print("No se encontró ninguna bebida con el ID indicado")
    
    
    def actualizar(self, id):
        for bebida in self.bebidas:
            if bebida.id == id:
                nombre = input("Ingrese el nuevo nombre de la bebida: ")
                precio = float(input("Ingrese el nuevo precio de la bebida: "))
                clasificacion = input("Ingrese la nueva clasificación de la bebida: ")
                marca = input("Ingrese la nueva marca de la bebida: ")
                
                bebida.nombre = nombre
                bebida.precio = precio
                bebida.clasificacion = clasificacion
                bebida.marca = marca
                print("Se actualizo correctamente la bebida.")
                return
        print("No se encontró ninguna bebida con el ID indicado.")
        
     
    def Mostrar(self):
        if len(self.bebidas) == 0:
            print("No existen bebidas registradas.")
        else:
            for bebida in self.bebidas:
                self.mostrarBebida(bebida) 
       
    def mostrarBebida(self, bebida):
        print(f'ID: {bebida.id}')
        print(f'Nombre: {bebida.nombre}')
        print(f'Precio: {bebida.precio}')
        print(f'Clasificacion: {bebida.clasificacion}')
        print(f'Marca: {bebida.marca}')
        print('----------------------------------------------------------------------------')
        
        
    def PrecioPromedio(self):
        if len(self.bebidas) == 0:
            print("No existen bebidas registradas")
        else:
            total_precios = sum(bebida.precio for bebida in self.bebidas)
            promedio = total_precios / len(self.bebidas)
            print(f'El precio promedio de las bebidas es: {promedio}')
            
            
    def BebidaMarca(self, marca):
        cantidad = sum(1 for bebida in self.bebidas if bebida.marca == marca)
        print(f'Cantidad de bebidas de la marca {marca}: {cantidad}')
    
    
    def Clasificacion(self, clasificacion):
        cantidad = sum(1 for bebida in self.bebidas if bebida.clasificacion == clasificacion)
        print(f'Cantidad de bebidas de la clasificación {clasificacion}: {cantidad}')



        
        
        
    






      
        