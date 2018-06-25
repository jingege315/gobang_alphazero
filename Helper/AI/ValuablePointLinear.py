from .ValuablePoint import ValuablePoint
from ..Base import *


class ValuablePointLinear(ValuablePoint):
	"""
	regard the point surrounding with a point which has moved as a valuable point
	"""

	def get_points(self, board: BoardSave, player: Chess):
		points = []

		def is_legal(x, y):
			shift = (
				(-1, -1), (-1, 0), (-1, 1),
				(0, -1), (0, 1),
				(1, -1), (1, 0), (1, 1),
			)
			if not board.is_none(x, y):
				return False
			for x_theta, y_theta in shift:
				x_ = x + x_theta
				y_ = y + y_theta
				if board.is_legal_point(x_, y_) and not board.is_none(x_, y_):
					return True
			return False

		for x, y in board.iter_board_point():
			if is_legal(x, y):
				points.append((x, y))
		return points
