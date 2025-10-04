from tkinter import *
from tkinter.filedialog import askopenfilename

import cv2
from PIL import ImageTk, Image
import sqlite3
import os
root = Tk()
root.geometry('1366x768')
root.title("Veh")



canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back1.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
def capt():
    os.system('python captvideo.py')
def readimg():
    filename = askopenfilename(filetypes=[("images", "*.*")])
    img = cv2.imread(filename)
    conn = sqlite3.connect('Form.db')
    cursor = conn.cursor()
    cursor.execute('delete from imgsave')
    cursor.execute('INSERT INTO imgsave(img ) VALUES(?)', (filename,))

    conn.commit()
    cv2.imshow("Vehicle", img)  # I used cv2 to show image
    cv2.waitKey(0)
def preprocessing():
    os.system('python preprocessing.py')
def seg():
    os.system('python seg.py')
def featext():
    os.system('python featext.py')
def det():
    os.system('python locate.py')
Button(root, text='Capture Video', cursor="mouse",width=13, height=3,bg='#18A3AA', fg='black',font=('BOLD',12),command=capt).place(x=100, y=350)
Button(root, text='Input Image', cursor="mouse",width=13, height=3,bg='#18A3AA', fg='black',font=('BOLD',12),command=readimg).place(x=250, y=350)
Button(root, text='Preprocessing',cursor="mouse", width=14, height=3,bg='#18A3AA', fg='black',font=('BOLD',12),command=preprocessing).place(x=400, y=350)
Button(root, text='Segmentation',cursor="mouse", width=14, height=3,bg='#18A3AA', fg='black',command=seg,font=('BOLD',12)).place(x=550, y=350)
Button(root, text='Feature Extraction', cursor="mouse",width=14, height=3,bg='#18A3AA', command=featext,fg='black',font=('BOLD',12)).place(x=700, y=350)
Button(root, text='Number Plate Detection', cursor="mouse",width=20, height=3,bg='#18A3AA', command=det,fg='black',font=('BOLD',12)).place(x=850, y=350)






root.mainloop()
