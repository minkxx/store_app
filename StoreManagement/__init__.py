import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import customtkinter as ctk
from PIL import Image, ImageTk

from StoreManagement.logger import log
from StoreManagement.database import Database

class ctkGUI:
    def __init__(self):
        self.db = Database()
        log.info("starting app")

        # theme settings ---------------------------------------------------------------------------------------------
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # root frame settings ----------------------------------------------------------------------------------------
        self.root = ctk.CTk()
        self.root.geometry("1200x675")
        self.root.title("Inventory App")
        self.root.wm_iconbitmap("StoreManagement//resources//management.ico")

        # data variables ---------------------------------------------------------------------------------------------
        self.output_var = ctk.StringVar()

        # login frame ------------------------------------------------------------------------------------------------
        self.login_frame = ctk.CTkFrame(master=self.root)
        self.login_frame.propagate(False)
        self.login_frame.pack(padx=300, pady=68, fill="both", expand=True)

        self.title_text = ctk.CTkLabel(master=self.login_frame, text="Login", font=("Microsoft YaHei UI Bold", 20))
        self.title_text.pack(pady=10)

        self.username_entry = ctk.CTkEntry(master=self.login_frame, placeholder_text="username", font=("Microsoft YaHei UI", 12))
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(master=self.login_frame, placeholder_text="password", font=("Microsoft YaHei UI", 12), show="*")
        self.password_entry.pack(pady=10)

        self.login_button =ctk.CTkButton(master=self.login_frame, text="Login", font=("Microsoft YaHei UI", 12), command=self.loginCmd)
        self.login_button.pack(pady=10)

        self.output_text = ctk.CTkLabel(master=self.login_frame, text="output", textvariable=self.output_var,font=("Microsoft YaHei UI", 15))
        # self.output_text.place(x=270, y=200)
        self.output_text.pack()

        # home frame --------------------------------------------------------------------------------------------------
        # self.home_frame = ctk.CTkFrame(master=self.root)
        # self.home_frame.propagate(False)
        # self.tabs= ctk.CTkTabview(master=self.home_frame)
        # self.tabs.add("Tab1")
        # self.tabs.add("Tab2")
        # self.tabs.add("Tab3")
        # self.sample_text = ctk.CTkLabel(master=self.tabs.tab("Tab1"), text="Blah blah.")
        # self.sample_text.pack()
        # self.sample_text = ctk.CTkLabel(master=self.tabs.tab("Tab2"), text="Blah blah.")
        # self.sample_text.pack()
        # self.sample_text = ctk.CTkLabel(master=self.tabs.tab("Tab3"), text="Blah blah.")
        # self.sample_text.pack()

        # self.home_frame.pack(fill="both", expand=True)

    def loginCmd(self):
        entered_password = self.password_entry.get()
        entered_username = self.username_entry.get()
        
        cred = self.db.getData("cred")
        db_username = cred["cred"]["username"]
        db_password = cred["cred"]["password"]
        
        if entered_username == db_username and entered_password == db_password:
            self.output_var.set("Combination matched!!")
        elif entered_username != db_username:
            self.output_var.set("username incorrect!")
        elif entered_password != db_password:
            self.output_var.set("password incorrect!")
        else:
            self.output_var.set("idk!!")

    def start(self):
        log.info("app started")
        self.root.mainloop()


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

        # login frame settings
        self.log_frame = ttk.Frame(master=self.root)
        self.log_frame.pack(expand=True, fill="both")

        ## login sub frames settings
        self.frame1 = tk.Frame(master=self.log_frame, borderwidth=1, relief="solid")
        self.frame2 = tk.Frame(master=self.log_frame)
        self.frame1.place(x=0, y=0, relwidth=0.5, relheight=1)
        self.frame2.place(relx=0.5, y=0, relwidth=0.5, relheight=1)
    
        ## frame2 griding
        self.frame2.rowconfigure((0,1,2,3), weight=1)
        self.frame2.columnconfigure((0,1,2), weight=1)

        ## frame 1 wigets setting
        # img = Image.open("StoreManagement//resources//logo_350.png")
        # photo = ImageTk.PhotoImage(img)
        # img_label = ttk.Label(master=self.frame1, image=photo, borderwidth=2, relief="solid")
        # img_label.place(x=10, y=10, width=370, height=370)

        # testlabel = ttk.Label(master=self.frame1, background="red")
        # testlabel.pack(expand=True, fill="both")

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
        # self.signup_button = ttk.Button(master=self.frame2, text="Sign up")
        # self.signup_button.place(x=230, y=320)
        
        ### output text temp
        self.output_text = ttk.Label(master=self.frame2, text="output", font=("Microsoft HaYei UI Light", 10), textvariable=self.output_var)
        self.output_text.place(x= 140, y=360)


        # home frame settings
        self.home_frame = ttk.Frame(master=self.root)
        # self.test_label = ttk.Label(master=self.home_frame, background="red")
        # self.test_label.pack(expand=True, fill="both")
        # self.test_button = ttk.Button(master=self.home_frame, text="Prev page", command=self.prevPage)
        # self.test_button.pack()

        ## bar frame settings
        self.bar_frame = ttk.Frame(master=self.home_frame)
        self.bar_frame.place(x=0, y=0, width=800, height=30)
        self.testlabel = ttk.Label(master=self.bar_frame, background="#356eb8")
        self.testlabel.pack(expand=True, fill="both")

        ## home sub frames settings
        self.menu_frame = ttk.Frame(master=self.home_frame)
        self.menu_frame.place(x=0, y=35, relwidth=0.2, relheight=1)
 
        ### menu frame widgets
        self.displayItems_button = ttk.Button(master=self.menu_frame, text="Display Items", width=24, command=self.displayI_frame)
        self.displayItems_button.place(x=0, y=10)
        self.addItems_button = ttk.Button(master=self.menu_frame, text="Add Items", width=24, command=self.addI_frame)
        self.addItems_button.place(x=0, y=50)
        self.removeItems_button = ttk.Button(master=self.menu_frame, text="Remove Items", width=24, command=self.removeI_frame)
        self.removeItems_button.place(x=0, y=90)
        self.xItems_button = ttk.Button(master=self.menu_frame, text="X Items", width=24, command=self.xI_frame)
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
        self.name_entry = ttk.Entry(master=self.addItems_frame)
        self.name_entry.pack()
        self.item_name_entry = ttk.Entry(master=self.addItems_frame)
        self.item_name_entry.pack()
        self.quantity_entry = ttk.Entry(master=self.addItems_frame)
        self.quantity_entry.pack()
        self.add_item_button = ttk.Button(master=self.addItems_frame, text="Add Item", command=self.add_data)
        self.add_item_button.pack()

    def add_data(self):
        self.db.insertData(self.name_entry.get(), self.item_name_entry.get(), int(self.quantity_entry.get()))        

    def removeI_frame(self):
        self.remove_frame = ttk.Frame(master=self.home_frame)
        self.remove_frame.place(x=170, y=45, width=620, height=400)
        self.text_label3 = ttk.Label(master=self.addItems_frame, text="Remove Items from Inventory", font=("Microsoft HaYei UI Bold", 20))
        self.text_label3.pack()
        self.name_entry = ttk.Entry(master=self.addItems_frame)
        self.name_entry.pack()
        self.item_name_entry = ttk.Entry(master=self.addItems_frame)
        self.item_name_entry.pack()

    def xI_frame(self):
        self.x_frame = ttk.Frame(master=self.home_frame)
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