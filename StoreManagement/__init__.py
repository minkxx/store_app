import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import customtkinter as ctk
from PIL import Image, ImageTk

from StoreManagement.logger import log
from StoreManagement.database import Database


class ttkGUI:
    def __init__(self):
        # database intregation
        self.db = Database()
        log.info("starting app")

        # display settings 
        self.root = ttk.Window(themename="darkly")
        self.root.geometry("800x450")
        self.root.title("Inventory App")
        self.root.wm_iconbitmap("StoreManagement//resources//management.ico")
        self.root.wm_resizable(False, False)

        # data variables
        self.output_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.add_name_var = tk.StringVar()
        self.add_item_var = tk.StringVar()
        self.add_quantity_var = tk.IntVar()

        # login frame settings
        self.log_frame = ttk.Frame(master=self.root)
        self.log_frame.pack(expand=True, fill="both")

        ## login sub frames settings
        self.frame1 = tk.Frame(master=self.log_frame)
        self.frame2 = tk.Frame(master=self.log_frame)
        self.frame1.place(x=0, y=0, relwidth=0.5, relheight=1)
        self.frame2.place(relx=0.5, y=0, relwidth=0.5, relheight=1)
    
        ## frame2 griding
        self.frame2.rowconfigure((0,1,2,3), weight=1)
        self.frame2.columnconfigure((0,1,2), weight=1)

        ## frame 1 wigets setting
        self.img = Image.open("StoreManagement//resources//inventory_login.png")
        self.photo = ImageTk.PhotoImage(self.img)
        self.img_label = ttk.Label(master=self.frame1, image=self.photo)
        self.img_label.place(x=30, y=30, width=370, height=370)

        ## frame 2 widgets settngs
        ### login in text 
        self.login_text = ttk.Label(master=self.frame2, text="Login", font=("Microsoft HaYei UI Bold", 25),anchor="center")
        self.login_text.pack(expand=True, fill="both")
        self.login_text.grid(row=0, column=1)
        
        ### username
        self.username_text = ttk.Label(master=self.frame2, text="username", font=("Microsoft HaYei UI Light", 10))
        self.username_text.place(x=50, y=130)
        self.username_entry = ttk.Entry(master=self.frame2, font=("Microsoft HaYei UI Light", 10), textvariable=self.username_var)
        self.username_entry.place(x=120, y=130)
        
       ### password
        self.password_text = ttk.Label(master=self.frame2, text="password", font=("Microsoft HaYei UI Light", 10))
        self.password_text.place(x=50, y=180)
        self.password_entry = ttk.Entry(master=self.frame2, show="*", font=("Microsoft HaYei UI Light", 10), textvariable=self.password_var)
        self.password_entry.place(x=120, y=180)
        
        ### sign in
        self.signin_button = ttk.Button(master=self.frame2, text="Sign in", command=self.signIn)
        self.signin_button.place(x=165, y=240)
        
        ### sign up 
        self.signup_text = ttk.Label(master=self.frame2, text="Didn't have an account?", font=("Microsoft HaYei UI Light", 10))
        self.signup_text.place(x= 90, y=320)
        self.temp_signup_text = ttk.Label(master=self.frame2, text="Sign up", font=("Microsoft HaYei UI Light", 9), foreground="gray")
        self.temp_signup_text.place(x= 230, y=320)
        
        ### output text temp
        self.output_text = ttk.Label(master=self.frame2, text="output", font=("Microsoft HaYei UI Light", 10), textvariable=self.output_var)
        self.output_text.place(x= 140, y=360)

        # home frame settings
        self.home_frame = ttk.Frame(master=self.root)

        ## bar frame settings
        self.bar_frame = ttk.Frame(master=self.home_frame)
        self.bar_frame.place(x=0, y=0, width=800, height=30)
        self.testlabel = ttk.Label(master=self.bar_frame, background="#356eb8")
        self.testlabel.pack(expand=True, fill="both")

        ## home sub frames settings
        self.menu_frame = ttk.Frame(master=self.home_frame)
        self.menu_frame.place(x=0, y=35, relwidth=0.2, relheight=1)
 
        ### menu frame widgets
        self.displayItems_button = ttk.Button(master=self.menu_frame, text="Display Items", width=22, command=self.displayI_frame)
        self.displayItems_button.place(x=0, y=10)
        self.addItems_button = ttk.Button(master=self.menu_frame, text="Add Items", width=22, command=self.addI_frame)
        self.addItems_button.place(x=0, y=50)
        self.removeItems_button = ttk.Button(master=self.menu_frame, text="Remove Items", width=22, command=self.removeI_frame)
        self.removeItems_button.place(x=0, y=90)
        self.xItems_button = ttk.Button(master=self.menu_frame, text="X Items", width=22, command=self.xI_frame)
        self.xItems_button.place(x=0, y=130)
        self.yItems_button = ttk.Button(master=self.menu_frame, text="Log out", command=self.prevPage, width=24)
        self.yItems_button.place(x=0, y=380)

        ### display frame
        self.displayI_frame()

        # page moving settings
        self.frames = [self.log_frame, self.home_frame]
        self.count = 0

    def displayI_frame(self):
        self.displayItems_frame = ttk.Frame(master=self.home_frame, borderwidth=2, relief="solid")
        self.displayItems_frame.place(x=170, y=45, width=620, height=400)
        self.text_label = ttk.Label(master=self.displayItems_frame, text="Items in Inventory", font=("Microsoft HaYei UI Bold", 20))
        self.text_label.pack()

    def addI_frame(self):
        self.addItems_frame = ttk.Frame(master=self.home_frame, borderwidth=2, relief="solid")
        self.addItems_frame.place(x=170, y=45, width=620, height=400)
        self.text_label2 = ttk.Label(master=self.addItems_frame, text="Add Items in Inventory", font=("Microsoft HaYei UI Bold", 20))
        self.text_label2.pack()
        self.add_name_label = ttk.Label(master=self.addItems_frame, text="Name", font=("Microsoft HaYei UI Light", 10))
        self.add_name_label.place(x=220,y=76)
        self.add_item_name_label = ttk.Label(master=self.addItems_frame, text="Item name", font=("Microsoft HaYei UI Light", 10))
        self.add_item_name_label.place(x=200,y=136)
        self.add_quantity_label = ttk.Label(master=self.addItems_frame, text="Quantity", font=("Microsoft HaYei UI Light", 10))
        self.add_quantity_label.place(x=210,y=196)
        self.name_entry = ttk.Entry(master=self.addItems_frame, textvariable=self.add_name_var)
        self.name_entry.place(x=275, y=75)
        self.item_name_entry = ttk.Entry(master=self.addItems_frame, textvariable=self.add_item_var)
        self.item_name_entry.place(x=275, y=135)
        self.quantity_entry = ttk.Entry(master=self.addItems_frame, textvariable=self.add_quantity_var)
        self.quantity_entry.place(x=275,y=196)
        self.add_item_button = ttk.Button(master=self.addItems_frame, text="Add Item", command=self.add_data, width=12)
        self.add_item_button.place(x=270, y=256)

    def add_data(self):
        self.db.insertData(self.add_name_var.get(), self.add_item_var.get(), self.add_quantity_var.get())      

    def removeI_frame(self):
        self.remove_frame = ttk.Frame(master=self.home_frame, borderwidth=2, relief="solid")
        self.remove_frame.place(x=170, y=45, width=620, height=400)
        self.text_label3 = ttk.Label(master=self.remove_frame, text="Remove Items from Inventory", font=("Microsoft HaYei UI Bold", 20))
        self.text_label3.pack()
        self.remove_name_label = ttk.Label(master=self.remove_frame, text="Name", font=("Microsoft HaYei UI Light", 10))
        self.remove_name_label.place(x=220,y=76)
        self.remove_item_name_label = ttk.Label(master=self.remove_frame, text="Item name", font=("Microsoft HaYei UI Light", 10))
        self.remove_item_name_label.place(x=200,y=136)
        self.remove_quantity_label = ttk.Label(master=self.remove_frame, text="Quantity", font=("Microsoft HaYei UI Light", 10))
        self.remove_quantity_label.place(x=210,y=196)
        self.remove_name_entry = ttk.Entry(master=self.remove_frame)
        self.remove_name_entry.place(x=275, y=75)
        self.remove_item_name_entry = ttk.Entry(master=self.remove_frame)
        self.remove_item_name_entry.place(x=275, y=135)
        self.remove_quantity_entry = ttk.Entry(master=self.remove_frame)
        self.remove_quantity_entry.place(x=275,y=196)
        self.remove_item_button = ttk.Button(master=self.remove_frame, text="Remove Item", command=self.add_data)
        self.remove_item_button.place(x=270, y=256)

    def xI_frame(self):
        self.x_frame = ttk.Frame(master=self.home_frame, borderwidth=2, relief="solid")
        self.x_frame.place(x=170, y=45, width=620, height=400)
        self.testlabel4 = ttk.Label(master=self.x_frame, text="Just a text", font=("Microsoft HaYei UI Bold", 20))
        self.testlabel4.pack()

    def nextPage(self):
        if not self.count > len(self.frames) -2:
            for f in self.frames:
                f.pack_forget()
            self.count += 1
            frame = self.frames[self.count]
            frame.pack(expand=True, fill="both")

    def prevPage(self):
        self.output_var.set("")
        self.username_var.set("")
        self.password_var.set("")
        self.add_item_var.set("")
        self.add_name_var.set("")
        self.add_quantity_var.set("")
        if not self.count == 0:
            for f in self.frames:
                f.pack_forget()
            self.count -= 1
            frame = self.frames[self.count]
            frame.pack(expand=True, fill="both")

    def signIn(self):
        entered_username = self.username_var.get()
        entered_password = self.password_var.get()
        
        cred = self.db.getData("cred")
        db_username = cred["cred"]["username"]
        db_password = cred["cred"]["password"]
        
        if entered_username == db_username and entered_password == db_password:
            self.nextPage()
        elif entered_username != db_username:
            self.output_var.set("username incorrect!")
        elif entered_password != db_password:
            self.output_var.set("password incorrect!")
        else:
            self.output_var.set("idk!!")

    def start(self):
        log.info("app started")
        self.root.mainloop()