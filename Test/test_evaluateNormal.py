from unittest import TestCase
from ..Helper.AI.EvaluateNormal import EvaluateNormal
from ..Helper.BoardSave import BoardSave


class TestEvaluateTranscendental(TestCase):
	def test__remove(self):
		array = [BoardSave.none, ] * 9
		for color in (BoardSave.black, BoardSave.white):
			other_color = BoardSave.exchangePlayer(color)
			for one in range(4):
				for two in range(5, 9):
					for front in range(0, one):
						array[front] = BoardSave.none
					array[one] = other_color
					for mid in range(one + 1, two):
						array[mid] = color
					array[two] = other_color
					for back in range(two + 1, 9):
						array[back] = BoardSave.none
					ret = EvaluateNormal._remove(array, other_color)
					assert len(ret) == two - one - 1

	def test_evaluate_one_direction(self):
		array = [BoardSave.none, ] * 2 + [BoardSave.black, ] * 5 + [BoardSave.none, ] * 2
		assert EvaluateNormal.evaluate_one_direction(array, BoardSave.black) == 5

		array = [BoardSave.none, ] * 2 + [BoardSave.black, ] * 4 + [BoardSave.none, ] * 3
		assert EvaluateNormal.evaluate_one_direction(array, BoardSave.black) == 4

		array = [BoardSave.none, ] * 2 + [BoardSave.black, ] * 3 + [BoardSave.none, ] * 4
		assert EvaluateNormal.evaluate_one_direction(array, BoardSave.black) == (3, False)

		array = [BoardSave.black, ] + [BoardSave.none, ] * 2 + [BoardSave.black, ] * 2 + [BoardSave.none, ] * 4
		assert EvaluateNormal.evaluate_one_direction(array, BoardSave.black) == (3, True)

		array = [BoardSave.none, ] * 3 + [BoardSave.black, ] * 2 + [BoardSave.none, ] * 4
		assert EvaluateNormal.evaluate_one_direction(array, BoardSave.black) == (2, False)

		array = [BoardSave.black, ] + [BoardSave.none, ] * 3 + [BoardSave.black, ] + [BoardSave.none, ] * 4
		assert EvaluateNormal.evaluate_one_direction(array, BoardSave.black) == (2, True)

		array = [BoardSave.none, ] * 4 + [BoardSave.black, ] + [BoardSave.none, ] * 4
		assert EvaluateNormal.evaluate_one_direction(array, BoardSave.black) == 1

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
		save = BoardSave(15, 15)
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
					save.add(x, y, char == '1')
			print(save)
			transcendental = EvaluateNormal(15, 15)
			print(transcendental.getValue(save, 2, 3, BoardSave.black))
