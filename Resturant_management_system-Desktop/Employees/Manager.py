from tkinter import *
from tkinter import ttk, messagebox
from turtle import update
import Login_window

class Manager:
    def __init__(self, root):
        self.root = root
        self.root.title("Manager Portal")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        win_dims = str(screen_width) + "x" + str(screen_height)
        self.root.geometry(win_dims)

        title = Label(self.root,text= "Manager Portal",font=('calibri',40,'bold'),bg='black',fg='blue')
        title.pack(side=TOP,fill=X)

        navigation_frame = Frame(self.root, bd=4, relief=RIDGE, bg="navy blue")
        navigation_frame.place(x=5, y=80, width=400, height=930)

        content_frame = Frame(self.root, bg="gray")
        content_frame.place(x=360, y=80, width=1555, height=930)

        self.update_user = Frame(content_frame,bg='green')
        self.view_revenue = Frame(content_frame,bg='yellow')

        logout_btn = Button(self.root, command=self.logout, text="Logout", fg="black",
                            font=("Calibri", 15, "bold"), bg="white").place(x=1800, y=30)

        update_user = Button(navigation_frame, command=self.__update_user_details, text="Update Details", fg="black",
                            font=("Calibri", 15, "bold"), bg="light blue").place(x=0, y=80, width=340, height=250)

        view_revenue = Button(navigation_frame, command=self.__view_revenue, text="View Revenue", fg="black",
                            font=("Calibri", 15, "bold"), bg="light blue").place(x=0, y=350, width=340, height=250)

    def __update_user_details(self):
        #self.view_revenue.destroy()
        self.update_user.place(x=300, y=80, width=1425, height=884)
        L1 = Label(self.update_user,text= "Update Details",font=('calibri',20,'bold'),bg='black',fg='blue')
        L1.pack(side="top",fill=X)

    def __view_revenue(self):
        #self.update_user.destroy()
        self.view_revenue.place(x=300, y=80, width=1425, height=884)
        L1 = Label(self.view_revenue,text= "View Revenue",font=('calibri',20,'bold'),bg='black',fg='blue')
        L1.pack(side="top",fill=X)

    def __view_inventory(self):
        return
    
    def logout(self):
        self.root.destroy()
        Login_window.init_login()

def init_manager_portal():
    rt = Tk()
    obj = Manager(rt)
    rt.mainloop()

def manager_prep():
    return None
