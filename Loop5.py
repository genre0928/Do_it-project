animals = []
userInput = " "

print("animals 리스트를 만들어 봅시다.")
print("한 번에 하나씩 동물을 입력해주세요.")
print("입력을 끝내려면 빈 칸을 입력하세요.")

while userInput != "" :
    userInput = input("동물 이름을 입력해주세요 : ").strip()
    if len(userInput) > 0 :
        animals.append(userInput)

animals.sort()
print(animals)