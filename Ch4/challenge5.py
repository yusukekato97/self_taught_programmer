def str_to_float(str):
    try:
        float_str = float(str)
    except(ValueError):
        print("cannnot convert to float type")
        float_str = None
    return float_str

str_num = input("Type a number: ")
float_num = str_to_float(str_num)
print("Your number is :")
print(float_num)
