from Helper import GUIHelper
import numpy as np

from Helper.Judge import Judge


class Controller(object):
	"""
	control the condition logic and the drawing logic of gobang
	五子棋盘的状态逻辑控制，和绘制逻辑控制
	"""

	def __init__(self, draw_helper: GUIHelper, judge: Judge, callback_win):
		"""
		:param callback_win: the callback function of winning，param:x,y,winCondition,isBlack
		"""
		self.draw_helper = draw_helper
		self.judge = judge
		self.callback_win = callback_win
		self.now_black = None
		self.order = None
		self.board = None
		self.win_now = False
		self.clear()

	def change_color(self):
		self.now_black = not self.now_black

	def move(self, x, y):
		if self.board[x, y] != -1:
			return
		if self.win_now:
			return
		self.order.append((x, y, self.now_black))
		self.board[x, y] = self.now_black

		self.draw_helper.draw_chess(x, y, self.now_black)
		self.change_color()
		self.isWin()

	def isWin(self):
		x, y, isWin, winCondition, isBlack = self.judge.win(self.board, self.order)
		if isWin:
			print('win! x=%r,y=%r,winCondition=%r,isBlack=%r' % (x, y, winCondition, isBlack))
			self.callback_win(x, y, winCondition, isBlack)
			self.win_now = True

	def back(self):
		if len(self.order) < 1:
			return
		self.draw_helper.clear()
		self.draw_helper.draw_board()
		self.board[self.order[-1][0], self.order[-1][1]] = -1
		self.order = self.order[:-1]
		for one in self.order:
			self.draw_helper.draw_chess(one[0], one[1], one[2])
		self.change_color()
		self.win_now = False

	def clear(self):
		self.draw_helper.clear()
		self.draw_helper.draw_board()
		self.now_black = True
		# save the order of chess moves,item=(x,y,color)
		self.order = []
		# save the board's content about chess,item=-1/1/0,respectively standing for none,black chess,white chess
		self.board = np.full((self.draw_helper.rows, self.draw_helper.columns), -1)
		# stand whether win
		self.win_now = False
