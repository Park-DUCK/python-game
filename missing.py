import random
import datetime #4 datetime 모듈 임포트
ALP = [
"A", "B", "C", "D", "E", "F", "G", # 리스트로 알파벳 정의
"H", "I", "J", "K", "L", "M", "N",
"O", "P", "Q", "R", "S", "T", "U",
"V", "W", "X", "Y", "Z"]
r = random.choice(ALP) #2 빠질 문자를 무작위로 결정
alp = ""    #2 변수 alp 선언 (상자안은 비어있다)

for i in ALP:
    if i != r: #2 i가 빠질 문자가 아니라면
        alp = alp + i #2 변수 alp에 알파벳 추가
print(alp)
st = datetime.datetime.now() #4 날짜와 시간을 변수 st에 대입
ans = input("빠진 알파벳은?") #3 input()으로 입력받아 변수 ans에 대입
if ans == r:    #3 맞으면
    print("정답입니다")
    et = datetime.datetime.now() #4 새로운 날짜와 시간을 변수 et에 대입
    print(str((et - st).seconds) + "초 걸렸습니다") #4, 5 st와 et의 차를 초 단위로 출력
else:           #3 아니면
    print("틀렸습니다")