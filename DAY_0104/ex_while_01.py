# ---------------------------------------------------------------
# 반복문 - 2 while 반복문
# - 반복의 횟수가 정해지지 않은 경우에 사용
# - 반복의 횟수가 정해진 경우에도 사용 가능함
# ---------------------------------------------------------------
# [ 요청 ]  사용자로부터 좋아하는 음식명을 입력 받아 주세요
#           => input()
#           단, 사용자가 종료라는 음식명 입력 전까지 입력 받으세요.
#           => 몇 번 입력 받아야 입력이 끝날지 알 수 없음
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# [ 요청 ]  사용자로부터 좋아하는 음식명을 입력 받아 주세요
#           => input()
#           단, Top 5 로 가장 좋아 하는 음식 5개만 입력 받으세요.
#           => 사용자의 Top5 음식명 출력
# ---------------------------------------------------------------
# foodlist = []
# for a in range(5):
#     food = input(f"가장 좋아하는 음식을 5개만 입력하세요: \n(현재 {a}개 입력)")
#     foodlist.append(food)
# print(foodlist)
#
# print('당신은 ', end='')
# for a in range(5):
#     print(foodlist[a],end=', ' if a != 4 else '')
# print(' 음식을 좋아하는군요')

debug = False       # Flag 변수
if debug:
    strfood = ''
    for a in range(5):
        food = input(f"가장 좋아하는 음식을 5개만 입력하세요: \n(현재 {a}개 입력)")
        strfood = strfood + food + (', ' if a != 4 else '')
    print(f'당신은 {strfood} 를 좋아하시는 군요')


# -------------------------------------------------------------------------------
# 기본 while 문법
# while 조건식:
# <--> 실행 코드
# <--> 실행 코드
# -------------------------------------------------------------------------------
# 타이머 프로그램 만들기 => 다운카운팅 : 10 9 8 7 ... 1
# -------------------------------------------------------------------------------


downCnt = 10
while downCnt > 0:              # while downcnt > 0
    print(downCnt)
    downCnt -= 1                # downCnt -= 1

# 타이머 프로그램 만들기 => 업카운팅 : 1 2 3 4 ... 10

upCnt = 1
while upCnt < 11:
    print(upCnt)
    upCnt += 1

# -------------------------------------------------------------------------------
# for in 반복으로 구현
# -------------------------------------------------------------------------------
# 다운 카운팅
import time
for a in range(10):
    print(f"다운 카운팅 {10 - a}초")
    time.sleep(0.5)

# 업 카운팅
for b in range(10):
    print(f"업 카운팅 {b + 1}초")
    time.sleep(0.5)




