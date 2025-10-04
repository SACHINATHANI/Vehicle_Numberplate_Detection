import sqlite3
import sys
import matplotlib as plt
from tkinter import *

from tkinter import ttk
import tkinter.filedialog
from tkinter.filedialog import askopenfilename # Open dialog box
from PIL import Image, ImageTk

import cv2, time

def open_File():

    filename = askopenfilename(filetypes=[("images","*.*")])
    img = cv2.imread(filename)
    conn = sqlite3.connect('Form.db')
    cursor = conn.cursor()
    cursor.execute('delete from imgsave')
    cursor.execute('INSERT INTO imgsave(img ) VALUES(?)',(filename,))

    conn.commit()
    cv2.imshow("Autism", img) # I used cv2 to show image
    cv2.waitKey(0)

#    filename.close()

rw = Tk()                              # Create window

rw.geometry('1366x768')
rw.title("Autism")
canv = Canvas(rw, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)

Label(rw, text='Select Image', width=14, bg='white', fg='red',font=("bold", 10)).place(x=500, y=400)

Button(rw, text='Browse Image', width=14, bg='brown', fg='white', command=open_File,font=("bold", 10)).place(x=650, y=400)

rw.mainloop()
