def has_33(nums):
    nums_str = ""
    for num in nums:
        nums_str += str(num)
    return "33" in nums_str
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print("Contains 33:", has_33(numbers))