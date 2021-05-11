import tkinter

root = tkinter.Tk()
root.title("La mia calcolatrice")

entraTesto = tkinter.Entry(root, width=28, borderwidth=5)
entraTesto.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def clickBtn(number):
    numCorrente = entraTesto.get()
    entraTesto.delete(0, 'end')
    entraTesto.insert(0, str(numCorrente) + str(number))

def btnCanc():
    entraTesto.delete(0, 'end')

def btnSomma():
    primoNum = entraTesto.get()
    global p_num
    global opMat
    opMat = 'somma'
    #--
    p_num = int(primoNum)
    entraTesto.delete(0, 'end')

def btnSottr():
    primoNum = entraTesto.get()
    global p_num
    global opMat
    opMat = 'sottrazione'
    p_num = int(primoNum)
    entraTesto.delete(0, 'end')

def btnMolti():
    primoNum = entraTesto.get()
    global p_num
    global opMat
    opMat = 'moltiplicazione'
    p_num = int(primoNum)
    entraTesto.delete(0, 'end')

def btnDivis():
    primoNum = entraTesto.get()
    global p_num
    global opMat
    opMat = 'divisione'
    p_num = int(primoNum)
    entraTesto.delete(0, 'end')

def btnUguale():
    secondoNum = entraTesto.get()
    entraTesto.delete(0, 'end')
    if opMat == 'somma':
        entraTesto.insert(0, p_num + int(secondoNum))
    elif opMat == 'sottrazione':
        entraTesto.insert(0, p_num - int(secondoNum))
    elif opMat == 'moltiplicazione':
        entraTesto.insert(0, p_num * int(secondoNum))
    elif opMat == 'divisione':
        entraTesto.insert(0, p_num / int(secondoNum))

btn_1 = tkinter.Button(root,
                       text="1",
                       padx=40,
                       pady=20,
                       command=lambda: clickBtn(1))
btn_2 = tkinter.Button(root,
                       text="2",
                       padx=40,
                       pady=20,
                       command=lambda: clickBtn(2))
btn_3 = tkinter.Button(root,
                       text="3",
                       padx=40,
                       pady=20,
                       command=lambda: clickBtn(3))
btn_4 = tkinter.Button(root,
                       text="4",
                       padx=40,
                       pady=20,
                       command=lambda: clickBtn(4))
btn_5 = tkinter.Button(root,
                       text="5",
                       padx=40,
                       pady=20,
                       command=lambda: clickBtn(5))
btn_6 = tkinter.Button(root,
                       text="6",
                       padx=40,
                       pady=20,
                       command=lambda: clickBtn(6))
btn_7 = tkinter.Button(root,
                       text="7",
                       padx=40,
                       pady=20,
                       command=lambda: clickBtn(7))
btn_8 = tkinter.Button(root,
                       text="8",
                       padx=40,
                       pady=20,
                       command=lambda: clickBtn(8))
btn_9 = tkinter.Button(root,
                       text="9",
                       padx=40,
                       pady=20,
                       command=lambda: clickBtn(9))
btn_0 = tkinter.Button(root,
                       text="0",
                       padx=40,
                       pady=20,
                       command=lambda: clickBtn(0))
btn_uguale = tkinter.Button(root,
                            text="=",
                            padx=39,
                            pady=20,
                            command=btnUguale)
btn_cancella = tkinter.Button(root,
                              text="Canc",
                              padx=28,
                              pady=20,
                              command=btnCanc)

btn_somma = tkinter.Button(root, text="+", padx=28, pady=20, command=btnSomma)
btn_sottr = tkinter.Button(root, text="-", padx=31, pady=20, command=btnSottr)
btn_molti = tkinter.Button(root, text="*", padx=30, pady=20, command=btnMolti)
btn_divis = tkinter.Button(root, text="/", padx=31, pady=20, command=btnDivis)

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=1)

btn_somma.grid(row=1, column=4)
btn_sottr.grid(row=2, column=4)
btn_molti.grid(row=3, column=4)
btn_divis.grid(row=4, column=4)

btn_uguale.grid(row=4, column=2)

btn_cancella.grid(row=4, column=0)

root.mainloop()
