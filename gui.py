from tkinter import*
import random


def ch1(): #사용자가 가위를 골랐을경우


img=PhotoImage(file="p1.gif")
imageLabel.configure(image=img)
imageLabel.image=img


r=random.randint(0,2) #컴퓨터의 선택에 따른 사진 변화
if r==0:
img=PhotoImage(file="p1.gif")
imageLabel2.configure(image=img)
imageLabel2.image=img
l2["text"]="비겼습니다!"#컴퓨터의 선택에 따른 문장(승부) 변화
elif r==1:
img=PhotoImage(file="p2.gif")
imageLabel2.configure(image=img)
imageLabel2.image=img
l2["text"]="졌습니다ㅠㅠ"
else:
img=PhotoImage(file="p3.gif")
imageLabel2.configure(image=img)
imageLabel2.image=img
l2["text"]="이겼습니다!!"


def ch2(): #사용자가 바위를 골랐을경우


img=PhotoImage(file="p2.gif")
imageLabel.configure(image=img)
imageLabel.image=img


r=random.randint(0,2) #컴퓨터의 선택에 따른 사진 변화
if r==0:
img=PhotoImage(file="p1.gif")
imageLabel2.configure(image=img)
imageLabel2.image=img
l2["text"]="이겼습니다!!" #컴퓨터의 선택에 따른 문장(승부) 변화
elif r==1:
img=PhotoImage(file="p2.gif")
imageLabel2.configure(image=img)
imageLabel2.image=img
l2["text"]="비겼습니다!"
else:
img=PhotoImage(file="p3.gif")
imageLabel2.configure(image=img)
imageLabel2.image=img
l2["text"]="졌습니다"


def ch3(): #사용자가 보를 골랐을경우


img=PhotoImage(file="p3.gif")
imageLabel.configure(image=img)
imageLabel.image=img


r=random.randint(0,2) #컴퓨터의 선택에 따른 사진 변화
if r==0:
img=PhotoImage(file="p1.gif")
imageLabel2.configure(image=img)
imageLabel2.image=img
l2["text"]="졌습니다ㅠㅠ"#컴퓨터의 선택에 따른 문장(승부) 변화
elif r==1:
img=PhotoImage(file="p2.gif")
imageLabel2.configure(image=img)
imageLabel2.image=img
l2["text"]="이겼습니다!!"
else:
img=PhotoImage(file="p3.gif")
imageLabel2.configure(image=img)
imageLabel2.image=img
l2["text"]="비겼습니다!"
window=Tk()
#------------라벨 생성------------
l1= Label(window,text=" >>>>>>> ",font=("Gothic",30))
l2= Label(window,text="승리는 누구??",font=("Gothic",30))


l1.grid(row=0,column=1)
l2.grid(row=1,column=1)


#------------그림 생성-------------


photo=PhotoImage(file="p1.gif")
imageLabel=Label(window,image=photo)
imageLabel.grid(row=0,column=0)


photo2=PhotoImage(file="p1.gif")
imageLabel2=Label(window,image=photo)
imageLabel2.grid(row=0,column=2)
#------------버튼 생성-------------


b1=Button(window,text="가위",command=ch1)
b2=Button(window,text="바위",command=ch2)
b3=Button(window,text="보",command=ch3)


b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)


window.mainloop()
