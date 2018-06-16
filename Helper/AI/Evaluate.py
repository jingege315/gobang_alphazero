from BoardSave import BoardSave


class Evaluate(object):
	"""
	to evaluate the score in coordinate(x,y) about player_me
	"""

	def getValue(self, boardSave: BoardSave, x, y, player_me):
		raise NotImplementedError()
