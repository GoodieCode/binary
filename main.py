from math import floor

def decimalToBinary(number:int) -> list:
    remainders:list = []
    last_number:int = number

    while last_number > 0:
        remainder = last_number % 2
        remainders.append(remainder)

        last_number = last_number // 2

    return remainders[::-1] #  [::-1] reverse the list
    
def binaryToDecimal(binary):
    binary = binary[::-1] #[::-1] reverse the list

    calculation = 0

    for i in range(len(binary)):
        digit = binary[i] * 2 
        
        power = digit ** i

        calculation += power

    
    return calculation

calc = decimalToBinary(1000)

binaryToDecimal(calc)

print(binaryToDecimal(calc))