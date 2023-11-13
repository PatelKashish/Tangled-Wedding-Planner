import pymysql
import mysql.connector
from tkinter import *
from PIL import ImageTk, Image
from addc import *
from tkinter import ttk 
from tkcalendar import DateEntry

def generate_client_id():
    
    mypass = "16012003"
    mydatabase="tangled"

    con = mysql.connector.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    sql_query = "SELECT client_id FROM Client ORDER BY client_id DESC LIMIT 1"
    
    # Execute the query
    cur.execute(sql_query)

    # Fetch the result
    result = cur.fetchone()

    # Close the database connection
    con.close()

    # Check if a result was returned and print the primary key value
    if result:
        primary_key_value = result[0]
        # print("The primary key value of the last row is:", primary_key_value)
    else:
        # print("No rows found in the table.")
        c_id = "C001"
        return c_id
    
    counter = primary_key_value[1:]
    counter = int(counter) + 1
    # print("new counter :",counter)
    c_id = 'C' + str(counter).zfill(3)
    return c_id

def create_root():

    # def destroy():
        # addclient()
        # # lable.destroy()
        # button.destroy()
        
    # root = Tk()
    # root.state('zoomed')
    # root.title("Tangled")
    # same = True
    # n = 1

    background_image = Image.open('bg2.png')
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth * 1.1)
    newImageSizeHeight = int(imageSizeHeight * 1.07)
    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
    bg_label = Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    # Load the background image
    # bg_image = PhotoImage(file="bg2.png")  # Replace "background.png" with your image file
    # bg_label = Label(root, image=bg_image)
    # bg_label.place(relwidth=1, relheight=1)

    # btn1 = Button(root, text="Say Yes!", font=('Lucida Calligraphy', 40), command=destroy)
    # btn1 = Button(root, text="Say Yes!", font=('Lucida Calligraphy', 40), command=addclient)
    btn1 = Button(root, text="Say Yes!", font=('Lucida Calligraphy', 40), command=events)

    btn1.place(relx=.4, rely=0.8, relwidth=0.20, relheight=0.1)
    root.mainloop()

def clientSignup():
    print("signup")

def clientlogin():
    
    global counter 
    client_id = generate_client_id()
    fname = clientfn.get()
    mname = clientmn.get()
    lname = clientln.get()
    phone_no = clientpn.get()
    email = clientemail.get()
    password = clientpwd.get()
    role = "user"
    
    # Role = Role.lower()
    try:
        clientInfo = "INSERT INTO Client VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(clientInfo, (client_id, fname, mname, lname, email, password, role))

        insert_phone = "INSERT INTO phone_no (client_id, phone_no) VALUES (%s, %s)"
        cur.execute(insert_phone, (client_id, phone_no))
        con.commit()

        messagebox.showinfo('Success', "User added successfully, your id is: " + str(client_id))
        events()
        
    except Exception as e:
        messagebox.showinfo("Error", f"Can't add data into Database: {str(e)}")
        print(e)

    # root.destroy()

