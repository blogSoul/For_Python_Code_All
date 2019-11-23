# PyCharm으로 구현
# pymysql 설치 필요

def MainPage():
    print("--------냉장고를 부탁해--------")
    print("1. 전체레시피")
    print("2. 내 냉장고")
    print("3. 가능한 요리")
    print("4. 종료")
    a = input("원하는 번호를 선택하세요 : ")
    return a

def Recipe():
    print("--------전체 레시피--------")
    print("1. 레시피 검색")
    print("2. 새로운 레시피 추가")
    print("3. 기존 레시피 수정")
    print("4. 기존 레시피 삭제")
    print("5. 전체 요리 검색")
    print("6. 메인메뉴")
    a = input("원하는 번호를 선택하세요 : ")
    return a

def Search_Recipe():
    print()
    a = input("원하는 요리를 입력하세요 : ")
    conn = pymysql.connect(host='localhost', user='root', password='0000',
                           db='cook_db', charset='utf8')

    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()

    # SQL문 실행
    # cook_kind에 cook_time.cook_time, cook_difficulty.cook_difficulty, cook_world.cook_world를 cookname 별로 Join
    # 원하는 요리의 이름, 종류, 시간, 난이도, 나라별 음식 출력
    sql = """select cook_kind.*, cook_time.cook_time, cook_difficulty.cook_difficulty, cook_world.cook_world from cook_kind left join cook_time
                        on cook_kind.cook_name = cook_time.cook_name
                        left join cook_difficulty
                        on cook_kind.cook_name = cook_difficulty.cook_name
                        left join cook_world
                        on cook_kind.cook_name = cook_world.cook_name
                        where cook_kind.cook_name = \"""" + a + "\""
    curs.execute(sql)


    # 데이타 Fetch
    rows = curs.fetchall()

    print()

    print(rows[0][0])
    print("요리 종류 : " + rows[0][1])
    print("요리 시간 : " + rows[0][2])
    print("요리 난이도 : " + rows[0][3])
    print(rows[0][4] + "입니다.")


    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()

    # 요리 재료 확인
    sql = "select cook_materials from cook_material where cook_name = \"" + a + "\""
    curs.execute(sql)

    # 데이타 Fetch
    rows = curs.fetchall()

    material = []
    for i in rows:
        material.append(i[0])

    print("요리 재료 : ")
    print(*material)

    print()

    # Connection 닫기
    conn.close()

def Add_Recipe():
    print()
    a1 = input("요리 이름 : ")

    conn = pymysql.connect(host='localhost', user='root', password='0000',
                           db='cook_db', charset='utf8')

    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()

    # SQL문 실행
    # 전체 요리 데이터 출력
    sql = "select cook_name from cook_kind"

    curs.execute(sql)

    # 데이타 Fetch
    rows = list(curs.fetchall())

    # 전체 요리 데이터를 리스트 형태로 저장
    recipe = []
    for i in rows:
        recipe.append(*i)

    # 입력받은 요리가 현재 레시피에 있는지 확인
    if a1 in recipe:
        print("이미 있는 음식입니다.")

    else:
        # 없을 경우 각 테이블별 데이터 삽입
        print()
        a2 = input("요리 종류 : ")
        curs = conn.cursor()
        sql = """insert into cook_kind
                                 values (%s, %s)"""
        curs.execute(sql, (a1, a2))


        a3 = input("요리 시간 : ")
        curs = conn.cursor()
        sql = """insert into cook_time
                                         values (%s, %s)"""
        curs.execute(sql, (a1, a3))


        a4 = input("요리 난이도 : ")
        curs = conn.cursor()
        sql = """insert into cook_difficulty
                                         values (%s, %s)"""
        curs.execute(sql, (a1, a4))


        a5 = input("나라별 음식 : ")
        curs = conn.cursor()
        sql = """insert into cook_world
                                         values (%s, %s)"""
        curs.execute(sql, (a1, a5))

        # 원하는 재료를 쉼표로 구분하여 재료의 개수만큼 데이터 삽입
        a6 = input("재료 : ")
        curs = conn.cursor()
        a6 = a6.split(", ")
        for i in a6:
            sql = """insert into cook_material
                             values (%s, %s)"""
            curs.execute(sql, (a1, i))
    print()
    conn.commit()
    conn.close()

