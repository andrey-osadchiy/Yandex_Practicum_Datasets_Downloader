Title: Yandex Practicum Datasets Downloader

Description:

This Python project helps download training datasets from Yandex Practicum. The project consists of two steps: getting a list of files and downloading them to your computer.

Step 1 involves running a Python script on the Yandex Practicum platform to retrieve the list of files. To do this, you can use the simulator or Jupyter Notebook project on the platform. The script is included in this project and can be found in the file step1.py.


Step 2 involves downloading the data sets to your computer. To do this, you need to run the script step2.py on your local computer. Before running the script, make sure to assign the values obtained in step 1 to the assets variable.

Instructions:

To use this project, follow these steps:

    Clone the repository to your local machine.
    Run the script step1.py on the Yandex Practicum platform to retrieve the list of files.
    Assign the values obtained in step 1 to the assets variable in step2.py.
    Run the script step2.py on your local computer to download the data sets.

Note: Make sure you have the necessary permissions to access the Yandex Practicum platform and download the datasets.

I hope this helps! Let me know if you have any other questions.

---
Название: Яндекс Практикум. Загрузчик датасетов

Описание:

Этот Python-проект помогает загружать учебные наборы данных из Yandex Practicum. Проект состоит из двух шагов: получение списка файлов и их загрузка на ваш компьютер.

Краткая инструкция:

Чтобы использовать этот проект, выполните следующие шаги:

    Клонируйте репозиторий на локальный компьютер.
    Запустите скрипт step1.py на платформе Yandex Practicum, чтобы получить список файлов.
    Присвойте значения, полученные на шаге 1, переменной assets в файле step2.py.
    Запустите сценарий step2.py на своем локальном компьютере, чтобы загрузить наборы данных.

Шаг 1 включает в себя запуск скрипта Python на платформе Yandex Practicum для получения списка файлов. Для этого вы можете использовать тренажер или учебный проект в Jupyter Notebook на платформе. Сценарий включен в этот проект и находится в файле step1.py.
```python
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
```
Шаг 2 включает загрузку наборов данных на ваш компьютер. Для этого необходимо запустить скрипт step2.py на локальном компьютере. Перед запуском скрипта убедитесь, что значения, полученные в шаге 1, присвоены переменной assets.
```python
# Шаг 2 (запускаем скрипт на локальном компьютере, на который будут скачаны файлы)

import os
import requests
import time
import random

my_url = 'https://code.s3.yandex.net'

assets = [  # !сюда нужно вставить данные, полученные на предыдущем шаге! ТРЕБУЕТСЯ ОЧЕНЬ МНОГО МЕСТА НА ДИСКЕ
    '/datasets/autos.csv', '/datasets/arrivals.xlsx', '/datasets/calls.csv', '/datasets/data.csv']

count = 0
skip_count = 0
except_count = 0
all_count = len(assets)
except_items = []

# получаем путь, по которому мы будем сохранять файлы
save_path = os.getcwd()
# или можно задать папку в домашней директории.
# Например: save_path = os.path.join(os.path.expanduser("~"), 'download')

for item in assets:
    try:
        # получаем имя каталога и имя файла из item
        dir_name, file_name = os.path.split(item)

        # убираем символ "/" у dir_name, чтобы сделать имя относительным
        dir_name = dir_name[1:] if dir_name.startswith('/') else dir_name

        # создаём каталог на диске, если он не существует
        os.makedirs(os.path.join(save_path, dir_name), exist_ok=True)

        # проверить, существует ли уже файл в директории
        if os.path.exists(os.path.join(save_path, dir_name + '/' + file_name)):
            print(f"{item} уже существует, пропускаем загрузку...")
            skip_count += 1 # пропускаем загрузку в случае уже существующего файла
        else:
            # скачиваем item и записываем его в переменную "r"
            r = requests.get(my_url + item)

            # сохраняем файл в директории заданной в переменной save_path.
            with open(os.path.join(save_path,  dir_name + '/' + file_name), 'wb') as f:
                f.write(r.content)

            # добавляем условие для добавления паузы
            # условие будет истинным только тогда, когда значение count будет кратно случайному целому числу от 3 до 5.
            if count % random.randint(3, 5) == 0:  
                print(f"Загружено {count} файлов из {all_count}")
                # добавляем рандомную паузу перед загрузкой нового файла
                # устанавливаем длительность паузы между загрузками = случайному целому числу от 2 до 8 секунд.
                pause = random.randint(2, 8)
                print(f"пауза между загрузкой файлов составляет {pause} секунд")
                time.sleep(pause)
            count += 1
            upload_percentage = count / all_count  # вычисляем процент загруженных файлов
            print(f"{upload_percentage:.2%}", item)
    except:
        except_count += 1
        except_items.append(item)
        print(f'{item}!! не удалось скачать! номер итерации {count}')

print("Все файлы скачаны!")
print(f"Всего загружено {count} файла(ов) из {all_count}. Процент загруженных файлов составляет {count / all_count:.2%}")
print(f"Пропущено (уже существуют) {skip_count} файла(ов) из {all_count}. ")
print(f"Всего загрузок {count - except_count}")
print(f"Не удалось скачать по причине каких-то ошибок/прерываний: {except_count} файла(ов)")
print(f"Список пропущенных файлов по причине каких-то ошибок/прерываний: {except_items}")
```


Примечание: Убедитесь, что у вас есть необходимые разрешения для доступа к платформе Yandex Practicum и загрузки наборов данных.

Надеюсь, это поможет! Дайте мне знать, если у вас возникнут другие вопросы.