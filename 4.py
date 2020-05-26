numbers = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_4.txt", "r+", encoding="utf-8") as my_file:
    content = my_file.readlines()
    b = []
    for i in content:
        n = i.split()
        for k in numbers.keys():
            if n[0] == k:
                n[0] = numbers[k]
        a = " ".join(n)
        b.append(a)
    with open("text_4_2.txt", "x", encoding="utf-8") as new_file:
        print("\n".join(b), file=new_file)
