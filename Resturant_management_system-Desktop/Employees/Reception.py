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

        title = Label(self.root, text="Receptionist Portal", font=("calibri", 40, "bold"), bg="black", fg="blue")
        title.pack(side=TOP, fill=X)

        navigation_frame = Frame(self.root, bd=4, relief=RIDGE, bg="navy blue")
        navigation_frame.place(x=5, y=80, width=400, height=930)

        content_frame = Frame(self.root, bg="gray")
        content_frame.place(x=360, y=80, width=1555, height=930)

        self.transaction_history = Frame(content_frame, bg='green')
        self.order_history = Frame(content_frame, bg='yellow')

        logout_btn = Button(self.root, command=self.logout, text="Logout", fg="black",
                            font=("Calibri", 15, "bold"), bg="white").place(x=1800, y=30)

        transaction = Button(navigation_frame, command=self.transaction_history, text="Transaction History", fg="black",
                             font=("Calibri", 15, "bold"), bg="light blue").place(x=0, y=80, width=340, height=250)

        order = Button(navigation_frame, command=self.order_history, text="Order History", fg="black",
                              font=("Calibri", 15, "bold"), bg="light blue").place(x=0, y=350, width=340, height=250)

    def transaction_history(self):
        #self.view_revenue.destroy()
        self.transaction_history.place(x=300, y=80, width=1425, height=884)
        L1 = Label(self.transaction_history,text= "Transcation History",font=('calibri',20,'bold'),bg='black',fg='blue')
        L1.pack(side="top",fill=X)

    def order_history(self):
        #self.update_user.destroy()
        self.order_history.place(x=300, y=80, width=1425, height=884)
        L1 = Label(self.order_history,text= "Order History",font=('calibri',20,'bold'),bg='black',fg='blue')
        L1.pack(side="top",fill=X)

    def logout(self):
        self.root.destroy()
        Login_window.init_login()

def init_receptionist_portal():
    rt = Tk()
    obj = Receptionist(rt)
    rt.mainloop()