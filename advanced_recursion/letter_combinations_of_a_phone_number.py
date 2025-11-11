class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        nums = []
        for ch in digits:
            nums.append(dic[ch])
        import itertools
        result = [''.join(p) for p in itertools.product(*nums)]

        return result
         