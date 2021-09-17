import csv

"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    people = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Петр', 'age': 49, 'job': 'Super Big boss'},
    ]

    with open('data/people.csv', mode='w', encoding='utf-8', newline='') as people_csv:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(people_csv, fields, delimiter=';')
        writer.writeheader()
        for human in people:
            writer.writerow(human)


if __name__ == "__main__":
    main()
