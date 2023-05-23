def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        for num in nums:
            if nums[low] == nums[target]:
                return num
            low += 1

# Example usage
nums = [4, 5, 6, 7, 0, 1, 2]
target = 5
result = search(nums, target)
print(result)
