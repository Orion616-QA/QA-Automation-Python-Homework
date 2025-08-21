# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def calculate_two_numbers():
    num1 = int(input('Введіть перше число: '))
    num2 = int(input('Введіть друге число: '))

    result = num1 + num2

    return result

print(f'Сумма двох чисел дорівнює: {calculate_two_numbers()}')


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_numbers_from_input(count=5):
    numbers = []
    for i in range(count):
        n = int(input(f'Введіть число {i+1}: '))
        numbers.append(n)
    return sum(numbers) / len(numbers)

print("Середнє арифметичне:", average_numbers_from_input())


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def string_reverse():
    text = input("Введіть текст: ")
    return text[::-1]

print(string_reverse())

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longer_word_in_list():
    words = input("Введіть слова через пробіл: ").split()

    longest_word = words[0]
    for word in words[1:]:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word
print(f'Найдовше слов у введенному списку: {longer_word_in_list()}')



# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# Функція рахує кількість унікальних символів. Якщо <= 10, то False, якщо > 10 - True
def check_unique_chars():
    text = input("Введіть ваш текст: ")
    unique_chars = len(set(text))
    return unique_chars > 10

print(check_unique_chars())

# Функція шукає літеру "Н" у тексті. Якщо знаходить - закінчує цикл. Якщо не знаходить - продовжує цикл
# де потрібно знову ввести текст
def check_letter_h():
    while True:
        value = input(f"Введіть ваш текст із літерою 'H': ")
        for text in value:
            if text.lower() == "h":
                print(f"Текст має літеру 'H'")
                break
        else:
            print(f"Текст не має літери 'H'")
            continue
        break

check_letter_h()

# Функція вибирає із першого списку лише стрінги та додає їх у другий список і повертає результат
def only_string():
    lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

    lst2 = []
    for s in lst1:
        if type(s) == str:
            lst2.append(s)
    return lst2

print(f'Список лише з стрінгами: {only_string()}')

# Функція створює рандомний список з 10 цілих чисел від 1 до 100 та повертає результат суми лише парних чисел


def even_numbers_sum():
    import random
    list_of_numbers = [random.randint(1, 100) for _ in range(10)]
    sum_of_even_numbers = sum(i for i in list_of_numbers if i % 2 == 0)
    return list_of_numbers, sum_of_even_numbers

numbers, even_sum = even_numbers_sum()

print(f'Список - {numbers}. Сума парних чисел у списку: {even_sum}')

even_numbers_sum()

