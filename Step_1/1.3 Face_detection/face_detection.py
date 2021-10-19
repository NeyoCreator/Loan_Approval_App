import cv2

def detect_face(img):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 1)

    #crop the image 
    
    
    return img,x,y,h,w

# Read the input image
img = cv2.imread('ids/id4.png')
img,x,y,h,w = detect_face(img)


cv2.imshow('img', img)
cv2.waitKey()