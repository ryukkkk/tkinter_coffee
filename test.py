import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def answer2selection(event=None):
    funcN = tk.Entry.get(textN)
    funcK = tk.Entry.get(textK)
    answer = int(funcK)/int(funcN)
    hInfo.config(text = f'최대 {int(answer)}잔을 교환할 수 있습니다.',font =('',30), fg='red')
    textN.config(state = 'disabled')
    textK.config(state = 'disabled')
    hBtn.config(state = 'normal')
    answerBtn.config(state = 'disabled')

def doAgain(event=None):
    hInfo.config(text = '')
    hBtn.config(state='disabled')
    textN.config(state = 'normal')
    textK.config(state = 'normal')
    textN.delete(0,len(tk.Entry.get(textN)))
    textK.delete(0,len(tk.Entry.get(textK)))
    answerBtn.config(state='normal')
    v.set(-1)


correctChoice = 0

hw = tk.Tk()
hw.title("AI-STREAM assignment")


pil_image = Image.open('ama.png')
pil_image = pil_image.resize((120, 160), Image.ANTIALIAS)

wall = ImageTk.PhotoImage(pil_image)
wall_label = Label(image = wall)
wall_label.place(x=0,y=0)
wall_label.pack()

hQuestion = tk.Label(hw, font=('', 14), text='''유경 선생님은 아메리카노를 매우 좋아한다.
유경 선생님의 단골 커피 전문점에서는 아메리카노를 한 잔 주문할 때마다 쿠폰을 하나 받을 수 있다.
이 쿠폰은 커피 전문점에서 정한 개수(N)가 되면 아메리카노 한 잔과 쿠폰 한 장으로 교환할 수 있다.
유경 선생님이 가진 쿠폰의 개수(K)와 커피 전문점에서 정한 아메리카노 교환에 필요한 쿠폰 개수(N)가 입력되면
선생님이 교환할 수 있는 아메리카노의 최대 잔 수를 구하시오.''')
hQuestion.pack()

numN = tk.Label(hw, text='<<Input N>>', font=('', 20))
numN.pack()
textN = tk.Entry(hw)
textN.pack()
numK = tk.Label(hw, text='<<Input K>>', font=('', 20))
textK = tk.Entry(hw)
numK.pack()
textK.pack()

answerBtn = tk.Button(hw,text = 'CALC',width = 15, command = answer2selection)
answerBtn.pack()

hInfo = tk.Label(hw, font=('', 14), text='')
hInfo.pack()

v = tk.IntVar()
v.set(-1)

hBtn = tk.Button(hw, text='Do Again', command=doAgain, font=('', 14),
                 state='disabled')
hBtn.pack()

doAgain()
hw.mainloop()
