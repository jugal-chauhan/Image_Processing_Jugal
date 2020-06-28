from tkinter import *
import tkinter as tk
from tkinter import filedialog, Text
from PIL import Image, ImageTk
#from Backend_v2 import mouse , warp_function, Get_Image, blur_function, ocr_function, save_img, auto_crop
import cv2
import numpy as np
import pytesseract 
from pytesseract import Output
import os

#Global Variables
og_img = np.zeros((), np.uint8)
cropped = np.zeros((), np.uint8)
ocr_image = np.zeros((), np.uint8)

text = ''

#GUI main loop
root = tk.Tk()
root.title('GUI for OCR')
canvas = tk.Canvas(root, height = 900, width = 1200, bg = "#662261")
canvas.pack()

frame = tk.Frame(root, bg = "#FFEDB5")
frame.place(relwidth = 0.6, relheight = 0.9, relx = 0.37, rely = 0.05)

text_box = tk.Frame(frame, bg="#FFBF00")
text_box.place(relwidth = 0.6, relheight = 0.6, relx = 0.2, rely = 0.2)

def open_btn_clicked():
    filename = filedialog.askopenfilename(initialdir = "/Users/jugal/covid/tkr/",title = 'Select an Image',filetypes = (('JPG','*.jpg'),('All files','*.*')))
    print(filename)

    global og_img
    og_img = cv2.imread(filename)
    cv2.imshow('IMAGE', og_img)
    Get_Image(og_img)

def blur_img():
    global cropped,og_img
    #image_gray=cv2.cvtColor(og_img,cv2.COLOR_BGR2GRAY)
    kernel=np.ones((2,2))
    gaussian_blur=cv2.GaussianBlur(og_img,(5,5),2)
    cropped=gaussian_blur.copy()
    cv2.imshow('BLUR',gaussian_blur)