def Update_Recipe():
    print()
    a1 = input("요리 이름 : ")

    conn = pymysql.connect(host='localhost', user='root', password='0000',
                           db='cook_db', charset='utf8')

    curs = conn.cursor()

    # SQL문 실행

    sql = "select cook_name from cook_kind where cook_name = \"" + a1 + "\""
    curs.execute(sql)

    rows = curs.fetchall()

    # 수정할 요리가 있는지 확인
    if len(rows) != 0:
        a2 = input("요리 종류 : ")
        a3 = input("요리 시간 : ")
        a4 = input("요리 난이도 : ")
        a5 = input("나라별 음식 : ")
        a6 = input("재료 : ")

        # 수정하고 싶지 않으면 엔터입력
        # 수정하고 싶은 테이블만 수정

        if a2 != '':
            curs = conn.cursor()
            sql = "update cook_kind set cook_kind = \"" + a2 + "\" where cook_name = \""  + a1 + "\""
            curs.execute(sql)

        if a3 != '':
            curs = conn.cursor()
            sql = "update cook_time set cook_time = \"" + a3 + "\" where cook_name = \"" + a1 + "\""
            curs.execute(sql)

        if a4 != '':
            curs = conn.cursor()
            sql = "update cook_difficulty set cook_difficulty = \"" + a4 + "\" where cook_name = \"" + a1 + "\""
            curs.execute(sql)

        if a5 != '':
            curs = conn.cursor()
            sql = "update cook_world  set cook_world  = \"" + a5 + "\" where cook_name = \"" + a1 + "\""
            curs.execute(sql)

        if a6 != '':
            # 요리재료는 먼저 수정할 요리의 데이터를 모두 삭제
            # 그리고 넣고 싶은 재료를 다시 삽입
            curs = conn.cursor()
            sql = "delete from cook_material where cook_name = \"" + a1 + "\""
            curs.execute(sql)

            a6 = a6.split(", ")
            for i in a6:
                sql = """insert into cook_material
                                        values (%s, %s)"""
                curs.execute(sql, (a1, i))

        print("수정되었습니다.")

    else:
        print("입력하신 요리의 정보가 없습니다.")
    print()

    conn.commit()
    conn.close()

def Delete_Recipe():
    print()
    a1 = input("요리 이름 : ")

    import pymysql

    conn = pymysql.connect(host='localhost', user='root', password='0000',
                           db='cook_db', charset='utf8')

    curs = conn.cursor()


    sql = "select cook_name from cook_kind where cook_name = \"" + a1 + "\""
    curs.execute(sql)
    rows = curs.fetchall()

    # 삭제할 요리가 있는지 확인
    if len(rows) != 0:
        curs = conn.cursor()
        # cook_kind에 각 테이블을 Join한 뒤 삭제할 요리를 확인하고 한번에 삭제
        sql = """delete cook_kind, cook_time, cook_difficulty, cook_world, cook_material from cook_kind left join cook_time
                            on cook_kind.cook_name = cook_time.cook_name
                            left join cook_difficulty
                            on cook_kind.cook_name = cook_difficulty.cook_name
                            left join cook_world
                            on cook_kind.cook_name = cook_world.cook_name
                            left join cook_material
                            on cook_kind.cook_name = cook_material.cook_name
                            where cook_kind.cook_name = \"""" + a1 + "\""
        curs.execute(sql)

        print("삭제되었습니다.")
    else:
        print("입력하신 요리는 없습니다.")
    print()

    conn.commit()
    conn.close()

