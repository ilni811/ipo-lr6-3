str1 = int (input("введите колво строк "))
if str1 < 1:
    print("введено не верно")
else:
    # ввод строк
    list = []
    for i in range(str1):
        list.append(str(input(f"Введите вашу строку {i + 1} ")))
        # обьединение строк с пробелами
        list_join = " ".join(list)
        # разделение строки на слова
        list_join = list_join.split()
        # длина исходной строки
        list_kolvo = len(list_join)
        # количество различных слов 
        list_negr = len(set(list_join))
print(f"различных слов {list_negr}, слов всего {list_kolvo}")
     
