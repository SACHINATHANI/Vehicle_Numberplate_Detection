import sqlite3

import cv2
import numpy as np

# Read image
conn = sqlite3.connect('Form.db')
with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM imgsave")
    rows = cursor.fetchall()
    for row in rows:
        filename = row[0]

img = cv2.imread(filename, 1)
gray = cv2.cvtColor(img, 0)
cv2.imshow('img', gray)
cv2.waitKey(0)

#read haarcascade
plates_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

plat_detector =  cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
plates = plates_cascade.detectMultiScale(gray, 1.2, 4)


for (x,y,w,h) in plates:

    #detect plate with rectangle
    #rec.start point (x,y), rect. end point (x+w, y+h), blue color(255,0,0), line width 1

    plates_rec = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1)        
    cv2.putText(plates_rec, 'Text', (x, y-3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

    gray_plates = gray[y:y+h, x:x+w]
    color_plates = img[y:y+h, x:x+w]
    cv2.imwrite('img1.jpg',gray_plates)
    cv2.imshow('img', gray_plates)
    cv2.waitKey(0)

    height, width, chanel = gray_plates.shape


cv2.imshow('img', img)
cv2.waitKey(0)
print('Number of detected licence plates:', len(plates))
conn = sqlite3.connect('Form.db')
cursor = conn.cursor()
cursor.execute('delete from pl1')
filename='img1.jpg'
cursor.execute('INSERT INTO pl1( plate1) VALUES(?)',(filename,))
