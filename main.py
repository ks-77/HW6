"""
HW6
Savchenko Kirill
"""

# 1


def product(list_n):
    prod = 1
    for num in list_n:
        prod *= num
    return prod


numbers = []
while True:
    user_inp = input("Enter number or 'stop' to stop creating the list: ")
    if user_inp == "stop":
        break
    try:
        number = user_inp
        numbers.append(int(number))
        print(f"number: {number} added to list")
    except ValueError:
        print("Enter only numbers!")
    except Exception as e:
        print(f"Error: {e}")

print(f"your list: {numbers}")
print(f"product of numbers in your list: {product(numbers)}")
