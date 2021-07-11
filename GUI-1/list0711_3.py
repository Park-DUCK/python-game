# 캔버스 사용하기
import tkinter
root = tkinter.Tk()
root.title("첫 번째 캔버스")
canvas = tkinter.Canvas(root, width=400, height=600) # 캔버스 컴포넌트 생성 / width 폭 height 높이 bg 배경색
canvas.pack() # 윈도우에 캔버스 배치
gazou = tkinter.PhotoImage(file="hyunju.png") #2 gazou에 이미지 파일 로딩
canvas.create_image(200, 300, image=gazou) #2 캔버스에 이미지 그리기
root.mainloop() # 윈도우 표시
#.