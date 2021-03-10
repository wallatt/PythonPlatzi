

class person:
    def __init__(self):
        self.__name=''
    def setname(self, name):
        print('setname() called')
        self.__name=name
    def getname(self):
        print('getname() called')
        return self.__name
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    name=property(getname, setname)

p1=person()
p1.name="Steve"
print(p1.name)
print(p1)
p1.setname("Walter")
print(p1.name)
#print(p1.__name) Tira error que no existe el atributo __name



