# 우리는 해외로 가방을 쌓을 때, 필요한 물건을 가지고 가려고 한다. 그리고
# 여행지에서 기념품을 사서 가지고 갈 때도 조금 더 가치있는 물건을 가지고
# 가려고 노력한다. 이러한 상황을 코드로 구현해보았습니다.

total_weight = 0
total_value = 0
weight_limit = 0
stuff_number = 0

print("여행지에 있는 기념품을 들고 갈건데, 무게에 맞춰서 가방을 싸봅시다!")
print("물건은 물건번호 : 무게 : 가치 순으로 나타내보겠습니다.")
print("기념조각상 1 : 5 : 2")
print("대나무부채 2 : 1 : 3")
print("악어가죽가방 3 : 4 : 5")
print("관광지사진첩 4 : 3 : 4")
print("대나무베개 5 : 2 : 2")

weight_limit = int(input("가방의 무게는 얼마나 견딜 수 있습니까?"))

print("가방 무게가 설정되었습니다.")
while(True):
    print("어떤 것을 집어 넣으시겠습니까?")
    stuff_number = int(input("물건번호를 입력해주세요 : "))
    if stuff_number == 1:
        total_weight += 5
        total_value += 2
        stuff_number = 0
    elif stuff_number == 2:
        total_weight += 1
        total_value += 3
        stuff_number = 0
    elif stuff_number == 3:
        total_weight += 4
        total_value += 5
        stuff_number = 0
    elif stuff_number == 4:
        total_weight += 3
        total_value += 4
        stuff_number = 0
    elif stuff_number == 5:
        total_weight += 2
        total_value += 2
        stuff_number = 0
    else:
        print("주문 번호를 다시 입력해주세요.")

    if weight_limit <= total_weight:
        print("가방이 가득 찾습니다!")
        break
    else:
        print("현재 가방의 총 무게는 " + str(total_weight) + "입니다.")
        print("현재 가방 속 들어있는 물건의 가치는 " + str(total_value) + "입니다.")

print("가방의 총 무게는 " + str(total_weight) + "입니다.")
print("가방 속 들어있는 물건의 가치는 " + str(total_value) + "입니다.")

