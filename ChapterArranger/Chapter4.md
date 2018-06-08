# 파이 크러스트: 코드 구조 #

* 라인을 유지할 땐 \ 를 사용 

 ex > test + 'test' + \
 'test2' + \
 'test3'
 
* if, else 는 파이썬의 선언문, elif는 else if // 괄호 대신 콜론 사용
  > if jenny:
        if jeju:
          print(True)
        else: 
          print(False)  
   
   
* True, False

  ** false로 간주되는 경우
  > null, 정수 0, 부동소수점 0.0, 빈 문자열 '', 빈 리스트 [], 빈 튜플 (), 빈 딕셔너리 {}, 빈 셋 set()
  
  
* zip() 함수로 여러 시퀀스를 병렬로 순회 가능

 > days = ['Monday', 'Tuesday]
   fruits = ['cherry', 'orange', 'banana']
   drinks = ['coffee', 'tea']
   for day, fruit, drink in zip(days, fruits, drinks);
   print(day, ":drink", drink, ":fruit" fruit)
   
* 숫자 시퀀스 생성은 range() range(start, stop, step) -step은 점프값
 
* 컴프리헨션은 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 콤팩트한 방법

* 반복문과 조건 테스트를 결합할 수 있음

* 아 그리고 튜플은 컴프리핸션이 없다

* 함수는 두가지 작업을 실행하는데 정의하기, 호출하기 임

* def 함수 이름 괄호 콜론

* None은 아무것도 없다는 것을 뜻하는 파이썬의 특별한 값
