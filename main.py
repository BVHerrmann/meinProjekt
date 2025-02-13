import os
import json
os.system("cls")
from tkinter import Tk

fenster = Tk()
fenster.mainloop()


# Neue Funktion hinzugekommen im feature branch
def write_default_file(path_name:str,data:list):
    try:
      with open(path_name,'w', encoding='utf-8') as stream:
          for item in data:
              stream.write(item + FEED_BACK_SEPERATOR)
          stream.close()
    except Exception as e:
        print('Can not write file: ',path_name,e)
