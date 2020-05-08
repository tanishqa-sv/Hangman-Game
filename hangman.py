from tkinter import *
from string import ascii_uppercase

window=Tk()
window.title("Hangman Game")

#an array of images to be used with indices :
photo=[PhotoImage(file=r"images\0.png"), PhotoImage(file=r"images\1.png"),  PhotoImage(file=r"images\2.png"),  PhotoImage(file=r"images\3.png"),  PhotoImage(file=r"images\4.png"),  PhotoImage(file=r"images\5.png"),  PhotoImage(file=r"images\6.png")] 

imgLabel=Label(window)                                                                        #a label for images
imgLabel.grid(row=0,column=0,columnspan=3,pady=40)
imgLabel.config(image=photo[0])				#assigning initial image to label 

#keyboard letter buttons :
n=0
for c in ascii_uppercase :
	Button(window, text=c,width=4,command= lambda letr=c : guess(letr), font=('Helvetica' ,'18')).grid(row=1+ n//9,column= n%9)
	n=n+1

window.mainloop()
