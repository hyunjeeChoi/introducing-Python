# 흘러가는 데이터 #

 * 플랫 파일 : 파일 이름으로 저장된 바이트 시퀀스
 
 ```
  fileobj = open(filename, mode)

 ``` 
 
 fileobj > 반환되는 파일 객체
 mode - 파일타입과 파일로 무엇을 할지 명시하는 문자열
 
 * write() > 쓰기 
 * read() readline() -라인 단위 readlines() > 텍스트 파일 읽기
 * whit > 파일 닫기 >> with.open('', ' ') as fout:
 * seek() > 파일 찾기 
 