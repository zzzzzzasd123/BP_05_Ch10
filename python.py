@1번
from tkinter import*


window=Tk()


l1= Label(window,text="간단한GUI프로그램!")
l1.grid(row=0,column=0)


b1=Button(window,text="환영합니다.")
b2=Button(window,text="종료")


b1.grid(row=2,column=0)
b2.grid(row=3,column=0)


window.mainloop()
@2번
from tkinter import*


window=Tk()


total=0
a=0
def c1():#더하기 함수 정의
b=int(e1.get())


total=a+b
l2["text"]=str(total)
global a
a=total
return


def c2():#빼기 함수 정의
b=int(e1.get())


total=a-b
l2["text"]=str(total)
global a
a=total
return
def c3(): #초기화 함수 정의


l2["text"]=str(0)
#-------상단 라벨 생성--------------
l1= Label(window,text="현재 합계")
l1.grid(row=0,column=0)
l2= Label(window,text=str(total))


l2.grid(row=0,column=1)


e1=Entry(window)
e1.grid(row=1)


#-------하단 버튼 생성------------
b1=Button(window,text="더하기(+)",command=c1)
b2=Button(window,text="빼기(-)",command=c2)
b3=Button(window,text="초기화",command=c3)


b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)


window.mainloop()
@3번
from tkinter import*
import random
window=Tk()
r=random.randint(0,100)
total=0
a=0
def c1():#게임 룰 함수 정의
b=int(e1.get())
if b==r:
l1["text"]="정답입니다!"
elif b>r:
l1["text"]="너무 높아요!"
else:
l1["text"]="너무 낮아요!"




def c2():#초기화 함수 정의
global r
r=random.randint(0,100)
return


#-------상단 라벨 생성--------------
l1= Label(window,text="즐거운 숫자 게임")
l1.grid(row=0,column=0)


e1=Entry(window)
e1.grid(row=1)


#-------하단 버튼 생성------------
b1=Button(window,text="숫자를 입력",command=c1)
b2=Button(window,text="게임을 다시시작",command=c2)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)


window.mainloop()
@4번
from tkinter import*


def process1(): #변환 함수 정의


t1=float(e1.get())
myt=t1*2.54 #인치 변환식
l3["text"]=str(myt)+"센티미터" #변환된 수를 표


window=Tk()
#-------상단 라벨 생성--------------
l1= Label(window,text="인치를 센티미터로 변환하는 프로그램")
l1.grid(row=0,column=0)


l2= Label(window,text="인치를 입력하시오:")
l2.grid(row=0,column=1)


l3= Label(window,text="변환 결과:")
l3.grid(row=2,column=0)


l3= Label(window,text="센티미터")
l3.grid(row=2,column=1)


#------입력부분 생성------------
e1=Entry(window)
e1.grid(row=0,column=1)


#-------하단 버튼 생성------------


b1=Button(window,text="변환!",command=process1)
b1.grid(row=2,column=2)


window.mainloop()
@5번from tkinter import*


window=Tk()
#-------상단 라벨 생성--------------
l1= Label(window,text="이름")
l2= Label(window,text="직업")
l3= Label(window,text="국적")


# 격자배열을 통해 1행에 배치
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)


#------입력부분 생성------------
e1=Entry(window)
e2=Entry(window)
e3=Entry(window)


# 격자배열을 통해 2행에 배치
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)


#-------하단 버튼 생성------------
b1=Button(window,text="Show")
b2=Button(window,text="Quit")


# 격자배열을 통해 3열에 배치
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)


window.mainloop()
