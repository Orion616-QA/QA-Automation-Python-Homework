# Підсумовує числа, розділені комою. Якщо є некоректні значення, повертає повідомлення про помилку
def sum_of_numbers(data: str):
    try:
        parts = data.split(",")
        return sum(int(x) for x in parts)
    except ValueError:
        return "Не можу це зробити"

# Виконує складання двох чисел. Якщо строка, то перетворює в int
def calculate_two_numbers(x, y):
    num1 = int(x)
    num2 = int(y)
    return num1 + num2

# Повертає строку у форматі реверсу символів
def string_reverse(text: str) -> str:
    return text[::-1]

# Повертає найдовше слово у списку
def longer_word_in_list(words: list[str]) -> str:
    if not words:
        raise ValueError("Список слов не может быть пустым")

    longest_word = words[0]
    for word in words[1:]:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

# Повертає індекс першого входження підстроки
def find_substring(str_1: str, str_2: str) -> int:
    return str_1.find(str_2)