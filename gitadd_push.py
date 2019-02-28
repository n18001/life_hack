#!/usr/bin/python3


# gitのadd commit pushを一気にやるよ
# pyautoguiを入れてね
#
# 初期化とかは自分でやってほしいよ
# commitは年月日でするよ
import pyautogui as gui
from datetime import datetime


# git add
gui.typewrite('git add .', 0.05)
gui.press('enter')


# git commit
today = datetime.now().strftime('%Y%m%d')
gui.typewrite("git commit -m '{}'".format(today), 0.05)
gui.press('enter')


# git push
gui.typewrite('git push origin master', 0.05)
gui.press('enter')


# 気持ち悪い動作だよ
# 綺麗に書くにはどうしたら良いんだよ
