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
   