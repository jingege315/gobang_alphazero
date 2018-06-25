from tkinter import *
from tkinter import messagebox as tk_message_box
from Helper import *

# main window
root = Tk()
# set the size of main window
root.geometry('700x700')
# create a canvas to draw board and chessman,and set the background of the canvas white
cv = Canvas(root, bg='white', width=600, height=600)
cv.pack()

window_size = WindowSize(10, 10, 590, 590)
board_size = BoardSize(15, 15)

gui = GuiTk(cv, callback_click=lambda x, y: gameController.set_click_event(x, y),
            window_size=window_size, board_size=board_size, theta=0.4, chess_radii=15)

player1 = PlayerHuman(Chess.BLACK)
player2 = PlayerHuman(Chess.WHITE)

game = Game(win_size=5, board_size=board_size, callback_win=lambda Chess: tk_message_box.showinfo('win', '%r' % Chess))

gameController = GameController(player1, player2, game, gui)

Button(root, text='back', command=gameController.back).pack()
Button(root, text='clear', command=gameController.clear).pack()

gameController.start()


def delete():
	gameController.stop()
	root.destroy()


root.protocol('WM_DELETE_WINDOW', delete)
root.mainloop()
