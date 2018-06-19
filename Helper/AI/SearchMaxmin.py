from copy import deepcopy

from Helper.Judge import Judge
from .Search import Search
from ..BoardSave import BoardSave
from .Evaluate import Evaluate
from .ValuablePoint import ValuablePoint


class SearchMaxmin(Search):
	def __init__(self, valuablePoint: ValuablePoint, evaluate: Evaluate, depth=6):
		assert depth % 2 == 0 and depth != 0
		super().__init__(valuablePoint, evaluate)
		self.depth = depth
		self.judge = Judge(15, 15, 5)

	def _run_core(self, boardSave: BoardSave, x0, y0, player_me, player_now, depth):
		"""

		:param boardSave: the board in this function
		:param x0: the point will move,if x0==-1,it means the first time running this function
		:param y0: the point will move
		:param player_me: the initial player
		:param player_now: the player now
		:param depth: the depth now,it should satisfy (deep%2==0 and deep!=0)
		:return: the score moving here and all points going through
		"""
		# stop recurrence
		if depth == 0 or self.judge.isWin(boardSave):
			score_me = self.evaluate.getValue(boardSave, x0, y0, player_me)
			score_opponent = self.evaluate.getValue(boardSave, x0, y0, BoardSave.exchangePlayer(player_me))
			score = score_me - score_opponent
			return score, [(x0, y0)]

		# move step
		if x0 != -1:
			boardSave.add(x0, y0, player_now == BoardSave.black)
			player_now = boardSave.exchangePlayer(player_now)

		# calculate the score of each valuable point
		scores = []
		routes = []
		points = self.valuablePoint.getPoints(boardSave, player_now)
		for x, y in points:
			score, route = self._run_core(deepcopy(boardSave), x, y, player_me, player_now, depth - 1)
			print('route:', route, ',score:', score)
			scores.append(score)
			routes.append(route)

		# get best point to move
		score = max(scores) if player_now == player_me else min(scores)
		score_index = scores.index(score)
		route = routes[score_index]

		# record the point going through
		if x0 != -1:
			route.append((x0, y0))
		else:
			self.scores = scores
			self.points = [one[-1] for one in routes]

		return score, route

	def _run(self, boardSave: BoardSave, player_me):
		self.score, self.route = self._run_core(boardSave, -1, -1, player_me, player_me, self.depth)
		self.point = self.route[-1]
