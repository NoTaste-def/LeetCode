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
    def resursion(x, left, right):
        if left >= right:
            return True
        if x[left] != x[right]:
            return False
        return resursion(x, left+1, right-1)

    return resursion(str(x), 0, len(str(x))-1)