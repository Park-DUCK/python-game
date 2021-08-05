import tkinter

def click_btn(): #2 버튼 클릭시 실행되는 함수 정의
    txt = entry.get() #2 입력 필드의 문자열을 변수 txt에 대입
    button["text"] = txt #2 버튼의 문자열에 txt의 값을 대입

root = tkinter.Tk()
root.title("첫번째 텍스트 입력 필드")
root.geometry("400x200")
entry = tkinter.Entry(width=20) #20 문자 크기 입력 필드 컴포넌트 생성
entry.place(x=20, y=20) #윈도우에 입력 필드 컴포넌트 배치

button = tkinter.Button(text="문자열 얻기", command=click_btn) #2 버튼 컴포넌트 생성, command=로 클릭시 실행할 함수 지정
button.place(x=20, y=100)
root.mainloop()