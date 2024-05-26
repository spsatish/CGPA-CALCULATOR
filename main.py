from tkinter import *
from tkinter import messagebox

# create root window
from turtle import goto

root = Tk()
# set window title
root.title('CGPA CALCULATER')
# create canvas as a child to root window

f = Frame(root, height=400, width=600)

h = Label(bg='yellow', fg='black', text='CGPA CALCULATER', font="Times 24 bold")
h.place(x=280, y=1)
c = Canvas(f, bg='#FFF9A6', height=820, width=900)
# create a line in the canvas
id = c.create_line(30, 50, 870, 50, width=1, fill='black')
c.pack()

etgpa = IntVar()
etgpa1 = IntVar()

l = Label(f, text="SEMESTER-1", font="Helvetica 15 bold", justify='center',  bg="#00cca3")
l.place(x=310, y=65)
l1 = Label(f, text="Subject 1 :  ", bg="#FFF9A6", font="Times 17 bold")
l1.place(x=20, y=150)
l2 = Label(f, text="Subject 2 :  ", bg="#FFF9A6", font="Times 17 bold")
l2.place(x=20, y=180)
l3 = Label(f, text="Subject 3 :  ", bg="#FFF9A6", font="Times 17 bold")
l3.place(x=20, y=210)
l4 = Label(f, text="Subject 4 :  ", bg="#FFF9A6", font="Times 17 bold")
l4.place(x=20, y=240)
l5 = Label(f, text="Subject 5 :  ", bg="#FFF9A6", font="Times 17 bold")
l5.place(x=20, y=270)
l6 = Label(f, text="Subject 6 :  ", bg="#FFF9A6", font="Times 17 bold")
l6.place(x=20, y=300)

l7 = Label(f, text='Grade', fg='black', bg='white', borderwidth=2, font='Verdana', relief='solid')
l7.place(x=210, y=110, width=120)
l7 = Label(f, text='Credit', fg='black', bg='white', borderwidth=2, font='Verdana', relief='solid')
l7.place(x=400, y=110, width=120)

# entry of grades and credits
g2 = IntVar()
g1 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g1.place(x=210, y=160, width=120)
g2 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g2.place(x=400, y=160, width=120)
g3 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g3.place(x=210, y=190, width=120)
g4 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g4.place(x=400, y=190, width=120)
g5 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g5.place(x=210, y=220, width=120)
g6 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g6.place(x=400, y=220, width=120)
g7 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g7.place(x=210, y=250, width=120)
g8 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g8.place(x=400, y=250, width=120)
g9 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g9.place(x=210, y=280, width=120)
g10 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g10.place(x=400, y=280, width=120)
g11 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g11.place(x=210, y=310, width=120)
g12 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g12.place(x=400, y=310, width=120)

# sem2
id = c.create_line(30, 350, 870, 350, width=1, fill='black')
c.pack()

lsem2 = Label(f, text="SEMESTER-2".center(20), font="Helvetica 15 bold", justify='center',  bg="#00cca3")
lsem2.place(x=310, y=380)
l8 = Label(f, text="Subject 1 :  ", bg="#FFF9A6", font="Times 17 bold")
l8.place(x=20, y=470)
l9 = Label(f, text="Subject 2 :  ", bg="#FFF9A6", font="Times 17 bold")
l9.place(x=20, y=500)
l10 = Label(f, text="Subject 3 :  ", bg="#FFF9A6", font="Times 17 bold")
l10.place(x=20, y=530)
l11 = Label(f, text="Subject 4 :  ", bg="#FFF9A6", font="Times 17 bold")
l11.place(x=20, y=560)
l12 = Label(f, text="Subject 5 :  ", bg="#FFF9A6", font="Times 17 bold")
l12.place(x=20, y=590)
l13 = Label(f, text="Subject 6 :  ", bg="#FFF9A6", font="Times 17 bold")
l13.place(x=20, y=620)

