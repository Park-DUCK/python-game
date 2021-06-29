# 이미지 표시
import tkinter
import random

def click_btn(): # 버튼 클릭 시 실행될 함수 정의
    label["text"] = random.choice(["대길", "중길", "소길", "흉"])
    # 라벨 문자열 무작위로 변경
 
    label.update() # 문자 변경 즉시 수행

root = tkinter.Tk()
root.title("제비뽑기 프로그램")
root.resizable(False, False) # 윈도우 크기 고정
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400, 300, image = gazou)

# GUI 배치
label = tkinter.Label(root, text="??",
font=("Times New Roman", 120), bg="white") # 라벨 컴포넌트 생성
label.place(x=380, y=60) # 라벨 배치

button = tkinter.Button(root, text="제비뽑기",
font=("Times New Roman", 36), fg="skyblue") # 버튼 컴포넌트 생성
button.place(x=360, y=400) # 버튼 배치

root.mainloop() # 윈도우 표시