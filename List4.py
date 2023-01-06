animals = ["개", "개미", "고양이", "박쥐", "장어"]

print(len(animals), "종류의 동물이 리스트에 있습니다.")
animals.append("여우")
print(len(animals), "종류의 동물이 리스트에 있습니다.")

list2 = ["염소", "이구아나", "하마"]

animals.extend(list2)
print(animals)

animals.pop(0)
print(animals)

animals.remove("장어")
print(animals)