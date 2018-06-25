from ..Player import *


class Game(object):
	"""
	control the condition logic and the drawing logic of gobang
	"""

	def __init__(self, win_size, board_size, callback_win):
		"""
		:param callback_win: the callback function of winning,param:chess:Chess
		"""
		self._judge = Judge(win_size)
		self.board = BoardSave(board_size)
		self._callback_win = callback_win

		self._win_now = False
		self._chess_now = Chess.BLACK

	def is_win(self):
		is_win = self._judge.is_win(self.board)
		if not self._win_now and is_win:
			chess = self._judge.get_win_chess()
			self._callback_win(chess)
			self._win_now = True
		return is_win

	def can_move(self, x, y) -> bool:
		return not self.board.is_moved(x, y) or self._win_now

	def move(self, x, y):
		if self.can_move(x, y):
			self.board.add(x, y, self._chess_now)
			self._chess_now = self._chess_now.exchange()
			self.is_win()

	def back(self):
		if self.board.back():
			self._win_now = False
			self._chess_now = self._chess_now.exchange()

	def back2steps(self):
		self.board.back()
		self.board.back()
		self._win_now = False

	def clear(self):
		self.board.clear()
		self._chess_now = Chess.BLACK
		# stand whether win
		self._win_now = False

	def get_chess_now(self) -> Chess:
		return self._chess_now
