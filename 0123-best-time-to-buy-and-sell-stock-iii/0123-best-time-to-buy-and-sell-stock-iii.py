class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)

        if n <= 1:
            return 0

        left = [0] * n

        min_price = prices[0]

        for i in range(1, n):
            min_price = min(min_price, prices[i]) # 현재가 매도일
            left[i] = max(
                left[i - 1],
                prices[i] - min_price
            )

        right = [0] * n

        max_price = prices[-1]

        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i]) # 현재가 매수일
            right[i] = max(
                right[i + 1],
                max_price - prices[i]
            )

        answer = 0

        for i in range(n):
            answer = max(
                answer,
                left[i] + right[i]
            )

        return answer