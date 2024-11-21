# 알파벳 소문자로 이루어진 n개의 단어가 들어오면 아래와 같은 조건에 따라 정렬
# 길이가 짧은 것부터
# 길이가 같으면 사전 순

n = int(input())

k = []
def check(s):
  flag = True
  c = []
  c.append(s[0])
  for i in range(1,len(s)):
    if s[i-1] == s[i] : # 이전과 문자가 같다면
      continue
    else: #이전과 문자가 다르다면
      for j in range(len(c)):
        if c[j] == s[i]: # 이전에 나온적이 있다면
          flag = False
          break
        else: # 이전에 나온적이 없다면
         c.append(s[i])
  return flag


count = 0
for i in range(n):
  s = input()
  if check(s) == True:
    count += 1

print(count)