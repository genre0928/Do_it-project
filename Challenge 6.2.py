from Encrypt import *
from Decrypt import *

asciiMin = 32 # 공백의 아스키코드
asciiMax = 126 # 물결표의 아스키코드

key = str(314159)

action = input("암호화(E) 또는 복호화(D) 중 어떤 일을 진행할까요? ").upper()

if action == "E" :
    encrypt()
elif action == "D" :
    decrypt()
else :
    print("정확한 단어를 입력해주세요. 프로그램을 종료합니다.")