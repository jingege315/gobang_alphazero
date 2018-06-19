from Helper.AI.Evaluate import Evaluate
from Helper.BoardSave import BoardSave


class Evaluate9Cells(Evaluate):
	"""
	evaluate 9 cells who's center is moving point in 4 directions
	"""

	def getValue(self, boardSave: BoardSave, x, y, player_me):
		player_him = BoardSave.exchangePlayer(player_me)

		def createCoordinate(x_fun, y_fun):
			ret = []
			for i in range(-4, 5):
				if i == 0:
					ret.append(player_me)
					continue
				x_ = x + x_fun(i)
				y_ = y + y_fun(i)
				if boardSave.isLegalPoint(x_, y_):
					ret.append(boardSave.board[x_][y_])
				else:
					ret.append(player_him)
			return ret

		# vertical
		coordinate1 = createCoordinate(lambda x: x, lambda y: 0)
		# horizontal
		coordinate2 = createCoordinate(lambda x: 0, lambda y: y)
		# right-falling
		coordinate3 = createCoordinate(lambda x: x, lambda y: y)
		# right-raising
		coordinate4 = createCoordinate(lambda x: -x, lambda y: y)
		scores = [self.evaluate_one_direction(one, player_me) for one in
				  (coordinate1, coordinate2, coordinate3, coordinate4)]
		return sum(scores)

	@staticmethod
	def evaluate_one_direction(array, player_me):
		"""
		get the value of the given array
		:param array: it is a list,dim=9
			index 4,the value represent the location where the chess need to move soon
		:param player_me:
		:return: score
		"""
		raise NotImplementedError()
