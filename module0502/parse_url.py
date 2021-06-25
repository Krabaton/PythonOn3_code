import re

google_url = "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"
rozetka_url = "kolichestvo-osnovnih-kamer=3630921;producer=xiaomi;23777=6-6-5;38435=677049"


def get_object_parameters(query, pattern="&|;", key_split="="):
    object_search = {}
    for el in re.split(pattern, query):
        key, value = el.split(key_split)
        object_search.update({key: value.replace("+", " ")})
    return object_search


print(get_object_parameters(google_url))
print(get_object_parameters(rozetka_url))
