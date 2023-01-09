# 하드 코딩을 예방하는 방법
import random

guesses = 0
numMin = 1
numMax = 100
userInput = ""
userGuess = 0

randNum = random.randrange(numMin, numMax + 1)

print(numMin, "~", numMax, "사이의 숫자가 지정됐습니다.\n이 숫자는 무엇일까요?")

while randNum != userGuess :
    userInput = input("숫자를 입력해주세요.\n").strip()
    if not userInput.isnumeric() :
        print(userInput, "은 숫자가 아닙니다. 다시 입력해주세요.")
    else :
        guesses = guesses + 1
        userGuess = int(userInput)

        if userGuess < numMin or userGuess > numMax :
            print(userGuess, "은", numMin, numMax, "사이의 숫자가 아닙니다.")
        elif randNum == userGuess :
            print("정답을 맞혔습니다. 게임을 종료합니다.")
            print("총 시도 횟수는", guesses, "회 입니다.")
        elif randNum > userGuess :
            print("숫자가 작습니다. 다시 입력해주세요.")
        else :
            print("숫자가 너무 큽니다. 다시 입력해주세요.")