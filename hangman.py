from tkinter import *
import string
from string import ascii_uppercase
import random
from tkinter import messagebox

window=Tk()
window.title("Hangman Game")

#an array of images to be used with indices :
photo=[PhotoImage(file=r"images\0.png"), PhotoImage(file=r"images\1.png"),  PhotoImage(file=r"images\2.png"),  PhotoImage(file=r"images\3.png"),  PhotoImage(file=r"images\4.png"),  PhotoImage(file=r"images\5.png"),  PhotoImage(file=r"images\6.png")] 
word_list=[ "INDIA", "AMERICA", "CHINA", "PAKISTAN", "SRILANKA", "MYANMAR", "NEPAL", "RUSSIA", "BHUTAN","BANGLADESH"]

def guess(letter) :
	global no_of_guesses
	if not display_word.get()==the_word_w_spaces and no_of_guesses<6:
		txt=list(the_word_w_spaces)
		guessed=list(display_word.get())
		if (the_word.count(letter)>0):
			for i in range (len(txt)):
				if txt[i]==letter:
					guessed[i]=letter
					display_word.set("".join(guessed))
			txtLabel.config(text=display_word.get())
			if display_word.get()==the_word_w_spaces:
				messagebox.showinfo("Hangman", "You guessed it!")
		else:
			no_of_guesses+=1
			imgLabel.config(image=photo[no_of_guesses])
			if no_of_guesses==6:
				messagebox.showwarning("Hangman","Game Over")


imgLabel=Label(window)					#a label for images
imgLabel.grid(row=0,column=0,columnspan=3,pady=40)			

imgLabel.config(image=photo[0])				#assigning initial image to label 

display_word=StringVar()
txtLabel=Label(window, text=display_word.get(), font=('Helvetica' ,'18'))	#label displays string variable
txtLabel.grid(column=3,columnspan=6,row=0)

the_word= random.choice(word_list)
display_word.set(" ".join("_"*len(the_word)))		#initially set display word to blanks
txtLabel.config(text=display_word.get())
the_word_w_spaces= " ".join(the_word)
no_of_guesses=0

#keyboard letter buttons :
n=0
for c in ascii_uppercase :
	Button(window, text=c,width=4,command= lambda letr=c : guess(letr), font=('Helvetica' ,'18')).grid(row=1+ n//9,column= n%9)
	n=n+1

window.mainloop()

