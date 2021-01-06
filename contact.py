from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk,Image

def initialize():
    global root
    global Frame_box1
    root = Tk()
    root.title("Contact_Book")
    root.geometry('960x450')
    root.resizable(False,False)
    bg_img = ImageTk.PhotoImage(Image.open('bg_img.jpeg'))
    bg = Label(root,image=bg_img)
    bg.place(x=0,y=0,relwidth=1,relheight=1)
    Frame_box1 = Frame(root,bg='white')
    Frame_box1.place(x=25,y=90,height=222,width=440)
    login()
    Frame_box1.mainloop()

def home():
    global view_button
    global add_button
    global more_button
    global Exit_button
    global home_label
    Frame_box1 = Frame(root,bg='white')
    Frame_box1.place(x=25,y=90,height=222,width=440)
    home_label = Label(root,text="Home",font=("times new roman",25),bg="#68abb3",fg="black")
    home_label.place(x=25,y=35,height=55)
    try:
        login_label.place_forget()
        user_name.place_forget()
        user_password.place_forget()
        login_button.place_forget()
    except:
        pass
    try:
        addcontact_label.place_forget()
    except:
        pass
    try:
        more_label.place_forget()
    except:
        pass
    try:
        search_box.place_forget()
        search_button.place_forget()
    except:
        pass
    try:
        n.place_forget()
        n_label.place_forget()
        p.place_forget()
        p_label.place_forget()
        e.place_forget()
        e_label.place_forget()
        button_next.place_forget()
        button_previous.place_forget()
    except:
        pass
    try:
        delete_all_button.place_forget()
        export_button.place_forget()
        import_button.place_forget()
        delete_contact_button.place_forget()

    except:
        pass
    try:
       submit_button.place_forget()
    except:
        pass
    view_button = Button(Frame_box1,text="View all contacts",command=lambda:view_all(0),bd=0,bg="#ff9966",fg="black")
    view_button.place(x=100,y=20,width=200,height=30)

    add_button = Button(Frame_box1,text='Add contact',command=insert_data,bd=0,bg='#ff9966',fg='black')
    add_button.place(x=100,y=70,width=200,height=30)

    more_button = Button(Frame_box1,text='More options',command=more_option,bd=0,bg='#ff9966',fg='black')
    more_button.place(x=100,y=120,width=200,height=30)

    log_button = Button(Frame_box1,text='Log out',command=more_option,bd=0,bg='#ff9966',fg='black')
    log_button.place(x=100,y=170,width=200,height=30)

    Exit_button = Button(root,text='Exit',command=exit,bd=0,bg='#ff6666',fg='white')
    Exit_button.place(x=390,y=330,width=70,height=35)


def entry_box():
    global n_label
    global n
    global p_label
    global p
    global e_label
    global e
    global Frame_box2

    Frame_box2 = Frame(root,bg='white')
    Frame_box2.place(x=25,y=90,height=222,width=440)

    n_label = Label(Frame_box2,text="Name:",font=('times new roman',12),bg='white',fg="orange")
    n_label.place(x=35,y=10)
    n = Entry(Frame_box2,font=(10),bg='white',bd=0.2)
    n.place(x=35,y=30,width=360,height=30) 

    p_label = Label(Frame_box2,text="Ph-No:",font=('times new roman',12),bg='white',fg="orange")
    p_label.place(x=35,y=63)
    p = Entry(Frame_box2,font=(10),bg='white',bd=0.2)
    p.place(x=35,y=83,width=360,height=30) 

    e_label = Label(Frame_box2,text="Email_Id:",font=('times new roman',12),bg='white',fg="orange")
    e_label.place(x=35,y=118)
    e = Entry(Frame_box2,font=(10),bg='white',bd=0.2)
    e.place(x=35,y=140,width=360,height=30) 

def create_database():
    global c
    global con
    try:
        con = sqlite3.connect("contacts_database.db")
        c = con.cursor()
        c.execute('CREATE TABLE contacts(Name text,Ph_No int,Email_Add text)')
        con.commit()
    except:
        pass

def insert_data():
    global addcontact_label
    entry_box()
    home_button = Button(root,text='home',command=home,bd=0,bg='#ff9966',fg='white')
    home_button.place(x=25,y=38,width=83,height=35)
    addcontact_label = Label(root,text="Add new contacts",font=("times new roman",20),bg="#68abb3",fg="black")
    addcontact_label.place(x=140,y=40)
    def get_data():
        create_database()
        global submit_button
        name = n.get()
        ph_no = p.get()
        email = e.get()
        c.execute("INSERT INTO contacts VALUES(?,?,?)",(name,ph_no,email))
        con.commit()
        print(name)
        print("hi")
    #delete current data in entry
        n.delete(0,END)
        p.delete(0,END)
        e.delete(0,END)
    #again Take input
        submit_button = Button(Frame_box2,text="Submit",command=get_data,bd=0.2,bg="orange")
        submit_button.place(x=180,y=180,width=70,height=35)
    submit_button = Button(Frame_box2,text="Submit",command=get_data,bd=0.2,bg="orange")
    submit_button.place(x=180,y=180,width=70,height=35)


