from .BoardSize import BoardSize
from .Chess import Chess
from .ChessLocation import ChessLocation


class BoardSave(object):
	def __init__(self, board_size: BoardSize):
		self.board_size = board_size
		self.clear()

	def add(self, x, y, chess: Chess):
		assert chess.is_chess_color()
		self._order.append(ChessLocation(x, y, chess))
		self._board[x][y] = chess

	def back(self) -> bool:
		if len(self._order) >= 1:
			self._board[self._order[-1].x][self._order[-1].y] = Chess.NONE
			self._order = self._order[:-1]
			return True
		return False

	def clear(self):
		# save the order of chess moves,item=ChessLocation
		self._order = []
		# save the board's content about chess,item=Chess
		self._board = [[Chess.NONE for i in range(self.board_size.columns)] for j in range(self.board_size.rows)]

	def is_none(self, x, y) -> bool:
		return self._board[x][y].is_none()

	def is_black(self, x, y) -> bool:
		return self._board[x][y].is_black()

	def is_white(self, x, y) -> bool:
		return self._board[x][y].is_white()

	def is_moved(self, x, y) -> bool:
		return not self.is_none(x, y)

	def is_legal_point(self, x, y) -> bool:
		return 0 <= x < self.board_size.rows and 0 <= y < self.board_size.columns

	def __str__(self):
		s = '\n'
		for i in range(self.board_size.rows):
			s += ' | '
			for j in range(self.board_size.columns):
				s += self._board[i][j].__str__() + ' '
			s += '| \n'
		return s

	def iter_board_point(self):
		for i in range(self.board_size.rows):
			for j in range(self.board_size.columns):
				yield i, j

	def get_chess(self, x, y) -> Chess:
		return self._board[x][y]

	def get_order(self) -> list:
		return self._order
