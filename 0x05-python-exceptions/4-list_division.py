#!/urs/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length
    for i in range(list_length):
        try:
            if i < len(my_list_1) and i < len(my_list_2):
                result[i] = my_list_1[i] / my_list_2[i]
            else:
                raise IndexError("out of range")
        except (ZeroDivisionError, TypeError):
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                print("division by 0")
            else:
                print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            pass
    return result
