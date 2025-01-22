"""
Name : Vaishakh V
Date: 19/01/2024
Description : Tic-Tac-Toe Game 
Sample input : Play the game
Sample out :   X has won or O has won
"""


from tkinter import *
from tkinter import messagebox

m=Tk()

# Creating the title of the game
m.title("Tic-Tac-Toe") 

# Creating the buttons from b1-b9 with font, height, width, background color
b1=Button(m,text="",font=('helvetica',20),height=3,width=6,bg="Antiquewhite", command=lambda: click(b1))
b1.grid(row=0, column=0)

b2=Button(m,text="",font=('helvetica',20),height=3,width=6,bg="Antiquewhite", command=lambda: click(b2))
b2.grid(row=0, column=1)

b3=Button(m,text="",font=('helvetica',20),height=3,width=6,bg="Antiquewhite", command=lambda: click(b3))
b3.grid(row=0, column=2)

b4=Button(m,text="",font=('helvetica',20),height=3,width=6,bg="Antiquewhite", command=lambda: click(b4))
b4.grid(row=1, column=0)

b5=Button(m,text="",font=('helvetica',20),height=3,width=6,bg="Antiquewhite", command=lambda: click(b5))
b5.grid(row=1, column=1)

b6=Button(m,text="",font=('helvetica',20),height=3,width=6,bg="Antiquewhite", command=lambda: click(b6))
b6.grid(row=1, column=2)

b7=Button(m,text="",font=('helvetica',20),height=3,width=6,bg="Antiquewhite", command=lambda: click(b7))
b7.grid(row=2, column=0)

b8=Button(m,text="",font=('helvetica',20),height=3,width=6,bg="Antiquewhite", command=lambda: click(b8))
b8.grid(row=2, column=1)

b9=Button(m,text="",font=('helvetica',20),height=3,width=6,bg="Antiquewhite", command=lambda: click(b9))
b9.grid(row=2, column=2)

clicked = True
count = 0

# Checking if the b1 buttion is clicked or not
def click(b1):

	global clicked, count
	if b1["text"]=="" and clicked==True:
		b1["text"]="X"
		clicked=False
		count+=1
		check_game_status()
      
	if b1["text"]=="" and clicked==False:
		b1["text"]="O"
		clicked=True
		count+=1
		check_game_status()

# Checking if the b2 buttion is clicked or not
def click(b2):

	global clicked, count
	if b2["text"]=="" and clicked==True:
		b2["text"]="X"
		clicked=False
		count+=1
		check_game_status()

	if b2["text"]=="" and clicked==False:
		b2["text"]="O"
		clicked=True
		count+=1
		check_game_status()

# Checking if the b3 buttion is clicked or not
def click(b3):

	global clicked, count
	if b3["text"]=="" and clicked==True:
		b3["text"]="X"
		clicked=False
		count+=1
		check_game_status()

	if b3["text"]=="" and clicked==False:
		b3["text"]="O"
		clicked=True
		count+=1
		check_game_status()

# Checking if the b4 buttion is clicked or not
def click(b4):

	global clicked, count
	if b4["text"]=="" and clicked==True:
		b4["text"]="X"
		clicked=False
		count+=1
		check_game_status()

	if b4["text"]=="" and clicked==False:
		b4["text"]="O"
		clicked=True
		count+=1
		check_game_status()

# Checking if the b5 buttion is clicked or not
def click(b5):

	global clicked, count
	if b5["text"]=="" and clicked==True:
		b5["text"]="X"
		clicked=False
		count+=1
		check_game_status()

	if b5["text"]=="" and clicked==False:
		b5["text"]="O"
		clicked=True
		count+=1
		check_game_status()

# Checking if the b6 buttion is clicked or not
def click(b6):

	global clicked, count
	if b6["text"]=="" and clicked==True:
		b6["text"]="X"
		clicked=False
		count+=1
		check_game_status()

	if b6["text"]=="" and clicked==False:
		b6["text"]="O"
		clicked=True
		count+=1
		check_game_status()

# Checking if the b7 buttion is clicked or not
def click(b7):

	global clicked, count
	if b7["text"]=="" and clicked==True:
		b7["text"]="X"
		clicked=False
		count+=1
		check_game_status()

	if b7["text"]=="" and clicked==False:
		b7["text"]="O"
		clicked=True
		count+=1
		check_game_status()

# Checking if the b8 buttion is clicked or not
def click(b8):

	global clicked, count
	if b8["text"]=="" and clicked==True:
		b8["text"]="X"
		clicked=False
		count+=1
		check_game_status()

	if b8["text"]=="" and clicked==False:
		b8["text"]="O"
		clicked=True
		count+=1
		check_game_status()

# Checking if the b9 buttion is clicked or not
def click(b9):

	global clicked, count
	if b9["text"]=="" and clicked==True:
		b9["text"]="X"
		clicked=False
		count+=1
		check_game_status()

	if b9["text"]=="" and clicked==False:
		b9["text"]="O"
		clicked=True
		count+=1
		check_game_status()

