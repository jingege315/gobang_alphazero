from ..Base import *
from .Player import Player


class PlayerHuman(Player):
	def __init__(self, chess_self: Chess):
		super().__init__(chess_self)
		self.new_coordinate = None
		self.x = None
		self.y = None

	def set_touched_coordinate(self, x, y):
		"""
		set the touched coordinate for 'getNext' function
		:param x: the coordinate x touched in board,ranging from 0 to rows-1
		:param y: the coordinate y touched in board,ranging from 0 to columns-1
		:return:
		"""
		self.new_coordinate = True
		self.x = x
		self.y = y

	def get_next(self, board: BoardSave):
		if not self.new_coordinate:
			return None
		self.new_coordinate = False
		return self.x, self.y

	@staticmethod
	def is_auto():
		return False
