from Helper import *


def callback_win(chess):
	print(game.board)
	print('%r' % chess)


board_size = BoardSize(15, 15)

game = Game(win_size=5, board_size=board_size, callback_win=callback_win)

valuablePoint = ValuablePointLinear()
evaluate = EvaluateNormal()
player1 = PlayerAISingleStep(Chess.BLACK, valuablePoint, evaluate)

valuablePoint = ValuablePointLinear()
evaluate = EvaluateNormal2()
player2 = PlayerAISingleStep(Chess.WHITE, valuablePoint, evaluate)

gameController = GameController(player1, player2, game, gui=None)

for i in range(3):
	gameController.start_no_thread()
