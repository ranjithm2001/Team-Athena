from tkinter import *
from tkinter import ttk, messagebox
import Login_window


class Receptionist:
    def __init__(self, root):
        self.root = root
        self.root.title("Receptionist Portal")
        self.root.geometry("1280x720")

        receptionist_frame = Frame(self.root, bg="white")
        receptionist_frame.place(x=150, y=150, height=380, width=500)

        login_btn = Button(receptionist_frame, command=self.logout, text="Logout", fg="white",
                           font=("Calibri", 15, "bold"), bg="black").place(x=200, y=300)

    def logout(self):
        self.root.destroy()
        Login_window.init_login()


def init_receptionist_portal():
    rt = Tk()
    obj = Receptionist(rt)
    rt.mainloop()
