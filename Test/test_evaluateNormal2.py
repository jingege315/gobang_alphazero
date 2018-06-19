from unittest import TestCase
from Helper.AI.EvaluateNormal2 import EvaluateNormal2
from Helper.BoardSave import BoardSave


class TestEvaluateNormal2(TestCase):
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
					ret = EvaluateNormal2._remove(array, other_color)
					assert len(ret) == two - one - 1

	@staticmethod
	def evaluate_one_direction_generator(s: str):
		if not s.__contains__('?'):
			yield s
			return
		index = s.find('?')
		s = s[:index] + 'w' + s[index + 1:]
		for one in TestEvaluateNormal2.evaluate_one_direction_generator(s):
			yield one
		s = s[:index] + 'n' + s[index + 1:]
		for one in TestEvaluateNormal2.evaluate_one_direction_generator(s):
			yield one

	def test_evaluate_one_direction_generator_test(self):
		print()
		for one in TestEvaluateNormal2.evaluate_one_direction_generator('??bb_bb??'):
			print(one)
		print()
		for one in TestEvaluateNormal2.evaluate_one_direction_generator('bb_bb'):
			print(one)

	def test__situation_match(self):
		for s in ('nbbnbn', 'nbbnbn'[::-1], 'nbbnbn', 'bbbnbb', 'bnnbb'):
			print()
			for situation in EvaluateNormal2.score_situation.keys():
				array = [BoardSave.none if i == 'n' else BoardSave.black if i == 'b' else BoardSave.white for i in s]
				print(EvaluateNormal2.score_situation[situation], ' : ',
					  EvaluateNormal2._situation_match(situation, array, BoardSave.black))

	def test_evaluate_one_direction(self):
		s = [
			('?? bb_bb ??', 'win'),
			('?n bb_b n??', 'will win'),
			('?? bb_nbb ?', 'must do'),
			('?? bb_nb ??', 'must do'),
			('?n bb_ nn??', 'force'),
			('nn bb_ n???', 'force'),
			('n bnb_ n???', 'force'),
			('bnnb_ ????', 'will must do'),
			('? bnn_b ???', 'will must do'),
			('??n b_ nn??', 'develop 1'),
			('?? bn_ nn??', 'develop 1'),
			('n bnn_ nnnn', 'develop 2'),
			('b nnn _ nnnn', 'one step'),
			('nnnn _ nnnn', 'one step'),

		]
		for situation, result in s:
			result = result.replace(' ', '_')
			for one_instance in TestEvaluateNormal2.evaluate_one_direction_generator(situation):
				two = one_instance.replace(' ', '')
				assert len(two) == 9
				assert two.count('_') == 1
				assert two.find('_') == 4
				array2 = [BoardSave.none if i == 'n' or i == '_' else BoardSave.black if i == 'b' else BoardSave.white
						  for i in two]
				result_real = EvaluateNormal2.evaluate_one_direction(array2, BoardSave.black)
				assertion = result_real == result
				print('condition=%s,%r==%r(real)' % (one_instance, result, result_real))
				assert assertion

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
			transcendental = EvaluateNormal2(15, 15)
			print(transcendental.getValue(save, 2, 3, BoardSave.black))
