with open("text_2.txt", "r", encoding="utf-8") as my_file:
    content = my_file.readlines()
    print(content)
    print("Количество строк в Вашем файле: ", len(content))

    for i in content:
        n = i.split()
        print(f"В строке {i} содержится {len(n)} слов!", end="\n")
