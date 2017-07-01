from tkinter import *

window = Tk()

window.geometry("500x500")

def yoAnsa():
    otherBools = CheckVar1.get() + CheckVar2.get() + CheckVar3.get() + CheckVar4.get()
 #   print(otherBools)
    if otherBools == 1:
        if CheckVar1.get() == True:
            print("We know he is a fruit.")
        elif CheckVar2.get() == True:
            print("He's runnin' around at the speed of sound")
        elif CheckVar3.get() == True:
            print("0.001 k/d ratio")
        elif CheckVar4.get() == True:
            print("Ye he dume?")
        else:
            print("Please, just choose one already! Gosh!")
    else:
        print("It's invalid you fool!")

label = Label(window, text="Choose one that you think is true!!!!!!!!")

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()      
CheckVar4 = IntVar()

C1 = Checkbutton(window, text = "Caleb is an orange", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(window, text = "Zack is Flash", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C3 = Checkbutton(window, text = "Derek is noob", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C4 = Checkbutton(window, text = "Brandune it dume", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)

button1 = Button(window, text="Submit Response", command = yoAnsa)


label.pack()

C1.pack()

C2.pack()

C3.pack()

C4.pack()

button1.pack()

window.mainloop()



 
 


