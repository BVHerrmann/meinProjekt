import os
import json
os.system("cls")
from tkinter import Tk

fenster = Tk()
fenster.mainloop()


#Hinzugefügt im main branch
def erzeuge_zufallszahlen_liste(n):
    return [random.randint(1, 100) for _ in range(n)]

