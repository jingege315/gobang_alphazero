from ..BoardSave import BoardSave


class ValuablePoint(object):
	"""
	get the valuable points in the board
	"""

	def getPoints(self, boardSave: BoardSave, player_me):
		"""

		:param boardSave:
		:param player_me:
		:return: the valuable points
		"""
		raise NotImplementedError()