# Declaring a win function
def win():

	# Checking if b1, b2 ,b3 is X and printing X has won
	if b1["text"]== "X" and b2["text"]== "X" and b3["text"]== "X":
		b1.config(bg = "red")
		b2.config(bg = "red")
		b3.config(bg = "red")
		messagebox.showinfo("Winner", "X has won")
		disablebutton()
	
	# Checking if b4, b5 ,b6 is X and printing X has won
	if b4["text"]== "X" and b5["text"]== "X" and b6["text"]== "X":
		b4.config(bg = "red")
		b5.config(bg = "red")
		b6.config(bg = "red")
		messagebox.showinfo("Winner", "X has won")
		disablebutton()

	# Checking if b7, b8 ,b9 is X and printing X has won
	if b7["text"]== "X" and b8["text"]== "X" and b9["text"]== "X":
		b7.config(bg = "red")
		b8.config(bg = "red")
		b9.config(bg = "red")
		messagebox.showinfo("Winner", "X has won")
		disablebutton()

	# Checking if b1, b4 ,b7 is X and printing X has won
	if b1["text"]== "X" and b4["text"]== "X" and b7["text"]== "X":
		b1.config(bg = "red")
		b4.config(bg = "red")
		b7.config(bg = "red")
		messagebox.showinfo("Winner", "X has won")
		disablebutton()

	# Checking if b2, b5 ,b8 is X and printing X has won
	if b2["text"]== "X" and b5["text"]== "X" and b8["text"]== "X":
		b2.config(bg = "red")
		b5.config(bg = "red")
		b8.config(bg = "red")
		messagebox.showinfo("Winner", "X has won")
		disablebutton()
	
	# Checking if b3, b6 ,b9 is X and printing X has won
	if b3["text"]== "X" and b6["text"]== "X" and b9["text"]== "X":
		b3.config(bg = "red")
		b6.config(bg = "red")
		b9.config(bg = "red")
		messagebox.showinfo("Winner", "X has won")
		disablebutton()

	# Checking if b1, b5 ,b9 is X and printing X has won
	if b1["text"]== "X" and b5["text"]== "X" and b9["text"]== "X":
		b1.config(bg = "red")
		b5.config(bg = "red")
		b9.config(bg = "red")
		messagebox.showinfo("Winner", "X has won")
		disablebutton()

	# Checking if b3, b5 ,b7 is X and printing X has won
	if b3["text"]== "X" and b5["text"]== "X" and b7["text"]== "X":
		b3.config(bg = "red")
		b5.config(bg = "red")
		b7.config(bg = "red")
		messagebox.showinfo("Winner", "X has won")
		disablebutton()



	# Checking if b1, b2 ,b3 is O and printing O has won
	if b1["text"]== "O" and b2["text"]== "O" and b3["text"]== "O":
		b1.config(bg = "red")
		b2.config(bg = "red")
		b3.config(bg = "red")
		messagebox.showinfo("Winner", "O has won")
		disablebutton()

	# Checking if b4, b5 ,b6 is O and printing O has won
	if b4["text"]== "O" and b5["text"]== "O" and b6["text"]== "O":
		b4.config(bg = "red")
		b5.config(bg = "red")
		b6.config(bg = "red")
		messagebox.showinfo("Winner", "O has won")
		disablebutton()

	# Checking if b7, b8 ,b9 is O and printing O has won
	if b7["text"]== "O" and b8["text"]== "O" and b9["text"]== "O":
		b7.config(bg = "red")
		b8.config(bg = "red")
		b9.config(bg = "red")
		messagebox.showinfo("Winner", "O has won")
		disablebutton()

	# Checking if b1, b4 ,b7 is O and printing O has won
	if b1["text"]== "O" and b4["text"]== "O" and b7["text"]== "O":
		b1.config(bg = "red")
		b4.config(bg = "red")
		b7.config(bg = "red")
		messagebox.showinfo("Winner", "O has won")
		disablebutton()

	# Checking if b2, b5 ,b8 is O and printing O has won
	if b2["text"]== "O" and b5["text"]== "O" and b8["text"]== "O":
		b2.config(bg = "red")
		b5.config(bg = "red")
		b8.config(bg = "red")
		messagebox.showinfo("Winner", "O has won")
		disablebutton()

	# Checking if b3 b6 ,b9 is O and printing O has won
	if b3["text"]== "O" and b6["text"]== "O" and b9["text"]== "O":
		b3.config(bg = "red")
		b6.config(bg = "red")
		b9.config(bg = "red")
		messagebox.showinfo("Winner", "O has won")
		disablebutton()

	# Checking if b1, b5 ,b9 is O and printing O has won
	if b1["text"]== "O" and b5["text"]== "O" and b9["text"]== "O":
		b1.config(bg = "red")
		b5.config(bg = "red")
		b9.config(bg = "red")
		messagebox.showinfo("Winner", "O has won")
		disablebutton()

	# Checking if b3, b5 ,b7 is O and printing O has won
	if b3["text"]== "O" and b5["text"]== "O" and b7["text"]== "O":
		b3.config(bg = "red")
		b5.config(bg = "red")
		b7.config(bg = "red")
		messagebox.showinfo("Winner", "O has won")
		disablebutton()

# Checking the status of the game being played whether its win or draw and print the message
def check_game_status():
	if win():
		return

	elif count == 9:
		messagebox.showinfo("Tic-Tac-Toe", "DRAW")
		m.destroy()

# Disable all the buttions once the game is over
def disablebutton():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)

m.mainloop()