def view_all(num):
    global search_box
    global search_button
    global home_button
    entry_box()
    home_label.place_forget()
    search_box = Entry(root,font=("times new roman",12),bg='white',bd=0)
    search_box.place(x=110,y=38,width=260,height=35)
    search_button = Button(root,text='search',command=lambda:search_contacts(0),bd=0,bg='orange')
    search_button.place(x=374,y=38,width=85,height=35)
    number = num
    def view(number):
        global button_next
        global button_previous
        # fetching database
        create_database()
        c.execute('SELECT rowid,* FROM contacts')
        contacts = c.fetchall()
        # fetchall returns all the contact in a list called contacts =  [(),(),]
        #all the contact will be in touple ex: contact =  (1,'subbu','344465','vmfdvn@kjh')
        if contacts:
            count = 0 + number
            contact = contacts[count]
            # 0th item is rowid
            name = contact[1]
            ph_no = contact[2]
            email = contact[3]

            n.delete(0,END)
            n.insert(0,name)
            p.delete(0,END)
            p.insert(0,ph_no)
            e.delete(0,END)
            e.insert(0,email)
                #Forward_button
            if count+1 < len(contacts):
                button_next = Button(Frame_box2,text=">>>",command=lambda:view(count + 1),bg="#ff944d",fg='black',bd=0)
                button_next.place(x=330,y=180,width=70,height=35)
                # Forword_button Disable
            else:
                button_next = Button(Frame_box2,text=">>>",command=DISABLED,bg="#ff944d",fg='black',bd=0)
                button_next.place(x=330,y=180,width=70,height=35)
                # Previous_button
            if count > 0:
                button_previous = Button(Frame_box2,text="<<<",command=lambda:view(count - 1),bg="#ff944d",fg='black',bd=0)
                button_previous.place(x=35,y=180,width=70,height=35)
            else:
                # Previous_button Disabled
                button_previous = Button(Frame_box2,text="<<<",command=DISABLED,bg="#ff944d",fg='black',bd=0)
                button_previous.place(x=35,y=180,width=70,height=35)
    view(number)
    #using a second loop to avoid programe calling entry_box() every time, which results in fast working
    home_button = Button(root,text='home',command=home,bd=0,bg='#ff9966',fg='white')
    home_button.place(x=25,y=38,width=83,height=35)

def search_contacts(num):
    Frame_box = Frame(root,bg='white')
    Frame_box.place(x=25,y=90,height=222,width=440)
    entry_box()
    number = num
    def search(num):
        create_database()
        view_button.place_forget()
        add_button.place_forget()
        more_button.place_forget()
        name = search_box.get()
        print(name)
        c.execute("SELECT rowid,* FROM contacts WHERE Name=?",(name,))
        contacts = c.fetchall()
        print(contacts)
        if contacts:
            count = 0 + num
            contact = contacts[count]
            name = contact[1]
            ph_no = contact[2]
            email = contact[3]

            n.delete(0,END)
            n.insert(0,name)
            p.delete(0,END)
            p.insert(0,ph_no)
            e.delete(0,END)
            e.insert(0,email)

            if count+1 < len(contacts):
                print(len(contacts))
                button_next = Button(Frame_box2,text=">>>",command=lambda:search(count + 1),bg="#ff944d",fg='black',bd=0)
                button_next.place(x=330,y=180,width=70,height=35)
                # Forword_button Disable
            else:
                button_next = Button(Frame_box2,text=">>>",command=DISABLED,bg="#ff944d",fg='black',bd=0)
                button_next.place(x=330,y=180,width=70,height=35)
                # Previous_button
            if count > 0:
                button_previous = Button(Frame_box2,text="<<<",command=lambda:search(count - 1),bg="#ff944d",fg='black',bd=0)
                button_previous.place(x=35,y=180,width=70,height=35)
            else:
                # Previous_button Disabled
                button_previous = Button(Frame_box2,text="<<<",command=DISABLED,bg="#ff944d",fg='black',bd=0)
                button_previous.place(x=35,y=180,width=70,height=35)
    search(number)

