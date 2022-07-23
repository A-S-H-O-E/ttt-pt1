from cgitb import text
from tkinter import *
import tkinter.messagebox 
root = Tk()
root.title('Tic Tac Toe')
playerA = StringVar()
playerB = StringVar()
player1 = Entry(root,textvariable = playerA)
player2 = Entry(root,textvariable = playerB)
player1.grid(row=1,column=1)
player2.grid(row=2,column=1)
bclck = True
flag = 0
def descideturn(b):
    global bclck,flag
    if(bclck == True and b['text'] == ' '):
        b['text'] = 'O'
        bclck = False
        flag = flag + 1
    if(bclck == False and b['text'] == ' '):
        b['text'] = 'X'
        bclck = True
        flag = flag + 1
        
label1 = Label(root,text = 'Player 1',font = 'Times 20 bold',bg = 'white',fg = 'black', height = 1, width = 8)
label1.grid(row=1,column=0)
label2 = Label(root,text = 'Player 2',font = 'Times 20 bold',bg = 'white',fg = 'black', height = 1, width = 8 )
label2.grid(row=2,column=0)

button1 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button1))
button1.grid(row=3,column = 0)

button2 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button2))
button2.grid(row=3,column = 1)

button3 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button3))
button3.grid(row=3,column = 2)

button4 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button4))
button4.grid(row=4,column = 0)

button5 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button5))
button5.grid(row=4,column = 1)

button6 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button6))
button6.grid(row=4,column = 2)

button7 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button7))
button7.grid(row=5,column = 0)

button8 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button8))
button8.grid(row=5,column = 1)

button9 = Button(root,text = ' ',font = 'Time 20 bold',bg = 'grey',fg = 'white', height = 4, width = 8, command = lambda: descideturn(button9))
button9.grid(row=5,column = 2)
root.mainloop()