#Converts a decimal number to binary
def toHex(number:int) -> list:
    hex_array:chr = [] #Character array to store the hexidecimal numbers

    while number != 0:
        # Stores the reminder in a tempory variable
        temp = int(number % 16)

        if temp < 10:
            hex_array.append(chr(temp  + 48))
        else:
            hex_array.append(chr(temp + 55))
        
        number = number // 16
    
    return hex_array

# Turns the hexidecimal list to a string output
def buildHexString(hex_array:list) -> str:
    output = ""
    
    for i in range(len(hex_array), 0, -1):
        output += str(hex_array[i - 1])
    
    return output


# Converts a value from hexidecimal to Decimal
def fromHex(digit) -> int:
    digit_values = len(digit)
    decimal = 0

    base = 1

    for i in range(digit_values - 1, -1, -1):
        print("test")
        # Numbers lie between 0 and 9
        if digit[i] >= '0' and digit[i] <= '9':
            decimal += (ord(digit[i]) - 48) * base

            base = base * 16

        # Numbers are between A(10) and F(16)
        elif digit[i] >= 'A' and digit[i] <= 'F':
            decimal += (ord(digit[i]) - 55) * base 

            base = base * 16

    return decimal

hex_values = toHex(1019)
str_hex = buildHexString
(hex_values)
dec_value = fromHex(str_hex)

print(f"Hex_list = {hex_values}, string_hex = {str_hex}, Decimal =  {dec_value}")