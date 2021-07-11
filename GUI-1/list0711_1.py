import tkinter
root = tkinter.Tk() # 윈도우 객체 생성
root.title("첫 번째 라벨") # 윈도우 제목 지정
root.geometry("800x600") # 윈도우 크기 지정
label = tkinter.Label(root, text="라벨 문자열", font=("System",24)) # 라벨 컴포넌트 생성
label.place(x=200, y= 100) # 윈도우에 라벨 배치
root.mainloop() # 윈도우 표시
#.