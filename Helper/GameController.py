import threading
import time

from Game import Game
from Player import Player


class GameController(object):
	"""
	control the drawing logic of gobang and the move of player1 and player2 whether human player or AI player
	"""

	def __init__(self, player_black: Player, player_white: Player, game: Game):
		self.player_black = player_black
		self.player_white = player_white
		self.game = game

	def _start(self):
		while not self.game._isWin():
			if self.game.now_black:
				ret = self.player_black.getNext(self.game.boardSave)
			else:
				ret = self.player_white.getNext(self.game.boardSave)
			if ret is None:
				time.sleep(0.01)
				continue
			x, y = ret
			self.game._move(x, y)
		self.game.isWin()

	def start(self):
		self.thread = threading.Thread(target=self._start)
		self.thread.start()
