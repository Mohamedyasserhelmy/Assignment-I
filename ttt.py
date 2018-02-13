# Importing tkinter library
from tkinter import *
import tkinter.messagebox

click = True
tk = None
# defining main function of the game
def main():
    global tk
    tk = Tk()
    tk.title("X---O Game")
    def play(button):
        global click
        # alternating between X and O
        if button["text"] == " " and click:
            button["text"] = "X"
            click = False
        elif button["text"] == " ":
            button['text'] = "O"
            click = True
        # winning conditions for X
        if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
            button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
            # choosing between replay or quit
            answer = tkinter.messagebox.askquestion('X-----Player wins!', 'Do you want to play again')
            # return the main function for playing
            if answer == 'yes':
                main()
        # Winning conditions for O        
        elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
            button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
            button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
            button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
            button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
            button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
            button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
            button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
            answer = tkinter.messagebox.askquestion('O----wins', 'Do you want to play again')
            
            if answer == 'yes':
                main()
        

   
    #defining buttons Functions and sizes
    button1 = Button(tk, text=" ", font=('Times 26 bold'), height=3, width=3, command=lambda:play(button1))
    button1.grid(row=1, column=0)

    button2 = Button(tk, text=" ", font=('Times 26 bold'), height=3, width=3, command=lambda:play(button2))
    button2.grid(row=1, column=1)

    button3 = Button(tk, text=" ", font=('Times 26 bold'), height=3, width=3, command=lambda:play(button3))
    button3.grid(row=1, column=2)

    button4 = Button(tk, text=" ", font=('Times 26 bold'), height=3, width=3, command=lambda:play(button4))
    button4.grid(row=2, column=0)

    button5 = Button(tk, text=" ", font=("Times 26 bold"), height=3, width=3, command=lambda:play(button5))
    button5.grid(row=2, column=1)

    button6 = Button(tk, text=" ", font=('Times 26 bold'), height=3, width=3, command=lambda:play(button6))
    button6.grid(row=2, column=2)

    button7 = Button(tk, text=" ", font=('Times 26 bold'), height=3, width=3, command=lambda:play(button7))
    button7.grid(row=3, column=0)

    button8 = Button(tk, text=" ", font=('Times 26 bold'), height=3, width=3, command=lambda:play(button8))
    button8.grid(row=3, column=1)

    button9 = Button(tk, text=" ", font=('Times 26 bold'), height=3, width=3, command=lambda:play(button9))
    button9.grid(row=3, column=2)

    #break the main loop when we click x button
    tk.mainloop()

# returning the main loop

main()
