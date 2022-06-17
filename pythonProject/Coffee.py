print("주문할 음료를 말씀하세요")
ame = int(input("아메리카노 개수 (잔) : "))
cafe = int(input("카페라떼 개수 (잔) : "))
ca = int(input("카푸치노 개수 (잔) : "))
all = (2500 * ame + 3000 * cafe + 3000 * ca)
print("총 금액은 : ", all, "원\n")
money = int(input("지불하실 금액을 입력하세요\n>>> "))
if (money < all):
    print("금액이 부족합니다.")
else:
    print("거스름돈은 " , (money - all) , " 원 입니다.")
