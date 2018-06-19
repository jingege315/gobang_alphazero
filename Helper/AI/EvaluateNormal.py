import numpy as np

from .Evaluate9Cells import Evaluate9Cells
from ..BoardSave import BoardSave


class EvaluateNormal(Evaluate9Cells):
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
		player_him = BoardSave.exchangePlayer(player_me)

		array = EvaluateNormal._remove(array, player_him)
		edge = array[0] == player_me or array[-1] == player_me
		num = array.count(player_me)

		if num in EvaluateNormal.scores.keys():
			if len(array) >= 5:
				return EvaluateNormal.scores[num]
			else:
				return EvaluateNormal.scores[0]
		elif (num, edge) in EvaluateNormal.scores.keys():
			if len(array) >= 6 or edge == True:
				return EvaluateNormal.scores[(num, edge)]
			else:
				return EvaluateNormal.scores[0]
		raise Exception()
