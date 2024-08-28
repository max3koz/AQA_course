def mysplit(strng):
    res = []
    add_sring = ""
    for srting_item in strng:
        if srting_item != " ":
            add_sring += srting_item
        elif add_sring != "":
            res.append(add_sring)
            add_sring = ""
    if add_sring != "":
        res.append(add_sring)
    return res


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

num_dict = {
    "0": ["***", "* *", "* *", "* *", "***"],
    "1": ["  *", "  *", "  *", "  *", "  *"],
    "2": ["***", "  *", "***", "*  ", "***"],
    "3": ["***", "  *", "***", "  *" ,"***"],
    "4": ["* *", "* *", "***", "  *", "  *"],
    "5": ["***", "*  ", "***", "  *", "***"],
    "6": ["***", "*  ", "***", "* *", "***"],
    "7": ["***", "  *", "  *", "  *", "  *"],
    "8": ["***", "* *", "***", "* *", "***"],
    "9": ["***", "* *", "***", "  *", "***"],
    ".": ["   ", "   ", "   ", "   ", "  *"]
}

def num_emulate(number_string):
    digits = [num_dict[digit] for digit in str(number_string)]
    for i in range(5):
        print("  ".join(segment[i] for segment in digits))

input_string: str = input("Enter number: ")
num_emulate(input_string)