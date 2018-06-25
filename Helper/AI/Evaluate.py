from ..Base import *


class Evaluate(object):
	"""
	evaluate the player's score in coordinate(x,y)
	"""

	def get_value(self, board: BoardSave, x, y, player: Chess) -> int:
		"""
		evaluate the player's score in coordinate(x,y)
		"""
		raise NotImplementedError()
