# 과제 1 : 동물 종류를 한 줄에 하나씩 출력하도록 수정하기
# 과제 2 : 리스트에 있는 동물은 입력하지 못하도록 하기

animals = []
userInput = " "

print("animals 리스트를 만들어 봅시다.")
print("한 번에 하나씩 동물을 입력해주세요.")
print("입력을 끝내려면 빈 칸을 입력하세요.")

while userInput != "" :
    userInput = input("동물 이름을 입력해주세요 : ").strip()
    if len(userInput) > 0 and userInput not in animals:
        animals.append(userInput)
        print(animals) # 과제 1
    else :
        print("중복된 값을 입력하셨습니다. 프로그램을 종료합니다.")
        print(animals)
        break
        