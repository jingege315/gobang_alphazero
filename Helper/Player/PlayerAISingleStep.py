import numpy
from ..AI import *
from .PlayerAI import PlayerAI


class PlayerAISingleStep(PlayerAI):
	def __init__(self, chess_self: Chess, valuable_point: ValuablePoint, evaluate: Evaluate):
		super().__init__(chess_self)
		self._valuablePoint = valuable_point
		self._evaluate = evaluate
		self._scores = None

	def get_next(self, board: BoardSave):
		points = self._valuablePoint.get_points(board, self._chess_self)
		if len(points) == 0:
			self._scores = zip(((7, 7),), (666,))
			return 7, 7

		values = [self._evaluate.get_value(board, x, y, self._chess_self)
		          + self._evaluate.get_value(board, x, y, self._chess_self.exchange())
		          for x, y in points]
		self._scores = [ChessScore(x, y, score) for (x, y), score in zip(points, values)]
		max_index = numpy.argmax(values)
		return points[max_index]

	def get_scores(self):
		return self._scores
