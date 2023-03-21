"""
    Найдите способ запустить скрипт (из шага 1) на платформе яндекс практикум
    (используйте тренажёр или проект в jupyter notebook на платформе яндекс практикум)
"""
# Шаг 1 (запускаем скрипт на платформе яндекс практикум)

import os

dir_ = '/datasets/'
subdir = []

with os.scandir(dir_) as files:
    for file in files:
        if file.is_dir():
            subdir.append(file.name)

# print(subdir) # выводит список папок в директории

dirs = ['/datasets/']

for item in subdir:
    dirs.append(f'/datasets/{item}/')

# print(dirs)  # выводит все папки в директории

assets_all = []

for item in dirs:
    assets_all.append([os.path.join(item, f) for f in os.listdir(item)])

assets = [item for sublist in assets_all for item in sublist]
print(assets)  # выводит список файлов в директории

# Скопируйте финальный вывод из консоли. Эти данные понадобятся на шаге 2.