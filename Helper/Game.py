import GUI_Base
from BoardSave import BoardSave
from Judge import Judge


class Game(object):
	"""
	control the condition logic and the drawing logic of gobang
	"""

	def __init__(self, boardSave: BoardSave, draw_helper: GUI_Base, judge: Judge, callback_win):
		"""
		:param callback_win: the callback function of winning，param:x,y,winCondition,isBlack
		"""
		self.draw_helper = draw_helper
		self.judge = judge
		self.callback_win = callback_win

		self.win_now = False
		self.now_black = None

		self.boardSave = boardSave

		self.clear()

	def _change_color(self):
		self.now_black = not self.now_black

	def _move(self, x, y):
		if not self.boardSave.isNone(x, y):
			return
		if self.win_now:
			return
		self.boardSave.add(x, y, self.now_black)

		self.draw_helper.draw_chess(x, y, self.now_black)
		self._change_color()

	def _isWin(self):
		x, y, isWin, winCondition, isBlack = self.judge.win(self.boardSave)
		return isWin

	def move(self, x, y):
		self._move(x, y)
		self.isWin()

	def isWin(self):
		x, y, isWin, winCondition, isBlack = self.judge.win(self.boardSave)
		if isWin:
			print('win! x=%r,y=%r,winCondition=%r,isBlack=%r' % (x, y, winCondition, isBlack))
			self.callback_win(x, y, winCondition, isBlack)
			self.win_now = True

	def __back(self):
		if len(self.boardSave.order) < 1:
			return
		self.draw_helper.clear()
		yield
		self.draw_helper.draw_chesses(self.boardSave.order)
		self.win_now = False

	def back(self):
		for one in self.__back():
			self.boardSave.back()
		self._change_color()

	def back2steps(self):
		for one in self.__back():
			self.boardSave.back()
			self.boardSave.back()

	def clear(self):
		self.draw_helper.clear()
		self.boardSave.clear()
		self.now_black = True
		# stand whether win
		self.win_now = False
