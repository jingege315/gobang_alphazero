from .Evaluate import Evaluate
from .ValuablePoint import ValuablePoint
from ..Base import *


class Search(object):
	def __init__(self, valuable_point: ValuablePoint, evaluate: Evaluate):
		self._valuablePoint = valuable_point
		self._evaluate = evaluate
		self._route = []
		self._score = None
		self._point = None
		# save the last scores's result
		self._scores = None
		self._points = None

	def run(self, board: BoardSave, player: Chess):
		raise NotImplementedError()

	def get_next(self, board: BoardSave, player) -> (int, int):
		"""
		get the point using search algorithm in 'run' function
		:param board:
		:param player:
		:return:
		"""
		return self._point

	def get_search_points(self) -> list:
		return self._route

	def get_search_score(self) -> int:
		return self._score

	def get_last_scores(self) -> list:
		return self._points, self._scores
