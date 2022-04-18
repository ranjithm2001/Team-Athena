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
        self.root.title("Chef Portal")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        win_dims = str(screen_width) + "x" + str(screen_height)
        self.root.geometry(win_dims)

        title = Label(self.root, text="Kitchen Portal", font=("calibri", 40, "bold"), bg="black", fg="blue")
        title.pack(side=TOP, fill=X)

        navigation_frame = Frame(self.root, bd=4, relief=RIDGE, bg="light blue")
        navigation_frame.place(x=5, y=80, width=400, height=930)

        content_frame = Frame(self.root, bg="gray")
        content_frame.place(x=410, y=80, width=1500, height=930)

        # menu_frame = Frame(self.root, bg="grey")
        # menu_frame.place(x=410, y=80, width=1500, height=930)

        # menu_frame.configure(state='disabled')
        # for child in menu_frame.winfo_children():
        #     child.configure(state='disabled')
        # kitchen_frame = Frame(self.root, bg="white")
        # kitchen_frame.place(x=150, y=150, height=380, width=500)

        logout_btn = Button(self.root, command=self.logout, text="Logout", fg="white",
                           font=("Calibri", 15, "bold"), bg="black").place(x=1800, y=30)

        menu_btn = Button(navigation_frame, command=self.logout, text="Change Menu", fg="black",
                           font=("Calibri", 25, "bold"), bg="light blue").place(x=0, y=80, width=390, height=250)

        orders_button = Button(navigation_frame, command=self.logout, text="Orders", fg="black",
                           font=("Calibri", 25, "bold"), bg="light blue").place(x=0, y=350, width=390, height=250)

        orders_frame = Frame(content_frame, bg="white")
        orders_frame.place(x=0, y=70, width=1500, height=500)
        global order_table
        order_table = ttk.Treeview(orders_frame, selectmode='browse')
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Calibri", 15))
        order_table["columns"] = ("1", "2", "3", "4")
        order_table["show"] = 'headings'
        order_table.heading("1", text="OrderID")
        order_table.heading("2", text="Items")
        order_table.heading("3", text="Table number")
        order_table.heading("4", text="Mode")

        order_table.place(x=0, y=0, width=1400, height=500)
        self.refresh_order_list()
        # x = threading.Timer(1, self.refresh_order_list).start()
        # self.root.after(1000, self.refresh_order_list())


    def refresh_order_list(self):
        orders = con.execute('SELECT * from order_data where status="recieved"')
        for item in order_table.get_children():
            order_table.delete(item)
        for i in orders:
            order_table.insert("", 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3]))
        threading.Timer(15, self.refresh_order_list).start()

    def logout(self):
        self.root.destroy()
        Login_window.init_login()


def init_kitchen_portal():
    rt = Tk()
    obj = Chef(rt)
    rt.mainloop()
