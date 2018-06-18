import numpy as np

from .Evaluate import Evaluate
from ..BoardSave import BoardSave


class EvaluateNormal(Evaluate):
	"""
	score dict:
	key : the board item number of array (dim:9) after _remove() function ,
			if is a tuple,the tuple's second item means whether the edge is player_mine,
				if True,need the length of array after _remove() >=5
				if False,need the length of array after _remove() >=6,
					because the score of this condition is higher than True,and the condition is more likely win the competition
	"""
	scores = {
		5: np.infty,
		(4, False): 1_000_000,
		(4, True): 100_000,
		(3, False): 10_000,
		(3, True): 1_000,
		(2, False): 100,
		(2, True): 10,
		1: 1,
		0: 0,
	}

	def __init__(self, rows, columns):
		self.rows, self.columns = rows, columns

	@staticmethod
	def _remove(array, player_him):
		"""
		get the maximum array that is not contain the chess of others in the given array
		:param array: it is a list,dim=9
		:return: array which remove other's chess
		"""
		assert len(array) == 9
		assert BoardSave.isPlayer(player_him)

		start = 3
		end = 5
		for i in range(start, -1, -1):
			if array[i] == player_him:
				start = i + 1
				break
		else:
			start = 0

		for i in range(end, len(array)):
			if array[i] == player_him:
				end = i - 1
				break
		else:
			end = 8

		return array[start:end + 1]

	@staticmethod
	def evaluate_one_direction(array, player_me):
		"""
		get the value of the given array
		:param array: it is a list,dim=9
			index 4,the value represent the location where the chess need to move soon
		:param player_me:
		:return: one item of conditions
		"""
		player_him = BoardSave.exchangePlayer(player_me)

		array = EvaluateNormal._remove(array, player_him)
		edge = array[0] == player_me or array[-1] == player_me
		num = array.count(player_me)

		if num in EvaluateNormal.scores.keys():
			if len(array) >= 5:
				return num
			else:
				return 0
		elif (num, edge) in EvaluateNormal.scores.keys():
			if len(array) >= 6 or edge == True:
				return num, edge
			else:
				return 0
		raise Exception()

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
		values = [EvaluateNormal.evaluate_one_direction(one, player_me) for one in
				  (coordinate1, coordinate2, coordinate3, coordinate4)]
		score = [EvaluateNormal.scores[one] for one in values]
		return sum(score)
