class Persona:
    def saludo(self):
        print('Hola')

    def comer(self, param1, param2):
        print('comer persona')

class Peruano(Persona):
    def saludo(self):
        print('Hablaaa')

    def comer(self):
        print('aca se come rico')

class Chileno(Persona):
    def saludo(self):
        print('Hola Gallo')

persona = Persona()
persona.saludo()
persona.comer(1, 2)

peruano = Peruano()
peruano.saludo()
peruano.comer()

chileno = Chileno()
chileno.saludo()
