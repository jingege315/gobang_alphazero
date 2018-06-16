from ..BoardSave import BoardSave
from ..Player.Player import Player
from ..AI.Evaluate import Evaluate
from ..AI.ValuablePoint import ValuablePoint


class PlayerAI(Player):
	def __init__(self, valuablePoint: ValuablePoint, evaluate: Evaluate):
		self.valuablePoint = valuablePoint
		self.evaluate = evaluate

	def getNext(self, boardSave: BoardSave, player_me):
		raise NotImplementedError()

	@staticmethod
	def isAuto():
		return True
