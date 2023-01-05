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