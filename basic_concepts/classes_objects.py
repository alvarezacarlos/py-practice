class Person:
    name = 'Carlos'

person1 = Person()

print(person1.name)

#.............. __init__ func. (contructor)
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
class Auto:
    def __init__(self, color, brand, price):
        self.color = color
        self.brand = brand
        self.price = price

    def getColor(self):
        return self.color

    def getBrand(self):
        return self.brand

    def getPrice(self):
        return self.price

ford = Auto('red', 'Ford', 25000)

print(ford.brand, ford.color, ford.price)

print(ford.getColor())
print(ford.getBrand())
print(ford.getPrice())


#delete object properties
del ford.color
# print(ford.color) #Erro object ford has not attribute color!


#delete an object completly
del ford

#Empty class
class Country:
    pass

#.......................Inheritance

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print(self.tipo)
        print(self.nombre)
        
class Gato(Animal): 
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        # Animal.__init__(self, nombre, onomatopeya)  #extendiento la el metodo init
        super().__init__(nombre, onomatopeya) #extendiento la el metodo init
        
class Perro(Animal):
    tipo = 'perro'
class Canario(Animal):
    tipo = 'canario'
           
gato = Gato('Laila', 'Maullido')
perro = Perro('Sasha', 'Ladrido')
canario = Canario('Pioplin', 'Silvido')

gato.saludo()
perro.saludo()
canario.saludo()



    