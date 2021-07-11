import tkinter
import random #2 랜덤 모듈 임포트

def click_btn():    #2 버튼 클릭 시 실행될 함수 정의
    label["text"] = random.choice(["대길", "중길", "소길", "흉"])
    label.update()

root = tkinter.Tk()
root.title("제비뽑기 프로그램")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400, 300, image=gazou)
label = tkinter.Label(root, text="??", font=("Times New Roman", 120), bg="White") # 라벨 컴포넌트 생성
label.place(x=380, y=60)
button = tkinter.Button(root, text="제비뽑기", font=("Times New Roman", 36), command=click_btn, fg="skyblue") # 버튼 컴포넌트 생성
button.place(x=360, y=400) # 버튼 배치
root.mainloop()
#.