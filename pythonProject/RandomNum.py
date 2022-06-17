import random

print("나랑 숫자 추측 게임을 해보자")
print("네 이름은 뭐니\n")

playerName = input()

print(playerName)
print("반가워. ", playerName, ",", "내가 1부터 30까지의 수를 가지고 있어.")
print("맞춰봐\n")

count = 0
limit = 5
playAgain = 'yes'
guessNumber = random.randrange(1, 30)

print(limit, "번만에 맞춰야 돼")
while True:
    a = int(input("추측한 숫자를 입력하세요 ==> "))
    if a == guessNumber:
        count += 1
        print(count, "번만에 맞췄어요!! 축하해요")
        print("게임을 다시 할까요?(YES or NO)")
        b = input()
        if b == playAgain:
            count = 0
            limit -= 1
            print("이제", limit, "번만에 맞춰야 돼")
        else:
            break


    elif a > guessNumber:
        count += 1
        print("추측한 숫자가 컴퓨터가 가지고 있는 숫자보다 커요")


    elif a < guessNumber:
        count += 1
        print("추측한 숫자가 컴퓨터가 가지고 있는 숫자보다 작아요")

    if count == limit:
        print("못맞췄습니다")
        print("게임을 다시 할까요?(YES or NO)")
        b = input()
        if b == playAgain:
            count = 0
            limit += 1
            print("이제", limit, "번만에 맞춰야 돼")
        else:
            break
