class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        array1=[]
        array2=[]
        for i in s:
            array1.append(i)
        for j in t:
            array2.append(j)
        array1.sort()
        array2.sort()
        if array1== array2:
            return True
        else:
            return False

        