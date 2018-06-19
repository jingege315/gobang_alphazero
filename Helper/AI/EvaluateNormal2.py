import numpy as np

from .Evaluate9Cells import Evaluate9Cells
from ..BoardSave import BoardSave


class EvaluateNormal2(Evaluate9Cells):
	score_dict = {
		'win': np.infty,
		'will_win': 1_000_000,
		'must_do': 100_000,
		'force': 10_000,
		'will_must_do': 1_000,
		'develop_1': 100,
		'develop_2': 10,
		'one_step': 1,
		0: 0,
	}
	score_situation = {
		# win
		'bbbbb': 'win',

		# will win
		' bbbb ': 'will_win',

		# must do
		(4, 5): 'must_do',

		# force
		' bb b ': 'force',
		' bbb  ': 'force',

		# will must do
		(3, 5): 'will_must_do',

		# develop 1
		'b b': 'develop_1',
		'bb': 'develop_1',

		# develop 2
		'b  b': 'develop_2',

		# one step
		'b': 'one_step',
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

		array[4] = player_me
		array = EvaluateNormal2._remove(array, player_him)
		if len(array) < 5:
			return 0
		for situation in EvaluateNormal2.score_situation.keys():
			if EvaluateNormal2._situation_match(situation, array, player_me):
				return EvaluateNormal2.score_dict[EvaluateNormal2.score_situation[situation]]
		raise Exception()

	@staticmethod
	def _situation_match(situation, array, player_me):
		if not isinstance(situation, tuple):
			situation = [player_me if one == 'b' else BoardSave.none for one in situation]
			situation_reverse = situation[::-1]
			l = len(situation)
			for i in range(0, len(array) - l + 1):
				sub_array = array[i:i + l]
				if sub_array == situation or sub_array == situation_reverse:
					return True
		else:
			number, length = situation
			for i in range(0, len(array) - length + 1):
				sub_array = array[i:i + length]
				if sub_array.count(player_me) == number:
					return True
		return False
