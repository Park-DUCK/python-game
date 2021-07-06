import random #랜덤 모듈 임포트
pl_pos = 1
com_pos = 1
def board():
    print("·" * (pl_pos - 1) + "P" + "·" * (30-pl_pos))
    print("·" * (com_pos - 1) + "C" + "·" * (30-com_pos))
while True:
    board()
    input("Enter를 누르면 말이 움직입니다") #입력대기
    pl_pos = pl_pos + random.randint(1, 6) #난수만큼 옮김
    com_pos = com_pos + random.randint(1, 6)
