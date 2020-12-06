##################################################
###   Author      : Ahmed Gama                ####
###   Description : Toggle Function GUI       ####
###                                           ####
###   Date        : 6 Dec 2020                ####
###   Version     : v1                        ####
##################################################

from tkinter import *  
flag = 0
def TogFn() :
    global flag
    if flag == 0 :
        print(0)
        flag = 1
    else :
        print(1)
        flag = 0
  
# create a tkinter window 
root = Tk()   
root.title("Toggle Function GUI")            
  
# Open window having dimension 100x100 
root.geometry('400x100')  
  
# Create a Button 
btn = Button(root, text = 'Toggle', bd = '5', command = TogFn)  
btn1 = Button(root, text = 'EXIT', bd = '5', command = root.destroy)  
# Set the position of button on the top of window.    
btn.pack(side = 'top')     
btn1.pack(side = 'top') 
root.mainloop()