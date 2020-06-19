from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("TIC-TAC-TOE")
#root.geometry("300x300")

root.configure(background = "light green")

#the main frame
Mainframe = LabelFrame(root)
Mainframe.pack()
#the game frame
gameframe = LabelFrame(Mainframe,padx = 10,pady = 10,bg = "blue")
gameframe.pack(side = LEFT)
#SCORE_fRAME
score_frame = LabelFrame(Mainframe,padx = 10,pady = 10,bg = "yellow")
score_frame.pack(side = RIGHT)
click = True        #for X
points_count_x = 0
points_count_o = 0
#creating functions
def click_buttons(button):
	global click
	if button["text"]=="" and click == True:
		button["text"] = "X"
		button.configure(bg = "white",fg = "red")
		click = False
		check_win()
	elif button["text"]=="" and click == False:
		button["text"] = "O"
		button.configure(bg = "white",fg = "blue")
		click = True
		check_win()

def reset():
	global click
	button1["text"] = ""
	button2["text"] = ""
	button3["text"] = ""
	button4["text"] = ""
	button5["text"] = ""
	button6["text"] = ""
	button7["text"] = ""
	button8["text"] = ""
	button9["text"] = ""
	#no ned for global arr as lists are mutable
	for ele in arr:
		ele.configure(bg = "white")
	click = True     #X will be first one as default


def check_win():
	global points_count_x,points_count_o
	if (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
		Player1 = e1.get()
		#to colour the three butoons 
		button1.configure(bg = "light green")
		button2.configure(bg = "light green")
		button3.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player1) + "  won!")
		points_count_x +=1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
		Player1 = e1.get()
		button4.configure(bg = "light green")
		button5.configure(bg = "light green")
		button6.configure(bg = "light green")
		messagebox.showinfo("WINNER","Congratulations! " + str(Player1) + "  won!")
		points_count_x +=1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
		Player1 = e1.get()
		button7.configure(bg = "light green")
		button8.configure(bg = "light green")
		button9.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player1) + "  won!")
		points_count_x +=1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
		Player1 = e1.get()
		button1.configure(bg = "light green")
		button4.configure(bg = "light green")
		button7.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player1) + "  won!")
		points_count_x +=1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
		Player1 = e1.get()
		button2.configure(bg = "light green")
		button5.configure(bg = "light green")
		button8.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player1) + "  won!")
		points_count_x +=1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
		Player1 = e1.get()

		button3.configure(bg = "light green")
		button6.configure(bg = "light green")
		button9.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player1) + "  won!")
		points_count_x +=1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
		Player1 = e1.get()
		button1.configure(bg = "light green")
		button5.configure(bg = "light green")
		button9.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player1) + "  won!")
		points_count_x +=1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
		Player1 = e1.get()
		button3.configure(bg = "light green")
		button5.configure(bg = "light green")
		button7.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player1) + "  won!")
		points_count_x +=1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
		Player2 = e2.get()
		button1.configure(bg = "light green")
		button2.configure(bg = "light green")
		button3.configure(bg = "light green")
		messagebox.showinfo("WINNER","Congratulations! " + str(Player2) + "  won!")
		points_count_o += 1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
		Player2 = e2.get()

		button4.configure(bg = "light green")
		button5.configure(bg = "light green")
		button6.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player2) + "  won!")
		points_count_o += 1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
		Player2 = e2.get()
		button7.configure(bg = "light green")
		button8.configure(bg = "light green")
		button9.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player2) + "  won!")
		points_count_o += 1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
		Player2 = e2.get()
		button1.configure(bg = "light green")
		button4.configure(bg = "light green")
		button7.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player2) + "  won!")
		points_count_o += 1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
		Player2 = e2.get()
		button2.configure(bg = "light green")
		button5.configure(bg = "light green")
		button8.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player2) + "  won!")
		points_count_o += 1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
		Player2 = e2.get()
		button3.configure(bg = "light green")
		button6.configure(bg = "light green")
		button9.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player2) + "  won!")
		points_count_o += 1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
		Player2 = e2.get()
		button1.configure(bg = "light green")
		button5.configure(bg = "light green")
		button9.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player2) + "  won!")
		points_count_o += 1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
		Player2 = e2.get()
		button3.configure(bg = "light green")
		button5.configure(bg = "light green")
		button7.configure(bg = "light green")

		messagebox.showinfo("WINNER","Congratulations! " + str(Player2) + "  won!")
		points_count_o += 1
		score_update(points_count_x,points_count_o)
		reset()

	elif (button1["text"]!="" and button2["text"]!="" and button3["text"]!="" and button4["text"]!="" and button5["text"]!="" and button6["text"]!="" and button7["text"]!="" and button8["text"]!="" and button9["text"]!=""):
		messagebox.showinfo("DRAW","It's a DRAW !!")
		reset()

