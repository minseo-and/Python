import random

array = [[0 for col in range(4)] for row in range(5)]
for i in range(4):
    for j in range(5):
        a = random.randint(1, 20)
        while True:
            if a in array[i][j]:
                a = random.randint(1, 20)
            else:
                a = array[i][j]
                break

for i in range(4):
    for j in range(5):
        print(" ",  array[i][j])

    print("\n")
