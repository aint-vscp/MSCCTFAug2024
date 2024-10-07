binary_num1 = '11111110'
binary_num2 = '01010000'

left_shift_result = int(binary_num1, 2) << 1

hex_result = hex(left_shift_result)

print("\nOperation 1: Left Shift")
print(f"Result after left shift: {bin(left_shift_result)[2:].zfill(len(binary_num1) + 1)}")
print(f"Hexadecimal result: {hex_result}")

right_shift_result = int(binary_num2, 2) >> 1

hex_result = hex(right_shift_result)

print("\nOperation 2: Right Shift")
print(f"Result after right shift: {bin(right_shift_result)[2:].zfill(len(binary_num2) - 1)}")
print(f"Hexadecimal result: {hex_result}")

bitwise_or_result = int(binary_num1, 2) | int(binary_num2, 2)

hex_result = hex(bitwise_or_result)

print("\nOperation 3: Bitwise OR")
print(f"Result after bitwise OR: {bin(bitwise_or_result)[2:].zfill(max(len(binary_num1), len(binary_num2)))}")
print(f"Hexadecimal result: {hex_result}")

and_result = int(binary_num1, 2) & int(binary_num2, 2)

hex_result = hex(and_result)

print("\nOperation 4: Bitwise AND")
print(f"Result after bitwise AND: {bin(and_result)[2:].zfill(len(binary_num1))}")
print(f"Hexadecimal result: {hex_result}")

add_result = int(binary_num1, 2) + int(binary_num2, 2)

hex_result = hex(add_result)

print("\nOperation 5: Addition")
print(f"Result after addition: {bin(add_result)[2:].zfill(len(binary_num1))}")
print(f"Hexadecimal result: {hex_result}")

multiply_result = int(binary_num1, 2) * int(binary_num2, 2)

hex_result = hex(multiply_result)

print("\nOperation 6: Multiplication")
print(f"Result after multiplication: {bin(multiply_result)[2:]}")
print(f"Hexadecimal result: {hex_result}")