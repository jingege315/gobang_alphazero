from ..Base import *


class ValuablePoint(object):
	"""
	get the valuable points in the board
	"""

	def get_points(self, board: BoardSave, player: Chess) -> list:
		"""
		:param board:
		:param player:
		:return: the valuable points
		"""
		raise NotImplementedError()
