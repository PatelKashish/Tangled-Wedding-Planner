from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from event import *
# from cocktail import *
# from rituals import *
# mypass = "16012003"
# mydatabase="tangled"

# con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
# cur = con.cursor()



def eventsdecoration():
    # Create a window for the main Events page
    root = Tk()
    root.title("Decoration")
    root.minsize(width=400,height=400)
    root.geometry("1800x800")

    same=True
    n=0.25

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Select your \n Events ", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    # btn1 = Button(root,text="",bg='black', fg='white', command=)
    # btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # Create buttons for each event (Mehendi, Rituals, Cocktail)
    mehendi_button = Button(labelFrame,text="Deco 1",bg='red', fg='white')
    mehendi_button.place(relx=0.1,rely=0.4,relwidth=0.25,relheight=0.4)

    rituals_button = Button(labelFrame,text="Deco 2",bg='red', fg='white')
    rituals_button.place(relx=0.40,rely=0.4,relwidth=0.25,relheight=0.4)

    cocktail_button = Button(labelFrame,text="Deco 3",bg='red', fg='white')
    cocktail_button.place(relx=0.70,rely=0.4,relwidth=0.25,relheight=0.4)

    root.destroy()