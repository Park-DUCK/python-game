import random #랜덤 모듈 임포트
pl_pos = 1
com_pos = 1
def board():
    print("·" * (pl_pos - 1) + "P" + "·" * (30-pl_pos) + "Goal")
    print("·" * (com_pos - 1) + "C" + "·" * (30-com_pos) + "Goal")

board() #함수호출
print("주사위 게임, 스타트!")
while True:
    input("Enter를 누르면 여러분의 말이 움직입니다") #입력대기
    pl_pos = pl_pos + random.randint(1, 6) #난수만큼 옮김
    if pl_pos > 30: #P 위치가 30을 넘으면
        pl_pos = 30 #말 위치를 30으로 함
    board()
    if pl_pos == 30: #도달하면
        print("여러분이 승리했습니다!")
        break #반복 중단
    input("Enter를 누르면 컴퓨터의 말이 움직입니다.")
    com_pos = com_pos + random.randint(1, 6)
    if com_pos > 30:
        com_pos = 30
    board()
    if com_pos == 30:
        print("컴퓨터가 승리했습니다!")
        break