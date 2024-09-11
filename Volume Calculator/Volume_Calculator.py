
def get_input (input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")
        try:
            user_input = input_type(raw_input)
            print("Thank you for your input.\n")
            break
        except ValueError:
            print(f"Please input a valid number")
    return user_input

width = get_input("please input the width of the object:", float) 
height = get_input("please input the height of the object:", float)
length = get_input("please input the length of the object:", float)

volume = width * height * length

print(volume)

