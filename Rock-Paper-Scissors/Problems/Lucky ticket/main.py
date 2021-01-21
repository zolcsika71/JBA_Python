# Save the input in this variable
ticket = str(input())

# Add up the digits for each half


def sum_digits(digits):
    result = 0
    for digit in digits:
        result += int(digit)

    return result


half1 = sum_digits(ticket[:3])
half2 = sum_digits(ticket[-3:])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
