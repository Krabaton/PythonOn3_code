import re

string = "Исключить из этой [строки группы] символов, [расположенные между] скобками [, ]."

lang = "The best language Java"
pattern = "Java"

result = re.sub(pattern, "Python", lang)
print(result)

pattern = r"\[.*?\]"
result = re.sub(pattern, "", string)
print(result)
