from tkinter import *
from tkinter import ttk, messagebox
import Login_window


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
        order_table = ttk.Treeview(orders_frame, columns=("Order ID", "Items", "Order Mode"))
        order_table.place(x=0, y=0, width=1400, height=500)

    def refresh_order_list(self):
        pass

    def logout(self):
        self.root.destroy()
        Login_window.init_login()


def init_kitchen_portal():
    rt = Tk()
    obj = Chef(rt)
    rt.mainloop()


