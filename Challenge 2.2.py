print("단어 채우기 게임에 오신 것을 환영합니다.")
name = input("주인공의 이름을 설정해주세요. : ")

print("\n입력하신 이름은 " + name + "입니다.")
print("지금부터 게임을 시작하겠습니다. 총 15개의 단어를 중복되지 않도록 입력해주세요.")

itemList = []
for i in range(1, 16) :
    item = input(str(i) + "번째 단어를 입력해주세요. : ") # i번째 단어라는 문구를 추가하기!!
    if item not in itemList :
        itemList.append(item)
        print(itemList)

    else :
        print("중복된 단어를 입력하였습니다. 게임을 종료합니다.")
        break

print("\n게임이 정상적으로 끝났습니다. 고생하셨습니다.")