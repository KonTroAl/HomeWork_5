my_file = open("text_1.txt", "x", encoding="utf-8")
print("Введите набор строк, которые будут записаны в файл, если захотите прервать запись в файл нажмите 'Enter'")
while True:
    n = input("")
    if n == "":
        break
    my_file.write(n)

my_file.close()
