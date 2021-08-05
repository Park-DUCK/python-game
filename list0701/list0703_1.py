import tkinter
import tkinter.messagebox #4 tkinter.messagebox 모듈 임포트

# def check(): #3 체크 버튼 클릭시 실행하는 함수 정의
    if cval.get() == True:
        print("체크되어 있습니다")
    else:
        print("체크되어 있지 않습니다")

root = tkinter.Tk()
root.title("처음부터 체크된 상태 만들기")
root.geometry("400x200")

cval = tkinter.BooleanVar() #2 BooleanVar() 객체 준비
cval.set(True) #2 객체 True 설정 - 체크 상태

cbtn = tkinter.Checkbutton(text="체크 버튼", variable=cval, command=check)
cbtn.pack()
root.mainloop()