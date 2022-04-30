from tkinter import *
from tkinter import ttk, messagebox
from turtle import update
import Login_window


class Manager:
    def __init__(self, root):
        self.root = root
        self.root.title("Kitchen Portal Portal")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        win_dims = str(screen_width) + "x" + str(screen_height)
        self.root.geometry(win_dims)

        title = Label(self.root, text="Manager Portal", font=("calibri", 40, "bold"), bg="black", fg="blue")
        title.pack(side=TOP, fill=X)

        self.content_frame = Frame(self.root, bg="gray")
        self.content_frame.place(x=360, y=80, width=1555, height=930)

        navigation_frame = Frame(self.root, bd=4, relief=RIDGE, bg="navy blue")
        navigation_frame.place(x=5, y=80, width=350, height=930)

        logout_btn = Button(self.root, command=self.logout, text="Logout", fg="black",
                            font=("Calibri", 15, "bold"), bg="white").place(x=1800, y=30)

        self.upd_usr_btn = Button(navigation_frame, command=self.__update_user_details, text="Update User", fg="black",
                                  font=("Calibri", 25, "bold"), bg="light blue").place(x=0, y=350, width=340,
                                                                                       height=250)

        self.view_rvn_btn = Button(navigation_frame, command=self.__view_revenue, text="View Revenue", fg="black",
                                   font=("Calibri", 25, "bold"), bg="light blue").place(x=0, y=80, width=340,
                                                                                        height=250)

        self.view_inv_btn = Button(navigation_frame, command=self.__view_inventory, text="View Inventory", fg="black",
                                   font=("Calibri", 25, "bold"), bg="light blue").place(x=0, y=620, width=340,
                                                                                        height=250)

        self.update_usr_frame = Frame(self.content_frame, bg="gray")
        self.view_rvn_frame = Frame(self.content_frame, bg='gray')
        self.view_inv_frame = Frame(self.content_frame, bg="white")
        self.view_inv_frame.place(x=0, y=70, width=1555, height=500)

        self.view_inv_lbl = Label(self.view_inv_frame, text="View Inventory", font=('calibri', 20, 'bold'), bg='black',
                                  fg='blue')
        self.view_rvn_lbl = Label(self.view_rvn_frame, text="View Revenue", font=('calibri', 20, 'bold'), bg='black',
                                  fg='blue')
        self.update_usr_lbl = Label(self.update_usr_frame, text="Update User", font=('calibri', 20, 'bold'), bg='black',
                                    fg='blue')

        self.view_inv = ttk.Treeview(self.view_inv_frame, selectmode='browse')
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Calibri", 15))
        self.view_inv["columns"] = ("1")
        self.view_inv["show"] = 'headings'
        self.view_inv.heading("1")
        self.view_inv.place(x=0, y=45, width=1555, height=500)
        self.__view_revenue()

        self.update_usr = ttk.Treeview(self.update_usr_frame, selectmode='browse')
        self.update_usr["columns"] = ("1")
        self.update_usr["show"] = 'headings'
        self.update_usr.place(x=0, y=45, width=1555, height=500)
        self.__update_user_details()

        self.view_rvn = ttk.Treeview(self.view_rvn_frame, selectmode='browse')
        self.view_rvn["columns"] = ("1")
        self.view_rvn["show"] = 'headings'
        self.view_rvn.place(x=0, y=45, width=1555, height=500)
        self.__view_revenue()

        self.dish_no = Entry(self.update_usr_frame, font=("Calibri", 15))
        self.dish_no.place(x=200, y=600)

        """add_btn = Button(self.update_usr_frame, command=self.remove_from_menu, text="Remove Dish from Menu", fg="white",
                         font=("Calibri", 15, "bold"), bg="black").place(x=500, y=600)

        remove_btn = Button(self.update_usr_frame, command=self.add_to_menu, text="Add Dish to Menu", fg="white",
                            font=("Calibri", 15, "bold"), bg="black").place(x=800, y=600)
"""

    def __update_user_details(self):
        self.view_rvn_frame.place_forget()
        self.view_inv_frame.place_forget()
        self.update_usr_lbl.pack(side="top", fill=X)
        self.update_usr_frame.place(x=0, y=70, width=1555, height=500)

    def __view_revenue(self):
        self.update_usr_frame.place_forget()
        self.view_inv_frame.place_forget()
        self.view_rvn_lbl.pack(side="top", fill=X)
        self.view_rvn_frame.place(x=0, y=70, width=1555, height=500)

    def __view_inventory(self):
        self.update_usr_frame.place_forget()
        self.view_rvn_frame.place_forget()
        self.view_inv_lbl.pack(side="top", fill=X)
        self.view_inv_frame.place(x=0, y=70, width=1555, height=500)

    def logout(self):
        self.root.destroy()
        Login_window.init_login()


def init_manager_portal():
    rt = Tk()
    obj = Manager(rt)
    rt.mainloop()


def manager_prep():
    return None
