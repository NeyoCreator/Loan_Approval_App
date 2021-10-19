
"""we will incoprorate the dlib library to make face detection and match two images 
    1. ask the user the face picture 
    2. ask the user for ID 
    3. see if the faces are similar
    4. display the results.
"""

#importing libraries
import cv2
import matplotlib.pyplot as plt
import dlib
import numpy as np
import tkinter as tk 
from tkinter import  messagebox  

video = cv2.VideoCapture(0)
a = 0
img_counter = 0

#obtain face image
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
        img_face = "face_img_{}.png".format(img_counter)
        cv2.imwrite(img_face, frame)
        print("{} written!".format(img_face))
        img_counter += 1
        break

    print(a)

#Obtain ID 
while True:

    a = a + 1
    check, frame = video.read()

    print(check)
    print(frame)

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
        img_id = "id_img_{}.png".format(img_counter)
        cv2.imwrite(img_id, frame)
        print("{} written!".format(img_id))
        img_counter += 1
        break
        
    print(a)

video.release()
cv2.destroyAllWindows()



# def face_recognition(img1,img2):

#     same = 0

#     #1.set the object and model 
#     detector = dlib.get_frontal_face_detector()
#     sp = dlib.shape_predictor("shape_predictor_5_face_landmarks.dat")
#     model = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

#     #2.apply face detection  using detector object 
#     img1_detect = detector(img1,1)
#     img2_detect = detector(img2,1)

#     #3.get the image shapes 
#     img1_shape = sp(img1,img1_detect[0])
#     img2_shape = sp(img2,img2_detect[0])

#     #4.align the images 
#     img1_align = dlib.get_face_chip(img1, img1_shape)
#     img2_align = dlib.get_face_chip(img2, img2_shape)

#     #5.implement the model 
#     img1_rep = model.compute_face_descriptor(img1_align)
#     img2_rep = model.compute_face_descriptor(img2_align)

#     #7.the representation of the images are dlib.vectors we need to convert them into numpy arrays
#     img1_rep = np.array(img1_rep)
#     img2_rep = np.array(img2_rep)

#     def find_distance(img_x1, img_x2):
#         euclidian_distance = img_x1 - img_x2
#         euclidian_distance = np.sum(np.multiply(euclidian_distance,euclidian_distance))
#         euclidian_distance = np.sqrt(euclidian_distance)
#         return euclidian_distance

#     distance = find_distance(img1_rep,img2_rep)

#     #8.threshold value 
#     threshold = 0.6 

#     if distance  < threshold :
#         same = 1
#     else :
#         same = 0

#     #same is a binary value , if the images are the same we return 1 if not 0

#     return same

# #get the images
# img_face = cv2.imread('face_img_0.png')
# img_id = cv2.imread('id_img_1.png')

# result = face_recognition(img_face, img_id)

# if result ==1 :
#     #the images are a match
#     tk.Tk().withdraw()
#     messagebox.showinfo(
#         title= "Result",
#         message= "The faces match"
#     )
# else :
#     tk.Tk().withdraw()
#     messagebox.showinfo(
#         title= "Result",
#         message= "The faces do not match"
#     )







