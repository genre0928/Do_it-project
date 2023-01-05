import random

# 1단계
# choices = "HT"
# coinToss = random.choice(choices)

# print(coinToss, "입니다.")

# 2단계
# choices = "앞면뒷면"
choices = ["앞면", "뒷면"] # 단어를 랜덤으로 선택할 때는 변수를 리스트로 만들어줘야 함
coinToss = random.choice(choices)

print(coinToss, "입니다.")