#creating buttons
button1 = Button(gameframe,text = "",height = 3,width = 6,bg = "white",command = lambda: click_buttons(button1),font = ("arial",10,"bold"))
button1.grid(row = 0,column = 0)
button2 = Button(gameframe,text = "",height = 3,width = 6,bg = "white",command = lambda: click_buttons(button2),font = ("arial",10,"bold"))
button2.grid(row = 0,column = 1)
button3 = Button(gameframe,text = "",height = 3,width = 6,bg = "white",command = lambda: click_buttons(button3),font = ("arial",10,"bold"))
button3.grid(row = 0,column = 2)
button4 = Button(gameframe,text = "",height = 3,width = 6,bg = "white",command = lambda: click_buttons(button4),font = ("arial",10,"bold"))
button4.grid(row = 1,column = 0)
button5 = Button(gameframe,text = "",height = 3,width = 6,bg = "white",command = lambda: click_buttons(button5),font = ("arial",10,"bold"))
button5.grid(row = 1,column = 1)
button6 = Button(gameframe,text = "",height = 3,width = 6,bg = "white",command = lambda: click_buttons(button6),font = ("arial",10,"bold"))
button6.grid(row = 1,column = 2)
button7 = Button(gameframe,text = "",height = 3,width = 6,bg = "white",command = lambda: click_buttons(button7),font = ("arial",10,"bold"))
button7.grid(row = 2,column = 0)
button8 = Button(gameframe,text = "",height = 3,width = 6,bg = "white",command = lambda: click_buttons(button8),font = ("arial",10,"bold"))
button8.grid(row = 2,column = 1)
button9 = Button(gameframe,text = "",height = 3,width = 6,bg = "white",command = lambda: click_buttons(button9),font = ("arial",10,"bold"))
button9.grid(row = 2,column = 2)
arr = [button1,button2,button3,button4,button5,button6,button7,button8,button9]

#creating functions button
reset_button = Button(score_frame,text = "RESET",height = 3,width = 10,bg = "cyan",command = reset,font = ("system",10,"bold"))
reset_button.grid(row = 3,column = 0)

#SCOREBOARD
#creating labels
label1 = Label(score_frame,text = "Player X",font = ("arial",20,"bold"),bg= "black",fg = "red")
label1.grid(row = 0,column = 0,sticky = W+E,pady = 5,padx = 5)
label2 = Label(score_frame,text = "Player O",font = ("arial",20,"bold"),bg = "black",fg = "red")
label2.grid(row = 1,column = 0,stick = W+E,pady = 5,padx = 7)
#creating entry widgets for inputting names
e1 = Entry(score_frame,width = 15,borderwidth = 5,relief = RIDGE)
e1.grid(row = 0,column = 1)
e2 = Entry(score_frame,width = 15,borderwidth = 5,relief = RIDGE)
e2.grid(row = 1,column = 1)
#scoreboard's default names
e1.insert(0,"X")
e2.insert(0,"Y")

#pass 0,0 when starting a new game
def new_game():
	global points_count_x,points_count_o
	points_count_x,points_count_o = 0,0
	#warning if starting a new game
	response = messagebox.askokcancel("NEW GAME NOTIFIER","Are you sure you wish to start a new game ? \nBoth players will lose their progress!")
	if response:
		if response==1:
			Label(score_frame,text = str(points_count_x),font = ("arial",15,"bold"),fg = "brown",bg = "yellow").grid(row = 0,column = 2,sticky = E,padx = 5)
			Label(score_frame,text = str(points_count_o),font = ("arial",15,"bold"),fg = "brown",bg = "yellow").grid(row = 1,column = 2,sticky = E,padx = 5)
	return


#updating scores
def score_update(points_count_x,points_count_o):
	label3 = Label(score_frame,text = str(points_count_x),font = ("arial",15,"bold"),fg = "brown",bg = "yellow")
	label3.grid(row = 0,column = 2,sticky = E,padx = 5)
	label4 = Label(score_frame,text = str(points_count_o),font = ("arial",15,"bold"),fg = "brown",bg = "yellow")
	label4.grid(row = 1,column = 2,sticky = E,padx = 5)
	return

#Scores set initially to zero
label3 = Label(score_frame,text = str(points_count_x),font = ("arial",15,"bold"),fg = "brown",bg = "yellow")
label3.grid(row = 0,column = 2,sticky = E,padx = 5)
label4 = Label(score_frame,text = str(points_count_o),font = ("arial",15,"bold"),fg = "brown",bg = "yellow")
label4.grid(row = 1,column = 2,sticky = E,padx = 5)
#create a new game button  ---->

new_button = Button(score_frame,text = "NEW GAME",height = 3,width = 10,bg = "cyan",command = new_game,font = ("system",10,"bold"))
new_button.grid(row = 3,column = 1)


root.mainloop()

