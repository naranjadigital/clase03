class ClaseotroEjemplo:
    def __init__(self):
        self.publico = 'Publico'
        self.__privado = 'Privado'

    def setPrivado(self, valor):
        self.__privado = valor

    def getPrivado(self):
        return self.__privado

x = ClaseotroEjemplo()
print(x.publico)
x.publico = 'cambie la publica'
print(x.publico)
x.setPrivado('cambie')
print(x.getPrivado())