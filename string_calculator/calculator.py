def add(numbers: str) -> int:
    if not numbers:
        return 0

    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
        numbers = numbers.replace(delimiter, ",")
    numbers = numbers.replace("\n", ",")
    if numbers[-1] == ",":
        raise ValueError("separators should not appear at the conclusion")
    if "," not in numbers:
        return int(numbers)
    nums = numbers.split(",")
    total = 0
    for num in nums:
        total += int(num)
    return total
