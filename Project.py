import cv2
from Tkinter import *
import PIL.Image
import PIL.ImageTk
import tkMessageBox

original_filename="a.bmp"

#Encryption
originalfile = open(original_filename,"rb")
encrypted=open("encrypted.bmp","wb")
i=0
for b in originalfile.read():
    if(i>53):
        encrypted.write(chr((ord(b)+100)%256))
    else:
        encrypted.write(b)
    i=i+1
encrypted.close()
originalfile.close()

#Decryption
filefor=open("encrypted.bmp","rb")
decryptedfile = open("decrypted.bmp","wb")
j=0
for b in filefor.read():
    if(j>53):
        #print ((ord(b)-100))%256
        decryptedfile.write(chr((ord(b)-100)%256))
    else:
        decryptedfile.write(b)
    j=j+1
filefor.close()
decryptedfile.close()

img = cv2.imread(original_filename)
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
cv2.imwrite("denoised.bmp", dst)

img1 = cv2.imread("encrypted.bmp")
dst1 = cv2.fastNlMeansDenoisingColored(img1,None,10,10,7,21)
cv2.imwrite("denoised1.bmp", dst)

filefor1=open("denoised1.bmp","rb")
decryptedfile1 = open("denoisedenc.bmp","wb")
j=0
for b in filefor1.read():
    if(j>53):
        #print ((ord(b)-100))%256
        decryptedfile1.write(chr((ord(b)-100)%256))
    else:
        decryptedfile1.write(b)
    j=j+1
filefor1.close()
decryptedfile1.close()


#Creating GUI
root = Tk()
root.title("Demonstration of Image Denoising in Encrypted Domain")
root.geometry("1370x700")

frame5=Frame(root)
frame5.pack(side=TOP)

frame6=Frame(root)
frame6.pack(side=BOTTOM)

#Frame for original image
frame2 = Frame(frame5, width=300, height=300)
frame2.pack(fill= None, expand =FALSE,side=TOP)
L1 = Label(frame2, text="Original Noisy Image")
L1.pack()

originalimg = PIL.Image.open(original_filename)
ratio=float(originalimg.size[0])/float(originalimg.size[1])
resized1 = originalimg.resize((300,int(300.00/ratio)),PIL.Image.ANTIALIAS)
resizedoriginalimage = PIL.ImageTk.PhotoImage(resized1)
container1 = Label(frame2, image = resizedoriginalimage)
container1.pack(fill= None, expand =FALSE)

#Frame for denoised image in encrypted domain
frame3 = Frame(frame6, width=300, height=300)
frame3.pack(fill=None, expand=FALSE,side=LEFT)
L2 = Label(frame3, text="Denoised Image in Encrypted Domain")
L2.pack()

#embededimg = PIL.Image.open("encrypted.bmp")
embededimg = PIL.Image.open("denoisedenc.bmp")
resized2 = embededimg.resize((300,int(300.00/ratio)), PIL.Image.ANTIALIAS)
resizedembededimage = PIL.ImageTk.PhotoImage(resized2)
container2 = Label(frame3, image=resizedembededimage)
container2.pack(fill=None, expand=FALSE)

#Frame for denoised image without encrypted domain
frame4 = Frame(frame6, width=300, height=300)
frame4.pack(fill=None, expand=FALSE,side=RIGHT)
L3 = Label(frame4, text="Denoised Image without Encrypted Domain")
L3.pack()

embededimg1 = PIL.Image.open("denoised.bmp")
resized3 = embededimg1.resize((300,int(300.00/ratio)), PIL.Image.ANTIALIAS)
resizedembededimage1 = PIL.ImageTk.PhotoImage(resized3)
container3 = Label(frame4, image=resizedembededimage1)
container3.pack(fill=None, expand=FALSE)

root.mainloop()

