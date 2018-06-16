from BoardSave import BoardSave
from AI.ValuablePoint import ValuablePoint


class ValuablePointLinear(ValuablePoint):
	"""
	regard the point surrounding with a point which has moved as a valuable point
	"""

	def getPoints(self, boardSave: BoardSave, player_me):
		points = []

		def isLegal(x, y):
			shift = (
				(-1, -1), (-1, 0), (-1, 1),
				(0, -1), (0, 1),
				(1, -1), (1, 0), (1, 1),
			)
			if not boardSave.isNone(x,y):
				return False
			for x_theta, y_theta in shift:
				x_ = x + x_theta
				y_ = y + y_theta
				if boardSave.isLegalPoint(x_, y_) and not boardSave.isNone(x_, y_):
					return True
			return False

		for x, y in boardSave.iterBoardPoint():
			if isLegal(x, y):
				points.append((x, y))
		return points