def Search_All_Cooks():
    conn = pymysql.connect(host='localhost', user='root', password='0000',
                           db='cook_db', charset='utf8')

    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()

    # SQL문 실행
    sql = "select cook_name  from cook_kind"

    curs.execute(sql)

    # 데이타 Fetch
    rows = list(curs.fetchall())

    # 전체 요리 이름을 출력하기 위해 리스트로 저장
    recipe = []
    for i in rows:
        recipe.append(*i)

    print()
    print("레시피가 있는 요리 :")
    print(*recipe)
    print()

    # Connection 닫기
    conn.close()

def MyMaterial():
    print("--------냉장고 현황--------")
    print("1. 재료 추가")
    print("2. 재료 삭제")
    print("3. 재료 확인")
    print("4. 메인메뉴")
    a = input("원하는 번호를 선택하세요 : ")
    return a

def Add_MyMaterial():
    a1 = input("추가할 재료 : ")

    conn = pymysql.connect(host='localhost', user='root', password='0000',
                           db='cook_db', charset='utf8')

    curs = conn.cursor()

    a1 = a1.split(", ")

    # 재료를 넣기 위해 중복을 방지하기 위해 먼저 기존에 있던 데이터 모두 삭제
    # 삭제 후 원하는 데이터 삽입
    
    for i in a1:
        sql = "delete from my_refrigerator_material where My_materials = \"" + i + "\""
        curs.execute(sql)

    for i in a1:
        sql = """insert into my_refrigerator_material
                            values (%s)"""
        curs.execute(sql, (i))


    print()
    print("추가 되었습니다.")
    print()

    conn.commit()
    conn.close()

def Delete_MyMaterial():
    a1 = input("지우고 싶은 재료를 입력하세요 : ")

    import pymysql

    conn = pymysql.connect(host='localhost', user='root', password='0000',
                           db='cook_db', charset='utf8')

    curs = conn.cursor()

    a1 = a1.split(", ")
    
    # 원하는 재료 삭제
    for i in a1:
        sql = "delete from my_refrigerator_material where My_materials = \"" + i + "\""
        curs.execute(sql)

    print()
    print("삭제되었습니다.")
    print()

    conn.commit()
    conn.close()

def Search_MyMaterial():
    conn = pymysql.connect(host='localhost', user='root', password='0000',
                           db='cook_db', charset='utf8')

    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()

    # SQL문 실행
    # 현재 가지고 있는 냉장고 재료 확인
    sql = "select *  from my_refrigerator_material"

    curs.execute(sql)

    # 데이타 Fetch
    rows = list(curs.fetchall())

    recipe = []
    for i in rows:
        recipe.append(*i)

    print()
    print("현재 내 냉장교 재료 :")
    print(*recipe)
    print()

    # Connection 닫기
    conn.close()

def Find_Cooking():
    print("--------가능한 요리--------")
    print("1. 가능한 요리 검색")
    print("2. 세부 검색")
    print("3. 메인메뉴")
    a = input("원하는 번호를 선택하세요 : ")
    return a

