# Mysql에서 database를 만들때 사용하는 코드입니다!

show databases;

CREATE database cook_DB default character SET UTF8;

use cook_DB;

CREATE table cook_kind
(
cook_name varchar(32) PRIMARY KEY not null,
cook_kind varchar(32) not null
)ENGINE=InnoDB;
#요리 이름과 요리 종류를 대응시킨 테이블입니다. 메인, 반찬,디저트로 나누어져 있습니다.
CREATE table cook_time
(
cook_name varchar(32) PRIMARY KEY not null,
cook_time varchar(32) not null
)ENGINE=InnoDB;
#요리 이름과 요리 시간을 대응시킨 테이블입니다. 10분이하,10분에서30분이하,30분에서1시간이하,1시간이상으로 나누어져 있습니다.
CREATE table cook_difficulty
(
cook_name varchar(32) PRIMARY KEY not null,
cook_difficulty varchar(32) not null
)ENGINE=InnoDB;
#요리 이름과 요리 난이도를 대응시킨 테이블입니다. 상,중,하로 나누어져 있습니다.
CREATE table cook_world
(
cook_name varchar(32) PRIMARY KEY not null,
cook_world varchar(32) not null
)ENGINE=InnoDB;
#나라별 요리를 정리한 테이블입니다. 한식,양식,중식,일식으로 나누어져 있습니다.
CREATE table cook_material
(
cook_name varchar(32) not null,
cook_materials varchar(32) not null
)ENGINE=InnoDB;
#요리 이름과 요리 재료를 1-1로 대응한 테이블입니다.
#요라재료를 넣을 때, 설탕,소금,간장,식초,후추,고춧가루,간마늘,식용류는 있다고 가정하고 재료를 넣었습니다.
CREATE table My_refrigerator_material
(
My_materials varchar(32) not null
)ENGINE=InnoDB;
#내 냉장고 안에 있는 요리재료를 의미합니다.

insert into My_refrigerator_material(My_materials) value('돼지고기');
insert into My_refrigerator_material(My_materials) value('떡');
insert into My_refrigerator_material(My_materials) value('고추장');
insert into My_refrigerator_material(My_materials) value('파');
insert into My_refrigerator_material(My_materials) value('양파');
#냉장고 안에 있는 재료 샘플입니다.

