import random

# 가위바위보 게임 프로그래밍 하기(이거는 내가 만들어보기)
tools = ["가위", "바위", "보"]

computer = random.choice(tools)
user = random.choice(tools)
notice = print("결과는 컴퓨터 : " + computer + " / 유저 : " + user + "입니다.")
if computer == user :
    print("비겼습니다. 승부를 종료합니다.")
else :
    if computer == "가위" :
        if user == "보" :
            notice
            print("컴퓨터가 승리하였습니다.")
        else :
            notice
            print("유저가 승리하였습니다.")
    elif computer == "바위" :
        if user == "가위" :
            notice
            print("컴퓨터가 승리하였습니다.")
        else :
            notice
            print("유저가 승리하였습니다.")
    else :
        if user == "묵" :
            notice
            print("컴퓨터가 승리하였습니다.")
        else :
            notice
            print("유저가 승리하였습니다.")
print("─────────────────────────────────────")
# 강의대로 해보기

print("가위, 바위, 보?")
name = input("당신의 이름은 무엇인가요? ")
print("안녕하세요, " + name + "님 저와 가위바위보 게임 한 번 하시겠습니까?")
uChoice = input("S(가위), R(바위), P(보) 중 하나를 고르세요 : ").upper().strip()
# 치트키
if name == "선우" :
    if uChoice == "R" :
        cChoice = "S"
    elif uChoice == "P" :
        cChoice = "R"
    elif uChoice == "S" :
        cChoice = "P"
else :
    cChoice = random.choice("SRP")


# print("여러분 : " + uChoice)
# print("컴퓨터 : " + cChoice)

if cChoice == uChoice :
    print("무승부입니다.")
elif uChoice == "R" and cChoice == "P" :
    print("여러분이 고른 것은 " + uChoice + ", 컴퓨터가 고른 것은 " + cChoice + ". 여러분이 이겼습니다.")
elif uChoice == "R" and cChoice == "S" :
    print("여러분이 고른 것은 " + uChoice + ", 컴퓨터가 고른 것은 " + cChoice + ". 여러분이 졌습니다.")
elif uChoice == "P" and cChoice == "R" :
    print("여러분이 고른 것은 " + uChoice + ", 컴퓨터가 고른 것은 " + cChoice + ". 여러분이 이겼습니다.")
elif uChoice == "P" and cChoice == "S" :
    print("여러분이 고른 것은 " + uChoice + ", 컴퓨터가 고른 것은 " + cChoice + ". 여러분이 졌습니다.")
elif uChoice == "S" and cChoice == "P" :
    print("여러분이 고른 것은 " + uChoice + ", 컴퓨터가 고른 것은 " + cChoice + ". 여러분이 이겼습니다.")
elif uChoice == "S" and cChoice == "R" :
    print("여러분이 고른 것은 " + uChoice + ", 컴퓨터가 고른 것은 " + cChoice + ". 여러분이 졌습니다.")
else :
    print("게임 설명을 더 듣기는 지겨우시죠?")
