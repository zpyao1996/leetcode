from itertools import combinations

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = set()
        parenthesis_stack = []
        all_left, all_right = [], []
        for idx, char in enumerate(s):
            if char == '(':
                all_left.append(idx)
                parenthesis_stack.append(['(', idx])
            elif char == ')':
                all_right.append(idx)
                if parenthesis_stack and parenthesis_stack[-1][0] == '(':
                    parenthesis_stack.pop()
                else:
                    parenthesis_stack.append([')', idx])
        left_parenthesis, right_parenthesis = [[[char, idx] for
                               [char,idx] in parenthesis_stack if
                        char == symbol] for symbol in ['(', ')']]
        left_indices = [idx for [_, idx] in left_parenthesis]
        left_to_remove = []
        if left_indices:
            min_left = left_indices[0]
            left_to_remove = [idx for idx in all_left if idx >= min_left]
        right_indices = [idx for [_, idx] in right_parenthesis]
        right_to_remove = []
        if right_indices:
            max_right = right_indices[-1]
            right_to_remove = [idx for idx in all_right if idx <= max_right]
        num_left, num_right = len(left_parenthesis), len(right_parenthesis)
        for left_removed in combinations(left_to_remove, num_left):
            for right_removed in combinations(right_to_remove, num_right):
                removed = left_removed + right_removed
                new_s = ''.join([char for idx, char in enumerate(s) if idx not in removed])
                ans.add(new_s)
        return list(ans)


sol = Solution()
a = "(()("
print(sol.removeInvalidParentheses(a))