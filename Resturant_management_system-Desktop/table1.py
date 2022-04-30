from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
con = sqlite3.connect('database.db')


class Customer:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Portal")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        win_dims = str(screen_width) + "x" + str(screen_height)
        self.root.geometry(win_dims)

        title = Label(self.root, text="Welcome To Salad Restaurant", font=("calibri", 40, "bold"), bg="black", fg="blue")
        title.pack(side=TOP, fill=X)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Calibri", 15))
        # Menu
        self.menu_frame = Frame(self.root, bg="gray")
        self.cart_frame = Frame(self.root, bg="gray")
        self.menu_frame.place(x=0, y=80, width=1300, height=1080)
        self.cart_frame.place(x=1305, y=80, width=620, height=1000)
        Label(self.menu_frame, text="Our Menu", font=('calibri', 20, 'bold'), bg='black', fg='blue').pack(
            side="top", fill=X)
        self.menu_table = ttk.Treeview(self.menu_frame, selectmode='browse')
        self.menu_table["columns"] = ("1", "2", "3", "4", "5", "6")
        self.menu_table["show"] = 'headings'
        self.menu_table.heading("1", text="Item No")
        self.menu_table.heading("2", text="Name")
        self.menu_table.heading("3", text="Type")
        self.menu_table.heading("4", text="Description")
        self.menu_table.heading("5", text="Ingredients")
        self.menu_table.heading("6", text="Price")
        self.menu_table.place(x=0, y=40, width=1300, height=500)
        self.fill_menu()

        item_label = Label(self.menu_frame, text="Enter Item No", font=("Calibri", 15, "bold"), bg="gray").place(x=150, y=650)
        self.item_no = Entry(self.menu_frame, font=("Calibri", 15))
        self.item_no.place(x=150, y=700)

        item_label = Label(self.menu_frame, text="Number of Servings", font=("Calibri", 15, "bold"), bg="gray").place(x=400, y=650)
        self.no_of_servings = Entry(self.menu_frame, font=("Calibri", 15))
        self.no_of_servings.place(x=400, y=700)

        add_btn = Button(self.menu_frame, command=self.add_to_cart, text="Add To Cart", fg="white",
                         font=("Calibri", 15, "bold"), bg="black").place(x=700, y=695)

        Label(self.menu_frame, text="Or", font=("Calibri", 15, "bold"), bg="gray").place(x=860, y=700)
        remove_btn = Button(self.menu_frame, command=self.remove_from_cart, text="Update/Remove Item", fg="white",
                            font=("Calibri", 15, "bold"), bg="black").place(x=900, y=695)

        #cart
        Label(self.cart_frame, text="Cart", font=('calibri', 20, 'bold'), bg='black', fg='blue').pack(
            side="top", fill=X)
        self.cart_table = ttk.Treeview(self.cart_frame, selectmode='browse')
        self.cart_table["columns"] = ("1", "2", "3", "4")
        self.cart_table["show"] = 'headings'
        self.cart_table.heading("1", text="Item No")
        self.cart_table.column("1", width=100)
        self.cart_table.heading("2", text="Name")
        self.cart_table.heading("3", text="No of Serving")
        self.cart_table.column("3", width=150)
        self.cart_table.heading("4", text="Amount")
        self.cart_table.column("4", width=150)
        self.cart_table.place(x=0, y=40, width=614, height=500)
        self.fill_cart()

        place_order_btn = Button(self.menu_frame, command=self.place_order, text="Place Order", fg="white",
                         font=("Calibri", 15, "bold"), bg="black").place(x=800, y=800)


    def fill_menu(self):
        item_list = []
        x = con.execute('SELECT Dish_No FROM menu ORDER BY Dish_No')
        for i in x:
            item_list.append(i[0])
        for i in item_list:
            dish_ = con.execute('SELECT * FROM dishes where Dish_No=?', (i,))
            for dish in dish_:
                self.menu_table.insert("", 'end', iid=dish[4], text=dish[4], values=(dish[4], dish[0], dish[1], dish[2], dish[3], dish[5]))

    def fill_cart(self):
        for item in self.cart_table.get_children():
            self.cart_table.delete(item)
        cart_items = con.execute('SELECT * FROM cart')
        for item in cart_items:
            self.cart_table.insert("", 'end', iid=item[3], text=item[3], values=(item[3], item[0], item[1], item[2]))

    def add_to_cart(self):
        price_of_item = 0
        if self.item_no.get() == "":
            messagebox.showerror("error", "Enter an Item number", parent=self.root)
        else:
            item_no = int(self.item_no.get())
            item_name = ""
            if self.no_of_servings.get() == "":
                no_of_serving = 1
            else:
                no_of_serving = self.no_of_servings.get()
            price = con.execute('SELECT price, name FROM dishes WHERE Dish_No=?', (item_no,))
            for i in price:
                price_of_item, item_name = float(i[0]), i[1]
            total = price_of_item * float(no_of_serving)
            con.execute('INSERT INTO cart VALUES(?,?,?,?)', (item_name, no_of_serving, total, item_no))
            con.commit()
            self.fill_cart()
            self.item_no.delete(0, END)
            self.no_of_servings.delete(0, END)

    def place_order(self):
        items_str = ""
        ta = con.execute('SELECT SUM(amount) from cart')
        items = con.execute('SELECT item, servings FROM cart')
        for i in items:
            entry = i[0] + " x " + str(i[1]) + ", "
            items_str += entry
        for i in ta:
            total_amount = float(i[0])
        order_number = 0
        o_no = con.execute('SELECT MAX(orderID) from order_data')
        for i in o_no:
            order_number = i[0] + 1
        table_number = 1
        con.execute('INSERT INTO order_data VALUES(?,?,?,?,?,?)', (items_str, table_number, "offline", "recieved", total_amount, order_number))
        con.execute('DELETE FROM cart')
        con.commit()
        self.fill_cart()

    def remove_from_cart(self):
        item = self.item_no.get()
        servings = self.no_of_servings.get()
        if self.item_no.get() == "":
            messagebox.showerror("error", "Enter an Item number", parent=self.root)
        else:
            con.execute('DELETE FROM cart WHERE Dish_No=?', (item,))
            con.commit()
            if self.no_of_servings.get() != "":
                self.add_to_cart()

        self.fill_cart()



def customer_window():
    rt = Tk()
    obj = Customer(rt)
    rt.mainloop()

if __name__ == "__main__":
    customer_window()