# Kata 2 – String Calculator

## Overview
The exercise requires creating a simple calculator that processes a `String` input and returns an `integer` result.

**Method Signature:** `int Add(string numbers)`

## Requirements

### Step 1: Basic Addition
The method should accept up to two numbers separated by commas and return their sum. Valid inputs include:
- Empty string: `""` (returns 0)
- One number: `"1"` (returns 1)
- Two numbers: `"1,2"` (returns 3)

Begin with the simplest case and progress methodically, following TDD principles of minimal code and refactoring.

### Step 2: Multiple Arguments
Extend the function to handle an unknown quantity of arguments rather than just two.

### Step 3: Flexible Separators
Support newlines alongside commas as delimiters.
- Example: `"1,2\n3"` should equal 6.
- Note: `"2,\n3"` represents invalid input.

### Step 4: End-of-String Validation
Reject inputs where separators appear at the conclusion, such as `"1,2,"`, which should trigger an error response.

### Step 5: Custom Delimiters
Enable custom delimiter specification using the format `//[delimiter]\n[numbers]`.
- Example: `"//;\n1;3"` returns 4.
- Example: `"//|\n1|2|3"` returns 6.

Invalid mixed delimiters should produce specific error messages.

### Step 6: Negative Numbers
Calling `Add` with negative numbers will return an error message: `"Negative number(s) not allowed: <negativeNumbers>"`.
- If there are multiple negative numbers, show all of them in the error message, separated by commas.

### Step 7: Multiple Errors
Calling `Add` with multiple errors will return all error messages separated by newlines.
- Example: `"//|\n1|2,-3"` might return:
  ```
  Negative number(s) not allowed: -3
  '|' expected but ',' found at position 3.
  ```

### Step 8: Ignore Large Numbers
Numbers bigger than 1000 should be ignored.
- Example: `2 + 1001 = 2`
