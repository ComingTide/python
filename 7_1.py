import os

mid_folder = 'my_project'
end_folders = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(mid_folder):
    for end_folder in end_folders:
        os.makedirs(os.path.join(mid_folder, end_folder))
    print('... Стартер для проекта успешно создан в текущей директории')
else:
    print(f'{mid_folder} уже существует')