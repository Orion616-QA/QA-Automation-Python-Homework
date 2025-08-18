import random

list_of_numbers = [random.randint(1,100) for _ in range(10)]
print(list_of_numbers)

sum_of_even_numbers = sum(i for i in list_of_numbers if i % 2 == 0)
print(sum_of_even_numbers)