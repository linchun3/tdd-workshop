def add(numbers: str) -> int:
    numbers = numbers.replace("\n", ",")
    print(numbers)
    if not numbers:
        return 0
    if "," not in numbers:
        return int(numbers)
    nums = numbers.split(",")
    total = 0
    for num in nums:
        total += int(num)
    return total
