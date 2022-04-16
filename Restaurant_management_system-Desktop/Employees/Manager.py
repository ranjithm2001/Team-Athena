from tkinter import *
from tkinter import ttk, messagebox
import Login_window


class Manager:
    def __init__(self, root):
        self.root = root
        self.root.title("Manager Portal")
        self.root.geometry("1280x720")

        manager_frame = Frame(self.root, bg="white")
        manager_frame.place(x=150, y=150, height=380, width=500)

        login_btn = Button(manager_frame, command=self.logout, text="Logout", fg="white",
                           font=("Calibri", 15, "bold"), bg="black").place(x=200, y=300)

    def logout(self):
        self.root.destroy()
        Login_window.init_login()


def init_manager_portal():
    rt = Tk()
    obj = Manager(rt)
    rt.mainloop()


def manager_prep():
    return None
