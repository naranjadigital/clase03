class Felino:
    def __init__(self):
        print('se creo felino')
        #codigo
        #codigo

    def rugido(self):
        print('el felino dio un rugido')


class Mascota:
    def sientate(self):
        print('sientate')


class Gato(Felino, Mascota):
    def __init__(self, energia, hambre):
        self.energia = energia
        self.hambre = hambre
        print('se creo un gato')

    def dormir(self):
        print('gato durmiendo')


garfield = Gato(10, 10)
garfield.dormir()
garfield.rugido()
garfield.sientate()