url = "https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"

# Парсим строку запрос и превращаем в словарь
_, query_search = url.split("?")  # ["https://www.google.com/search", "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"]
print(query_search)
list_parameters = query_search.split("&")
print(list_parameters)

object_search = {}
for el in list_parameters:
    key, value = el.split("=")
    object_search.update({key: value.replace("+", " ")})

print(object_search)

# Формируем строку запрос
url_string = ''
for key, value in object_search.items():
    url_string = url_string + "=".join([key, value.replace(" ", "+")])
print(url_string)