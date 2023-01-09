# 특정 범위의 숫자 맞히기 게임
# 사용자는 업다운으로 힌트를 얻음
# 총 시도 횟수 출력

import random

userInput = ""
userGuess = 0
i = 1
randNum = random.randrange(1, 101)

print("숫자 맞히기 게임을 시작하겠습니다.")

while randNum != userGuess :
    userInput = input("예상 숫자 : ").strip()
    
    if not userInput.isnumeric() :
        print("입력한 값 " + str(userInput) + "은 숫자가 아닙니다.")
    else :
        userGuess = int(userInput)
    
    if randNum == userGuess :
        print("축하합니다. 정답을 맞추셨습니다. 게임을 종료합니다.")
        print(f"총 {i}회 게임을 진행하셨습니다")
    elif randNum > userGuess :
        print("너무 작습니다. 다시 입력해주세요.")
        i = i + 1
    else :
        print("너무 큽니다. 다시 입력해주세요.")
        i = i + 1