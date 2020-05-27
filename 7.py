import json

with open("text_7.txt", "r", encoding="utf-8") as my_file:
    con = my_file.readlines()
    result = 0
    n = 0
    temp = []
    my_list = []
    dict_2 = {}
    for i in con:
        n = i.split()
        res = [int(n[a]) - int(n[b]) for a in range(2, len(n) - 1) for b in range(3, len(n))]
        if res[0] > 0:
            temp.append(res[0])
            result += res[0]

        name = [n[el] for el in range(len(n)) if n[el] == n[0]]
        for arg in range(len(name)):
            dict_2[name[arg]] = res[arg]

    my_list.append(dict_2)
    med = {"average_profit": result / len(temp)}
    my_list.append(med)
    print(my_list)

with open("m_j.json", "x", encoding="utf-8") as my_file_2:
    json.dump(my_list, my_file_2, ensure_ascii=False, indent=4)
