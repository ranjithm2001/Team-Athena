from tkinter import *
from tkinter import ttk, messagebox
from Employees import Manager, Reception, Kitchen
import cv2
from PIL import ImageTk, Image
import sqlite3
con = sqlite3.connect('database.db')


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Portal Login")
        self.root.geometry("1280x720")

        login_form = Frame(self.root, bg="white")
        login_form.place(x=150, y=150, height=380, width=500)

        global web_cam_display
        web_cam_display = Label(self.root)
        web_cam_display.place(x=700, y=150, height=400, width=400)

        title = Label(login_form, text="Login", font=("Calibri", 25, "bold"), bg="white").place(x=40, y=30)

        user_label = Label(login_form, text="Employee ID", font=("Calibri", 15, "bold"), bg="white").place(x=40, y=160)
        self.user_txt = Entry(login_form, font=("Calibri", 15))
        self.user_txt.place(x=190, y=160)

        password_label = Label(login_form, text="Password", font=("Calibri", 15, "bold"), bg="white").place(x=40, y=220)
        self.password_text = Entry(login_form, font=("Calibri", 15))
        self.password_text.place(x=190, y=220)

        login_btn = Button(login_form, command=self.validate_login, text="Login", fg="white", font=("Calibri", 15, "bold"), bg="black").place(x=200, y=300)
        #threading.Timer(0.5, self.scan_qr).start()

    def scan_qr(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)
            web_cam_display.imgtk = image
            web_cam_display.configure(image=image)

            cv2.waitKey(1)

    def validate_login(self):
        username = self.user_txt.get()
        password = self.password_text.get()
        if username == "" or password == "":
            messagebox.showerror("error", "All field required", parent=self.root)
        elif username == "chef":
            self.root.destroy()
            Kitchen.init_kitchen_portal()
        elif username == "manager":
            self.root.destroy()
            Manager.init_manager_portal()
        elif username == "receptionist":
            self.root.destroy()
            Reception.init_receptionist_portal()

def init_login():
    rt = Tk()
    obj = Login(rt)
    rt.mainloop()

if __name__ == "__main__":
    init_login()
