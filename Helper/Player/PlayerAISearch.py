from ..AI import *
from .PlayerAI import PlayerAI


class PlayerAISearch(PlayerAI):
	def __init__(self, chess_self: Chess, search: Search):
		super().__init__(chess_self)
		self.search = search

	def get_next(self, board: BoardSave):
		return self.search.get_next(board, self._chess_self)

	def get_scores(self):
		return self.search.get_last_scores()
