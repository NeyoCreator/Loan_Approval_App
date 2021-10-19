"""The aim is to create a pop up message that will displaye the result"""

import tkinter as tk 
from tkinter import  messagebox  

tk.Tk().withdraw()
messagebox.showinfo(
    title= "Result",
    message= "The faces match"
)


# class Win :
#     def popup(self,title = "", sentence = ""):

#         tk.Tk().withdraw()
#         name = messagebox.showinfo(
#             title=title, message=sentence)

# win = Win()
# win.popup("Alert","This is a message")

