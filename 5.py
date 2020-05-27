with open("text_5.txt", "x", encoding="utf-8") as my_file:
    try:
        n = map(int, input("Введи целые числа, для которых хотите посчитать сумму: \n").split())
        print(f"Сумма чисел в файле - {sum(n)}!")
        my_file.write(" ".join(n))
    except ValueError:
        print("Необходимо вводить целые числа!")
