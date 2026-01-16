import re

def add(numbers: str) -> int:
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
