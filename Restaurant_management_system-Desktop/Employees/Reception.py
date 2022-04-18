from tkinter import *
from tkinter import ttk, messagebox
import Login_window


class Receptionist:
    def __init__(self, root):
        self.root = root
        self.root.title("Receptionist Portal")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        win_dims = str(screen_width) + "x" + str(screen_height)
        self.root.geometry(win_dims)

        logout_btn = Button(self.root, command=self.logout, text="Logout", fg="white",
                            font=("Calibri", 15, "bold"), bg="black").place(x=1800, y=30)

    def logout(self):
        self.root.destroy()
        Login_window.init_login()


def init_receptionist_portal():
    rt = Tk()
    obj = Receptionist(rt)
    rt.mainloop()
