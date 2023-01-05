import datetime

today = datetime.datetime.now()

# 1단계
# print(today.weekday())
# if today.weekday() == 6 or today.weekday() == 5 :
#     print("주말이므로 학교에 가지 않습니다! \n온종일 코딩하며 지낼 수 있어요!")
# elif today.weekday() == 4 :
#     print("금요일이면 내일 코딩하며 시간을 보낼 수 있어요!")
# else :
#     print("오늘은 학교가는 날입니다.")

# 2단계, 조건거는 방법을 두 가지로 나누어서 설명함
if today.weekday() in [5, 6] :
    print("오늘은 주말입니다.")
else :
    print("평일이니까 학교를 가야해요 시박")