l14 = Label(f, text='Grade', fg='black', bg='white', borderwidth=2, font='Verdana', relief='solid')
l14.place(x=210, y=430, width=120)
l15 = Label(f, text='Credit', fg='black', bg='white', borderwidth=2, font='Verdana', relief='solid')
l15.place(x=400, y=430, width=120)

g13 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g13.place(x=210, y=480, width=120)
g14 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g14.place(x=400, y=480, width=120)
g15 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g15.place(x=210, y=510, width=120)
g16 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g16.place(x=400, y=510, width=120)
g17 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g17.place(x=210, y=540, width=120)
g18 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g18.place(x=400, y=540, width=120)
g19 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g19.place(x=210, y=570, width=120)
g20 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g20.place(x=400, y=570, width=120)
g21 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g21.place(x=210, y=600, width=120)
g22 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g22.place(x=400, y=600, width=120)
g23 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g23.place(x=210, y=630, width=120)
g24 = Entry(f, bg='white', fg='black', borderwidth=1, relief='solid')
g24.place(x=400, y=630, width=120)

# final cgpa


# backend

# storing all the grades of sem1 in array


tgpa1 = 0.00


def calculatetgpa1():
    global tgpa1
    # storing all the grades of sem1 in array
    global grades, credits
    grades = []
    grades.append(g1.get())
    grades.append(g3.get())
    grades.append(g5.get())
    grades.append(g7.get())
    grades.append(g9.get())
    grades.append(g11.get())

    # storing all the credits of sem1 in array
    credits = []

    credits.append(int(eval(g2.get())))
    credits.append(int(eval(g4.get())))
    credits.append(int(eval(g6.get())))
    credits.append(int(eval(g8.get())))
    credits.append(int(eval(g10.get())))
    credits.append(int(eval(g12.get())))

    tsum = 0
    sum_credits = 0
    for i in range(0, 6):
        if (grades[i] == 'O'):
            tsum = tsum + 10 * credits[i]
        elif (grades[i] == 'A+'):
            tsum = tsum + 9 * credits[i]
        elif (grades[i] == 'A'):
            tsum = tsum + 8 * credits[i]
        elif (grades[i] == 'B+'):
            tsum = tsum + 7 * credits[i]
        elif (grades[i] == 'B'):
            tsum = tsum + 6 * credits[i]
        elif (grades[i] == 'C'):
            tsum = tsum + 5 * credits[i]
        elif (grades[i] == 'E'):
            tsum = tsum + 0 * credits[i]
        elif (grades[i] == ''):
            messagebox.showinfo('Empty grade', "please enter grade")
            goto(41)
        else:
            messagebox.showinfo('Invalid grade', "please enter a valid grade")
            goto(41)
    for j in range(0, 6):
        sum_credits = sum_credits + credits[j]

    tgpa1 = float("{:.2f}".format(tsum / sum_credits))
    etgpa = Label(bg='#0000FF', fg='white', borderwidth=2, height=1, width=20, font="sans 12", relief='solid', text=tgpa1)
    etgpa.place(x=700, y=200)


tgpa2 = 0.00


