import threading
from tkinter import *
from tkinter import ttk, messagebox
import Login_window
import time
import sqlite3
con = sqlite3.connect('database.db', check_same_thread=False)
# orders = con.execute('SELECT * from order_data where status="recieved"')
# for i in orders:
#     print(i[0], i[1], i[2], i[3])

class Chef:
    def __init__(self, root):
        self.root = root
        self.root.title("Kitchen Portal Portal")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        win_dims = str(screen_width) + "x" + str(screen_height)
        self.root.geometry(win_dims)

        title = Label(self.root, text="Kitchen Portal", font=("calibri", 40, "bold"), bg="black", fg="blue")
        title.pack(side=TOP, fill=X)

        self.content_frame = Frame(self.root, bg="gray")
        self.content_frame.place(x=360, y=80, width=1555, height=930)

        navigation_frame = Frame(self.root, bd=4, relief=RIDGE, bg="light blue")
        navigation_frame.place(x=5, y=80, width=350, height=930)

        self.menu_frame = Frame(self.content_frame, bg="yellow")
        self.orders_frame = Frame(self.content_frame, bg="white")

        logout_btn = Button(self.root, command=self.logout, text="Logout", fg="white",
                           font=("Calibri", 15, "bold"), bg="black").place(x=1800, y=30)

        menu_btn = Button(navigation_frame, command=self.raise_menu, text="Change Menu", fg="black",
                           font=("Calibri", 25, "bold"), bg="light blue").place(x=0, y=80, width=340, height=250)

        orders_button = Button(navigation_frame, command=self.raise_orders, text="View Orders", fg="black",
                           font=("Calibri", 25, "bold"), bg="light blue").place(x=0, y=350, width=340, height=250)

        self.orders_frame.place(x=0, y=70, width=1555, height=500)
        # global order_table
        self.order_table = ttk.Treeview(self.orders_frame, selectmode='browse')
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Calibri", 15))
        self.order_table["columns"] = ("1", "2", "3", "4")
        self.order_table["show"] = 'headings'
        self.order_table.heading("1", text="OrderID")
        self.order_table.heading("2", text="Items")
        self.order_table.heading("3", text="Table number")
        self.order_table.heading("4", text="Mode")
        self.order_table.place(x=0, y=0, width=1555, height=500)
        self.refresh_order_list()
        # x = threading.Timer(1, self.refresh_order_list).start()
        # self.root.after(1000, self.refresh_order_list())

    def refresh_order_list(self):
        orders = con.execute('SELECT * from order_data where status="recieved"')
        for item in self.order_table.get_children():
            self.order_table.delete(item)
        for i in orders:
            self.order_table.insert("", 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3]))
        threading.Timer(1, self.refresh_order_list).start()

    def raise_menu(self):
        self.orders_frame.place_forget()
        self.menu_frame.place(x=0, y=0, width=1555, height=930)

    def raise_orders(self):
        self.menu_frame.place_forget()
        self.orders_frame.place(x=0, y=70, width=1555, height=500)

    def logout(self):
        self.root.destroy()
        Login_window.init_login()


def init_kitchen_portal():
    rt = Tk()
    obj = Chef(rt)
    rt.mainloop()
