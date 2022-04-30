import threading
from tkinter import *
from tkinter import ttk, messagebox
import Login_window
import sqlite3
con = sqlite3.connect('database.db', check_same_thread=False)

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

        self.navigation_frame = Frame(self.root, bd=4, relief=RIDGE, bg="navy blue")
        self.navigation_frame.place(x=5, y=80, width=350, height=930)

        logout_btn = Button(self.root, command=self.logout, text="Logout", fg="black",
                            font=("Calibri", 15, "bold"), bg="white").place(x=1800, y=30)
        menu_btn = Button(self.navigation_frame, command=self.raise_menu, text="Change Menu", fg="black",
                          font=("Calibri", 25, "bold"), bg="light blue").place(x=0, y=350, width=340, height=250)
        orders_button = Button(self.navigation_frame, command=self.raise_orders, text="View Orders", fg="black",
                               font=("Calibri", 25, "bold"), bg="light blue").place(x=0, y=80, width=340, height=250)
        new_recipe_button = Button(self.navigation_frame, command=self.raise_new_dish, text="Add new Dish", fg="black",
                               font=("Calibri", 25, "bold"), bg="light blue").place(x=0, y=620, width=340, height=250)

        self.menu_frame = Frame(self.content_frame, bg="gray")
        self.new_dish_frame = Frame(self.content_frame, bg='gray')
        self.orders_frame = Frame(self.content_frame, bg="gray")
        self.orders_frame.place(x=0, y=0, width=1555, height=930)

        # active orders frame
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
        self.order_table.place(x=0, y=40, width=1555, height=500)
        self.refresh_order_list()

        self.order_no = Entry(self.orders_frame, font=("Calibri", 15))
        self.order_no.place(x=200, y=600)

        order_delivered_btn = Button(self.orders_frame, command=self.order_delivered, text="Processed Order", fg="white",
                         font=("Calibri", 15, "bold"), bg="black").place(x=500, y=600)

        # menu items frame
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

        # add new dish frame
        Label(self.new_dish_frame, text="All Dishes", font=('calibri', 20, 'bold'), bg='black', fg='blue').pack(side="top", fill=X)
        self.new_dishes_table = ttk.Treeview(self.new_dish_frame, selectmode='browse')
        self.new_dishes_table["columns"] = ("1", "2", "3", "4", "5")
        self.new_dishes_table["show"] = 'headings'
        self.new_dishes_table.heading("1", text="Dish No")
        self.new_dishes_table.heading("2", text="Name")
        self.new_dishes_table.heading("3", text="Type")
        self.new_dishes_table.heading("4", text="Description")
        self.new_dishes_table.heading("5", text="Price")
        self.new_dishes_table.place(x=0, y=40, width=1555, height=500)
        self.populate_new_menu()

        item_label = Label(self.new_dish_frame, text="Name", font=("Calibri", 15, "bold"), bg="gray").place(x=50, y=600)
        self.dish_name = Entry(self.new_dish_frame, font=("Calibri", 15))
        self.dish_name.place(x=250, y=600)

        item_label = Label(self.new_dish_frame, text="Type", font=("Calibri", 15, "bold"), bg="gray").place(x=50, y=650)
        self.dish_type = Entry(self.new_dish_frame, font=("Calibri", 15))
        self.dish_type.place(x=250, y=650)

        item_label = Label(self.new_dish_frame, text="Description", font=("Calibri", 15, "bold"), bg="gray").place(x=50, y=700)
        self.dish_description = Entry(self.new_dish_frame, font=("Calibri", 15))
        self.dish_description.place(x=250, y=700)

        item_label = Label(self.new_dish_frame, text="Ingredients", font=("Calibri", 15, "bold"), bg="gray").place(x=50, y=750)
        self.dish_ingredients = Entry(self.new_dish_frame, font=("Calibri", 15))
        self.dish_ingredients.place(x=250, y=750)

        item_label = Label(self.new_dish_frame, text="Price", font=("Calibri", 15, "bold"), bg="gray").place(x=50, y=800)
        self.dish_price = Entry(self.new_dish_frame, font=("Calibri", 15))
        self.dish_price.place(x=250, y=800)

        add_btn = Button(self.new_dish_frame, command=self.add_dish_to_db, text="Add Dish", fg="white",
                         font=("Calibri", 15, "bold"), bg="black").place(x=550, y=700)

        item_label = Label(self.new_dish_frame, text="Dish No. to be Deleted", font=("Calibri", 15, "bold"), bg="gray").place(x=750, y=600)
        self.dish_tobe_removed = Entry(self.new_dish_frame, font=("Calibri", 15))
        self.dish_tobe_removed.place(x=1000, y=600)
        add_btn = Button(self.new_dish_frame, command=self.remove_dish_from_db, text="Remove Dish", fg="white",
                         font=("Calibri", 15, "bold"), bg="black").place(x=1300, y=600)

    def order_delivered(self):
        order_number = self.order_no.get()
        con.execute('UPDATE order_data SET status=? WHERE orderID=?', ("delivered", order_number))
        con.commit()

    def add_dish_to_db(self):
        dish_name = str(self.dish_name.get())
        dish_type = str(self.dish_type.get())
        dish_description = str(self.dish_description.get())
        dish_ingredients = str(self.dish_ingredients.get())
        dish_price = float(self.dish_price.get())
        dish_num = 0
        all_dish_nos = []
        dish_nos = con.execute('SELECT Dish_No from dishes')
        for i in dish_nos:
            all_dish_nos.append(i[0])
        for i in range(1, max(all_dish_nos)+2):
            if i not in all_dish_nos:
                dish_num = i
                break
        con.execute('INSERT INTO dishes VALUES(?,?,?,?,?,?)', (dish_name, dish_type, dish_description, dish_ingredients, dish_num, dish_price))
        con.commit()
        self.populate_new_menu()

    def remove_dish_from_db(self):
        dish_no = int(self.dish_tobe_removed.get())
        con.execute('DELETE FROM dishes where Dish_No=?', (dish_no,))
        con.commit()
        self.populate_new_menu()

    def populate_menu(self):
        for item in self.menu_table.get_children():
            self.menu_table.delete(item)
        menu_items = con.execute('SELECT * FROM menu')
        for item in menu_items:
            self.menu_table.insert("", 'end', iid=item[1], text=item[1], values=(item[1], item[0]))

    def populate_new_menu(self):
        for item in self.new_dishes_table.get_children():
            self.new_dishes_table.delete(item)
        dishes = con.execute('SELECT * FROM dishes ORDER BY Dish_No')
        for dish in dishes:
            self.new_dishes_table.insert("", 'end', iid=dish[4], text=dish[4], values=(dish[4], dish[0], dish[1], dish[2], dish[5]))

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
            self.order_table.insert("", 'end', iid=i[5], text=i[5], values=(i[5], i[0], i[1], i[2]))
        self.refresh_order_thread = threading.Timer(1, self.refresh_order_list)
        self.refresh_order_thread.start()

    def raise_menu(self):
        self.orders_frame.place_forget()
        self.new_dish_frame.place_forget()
        self.populate_dishes_list()
        self.menu_frame.place(x=0, y=0, width=1555, height=930)

    def raise_orders(self):
        self.menu_frame.place_forget()
        self.new_dish_frame.place_forget()
        self.orders_frame.place(x=0, y=0, width=1555, height=930)

    def raise_new_dish(self):
        self.menu_frame.place_forget()
        self.orders_frame.place_forget()
        self.new_dish_frame.place(x=0, y=0, width=1555, height=930)

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
        dishes = con.execute('SELECT * FROM dishes ORDER BY Dish_No')
        for item in self.dishes_table.get_children():
            self.dishes_table.delete(item)
        for dish in dishes:
            self.dishes_table.insert("", 'end', iid=dish[4], text=dish[4], values=(dish[4], dish[0], dish[5]))

def init_kitchen_portal():
    rt = Tk()
    obj = Chef(rt)
    rt.mainloop()
