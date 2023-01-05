import random

# die1 = random.randrange(1, 7)
# die2 = random.randrange(1, 7)


# print("주사위는", die1, ",", die2, "(이)가 나왔으며 합은" , die1 + die2, "입니다.")


# 띄어쓰기가 불편해서 내가 수정해본 버전
die1 = str(random.randrange(1, 7))
die2 = str(random.randrange(1, 7))
sumDie = int(die1) + int(die2)

print("주사위는 " + die1, ", " + die2 + "(이)가 나왔으며 합은 "+ str(sumDie) + "입니다.")