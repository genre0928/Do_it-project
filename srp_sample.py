import random

resStr = ["승리했습니다!!", "패배했습니다!!"]
selStr = ["가위", "바위", "보"] # 명칭 통일할거임

def checkwin(user, com) : #승패를 체크하는 함수 / 0은 유저 승, 1은 컴퓨터 승, 2는 비김
    if user == com : # 비김
        return 2
    elif user == 0 and com == 1 :  # 가위, 바위 컴 승
        return 1
    elif user == 1 and com == 2 : # 바위, 보 컴 승
        return 1
    elif user == 2 and com == 0 : # 보, 가위 컴 승
        return 1
    else :
        return 0 # 유저 승

def checkUser(user) : # user 입력의 정확도 체크
    if user < 0 or user > 2 :
        print("잘못 입력하였습니다. 다시 입력하세요 / 가위(0), 바위(1), 보(2)")
        return False
    return True

# 게임 시작
print("선공을 정하겠습니다. 가위 바위 보를 선택해주세요.\n")
result = 0
while True :
    user = int(input("가위(0), 바위(1), 보(2)를 선택하세요.\n"))
    if checkUser(user) :
        com = random.randint(0, 2)
         # 리스트안에 두 개의 리스트가 있을 때 첫 [] = 몇 번째 리스트인 지 / 두 번째 [] = 선택한 리스트 안에서 몇 번째 위치하는 지
        print(f"<결과>\n유저 : {selStr[user]} vs 컴퓨터 : {selStr[com]}")
        result = checkwin(user, com) # 승패 체크
        if result == 2 :
            print("비겼습니다. 가위 바위보를 다시 진행합니다.")
        else :
            break


print("묵찌빠 게임을 시작합니다.")
attack = 0
while True :
    print() # 공백
    # if result == 0 :
    #     print("[공격하세요] : ", end="")
    #     attack = 0
    # elif result == 1 :
    #     print("[수비하세요] : ", end="")
    #     attack = 1
    # else :
    #     print("[다시하세요] : ", end="")
    ad = ["[공격하세요] : ", "[수비하세요] : "] # 접두사를 리스트로 만들었음(어차피 숫자로 리턴하니까 이런 경우면 리스트도 괜찮은 듯)
    print(ad[result], end="")
    user = int(input("가위(0), 바위(1), 보(2)를 선택하세요 : ")) # 앞에 접두사 선택 후에
    com = random.randint(0, 2)
    print(f"결과 => 사용자 {selStr[user]}, 컴퓨터 {selStr[com]}")

    result = checkwin(user, com)

    if result == 2 :
        print(resStr[attack])
        break

    if attack == 0 : # 0은 유저 승, 1은 컴퓨터 승
        if result == 1 :
            attack = 1
    else :
        if result == 0 :
            attack = 0