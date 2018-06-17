from tkinter import *
from tkinter import messagebox as tkMessageBox

from Helper.BoardSave import BoardSave
from Helper.GameController import GameController
from Helper.Game import Game
from Helper.GUI_TK import GUI_TK
from Helper.Judge import Judge

from Helper.AI.EvaluateTranscendental import EvaluateTranscendental
from Helper.AI.ValuablePointLinear import ValuablePointLinear

from Helper.Player.PlayerAI_stupid_attacking import PlayerAI_stupid_attacking
from Helper.Player.PlayerHuman import PlayerHuman

# main window

root = Tk()
# set the size of main window
root.geometry('700x700')
# create a canvas to draw board and chessman,and set the background of the canvas white
cv = Canvas(root, bg='white', width=600, height=600)
cv.pack()


def callback_click(x, y):
	if game.now_black:
		player1.setTouchCoordinate(x, y)


gui = GUI_TK(cv, 10, 10, 590, 590, callback_click=callback_click, theta=0.4,chess_radii=15)
judge = Judge(15, 15, win_size=5)
boardSave = BoardSave(15, 15)
game = Game(boardSave, gui, judge, callback_win=lambda x, y, winCondition, isBlack: tkMessageBox.showinfo(
	'win', 'x=%r,y=%r,winCondition=%r,isBlack=%r' % (x, y, winCondition, isBlack)))

player1 = PlayerHuman()

valuablePoint = ValuablePointLinear()
evaluate = EvaluateTranscendental(15, 15)
player2 = PlayerAI_stupid_attacking(valuablePoint, evaluate, gui)

gameController = GameController(player1, player2, game)
Button(root, text='back', command=gameController.back).pack()
Button(root, text='clear', command=gameController.clear).pack()

gameController.start()


def delete():
	gameController.stop()
	root.destroy()


root.protocol('WM_DELETE_WINDOW', delete)
root.mainloop()
