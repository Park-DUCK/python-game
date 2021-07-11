import tkinter

def click_btn():
    button["text"] = "클릭했습니다" #2 함수 선언 버튼 문자열 생성

root = tkinter.Tk() # 윈도우 객체 생성
root.title("첫 번째 버튼") # 윈도우 제목 지정
root.geometry("800x600") # 윈도우 크기 지정

button = tkinter.Button(root, text="클릭하십시오",
font=("Times New Roman", 24), # 버튼 컴포넌트 생성
command = click_btn) #2 command=로 클릭 시 동작할 함수 지정

button.place(x=200, y= 100) # 윈도우에 버튼 배치
root.mainloop() # 윈도우 표시 