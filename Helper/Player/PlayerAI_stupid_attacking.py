from AI.Evaluate import Evaluate
from AI.ValuablePoint import ValuablePoint
from BoardSave import BoardSave
from Player.PlayerAI import PlayerAI
import numpy


class PlayerAI_stupid_attacking(PlayerAI):
	def __init__(self, valuablePoint: ValuablePoint, evaluate: Evaluate):
		super().__init__(valuablePoint, evaluate)

	def getNext(self, boardSave: BoardSave, player_me):
		points = self.valuablePoint.getPoints(boardSave, player_me)
		if len(points) == 0:
			return 7, 7
		values = [self.evaluate.getValue(boardSave, x, y, player_me) for x, y in points]
		max_index = numpy.argmax(values)
		return points[max_index]
