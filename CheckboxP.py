 
from tkinter import *

window = Tk()

window.geometry("500x500")

# this function determines whether or not the inputs are valid or not and prints a
#response accordingly
# the otherBools variable checks to see if more than one box is checked by adding the
#boolian variables together (True = 1 False = 0
def yoAnsa():
    otherBools = CheckVar1.get() + CheckVar2.get() + CheckVar3.get() + CheckVar4.get()
# the otherBools variable checks to see if more than one box is checked by adding the
#boolian variables together (True = 1 False = 0
    if otherBools == 1:
# take the number from the otherBools variable and sees if it is true and if it is it
# prints the corresponding statment
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

#checks to see if the boxes are checked and sets it to a variable
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()      
CheckVar4 = IntVar()

#checkbutton widgets that show up in the tab with the diffrent labels on them
C1 = Checkbutton(window, text = "Caleb is an orange", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(window, text = "Zack is the Flash", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C3 = Checkbutton(window, text = "Derek is a noob", variable = CheckVar3, \
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



 
 


