from .Evaluate import Evaluate
from ..Base import *


class Evaluate9Cells(Evaluate):
	"""
	evaluate the player's score in coordinate(x,y) using 9 cells way whose center is moving point in 4 directions
	"""

	def get_value(self, board: BoardSave, x, y, player: Chess) -> int:
		player_him = player.exchange()

		def create_coordinate(x_fun, y_fun):
			ret = []
			for i in range(-4, 5):
				if i == 0:
					ret.append(player)
					continue
				x_ = x + x_fun(i)
				y_ = y + y_fun(i)
				if board.is_legal_point(x_, y_):
					ret.append(board.get_chess(x_, y_))
				else:
					ret.append(player_him)
			return ret

		# vertical
		coordinate1 = create_coordinate(lambda x: x, lambda y: 0)
		# horizontal
		coordinate2 = create_coordinate(lambda x: 0, lambda y: y)
		# right-falling
		coordinate3 = create_coordinate(lambda x: x, lambda y: y)
		# right-raising
		coordinate4 = create_coordinate(lambda x: -x, lambda y: y)
		scores = [self._evaluate_one_direction(one, player) for one in (coordinate1, coordinate2, coordinate3, coordinate4)]
		return sum(scores)

	@staticmethod
	def _evaluate_one_direction(array, player: Chess) -> int:
		"""
		get the value of the given array in one direction
		:param array: it is a list whose length is 9
						index 4,the value represent the location where the chess need to move soon
		:param player:
		:return: score
		"""
		raise NotImplementedError()
