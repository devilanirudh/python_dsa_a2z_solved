class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(st, open_count, close_count):
            if len(st) == 2 * n:
                res.append(st)
                return
            if open_count < n:
                backtrack(st + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(st + ')', open_count, close_count + 1)

        backtrack("", 0, 0)
        return res
