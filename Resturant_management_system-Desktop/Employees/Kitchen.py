import threading
from tkinter import *
from tkinter import ttk, messagebox
import Login_window
import sqlite3
con = sqlite3.connect('../database.db', check_same_thread=False)

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

        navigation_frame = Frame(self.root, bd=4, relief=RIDGE, bg="navy blue")
        navigation_frame.place(x=5, y=80, width=350, height=930)

        logout_btn = Button(self.root, command=self.logout, text="Logout", fg="black",
                            font=("Calibri", 15, "bold"), bg="white").place(x=1800, y=30)

        menu_btn = Button(navigation_frame, command=self.raise_menu, text="Change Menu", fg="black",
                          font=("Calibri", 25, "bold"), bg="light blue").place(x=0, y=350, width=340, height=250)

        orders_button = Button(navigation_frame, command=self.raise_orders, text="View Orders", fg="black",
                               font=("Calibri", 25, "bold"), bg="light blue").place(x=0, y=80, width=340, height=250)

        new_recipe_button = Button(navigation_frame, command=self.raise_new_dish, text="Add new Dish", fg="black",
                               font=("Calibri", 25, "bold"), bg="light blue").place(x=0, y=620, width=340, height=250)

        self.menu_frame = Frame(self.content_frame, bg="gray")
        self.new_dish_frame = Frame(self.content_frame, bg='gray')
        self.orders_frame = Frame(self.content_frame, bg="white")
        self.orders_frame.place(x=0, y=70, width=1555, height=500)

        orders_label = Label(self.orders_frame, text="Active Orders", font=('calibri', 20, 'bold'), bg='black', fg='blue')
        orders_label.pack(side="top", fill=X)

        self.order_table = ttk.Treeview(self.orders_frame, selectmode='browse')
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Calibri", 15))
        self.order_table["columns"] = ("1", "2", "3", "4")
        self.order_table["show"] = 'headings'
        self.order_table.heading("1", text="OrderID")
        self.order_table.heading("2", text="Items")
        self.order_table.heading("3", text="Table number")
        self.order_table.heading("4", text="Mode")
        self.order_table.place(x=0, y=45, width=1555, height=500)
        self.refresh_order_list()

        self.dishes_table = ttk.Treeview(self.menu_frame, selectmode='browse')
        self.dishes_table["columns"] = ("1", "2", "3")
        self.dishes_table["show"] = 'headings'
        self.dishes_table.heading("1", text="Dish No")
        self.dishes_table.heading("2", text="Name")
        self.dishes_table.heading("3", text="Price")
        self.dishes_table.place(x=755, y=60, width=805, height=500)
        self.populate_dishes_list()

        self.menu_table = ttk.Treeview(self.menu_frame, selectmode='browse')
        self.menu_table["columns"] = ("1", "2")
        self.menu_table["show"] = 'headings'
        self.menu_table.heading("1", text="Dish Number")
        self.menu_table.heading("2", text="Dish Name")
        self.menu_table.place(x=0, y=60, width=750, height=500)
        self.populate_menu()

        self.dish_no = Entry(self.menu_frame, font=("Calibri", 15))
        self.dish_no.place(x=200, y=600)

        add_btn = Button(self.menu_frame, command=self.remove_from_menu, text="Remove Dish from Menu", fg="white",
                            font=("Calibri", 15, "bold"), bg="black").place(x=500, y=600)

        remove_btn = Button(self.menu_frame, command=self.add_to_menu, text="Add Dish to Menu", fg="white",
                            font=("Calibri", 15, "bold"), bg="black").place(x=800, y=600)

    def populate_menu(self):
        for item in self.menu_table.get_children():
            self.menu_table.delete(item)
        menu_items = con.execute('SELECT * FROM menu')
        for item in menu_items:
            self.menu_table.insert("", 'end', iid=item[1], text=item[1], values=(item[1], item[0]))

    def add_to_menu(self):
        dishno = self.dish_no.get()
        if dishno == "":
            messagebox.showerror("error", "Enter a dish number", parent=self.root)
            return None
        else:
            dish_name = con.execute('SELECT name FROM dishes where Dish_No=?', (int(dishno),))
            for i in dish_name:
                x = str(i[0])
                append_list = (x)
                con.execute('INSERT INTO menu VALUES(?,?)', (append_list, int(dishno)))
                con.commit()
        self.populate_menu()

    def refresh_order_list(self):
        orders = con.execute('SELECT * from order_data where status="recieved"')
        for item in self.order_table.get_children():
            self.order_table.delete(item)
        for i in orders:
            self.order_table.insert("", 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3]))
        self.refresh_order_thread = threading.Timer(1, self.refresh_order_list)
        self.refresh_order_thread.start()

    def raise_menu(self):
        self.orders_frame.place_forget()
        self.new_dish_frame.place_forget()
        self.menu_frame.place(x=0, y=0, width=1555, height=930)

    def raise_orders(self):
        self.menu_frame.place_forget()
        self.new_dish_frame.place_forget()
        self.orders_frame.place(x=0, y=70, width=1555, height=500)

    def raise_new_dish(self):
        self.menu_frame.place_forget()
        self.orders_frame.place_forget()
        self.new_dish_frame.place(x=0, y=70, width=1555, height=500)

    def logout(self):
        self.refresh_order_thread.cancel()
        self.root.destroy()
        Login_window.init_login()

    def remove_from_menu(self):
        dishno = self.dish_no.get()
        if dishno == "":
            messagebox.showerror("error", "Enter a dish number", parent=self.root)
            return None
        else:
            con.execute("DELETE FROM menu where Dish_No=?", (int(dishno),))
            con.commit()
        self.populate_menu()

    def populate_dishes_list(self):
        dishes = con.execute('SELECT * FROM dishes')
        for dish in dishes:
            self.dishes_table.insert("", 'end', iid=dish[4], text=dish[4], values=(dish[4], dish[0], dish[5]))

def init_kitchen_portal():
    rt = Tk()
    obj = Chef(rt)
    rt.mainloop()
