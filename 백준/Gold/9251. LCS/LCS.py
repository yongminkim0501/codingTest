str1 = input()
str2 = input()

if len(str1) > len(str2):
    str1, str2 = str2, str1

prev = [0] * (len(str1) + 1)
current = [0] * (len(str1) + 1)

for i in range(len(str2)):
    for j in range(len(str1)):
        if str1[j] == str2[i]:
            current[j + 1] = prev[j] + 1
        else:
            current[j + 1] = max(current[j], prev[j + 1])
    prev, current = current, prev

print(prev[len(str1)])