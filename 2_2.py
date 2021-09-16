# in init_list added initial list
init_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
right_list = []     # create a new list in which we will put the correct values
# separate numbers from strings and add "0" to two integer digits
for n in init_list:
    if n.replace("+", "").replace("-", "").isdigit():
        if n.isdigit():
            right_list.append(f'"{int(n):02}"')
        else:
            right_list.append(f'"{n[0]}{int(n[1:]):02}"')
    else:
        right_list.append(n)
# output of a string using the method .join
print(" ".join(right_list))