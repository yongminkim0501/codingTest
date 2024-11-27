# fizzbuzz
# i가 3의 배수이면서 5의 배수이면 FizzBuzz
# i가 3의 배수이지만 5의 배수가 아니면 Fizz
# i가 3의 배수가 아니지만 5의 배수이면 Buzz
# i가 3의 배수도, 5의 배수도 아니면 i그대로 출력
# 입력 데이터는 연속으로 출력된 세 개의 문자열이 한 줄에 하나씩 주어짐.
# 각 문자열의 길이는 8이하
# 출력 : 연속으로 출력된 세 개의 문자열 다음에 올 문자열을 출력
# 여러 문자열이 올 수 있는 경우, 아무거나 하나 출력

# 예제 입력
# fizz - buzz - 11 - (12) : 3의 배수 임으로 fizz
# 980803 980804 fizzbuzz -> 980806 (이건 그대로 출력) 

# 힌트
s = [1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz",11,"Fizz",13,14,"FizzBuzz",16,17,"Fizz",19,"Buzz"] # 이렇게 반복
a = []
k = 0
num = 0
count = 0
tmp_idx = 0
for i in range(3):
  tmp = input()
  if tmp != "Fizz" and tmp != "Buzz" and tmp != "FizzBuzz":
    count = i # 몇 번째 등장하는 수 인지, 실제 수 - 1 상태
    k = int(tmp)
    num = k // 15 # k를 15로 나눈 몫 (니중에 다음에 올 문자열 예측할 때 사용)
    tmp_idx = k % 15 - 1 # 나중에 s의 어느 위치에 있는지를 나타낼 것

    
tmp = s[tmp_idx + 3 - count] #만약 count 값이 2라면, 정수의 값이 2번째로 나타난 것, 다음 숫자 예측
if tmp != "Fizz" and tmp != "Buzz" and tmp != "FizzBuzz":
  print(tmp+num*15)
else:
  print(tmp)

  #fizz, buzz, 11