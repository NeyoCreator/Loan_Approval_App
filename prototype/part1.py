"""
The main aim of this window is to Sign up the user 
what we will obtain is email and password
"""


# Import Libraries
from tkinter import *
import sqlite3
import cv2
import matplotlib.pyplot as plt
import dlib
import numpy as np
import tkinter as tk 
from tkinter import  messagebox  

#BEGIN

# Assign Global variables
global image_face
global image_id

# Obtain from user
global img_face
global img_id

global conn

# Create part1 window
root = Tk()
root.title("Sign up")
root.geometry("400x400")

# Window that takes face image
def face_image():
    video = cv2.VideoCapture(0)
    a = 0
    img_counter = 0

    # Obtain face image
    while True:
        a = a + 1
        check, frame = video.read()
        print(check)
        print(frame)

        #indicator text
        cv2.putText(frame, "Capture Face", (60, 60), cv2.FONT_HERSHEY_SIMPLEX, 2.3, (0,30,255))
        #annotate rectangle 
        cv2.rectangle(frame, (80,80), (450,450), (0,30,255), thickness= 2, lineType=cv2.LINE_AA)
        cv2.imshow("Main frame thing", frame)

        # cv2.waitKey(0)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('s'):
            # SPACE pressed
            face_image.variable = "face_img_{}.png".format(img_counter)
            cv2.imwrite(face_image.variable, frame)
            print("{} written!".format(face_image.variable))
            img_counter += 1
            video.release()
            cv2.destroyAllWindows()
            break


        
# Window that take card image 
def id_card():
    video = cv2.VideoCapture(0)
    a = 0
    img_counter = 0

    #Obtain ID 
    while True:
        a = a + 1
        check, frame = video.read()

        #indicator text
        cv2.putText(frame, "Capture ID", (60, 60), cv2.FONT_HERSHEY_SIMPLEX, 2.3, (0,30,255))

        #annotate rectangle 
        cv2.rectangle(frame, (80,80), (450,450), (0,30,255), thickness= 2, lineType=cv2.LINE_AA)
        cv2.imshow("Main frame thing", frame)

        # cv2.waitKey(0)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('s'):
            # SPACE pressed
            id_card.variable = "id_img_{}.png".format(img_counter)
            cv2.imwrite(id_card.variable, frame)
            print("{} written!".format(id_card.variable))
            img_counter += 1
            video.release()
            cv2.destroyAllWindows()
            break
            
        print(a)
        

# Convert images to Binary 
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


# Load variables to dataframe
def submit():
    #convert images 
    image_face = convertToBinaryData(face_image.variable)
    image_id = convertToBinaryData(id_card.variable)

    data_tuple = (email,password,image_face,image_id)

    # Create database
    conn = sqlite3.connect('user_profile.db')
    # create cursor
    c = conn.cursor()
    sqlite_insert_blob_query = """INSERT INTO users(
        email,    
        password,
        image_face,
        image_id) values(?,?,?,?)"""

    c.execute(sqlite_insert_blob_query,data_tuple)    
    # Commit Changes 
    conn.commit()
    # Close connection
    conn.close()

    
# Sign up user to application
def sign_up():
    # Set global variables
    global email
    global password

    conn = sqlite3.connect('user_profile.db')
    # create cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
        email TEXT NOT NULL,    
        password TEXT NOT NULL,
        image_face BLOB NOT NULL,
        image_id BLOB NOT NULL
        )""")
    # Commit Changes 
    conn.commit()
    # Close connection
    conn.close()

    # Get variables
    email = mail_ent.get()
    password = pass_ent.get()
    print(email)
    print(password)

    # Open new window
    part2 = Toplevel()
    Button(part2, text ="Take Image", command= face_image).pack()
    Button(part2, text ="Take ID card", command= id_card).pack()
    Button(part2, text ="Submit",command = submit).pack()

#email_entry
mail_ent = Entry(root,)
mail_ent.pack()
mail_ent.insert(0,"e-mail: ")

#password_entry
pass_ent = Entry(root,)
pass_ent.pack()
pass_ent.insert(0,"password: ")

myButton = Button(root, text ="Continue", command=sign_up)
myButton.pack()


root.mainloop()
#END