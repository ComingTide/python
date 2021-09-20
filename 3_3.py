def thesaurus(*args):
    dict_name = {}
    for n in sorted(args):
        word = n[0]
        if word in dict_name:
            dict_name[word] += [n]
        else:
            dict_name[word] = [n]
    return dict_name


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Алёна", "Елена", "Бабушка", "Витя"))
