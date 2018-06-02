from tkinter import *
from tkinter import messagebox as tkMessageBox

from Helper.Controller import Controller
from Helper.GUIHelper2 import GUIHelper2
from Helper.Judge import Judge

# main window
# 主窗口
root = Tk()
# set the size of main window
# 界面大小
root.geometry('500x500')
# create a canvas to draw board and chessman,and set the background of the canvas white
# 画布，画布颜色白色
cv = Canvas(root, bg='white', width=400, height=400)
cv.pack()

helper = GUIHelper2(cv, 10, 10, 390, 390, lambda x, y: controller.move(x, y),theta=0.4)
judge = Judge(15, 15, win_size=5)
controller = Controller(helper, judge, callback_win=lambda x, y, winCondition, isBlack: tkMessageBox.showinfo(
	'win', 'x=%r,y=%r,winCondition=%r,isBlack=%r' % (x, y, winCondition, isBlack)))
Button(root, text='back', command=controller.back).pack()
Button(root, text='clear', command=controller.clear).pack()

root.mainloop()
