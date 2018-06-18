from .BoardSave import BoardSave


class Judge(object):
	"""
	judge whether some player win
	判断是否胜利
	"""

	def __init__(self, rows, columns, win_size):
		self.rows, self.columns, self.win_size = rows, columns, win_size

	def create_check_grid(self):
		"""
		create all the grid that need to check in the upper left corner
		生成所有的左上角网格
		:return: the coordinate(x,y) of each grid
		"""
		for i in range(self.rows - self.win_size + 1):
			for j in range(self.columns - self.win_size + 1):
				yield i, j

	def check_one_grid_condition(self, x, y, boardSave: BoardSave, get_x_fun, get_y_fun):
		"""
		:param x:
		:param y:
		:param boardSave:
		:param get_x_fun: 得到0~win_size-1的对应检查的坐标位置
		:param get_y_fun:
		:return:
		"""
		if boardSave.isNone(x + get_x_fun(0), y + get_y_fun(0)):
			return False
		for i in range(1, self.win_size):
			if boardSave.board[x + get_x_fun(0), y + get_y_fun(0)] != \
					boardSave.board[x + get_x_fun(i), y + get_y_fun(i)]:
				return False
		return True

	def check_one_grid(self, x, y, boardSave: BoardSave):
		"""
		检查一个左上角网格是否胜利
		:param x:
		:param y:
		:param boardSave:
		:return: 1/2/3/4 代表胜利的横竖撇捺，0 代表没有胜利
		"""
		if self.check_one_grid_condition(x, y, boardSave, lambda x: x, lambda y: 0):
			return 1
		if self.check_one_grid_condition(x, y, boardSave, lambda x: 0, lambda y: y):
			return 2
		if self.check_one_grid_condition(x, y, boardSave, lambda x: self.win_size - x - 1, lambda y: y):
			return 3
		if self.check_one_grid_condition(x, y, boardSave, lambda x: x, lambda y: y):
			return 4
		return 0

	def win(self, boardSave: BoardSave):
		"""
		判断是否胜利
		:return: (x,y,isWin,winCondition,isBlack)
					winCondition: 1/2/3/4 代表胜利的横竖撇捺，0 代表没有胜利，5 代表平局
		"""
		if len(boardSave.order) == self.columns * self.rows:
			return 0, 0, True, 5, 0
		for x, y in self.create_check_grid():
			check = self.check_one_grid(x, y, boardSave)
			if check != 0:
				return x, y, True, check, boardSave.board[x, y] == BoardSave.black
		return 0, 0, False, 0, 0

	def isWin(self, boardSave: BoardSave):
		x, y, isWin, winCondition, isBlack = self.win(boardSave)
		return isWin
