'''
나무 m미터 필요

절단기에 높이 H를 지정
높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라감.
한 줄에 연속해있는 나무를 모두 절단
나무 높이가 20 15 10 17
높이 15로 지정시
15 15 10 15가 됨

-> 길이 5, 2인 나무를 들고 집에감 => 7미터
나무를 필요한 만큼만 집에 가져가려고 함
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값
첫줄 : 나무의 수 n, 집으로 가져가려 하는 나무의 길이 m
두번째줄 : 나무의 높이

4 7
20 15 10 17

출력 : 15
'''
import sys
def main():
    n, m = map(int, input().split())
    trees = list(map(int, sys.stdin.readline().split(" ")))
    start = 0
    end = max(trees)

    while start<=end:
        mid = (end + start) // 2

        goal_result = 0
        for tree in trees:
            if tree - mid > 0:
                goal_result += (tree - mid)

        if goal_result >= m:
            result = mid
            start = mid + 1
        else:
            end = mid -1

    print(result)

if __name__ == "__main__":
    main()