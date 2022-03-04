import random

def select_number():
    while True:
        n = random.randint(1000, 9999)
        string_n = str(n)
        if string_n[0] == string_n[1]:
            False
        else:
            if string_n[0] == string_n[2]:
                False
            else:
                if string_n[0] == string_n[3]:
                    False
                else:
                    if string_n[1] == string_n[2]:
                        False
                    else:
                        if string_n[1] == string_n[3]:
                            False
                        else:
                            if string_n[2] == string_n[3]:
                                False
                            else:
                                return n


print(select_number())










