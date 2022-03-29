stored_numbers = []
while True:
    number = input("Enter a number : ")
    try:
        if number.lower() == "done":
            print(f"Maximum : {max(stored_numbers)}")
            print(f"Minimum : {min(stored_numbers)}")
            break
        number = int(number)
    except:
        print("\tInvalid Input")
        continue
    number = float(number)
    stored_numbers.append(number)

#
# new_list = []
# while True:
#     number = input("enter a number: ")
#     try:
#         if number == "done".lower():
#             break
#         number1 = int(number)
#         new_list.append(number1)
#     except:
#         print("invalid input")
# print(new_list)
# print(f"the max number is :{(max(new_list))}")
# print(f"the min number is :{(min(new_list))}")