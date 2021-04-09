from random import *
import string
from tkinter import *

root=Tk()

root.title('Password Generator')

def enter():
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','"','#','$','%','&',"'",'(',')','*','+','-','.','/',':',';','<','=','>','?','@','[',']','^','_','{','|','}','~']
    length=int(entry.get())
    if length>3 and length<99:
        password_in_list = choices(characters,k=length)
        shuffle(password_in_list)
        password="" 
        for i in password_in_list:
            password += i
        label3=Label(root,text=password)
        label3.pack()
    elif length>=0 and length<4:
        label3=Label(root,text="A valid password cannot be length of 0 or 1 or 2 or 3")
        label3.pack()
    else:
        label3=Label(root,text="Invalid length")
        label3.pack()

label1=Label(root,text="Welcome to the Password Generator")
label1.pack()

label2=Label(root,text="Enter the length of the password(recommanded 8-16):")
label2.pack()

entry=Entry(root)
entry.pack()

button=Button(root,text="Enter",command=enter)
button.pack()

root.mainloop()