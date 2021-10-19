"""The aim of the script is to capture the required data ID , snapshot of the user 
   from the webcam
"""


import cv2

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
        img_name = "face_img_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
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
        img_name = "id_img_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        break
        
    print(a)

video.release()
cv2.destroyAllWindows()