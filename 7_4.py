import os

all_files = []
for root, dirs, files in os.walk('../'):
    for file in files:
        all_files.append(os.path.getsize(os.path.join(root, file)))
max_size = max(all_files)

my_dict = {}
i = 1
for x in range(len(str(max_size))):
    i *= 10
    if i == 10:
        my_dict[int(i)] = len([file for file in all_files if i >= file >= 0])
    else:
        my_dict[int(i)] = len([file for file in all_files if i >= file >= i / 10])
print(my_dict)