insert into cook_kind(cook_name,cook_kind)value('떡볶이','메인');
insert into cook_kind(cook_name,cook_kind)value('짜장면','메인');
insert into cook_kind(cook_name,cook_kind)value('탕수육','메인');
insert into cook_kind(cook_name,cook_kind)value('스파게티','메인');
insert into cook_kind(cook_name,cook_kind)value('피자','메인');
insert into cook_kind(cook_name,cook_kind)value('된장찌개','반찬');
insert into cook_kind(cook_name,cook_kind)value('돼지국밥','메인');
insert into cook_kind(cook_name,cook_kind)value('핫도그','메인');
insert into cook_kind(cook_name,cook_kind)value('계란찜','반찬');
insert into cook_kind(cook_name,cook_kind)value('라멘','메인');
insert into cook_kind(cook_name,cook_kind)value('초밥','메인');
insert into cook_kind(cook_name,cook_kind)value('마파두부','반찬');
insert into cook_kind(cook_name,cook_kind)value('잔치국수','메인');
insert into cook_kind(cook_name,cook_kind)value('규동','메인');
insert into cook_kind(cook_name,cook_kind)value('깻잎장아찌','반찬');
insert into cook_kind(cook_name,cook_kind)value('크로와상','디저트');
insert into cook_kind(cook_name,cook_kind)value('에그타르트','디저트');
insert into cook_kind(cook_name,cook_kind)value('롤케익','디저트');
insert into cook_kind(cook_name,cook_kind)value('식혜','디저트');
insert into cook_kind(cook_name,cook_kind)value('불고기','반찬');
insert into cook_kind(cook_name,cook_kind)value('마늘쫑장아찌','반찬');
insert into cook_kind(cook_name,cook_kind)value('스콘','디저트');
insert into cook_kind(cook_name,cook_kind)value('햄버거','메인');
insert into cook_kind(cook_name,cook_kind)value('피클','반찬');
insert into cook_kind(cook_name,cook_kind)value('쿠키','디저트');
insert into cook_kind(cook_name,cook_kind)value('감자전','메인');
insert into cook_kind(cook_name,cook_kind)value('안동찜닭','메인');
insert into cook_kind(cook_name,cook_kind)value('멘보샤','디저트');
insert into cook_kind(cook_name,cook_kind)value('딤섬','메인');
insert into cook_kind(cook_name,cook_kind)value('오향장육','반찬');
insert into cook_kind(cook_name,cook_kind)value('만두','메인');
insert into cook_kind(cook_name,cook_kind)value('돈까스','메인');
insert into cook_kind(cook_name,cook_kind)value('샤브샤브','메인');
insert into cook_kind(cook_name,cook_kind)value('오꼬노미야끼','메인');
insert into cook_kind(cook_name,cook_kind)value('올리브파스타','메인');
insert into cook_kind(cook_name,cook_kind)value('피쉬앤칩스','디저트');
insert into cook_kind(cook_name,cook_kind)value('타코','메인');
insert into cook_kind(cook_name,cook_kind)value('또띠아','디저트');
insert into cook_kind(cook_name,cook_kind)value('까르보나라','메인');
insert into cook_kind(cook_name,cook_kind)value('오믈렛','메인');
insert into cook_kind(cook_name,cook_kind)value('부추전','반찬');
insert into cook_kind(cook_name,cook_kind)value('연근조림','반찬');
insert into cook_kind(cook_name,cook_kind)value('칼국수','메인');
insert into cook_kind(cook_name,cook_kind)value('코울슬로','반찬');
insert into cook_kind(cook_name,cook_kind)value('콩자반','반찬');
insert into cook_kind(cook_name,cook_kind)value('타코야키','디저트');
insert into cook_kind(cook_name,cook_kind)value('메밀소바','메인');
insert into cook_kind(cook_name,cook_kind)value('탄탄면','메인');
insert into cook_kind(cook_name,cook_kind)value('김밥','메인');
#음식종류에 관한 샘플입니다.

