import tkinter

def click_btn():
    text.insert(tkinter.END, "몬스터가 나타났다!")

root = tkinter.Tk()
root.title("여러 행 텍스트 입력")
root.geometry("400x200")
button = tkinter.Button(text="메세지", command=click_btn)
button.pack() #버튼 배치

text = tkinter.Text() #여러 행 텍스트 입력 필드 컴포넌트 생성
text.pack() #입력 필드 컴포넌트 배치
root.mainloop()