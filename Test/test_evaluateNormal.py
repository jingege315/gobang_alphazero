from unittest import TestCase
from Helper import *


class TestEvaluateNormal(TestCase):
	def test__remove(self):
		array = [Chess.NONE, ] * 9
		for color in (Chess.BLACK, Chess.WHITE):
			other_color = color.exchange()
			for one in range(4):
				for two in range(5, 9):
					for front in range(0, one):
						array[front] = Chess.NONE
					array[one] = other_color
					for mid in range(one + 1, two):
						array[mid] = color
					array[two] = other_color
					for back in range(two + 1, 9):
						array[back] = Chess.NONE
					ret = EvaluateNormal._remove(array, other_color)
					assert len(ret) == two - one - 1

	def test_evaluate_one_direction(self):
		array = [Chess.NONE, ] * 2 + [Chess.BLACK, ] * 5 + [Chess.NONE, ] * 2
		assert EvaluateNormal._evaluate_one_direction(array, Chess.BLACK) == EvaluateNormal._scores[5]

		array = [Chess.NONE, ] * 2 + [Chess.BLACK, ] * 4 + [Chess.NONE, ] * 3
		assert EvaluateNormal._evaluate_one_direction(array, Chess.BLACK) == EvaluateNormal._scores[(4, False)]

		array = [Chess.NONE, ] * 2 + [Chess.BLACK, ] * 3 + [Chess.NONE, ] * 4
		assert EvaluateNormal._evaluate_one_direction(array, Chess.BLACK) == EvaluateNormal._scores[(3, False)]

		array = [Chess.BLACK, ] + [Chess.NONE, ] * 2 + [Chess.BLACK, ] * 2 + [Chess.NONE, ] * 4
		assert EvaluateNormal._evaluate_one_direction(array, Chess.BLACK) == EvaluateNormal._scores[(3, True)]

		array = [Chess.NONE, ] * 3 + [Chess.BLACK, ] * 2 + [Chess.NONE, ] * 4
		assert EvaluateNormal._evaluate_one_direction(array, Chess.BLACK) == EvaluateNormal._scores[(2, False)]

		array = [Chess.BLACK, ] + [Chess.NONE, ] * 3 + [Chess.BLACK, ] + [Chess.NONE, ] * 4
		assert EvaluateNormal._evaluate_one_direction(array, Chess.BLACK) == EvaluateNormal._scores[(2, True)]

		array = [Chess.NONE, ] * 4 + [Chess.BLACK, ] + [Chess.NONE, ] * 4
		assert EvaluateNormal._evaluate_one_direction(array, Chess.BLACK) == EvaluateNormal._scores[1]

	def test_getValue(self):
		"""
		test the condition below
		'1' replace black
		'0' replace moving black in next step
		' ' replace none
		'2' replace white

		| _ _ _ _ _ _ _ _
		| 2 1 2 2 2 1 2 2
		| 2 2 1 2 1 2 2 2
		| 2   1 0 1 1   2
		| 2 2 1 2 1 2 2 2
		| 2 2 2 2 2 1 2 2
		| 2 2 2 2 2 2 2 2
		| 2 2 2 2 2 2 2 2

		| _ _ _ _ _ _ _ _
		| 2   2 2 2 1 2 2
		| 2 2 1 2 1 2 2 2
		| 2 2 1 0 1 1   2
		| 2 2 1 2 1 2 2 2
		| 2 2 2 2 2   2 2
		| 2 2 2 2 2 2 2 2
		| 2 2 2 2 2 2 2 2
		:return:
		"""
		board_size = BoardSize(15, 15)
		save = BoardSave(board_size)
		s = [[
			'21222122',
			'22121222',
			'2 1 11 2',
			'22121222',
			'22222122',
			'22222222',
			'22222222',
		], [
			'2 222122',
			'22121222',
			'221 11 2',
			'22121222',
			'22222 22',
			'22222222',
			'22222222',
		], [
			'2 222122',
			'22121222',
			'2 1 11 2',
			'22121222',
			'22222 22',
			'22222222',
			'22222222',
		]]
		for s_one in s:
			save.clear()
			for x, one in enumerate(s_one):
				for y, char in enumerate(one):
					if char == ' ':
						continue
					save.add(x, y, Chess.BLACK if char == '1' else Chess.WHITE)
			print(save)
			transcendental = EvaluateNormal()
			print(transcendental.get_value(save, 2, 3, Chess.BLACK))
