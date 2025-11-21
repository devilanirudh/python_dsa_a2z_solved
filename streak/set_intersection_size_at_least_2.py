class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end ascending, and if tie, start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # These will store the last two selected numbers
        a = -1
        b = -1
        result = 0

        for start, end in intervals:
            # Case 1: No selected numbers are in this interval
            if b < start:
                # pick the last two possible numbers inside this interval
                a = end - 
                b = end
                result += 2

            # Case 2: Only one selected number (b) is inside the interval
            elif a < start:
                # pick one more number as far right as possible
                a = b
                b = end
                result += 1

            # Case 3: both a and b are already inside interval → nothing to do

        return result
