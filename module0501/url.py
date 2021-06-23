url_rozetka = "https://rozetka.com.ua/mobile-phones/c80003/kolichestvo-osnovnih-kamer=3630921;producer=xiaomi;23777=6" \
              "-6-5;38435=677049/ "

query_url_rozetka = "kolichestvo-osnovnih-kamer=3630921;producer=xiaomi;23777=6-6-5;38435=677049"

query_rozetka = query_url_rozetka.split(";")

print(query_rozetka)

object_rozetka = {}
for el in query_rozetka:
    key, value = el.split("=")
    object_rozetka.update({key: value})

print(object_rozetka)