insert into cook_time(cook_name,cook_time)value('떡볶이','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('짜장면','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('탕수육','1시간이상');
insert into cook_time(cook_name,cook_time)value('스파게티','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('피자','1시간이상');
insert into cook_time(cook_name,cook_time)value('된장찌개','1시간이상');
insert into cook_time(cook_name,cook_time)value('돼지국밥','1시간이상');
insert into cook_time(cook_name,cook_time)value('핫도그','10분이하');
insert into cook_time(cook_name,cook_time)value('계란찜','1시간이상');
insert into cook_time(cook_name,cook_time)value('라멘','1시간이상');
insert into cook_time(cook_name,cook_time)value('초밥','10분이하');
insert into cook_time(cook_name,cook_time)value('마파두부','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('잔치국수','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('규동','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('깻잎장아찌','10분에서30분이하');
insert into cook_time(cook_name,cook_time)value('크로와상','1시간이상');
insert into cook_time(cook_name,cook_time)value('에그타르트','1시간이상');
insert into cook_time(cook_name,cook_time)value('롤케익','1시간이상');
insert into cook_time(cook_name,cook_time)value('식혜','1시간이상');
insert into cook_time(cook_name,cook_time)value('불고기','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('마늘쫑장아찌','10분에서30분이하');
insert into cook_time(cook_name,cook_time)value('스콘','1시간이상');
insert into cook_time(cook_name,cook_time)value('햄버거','10분에서30분이하');
insert into cook_time(cook_name,cook_time)value('피클','1시간이상');
insert into cook_time(cook_name,cook_time)value('쿠키','1시간이상');
insert into cook_time(cook_name,cook_time)value('감자전','10분에서30분이하');
insert into cook_time(cook_name,cook_time)value('안동찜닭','1시간이상');
insert into cook_time(cook_name,cook_time)value('멘보샤','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('딤섬','10분에서30분이하');
insert into cook_time(cook_name,cook_time)value('오향장육','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('만두','10분에서30분이하');
insert into cook_time(cook_name,cook_time)value('돈까스','10분에서30분이하');
insert into cook_time(cook_name,cook_time)value('샤브샤브','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('오꼬노미야끼','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('올리브파스타','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('피쉬앤칩스','10분에서30분이하');
insert into cook_time(cook_name,cook_time)value('타코','10분에서30분이하');
insert into cook_time(cook_name,cook_time)value('또띠아','10분에서30분이하');
insert into cook_time(cook_name,cook_time)value('까르보나라','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('오믈렛','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('부추전','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('연근조림','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('칼국수','1시간이상');
insert into cook_time(cook_name,cook_time)value('코울슬로','10분에서30분이하');
insert into cook_time(cook_name,cook_time)value('콩자반','10분에서30분이하');
insert into cook_time(cook_name,cook_time)value('타코야키','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('메밀소바','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('탄탄면','30분에서1시간이하');
insert into cook_time(cook_name,cook_time)value('김밥','10분이하');
#요리시간에 관한 샘플입니다.

insert into cook_difficulty(cook_name,cook_difficulty)value('떡볶이','중');
insert into cook_difficulty(cook_name,cook_difficulty)value('짜장면','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('탕수육','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('스파게티','중');
insert into cook_difficulty(cook_name,cook_difficulty)value('피자','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('된장찌개','중');
insert into cook_difficulty(cook_name,cook_difficulty)value('돼지국밥','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('핫도그','하');
insert into cook_difficulty(cook_name,cook_difficulty)value('계란찜','중');
insert into cook_difficulty(cook_name,cook_difficulty)value('라멘','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('초밥','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('마파두부','중');
insert into cook_difficulty(cook_name,cook_difficulty)value('잔치국수','중');
insert into cook_difficulty(cook_name,cook_difficulty)value('규동','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('깻잎장아찌','하');
insert into cook_difficulty(cook_name,cook_difficulty)value('크로와상','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('에그타르트','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('롤케익','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('식혜','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('불고기','중');
insert into cook_difficulty(cook_name,cook_difficulty)value('마늘쫑장아찌','하');
insert into cook_difficulty(cook_name,cook_difficulty)value('스콘','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('햄버거','하');
insert into cook_difficulty(cook_name,cook_difficulty)value('피클','하');
insert into cook_difficulty(cook_name,cook_difficulty)value('쿠키','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('감자전','중');
insert into cook_difficulty(cook_name,cook_difficulty)value('안동찜닭','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('멘보샤','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('딤섬','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('오향장육','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('만두','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('돈까스','중');
insert into cook_difficulty(cook_name,cook_difficulty)value('샤브샤브','중');
insert into cook_difficulty(cook_name,cook_difficulty)value('오꼬노미야끼','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('올리브파스타','중');
insert into cook_difficulty(cook_name,cook_difficulty)value('피쉬앤칩스','하');
insert into cook_difficulty(cook_name,cook_difficulty)value('타코','하');
insert into cook_difficulty(cook_name,cook_difficulty)value('또띠아','하');
insert into cook_difficulty(cook_name,cook_difficulty)value('까르보나라','하');
insert into cook_difficulty(cook_name,cook_difficulty)value('오믈렛','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('부추전','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('연근조림','하');
insert into cook_difficulty(cook_name,cook_difficulty)value('칼국수','중');
insert into cook_difficulty(cook_name,cook_difficulty)value('코울슬로','하');
insert into cook_difficulty(cook_name,cook_difficulty)value('콩자반','하');
insert into cook_difficulty(cook_name,cook_difficulty)value('타코야키','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('메밀소바','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('탄탄면','상');
insert into cook_difficulty(cook_name,cook_difficulty)value('김밥','하');
#요리 난이도에 관한 샘플입니다.

insert into cook_world(cook_name,cook_world)value('떡볶이','한식');
insert into cook_world(cook_name,cook_world)value('짜장면','중식');
insert into cook_world(cook_name,cook_world)value('탕수육','중식');
insert into cook_world(cook_name,cook_world)value('스파게티','양식');
insert into cook_world(cook_name,cook_world)value('피자','양식');
insert into cook_world(cook_name,cook_world)value('된장찌개','한식');
insert into cook_world(cook_name,cook_world)value('돼지국밥','한식');
insert into cook_world(cook_name,cook_world)value('핫도그','양식');
insert into cook_world(cook_name,cook_world)value('계란찜','한식');
insert into cook_world(cook_name,cook_world)value('라멘','일식');
insert into cook_world(cook_name,cook_world)value('초밥','일식');
insert into cook_world(cook_name,cook_world)value('마파두부','중식');
insert into cook_world(cook_name,cook_world)value('잔치국수','한식');
insert into cook_world(cook_name,cook_world)value('규동','일식');
insert into cook_world(cook_name,cook_world)value('깻잎장아찌','한식');
insert into cook_world(cook_name,cook_world)value('크로와상','양식');
insert into cook_world(cook_name,cook_world)value('에그타르트','양식');
insert into cook_world(cook_name,cook_world)value('롤케익','양식');
insert into cook_world(cook_name,cook_world)value('식혜','한식');
insert into cook_world(cook_name,cook_world)value('불고기','한식');
insert into cook_world(cook_name,cook_world)value('마늘쫑장아찌','한식');
insert into cook_world(cook_name,cook_world)value('스콘','양식');
insert into cook_world(cook_name,cook_world)value('햄버거','양식');
insert into cook_world(cook_name,cook_world)value('피클','양식');
insert into cook_world(cook_name,cook_world)value('쿠키','양식');
insert into cook_world(cook_name,cook_world)value('감자전','한식');
insert into cook_world(cook_name,cook_world)value('안동찜닭','한식');
insert into cook_world(cook_name,cook_world)value('멘보샤','중식');
insert into cook_world(cook_name,cook_world)value('딤섬','중식');
insert into cook_world(cook_name,cook_world)value('오향장육','중식');
insert into cook_world(cook_name,cook_world)value('만두','중식');
insert into cook_world(cook_name,cook_world)value('돈까스','일식');
insert into cook_world(cook_name,cook_world)value('샤브샤브','일식');
insert into cook_world(cook_name,cook_world)value('오꼬노미야끼','일식');
insert into cook_world(cook_name,cook_world)value('올리브파스타','양식');
insert into cook_world(cook_name,cook_world)value('피쉬앤칩스','양식');
insert into cook_world(cook_name,cook_world)value('타코','양식');
insert into cook_world(cook_name,cook_world)value('또띠아','양식');
insert into cook_world(cook_name,cook_world)value('까르보나라','양식');
insert into cook_world(cook_name,cook_world)value('오믈렛','양식');
insert into cook_world(cook_name,cook_world)value('부추전','한식');
insert into cook_world(cook_name,cook_world)value('연근조림','한식');
insert into cook_world(cook_name,cook_world)value('칼국수','한식');
insert into cook_world(cook_name,cook_world)value('코울슬로','양식');
insert into cook_world(cook_name,cook_world)value('콩자반','한식');
insert into cook_world(cook_name,cook_world)value('타코야키','일식');
insert into cook_world(cook_name,cook_world)value('메밀소바','일식');
insert into cook_world(cook_name,cook_world)value('탄탄면','중식');
insert into cook_world(cook_name,cook_world)value('김밥','한식');
#나라별요리에 관한 샘플입니다.

insert into cook_material(cook_name,cook_materials)value('떡볶이','떡');
insert into cook_material(cook_name,cook_materials)value('떡볶이','고추장');
insert into cook_material(cook_name,cook_materials)value('떡볶이','파');
insert into cook_material(cook_name,cook_materials)value('떡볶이','양파');

insert into cook_material(cook_name,cook_materials)value('짜장면','밀가루');
insert into cook_material(cook_name,cook_materials)value('짜장면','돼지고기');
insert into cook_material(cook_name,cook_materials)value('짜장면','감자');
insert into cook_material(cook_name,cook_materials)value('짜장면','당근');

insert into cook_material(cook_name,cook_materials)value('탕수육','양파');
insert into cook_material(cook_name,cook_materials)value('탕수육','돼지고기');
insert into cook_material(cook_name,cook_materials)value('탕수육','빵가루');
insert into cook_material(cook_name,cook_materials)value('탕수육','기름');
insert into cook_material(cook_name,cook_materials)value('탕수육','전분가루');
insert into cook_material(cook_name,cook_materials)value('탕수육','굴소스');

insert into cook_material(cook_name,cook_materials)value('스파게티','밀가루');
insert into cook_material(cook_name,cook_materials)value('스파게티','토마토');
insert into cook_material(cook_name,cook_materials)value('스파게티','버섯');
insert into cook_material(cook_name,cook_materials)value('스파게티','양파');
insert into cook_material(cook_name,cook_materials)value('스파게티','베이컨');

insert into cook_material(cook_name,cook_materials)value('피자','밀가루');
insert into cook_material(cook_name,cook_materials)value('피자','토마토');
insert into cook_material(cook_name,cook_materials)value('피자','버섯');
insert into cook_material(cook_name,cook_materials)value('피자','양파');
insert into cook_material(cook_name,cook_materials)value('피자','베이컨');
insert into cook_material(cook_name,cook_materials)value('피자','올리브');
insert into cook_material(cook_name,cook_materials)value('피자','치즈');

insert into cook_material(cook_name,cook_materials)value('된장찌개','된장');
insert into cook_material(cook_name,cook_materials)value('된장찌개','두부');
insert into cook_material(cook_name,cook_materials)value('된장찌개','애호박');
insert into cook_material(cook_name,cook_materials)value('된장찌개','양파');
insert into cook_material(cook_name,cook_materials)value('된장찌개','파');

insert into cook_material(cook_name,cook_materials)value('돼지국밥','고기육수');
insert into cook_material(cook_name,cook_materials)value('돼지국밥','머리고기');
insert into cook_material(cook_name,cook_materials)value('돼지국밥','순대');
insert into cook_material(cook_name,cook_materials)value('돼지국밥','파');
insert into cook_material(cook_name,cook_materials)value('돼지국밥','다데기');
insert into cook_material(cook_name,cook_materials)value('돼지국밥','새우젓');
insert into cook_material(cook_name,cook_materials)value('돼지국밥','마늘');

insert into cook_material(cook_name,cook_materials)value('핫도그','빵가루');
insert into cook_material(cook_name,cook_materials)value('핫도그','소시지');
insert into cook_material(cook_name,cook_materials)value('핫도그','기름');

insert into cook_material(cook_name,cook_materials)value('계란찜','계란');
insert into cook_material(cook_name,cook_materials)value('계란찜','파');

insert into cook_material(cook_name,cook_materials)value('라멘','고기육수');
insert into cook_material(cook_name,cook_materials)value('라멘','돼지수육');
insert into cook_material(cook_name,cook_materials)value('라멘','숙주나물');
insert into cook_material(cook_name,cook_materials)value('라멘','파');
insert into cook_material(cook_name,cook_materials)value('라멘','마늘');

insert into cook_material(cook_name,cook_materials)value('초밥','밥');
insert into cook_material(cook_name,cook_materials)value('초밥','생선');
insert into cook_material(cook_name,cook_materials)value('초밥','와사비');

insert into cook_material(cook_name,cook_materials)value('마파두부','두부');
insert into cook_material(cook_name,cook_materials)value('마파두부','돼지고기');
insert into cook_material(cook_name,cook_materials)value('마파두부','마늘');
insert into cook_material(cook_name,cook_materials)value('마파두부','파');
insert into cook_material(cook_name,cook_materials)value('마파두부','두반장');

insert into cook_material(cook_name,cook_materials)value('잔치국수','멸치육수');
insert into cook_material(cook_name,cook_materials)value('잔치국수','계란');
insert into cook_material(cook_name,cook_materials)value('잔치국수','파');
insert into cook_material(cook_name,cook_materials)value('잔치국수','애호박');

insert into cook_material(cook_name,cook_materials)value('규동','소고기');
insert into cook_material(cook_name,cook_materials)value('규동','양파');
insert into cook_material(cook_name,cook_materials)value('규동','생강술');
insert into cook_material(cook_name,cook_materials)value('규동','생강');
insert into cook_material(cook_name,cook_materials)value('규동','밥');

insert into cook_material(cook_name,cook_materials)value('깻잎장아찌','깻잎');
insert into cook_material(cook_name,cook_materials)value('깻잎장아찌','고추');
insert into cook_material(cook_name,cook_materials)value('깻잎장아찌','마늘');

insert into cook_material(cook_name,cook_materials)value('크로와상','강력분');
insert into cook_material(cook_name,cook_materials)value('크로와상','버터');
insert into cook_material(cook_name,cook_materials)value('크로와상','이스트');

insert into cook_material(cook_name,cook_materials)value('에크타르트','강력분');
insert into cook_material(cook_name,cook_materials)value('에크타르트','버터');
insert into cook_material(cook_name,cook_materials)value('에크타르트','이스트');
insert into cook_material(cook_name,cook_materials)value('에크타르트','계란');

insert into cook_material(cook_name,cook_materials)value('롤케익','강력분');
insert into cook_material(cook_name,cook_materials)value('롤케익','버터');
insert into cook_material(cook_name,cook_materials)value('롤케익','이스트');
insert into cook_material(cook_name,cook_materials)value('롤케익','슈크림');

insert into cook_material(cook_name,cook_materials)value('식혜','엿기름');
insert into cook_material(cook_name,cook_materials)value('식혜','밥');

insert into cook_material(cook_name,cook_materials)value('불고기','소고기');
insert into cook_material(cook_name,cook_materials)value('불고기','양파');
insert into cook_material(cook_name,cook_materials)value('불고기','대파');
insert into cook_material(cook_name,cook_materials)value('불고기','양파');

insert into cook_material(cook_name,cook_materials)value('마늘쫑장아찌','마늘쫑');
insert into cook_material(cook_name,cook_materials)value('마늘쫑장아찌','마늘');
insert into cook_material(cook_name,cook_materials)value('마늘쫑장아찌','맛술');

insert into cook_material(cook_name,cook_materials)value('스콘','강력분');
insert into cook_material(cook_name,cook_materials)value('스콘','버터');
insert into cook_material(cook_name,cook_materials)value('스콘','이스트');

insert into cook_material(cook_name,cook_materials)value('햄버거','빵가루');
insert into cook_material(cook_name,cook_materials)value('햄버거','소고기');
insert into cook_material(cook_name,cook_materials)value('햄버거','양파');
insert into cook_material(cook_name,cook_materials)value('햄버거','토마토');
insert into cook_material(cook_name,cook_materials)value('햄버거','양상추');
insert into cook_material(cook_name,cook_materials)value('햄버거','케첩');
insert into cook_material(cook_name,cook_materials)value('햄버거','마요네즈');

insert into cook_material(cook_name,cook_materials)value('피클','오이');
insert into cook_material(cook_name,cook_materials)value('피클','피클링스파이스');

insert into cook_material(cook_name,cook_materials)value('쿠키','강력분');
insert into cook_material(cook_name,cook_materials)value('쿠키','버터');
insert into cook_material(cook_name,cook_materials)value('쿠키','이스트');
insert into cook_material(cook_name,cook_materials)value('쿠키','초콜릿');

insert into cook_material(cook_name,cook_materials)value('감자전','감자');
insert into cook_material(cook_name,cook_materials)value('감자전','밀가루');
insert into cook_material(cook_name,cook_materials)value('감자전','부침가루');

insert into cook_material(cook_name,cook_materials)value('안동찜닭','닭고기');
insert into cook_material(cook_name,cook_materials)value('안동찜닭','감자');
insert into cook_material(cook_name,cook_materials)value('안동찜닭','당면');
insert into cook_material(cook_name,cook_materials)value('안동찜닭','양파');
insert into cook_material(cook_name,cook_materials)value('안동찜닭','파');
insert into cook_material(cook_name,cook_materials)value('안동찜닭','고추장');
insert into cook_material(cook_name,cook_materials)value('안동찜닭','당근');
insert into cook_material(cook_name,cook_materials)value('안동찜닭','버섯');

insert into cook_material(cook_name,cook_materials)value('멘보샤','식빵');
insert into cook_material(cook_name,cook_materials)value('멘보샤','새우');
insert into cook_material(cook_name,cook_materials)value('멘보샤','빵가루');
insert into cook_material(cook_name,cook_materials)value('멘보샤','기름');

insert into cook_material(cook_name,cook_materials)value('딤섬','밀가루');
insert into cook_material(cook_name,cook_materials)value('딤섬','돼지고기');
insert into cook_material(cook_name,cook_materials)value('딤섬','쪽파');

insert into cook_material(cook_name,cook_materials)value('오향장육','수육');
insert into cook_material(cook_name,cook_materials)value('오향장육','올리브잎');
insert into cook_material(cook_name,cook_materials)value('오향장육','통후추');
insert into cook_material(cook_name,cook_materials)value('오향장육','정향');
insert into cook_material(cook_name,cook_materials)value('오향장육','양파');
insert into cook_material(cook_name,cook_materials)value('오향장육','대파');
insert into cook_material(cook_name,cook_materials)value('오향장육','생강');
insert into cook_material(cook_name,cook_materials)value('오향장육','청주');

insert into cook_material(cook_name,cook_materials)value('만두','밀가루');
insert into cook_material(cook_name,cook_materials)value('만두','돼지고기');
insert into cook_material(cook_name,cook_materials)value('만두','쪽파');

insert into cook_material(cook_name,cook_materials)value('돈까스','빵가루');
insert into cook_material(cook_name,cook_materials)value('돈까스','돼지고기');
insert into cook_material(cook_name,cook_materials)value('돈까스','계란');

insert into cook_material(cook_name,cook_materials)value('샤브샤브','고기육수');
insert into cook_material(cook_name,cook_materials)value('샤브샤브','버섯');
insert into cook_material(cook_name,cook_materials)value('샤브샤브','숙주나물');
insert into cook_material(cook_name,cook_materials)value('샤브샤브','양상추');
insert into cook_material(cook_name,cook_materials)value('샤브샤브','대파');

insert into cook_material(cook_name,cook_materials)value('오꼬노미야끼','양배추');
insert into cook_material(cook_name,cook_materials)value('오꼬노미야끼','부침가루');
insert into cook_material(cook_name,cook_materials)value('오꼬노미야끼','계란');

insert into cook_material(cook_name,cook_materials)value('올리브파스타','파스타면');
insert into cook_material(cook_name,cook_materials)value('올리브파스타','올리브유');
insert into cook_material(cook_name,cook_materials)value('올리브파스타','베이컨');
insert into cook_material(cook_name,cook_materials)value('올리브파스타','양파');

insert into cook_material(cook_name,cook_materials)value('피쉬앤칩스','부침가루');
insert into cook_material(cook_name,cook_materials)value('피쉬앤칩스','생선고기');
insert into cook_material(cook_name,cook_materials)value('피쉬앤칩스','나쵸');
insert into cook_material(cook_name,cook_materials)value('피쉬앤칩스','감자');

insert into cook_material(cook_name,cook_materials)value('타코','토르티야');
insert into cook_material(cook_name,cook_materials)value('타코','양상추');
insert into cook_material(cook_name,cook_materials)value('타코','버섯');
insert into cook_material(cook_name,cook_materials)value('타코','소고기');
insert into cook_material(cook_name,cook_materials)value('타코','사워크림');

insert into cook_material(cook_name,cook_materials)value('또띠아','토르티야');
insert into cook_material(cook_name,cook_materials)value('또띠아','양상추');
insert into cook_material(cook_name,cook_materials)value('또띠아','버섯');
insert into cook_material(cook_name,cook_materials)value('또띠아','소고기');
insert into cook_material(cook_name,cook_materials)value('또띠아','살사소스');
insert into cook_material(cook_name,cook_materials)value('또띠아','치즈');

insert into cook_material(cook_name,cook_materials)value('까르보나라','파스타면');
insert into cook_material(cook_name,cook_materials)value('까르보나라','생크림');
insert into cook_material(cook_name,cook_materials)value('까르보나라','우유');
insert into cook_material(cook_name,cook_materials)value('까르보나라','베이컨');
insert into cook_material(cook_name,cook_materials)value('까르보나라','양파');

insert into cook_material(cook_name,cook_materials)value('오믈렛','계란');

insert into cook_material(cook_name,cook_materials)value('연근조림','연근');

insert into cook_material(cook_name,cook_materials)value('부추전','부추');
insert into cook_material(cook_name,cook_materials)value('부추전','부침가루');
insert into cook_material(cook_name,cook_materials)value('부추전','고추');

insert into cook_material(cook_name,cook_materials)value('칼국수','밀가루');
insert into cook_material(cook_name,cook_materials)value('칼국수','멸치육수');
insert into cook_material(cook_name,cook_materials)value('칼국수','애호박');
insert into cook_material(cook_name,cook_materials)value('칼국수','계란');
insert into cook_material(cook_name,cook_materials)value('칼국수','대파');

insert into cook_material(cook_name,cook_materials)value('코울슬로','양배추');
insert into cook_material(cook_name,cook_materials)value('코울슬로','파프리카');
insert into cook_material(cook_name,cook_materials)value('코울슬로','당근');
insert into cook_material(cook_name,cook_materials)value('코울슬로','마요네즈');

insert into cook_material(cook_name,cook_materials)value('콩자반','검은콩');
insert into cook_material(cook_name,cook_materials)value('콩자반','물엿');

insert into cook_material(cook_name,cook_materials)value('타코야키','타코야키파우더');
insert into cook_material(cook_name,cook_materials)value('타코야키','문어다리');
insert into cook_material(cook_name,cook_materials)value('타코야키','가츠오부시');
insert into cook_material(cook_name,cook_materials)value('타코야키','쪽파');

insert into cook_material(cook_name,cook_materials)value('메밀소바','메밀면');
insert into cook_material(cook_name,cook_materials)value('메밀소바','쯔유');

insert into cook_material(cook_name,cook_materials)value('탄탄면','라면');
insert into cook_material(cook_name,cook_materials)value('탄탄면','두반장');
insert into cook_material(cook_name,cook_materials)value('탄탄면','굴소스');
insert into cook_material(cook_name,cook_materials)value('탄탄면','고기육수');
insert into cook_material(cook_name,cook_materials)value('탄탄면','땅콩');

insert into cook_material(cook_name,cook_materials)value('김밥','김');
insert into cook_material(cook_name,cook_materials)value('김밥','밥');
insert into cook_material(cook_name,cook_materials)value('김밥','단무지');
insert into cook_material(cook_name,cook_materials)value('김밥','우엉');
insert into cook_material(cook_name,cook_materials)value('김밥','소시지');
#요리재료 샘플입니다.
