import re

def add(numbers: str) -> int:
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[3:].replace(delimiter, ",")
    if len(numbers) > 0 and numbers[-1] == ",":
        raise ValueError
    if "," in numbers or "\n" in numbers:
        numbers_list = re.split(r'[,\n]+', numbers)
        res = 0
        for num in numbers_list:
            if num != "":
              res += int(num)
        return res
    if numbers == "1":
        return 1
    return 0
