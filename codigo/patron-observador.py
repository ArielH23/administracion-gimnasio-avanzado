class Subject:
    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self):
        for observador in self.observadores:
            observador.update()  # llama a las clases ConcreteObserverA y B


class TemaConcreto(Subject):
    def __init__(
        self,
    ):
        self.estado = None

    def set_estado(self, value):
        self.estado = value
        self.notificar()  # llama para notificar el cambio de estado

    def get_estado(self):
        return self.estado


class Observador:
    def update(
        self,
    ):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self):  # llamada desde Subject
        print("Actualización dentro de observador ConcreteObserverA")
        self.estado = self.observado_a.get_estado()
        print("Estado= ", self.estado)


class ConcreteObserverB(Observador):
    def __init__(self, obj):
        self.observado_b = obj
        self.observado_b.agregar(self)

    def update(self):  # llamada desde Subject
        print("Actualización dentro de observador ConcreteObserverB")
        self.estado = self.observado_b.get_estado()
        print("Estado= ", self.estado)


tema1 = TemaConcreto()
observador_a = ConcreteObserverA(tema1)
observador_b = ConcreteObserverB(tema1)
tema1.set_estado(1)
