'''
좌표 압축
n개의 좌표 x_1 ~ x_n

x_i를 좌표 압축한 결과 x'_i의 값은 x_i > x_j 
를 만족하는 서로 다른 좌표 x_j의 개수와 같아야 함

x_1, x_2, ..., x_n에 좌표 압축을 적용한 결과 x'_1 ~ x'_n을 출력해보자

입력 :
5
2 4 -10 4 -9
출력 : 
2 3 0 3 1

arr.sort()
한 후,
index값 반환
'''
n = int(input())
arr = list(map(int,input().split()))
brr = sorted(list(set(arr)))
result = []

'''for i in arr:
    for j in range(len(brr)):
        if i == brr[j] :
            result.append(j)
# enumerate 순서가 있는 
print(*result)'''

value_to_index = {value: index for index, value in enumerate(brr)}

# 원본 배열의 각 원소를 압축된 좌표로 변환
result = [value_to_index[x] for x in arr]

print(*result)