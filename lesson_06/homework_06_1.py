value = input("Введіть ваш текст: ")
unique_chars = len(set(value))

if unique_chars > 10:
    print(True)
else:
    print(False)