from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from mehendi import *
from cocktail import *
from rituals import *

def events():
    # Create a window for the main Events page
    root = Tk()
    root.title("Events")
    root.minsize(width=400,height=400)
    root.geometry("1800x800")

    same=True
    n=0.25

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Select your \n Events ", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # Create buttons for each event (Mehendi, Rituals, Cocktail)
    mehendi_button = Button(labelFrame,text="Mehndi",bg='red', fg='white', command=mehendi)
    mehendi_button.place(relx=0.1,rely=0.4,relwidth=0.25,relheight=0.4)

    rituals_button = Button(labelFrame,text="Rituals",bg='red', fg='white', command=rituals)
    rituals_button.place(relx=0.40,rely=0.4,relwidth=0.25,relheight=0.4)

    cocktail_button = Button(labelFrame,text="Cocktail",bg='red', fg='white', command=cocktail)
    cocktail_button.place(relx=0.70,rely=0.4,relwidth=0.25,relheight=0.4)

    root.mainloop()