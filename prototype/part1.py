"""
The main aim of this window is to Sign up the user 
what we will obtain is email and password
"""

from tkinter import *
import sqlite3

root = Tk()
root.title("Sign up")
root.geometry("400x400")
#Need to work on the padding

#BEGIN

def sign_up():
    #Write database
    conn = sqlite3.connect('user_profile.db')
    # create cursor
    c = conn.cursor()

    c.execute(" INSERT INTO users VALUES (:email, :password)",
    {
        "email": mail_ent.get(),
        "password":pass_ent.get()
    }
    )
    
    #commit Changes 
    conn.commit()
    # #close connection
    conn.close()
    

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

#Create database
conn = sqlite3.connect('user_profile.db')
# create cursor
c = conn.cursor()
# c.execute("""CREATE TABLE users(
#     email text,    
#     password text
#     )""")

#commit Changes 
conn.commit()
# #close connection
conn.close()




root.mainloop()
#END