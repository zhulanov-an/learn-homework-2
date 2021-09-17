"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('data/referat.txt', mode='r', encoding='utf-8') as ref_1:
        strings = ref_1.readlines()
        print(f"количество строк: {len(strings)}")
        cnt = 0
        for idx, string in enumerate(strings):
            cnt += len(string.split())
            strings[idx] = string.replace('.', '!')
        print(f"количество слов {cnt}")
        with open("data/referat2.txt", mode="w", encoding="utf-8") as ref_2:
            ref_2.writelines(strings)


if __name__ == "__main__":
    main()