def grayscale():
    global cropped,og_img
    image_gray=cv2.cvtColor(og_img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('GRAY',image_gray)

def hsv():
    global cropped,og_img
    img_hsv = cv2.cvtColor(og_img,cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV',img_hsv)

def auto_crop():
    global transform_auto, og_img

    img_gray = cv2.cvtColor(og_img, cv2.COLOR_BGR2GRAY)
    img_gray_smooth = cv2.GaussianBlur(img_gray,(5,5),0)
    ret,img_gray_smooth_thresh = cv2.threshold(img_gray_smooth,180,255,cv2.THRESH_BINARY)
    canny = cv2.Canny(img_gray_smooth_thresh,150, 300)

    contour, heirarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    areas = [cv2.contourArea(c) for c in contour]
    max_index = np.argmax(areas)
    max_contour = contour[max_index]

    perimeter = cv2.arcLength(max_contour, True)
    coordinates = cv2.approxPolyDP(max_contour, 0.01*perimeter, True)

    #cv2.drawContours(img, [coordinates], -1, (0,0,255), 5)

    pt1 = np.array([coordinates[1], coordinates[0], coordinates[2], coordinates[3]], np.float32)
    pt2 = np.array([(0,0), (700,0), (0,600) , (700,600)], np.float32)

    pers = cv2.getPerspectiveTransform(pt1, pt2)
    transform_auto = cv2.warpPerspective(og_img, pers, (700,600))
    #transform_auto = cv2.rotate(transform_auto, cv2.ROTATE_90_COUNTERCLOCKWISE)

    cv2.imshow('AUTO CROPPED', transform_auto)
    return(transform_auto)

def manual_crop():
    global transform_manual, og_img
    req_pts = []
    
    counter = 0

    def mouse_func(event, x, y, flags, param):
        
        if event == cv2.EVENT_LBUTTONDOWN:
            if (x,y) is not None:
                req_pts.append((x,y))
                # print((x,y))

            if len(req_pts) == 4:
                print(req_pts)
                req_pt = np.array([req_pts[0], req_pts[1], req_pts[3], req_pts[2]], np.float32)
                dst_pt = np.array([(0,0), (700,0), (0,600), (700,600)], np.float32)
                pers = cv2.getPerspectiveTransform(req_pt, dst_pt)
                transform_manual = cv2.warpPerspective(og_img, pers, (700,600)) 
                cv2.imshow('MANUAL CROP', transform_manual)
                return(transform_manual)
    cv2.namedWindow('Image')
    cv2.imshow('Image', og_img)
    cv2.setMouseCallback('Image', mouse_func)

def OCR_btn():
    
    global og_img, text, ocr_image
    ret,global_thresh=cv2.threshold(og_img,170,255,cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(global_thresh,lang= 'eng')
    data = pytesseract.image_to_data(global_thresh,output_type= Output.DICT)
    no_word = len(data['text'])

    for i in range(no_word):
        if int(data['conf'][i]) > 50:
            x,y,w,h = data['left'][i],data['top'][i],data['width'][i],data['height'][i]
            cv2.rectangle(global_thresh,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow('OCR',global_thresh)
            cv2.waitKey(200)
    'cropped=global_thresh.copy()'
    ocr_image = global_thresh.copy()

def show_text():
    global text
    textbox = tk.Frame(frame,bg = '#FDFFD6')
    textbox.place(relx = 0.2,rely = 0.2,relwidth =0.6,relheight =0.6)
    textframe = Text(textbox,bg = '#FDFFD6')
    textframe.insert('1.0',text)
    textframe.pack()

def save_img():
    global ocr_image
    filename = filedialog.asksaveasfilename(initialdir = "/Users/jugal/Desktop/Github/Image_Processing_jugal/Task_1", title = 'Save File', filetypes = (('JPG', '*.jpg'), ('All files','*.*')))
    print(filename)
    cv2.imwrite(filename, ocr_image)

def save_txt_file():
    f = open("ocr_text.txt", "w")
    f.write(text)
    f.close()
    print("done")
    f = open("ocr_text.txt", "r")
    print(f.read())

def Close_All_Windows():
    cv2.destroyAllWindows()

label=tk.Label(frame,text='GUI for OCR',fg='black',bg='white',font=('Bold',20))
label.place(relx=0.3,rely=0.1)

open_btn = tk.Button(canvas,text = 'Open Image',fg = 'black',padx = 5,pady = 5, command = open_btn_clicked)
open_btn.place(relx=0.04,rely=0.05)

blur_img_btn=tk.Button(canvas,text='Blur Image',fg = 'black',padx = 5,pady = 5, command = blur_img)
blur_img_btn.place(relx=0.04,rely=0.15)

auto_crop_btn=tk.Button(canvas,text='Auto Crop',fg = 'black',padx = 5,pady = 5, command = auto_crop)
auto_crop_btn.place(relx=0.04,rely=0.25)

manual_crop_btn=tk.Button(canvas,text='Manual Crop',fg = 'black',padx = 5,pady = 5, command = manual_crop)
manual_crop_btn.place(relx=0.04,rely=0.35)

g_btn=tk.Button(canvas,text='Gray Image',fg = 'black',padx = 5,pady = 5, command = grayscale)
g_btn.place(relx=0.04,rely=0.45)

h_btn=tk.Button(canvas,text='Gray Image',fg = 'black',padx = 5,pady = 5, command = hsv)
h_btn.place(relx=0.04,rely=0.55)

OCR_btn=tk.Button(canvas,text='OCR',fg = 'black',padx = 5,pady = 5, command = OCR_btn)
OCR_btn.place(relx=0.04,rely=0.65)

show_text_btn=tk.Button(canvas,text='Show text',fg = 'black',padx = 5,pady = 5, command = show_text)
show_text_btn.place(relx=0.04,rely=0.75)

save_img_btn=tk.Button(canvas,text='Save Image',fg = 'black',padx = 5,pady = 5, command = save_img)
save_img_btn.place(relx=0.04,rely=0.85)

save_btn = tk.Button(canvas, text='save as .txt', fg = 'black',padx = 5,pady = 5, command=save_txt_file)
save_btn.place(relx=0.04, rely=0.95)

Close_All_Windows_btn = tk.Button(canvas, text = 'Close All Windows', fg = 'black', padx = 5, pady = 5, command = Close_All_Windows)
Close_All_Windows_btn.place(relx = 0, rely = 0)

root.mainloop()