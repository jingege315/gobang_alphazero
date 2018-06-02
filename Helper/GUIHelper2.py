from Helper.GUIHelper import GUIHelper


class GUIHelper2(GUIHelper):
	"""
	GUI五子棋绘制类，特化
	"""

	def __init__(self, cv, x1, y1, x2, y2, callback_click, chess_radii=10, rows=15, columns=15, theta=0.3):
		"""
		:param cv:
		:param x1:
		:param y1:
		:param x2:
		:param y2:
		:param callback_click: click事件的回调，参数下x,y，代表棋盘坐标
		:param chess_radii:
		:param rows:
		:param columns:
		:param theta: 棋盘坐标误差，可以在+/-theta的误差内认为是对应的棋盘坐标，范围(0,0.5)
		"""

		def draw_line_fun(x1, y1, x2, y2):
			cv.create_line(x1, y1, x2, y2)

		def draw_chess_fun(x, y, black):
			rect = (x - chess_radii, y - chess_radii, x + chess_radii, y + chess_radii)
			if black:
				cv.create_oval(rect, fill='black')
			else:
				cv.create_oval(rect, fill='white')

		def clear_fun():
			cv.delete('all')

		def paint(event):
			x, y = event.x, event.y
			# print('x=%r,y=%r' % (x, y))
			x, y = self.get_coordinate(x, y, theta=theta)
			# print('x=%r,y=%r' % (x, y))
			if x != -1:
				callback_click(x, y)

		cv.bind('<Button-1>', paint)

		GUIHelper.__init__(self, x1, y1, x2, y2, rows, columns, draw_line_fun, draw_chess_fun, clear_fun)
