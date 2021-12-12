def toHex(number:int):
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

def outputHex(hex_array:list) -> str:
    for i in range(len(hex_array), 0, -1):
        print(hex_array[i - 1], end= '')

outputHex(toHex(33))