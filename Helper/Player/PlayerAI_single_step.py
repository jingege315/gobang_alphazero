from ..GUI_Base import GUI_Base
from ..AI.Evaluate import Evaluate
from ..AI.ValuablePoint import ValuablePoint
from ..BoardSave import BoardSave
from ..Player.PlayerAI import PlayerAI
import numpy


class PlayerAI_single_step(PlayerAI):
	def __init__(self, valuablePoint: ValuablePoint, evaluate: Evaluate, gui: GUI_Base):
		super().__init__(valuablePoint, evaluate, gui)
		self.data = None

	def getNext(self, boardSave: BoardSave, player_me):
		points = self.valuablePoint.getPoints(boardSave, player_me)
		if len(points) == 0:
			self.data = zip(((7,7),), (666,))
			return 7, 7

		values = [self.evaluate.getValue(boardSave, x, y, player_me)
				  + self.evaluate.getValue(boardSave, x, y, BoardSave.exchangePlayer(player_me))
				  for x, y in points]
		self.data = zip(points, values)
		max_index = numpy.argmax(values)
		return points[max_index]

	def MoveFinish(self, boardSave: BoardSave):
		if self.gui is None:
			return
		self.gui.draw_chesses(boardSave.order, is_clear=True)
		for (x, y), score in self.data:
			if score == numpy.infty:
				self.gui.draw_text(x, y, 'inf')
			else:
				self.gui.draw_text(x, y, '%d' % score)
