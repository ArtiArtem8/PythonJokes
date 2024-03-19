# -*- coding: utf-8 -*-

"""A. Эмо бой
Ограничение времени 	1 секунда
Ограничение памяти 	64Mb
Ввод 	стандартный ввод или input.txt
Вывод 	стандартный вывод или output.txt
При регистрации на портале каждый эмо бой обязан придумать себе никнейм.
Никнейм должен быть не короче восьми символов, содержать в себе хотя бы одну цифру,
и хотя бы по одной заглавной и прописной английской букве.

Формат ввода.
Вводится никнейм — последовательность букв и цифр без пробелов.
Длина строки не превосходит 100 символов.

Формат вывода.
Выведите «YES», если ник подходит для эмо боя, и «NO» — в противном случае. """


def check(name: str) -> bool:
    """
    Проверяет никнейм на соответствие требованиям
    :param name: никнейм
    :type name: str
    :rtype: bool
    """
    return (
            len(name) >= 8 and
            any(i.isdigit() for i in name) and
            any(i.isupper() for i in name) and
            any(i.islower() for i in name)
    )


input_name = input()
print("YES" if check(input_name) else "NO")

# Тесты