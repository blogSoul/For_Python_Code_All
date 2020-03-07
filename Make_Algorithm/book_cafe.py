# 카페에 가면 가끔씩 카페에 책이 있는 경우가 있습니다. 이러한 책들을
# 정리하고 추가하고 정리하는 상황을 코드로 구현해보겠습니다.
book_table = []
bookshelf = []
book_number = 0
order_number = 0
for i in range(1, 11):
    bookshelf.append(i)

while(True):
    print("안녕하세요! 원하시는 도서 서비스를 주문하세요.")
    print("1 : 도서 대출")
    print("2 : 도서 반납")
    print("3 : 도서 정리")
    print("4 : 서비스 종료")
    print("현재 도서 책장 상황입니다." + str(bookshelf))
    print("현재 가지고 계신 도서 현황입니다." + str(book_table))
    order_number = int(input("주문 번호를 입력해주세요. : "))

    if order_number == 1:
        if len(bookshelf) == 0:
            print("대출하실 책이 존재하지 않습니다.")
            continue
        print("대출하고 싶은 도서 번호를 입력해주세요.")
        book_number = int(input("도서 번호를 입력해주세요. : "))
        book_table.append(book_number)
        bookshelf.remove(book_number)
    elif order_number == 2:
        if len(book_table) == 0:
            print("반납하실 책이 존재하지 않습니다.")
            continue
        print("반납하고 싶은 도서 번호를 입력해주세요.")
        book_number = int(input("도서 번호를 입력해주세요. : "))
        bookshelf.append(book_number)
        book_table.remove(book_number)
    elif order_number == 3:
        print("도서를 정리하시겠습니까? 1.네 2.아니요")
        order_number = int(input("도서 번호를 입력해주세요. : "))
        if order_number == 1:
            bookshelf.sort()
            book_table.sort()
        elif order_number == 2:
            continue
        else:
            print("값을 정확히 입력해주세요. 서비스 초기화면으로 이동합니다.")
    elif order_number == 4:
        print("서비스를 종료하시겠습니까? 1.네 2.아니요")
        order_number = int(input("번호를 입력해주세요. : "))
        if order_number == 1:
            bookshelf.sort()
            book_table.sort()
            if len(book_table) == 0:
                print("서비스를 종료합니다.")
                break
        elif order_number == 2:
            continue
        else:
            print("값을 정확히 입력해주세요. 서비스 초기화면으로 이동합니다.")
    else:
        print("값을 정확히 입력해주세요. 서비스 초기화면으로 이동합니다.")
