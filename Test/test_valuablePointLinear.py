from unittest import TestCase

from BoardSave import BoardSave
from ValuablePointLinear import ValuablePointLinear


class TestValuablePointLinear(TestCase):
	def test_getPoints(self):
		linear = ValuablePointLinear()
		save = BoardSave(15, 15)
		save.add(1, 1, True)
		save.add(0, 14, False)
		save.add(7, 7, True)
		save.add(8, 8, False)
		print(save)

		ret = linear.getPoints(save, BoardSave.black)

		# (1,1) -> 8
		# (0,14) -> 3
		# (7,7)+(8,8) -> 8*2-4=12
		assert len(ret) == 8 + 3 + 12
		print(ret)