def addclient():

    # lable.destroy()
    # button.destroy()
    global clientid, clientfn, clientmn, clientln, clientpn, clientemail, clientpwd, role
    global root, Canvas1, con, cur, ClientTable

    # root = Tk()
    # root.state('zoomed')
    # root.title("Client Login")
    # root.minsize(width=400,height=400)
    # root.geometry("1800x800")

    mypass = "16012003"
    mydatabase="tangled"

    con = mysql.connector.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    ClientTable = "Client"

    background_image = Image.open('lbg.png')
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth * 0.8)
    newImageSizeHeight = int(imageSizeHeight * 0.75)
    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
    bg_label = Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)
    

    # Client_ID Signup
    lb01 = Label(root, text="Client_id : ", bg='white', fg='black',font=('Lucida Calligraphy', 16))
    lb01.place(relx=0.05, rely=0.38,relwidth=0.1, relheight=0.08)     
    client_ID = Entry(root, bg='white',fg='black')
    client_ID.place(relx=0.2,rely=0.38, relwidth=0.25, relheight=0.08)

    # Client_PWD Signup
    lb02 = Label(root, text="Password : ", bg='white', fg='black',font=('Lucida Calligraphy', 16))
    lb02.place(relx=0.05,rely=0.51,relwidth=0.1, relheight=0.08)   
    client_PWD = Entry(root, bg='white',fg='black')
    client_PWD.place(relx=0.2,rely=0.51, relwidth=0.25, relheight=0.08)

    # F Name
    lb1 = Label(root, text="First Name : ", bg='black', fg='white',font=('Lucida Calligraphy', 12))
    lb1.place(relx=0.55, rely=0.38,relwidth=0.1, relheight=0.05)     
    clientfn = Entry(root, bg='black',fg='white')
    clientfn.place(relx=0.7,rely=0.38, relwidth=0.25, relheight=0.05)

    # M Name
    lb2 = Label(root, text="Middle Name : ", bg='black', fg='white',font=('Lucida Calligraphy', 12))
    lb2.place(relx=0.55,rely=0.45,relwidth=0.1, relheight=0.05)   
    clientmn = Entry(root, bg='black',fg='white')
    clientmn.place(relx=0.7,rely=0.45, relwidth=0.25, relheight=0.05)

    # L Name 
    lb3 = Label(root,text="Last Name : ", bg='black', fg='white',font=('Lucida Calligraphy', 12))
    lb3.place(relx=0.55,rely=0.52,relwidth=0.1, relheight=0.05)  
    clientln = Entry(root,bg='black',fg='white')
    clientln.place(relx=0.7,rely=0.52, relwidth=0.25, relheight=0.05)

    # Phone Number
    lb4 = Label(root,text="Phone Number : ", bg='black', fg='white',font=('Lucida Calligraphy', 12))
    lb4.place(relx=0.55,rely=0.59,relwidth=0.1, relheight=0.05)
    clientpn = Entry(root, bg='black',fg='white')
    clientpn.place(relx=0.7,rely=0.59, relwidth=0.25, relheight=0.05)

    # Email
    lb5 = Label(root,text="Email : ", bg='black', fg='white',font=('Lucida Calligraphy', 12))
    lb5.place(relx=0.55,rely=0.66,relwidth=0.1, relheight=0.05)   
    clientemail = Entry(root,bg='black',fg='white')
    clientemail.place(relx=0.7,rely=0.66, relwidth=0.25, relheight=0.05)

    # Password
    lb6 = Label(root,text="Password : ", bg='black', fg='white',font=('Lucida Calligraphy', 12))
    lb6.place(relx=0.55,rely=0.73,relwidth=0.1, relheight=0.05)
    clientpwd = Entry(root, show = "*",bg='black',fg='white',font=('Lucida Calligraphy', 12))
    clientpwd.place(relx=0.7,rely=0.73, relwidth=0.25, relheight=0.05)

    #Submit Button

    SignupBtn = Button(root,text="Your Bookings", fg='black',bg='white',font=('Lucida Calligraphy', 20), command=clientSignup)
    SignupBtn.place(relx=0.155,rely=0.65, relwidth=0.2,relheight=0.07)

    SubmitBtn = Button(root,text="Get Started", fg='white',bg='black',font=('Lucida Calligraphy', 20), command=clientlogin)
    SubmitBtn.place(relx=0.655,rely=0.85, relwidth=0.2,relheight=0.07)
    
    root.mainloop()

def events():

    same = True
    n = 1.8
    # root = Tk()
    # root.title("Events")
    # root.state('zoomed')
    # root.minsize(width=400, height=400)
    # root.geometry("1800x800")

    background_image = Image.open('Eventbg.png')
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth * 1.78)
    newImageSizeHeight = int(imageSizeHeight * 1.5)
    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
    bg_label = Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    mehendi_image = Image.open('mehendi.png')
    mehendi_image = mehendi_image.resize((400, 250))
    mehendi_photo = ImageTk.PhotoImage(mehendi_image)    
    label1 = Label(root, image=mehendi_photo)
    label1.place(relx=0.07, rely=0.4, relwidth=0.25, relheight=0.3)

    rituals_image = Image.open('rituals.png')
    rituals_image = rituals_image.resize((400, 250))
    rituals_photo = ImageTk.PhotoImage(rituals_image)
    label2 = Label(root, image=rituals_photo)
    label2.place(relx=0.37, rely=0.4, relwidth=0.25, relheight=0.3)

    cocktail_image = Image.open('cocktail.png')
    cocktail_image = cocktail_image.resize((400, 250))
    cocktail_photo = ImageTk.PhotoImage(cocktail_image)
    label3 = Label(root, image=cocktail_photo)
    label3.place(relx=0.67, rely=0.4, relwidth=0.25, relheight=0.3)
    
    mehendi_button = Button(root, text="Mehendi", bg='black', fg='white', command=mehendi, font=('Lucida Calligraphy', 15))
    mehendi_button.place(relx=0.07, rely=0.75, relwidth=0.25, relheight=0.1)

    rituals_button = Button(root, text="Rituals", bg='black', fg='white', command=rituals, font=('Lucida Calligraphy', 15))
    rituals_button.place(relx=0.37, rely=0.75, relwidth=0.25, relheight=0.1)

    cocktail_button = Button(root, text="Cocktail", bg='black', fg='white', command=cocktail, font=('Lucida Calligraphy', 15))
    cocktail_button.place(relx=0.67, rely=0.75, relwidth=0.25, relheight=0.1)

    root.mainloop()

