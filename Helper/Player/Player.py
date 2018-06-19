from ..BoardSave import BoardSave


class Player(object):
	"""
	the player can use the information of board and order to decide how to move in next step
	"""

	def __init__(self):
		self.isBlack = None

	def getNext(self, boardSave: BoardSave, player_me):
		"""
		the player can use the information of board and order to decide how to move in next step
		:param boardSave:
		:param player_me:
		:return: 	the move about next step,return (x,y)
					if waiting,return None
		"""
		raise NotImplementedError()

	@staticmethod
	def isAuto():
		"""
		whether the player is auto to move
		:return:
		"""
		raise NotImplementedError()

	def MoveFinish(self, boardSave: BoardSave):
		"""
		after using 'getNext' function moving successfully and _move(x,y) the point getNext return ,
		this function will be callback to draw something and so on.
		:param boardSave:
		:return:
		"""
		pass
