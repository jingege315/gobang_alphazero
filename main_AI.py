from tkinter import *
from tkinter import messagebox as tkMessageBox

from Helper.BoardSave import BoardSave
from Helper.GameController import GameController
from Helper.Game import Game
from Helper.GUI_TK import GUI_TK
from Helper.Judge import Judge

from Helper.AI.EvaluateNormal2 import EvaluateNormal2
from Helper.AI.EvaluateNormal import EvaluateNormal
from Helper.AI.ValuablePointLinear import ValuablePointLinear
from Helper.AI.SearchMaxmin import SearchMaxmin
from Helper.Player.PlayerAI_search import PlayerAI_search

from Helper.Player.PlayerAI_single_step import PlayerAI_single_step
from Helper.Player.PlayerHuman import PlayerHuman

# main window
root = Tk()
# set the size of main window
root.geometry('700x700')
# create a canvas to draw board and chessman,and set the background of the canvas white
cv = Canvas(root, bg='white', width=600, height=600)
cv.pack()


def callback_click(x, y):
	if game.now_black == player1.isBlack:
		player1.setTouchCoordinate(x, y)


gui = GUI_TK(cv, 10, 10, 590, 590, callback_click=callback_click, theta=0.4, chess_radii=15)
judge = Judge(15, 15, win_size=5)
boardSave = BoardSave(15, 15)
game = Game(boardSave, gui, judge, callback_win=lambda x, y, winCondition, isBlack: tkMessageBox.showinfo(
	'win', 'x=%r,y=%r,winCondition=%r,isBlack=%r' % (x, y, winCondition, isBlack)))

player1 = PlayerHuman()

# define player2
valuablePoint = ValuablePointLinear()
# evaluate = EvaluateNormal(15, 15)
evaluate = EvaluateNormal2(15, 15)
player2 = PlayerAI_single_step(valuablePoint, evaluate, gui)
# search = SearchMaxmin(valuablePoint, evaluate, depth=2)
# player2=PlayerAI_search(valuablePoint, evaluate,gui,search)

gameController = GameController(player1, player2, game)
Button(root, text='back', command=gameController.back).pack()
Button(root, text='clear', command=gameController.start).pack()

gameController.start()


def delete():
	gameController.stop()
	root.destroy()


root.protocol('WM_DELETE_WINDOW', delete)
root.mainloop()
