from tkinter import *
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.units import mm, inch
from tkinter import messagebox
from reportlab.pdfgen import canvas
from PIL import Image, ImageTk

root = Tk()
root.geometry("796x465")
root.resizable(width=0, height=0)
root.title("CERTIFICATE GENERATOR v1.0")

#photo = PhotoImage(file="main.png", width=200, height=150)
#photolabel = Label(root, image=photo)
#photolabel.place(x=100, y=50)

load2 = Image.open("main.png")
img2 = ImageTk.PhotoImage(Image.open("main.png"))
resized2 = load2.resize((460,320), Image.ANTIALIAS)
new_pic2 = ImageTk.PhotoImage(resized2)
panel2 = Label(root, image = new_pic2)
panel2.place(x=310,y=90)

#resized = photo.resize((400,300), Image.ANTIALIAS)
#new_pic = PhotoImage(resized)
#photolabel2 = Label(root, image=new_pic)
#photolabel2.place(x=150, y=50)



def gen():


    if(e1.get()=='' or e2.get()=='' or e3.get()=='' or e4.get()==''):

        messagebox.showerror("Error","All Fields are mandatory!" )
    else:

        pagesize = (11 * inch, 8 * inch)
        pdf = canvas.Canvas('cert.pdf', pagesize=pagesize)

        pdf.drawImage('background.png', 10,10,772,555)

        pdf.drawString(240,75, e4.get().upper())
        pdf.drawString(440,75, e3.get().upper())
        pdf.drawString(407, 191, e2.get().upper())


        pdf.setFont("Helvetica", 36)
        #pdf.setFillColorRGB(0,255,0)
        pdf.drawString(245,275, e1.get().upper())



        pdf.showPage()
        pdf.save()

        messagebox.showinfo("Status","YOUR CERTIFICATE IS GENERATED! ")







frame1 = LabelFrame(root, text="INSTRUCTION").place(x=10, y=20, width=400, height=305)
l1 = Label(frame1, text="Name Of Awardee : ").place(x=20, y=60)
l2 = Label(frame1, text="Event Name : ").place(x=20, y=100)
l3 = Label(frame1, text="Name Of Event Organizer : ").place(x=20, y=140)
l4 = Label(frame1, text="Name Of Coordinator : ").place(x=20, y=180)

e1 = Entry(frame1)
e1.place(x=200, y=60)
e2 = Entry(frame1)
e2.place(x=200, y=100)
e3 = Entry(frame1)
e3.place(x=200, y=140)
e4 = Entry(frame1)
e4.place(x=200, y=180)

b1 = Button(frame1, text="Generate Certificate", relief="solid", bg="gold",fg="black",highlightcolor="blue" ,command=gen).place(x=210, y=250)











root.mainloop()
