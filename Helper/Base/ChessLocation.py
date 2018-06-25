from .Chess import Chess


class ChessLocation(object):
	def __init__(self, x: int, y: int, chess: Chess):
		self.x = x
		self.y = y
		self.chess = chess
