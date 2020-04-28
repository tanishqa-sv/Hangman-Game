from tkinter import *
from string import ascii_uppercase

window=Tk()
window.title("Hangman Game")

#keyboard letter buttons :
n=0
for c in ascii_uppercase :
	Button(window, text=c,width=4,command= lambda letr=c : guess(letr), font=('Helvetica' ,'18')).grid(row=1+ n//9,column= n%9)
	n=n+1

window.mainloop()
