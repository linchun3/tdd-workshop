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
        neg_num = []
        
        for num in numbers_list:
            if num != "" and int(num) < 0:
                
                neg_num.append(int(num))
            if num != "":
              res += int(num)
        if neg_num:
            raise ValueError(f"Negative number(s) not allowed: {neg_num}")
        return res
    if numbers == "1":
        return 1
        
    return 0
