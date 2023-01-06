asciiMin = 32 # 공백의 아스키코드
asciiMax = 126 # 물결표의 아스키코드

key = str(314159)

def decrypt() :
    message = input("복호화할 메시지를 입력하세요. ")
    messEncr = ""

    for index in range(0, len(message)) :
        char = ord(message[index])
        if char < asciiMin or char > asciiMax :
            messEncr += message[index]
        else :
            ascNum = char - int(key[index % len(key)])
            if ascNum < asciiMin :
                ascNum += (asciiMax - asciiMin)
            messEncr = messEncr + chr(ascNum)

    print("복호화한 메시지 :", messEncr)