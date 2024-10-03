import random
import time 
import tkinter as tk
from tkinter import ttk

#This allows us to use procedures in another file
from PetProceduresShell import *  


bob = pet()




def test():
    pass


#first time to just show stats
bob.update_stats()

#main menu buttons
bob.name_set()

bob.root.mainloop()