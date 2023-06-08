"""
    This function takes a digit of a hexadecimal string and returns its decimal representation.
    Args:
    - digit (str): A single character from a hexadecimal string
    Returns:
    - int: The decimal representation of the digit.
"""
def hex_char_decode(digit):
    # Define a string of hexadecimal characters
    hex_chars = "0123456789abcdefABCDEF"
    # If the digit is in the first 10 characters of the hex_chars string, return its integer value
    if digit in hex_chars[0:10]:
        return int(digit)
    # If the digit is in the next 6 characters of the hex_chars string, return its decimal value
    elif digit in hex_chars[10:16]:
        return 10 + hex_chars[10:16].index(digit)
    # If the digit is in the final 6 characters of the hex_chars string, return its decimal value
    else:
        return 10 + hex_chars[16:22].index(digit)




"""
    This function takes a hexadecimal string and returns its decimal representation.
    Args:
    - hex (str): The hexadecimal string
    Returns:
    - int: The decimal representation of the hexadecimal string.
"""
def hex_string_decode(hex):   
    decimal = 0                     # Initial decimal value              
    hex = hex.lower()               # Convert the hex string to lower case 
    if hex.startswith("0x"):        # Check if the hex string starts with "0x", and if it does, remove it
        hex = hex[2:]
    for i in range(len(hex)):       # Iterate over each character in the hex string
        # Add the decimal value of the current character to the decimal result
        decimal += hex_char_decode(hex[i]) * (16 ** (len(hex) - i - 1))
    return decimal                  # Return the decimal result




"""
    This function takes a binary string and returns its decimal representation.
    Args:
    - binary (str): The binary string
    Returns:
    - int: The decimal representation of the binary string.
"""
def binary_string_decode(binary):
    decimal = 0         # Initial decimal vaule
    if binary.startswith("0b"):         # Check if the binary string starts with "0b", and remove it if so
        binary = binary[2:]
    for i in range(len(binary)):            # Iterate over each character in the binary string
        # Add the decimal value of the current character to the decimal result
        decimal += int(binary[i]) * (2 ** (len(binary) - i - 1))
    return decimal          # Return the decimal result




"""
    This function takes a binary string and returns its hexadecimal representation.
    Args:
    - binary (str): The binary string
    Returns:
    - str: The hexadecimal representation of the binary string.
"""
def binary_to_hex(binary):
    decimal = binary_string_decode(binary)              # Convert the binary string to decimal
    hex = ""                                            # Initial hex string result
    while decimal > 0:
        # Add the hexadecimal character representing the remainder of decimal divided by 16 to the beginning of the hex string
        hex = "0123456789ABCDEF"[decimal % 16] + hex
        decimal = decimal // 16             # Update decimal to be the integer division of decimal by 16
    return hex                              # Return the hex string result



if __name__ == '__main__':      #Run as a standalone script instead of an imported module. This is the main block of code to be run from the command line. 
    while True:                 # Repeat the following indefinitely
        #Print the decoding Menu
        print("Decoding Menu")
        print("-------------")
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit\n")
        option = int(input("\nPlease enter an option: "))       # Get user's input for operation choice
        if option == 1:
            hex_string = input("\nPlease enter the numeric string to convert: ")
            result = hex_string_decode(hex_string)              # Decode the hexadecimal string
            print("\nResult:", result,"\n")                     # Print the result
        elif option == 2:
            binary_string = input("\nPlease enter the numeric string to convert: ")     # Get the binary string to decode
            result = binary_string_decode(binary_string)                                # Decode the binary string
            print("\nResult:", result,"\n")                                             # Print the result
        elif option == 3:
            binary_string = input("Please enter the numeric string to convert: ")       # Get the binary string to convert to hexadecimal
            result = binary_to_hex(binary_string)                                       # Convert the binary string to hexadecimal
            print("\nResult:", result,"\n")                                             # Print the result
        elif option == 4:
            print("Goodbye!")
            break                       # If option 4 is chosen, exit the loop
        else:
            print("Invalid option. Please try again.") # if the user's input is invalid, not on the menu, print an error message 
