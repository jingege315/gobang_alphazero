from . import Player
from ..Base import *


class PlayerAI(Player):
	def __init__(self, chess_self: Chess):
		super().__init__(chess_self)

	@staticmethod
	def is_auto():
		return True

	def get_scores(self) -> list:
		"""
		:return: after calling 'getNext' function,the scores in each point considered
		"""
		raise NotImplementedError()
