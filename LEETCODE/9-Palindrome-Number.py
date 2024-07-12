# class Solution(object):
#     def isPalindrome(self, x):
#         x = str(x)
#         n = x[::-1]
#         if x == n:
#             return True
#         else:
#             return False

class Solution(object):
  def isPalindrome(self, x):
    if x < 0 :
        return False
    def recursion(x, left, right):
        if left >= right:
            return True
        if x[left] != x[right]:
            return False
        return recursion(x, left+1, right-1)

    return recursion(str(x), 0, len(str(x))-1)
