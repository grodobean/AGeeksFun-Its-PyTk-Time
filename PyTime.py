import sys
import time
import os
import subprocess
import shutil
import webbrowser
from tkinter import *
#decleration of the GUI settings
master = Tk()
master.title("All Use App")
#decleration and definition of all functions to be used in buttons
def openUserWeb():
    Label(master,text="The website entered is %s .\n Would you like to go to that website?\nIf so type in 'Yes'"%(web_loca.get())).grid(row=11,column=4)
    if (user_in.get() == "Yes"):
        webbrowser.open(""+(web_loca.get()))
    else:
        master.quit()
def endApp():
    L2 = Label(master,text="The app ended at "+time.ctime()+" .\n")
    L2.grid(row=6,column=0)
    master.quit()
#the function that prints the first and last name of the user
def LabPrintName():
   L1=Label(master,text="Hello, %s %s , this is my first tk application! \n"%(VarO.get(),VarT.get()))
   L1.grid(row=5,column=0)
def write_dir():
    Label(master,text="Enter the file location, or where you want it to be saved.\n").grid(row=10,column=4)
    Label(master,text="Enter the file name and extensions.\n").grid(row=9,column=4)
def write_file():
    Label(master,text="The path is %s.\nAnd the name is %s.\n" %(file_loca.get(),name_beta.get())).grid(row=10,column=1)
    file_mix = file_loca.get()+name_beta.get()
    if os.path.exists("%s"%file_mix):
        Label(master,text="It exists.\n").grid(row=8,column=1)
    else:
        open(file_mix,mode="w+")
        if sys.platform == "win32":
            os.startfile(file_mix)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subbprocess.call([opener,file_mix])
#Labels used to show what an entry box is for
Label(master,text="First Name").grid(row=0)
Label(master,text="Last Name").grid(row=1)
Label(master,text="Directory").grid(row=2)
Label(master,text="File Name").grid(row=3)
Label(master,text="Website Location").grid(row=4)
Label(master,text="User Input Box").grid(row=5)
#Initializes The Entry Boxes
VarO = Entry(master)
VarT = Entry(master)
file_loca = Entry(master)
name_beta = Entry(master)
web_loca = Entry(master)
user_in = Entry(master)
#Pushes the location of the boxes onto the screen
VarO.grid(row=0,column=1)
VarT.grid(row=1,column=1)
file_loca.grid(row=2,column=1)
name_beta.grid(row=3,column=1)
web_loca.grid(row=4,column=1)
user_in.grid(row=5,column=1)
#Buttons that call functions
Button(master,text="Quit",command=endApp).grid(row=4,column=8,sticky=W,pady=4)
Button(master,text="Show",command=LabPrintName).grid(row=5,column=8,sticky=W,pady=4)
Button(master,text="Write Instructions",command=write_dir).grid(row=6,column=8,sticky=W,pady=4)
Button(master,text="Write File",command=write_file).grid(row=7,column=8,sticky=W,pady=4)
Button(master,text="Web Opener",command=openUserWeb).grid(row=8,column=8,sticky=W,pady=4)
#Input Pointers
First_Name = VarO.get()
Last_Name = VarT.get()
file_location = file_loca.get()
name_file = name_beta.get()
web_location = web_loca.get()
mainloop()

