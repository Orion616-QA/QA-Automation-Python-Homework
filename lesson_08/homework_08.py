my_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_of_numbers(data):
    try:
        parts = data.split(",")
        return sum(int(x) for x in parts)
    except ValueError:
        return "Не можу це зробити"

for item in my_list:
    print(sum_of_numbers(item))