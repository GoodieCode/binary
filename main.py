from math import floor

def decimalToBinary(number:int) -> list:
    remainders:list = []
    last_number:int = number

    while last_number > 0:
        remainder = last_number % 2
        remainders.append(remainder)

        last_number = last_number // 2

    return remainders[::-1] #  [::-1] reverse the list
    
def binaryToDecimal(binary:list):
    binary = binary[::-1] #[::-1] reverse the list

    calculation = 0

    for i in range(len(binary)):
        digit = binary[i] * 2 
        
        power = digit ** i

        calculation += power

    
    return calculation

def notOperator(binary_list:list) -> list:
    for i in range(len(binary_list)):
        
        # Flips the bits 
        if binary_list[i] == 0:
            binary_list[i] = 1
        else:
            binary_list[i] = 0
        
    return binary_list

print(notOperator([1, 1, 0]))