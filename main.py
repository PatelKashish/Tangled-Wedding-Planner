
from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from addClient import *

mypass = "16012003"
mydatabase = "tangled"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Tangled")
root.minsize(width=400, height=400)
root.geometry("1800x800")

# Take n greater than 0.25 and less than 5
same = True
n = 1

background_image = Image.open('bg2.png')
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n) 
if same:
    newImageSizeHeight = int(imageSizeHeight * n) 
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)
Canvas1.create_image(0, 0, anchor=NW, image=img)
Canvas1.config(bg="white", width=1800, height=800)
Canvas1.pack(expand=True, fill=BOTH)

# headingLabel = Label(root, text="Welcome to Tangled ",fg='navy',compound='center',font=('Lucida Calligraphy', 40))
# headingLabel.place(relx=0.21, rely=0, relwidth=.6, relheight=.1)
background_image = PhotoImage(file="login.png")  # Replace "background.png" with your image file path


btn1 = Button(root,image=background_image, font=('Lucida Calligraphy', 40),command=addclient)
btn1.place(relx=.4, rely=0.5, relwidth=0.35, relheight=0.45)



root.mainloop()
