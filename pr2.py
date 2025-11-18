def concatenate_digits_no_join(digit_list):
    result = ""
    for digit in digit_list:
        result += digit  # add each digit to the result string
    return result


digits = ['1', '2', '3', '4', '5']
print(concatenate_digits_no_join(digits))  # Output: '12345'