def Search_for_possible_dishes():
    conn = pymysql.connect(host='localhost', user='root', password='0000',
                           db='cook_db', charset='utf8')

    curs = conn.cursor()

    # 먼저 현재 가지고 있는 재료 확인
    sql = "select *  from my_refrigerator_material"

    curs.execute(sql)

    rows = list(curs.fetchall())

    recipe1 = []
    for i in rows:
        recipe1.append(*i)

    print()
    print("내가 가지고 있는 재료")
    print(*recipe1)

    curs = conn.cursor()

    # 각 요리별 레시피와 비교하기 위해 먼저 전체 요리를 리스트로 저장
    sql = "select cook_name from cook_kind"

    curs.execute(sql)

    rows = list(curs.fetchall())

    cook = [];
    for i in rows:
        cook.append(i[0])

    # 가능한 요리 초기화
    possible_cook = []

    # 각 요리별 필요한 재료 확인
    for i in cook:
        sql = "select *  from cook_material where cook_name = \"" + i + "\""
        curs.execute(sql)
        # 데이타 Fetch
        rows = curs.fetchall()
        recipe = []
        for j in rows:
            recipe.append(j[1])

        # 필요한 재료와 내가 가지고 있는 재료의 교집합
        intersect_recipe = intersect(recipe1,recipe)

        # 리스트별 비교할 때 문자열이므로 정렬을 해줌
        intersect_recipe.sort()
        recipe.sort()

        # 교집합이 공집합이 아니거나 필요한 재료와 동일하다면 가능한 요리에 요리 이름 추가
        if (intersect_recipe == recipe) and (intersect_recipe != []):
            possible_cook.append(i)

    print()
    print("현재 내가 가지고 있는 재료로 가능한 요리 : ")
    if len(possible_cook) == 0:
        print("가능한 요리가 없습니다.")
    else:
        print(*possible_cook)
    print()
# 내 재료, 각 요리별 재료 확인

# set의 교집합
def intersect(a, b):
    return list(set(a) & set(b))

def Detail_Search():
    conn = pymysql.connect(host='localhost', user='root', password='0000',
                           db='cook_db', charset='utf8')

    curs = conn.cursor()

    # 원하는 요리 종류
    # 각 데이터의 값을 중복 제거하여 사용자가 필요로하는 데이터만 선택
    sql = "select distinct cook_kind from cook_kind"
    curs.execute(sql)

    rows = list(curs.fetchall())
    kind = []
    cnt = 1
    for i in rows:
        kind.append(*i)
    for i in kind:
        print(str(cnt) + ":" + i)
        cnt = cnt + 1

    # 다중 선택 가능
    cook_kind_num = input("원하는 번호를 입력하시오 :")
    cook_kind_num = cook_kind_num.split(",")
    for i in cook_kind_num:
        print(kind[int(i)-1])

    cnt = 0
    cook_kind_sql = ""

    # 선택한 번호를 확인해 뒤에 조건문으로 추가하기 위해 하나의 sql문으로 저장
    for i in cook_kind_num:
        cook_kind_sql = cook_kind_sql + "cook_kind.cook_kind = \"" + kind[int(i) - 1] + "\" "
        cnt = cnt + 1
        if cnt == len(cook_kind_num):
            break
        else:
            cook_kind_sql = cook_kind_sql + " or "


    # 원하는 요리 시간
    sql = "select distinct cook_time from cook_time"
    curs.execute(sql)

    rows = list(curs.fetchall())
    time = []
    cnt = 1
    for i in rows:
        time.append(*i)
    for i in time:
        print(str(cnt) + ":" + i)
        cnt = cnt + 1

    cook_time_num = input("원하는 번호를 입력하시오 :")
    cook_time_num = cook_time_num.split(",")

    for i in cook_time_num:
        print(time[int(i) - 1])

    cnt = 0
    cook_time_sql = ""

    for i in cook_time_num:
        cook_time_sql = cook_time_sql + "cook_time.cook_time = \"" + time[int(i) - 1] + "\" "
        cnt = cnt + 1
        if cnt == len(cook_time_num):
            break
        else:
            cook_time_sql = cook_time_sql + " or "


    # 원하는 요리 난이도
    sql = "select distinct cook_difficulty from cook_difficulty"
    curs.execute(sql)
    # 데이타 Fetch
    rows = list(curs.fetchall())
    difficulty = []
    cnt = 1
    for i in rows:
        difficulty.append(*i)
    for i in difficulty:
        print(str(cnt) + ":" + i)
        cnt = cnt + 1

    cook_difficulty_num = input("원하는 번호를 입력하시오 :")
    cook_difficulty_num = cook_difficulty_num.split(",")

    for i in cook_difficulty_num:
        print(difficulty[int(i) - 1])

    cnt = 0
    cook_difficulty_sql = ""

    for i in cook_difficulty_num:
        cook_difficulty_sql = cook_difficulty_sql + "cook_difficulty.cook_difficulty = \"" + difficulty[int(i) - 1] + "\" "
        cnt = cnt + 1
        if cnt == len(cook_difficulty_num):
            break
        else:
            cook_difficulty_sql = cook_difficulty_sql + " or "


    # 원하는 요리의 나라
    sql = "select distinct cook_world from cook_world"
    curs.execute(sql)
    # 데이타 Fetch
    rows = list(curs.fetchall())
    world = []
    cnt = 1
    for i in rows:
        world.append(*i)
    for i in world:
        print(str(cnt) + ":" + i)
        cnt = cnt + 1

    cook_world_num = input("원하는 번호를 입력하시오 :")
    cook_world_num = cook_world_num.split(",")

    for i in cook_world_num:
        print(world[int(i) - 1])

    cnt = 0
    cook_world_sql = ""

    for i in cook_world_num:
        cook_world_sql = cook_world_sql + "cook_world.cook_world = \"" + world[int(i) - 1] + "\" "
        cnt = cnt + 1
        if cnt == len(cook_world_num):
            break
        else:
            cook_world_sql = cook_world_sql + " or "



    # 먼저 cook_kind에 각 테이블을 Join
    # 세부적으로 원하는 값들을 저장한 sql문을 and 연산으로 묶어줌
    sql = '''select cook_kind.cook_name from cook_kind left join cook_time
            on cook_kind.cook_name = cook_time.cook_name
            left join cook_difficulty
            on cook_kind.cook_name = cook_difficulty.cook_name
            left join cook_world
            on cook_kind.cook_name = cook_world.cook_name
            where (''' + cook_kind_sql + ") and (" + cook_time_sql + ") and (" + cook_difficulty_sql + ") and (" + cook_world_sql + ")"


    curs.execute(sql)

    rows = list(curs.fetchall())

    print("--------------------------------")
    print("검색하신 조건을 만족하는 음식입니다.")
    for i in rows:
        print(i[0])


