class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]

        roman_num = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        result = 0
        tmp = 0

        for key in s:

            value = roman_num[key]

            if tmp > value:
                result -= value
            else:
                result += value
                tmp = value
            
        return result