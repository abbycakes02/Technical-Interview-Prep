class Solution(object):
    def isPalindrome(self, s):
        array_str = [i.lower() for i in s if i.isalnum()]
        start = 0
        end = len(array_str) - 1
        while start < end :
            if array_str[start] != array_str[end]:
                return False
            start +=1
            end -= 1
        return True
    

class Two_Line_Solution(object):
    def isPalindrome(self, s):
        array_str = [i.lower() for i in s if i.isalnum()]
        return all (array_str[i] == array_str[-(i + 1)] for i in range(len(array_str)//2))