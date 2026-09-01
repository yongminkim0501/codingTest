class Solution:
    def longestConsecutive(self, nums) -> int:
        search_dict = {}
        for num in nums:
            search_dict[num] = True
        
        nums = search_dict.keys()
        max_count = 0
        cur_count = 0
        for num in nums:
          flag = num - 1
          if flag not in nums:
            cur_data = num
            while cur_data in nums:
              cur_count += 1
              cur_data += 1
            if max_count < cur_count :
              max_count = cur_count
            cur_count = 0
        return max_count