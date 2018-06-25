from .BoardSave import *


class Judge(object):
	def __init__(self, win_size):
		self._win_size = win_size
		self._is_win = False
		self._win_chess = None

	def is_win(self, board: BoardSave) -> bool:
		"""
		judge win or not
		"""
		if len(board.get_order()) == board.board_size.columns * board.board_size.rows:
			self._win_chess = Chess.NONE
			return True
		for x in range(board.board_size.rows - self._win_size + 1):
			for y in range(board.board_size.columns - self._win_size + 1):
				win_chess = self._check_one_grid(x, y, board)
				if win_chess is not None:
					self._win_chess = win_chess
					return True
		return False

	def get_win_chess(self) -> Chess:
		return self._win_chess

	def _check_one_grid(self, x, y, board: BoardSave):
		"""
		check win condition in one grid
		:param x:
		:param y:
		:param board:
		:return: win condition
		"""
		get_functions = (
			(lambda x: x, lambda y: 0),
			(lambda x: 0, lambda y: y),
			(lambda x: x, lambda y: 0),
			(lambda x: self._win_size - x - 1, lambda y: y),
		)
		for get_x_fun, get_y_fun in get_functions:
			condition = self._check_one_grid_condition(x, y, board, get_x_fun, get_y_fun)
			if condition is not None:
				return condition
		return None

	def _check_one_grid_condition(self, x, y, board: BoardSave, get_x_fun, get_y_fun):
		"""
		:param x:
		:param y:
		:param board:
		:param get_x_fun: get checked point from 0~win_size-1
		:param get_y_fun:
		:return:
		"""
		x_0 = board.get_chess(x + get_x_fun(0), y + get_y_fun(0))
		if x_0.is_none():
			return None
		for i in range(1, self._win_size):
			x_ = x + get_x_fun(i)
			y_ = y + get_y_fun(i)
			if x_0 != board.get_chess(x_, y_):
				return None
		return x_0
