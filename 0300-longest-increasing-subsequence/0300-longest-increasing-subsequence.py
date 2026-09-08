class Solution:
    def lengthOfLIS(self, nums) -> int:
      n = len(nums)
      arr = [1 for _ in range(n)]
      
      for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                arr[i] = max(arr[i], arr[j]+1)
      
      result = max(arr)
      
      return result
