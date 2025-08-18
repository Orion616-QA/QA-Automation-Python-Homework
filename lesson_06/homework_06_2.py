while True:
    value = input(f"Введіть ваш текст із літерою 'H': ")
    for text in value:
        if text.lower() == "h":
            print(f"Текст має літеру 'H'")
            break
    else:
        print(f"Текст не має літери 'H'")
        continue