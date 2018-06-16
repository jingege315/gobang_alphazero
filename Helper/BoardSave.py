import numpy as np


class BoardSave(object):
	none = -1
	black = 1
	white = 0

	def __init__(self, rows, columns):
		self.__rows, self.__columns = rows, columns
		self.clear()

	@staticmethod
	def isBoard(board):
		"""
		judge whether the board value is legal board (none or black or white)
		:param board:
		:return:
		"""
		return board == BoardSave.none or board == BoardSave.black or board == BoardSave.white

	@staticmethod
	def isPlayer(board):
		"""
		judge whether the board value is legal player (black or white)
		:param board:
		:return:
		"""
		return board == BoardSave.black or board == BoardSave.white

	@staticmethod
	def exchangePlayer(board):
		assert BoardSave.isPlayer(board)
		return BoardSave.black if board == BoardSave.white else BoardSave.white

	def add(self, x, y, is_black):
		self.order.append((x, y, is_black))
		self.board[x, y] = is_black

	def back(self):
		self.board[self.order[-1][0], self.order[-1][1]] = -1
		self.order = self.order[:-1]

	def clear(self):
		# save the order of chess moves,item=(x,y,color)
		self.order = []
		# save the board's content about chess,item=-1/1/0,respectively standing for none,black chess,white chess
		self.board = np.full((self.__rows, self.__columns), -1)

	def isNone(self, x, y):
		return self.board[x, y] == BoardSave.none

	def isBlack(self, x, y):
		return self.board[x, y] == BoardSave.black

	def isWhite(self, x, y):
		return self.board[x, y] == BoardSave.white

	def iterBoardPoint(self):
		for i in range(self.__rows):
			for j in range(self.__columns):
				yield i, j

	def isLegalPoint(self, x, y):
		return 0 <= x < self.__rows and 0 <= y < self.__columns

	def __str__(self):
		def board_item_2_char(item):
			if item == BoardSave.black:
				return '1'
			elif item == BoardSave.white:
				return '2'
			else:
				return ' '

		s = '\n'
		for i in range(self.__rows):
			s += ' | '
			for j in range(self.__columns):
				s += board_item_2_char(self.board[i][j]) + ' '
			s += '| \n'
		return s
