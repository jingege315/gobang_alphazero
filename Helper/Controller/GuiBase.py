from ..Player import *


class GuiBase(object):
	"""
	GUI draw controller for gobang
	"""

	def __init__(self, window_size: WindowSize, board_size: BoardSize):
		"""
		clear_fun: param=None
		draw_chess_fun: param=x,y,black
		draw_line_fun: param=x1,x2,y1,y2
		draw_chess_fun: param=x,y,black
		"""
		self.window_size, self.board_size = window_size, board_size
		self._draw_line_fun = None
		self._draw_chess_fun = None
		self._clear_fun = None
		self._draw_text_fun = None

	def clear(self):
		if self._clear_fun is not None:
			self._clear_fun()
			self.draw_board()

	def get_real_coordinate(self, x, y, theta) -> (int, int):
		"""
		convert from screen coordinate to board coordinate
		:param x: screen coordinate x
		:param y: screen coordinate y
		:param theta: the percent of error theta,consider the coordinate available in the error of -theta~theta percent,
						ranging from 0 to 0.5
		:return: board coordinate
		"""
		x = (x - self.window_size.x1) / ((self.window_size.x2 - self.window_size.x1) / (self.board_size.rows - 1))
		y = (y - self.window_size.y1) / ((self.window_size.y2 - self.window_size.y1) / (self.board_size.columns - 1))
		if abs(x - round(x)) <= theta and abs(y - round(y)) <= theta:
			return round(x), round(y)
		return None

	def draw_board(self):
		if self._draw_line_fun is not None:
			for i in range(self.board_size.rows):
				x = self.window_size.x1 + i * (self.window_size.x2 - self.window_size.x1) / (self.board_size.rows - 1)
				self._draw_line_fun(x, self.window_size.y1, x, self.window_size.y2)
			for i in range(self.board_size.columns):
				y = self.window_size.y1 + i * (self.window_size.y2 - self.window_size.y1) / (
						self.board_size.columns - 1)
				self._draw_line_fun(self.window_size.x1, y, self.window_size.x2, y)

	def draw_chess(self, chess_location: ChessLocation):
		x = self.window_size.x1 + chess_location.x * (self.window_size.x2 - self.window_size.x1) / (
				self.board_size.rows - 1)
		y = self.window_size.y1 + chess_location.y * (self.window_size.y2 - self.window_size.y1) / (
				self.board_size.columns - 1)
		if self._draw_chess_fun is not None:
			self._draw_chess_fun(x, y, chess_location.chess)

	def draw_text(self, x: int, y: int, text: str):
		assert 0 <= x <= self.board_size.rows - 1 and 0 <= y <= self.board_size.columns - 1
		x = self.window_size.x1 + x * (self.window_size.x2 - self.window_size.x1) / (self.board_size.rows - 1)
		y = self.window_size.y1 + y * (self.window_size.y2 - self.window_size.y1) / (self.board_size.columns - 1)
		if self._draw_text_fun is not None:
			self._draw_text_fun(x, y, text)

	def draw_chesses(self, chess_locations):
		for one in chess_locations:
			self.draw_chess(one)
