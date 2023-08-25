from datetime import datetime


class Sujeto:
    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(*args)


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.arch_texto = "Observaciones.txt"
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, *args):
        print("Actualización dentro de ObservadorConcretoA")
        if args[0] == "Alta":
            observacion = (
                "A las "
                + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                + " - "
                + "Se agregó nuevo socio:\n"
                + "Nombre y Apellido: "
                + str(args[1])
                + " "
                + str(args[2])
                + "\nNro Documento: "
                + str(args[3])
                + "\n\n"
            )
        elif args[0] == "Baja":
            observacion = (
                "A las "
                + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                + " - "
                + "Se eliminó el socio:\n"
                + "Nombre y Apellido: "
                + str(args[1])
                + " "
                + str(args[2])
                + "\nNro Documento: "
                + str(args[3])
                + "\n\n"
            )
        elif args[0] == "Modificacion":
            observacion = (
                "A las "
                + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                + " - "
                + "Se modificó el socio:\n"
                + "Nombre y Apellido: "
                + str(args[1])
                + " "
                + str(args[2])
                + "\nNro Documento: "
                + str(args[3])
                + "\n A \n"
                + "Nombre y Apellido: "
                + str(args[4])
                + " "
                + str(args[5])
                + "\nNro Documento: "
                + str(args[6])
                + "\n\n"
            )
        with open(self.arch_texto, "a+") as arch:
            arch.write(observacion)
