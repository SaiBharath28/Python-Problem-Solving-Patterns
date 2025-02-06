def three_sum(nums):
    nums.sort()  # Step 1: Sort the array
    result = []

    for i in range(len(nums) - 2):  # Step 2: Iterate with `i`
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate `nums[i]`
            continue

        left, right = i + 1, len(nums) - 1  # Step 3: Two pointers

        while left < right:  # Step 4: Finding triplets
            total = nums[i] + nums[left] + nums[right]

            if total == 0:  # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:  # Skip duplicates
                    left += 1
                while left < right and nums[right] == nums[right + 1]:  # Skip duplicates
                    right -= 1

            elif total < 0:  # Increase sum
                left += 1
            else:  # Decrease sum
                right -= 1

    return result


# Example Usage
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))  # Expected Output: [[-1, -1, 2], [-1, 0, 1]]
