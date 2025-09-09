class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Edge case: empty needle should return 0
        if needle == "":
            return 0
        
        # Use Python's built-in find() method
        return haystack.find(needle)
