import sys

customer_pay = 0
total_menu_cost = 0
change = 0

print("안녕하세요! 무엇을 주문하시겠습니까?")
print("아메리카노 : 1")
print("카라멜 마키야또 : 2")
print("버블티 : 3")
print("자바칩 프라프치노 : 4")
print("딸기 스무디 : 5")
print("메뉴판 입니다! (메뉴번호, )")

select_menu = int(input("메뉴를 선택하세요 : "))
if select_menu == 1:
    total_menu_cost += 1500
elif select_menu == 2:
    total_menu_cost += 2000
elif select_menu == 3:
    total_menu_cost += 2500
elif select_menu == 4:
    total_menu_cost += 4500
elif select_menu == 5:
    total_menu_cost += 3000
else:
    print("1번부터 5번까지만 입력할 수 있습니다. 다시 주문해주세요!")
    sys.exit(1)

print("당신이 주문하신 메뉴 번호는 " + str(select_menu) + "입니다!")
print("얼마를 입금하시겠습니까?")
customer_pay = int(input("입금금액을 입력하세요 : "))

change = customer_pay - total_menu_cost
if change > 0:
    print("잔액은 " + str(change) + "입니다.")
    print("이용해주셔서 감사합니다!")
elif change == 0:
    print("이용해주셔서 감사합니다!")
else:
    print("결제 금액이 부족합니다! 다시 주문해주세요!")
