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

        logout_btn = Button(self.root, command=self.logout, text="Logout", fg="black",
                            font=("Calibri", 15, "bold"), bg="white").place(x=1800, y=30)

        transaction = Button(navigation_frame, command=self.t_history, text="Transaction History", fg="black",
                             font=("Calibri", 15, "bold"), bg="light blue").place(x=0, y=80, width=340, height=250)

        order = Button(navigation_frame, command=self.o_history, text="Order History", fg="black",
                              font=("Calibri", 15, "bold"), bg="light blue").place(x=0, y=350, width=340, height=250)

        self.t_frame = Frame(content_frame, bg='gray')
        self.o_frame = Frame(content_frame, bg='gray')
        self.t_frame.place(x=0, y=0, width=1555, height=930)

        t_label = Label(self.t_frame, text="Transaction History", font=('calibri', 20, 'bold'), bg='black',fg='blue')
        t_label.pack(side="top", fill=X)

        o_label = Label(self.o_frame, text="Order History", font=('calibri', 20, 'bold'), bg='black',fg='blue')
        o_label.pack(side="top", fill=X)

        self.t_table = ttk.Treeview(self.t_frame, selectmode='browse')
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Calibri", 15))
        self.t_table["columns"] = ("1","2","3","4","5","6")
        self.t_table["show"] = 'headings'
        self.t_table.heading("1", text="OrderID")
        self.t_table.heading("2", text="Items")
        self.t_table.heading("3", text="Table number")
        self.t_table.heading("4", text="Mode")
        self.t_table.heading("4", text="Status")
        self.t_table.heading("4", text="Amount")
        self.t_table.place(x=0, y=40, width=1555, height=500)
        self.t_history()

        self.o_table = ttk.Treeview(self.o_frame, selectmode='browse')
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Calibri", 15))
        self.o_table["columns"] = ("1", "2", "3", "4", "5", "6")
        self.o_table["show"] = 'headings'
        self.o_table.heading("1", text="OrderID")
        self.o_table.heading("2", text="Items")
        self.o_table.heading("3", text="Table number")
        self.o_table.heading("4", text="Mode")
        self.o_table.heading("4", text="Status")
        self.o_table.heading("4", text="Amount")
        self.o_table.place(x=0, y=60, width=1555, height=500)
        self.o_history()

    def t_history(self):
        self.o_frame.place_forget()
        self.t_frame.place(x=0, y=0, width=1555, height=930)
        t = Login_window.con.execute('SELECT * from order_data where status="delivered"')
        for item in self.t_table.get_children():
            self.t_table.delete(item)
        for i in t:
            self.t_table.insert("", 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3],i[4],i[5]))

    def o_history(self):
        self.t_frame.place_forget()
        self.o_frame.place(x=0, y=0, width=1555, height=930)
        o = Login_window.con.execute('SELECT * from order_data')
        for item in self.o_table.get_children():
            self.o_table.delete(item)
        for i in o:
            self.o_table.insert("", 'end', iid=i[0], text=i[0], values=(i[0], i[1], i[2], i[3], i[4], i[5]))

    def logout(self):
        self.root.destroy()
        Login_window.init_login()

def init_receptionist_portal():
    rt = Tk()
    obj = Receptionist(rt)
    rt.mainloop()

# receptionist