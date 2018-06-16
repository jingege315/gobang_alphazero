import threading
import time

from .BoardSave import BoardSave
from .Game import Game
from .Player import Player


class GameController(object):
	"""
	control the drawing logic of gobang and the move of player1 and player2 whether human player or AI player
	"""

	def __init__(self, player_black: Player, player_white: Player, game: Game):
		self.player_black = player_black
		self.player_white = player_white
		self.game = game
		self.thread = None
		self.exit = False

	def _start(self):
		while not self.game._isWin():
			if self.exit:
				return
			if self.game.now_black:
				ret = self.player_black.getNext(self.game.boardSave, BoardSave.black)
			else:
				ret = self.player_white.getNext(self.game.boardSave, BoardSave.white)
			if ret is None:
				time.sleep(0.01)
				continue
			x, y = ret
			self.game._move(x, y)
		self.game.isWin()

	def start(self):
		if self.thread is None or not self.thread.isAlive():
			self.thread = threading.Thread(target=self._start)
			self.thread.start()

	def stop(self):
		self.exit = True

	def back(self):
		if self.player_black.isAuto() and self.player_white.isAuto():
			return
		if self.game.now_black and self.player_white.isAuto():
			self.game.back2steps()
		elif not self.game.now_black and self.player_black.isAuto():
			self.game.back2steps()
		else:
			self.game.back()
		self.start()

	def clear(self):
		self.game.clear()
		self.start()
