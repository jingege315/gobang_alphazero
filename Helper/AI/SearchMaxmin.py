from copy import deepcopy
from .Search import Search
from .Evaluate import Evaluate
from .ValuablePoint import ValuablePoint
from ..Base import *


class SearchMaxmin(Search):
	def __init__(self, valuable_point: ValuablePoint, evaluate: Evaluate, win_size, depth=6):
		assert depth % 2 == 0 and depth != 0
		super().__init__(valuable_point, evaluate)
		self.depth = depth
		self.judge = Judge(win_size)

	def _run_core(self, board: BoardSave, x0, y0, player_me, player_now, depth):
		"""

		:param board: the board in this function
		:param x0: the point will move,if x0==-1,it means the first time running this function
		:param y0: the point will move
		:param player_me: the initial player
		:param player_now: the player now
		:param depth: the depth now,it should satisfy (deep%2==0 and deep!=0)
		:return: the score moving here and all points going through
		"""
		# stop recurrence
		if depth == 0 or self.judge.is_win(board):
			score_me = self._evaluate.get_value(board, x0, y0, player_me)
			score_opponent = self._evaluate.get_value(board, x0, y0, player_me.exchange())
			score = score_me - score_opponent
			return score, [(x0, y0)]

		# move step
		if x0 != -1:
			board.add(x0, y0, player_now)
			player_now = player_now.exchange()

		# calculate the score of each valuable point
		scores = []
		routes = []
		points = self._valuablePoint.get_points(board, player_now)
		for x, y in points:
			score, route = self._run_core(deepcopy(board), x, y, player_me, player_now, depth - 1)
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

	def run(self, board: BoardSave, player):
		self.score, self.route = self._run_core(board, -1, -1, player, player, self.depth)
		self.point = self.route[-1]
