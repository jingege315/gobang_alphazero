from ..BoardSave import BoardSave
from ..Player.Player import Player
from ..AI.Evaluate import Evaluate
from ..AI.ValuablePoint import ValuablePoint
from ..GUI_Base import GUI_Base


class PlayerAI(Player):
	def __init__(self, valuablePoint: ValuablePoint, evaluate: Evaluate, gui: GUI_Base):
		self.valuablePoint = valuablePoint
		self.evaluate = evaluate
		self.gui = gui

	def getNext(self, boardSave: BoardSave, player_me):
		raise NotImplementedError()

	@staticmethod
	def isAuto():
		return True
