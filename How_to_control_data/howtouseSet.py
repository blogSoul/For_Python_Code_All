list_A = ['글로벌', '외국어', '활용', '문화', '수용력', '세계', '변화', '글로벌', '사회', '문화주도', '외국어', '다문화', '수용', '개방적', '태도', '국제', '적응', '정서', '유연한', '대처', '이해', '강의', '과목', '과정', '능력', '목적', '역사', '시대', '이론', '지식', '학생', '목표', '수업', '진행', '학습', '강좌', '개념', '경제', '경험', '기초', '관점', '교과목', '기술', '수업', '습득', '대상', '문제', '정치', '바탕', '방법', '분석', '생활', '수강', '이론', '인간', '전반', '한국', '함양', '환경']
list_B = ['글로벌', '외국어', '활용', '문화', '수용력', '세계', '변화', '글로벌', '사회', '문화주도', '외국어', '다문화', '수용', '개방적', '태도', '국제', '적응', '정서', '유연한', '대처', '이해', '강의', '과목', '과정', '능력', '목적', '역사', '시대', '이론', '지식', '학생', '학습', '기초', '수업']

sets_union = set(list_A).union(set(list_B)) #합집합
sets_intersection = set(list_A).intersection(set(list_B)) #교집합
sets_difference = set(list_A).difference(set(list_B)) #차집합
sets_symmetric_difference = set(list_A).symmetric_difference(set(list_B)) #대칭 차집합
sets_issubset = set(list_A).issubset(set(list_B)) # 부분집합인지 확인
sets_isdisjoint = set(list_A).isdisjoint(set(list_B)) # 부분집합인지 확인

set(list_A).add('활력') # 추가
set(list_A).update(['활동']) #리스트 방식으로 추가
set(list_A).discard('활동') # 요소 제거 하지만 제거하려는 원소가 없는 경우 오류를 발생하지 않습니다.
set(list_A).remove('활동') # 요소 제거 하지만 제거하려는 원소가 없는 경우 오류를 발생합니다.
tmp = set(list_A).pop() # 마지막 원소 제거
set(list_A).clear() # 모든 요소 제거
print(sets)
