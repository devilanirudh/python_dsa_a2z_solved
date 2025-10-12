class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            to_find = target - nums[i]
            if to_find in hash_map and i!= hash_map.get(to_find):
                return [hash_map.get(to_find),i]
            hash_map.update({nums[i]:i})

        