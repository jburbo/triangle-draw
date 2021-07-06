from tkinter import *
from tkinter import Label


def setwindow(root):  # separete function 1
    root.title("Programm Window")
    root.resizable(False, False)  # windows change permision

    w = 550
    h = 650
    ws = root.winfo_screenmmwidth()
    wh = root.winfo_screenheight()

    x = int(ws * 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))


root = Tk()
setwindow(root)  # separete function 1

label = Label(root, text="Triangle Draw", font="Tahome 18", bg="#ccffdd")
label.pack()  # method pack


# Buuton
def handlerButton(event=False):
    global en1
    global en2
    global en3
    global result1
    global result2
    try:
        a = float(en1.get())
        b = float(en2.get())
        c = float(en3.get())

        if a == 0 and b == 0 and c == 0:
            result2.config(text="you haven't entered anything!")
        elif a + b >= c and b + c >= a and a + c >= b:
            # result2.config(text="Triangle exsist")

            if a == b and a == c and c == b:
                result1.config(image=photo2)
                result2.config(text="Equilateral triangle")
            elif a == b or b == c or a == c:
                result1.config(image=photo1)
                result2.config(text="Isosceles triangle")
            else:
                result1.config(image=photo3)
                result2.config(text="Versatile triangle")
        else:
            result2.config(text="Not possible")

    except ValueError:
        if not en1.get() or not en2.get() or not en3.get():
            result2.config(text="you haven't entered anything!")
        else:
            result2.config(text="You entered not a number!")


button = Button(root, text="Submit", font="Tahoma 16", command=handlerButton, bg="Blue", fg="Red")
button.pack()

# Input fields (three areas)
en1 = Entry(root, font="Tahoma")
en2 = Entry(root, font="Tahoma")
en3 = Entry(root, font="Tahoma")
en1.pack()
en2.pack()
en3.pack()


# Tags(Метки)
label1 = Label(root, text="A:", font="Tahome 16", bg="#ccffdd")
label2 = Label(root, text="B:", font="Tahome 16", bg="#ccffdd")
label3 = Label(root, text="C:", font="Tahome 16", bg="#ccffdd")

# Tags placment(размешенияметки)
label1.place(relx=0.15, rely=0.55)
label2.place(relx=0.15, rely=0.65)
label3.place(relx=0.15, rely=0.75)
button.place(relx=0.2, rely=0.85, anchor="n")

# method insert field
en1.insert(END, " ")
en2.insert(END, " ")
en3.insert(END, " ")

en1.place(relx=0.4, rely=0.55, anchor="n")
en2.place(relx=0.4, rely=0.65, anchor="n")
en3.place(relx=0.4, rely=0.75, anchor="n")


# output of results
frame1 = Frame(master=root, width=330, height=300, bg="", bd=1)
frame1.pack()

photo = PhotoImage(file="triangle_0.png")
photo1 = PhotoImage(file="isosceles triangle.png")
photo2 = PhotoImage(file="equilateral triangle .png")
photo3 = PhotoImage(file="versatile triangle .png")

# Place1 for Triangle pictures

# label1 = Label(master=frame1, text="Triangle", bg="red")
# label1 = Label(master=frame1, image=result1)

result1 = Label(master=frame1, image=photo)
result1.place(x=160, y=130, anchor="center")

# Place2 for Text
# label5 = Label(master=frame1, text="Equilateral Triangle", bg="yellow")
# label5=Label(master=frame1, text=result, bg="yellow")

result2 = Label(master=frame1, font="Tahoma", bg="yellow")
result2.place(x=160, y=270, anchor="center")

# To enter from the "Enter" button
#a = en1.bind("<Return>", handlerButton()) # not working
#b = en2.bind("<Return>", handlerButton())
#c = en3.bind("<Return>", handlerButton())

root.mainloop()  # infinity loop for work windows
