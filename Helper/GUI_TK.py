from tkinter import Canvas

from .GUI_Base import GUI_Base


class GUI_TK(GUI_Base):
	"""
	GUI五子棋绘制类，使用tkinter库渲染的特化类
	"""

	def __init__(self, cv: Canvas, x1, y1, x2, y2, callback_click,
				 chess_radii=10, rows=15, columns=15, theta=0.3):
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
			cv.create_oval(rect, fill='black' if black else 'white')

		def draw_text_fun(x, y, text):
			rect = (x - chess_radii, y - chess_radii, x + chess_radii, y + chess_radii)
			cv.create_text(x, y, text=text, fill='red', font=("Purisa", 8))

		def clear_fun():
			cv.delete('all')

		def _callback_click(event):
			x, y = event.x, event.y
			x, y = self.get_coordinate(x, y, theta=theta)
			if x != -1:
				callback_click(x, y)

		cv.bind('<Button-1>', _callback_click)

		GUI_Base.__init__(self, x1, y1, x2, y2, rows, columns)
		self.draw_line_fun, self.draw_chess_fun, self.clear_fun, self.draw_text_fun = \
			draw_line_fun, draw_chess_fun, clear_fun, draw_text_fun
