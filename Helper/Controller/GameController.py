import threading
import time
import numpy
from ..Player import *
from .Game import Game
from .GuiBase import GuiBase


class GameController(object):
	"""
	control the drawing logic of gobang and the move of player1 and player2 whether human player or AI player
	"""

	def __init__(self, player1: Player, player2: Player, game: Game, gui: GuiBase):
		assert player1.get_chess_color() != player2.get_chess_color()
		if player1.get_chess_color().is_black():
			self._player = {Chess.BLACK: player1, Chess.WHITE: player2}
		else:
			self._player = {Chess.BLACK: player2, Chess.WHITE: player1}
		self._game = game
		self._gui = gui
		self._thread = None
		self._exit = False

	def _move(self, x, y):
		if self._gui is not None:
			self._gui.draw_chess(ChessLocation(x, y, self._game.get_chess_now()))
		self._game.move(x, y)

	def _function(self):
		"""
		the function keep game proceed
		"""
		while not self._game.is_win() or self._exit:
			ret = self._player[self._game.get_chess_now()].get_next(self._game.board)
			if ret is None:
				time.sleep(0.01)
				continue
			x, y = ret
			self._move(x, y)
		self._game.is_win()
		self.stop()

	def start(self):
		self._refresh()
		self._exit = False
		if self._thread is None or not self._thread.isAlive():
			self._thread = threading.Thread(target=self._function)
			self._thread.start()

	def _refresh(self):
		if self._gui is None:
			return
		self._gui.clear()
		self._gui.draw_board()
		self._gui.draw_chesses(self._game.board.get_order())

	def start_no_thread(self):
		self._function()

	def stop(self):
		self._exit = True

	def is_stop(self):
		return self._exit

	def back(self):
		if self._player[self._game.get_chess_now().exchange()].is_auto():
			self._game.back2steps()
		else:
			self._game.back()

		# refresh
		if self.is_stop():
			self.start()
		else:
			self._refresh()

	def clear(self):
		self._game.clear()
		self._refresh()
		# refresh
		if self.is_stop():
			self.start()
		else:
			self._refresh()

	def _need_draw_scores(self)->bool:
		return isinstance(self._player[self._game.get_chess_now().exchange()], PlayerAI)

	def _draw_scores(self):
		"""
		try to draw the scores's context to screen
		:return: success to get the scores in AI player
		"""
		player = self._player[self._game.get_chess_now().exchange()]
		if isinstance(player, PlayerAI):
			scores = player.get_scores()
			for chess_score in scores:
				x, y, score = chess_score.x, chess_score.y, chess_score.score
				if score == numpy.infty:
					self._gui.draw_text(x, y, 'inf')
				else:
					self._gui.draw_text(x, y, '%d' % score)

	def set_click_event(self, x, y):
		"""
		allocate the click event to human player
		"""
		player = self._player[self._game.get_chess_now()]
		if isinstance(player, PlayerHuman):
			player.set_touched_coordinate(x, y)