def delete_contact(): 
    global search_box
    global search_button
    delete_all_button.place_forget()
    delete_contact_button.place_forget()
    export_button.place_forget()
    import_button.place_forget()
    home_label.place_forget()
    #create_database()
    entry_box()
    search_box = Entry(root,font=("times new roman",12),bg='white',bd=0)
    search_box.place(x=120,y=40,width=260,height=35)
    def delete():
            create_database()
            name = n.get()
            c.execute("DELETE FROM contacts WHERE Name=?",(name,))
            con.commit()
            n.delete(0,END)
            p.delete(0,END)
            e.delete(0,END)
    def preview():
        create_database()
        contact = search_box.get()
        c.execute("SELECT rowid, * FROM contacts WHERE Name=?",(contact,))
        contacts = c.fetchall()
        print(contact)
        if contacts:
            contact = contacts[0]
            name = contact[1]
            print(name)
            ph_no = contact[2]
            email = contact[3]

            n.delete(0,END)
            n.insert(0,name)
            p.delete(0,END)
            p.insert(0,ph_no)
            e.delete(0,END)
            e.insert(0,email)
            delete_contact_button = Button(Frame_box2,text="Delete",command=delete,bd=0.2,bg="orange")
            delete_contact_button.place(x=180,y=180,width=70,height=35)
    search_button = Button(root,text='preview',command=preview,bd=0,bg='orange')
    search_button.place(x=390,y=40,width=75,height=35)

def delete_all():
    create_database()
    response = messagebox.askokcancel("delete all contact","It will delete all the contacts")
    if response == 1:
        c.execute("DELETE FROM contacts")
        con.commit()
def more_option():
    global export_button
    global import_button
    global delete_all_button
    global delete_contact_button
    global more_label
    Frame_box = Frame(root,bg='white')
    Frame_box.place(x=25,y=90,height=222,width=440)
    more_label = Label(root,text="More options",font=("times new roman",20),bg="#68abb3",fg="black")
    more_label.place(x=140,y=38)

    try:
        home_label.place_forget()
    except:
        pass

    try:
        n.place_forget()
        n_label.place_forget()
        p.place_forget()
        p_label.place_forget()
        e.place_forget()
        e_label.place_forget()
    except:
        pass

    try:
        view_button.place_forget()
        add_button.place_forget()
        more_button.place_forget()
    except:
        pass

    Exit_button.place_forget()
    home_button = Button(root,text='home',command=home,bd=0,bg='#ff9966',fg='white')
    home_button.place(x=25,y=38,width=83,height=35)
    delete_contact_button = Button(Frame_box,text="Delete a contact",command=delete_contact,bg="orange",fg="white",bd=0.2)
    delete_contact_button.place(x=100,y=20,width=200,height=30)
    delete_all_button = Button(Frame_box,text="Delete all Contacts",bg="orange",command=delete_all,fg="white",bd=0.2)
    delete_all_button.place(x=100,y=170,width=200,height=30)
    export_button = Button(Frame_box,text="Export Contacts",bg="orange",fg="white",bd=0.2)
    export_button.place(x=100,y=70,width=200,height=30)
    import_button = Button(Frame_box,text="Import Contacts",bg="orange",fg="white",bd=0.2)
    import_button.place(x=100,y=120,width=200,height=30)

def login():
    global user_name
    global user_password
    global login_button
    global login_label
    login_label = Label(root,text="Login Page",bg="#68abb3",fg="orange",font=("times new roman",25,"bold"))
    login_label.place(x=180,y=35)
    user_label = Label(Frame_box1,text="User Name",font=("times new roman",15),bg="white",fg="orange")
    user_label.place(x=35,y=30,)
    user_name = Entry(Frame_box1,font=(15),bg="white",fg="black",bd=0)
    user_name.place(x=35,y=60,width=360,height=30)
    user_pass_label = Label(Frame_box1,text="Pssword",font=("times new roman",15),bg="white",fg="orange")
    user_pass_label.place(x=35,y=93)
    user_password = Entry(Frame_box1,font=(15),bg="white",fg="black",bd=0)
    user_password.place(x=35,y=123,width=360,height=30)

    def autentiate():
        password = user_password.get()
        username = user_name.get()
        if username == "root" and password == "root":
            home()
        elif username == "" and password == "":
            messagebox.showerror("Authentication Error","All fields are required")
        else:
           messagebox.showerror("Authentication Error","Please re-enter details")
    login_button = Button(Frame_box1,text="Login",bg="orange",fg="white",command=autentiate,bd=0)
    login_button.place(x=180,y=170,width=90,height=35)

initialize()