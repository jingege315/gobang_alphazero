from unittest import TestCase
from ..Helper.AI.EvaluateNormal import EvaluateNormal
from ..Helper.AI.SearchMaxmin import SearchMaxmin
from ..Helper.AI.ValuablePointLinear import ValuablePointLinear
from ..Helper.BoardSave import BoardSave


class TestSearchMaxmin(TestCase):
	def test_run(self):
		board = BoardSave(15, 15)
		valuablePoint = ValuablePointLinear()
		evaluate = EvaluateNormal(15, 15)

		board.add(7, 7, True)
		board.add(6, 6, False)
		board.add(6, 8, True)
		board.add(8, 6, False)
		search = SearchMaxmin(valuablePoint, evaluate, depth=2)
		search._run(board, BoardSave.black)
		print(board)
		print('route : ', search.route)
		print('score : ', search.score)
		print('point : ', search.point)

		board.add(search.point[0],search.point[1],True)
		print(board)
