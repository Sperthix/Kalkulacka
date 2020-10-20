from tkinter import *

okno = Tk()
okno.title("Kalkulacicocka")

medzivysledok = 0
akcia = 0

def klik(znak):
    aktualne = vstup.get()
    vstup.delete(0, END)
    vstup.insert(0, str(aktualne) + str(znak))
    return


def plus():
    global medzivysledok
    global akcia
    akcia = 1
    medzivysledok= int(vstup.get())
    vstup.delete(0, END)
    return


def minus():
    global medzivysledok
    global akcia
    akcia = 2
    medzivysledok = int(vstup.get())
    vstup.delete(0, END)

    return


def krat():
    global medzivysledok
    global akcia
    akcia = 3
    medzivysledok = int(vstup.get())
    vstup.delete(0, END)
    return


def deleno():
    global medzivysledok
    global akcia
    akcia = 4
    medzivysledok = int(vstup.get())
    vstup.delete(0, END)
    return

def rovna_sa():
    global medzivysledok
    global akcia
    if akcia == 1: vysledok = medzivysledok + int(vstup.get())
    elif akcia == 2: vysledok = medzivysledok - int(vstup.get())
    elif akcia == 3: vysledok = medzivysledok * int(vstup.get())
    elif akcia == 4: vysledok = medzivysledok // int(vstup.get())
    vstup.delete(0, END)
    vstup.insert(0, str(vysledok))
    return


vstup = Entry(okno, width=70, borderwidth=5)

vstup.grid(row=0, column=0, columnspan=3)

#Tlacidla

Tlacidlo_0 = Button(okno, text="0", padx=40, pady=20, command=lambda: klik(0))
Tlacidlo_1 = Button(okno, text="1", padx=40, pady=20, command=lambda: klik(1))
Tlacidlo_2 = Button(okno, text="2", padx=40, pady=20, command=lambda: klik(2))
Tlacidlo_3 = Button(okno, text="3", padx=40, pady=20, command=lambda: klik(3))
Tlacidlo_4 = Button(okno, text="4", padx=40, pady=20, command=lambda: klik(4))
Tlacidlo_5 = Button(okno, text="5", padx=40, pady=20, command=lambda: klik(5))
Tlacidlo_6 = Button(okno, text="6", padx=40, pady=20, command=lambda: klik(6))
Tlacidlo_7 = Button(okno, text="7", padx=40, pady=20, command=lambda: klik(7))
Tlacidlo_8 = Button(okno, text="8", padx=40, pady=20, command=lambda: klik(8))
Tlacidlo_9 = Button(okno, text="9", padx=40, pady=20, command=lambda: klik(9))

Tlacidlo_rovna_sa = Button(okno, text="=", padx=39, pady=20, command=rovna_sa)
Tlacidlo_vycisti = Button(okno, text="C", padx=40, pady=20, command=lambda: vstup.delete(0, END))

Tlacidlo_plus = Button(okno, text="+", padx=39, pady=20, command=plus)
Tlacidlo_minus = Button(okno, text="-", padx=39, pady=20, command=minus)
Tlacidlo_krat = Button(okno, text="*", padx=39, pady=20, command=krat)
Tlacidlo_deleno = Button(okno, text="/", padx=39, pady=20, command=deleno)


#Umiestnenie tlacidiel

Tlacidlo_1.grid(row=1, column=0)
Tlacidlo_2.grid(row=1, column=1)
Tlacidlo_3.grid(row=1, column=2)
Tlacidlo_4.grid(row=2, column=0)
Tlacidlo_5.grid(row=2, column=1)
Tlacidlo_6.grid(row=2, column=2)
Tlacidlo_7.grid(row=3, column=0)
Tlacidlo_8.grid(row=3, column=1)
Tlacidlo_9.grid(row=3, column=2)
Tlacidlo_0.grid(row=4, column=1)

Tlacidlo_rovna_sa.grid(row=4, column=2)
Tlacidlo_vycisti.grid(row=4, column=0)

Tlacidlo_plus.grid(row=1, column=4)
Tlacidlo_minus.grid(row=2, column=4)
Tlacidlo_krat.grid(row=3, column=4)
Tlacidlo_deleno.grid(row=4, column=4)


okno.mainloop()