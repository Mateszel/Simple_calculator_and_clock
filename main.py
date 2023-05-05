from tkinter import *
from time import strftime


def replace_a(x):
    a[0] = x


def change_button_skin(y):
    button_0.config(bg=y)
    button_1.config(bg=y)
    button_2.config(bg=y)
    button_3.config(bg=y)
    button_4.config(bg=y)
    button_5.config(bg=y)
    button_6.config(bg=y)
    button_7.config(bg=y)
    button_8.config(bg=y)
    button_9.config(bg=y)
    button_add.config(bg=y)
    button_subtraction.config(bg=y)
    button_multiplying.config(bg=y)
    button_dividing.config(bg=y)
    button_CE.config(bg=y)


def adding():
    b[0] += a[0]
    label_wynik = Label(text="Wynik:   "+str("%.2f" % b[0]), fg="black", width=20, height=3)
    label_wynik.place(x=0, y=286)


def subtraction():
    b[0] -= a[0]
    label_wynik = Label(text="Wynik:   " + str("%.2f" % b[0]), fg="black", width=20, height=3)
    label_wynik.place(x=0, y=286)


def dividing():
    if a[0] == 0:
        print('Cant divide by 0')
    else:
        b[0] = b[0]/a[0]
    label_wynik = Label(text="Wynik:   " + str("%.2f" % b[0]), fg="black", width=20, height=3)
    label_wynik.place(x=0, y=286)


def multiplying():
    b[0] = b[0]*a[0]
    label_wynik = Label(text="Wynik:   " + str("%.2f" % b[0]), fg="black", width=20, height=3)
    label_wynik.place(x=0, y=286)


def getTextInput():
    result = textExample.get("1.0", "end")
    a[0] = float(result)


def Clear_everything():
    b[0] = 0
    label_wynik = Label(text="Wynik:   " + str("%.2f" % b[0]), fg="black", width=20, height=3)
    label_wynik.place(x=0, y=286)


def time():
    string = strftime('%H:%M:%S')
    clock_label.config(text=string)
    clock_label.after(1000, time)


def clock_color(x):
    clock_label.config(bg=x)


def change_background():
    if buf[0] == 0:
        background_label.config(image=bg_2)
        buf[0] = 1
    elif buf[0] == 1:
        background_label.config(image=bg_3)
        buf[0] = 2
    elif buf[0] == 2:
        background_label.config(image=bg_1)
        buf[0] = 0


a = [0]
b = [0]
buf = [0]

# building window
root = Tk()
root.geometry("800x640")

# label frame
frame1 = Frame(master=root, width=800, height=50, bg="grey")
frame1.place(x=0, y=0)

# background
bg_1 = PhotoImage(file="back_4.png")
bg_2 = PhotoImage(file="back_6.png")
bg_3 = PhotoImage(file="back_1.png")
background_label = Label(root, image=bg_1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
button_background = Button(root, width=20, height=5, text="Change background", command=lambda: change_background())
button_background.place(x=250, y=550)

# main label
label1 = Label(text="Prosty kalkulator i zegar", fg="black", width=40, height=3)
label1.pack()

# typing number in
textExample = Text(root, height=1, width=20)
textExample.place(x=0, y=344)
btnRead = Button(root, height=1, width=10, text="Read number", command=getTextInput)
btnRead.place(x=45, y=364)

# defining number buttons
button_1 = Button(root, text=" 1 ", width=6, height=3, command=lambda: replace_a(1))
button_1.place(x=0, y=54)
button_2 = Button(root, text=" 2 ", width=6, height=3, command=lambda: replace_a(2))
button_2.place(x=54, y=54)
button_3 = Button(root, text=" 3 ", width=6, height=3, command=lambda: replace_a(3))
button_3.place(x=108, y=54)
button_4 = Button(root, text=" 4 ", width=6, height=3, command=lambda: replace_a(4))
button_4.place(x=0, y=112)
button_5 = Button(root, text=" 5 ", width=6, height=3, command=lambda: replace_a(5))
button_5.place(x=54, y=112)
button_6 = Button(root, text=" 6 ", width=6, height=3, command=lambda: replace_a(6))
button_6.place(x=108, y=112)
button_7 = Button(root, text=" 7 ", width=6, height=3, command=lambda: replace_a(7))
button_7.place(x=0, y=170)
button_8 = Button(root, text=" 8 ", width=6, height=3, command=lambda: replace_a(8))
button_8.place(x=54, y=170)
button_9 = Button(root, text=" 9 ", width=6, height=3, command=lambda: replace_a(9))
button_9.place(x=108, y=170)
button_0 = Button(root, text=" 0 ", width=6, height=3, command=lambda: replace_a(0))
button_0.place(x=54, y=228)

# defining actions
button_add = Button(root, text=" + ", width=6, height=3, command=lambda: adding())
button_add.place(x=162, y=54)
button_subtraction = Button(root, text=" - ", width=6, height=3, command=lambda: subtraction())
button_subtraction.place(x=162, y=112)
button_multiplying = Button(root, text=" * ", width=6, height=3, command=lambda: multiplying())
button_multiplying.place(x=162, y=170)
button_dividing = Button(root, text=" / ", width=6, height=3, command=lambda: dividing())
button_dividing.place(x=162, y=228)
button_CE = Button(root, text=" C ", width=6, height=3, command=lambda: Clear_everything())
button_CE.place(x=0, y=228)

# changing calculator colors
click_button_1 = Button(root, text="Blue", width=10, height=5, command=lambda: change_button_skin('blue'))
click_button_1.place(x=0, y=450)
click_button_2 = Button(root, text="Red", width=10, height=5, command=lambda: change_button_skin('red'))
click_button_2.place(x=80, y=450)
click_button_3 = Button(root, text="White", width=10, height=5, command=lambda: change_button_skin('white'))
click_button_3.place(x=160, y=450)

# clock
clock_label = Label(root, font=('calibri', 60, 'bold'), bg="purple")
clock_label.place(x=350, y=120)
time()

# changing clock colors
click_button_clock = Button(root, text="Blue Clock", width=10, height=5, command=lambda: clock_color('blue'))
click_button_clock.place(x=0, y=550)
click_button_clock_1 = Button(root, text="Red Clock", width=10, height=5, command=lambda: clock_color('red'))
click_button_clock_1.place(x=80, y=550)
click_button_clock_2 = Button(root, text="White Clock", width=10, height=5, command=lambda: clock_color('white'))
click_button_clock_2.place(x=160, y=550)

# click_button.config(width=50)
root.mainloop()
