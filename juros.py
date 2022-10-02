import math


captaporte = []
for word in input('Digite o Capital e Aporte : ').split():
    s = word.split(" ")
    captaporte.extend(s)

jurostempo = []
for word in input('Digite os juros em % e o tempo: ').split():
    s = word.split(" ")
    jurostempo.extend(s)



capital = int(captaporte[0])
aporte = int(captaporte[1])

juros = float(jurostempo[0]) / 100
tempo = int(jurostempo[1])



if aporte != 0:
    montanteaporte = (aporte * ((1+ juros)**tempo - 1)) / juros
    valorfinal = (capital * (1 + juros)**tempo) + montanteaporte
    print(math.floor(valorfinal))
else:
    print('oi')



from tkinter import *

def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(gui, text= str(math.floor(valorfinal)))
    #this creates a new label to the GUI
    label.pack() 

gui = Tk()

button = Button(gui, text="Calcular", command=printSomething) 
button.pack()
gui.geometry('400x250')
gui.mainloop()



