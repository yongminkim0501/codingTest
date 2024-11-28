'''
A+	4.5
A0	4.0
B+	3.5
B0	3.0
C+	2.5
C0	2.0
D+	1.5
D0	1.0
F	0.0
p/f => 등급이 p인 과목은 계산에서 제외해야함
전공 평점 : 학점 * 과목평점의 합을 학점의 총합으로 나눈 값

20줄에 걸쳐 치훈이가 수강한 전공 과목의 과목명, 학점, 등급이 공백으로 구분되어 주어짐
'''
sum_t = 0
total_num = 0
for i in range (20):
  _, num, score = input().split(" ")
  num = float(num)
  if score == 'A+' : score = 4.5
  elif score == 'A0' : score = 4.0
  elif score == 'B+' : score = 3.5
  elif score == 'B0' : score = 3.0
  elif score == 'C+' : score = 2.5
  elif score == 'C0' : score = 2.0
  elif score == 'D+' : score = 1.5
  elif score == 'D0' : score = 1.0
  elif score == 'F' : score = 0.0
  elif score == 'P' : continue
  sum_t += (num*score)
  total_num += num
  result = sum_t / total_num
print(f"{result:.6f}")