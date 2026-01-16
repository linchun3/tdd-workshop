def add(numbers: str) -> int:
    if not numbers:
        return 0
    if "," not in numbers:
        return int(numbers)
    nums = numbers.split(",")
    total = 0
    for num in nums:
        total += int(num)
    return total
