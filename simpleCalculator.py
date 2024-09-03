#simpleCalculator.py
#simple calculator using Tkinter
#todo: resize fontsize with windowsize

from Tkinter import *
from expression import *

#create root window
root = Tk()

#root window title and dimension
root.title("Calculator")
root.minsize(200, 200)

#create an Expression for user input
expression = Expression(StringVar())

#create 6 frames for root window
#frame 0 is for the label that displays user input/output
#frames 1-5 are for buttons
frames = []
for i in range(6):
	frames.append(Frame(root))
	frames[i].pack(expand=True, fill=BOTH, side=TOP)

#label for displaying user input/ouput
#todo: justify text to the right with padding
displayFrame = frames[0]
display = Label(displayFrame, textvariable=expression.expression, height=2, width=20, bg="white", relief=RAISED, anchor="e")
display.pack(expand=True, fill=BOTH, padx=2, pady=2)

#button info in the form of (text, frame index)
buttonsInfo =  [("7",1), ("8",1), ("9",1), ("+",1),
		("4",2), ("5",2), ("6",2), ("-",2),
		("1",3), ("2",3), ("3",3), ("*",3),
		("0",4), (".",4), ("=",4), ("/",4),
		("CLEAR", 5), ("DELETE", 5)]

#create buttons and add them to appropriate frames
buttons = []
for button in buttonsInfo:
	buttonText = button[0]
	buttonFrame = frames[button[1]]
	newButton = Button(buttonFrame,
		text=buttonText,
		width=1,#give buttons a width so they align properly in each frame
		command=lambda buttonText=buttonText: 				
			expression.append(buttonText))
	newButton.pack(expand=True, fill=BOTH, side=LEFT)
	buttons.append(newButton)

#The default button command was set to append when we created our 
#buttons. Here, we reassign special commands to the buttons with 
#special functions i.e. equals, clear, and delete.

#set = button command to calculate()
equalsButton = buttons[14]
equalsButton.configure(command=expression.calculate)

#set CLEAR button command to clear()
clearButton = buttons[16]
clearButton.configure(command=expression.clear)

#set DELETE button command to delete()
deleteButton = buttons[17]
deleteButton.configure(command=expression.delete)

#execute Tkinter
root.mainloop()
