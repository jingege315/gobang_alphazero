from tkinter import Canvas
from .GuiBase import GuiBase
from ..Player import *


class GuiTk(GuiBase):
	"""
	GUI draw controller for gobang,using tkinter library
	"""

	def __init__(self, cv: Canvas, callback_click, window_size: WindowSize, board_size: BoardSize, chess_radii=10,
	             theta=0.3):
		super().__init__(window_size, board_size)

		def draw_line_fun(x1, y1, x2, y2):
			cv.create_line(x1, y1, x2, y2)

		def draw_chess_fun(x, y, chess: Chess):
			rect = (x - chess_radii, y - chess_radii, x + chess_radii, y + chess_radii)
			cv.create_oval(rect, fill='black' if chess.is_black() else 'white')

		def draw_text_fun(x, y, text):
			rect = (x - chess_radii, y - chess_radii, x + chess_radii, y + chess_radii)
			cv.create_text(x, y, text=text, fill='red', font=("Purisa", 8))

		def clear_fun():
			cv.delete('all')

		def _callback_click(event):
			if callback_click is None:
				return
			x, y = event.x, event.y
			coordinate = self.get_real_coordinate(x, y, theta=theta)
			if coordinate is not None:
				x, y = coordinate
				callback_click(x, y)

		cv.bind('<Button-1>', _callback_click)

		self._draw_line_fun, self._draw_chess_fun, self._clear_fun, self._draw_text_fun = \
			draw_line_fun, draw_chess_fun, clear_fun, draw_text_fun
