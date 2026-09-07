class Solution:
    def maximalSquare(self, matrix) -> int:
        
        def get_min_value(i,j):
          min_value = min(arr[i-1][j], arr[i-1][j-1], arr[i][j-1])
          return min_value
        
        def is_check(i,j):
          if matrix[i-1][j] == "0" and matrix[i-1][j-1] == "0" and matrix[i][j-1] == "0":
            return False
          return True

        n_row = len(matrix)
        n_col = len(matrix[0])

        arr = [[0 for _ in range(n_col+1)]for idx in range(n_row)]
        for row in range(n_row):
          for col in range(n_col):
            if row == 0 or col == 0:
              arr[row][col] = int(matrix[row][col])
            else:
              if matrix[row][col] == "1":
                if is_check(row, col):
                  arr[row][col] = get_min_value(row, col)+1
                else:
                  arr[row][col] += 1
                  #arr[row][col] = -1
              else:
                arr[row][col] = int(matrix[row][col])

            arr[row][-1] = max(arr[row])

        cur_max = 0

        for idx in range(n_row):
          max_value = max(cur_max, arr[idx][-1])
          cur_max = max_value


        return max_value**2