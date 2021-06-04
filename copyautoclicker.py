
import math
from tkinter.constants import BOTTOM, CENTER, LEFT, RIDGE
import pyautogui, keyboard, time, random
from tkinter import Button, Checkbutton, Entry, Image, Label, PhotoImage, StringVar, Text, Tk, IntVar, Widget, LEFT

root = Tk()
root.geometry("475x500")
root.maxsize(475,500)
root.minsize(475,500)
root.title("Bakraa Autoclicker")

photo = PhotoImage(file="bakraa_logo.png")
_imageLabel = Label(image=photo)
_imageLabel.grid(row=0,column=0)

def main():
    start_btn_widget.grid_forget()
    stop_btn_widget.grid(row=7,column=1)
    if smartcheckval.get() == 1:
            thenPos = getPos()
            print(thenPos)
            time.sleep(3)
            nowPos = getPos()
            print(nowPos)
            if nowPos != thenPos:
                print("stopping")
                stop_btn_widget.grid_forget()
                start_btn_widget.grid(row=7,column=1)
                return
            elif nowPos == thenPos:
                clicks(random.randint(math.ceil(int(intervalValfrom.get())/5), math.ceil(int(intervalValto.get())/5)))
    elif (i % 2)!= 0:
        stop_btn_widget.grid_forget()
        start_btn_widget.grid(row=7,column=1)
        
         
        return
    elif None:
        pass
    elif (i % 2) == 0:
        if smartcheckval.get() == 0:
            clicks(random.randint(math.ceil(int(intervalValfrom.get()))/2, math.ceil(int(intervalValto.get())/2 )))

    root.after((round(int(intervalValfrom.get()))*500) , main)

def repeat():
    pass

def clicks(secs):
    pyautogui.click(clicks=int(clickVal.get()),interval=secs)
    # root.after(int(intervalVal.get())*1000, click)

def getPos():
    time.sleep(1)
    return pyautogui.position()

i = 1
def increment(self):
    global i
    i+=1
    return i  

_clickval = Label(root, text="clicks")
_clickval.grid(row=1,column=0,padx=3,pady=3)

_interval = Label(root, text="Interval   From")
_interval.grid(row=2,column=0,padx=1,pady=3)


_intervalto = Label(root, text="to")
_intervalto.grid(row=2,column=2)

clickVal = StringVar()
intervalValfrom = StringVar()
intervalValto = StringVar()
smartcheckval = IntVar()

clickentry = Entry(root, textvariable=clickVal)
clickentry.grid(row=1 ,column=1)

intervalentryfrm = Entry(root, textvariable=intervalValfrom)
intervalentryfrm.grid(row=2, column=1,padx=3)

intervalentryto = Entry(root, textvariable=intervalValto)
intervalentryto.grid(row=2,column=3,padx=3)

smartcheckbtn = Checkbutton(root, text="Smart Disable", variable=smartcheckval)
smartcheckbtn.grid(row=4,column=1)


start_btn_widget = Button(root, text="Start", command=main, border=0, bg="#dadada", relief=RIDGE, padx=80,pady=40)
start_btn_widget.grid(row=7,column=1)
start_btn_widget.bind('<Button-1>', increment)
stop_btn_widget = Button(root, text="Stop", command=main, border=0, bg="#dadada", relief=RIDGE, padx=80,pady=40)
stop_btn_widget.bind('<Button-1>', increment)

# keyboard.wait(f"{lst[0]}+{lst[1]}")

root.mainloop()
