'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        length=len(s)
        ans=[[0 for _ in range(length)] for _ in range(length)]
        cmax=1
        cans=[0,1]
        for delta in range(1,length+1):
            for i in range(length+1-delta):
                if (delta <3 or ans[i+1][i+delta-2]==1) and s[i]==s[i+delta-1]:
                    ans[i][i+delta-1]=1
                    if delta>cmax:
                        cmax=delta
                        cans=[i,i+delta]
        return s[cans[0]:cans[1]]
'''


# Manacher algorithm
# http://en.wikipedia.org/wiki/Longest_palindromic_substring
class Solution:
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]
sol=Solution()
print(sol.longestPalindrome('12321'))


