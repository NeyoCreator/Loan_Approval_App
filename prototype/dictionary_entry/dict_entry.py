from tkinter import *
import sqlite3
import cv2
import matplotlib.pyplot as plt
import dlib
import numpy as np
import tkinter as tk 
from tkinter import  messagebox  
from PIL import ImageTk, Image
from tkinter import filedialog
import fitz  # this is pymupdf
import pandas as pd

root = Tk()

def Create():
    myLabel = Label(root, text="I have been clicked")
    myLabel.pack()

    
    conn = sqlite3.connect('users.db')
    # create cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
        email TEXT NOT NULL,    
        password TEXT NOT NULL,
        metadata TEXT NOT NULL
        )""")
    conn.commit()
    # Close connection
    conn.close()

def insert():
    dictionary_user = {"Name": "Neo",
                        "Age": 30,
                        "Location" : "Los Angeles",
                        "Networth" : "980 Trillion"  
    }

    string_dictonary = str(dictionary_user)

    datatuple = ("Luke", "Hurmane",string_dictonary)

    # Create database
    conn = sqlite3.connect('users.db')
    # 2.Create cursor
    c = conn.cursor()
    sqlite_insert_blob_query = """INSERT INTO users(
            email,    
            password,
            metadata) values(?,?,?)"""

    # sqlite_insert_blob_query = """INSERT INTO users(
    #         email,    
    #         password,
    #         image_face,
    #         image_id) values(?,?,?,?)"""

    c.execute(sqlite_insert_blob_query,datatuple)    
    # Commit Changes 
    conn.commit()
    # Close connection
    conn.close()
    print("I have been added!")

button_create = Button(root, text= 'Create!',command=Create, fg = "blue")
button_create.pack()
button_insert = Button(root, text= 'Insert!',command=insert, fg = "blue").pack()


root.mainloop()