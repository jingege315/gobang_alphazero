import BoardSave
from Player import Player


class PlayerHuman(Player):
	def __init__(self):
		self.new = None
		self.x = None
		self.y = None

	def setTouchCoordinate(self, x, y):
		self.new = True
		self.x = x
		self.y = y

	def getNext(self, boardSave:BoardSave):
		if not self.new:
			return None
		self.new = False
		return self.x, self.y
