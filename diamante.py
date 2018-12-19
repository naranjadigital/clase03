class A:
    def llamada(self):
        print('Llamada A')

class B(A):
    def llamada(self):
        print('Llamada B')
        super().llamada()

class C(A):
    def llamada(self):
        print('llamada C')
        super().llamada()

class D(B,C):
    def llamada(self):
        print('Llamada D')
        super().llamada()

d = D()
d.llamada()