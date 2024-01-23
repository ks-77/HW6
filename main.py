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

# 2


def mini(list_mini):
    return min(list_mini)


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
print(f"the smallest number in your list: {mini(numbers)}")

# 3


def prime(list_prime):
    return len(list_prime)


numbers = []
while True:
    user_inp = input("Enter number or 'stop' to stop creating the list: ")
    if user_inp == "stop":
        break
    try:
        number = user_inp
        if int(number) != 1 and int(number) // 1 and int(number) // int(number):
            numbers.append(int(number))
            print(f"number: {number} added to list")
        else:
            print(f"number: {number} is not prime")

    except ValueError:
        print("Enter only numbers!")
    except Exception as e:
        print(f"Error: {e}")

print(f"your list: {numbers}")
print(f"the quantity of prime numbers in your list: {prime(numbers)}")

# 4


def delete():
    user_list = []

    while True:
        try:
            user_input = input("Enter number or 'stop' to stop creating the list: ")
            if user_input == "stop":
                break
            user_number = int(user_input)
            user_list.append(user_number)
        except ValueError:
            print("Enter only numbers!")
    try:
        number_to_del = int(input("Enter a number to delete: "))
        count_del = user_list.count(number_to_del)
    except ValueError:
        print("Enter only numbers!")

    return count_del


dell = delete()
print(f"quantity of deleted numbers: {dell} ")

# 5


def common(list_1, list_2):
    com_list = set(list_1) & set(list_2)
    common_list = list(com_list)
    return common_list


inp_1 = []
while True:
    user_inp = input("Enter something or 'stop' to stop creating the first list: ")
    if user_inp == "stop":
        break
    inp_1.append(user_inp)
    print(f"'{user_inp}' is now in the list")
inp_2 = []
while True:
    user_inp = input("Enter something or 'stop' to stop creating the second list: ")
    if user_inp == "stop":
        break
    inp_2.append(user_inp)
    print(f"'{user_inp}' is now in the list")
new_list = common(inp_1, inp_2)
print(f"common elements in your lists: {new_list}")
