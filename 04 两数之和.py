给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target - nums[i] in nums and i != nums.index(target-nums[i])):
                return [i, nums.index(target-nums[i])]

test = Solution()
result = test.twoSum([2,7,11,15], 9)
print(result)


解题的大致思路：
1、让 下标i 在 len(nums) 范围内遍历
2、判断 目标值 - i下标对应的的值nums[i] 是否在nums列表中
3、并且判断 这个值对应的下标是否与 i 相等
4、输出两个下标值

