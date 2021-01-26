import tkinter
import tkinter as tk
from tkinter import * 
import tkinter.messagebox as tkmsgbox
import tkinter.messagebox as msgbox

import csv
import time

reader = csv.reader(open("data.csv" , "r+"))
mydict = dict()
for line in reader :
    mydict[line[0]] = {"name":line[1],"Password":line[2],"Balance":line[3]}
print(mydict)
print(len(mydict))
k = 0
flag = 0
Pass_Entry = str()
Pass = str()
ID = str()
mony = str()
newPass = str()


def monyWant() :
    global Pass
    global mony
    print(str(mony))
    print(ID)
    print(Pass)
    
def sa7b() :
    global mony
    root.withdraw()
    mysa7b = tk.Toplevel(root)
    mysa7b.geometry("300x300+100+100")
    labelExample = tk.Label(mysa7b, text = "Enter the Mony you want :").pack()
    mony_Entry = tk.Entry(mysa7b,width = 15)
    mony_Entry.pack()
    mony = mony_Entry.get()
    print(mony)
    buttonExample = tk.Button(mysa7b, text = "Enter",command=monyWant).pack()
    buttonExample1 = tk.Button(mysa7b, text = "EXIT",command=mysa7b.destroy).pack()      

def MyBalance() :
    mybalance = tk.Toplevel(root)
    mybalance.geometry("300x300+100+100")
    labelExample = tk.Label(mybalance, text = "Your Balance is "+mydict[ID]["Balance"]+" LE").pack()
    buttonExample1 = tk.Button(mybalance, text = "EXIT",command=mybalance.destroy).pack()
    

def ChangePass() :
    global newPass
    myPass = tk.Toplevel(root)
    myPass.geometry("300x300+100+100")
    labelExample = tk.Label(myPass, text = "Enter You New Password : ").pack()
    newPass_Entry = tk.Entry(myPass,width = 15)
    newPass_Entry.pack()
    newPass = newPass_Entry.get()
    #print(mydict)
    buttonExample1 = tk.Button(myPass, text = "Exit",command=myPass.destroy).pack()

    
    
def createNewWindow():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("300x300+100+100")
    labelExample = tk.Label(newWindow, text = "Welcome "+mydict[ID]["name"]).pack()
    buttonExample = tk.Button(newWindow, text = "Cash Withdraw",command= sa7b).pack()
    buttonExample1 = tk.Button(newWindow, text = "Balance Inquiry",command = MyBalance).pack()
    buttonExample2 = tk.Button(newWindow, text = "Fawry Services",command = MyBalance).pack()
    buttonExample3 = tk.Button(newWindow, text = "Password Change",command = ChangePass).pack()
    
    buttonExample4 = tk.Button(newWindow, text = "EXIT",command=root.destroy).pack()
    
    root.withdraw()

def popup_ErrorAccount():
    print(tkmsgbox.askretrycancel("ERROR Account Number", "Please Try again!"))

def popup_ErrorPassword():
    print(tkmsgbox.askretrycancel("ERROR Password", "Please Try again!"))
    root.d
def popup_showinfo():
    print(tkmsgbox.showerror("Blocked System", "System is Blocked,You can return to Bank Branch"))    
def Exitfn():
    print("System Blocked")
    
def Enter1():
    global mydict
    global ID
    ID = User_Entry.get()
    if ID in mydict :
        print(ID)
        PassWin()
    else :
        print("Incorect data try again!")
        popup_ErrorAccount()
    
def Enter2 () :
    global flag
    global Pass
    global k
    Pass = Pass_Entry.get()
    while k < 2  :
        if Pass == mydict[ID]["Password"] :
            print("Welcome")
            createNewWindow()
            break
        else :
            k = k + 1
            flag = flag +1
            popup_ErrorPassword()
            
    if flag == 2 :
        popup_showinfo()
        root.after(1000,root.destroy)
        
        
'''def gameover():
   top = tk.Toplevel(root)
   label = tk.Label(top, text="Game over!")
   label.pack(padx=20, pady=20, expand=True)
   top.after(2000, top.destroy)  '''
            
            
def PassWin() :
        global Pass_Entry
        root.withdraw()
        newWindow = tk.Toplevel(root)
        newWindow.geometry("300x300+100+100")
        label = tk.Label(newWindow, text ="Please Enter Your Password!")
        label.grid(row = 0, column = 1)
        #Creat Entry password
        Pass_Entry = tk.Entry(newWindow,width = 15, show = '*')
        Pass_Entry.grid(row = 2, column = 1)
        user_password = tk.Label(newWindow, text = "Password").grid(row = 2, column = 0)

        #Creat Button
        Sign_Button = tk.Button(newWindow,text= 'Enter', command = Enter2)
        Sign_Button.grid(row = 3, column = 1)
             
#Creat Main Window
root = tkinter.Tk()
root.title("Welcome to ATM ALEXANDRIA BANK") 
root.geometry("400x300+100+100")

i=0
while i< 4:
	root.columnconfigure(i,minsize='10')
	i+=1
i=0
while i<4:
	root.rowconfigure(i,minsize='10')
	i+=1

label = tkinter.Label(root, text ="Please Enter Your Account Number!")
label.grid(row = 0, column = 1)
#Creat Entry ID
User_Entry = tkinter.Entry(root,width = 15)
User_Entry.grid(row = 1, column = 1)
user_Name = tkinter.Label(root, text = "Account Number").grid(row = 1, column = 0) 

#Creat Button
Sign_Button = tkinter.Button(root,text= 'Enter', command = Enter1)
Sign_Button.grid(row = 3, column = 1)

root.mainloop()