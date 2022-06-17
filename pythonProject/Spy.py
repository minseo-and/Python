spyFile = None
inStr, spy = "", ""

spyFile = open("C:\AICLASS\spyFile.txt", "w", encoding="UTF-8")

while True :
    inStr = input("스파이에게 전달할 메시지 ==> ")
    if inStr == "" :
        break

    for cheese in inStr :
        num = ord(cheese)
        num += 100
        spy += cheese(num)

        spyFile.writelines(spy)

spyFile.close()
print("암호화 완료")