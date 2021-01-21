import pyautogui
import tkinter
from tkinter import messagebox
import time
import threading
import random

# 전역변수 설정
operating = 0

window = tkinter.Tk()
window.title("SevenKnights2 Macro")
window.geometry("+950+500")
window.resizable(False, False)


first_f = tkinter.Frame(window)
# 매크로 과정을 데몬 프로세스로 실행 (tkinter 특성 상 어쩔 수 없는 선택..)
# 매크로를 종료하면 프로세스도 종료하기 위해서 데몬 프로세스로 설정


def demon_macro():
    global operating

    # t = random.randrange(1)
    t = 1

    print(t)

    time.sleep(10)

    pyautogui.keyDown('g')
    pyautogui.keyUp('g')  # 키보드를 누르고 있는 것을 해제

    time.sleep(3)

    pyautogui.keyDown('h')
    pyautogui.keyUp('h')  # 키보드를 누르고 있는 것을 해제

    time.sleep(3)

    pyautogui.keyDown('j')
    pyautogui.keyUp('j')  # 키보드를 누르고 있는 것을 해제

    time.sleep(2)

    pyautogui.keyDown('l')
    pyautogui.keyUp('l')

    time.sleep(3)

    pyautogui.keyDown('k')
    pyautogui.keyUp('k')  # 키보드를 누르고 있는 것을 해제 #확인 k

    time.sleep(5)

    pyautogui.keyDown('k')
    pyautogui.keyUp('k')  # 키보드를 누르고 있는 것을 해제 #확인 k #마우스 오른쪽버튼#아무거나 클릭

    while operating:

        t = random.randrange(100, 300)

        time.sleep(t)

        pyautogui.keyDown('h')
        pyautogui.keyUp('h')  # 키보드를 누르고 있는 것을 해제

        time.sleep(3)

        pyautogui.keyDown('j')
        pyautogui.keyUp('j')  # 키보드를 누르고 있는 것을 해제

        time.sleep(3)

        pyautogui.keyDown('l')
        pyautogui.keyUp('l')

        time.sleep(3)

        pyautogui.keyDown('k')
        pyautogui.keyUp('k')

        time.sleep(5)

        # 아무 키 입력

        pyautogui.keyDown('k')
        pyautogui.keyUp('k')

        time.sleep(5)

        pyautogui.keyDown('k')
        pyautogui.keyUp('k')

    print('end')

# 시작 버튼을 누르면 실행됨, 한번 누르는거만 적용되게 하려고 operating flag 사용


def do_macro():
    global operating
    if operating:
        messagebox.showinfo("오류", "이미 실행중!")
        return
    messagebox.showinfo("알림", "시작!")
    operating = 1
    d_process = threading.Thread(target=demon_macro)
    d_process.daemon = True
    d_process.start()

# 키보드 인터럽트나 종료 버튼을 누르면 operating flag를 0으로 클리어 한 후 매크로 프로세스 종료


def end_macro(event=None):
    global operating
    if operating == 0:
        messagebox.showinfo("알림", "아직 실행을 안했어유!")
        return
    operating = 0
    messagebox.showinfo("알림", "중지 됨!")


last = tkinter.Frame(window)
button2 = tkinter.Button(last, text='시작', width=13, height=2, command=do_macro)
button2.grid(row=0, column=1)
button3 = tkinter.Button(last, text='중지(x)', width=13,
                         height=2, command=end_macro)
button3.grid(row=0, column=2)
last.pack()

# 마우스 좌표 설정을 위한 이벤트 처리

window.bind('<x>', end_macro)
window.mainloop()
