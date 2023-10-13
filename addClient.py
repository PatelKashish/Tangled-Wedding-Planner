from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from event import *

def generate_client_id():
    mypass = "16012003"
    mydatabase="tangled"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    sql_query = "SELECT client_id FROM Client ORDER BY client_id DESC LIMIT 1"
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
        print("The primary key value of the last row is:", primary_key_value)
    else:
        print("No rows found in the table.")
        c_id = "C001"
        return c_id
    counter = primary_key_value[1:]
    counter = int(counter) + 1
    print("new counter :",counter)
    c_id = 'C' + str(counter).zfill(3)
    return c_id

def clientlogin():

    # mypass = "16012003"
    # mydatabase="tangled"

    # con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    # cur = con.cursor()
    # sql_query = "SELECT f_name FROM Client ORDER BY f_name DESC LIMIT 1"
    # cur.execute(sql_query)

    # result = cur.fetchone()
    # con.close()
    # C_text = StringVar()
    # C_text.set(Fname)

    root = Tk()
    root.title("Ready to Plan your Event")
    root.minsize(width=400,height=400)
    root.geometry("1800x800")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Welcome to Tangled ",fg='navy',compound='center',font=('Lucida Calligraphy', 40))
    headingLabel.place(relx=0.25, rely=0, relwidth=.6, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # ClientLabel = Label(labelFrame, textvariable=C_text,fg='navy',compound='center',font=('Lucida Calligraphy', 40))
    # ClientLabel.place(relx=0.21, rely=.3, relwidth=.6, relheight=1)

    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=events)
    SubmitBtn.place(relx=0.28,rely=0.7, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.7, relwidth=0.18,relheight=0.08)

    global counter 
    Client_id = generate_client_id()
    Fname = clientfn.get()
    Mname = clientmn.get()
    Lname = clientln.get()
    Phone_No = clientpn.get()
    Email = clientemail.get()
    Password = clientpwd.get()
    Role = "user"
    
    # Role = Role.lower()
    clientInfo = "INSERT INTO Client VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        cur.execute(clientInfo, (Client_id, Fname, Mname, Lname, Phone_No, Email, Password, Role))
        # con.commit()

        # messagebox.showinfo('Success', "User added successfully")
    except Exception as e:
        # messagebox.showinfo("Error", f"Can't add data into Database: {str(e)}")
        print(e)
    

    print(Client_id)
    print(Fname)
    print(Mname)
    print(Lname)
    print(Role)

    # root.mainloop()
    root.destroy()

def addclient():

    global clientid,clientfn,clientmn,clientln,clientpn,clientemail,clientpwd,role
    global root,Canvas1,con,cur,ClientTable

    root = Tk()
    root.title("Client Login")
    root.minsize(width=400,height=400)
    root.geometry("1800x800")

    mypass = "16012003"
    mydatabase="tangled"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    ClientTable = "Client"

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Client Login", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    # F name
    lb1 = Label(labelFrame,text="F Name : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)     
    clientfn = Entry(labelFrame)
    clientfn.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)  
    # M Name
    lb2 = Label(labelFrame,text="M Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)   
    clientmn = Entry(labelFrame)
    clientmn.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08) 
    # L Name 
    lb3 = Label(labelFrame,text="L Name : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.40, relheight=0.08)  
    clientln = Entry(labelFrame)
    clientln.place(relx=0.3,rely=0.40, relwidth=0.62, relheight=0.08) 
    # Phone Number
    lb4 = Label(labelFrame,text="Phone Number : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.5, relheight=0.08)
    clientpn = Entry(labelFrame)
    clientpn.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08)
    # Email
    lb5 = Label(labelFrame,text="Email : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.60, relheight=0.08)   
    clientemail = Entry(labelFrame)
    clientemail.place(relx=0.3,rely=0.60, relwidth=0.62, relheight=0.08)
    # Password
    lb6 = Label(labelFrame,text="Password : ", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.7, relheight=0.08)
    clientpwd = Entry(labelFrame)
    clientpwd.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.08)
    #Submit Button
    SubmitBtn = Button(labelFrame,text="Login",bg='#d1ccc0', fg='black',command=clientlogin)
    SubmitBtn.place(relx=0.41,rely=0.85, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    root.destroy()
    


    
