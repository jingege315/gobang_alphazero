class GUI_Base(object):
	"""
	GUI五子棋绘制类
	"""
	def __init__(self, x1, y1, x2, y2, rows, columns, draw_line_fun, draw_chess_fun,clear_fun):
		self.x1, self.y1, self.x2, self.y2, self.rows, self.columns = x1, y1, x2, y2, rows, columns
		self.draw_line_fun, self.draw_chess_fun ,self.clear_fun= draw_line_fun, draw_chess_fun,clear_fun

	@staticmethod
	def _draw_board(x1, y1, x2, y2, rows, columns, draw_line_fun):
		"""
		横向是x，纵向是y，左上角是起点
		:param draw_line_fun: 传入参数（x1,y1,x2,y2）
		"""
		for i in range(rows):
			x = x1 + i * (x2 - x1) / (rows - 1)
			draw_line_fun(x, y1, x, y2)
		for i in range(columns):
			y = y1 + i * (y2 - y1) / (columns - 1)
			draw_line_fun(x1, y, x2, y)

	@staticmethod
	def _draw_chess(x1, y1, x2, y2, rows, columns, x, y, black, draw_chess_fun):
		"""
		绘制棋子，横向是x，纵向是y，左上角是起点
		:param x: 落子的x坐标，范围0~rows-1
		:param y: 落子的y坐标，范围0~columns-1
		:param draw_chess_fun: 传入参数（x,y,black）
		"""
		assert 0 <= x <= rows - 1 and 0 <= y <= columns - 1
		x = x1 + x * (x2 - x1) / (rows - 1)
		y = y1 + y * (y2 - y1) / (columns - 1)
		draw_chess_fun(x, y, black)

	@staticmethod
	def _get_coordinate(x1, y1, x2, y2, rows, columns, x, y, theta):
		"""
		得到屏幕坐标x，y对应的棋盘坐标
		:param x: 屏幕坐标x
		:param y: 屏幕坐标y
		:param theta: 棋盘坐标误差，可以在+/-theta的误差内认为是对应的棋盘坐标，范围(0,0.5)
		:return: 棋盘坐标x_,y_，当失败的时候返回-1，-1
		"""
		x = (x - x1) / ((x2 - x1) / (rows - 1))
		y = (y - y1) / ((y2 - y1) / (columns - 1))
		if abs(x - round(x)) <= theta and abs(y - round(y)) <= theta:
			return round(x), round(y)
		return -1, -1

	def draw_board(self):
		self._draw_board(self.x1, self.y1, self.x2, self.y2, self.rows, self.columns, self.draw_line_fun)

	def draw_chess(self, x, y, black):
		self._draw_chess(self.x1, self.y1, self.x2, self.y2, self.rows, self.columns, x, y, black, self.draw_chess_fun)

	def draw_chesses(self,ls):
		"""
		绘制所有棋子
		"""
		for one in ls:
			self.draw_chess(*one)

	def get_coordinate(self, x, y, theta):
		return self._get_coordinate(self.x1, self.y1, self.x2, self.y2, self.rows, self.columns, x, y, theta)

	def draw_chess_black(self, x, y):
		self.draw_chess(x, y, True)

	def draw_chess_white(self, x, y):
		self.draw_chess(x, y, False)

	def clear(self):
		"""
		清空棋盘
		"""
		self.clear_fun()
		self.draw_board()
