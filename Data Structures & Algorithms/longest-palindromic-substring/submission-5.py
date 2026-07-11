class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        """
        Finds the longest palindromic substring in the given string.
        Uses center expansion for O(n^2) time and O(1) space complexity.
        """
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")
        if len(s) == 0:
            return ""

        start, end = 0, 0  # Track the best palindrome boundaries

        def expand_from_center(left: int, right: int) -> tuple[int, int]:
            """Expand around the center and return the start and end indices of the palindrome."""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the indices of the palindrome boundaries
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd-length palindrome
            l1, r1 = expand_from_center(i, i)
            # Even-length palindrome
            l2, r2 = expand_from_center(i, i + 1)

            # Update the best palindrome if found longer
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]


        