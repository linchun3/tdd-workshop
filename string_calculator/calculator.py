def add(numbers: str) -> int:
    if not numbers:
        return 0

    numbers = numbers.replace("\n", ",")
    if numbers[-1] == ",":
        raise ValueError("separators should not appear at the conclusion")
    if "," not in numbers:
        return int(numbers)
    nums = numbers.split(",")
    print(nums)
    total = 0
    for num in nums:
        total += int(num)
    return total