# mysql을 연동하기 위해 pymysql을 import
import pymysql

# Main 시작
a = MainPage()


while(1):
    if a == '1':
        b = Recipe();
        if b == '1':
            try:
                Search_Recipe()
            except:
                print("입력하신 요리의 정보가 없습니다.")
                print()
                a = MainPage()
        elif b == '2':
            try:
                Add_Recipe()
            except:
                a = MainPage()
        elif b == '3':
            try:
                Update_Recipe()
            except:
                a = MainPage()
        elif b == '4':
            try:
                Delete_Recipe()
            except:
                a = MainPage()
        elif b == '5':
            try:
                Search_All_Cooks()
            except:
                a = MainPage()
        elif b == '6':
            a = MainPage()
        else:
            print("다시 입력하세요")
            continue
    elif a == '2':
        b = MyMaterial()
        if b == '1':
            try:
                Add_MyMaterial()
                a = MainPage()
            except:
                a = MainPage()
        elif b == '2':
            try:
                Delete_MyMaterial()
                a = MainPage()
            except:
                a = MainPage()
        elif b == '3':
            try:
                Search_MyMaterial()
                a = MainPage()
            except:
                a = MainPage()
        elif b == '4':
            a = MainPage()
        else:
            print("다시 입력하세요")
            continue
    elif a == '3':
        b = Find_Cooking()
        if b == '1':
            try:
                Search_for_possible_dishes()
                a = MainPage()
            except:
                a = MainPage()
        elif b == '2':
            try:
                Detail_Search()
                a = MainPage()
            except:
                a = MainPage()
        elif b == '3':
            a = MainPage()
        else:
            print("다시 입력하세요")
            continue
    elif a == '4':
        break
    else:
        a = input("다시 입력하시오 : ")
