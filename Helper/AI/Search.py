from .Evaluate import Evaluate
from .ValuablePoint import ValuablePoint
from ..BoardSave import BoardSave


class Search(object):
	def __init__(self, valuablePoint: ValuablePoint, evaluate: Evaluate):
		self.valuablePoint = valuablePoint
		self.evaluate = evaluate
		self.route = []
		self.score = None
		self.point = None
		# save the last scores's result
		self.scores = None
		self.points = None

	def _run(self, boardSave: BoardSave, player_me):
		raise NotImplementedError()

	def getNext(self, boardSave: BoardSave, player_me):
		self._run(boardSave, player_me)
		return self.point

	def getSearchPoints(self):
		return self.route

	def getSearchScore(self):
		return self.score

	def getLastScores(self):
		return self.points, self.scores
