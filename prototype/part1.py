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
from PIL import ImageTk, Image

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
root.geometry("250x250")

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
    # 1.Convert images 
    image_face_blob = convertToBinaryData(face_image.variable)
    image_id_blob = convertToBinaryData(id_card.variable)


    #load the image 
    image_face = dlib.load_rgb_image(face_image.variable)
    image_id = dlib.load_rgb_image(id_card.variable)

    # 2.Create tuple for all values
    data_tuple = (email,password,image_face_blob,image_id_blob)

    # 3.Match the Images
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor("shape_predictor_5_face_landmarks.dat")
    model = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

    # 4.Apply face detection  using detector object 
    img1_detect = detector(image_face,1)
    img2_detect = detector(image_id,1)

    # 5.Get the image shapes 
    img1_shape = sp(image_face,img1_detect[0])
    img2_shape = sp(image_id,img2_detect[0])

    # 6.Align the images 
    img1_align = dlib.get_face_chip(image_face, img1_shape)
    img2_align = dlib.get_face_chip(image_id, img2_shape)

    #implement the model 
    img1_rep = model.compute_face_descriptor(img1_align)
    img2_rep = model.compute_face_descriptor(img2_align)

    #the representation of the images are dlib.vectors we need to convert them into numpy arrays
    img1_rep = np.array(img1_rep)
    img2_rep = np.array(img2_rep)

    """the final step is verification we need to find the distance between the arrays
        the greater the distance the less similar the images are to each other.
        Create a function that find the euclidian distance between the images """

    def find_distance(img_x1, img_x2):
        euclidian_distance = img_x1 - img_x2
        euclidian_distance = np.sum(np.multiply(euclidian_distance,euclidian_distance))
        euclidian_distance = np.sqrt(euclidian_distance)
        return euclidian_distance

    distance = find_distance(img1_rep,img2_rep)


    if distance < 0.6 :
        # Show results 
        result = "Images match"
        label_result = Label(part2, text=result)
        label_result.grid(row=3, column=0)

        # Create database
        conn = sqlite3.connect('user_profile.db')
        # 2.Create cursor
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
    else :
        result = "Images do not match"
        label_result = Label(part2, text=result)
        label_result.grid(row=3, column=0)

    
# Sign up user to application
def sign_up():
    # Set global variables
    global email
    global password
    global part2

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
    part2.title("Personal Details")
    part2.geometry("250x250")
    btn_image = Button(part2, text ="Take Image", command= face_image)
    btn_image.grid(row=0, column=0, columnspan=3, padx=10,pady=10)
    btn_card = Button(part2, text ="Take ID card", command= id_card)
    btn_card.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    btn_submit= Button(part2, text ="Submit",command = submit)
    btn_submit.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

#email_entry
mail_ent = Entry(root,width = 35,borderwidth=5)
mail_ent.grid(row=0, column=0,columnspan=3,padx=10,pady=10)
mail_ent.insert(0,"e-mail: ")

#password_entry
pass_ent = Entry(root,width = 35,borderwidth=5)
pass_ent.grid(row=1, column=0,columnspan=3,padx=10,pady=10)
pass_ent.insert(0,"password: ")

myButton = Button(root, text ="Continue", command=sign_up)
myButton.grid(row=2, column=0,columnspan=3,padx=10,pady=10)



root.mainloop()
#END