from tkinter import *
from tkinter import messagebox as tkMessageBox

from BoardSave import BoardSave
from Helper.Game import Game
from Helper.GUI_TK import GUI_TK
from Helper.Judge import Judge

# main window
root = Tk()
# set the size of main window
root.geometry('500x500')
# create a canvas to draw board and chessman,and set the background of the canvas white
cv = Canvas(root, bg='white', width=400, height=400)
cv.pack()

helper = GUI_TK(cv, 10, 10, 390, 390, lambda x, y: game.move(x, y), theta=0.4)
judge = Judge(15, 15, win_size=5)
boardSave = BoardSave(15, 15)
game = Game(boardSave, helper, judge, callback_win=lambda x, y, winCondition, isBlack: tkMessageBox.showinfo(
	'win', 'x=%r,y=%r,winCondition=%r,isBlack=%r' % (x, y, winCondition, isBlack)))
Button(root, text='back', command=game.back).pack()
Button(root, text='clear', command=game.clear).pack()

root.mainloop()
