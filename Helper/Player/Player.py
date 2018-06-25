from ..Base import *


class Player(object):
	"""
	the player playing gobang can be human or AI
	"""

	def __init__(self, chess_self: Chess):
		self._chess_self = chess_self

	def get_next(self, board: BoardSave) -> (int, int):
		"""
		the player can use the information of board and order to decide how to move in next step
		:param board:
		:return:
			return (x,y):the move about next step
			return None:waiting for human click
		"""
		raise NotImplementedError()

	@staticmethod
	def is_auto() -> bool:
		"""
		:return: whether the player is AI to auto move chess
		"""
		raise NotImplementedError()

	def get_chess_color(self) -> Chess:
		"""
		:return: the chess's color of this player
		"""
		return self._chess_self
