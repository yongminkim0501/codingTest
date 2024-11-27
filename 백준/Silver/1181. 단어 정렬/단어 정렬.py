import sys
n = int(input())
word = set()
for i in range(n):
  word.add(sys.stdin.readline())

sort_word = sorted(word, key=lambda x : (len(x), x))

for i in sort_word:
  print(i, end='')