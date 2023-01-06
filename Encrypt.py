asciiMin = 32 # 공백의 아스키코드
asciiMax = 126 # 물결표의 아스키코드

key = str(314159) # 누구에게도 알려줄 수 없는 비밀키임

def encrypt() :
    message = input("암호화할 메시지를 입력하세요.")
    messEncr = ""

    for index in range(0, len(message)) : # 0부터 입력한 메시지 길이만큼 index 변수에 저장
        char = ord(message[index]) # char 변수는 message[i]번째의 아스키코드를 저장
        if char < asciiMin or char > asciiMax : # 만약 char 변수가 32 미만이거나 126 초과인 경우
            messEncr += message[index] # messEncr 변수에 message[i]번째 값을 추가해줘라
        else : # 근데 그게 아니라고 하면 나는 암호화를 시작할 것이다.
            ascNum = char + int(key[index % len(key)]) # ascNum 변수는 message[i]번째 글자의 아스키코드 + key[i/6] 값을 추가해주는 방식으로 암호화 해줌
            if ascNum > asciiMax : # 만약 ascNum이 126을 초과하는 경우
                ascNum -= (asciiMax - asciiMin) #ascNum 변수는 126-32 값을 빼줌
            messEncr = messEncr + chr(ascNum) # 그게 아니라면 원래 예정된대로 암호화를 진행할 것이다.

    print("암호화한 메시지 :", messEncr)