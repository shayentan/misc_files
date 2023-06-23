i = [1,2,3,4,5,6]
# print(len(i))

target = 6


def check_sum(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            a = nums[i] + nums[j]
            if a == k:
                print(nums[i], nums[j])
                return True
    return False


print(check_sum(i, 6))
