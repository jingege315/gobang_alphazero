from unittest import TestCase
from Helper import *


class TestValuablePointLinear(TestCase):
	def test_getPoints(self):
		linear = ValuablePointLinear()
		board_size = BoardSize(15, 15)
		save = BoardSave(board_size)
		save.add(1, 1, Chess.BLACK)
		save.add(0, 14, Chess.WHITE)
		save.add(7, 7, Chess.BLACK)
		save.add(8, 8, Chess.WHITE)
		print(save)

		ret = linear.get_points(save, Chess.BLACK)

		# (1,1) -> 8
		# (0,14) -> 3
		# (7,7)+(8,8) -> 8*2-4=12
		assert len(ret) == 8 + 3 + 12
		print(ret)
