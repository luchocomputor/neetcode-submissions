class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))

        max_len = 1
        streak = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                streak += 1
            else:
                streak = 1

            max_len = max(max_len, streak)

        return max_len