from tkinter import *
from tkinter import ttk, messagebox
import Login_window


class Chef:
    def __init__(self, root):
        self.root = root
        self.root.title("Chef Portal")
        self.root.geometry("1280x720")

        kitchen_frame = Frame(self.root, bg="white")
        kitchen_frame.place(x=150, y=150, height=380, width=500)

        login_btn = Button(kitchen_frame, command=self.logout, text="Logout", fg="white",
                           font=("Calibri", 15, "bold"), bg="black").place(x=200, y=300)

    def refresh_order_list(self):
        pass

    def logout(self):
        self.root.destroy()
        Login_window.init_login()


def init_kitchen_portal():
    rt = Tk()
    obj = Chef(rt)
    rt.mainloop()


