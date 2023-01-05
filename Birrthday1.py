import datetime

year = int(input("태어난 해는 언제인가요?"))
month = int(input("태어난 달은 언제인가요?"))
day = int(input("태어난 날은 언제인가요?"))

bday = datetime.datetime(year, month, day)

# 1단계
# if bday.weekday() == 6 :
#     print("태어난 날은 일요일이군요")
# elif bday.weekday() == 5 : 
#     print("태어난 날은 토요일이군요")
# elif bday.weekday() == 4 : 
#     print("태어난 날은 금요일이군요")
# elif bday.weekday() == 3 :
#     print("태어난 날은 목요일이군요")
# elif bday.weekday() == 2 :
#     print("태어난 날은 수요일이군요")
# elif bday.weekday() == 1 :
#     print("태어난 날은 화요일이군요")
# else :
#     print("태어난 날은 월요일이군요")

# 2단계
if bday.weekday() == 6 :
    dow = "일"
elif bday.weekday() == 5 : 
    dow = "토"
elif bday.weekday() == 4 : 
    dow = "금"
elif bday.weekday() == 3 :
    dow = "목"
elif bday.weekday() == 2 :
    dow = "수"
elif bday.weekday() == 1 :
    dow = "화"
else :
    dow = "금"

print("당신이 태어난 요일은 " + dow + "요일입니다.")