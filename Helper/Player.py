from BoardSave import BoardSave


class Player(object):
	"""
	the player can use the information of board and order to decide how to move in next step
	"""
	def getNext(self, boardSave:BoardSave):
		"""
		the player can use the information of board and order to decide how to move in next step
		:param boardSave:
		:return: 	the move about next step,return (x,y)
					if waiting,return None
		"""
		raise NotImplementedError()
