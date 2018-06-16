import numpy as np


class BoardSave(object):
	none = -1
	black = 1
	white = 0

	def __init__(self, rows, columns):
		self.rows, self.columns = rows, columns
		self.clear()

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
		self.board = np.full((self.rows, self.columns), -1)

	def isNone(self, x, y):
		return self.board[x, y] == BoardSave.none

	def isBlack(self, x, y):
		return self.board[x, y] == BoardSave.black

	def isWhite(self, x, y):
		return self.board[x, y] == BoardSave.white
