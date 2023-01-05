import random

animals = ["사자", "호랑이", "고래", "돌고래", "문어", "지렁이"]
adjectives = ["귀여운", "죽은", "생동감이 넘치는", "아프리카에 살고 있는"]


animalChoice = random.choice(animals)
adjectiveChoice = random.choice(adjectives)

print("저에게는", adjectiveChoice, animalChoice + "가 있습니다.")