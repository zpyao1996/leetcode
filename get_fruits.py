class Solution:
    def get_fruits(self, fruits):
        if not fruits:
            return 0
        two_fruit_set, two_fruit_idx = {fruits[0]}, 0
        one_fruit, one_fruit_idx = fruits[0], 0
        c_max = 1
        for idx, fruit in enumerate(fruits[1:]):
            if fruit == one_fruit:
                pass
            else:
                if fruit in two_fruit_set:
                    pass
                elif len(two_fruit_set) == 1:
                    two_fruit_set.add(fruit)
                else:
                    two_fruit_set = set([one_fruit, fruit])
                    two_fruit_idx = one_fruit_idx
                one_fruit, one_fruit_idx = fruit, idx + 1
            c_max = max(idx + 2 - two_fruit_idx, c_max)
        return c_max

sol=Solution()
print(sol.get_fruits([1,2,1,3,4,3,5,1,2]))