def mehendi():

    def decobtn1():

        background_image = Image.open('deco1.png')
        [imageSizeWidth, imageSizeHeight] = background_image.size
        newImageSizeWidth = int(imageSizeWidth * 0.8)
        newImageSizeHeight = int(imageSizeHeight * 0.8)
        background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
        bg_label = Label(root, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        btn = Button(root,text="Return", font=('Lucida Calligraphy', 26), bg='black', fg='white', command=mehendi)
        btn.place(relx=0.2,rely=0.75, relwidth=0.2,relheight=0.07)

        root.mainloop()

    def decobtn2():

        background_image = Image.open('deco2.png')
        [imageSizeWidth, imageSizeHeight] = background_image.size
        newImageSizeWidth = int(imageSizeWidth * 0.8)
        newImageSizeHeight = int(imageSizeHeight * 0.8)
        background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
        bg_label = Label(root, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        btn = Button(root,text="Return", font=('Lucida Calligraphy', 26), bg='black', fg='white', command=mehendi)
        btn.place(relx=0.2,rely=0.75, relwidth=0.2,relheight=0.07)

        root.mainloop()

    def decobtn3():

        background_image = Image.open('deco3.png')
        [imageSizeWidth, imageSizeHeight] = background_image.size
        newImageSizeWidth = int(imageSizeWidth * 0.8)
        newImageSizeHeight = int(imageSizeHeight * 0.8)
        background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
        bg_label = Label(root, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        btn = Button(root,text="Return", font=('Lucida Calligraphy', 26), bg='black', fg='white', command=mehendi)
        btn.place(relx=0.2,rely=0.75, relwidth=0.2,relheight=0.07)

        root.mainloop()

    def decobtn4():

        background_image = Image.open('deco4.png')
        [imageSizeWidth, imageSizeHeight] = background_image.size
        newImageSizeWidth = int(imageSizeWidth * 0.8)
        newImageSizeHeight = int(imageSizeHeight * 0.8)
        background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
        bg_label = Label(root, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        btn = Button(root,text="Return", font=('Lucida Calligraphy', 26), bg='black', fg='white', command=mehendi)
        btn.place(relx=0.2,rely=0.75, relwidth=0.2,relheight=0.07)
        root.mainloop()

    mypass = "16012003"
    mydatabase = "tangled"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    
    background_image = Image.open('mbg3.png')
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth * 1.5)
    newImageSizeHeight = int(imageSizeHeight * 1.5)
    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
    bg_label = Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    # btn1 = Button(root,text="Decorate Venue", font=('Lucida Calligraphy', 40),command=eventsdecoration)
    # btn1.place(relx=.525, rely=0.8, relwidth=0.20, relheight=0.1)
    # btn1.attributes('-alpha',0.4)

    def on_entry_click(event):
        if time_e.get() == "HH:MM:SS":
            time_e.delete(0, "end")
            time_e.config(fg='grey')  # Change text color to black

    def on_focus_out(event):
        if time_e.get() == "":
            time_e.insert(0, "HH:MM:SS")
            time_e.config(fg='grey')  # Change text color to grey

    
    # Date
    date = Label(root, text="Date : ", bg='white', fg='black',font=('Lucida Calligraphy', 16))
    date.place(relx=0.05, rely=0.25,relwidth=0.1, relheight=0.08)
    date_e = DateEntry(root, bg='white',fg='black',font=('Lucida Calligraphy', 16))
    date_e.place(relx=0.2,rely=0.25, relwidth=0.25, relheight=0.08)

    # Time
    time = Label(root, text="Time : ", bg='white', fg='black',font=('Lucida Calligraphy', 16))
    time.place(relx=0.05, rely=0.38,relwidth=0.1, relheight=0.08)     
    time_e = Entry(root, bg='white',fg='black',font=('Lucida Calligraphy', 16))
    time_e.insert(0, "HH:MM:SS")
    time_e.bind("<FocusIn>", on_entry_click)
    time_e.bind("<FocusOut>", on_focus_out)
    time_e.place(relx=0.2,rely=0.38, relwidth=0.25, relheight=0.08)

    # Location
    lb02 = Label(root, text="Location : ", bg='white', fg='black',font=('Lucida Calligraphy', 16))
    lb02.place(relx=0.05,rely=0.51,relwidth=0.1, relheight=0.08)   
    choices = ["Bengaluru", "Udaipur", "Goa", "Ahmedabad", "Mumbai"]
    selected_location = StringVar(value=choices[0])
    location_dropdown = ttk.Combobox(root, textvariable=selected_location, values=choices,font=('Lucida Calligraphy', 16) )
    location_dropdown.place(relx=0.2,rely=0.51, relwidth=0.25, relheight=0.08)

    # Decorations 
    lb03 = Label(root, text="Decoration : ", bg='white', fg='black',font=('Lucida Calligraphy', 16))
    lb03.place(relx=0.05,rely=0.64,relwidth=0.1, relheight=0.08)   
    decos = ["Crimson And Cupid's Connections", "Marigold Magic", "Mint To Be", "Vows And Purple Wows"]
    selected_deco = StringVar(value=decos[0])
    location_deco = ttk.Combobox(root, textvariable=selected_deco, values=decos,font=('Lucida Calligraphy', 16) )
    location_deco.place(relx=0.2,rely=0.64, relwidth=0.25, relheight=0.08)

    bookV = Button(root,text="Book venue", fg='black',bg='white',font=('Lucida Calligraphy', 20)) #command=clientSignup
    bookV.place(relx=0.155,rely=0.78, relwidth=0.2,relheight=0.07)

    deco1 = Image.open('MarigoldMagic.png')
    deco1 = deco1.resize((300, 400))
    deco_1 = ImageTk.PhotoImage(deco1)  
    # label1 = Label(root, image=deco_1)  
    label1 = Button(root, image=deco_1, command=decobtn1)
    label1.place(relx=0.5, rely=0.1, relwidth=0.15, relheight=0.4)

    deco2 = Image.open('MintToBe.png')
    deco2 = deco2.resize((264, 405))
    deco_2 = ImageTk.PhotoImage(deco2)
    label2 = Button(root, image=deco_2, command=decobtn2)
    label2.place(relx=0.75, rely=0.1, relwidth=0.15, relheight=0.4)

    deco3 = Image.open('VowsAndPurpleWows.png')
    deco3 = deco3.resize((264, 405))
    deco_3 = ImageTk.PhotoImage(deco3)
    label3 = Button(root, image=deco_3, command=decobtn3)
    label3.place(relx=0.5, rely=0.55, relwidth=0.15, relheight=0.4)

    deco4 = Image.open('CCConnections.png')
    deco4 = deco4.resize((223, 350))
    deco_4 = ImageTk.PhotoImage(deco4)
    label4 = Button(root, image=deco_4, command=decobtn4)
    label4.place(relx=0.75, rely=0.55, relwidth=0.15, relheight=0.4)

    root.mainloop()

def cocktail():

    mypass = "16012003"
    mydatabase = "tangled"
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    def decobtn1():

        background_image = Image.open('deco1.png')
        [imageSizeWidth, imageSizeHeight] = background_image.size
        newImageSizeWidth = int(imageSizeWidth * 0.8)
        newImageSizeHeight = int(imageSizeHeight * 0.8)
        background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
        bg_label = Label(root, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        btn = Button(root,text="Return", font=('Lucida Calligraphy', 26), bg='black', fg='white', command=cocktail)
        btn.place(relx=0.2,rely=0.75, relwidth=0.2,relheight=0.07)

        root.mainloop()

    def decobtn2():

        background_image = Image.open('deco2.png')
        [imageSizeWidth, imageSizeHeight] = background_image.size
        newImageSizeWidth = int(imageSizeWidth * 0.8)
        newImageSizeHeight = int(imageSizeHeight * 0.8)
        background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
        bg_label = Label(root, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        btn = Button(root,text="Return", font=('Lucida Calligraphy', 26), bg='black', fg='white', command=cocktail)
        btn.place(relx=0.2,rely=0.75, relwidth=0.2,relheight=0.07)

        root.mainloop()

    def decobtn3():

        background_image = Image.open('deco3.png')
        [imageSizeWidth, imageSizeHeight] = background_image.size
        newImageSizeWidth = int(imageSizeWidth * 0.8)
        newImageSizeHeight = int(imageSizeHeight * 0.8)
        background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
        bg_label = Label(root, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        btn = Button(root,text="Return", font=('Lucida Calligraphy', 26), bg='black', fg='white', command=cocktail)
        btn.place(relx=0.2,rely=0.75, relwidth=0.2,relheight=0.07)

        root.mainloop()

    def decobtn4():

        background_image = Image.open('deco4.png')
        [imageSizeWidth, imageSizeHeight] = background_image.size
        newImageSizeWidth = int(imageSizeWidth * 0.8)
        newImageSizeHeight = int(imageSizeHeight * 0.8)
        background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
        bg_label = Label(root, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        btn = Button(root,text="Return", font=('Lucida Calligraphy', 26), bg='black', fg='white', command=cocktail)
        btn.place(relx=0.2,rely=0.75, relwidth=0.2,relheight=0.07)
        root.mainloop()

    mypass = "16012003"
    mydatabase = "tangled"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    
    background_image = Image.open('cbg.png')
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth * 0.8)
    newImageSizeHeight = int(imageSizeHeight * 0.8)
    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
    bg_label = Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    # btn1 = Button(root,text="Decorate Venue", font=('Lucida Calligraphy', 40),command=eventsdecoration)
    # btn1.place(relx=.525, rely=0.8, relwidth=0.20, relheight=0.1)
    # btn1.attributes('-alpha',0.4)

    def on_entry_click(event):
        if time_e.get() == "HH:MM:SS":
            time_e.delete(0, "end")
            time_e.config(fg='grey')  # Change text color to black

    def on_focus_out(event):
        if time_e.get() == "":
            time_e.insert(0, "HH:MM:SS")
            time_e.config(fg='grey')  # Change text color to grey

    
    # Date
    date = Label(root, text="Date : ", bg='white', fg='black',font=('Lucida Calligraphy', 16))
    date.place(relx=0.05, rely=0.25,relwidth=0.1, relheight=0.08)
    date_e = DateEntry(root, bg='white',fg='black',font=('Lucida Calligraphy', 16))
    date_e.place(relx=0.2,rely=0.25, relwidth=0.25, relheight=0.08)

    # Time
    time = Label(root, text="Time : ", bg='white', fg='black',font=('Lucida Calligraphy', 16))
    time.place(relx=0.05, rely=0.38,relwidth=0.1, relheight=0.08)     
    time_e = Entry(root, bg='white',fg='black',font=('Lucida Calligraphy', 16))
    time_e.insert(0, "HH:MM:SS")
    time_e.bind("<FocusIn>", on_entry_click)
    time_e.bind("<FocusOut>", on_focus_out)
    time_e.place(relx=0.2,rely=0.38, relwidth=0.25, relheight=0.08)

    # Location
    lb02 = Label(root, text="Location : ", bg='white', fg='black',font=('Lucida Calligraphy', 16))
    lb02.place(relx=0.05,rely=0.51,relwidth=0.1, relheight=0.08)   
    choices = ["Bengaluru", "Udaipur", "Goa", "Ahmedabad", "Mumbai"]
    selected_location = StringVar(value=choices[0])
    location_dropdown = ttk.Combobox(root, textvariable=selected_location, values=choices,font=('Lucida Calligraphy', 16) )
    location_dropdown.place(relx=0.2,rely=0.51, relwidth=0.25, relheight=0.08)

    # Decorations 
    lb03 = Label(root, text="Decoration : ", bg='white', fg='black',font=('Lucida Calligraphy', 16))
    lb03.place(relx=0.05,rely=0.64,relwidth=0.1, relheight=0.08)   
    decos = ["Crimson And Cupid's Connections", "Marigold Magic", "Mint To Be", "Vows And Purple Wows"]
    selected_deco = StringVar(value=decos[0])
    location_deco = ttk.Combobox(root, textvariable=selected_deco, values=decos,font=('Lucida Calligraphy', 16) )
    location_deco.place(relx=0.2,rely=0.64, relwidth=0.25, relheight=0.08)

    bookV = Button(root,text="Book venue", fg='black',bg='white',font=('Lucida Calligraphy', 20)) #command=clientSignup
    bookV.place(relx=0.155,rely=0.78, relwidth=0.2,relheight=0.07)

    deco1 = Image.open('MarigoldMagic.png')
    deco1 = deco1.resize((300, 400))
    deco_1 = ImageTk.PhotoImage(deco1)  
    # label1 = Label(root, image=deco_1)  
    label1 = Button(root, image=deco_1, command=decobtn1)
    label1.place(relx=0.5, rely=0.1, relwidth=0.15, relheight=0.4)

    deco2 = Image.open('MintToBe.png')
    deco2 = deco2.resize((264, 405))
    deco_2 = ImageTk.PhotoImage(deco2)
    label2 = Button(root, image=deco_2, command=decobtn2)
    label2.place(relx=0.75, rely=0.1, relwidth=0.15, relheight=0.4)

    deco3 = Image.open('VowsAndPurpleWows.png')
    deco3 = deco3.resize((264, 405))
    deco_3 = ImageTk.PhotoImage(deco3)
    label3 = Button(root, image=deco_3, command=decobtn3)
    label3.place(relx=0.5, rely=0.55, relwidth=0.15, relheight=0.4)

    deco4 = Image.open('CCConnections.png')
    deco4 = deco4.resize((223, 350))
    deco_4 = ImageTk.PhotoImage(deco4)
    label4 = Button(root, image=deco_4, command=decobtn4)
    label4.place(relx=0.75, rely=0.55, relwidth=0.15, relheight=0.4)

    root.mainloop()

def rituals():
    same = True
    n = 1.6    
    mypass = "16012003"
    mydatabase = "tangled"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    
    def decobtn1():

        background_image = Image.open('deco1.png')
        [imageSizeWidth, imageSizeHeight] = background_image.size
        newImageSizeWidth = int(imageSizeWidth * 0.8)
        newImageSizeHeight = int(imageSizeHeight * 0.8)
        background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
        bg_label = Label(root, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        btn = Button(root,text="Return", font=('Lucida Calligraphy', 26), bg='black', fg='white', command=rituals)
        btn.place(relx=0.2,rely=0.75, relwidth=0.2,relheight=0.07)

        root.mainloop()

    def decobtn2():

        background_image = Image.open('deco2.png')
        [imageSizeWidth, imageSizeHeight] = background_image.size
        newImageSizeWidth = int(imageSizeWidth * 0.8)
        newImageSizeHeight = int(imageSizeHeight * 0.8)
        background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
        bg_label = Label(root, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        btn = Button(root,text="Return", font=('Lucida Calligraphy', 26), bg='black', fg='white', command=rituals)
        btn.place(relx=0.2,rely=0.75, relwidth=0.2,relheight=0.07)

        root.mainloop()

    def decobtn3():

        background_image = Image.open('deco3.png')
        [imageSizeWidth, imageSizeHeight] = background_image.size
        newImageSizeWidth = int(imageSizeWidth * 0.8)
        newImageSizeHeight = int(imageSizeHeight * 0.8)
        background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
        bg_label = Label(root, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        btn = Button(root,text="Return", font=('Lucida Calligraphy', 26), bg='black', fg='white', command=rituals)
        btn.place(relx=0.2,rely=0.75, relwidth=0.2,relheight=0.07)

        root.mainloop()

    def decobtn4():

        background_image = Image.open('deco4.png')
        [imageSizeWidth, imageSizeHeight] = background_image.size
        newImageSizeWidth = int(imageSizeWidth * 0.8)
        newImageSizeHeight = int(imageSizeHeight * 0.8)
        background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
        bg_label = Label(root, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        btn = Button(root,text="Return", font=('Lucida Calligraphy', 26), bg='black', fg='white', command=rituals)
        btn.place(relx=0.2,rely=0.75, relwidth=0.2,relheight=0.07)
        root.mainloop()

    mypass = "16012003"
    mydatabase = "tangled"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    
    background_image = Image.open('rbg3.png')
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth * 0.8)
    newImageSizeHeight = int(imageSizeHeight * 0.8)
    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(background_image)  # Replace "background.png" with your image file
    bg_label = Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    # btn1 = Button(root,text="Decorate Venue", font=('Lucida Calligraphy', 40),command=eventsdecoration)
    # btn1.place(relx=.525, rely=0.8, relwidth=0.20, relheight=0.1)
    # btn1.attributes('-alpha',0.4)

    def on_entry_click(event):
        if time_e.get() == "HH:MM:SS":
            time_e.delete(0, "end")
            time_e.config(fg='grey')  # Change text color to black

    def on_focus_out(event):
        if time_e.get() == "":
            time_e.insert(0, "HH:MM:SS")
            time_e.config(fg='grey')  # Change text color to grey

    
    # Date
    date = Label(root, text="Date : ",bg='black', fg='white',font=('Lucida Calligraphy', 16))
    date.place(relx=0.05, rely=0.25,relwidth=0.1, relheight=0.08)
    date_e = DateEntry(root, bg='white',fg='black',font=('Lucida Calligraphy', 16))
    date_e.place(relx=0.2,rely=0.25, relwidth=0.25, relheight=0.08)

    # Time
    time = Label(root, text="Time : ",bg='black', fg='white',font=('Lucida Calligraphy', 16))
    time.place(relx=0.05, rely=0.38,relwidth=0.1, relheight=0.08)     
    time_e = Entry(root, bg='white',fg='black',font=('Lucida Calligraphy', 16))
    time_e.insert(0, "HH:MM:SS")
    time_e.bind("<FocusIn>", on_entry_click)
    time_e.bind("<FocusOut>", on_focus_out)
    time_e.place(relx=0.2,rely=0.38, relwidth=0.25, relheight=0.08)

    # Location
    lb02 = Label(root, text="Location : ",bg='black', fg='white',font=('Lucida Calligraphy', 16))
    lb02.place(relx=0.05,rely=0.51,relwidth=0.1, relheight=0.08)   
    choices = ["Bengaluru", "Udaipur", "Goa", "Ahmedabad", "Mumbai"]
    selected_location = StringVar(value=choices[0])
    location_dropdown = ttk.Combobox(root, textvariable=selected_location, values=choices,font=('Lucida Calligraphy', 16) )
    location_dropdown.place(relx=0.2,rely=0.51, relwidth=0.25, relheight=0.08)

    # Decorations 
    lb03 = Label(root, text="Decoration : ", bg='black', fg='white',font=('Lucida Calligraphy', 16))
    lb03.place(relx=0.05,rely=0.64,relwidth=0.1, relheight=0.08)   
    decos = ["Crimson And Cupid's Connections", "Marigold Magic", "Mint To Be", "Vows And Purple Wows"]
    selected_deco = StringVar(value=decos[0])
    location_deco = ttk.Combobox(root, textvariable=selected_deco, values=decos,font=('Lucida Calligraphy', 16) )
    location_deco.place(relx=0.2,rely=0.64, relwidth=0.25, relheight=0.08)

    bookV = Button(root,text="Book venue",bg='black', fg='white',font=('Lucida Calligraphy', 20)) #command=clientSignup
    bookV.place(relx=0.155,rely=0.78, relwidth=0.2,relheight=0.07)

    deco1 = Image.open('MarigoldMagic.png')
    deco1 = deco1.resize((300, 400))
    deco_1 = ImageTk.PhotoImage(deco1)  
    # label1 = Label(root, image=deco_1)  
    label1 = Button(root, image=deco_1, command=decobtn1)
    label1.place(relx=0.5, rely=0.1, relwidth=0.15, relheight=0.4)

    deco2 = Image.open('MintToBe.png')
    deco2 = deco2.resize((264, 405))
    deco_2 = ImageTk.PhotoImage(deco2)
    label2 = Button(root, image=deco_2, command=decobtn2)
    label2.place(relx=0.75, rely=0.1, relwidth=0.15, relheight=0.4)

    deco3 = Image.open('VowsAndPurpleWows.png')
    deco3 = deco3.resize((264, 405))
    deco_3 = ImageTk.PhotoImage(deco3)
    label3 = Button(root, image=deco_3, command=decobtn3)
    label3.place(relx=0.5, rely=0.55, relwidth=0.15, relheight=0.4)

    deco4 = Image.open('CCConnections.png')
    deco4 = deco4.resize((223, 350))
    deco_4 = ImageTk.PhotoImage(deco4)
    label4 = Button(root, image=deco_4, command=decobtn4)
    label4.place(relx=0.75, rely=0.55, relwidth=0.15, relheight=0.4)

    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.state('zoomed')
    root.title("Tangled")
    root.minsize(width=400, height=400)
    root.geometry("1800x800")
    root = create_root()
    # root.mainloop()
