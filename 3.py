with open("text_3.txt", "r", encoding="utf-8") as my_file:
    content = my_file.readlines()
    sum = 0
    b = []
    for i in content:
        n = i.split()
        a = float(n[1])
        sum += a
        if a < 20000:
            b.append(n[0])
    c = ", ".join(b)
    med_val = sum / len(content)
    print(f"Сотрудники, у которых заработная плата ниже 20000:\n{c}")
    print(f"Средняя заработная плата в компании: {med_val} рублей!")
