class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map={}
        prefix_sum = 0
        count = 0
        hash_map.update({0:1})
        for i in range(len(nums)):
            prefix_sum = prefix_sum+nums[i]
            to_check = prefix_sum-k
            if to_check in hash_map:
                f = hash_map.get(to_check)
                count = count +f
            if prefix_sum in hash_map:
                g = hash_map.get(prefix_sum)
                hash_map.update({prefix_sum:g+1})
            if prefix_sum not in hash_map:
                hash_map.update({prefix_sum:1})
        return count

            