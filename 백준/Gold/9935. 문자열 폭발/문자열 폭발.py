'''
폭발 문자열이 폭발하면 그 문자는 문자열에서 사라짐, 남은 문자열은 합쳐진다
폭발은 다음과 같은 과정으로 진행

문자열이 폭발 문자열을 포함하고 있으면 -> 모든 폭발 문자열이 폭발, 남은 문자열을 순서대로 이어 붙여
새로운 문자열을 만든다

새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
폭발은 폭발 문자열이 문자열에 없을 때까지 계속됨

모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려 함
남아 있는 문자가 없는 경우가 있음.
이때는 "FRULA"을 출력

폭발 문자열은 같은 문자를 두 개 이상 포함 x

예제 입력 1
mirkovC4nizCC44
C4

mirkov(C4)niz(C(C4)4)

-> mirkovniz


(12ab)(1(12ab)2ab)
12ab
-> 남은 문자열이 없으므로 "FRULA"
'''
import sys

targetInput = list(sys.stdin.readline().rstrip())
bomb = sys.stdin.readline().rstrip()
bombdata = bomb
bomb = list(bomb)
result = []

index = 0

for index in range(len(targetInput)):
    result.append(targetInput[index])
    if targetInput[index] == bomb[-1] and len(targetInput) >= len(bomb):
        if ''.join(result[-len(bomb):]) == bombdata:
            del result[-len(bomb):]

if len(result) == 0:
    print("FRULA")
else:
    resultData = "".join(result)
    print(resultData)