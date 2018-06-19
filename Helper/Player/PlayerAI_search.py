import numpy

from ..GUI_Base import GUI_Base
from ..AI.Evaluate import Evaluate
from ..AI.Search import Search
from ..AI.ValuablePoint import ValuablePoint
from ..BoardSave import BoardSave
from ..Player.PlayerAI import PlayerAI


class PlayerAI_search(PlayerAI):
	def __init__(self, valuablePoint: ValuablePoint, evaluate: Evaluate, gui: GUI_Base, search: Search):
		super().__init__(valuablePoint, evaluate, gui)
		self.search = search

	def getNext(self, boardSave: BoardSave, player_me):
		return self.search.getNext(boardSave, player_me)

	def MoveFinish(self, boardSave: BoardSave):
		self.gui.draw_chesses(boardSave.order, is_clear=True)
		for (x, y), score in zip(*self.search.getLastScores()):
			if score == numpy.infty or score == -numpy.infty:
				self.gui.draw_text(x, y, 'inf')
			else:
				self.gui.draw_text(x, y, '%d' % score)
