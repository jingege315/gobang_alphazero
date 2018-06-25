from enum import Enum


class Chess(Enum):
	"""
	the chess's enum
	"""
	BLACK = 1
	WHITE = 2
	NONE = 3

	def is_black(self) -> bool:
		return self == self.BLACK

	def is_white(self) -> bool:
		return self == self.WHITE

	def is_none(self) -> bool:
		return self == self.NONE

	def exchange(self):
		return self.BLACK if self.is_white() else self.WHITE

	def is_chess_color(self) -> bool:
		return self.is_black() or self.is_white()

	def is_chess(self) -> bool:
		return self.is_chess_color() or self.is_none()

	def __str__(self) -> str:
		if self.is_black():
			return '1'
		elif self.is_white():
			return '2'
		else:
			return ' '
