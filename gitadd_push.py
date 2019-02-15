#!/usr/bin/python3


# gitのadd commit pushを一気にやるよ
# 初期化とかは自分でやってほしいよ
# commit は日付でするよ
import pyautogui as gui





# git add
gui.typewrite('git add -u', 0.1)
gui.press('enter')


# git commit
comment = input('comment :')
gui.typewrite("git commit -m '{}'".format(comment), 0.1)
gui.press('enter')


# git push
gui.typewrite('git push origin master', 0.1)
gui.press('enter')
