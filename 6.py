with open("text_6.txt", "r", encoding="utf-8") as my_file:
    content = my_file.readlines()
    z = 0
    c = 0
    my_dict = {}
    for i in content:
        n = list(i)
        my_list = [el for el in n if 48 <= ord(el) <= 57 or 65 <= ord(el) <= 122]

        key = [el_1 for el_1 in my_list if 65 <= ord(el_1) <= 122]
        val = [el_2 for el_2 in my_list if 48 <= ord(el_2) <= 57]
        val_2 = [val[el_3 - 1] + val[el_3] for el_3 in range(1, len(val), 2)]
        b = ["".join(key)]
        if len(val_2) > 1:
            d = [int(arg) for arg in val_2]
            z = sum(d)
        else:
            z = val_2[0]

        my_dict_2 = {arg_1: z for arg_1 in b}
        my_dict.update(my_dict_2)

    print(my_dict)