def calculatetgpa2():
    global grades1, credits1
    global tgpa2
    grades1 = []
    grades1.append(g13.get())
    grades1.append(g15.get())
    grades1.append(g17.get())
    grades1.append(g19.get())
    grades1.append(g21.get())
    grades1.append(g23.get())

    # storing all the credits of sem1 in array
    credits1 = []
    credits1.append(int(eval(g14.get())))
    credits1.append(int(eval(g16.get())))
    credits1.append(int(eval(g18.get())))
    credits1.append(int(eval(g20.get())))
    credits1.append(int(eval(g22.get())))
    credits1.append(int(eval(g24.get())))
    tsum1 = 0
    sum_credits1 = 0
    for i in range(0, 6):
        if (grades1[i] == 'O'):
            tsum1 = tsum1 + 10 * credits1[i]
        elif (grades1[i] == 'A+'):
            tsum1 = tsum1 + 9 * credits1[i]
        elif (grades1[i] == 'A'):
            tsum1 = tsum1 + 8 * credits1[i]
        elif (grades1[i] == 'B+'):
            tsum1 = tsum1 + 7 * credits1[i]
        elif (grades1[i] == 'B'):
            tsum1 = tsum1 + 6 * credits1[i]
        elif (grades1[i] == 'C'):
            tsum1 = tsum1 + 5 * credits1[i]
        elif (grades1[i] == 'E'):
            tsum1 = tsum1 + 0 * credits1[i]
        elif (grades1[i] == ''):
            messagebox.showinfo('Empty grade', "please enter grade")
            goto()
        else:
            messagebox.showinfo('Invalid grade', "please enter a valid grade")
            goto()

    for j in range(0, 6):
        sum_credits1 = sum_credits1 + credits1[j]

    tgpa2 = float("{:.2f}".format(tsum1 / sum_credits1))
    etgpa1 = Label(bg= '#0000FF', fg='white', borderwidth=2, height=1, width=20, font="sans 12", relief='solid', text=tgpa2)
    etgpa1.place(x=700, y=500)


cgpa = 0.00
id = c.create_line(30, 670, 870, 670, width=1, fill='black')
lcgpa = LabelFrame(bg='#8B0A50', height=80, width=200, font="sans 12")
lcgpa.place(x=40, y=700)


def calculatecgpa():
    global cgpa
    cgpa = float((tgpa1 + tgpa2) / 2)
    m1 = Label(lcgpa, text=cgpa, font="Helvetica 15")
    m1.grid(row=1, column=5)


def remarks():
    count = 0
    count1 = 0
    global subno, subno1

    # checking reappear in 1st sem
    for i in range(0, 6):
        if grades[i] == 'E':
            subno = i
            count = count + 1
    # checking reappear in 2nd sem
    for i in range(0, 6):
        if grades1[i] == 'E':
            subno1 = i
            count1 = count1 + 1
    if (count > 0 and count1 == 0):
        m2 = Label(lcgpa, text=('Reappear in subject', subno + 1, 'in semester 1'), borderwidth=1, width=30, font="Helvetica 15")
        m2.grid(row=2, column=2)
    elif (count == 0 and count1 > 0):
        m2 = Label(lcgpa, text=('Reappear in subject', subno1 + 1, 'in semester 2'), borderwidth=1, width=30, font="Helvetica 15")
        m2.grid(row=2, column=2)
    elif (count > 0 and count1 > 0):
        m2 = Label(lcgpa, text='Reappear in both semesters', borderwidth=1, width=30, font="Helvetica 15")
        m2.grid(row=2, column=2)
    else:
        m2 = Label(lcgpa, text='Pass', borderwidth=1, width=30, font="Helvetica 15")
        m2.grid(row=2, column=2)


# cgpacalulate
l1cgpa = Button(lcgpa, text='CGPA', borderwidth=1, relief='solid', bg='#FFC125', width=10, height=2, font="Helvetica 12 bold",
                command=calculatecgpa)
l1cgpa.grid(row=1, column=2)

# remarks
l2cgpa = Button(lcgpa, text='Remarks', borderwidth=1, relief='solid', bg='#FF3030', width=10, height=2, font="Helvetica 12 bold", command=remarks)
l2cgpa.grid(row=2, column=2)

# calculatetgpa1
ltgpa = Button(text='TGPA', bg='#FF1493', fg='white', font="sans 10", borderwidth=2, relief='solid', width=30, command=calculatetgpa1)
ltgpa.place(x=600, y=200, width=80)

# calculatetgpa2
ltgpa = Button(text='TGPA', bg='#FF1493', fg='white', font="sans 10",  borderwidth=2, relief='solid', width=30, command=calculatetgpa2)
ltgpa.place(x=600, y=500, width=80)

c.pack()
f.pack()
root.mainloop()