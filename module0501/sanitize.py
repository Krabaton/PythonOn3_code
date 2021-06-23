"""
Дана строка символов.
Исключить из этой строки группы символов, расположенные между скобками [, ].
Сами скобки тоже должны быть исключены.
Предполагается, что внутри каждой пары скобок нет других скобок.
"""

string = "Исключить из этой [строки группы] символов, [расположенные между] скобками [, ]."


# test = "этой [строки группы] символов"
# start_index = test.find("[")
# end_index = test.find("]")
# print(start_index, end_index)
# new_string = test[:start_index] + test[end_index + 1:]
# print(new_string)


def sanitize(data):
    while True:
        start_index = data.find("[")
        end_index = data.find("]")
        if start_index == -1:
            break
        data = data[:start_index] + data[end_index + 1:]
    return data


print(sanitize(string))
