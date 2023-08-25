from tkinter import Tk
from vista import Ventana
import observador

if (
    __name__ == "__main__"
):  # si se abre directamente controlador.py se ejecuta lo de adentro sino no
    root = Tk()
    obj1 = Ventana(root)
    el_observador = observador.ConcreteObserverA(obj1.objeto_base)
    root.mainloop()
