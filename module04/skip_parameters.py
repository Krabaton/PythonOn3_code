def modeling(factor, *_, correction=0.5):
    return factor * correction


print(modeling(4, 5, 6, correction=1.5))