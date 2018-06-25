from unittest import TestCase
from Helper import *


class TestSearchMaxmin(TestCase):
	def test_run(self):
		board_size = BoardSize(15, 15)
		board = BoardSave(board_size)
		valuable_point = ValuablePointLinear()
		evaluate = EvaluateNormal()

		board.add(7, 7, Chess.BLACK)
		board.add(6, 6, Chess.WHITE)
		board.add(6, 8, Chess.BLACK)
		board.add(8, 6, Chess.WHITE)
		search = SearchMaxmin(valuable_point, evaluate, win_size=5, depth=2)
		search.run(board, Chess.BLACK)
		print(board)
		print('route : ', search.route)
		print('score : ', search.score)
		print('point : ', search.point)

		board.add(search.point[0], search.point[1], Chess.BLACK)
		print(board)
