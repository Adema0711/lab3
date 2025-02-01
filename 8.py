def has_007(nums):
    sequence = "007"
    nums_str = ""
    for num in nums:
        nums_str += str(num)
    return sequence in nums_str
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print("Contains 007:", has_007(numbers))