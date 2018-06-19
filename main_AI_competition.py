from Helper.BoardSave import BoardSave
from Helper.GameController import GameController
from Helper.Game import Game
from Helper.Judge import Judge

from Helper.AI.EvaluateNormal2 import EvaluateNormal2
from Helper.AI.EvaluateNormal import EvaluateNormal
from Helper.AI.ValuablePointLinear import ValuablePointLinear

from Helper.Player.PlayerAI_single_step import PlayerAI_single_step

def callback_win(x, y, winCondition,isBlack):
	print(boardSave)
	print('x=%r,y=%r,winCondition=%r,isBlack=%r' % (x, y, winCondition, isBlack))

judge = Judge(15, 15, win_size=5)
boardSave = BoardSave(15, 15)
game = Game(boardSave, None, judge, callback_win=callback_win)

valuablePoint = ValuablePointLinear()
evaluate = EvaluateNormal(15, 15)
player1 = PlayerAI_single_step(valuablePoint, evaluate, None)

valuablePoint = ValuablePointLinear()
evaluate = EvaluateNormal2(15, 15)
player2 = PlayerAI_single_step(valuablePoint, evaluate, None)

gameController = GameController(player1, player2, game)

for i in range(3):
	gameController.start_noThread()
