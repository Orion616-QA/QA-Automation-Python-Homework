print("tasks 01 - 04:\n")
alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."\n')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
print("task 05:\n")
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area_str = "436 402"
azov_sea_area_str = "37 800"

black_sea_area_int = 436402
azov_sea_area_int = 37800

total_area_int = black_sea_area_int + azov_sea_area_int
total_area_str = str(total_area_int)

total_area_str = total_area_str[:3] + " " + total_area_str[3:]

print(
    f'Площа Чорного моря становить {black_sea_area_str} км2, а площа Азовського моря становить {azov_sea_area_str} км2.'
    f'\nТож загальну площу Чорного та Азовського морів рахуємо так:'
    f'\nплощу Чорного моря  додаємо до площі Азовського моря - {black_sea_area_str} км2 + {azov_sea_area_str} км2 = {total_area_str} км2\n')

print("task 06:\n")

"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
store_str_all = "375 291"
store_str_1_2 = "250 449"
store_str_2_3 = "222 950"

store_all_int = 375291
store_1_2_int = 250449
store_2_3_int = 222950

store_3_int = store_all_int - store_1_2_int
store_2_int = store_2_3_int - store_3_int
store_1_int = store_1_2_int - store_2_int

store_1_str = str(store_1_int)
store_2_str = str(store_2_int)
store_3_str = str(store_3_int)

store_1_str = store_1_str[:-3] + " " + store_1_str[-3:]
store_2_str = store_2_str[:-3] + " " + store_2_str[-3:]
store_3_str = store_3_str[:-3] + " " + store_3_str[-3:]

print(
    f'Усього товарів на складах: {store_str_all} товарів.'
    f'\nНа 1-му та 2-му складах разом: {store_str_1_2} товарів.'
    f'\nНа 2-му та 3-му складах разом: {store_str_2_3} товарів.'
    f'\n\nРозвʼязання:'
    f'\n3-й склад = від загальної кількість товарів на всіх складах віднімаємо сумму складів 1 та 2: {store_str_all} - {store_str_1_2} = {store_3_str}'
    f'\n2-й склад = від кількість товарів на складах 2 та 3 віднімаємо кількість товарів на складі 3: {store_str_2_3} - {store_3_str} = {store_2_str}'
    f'\n1-й склад = від кількість товарів на складах 1 та 2 віднімаємо кількість товарів на складі 2: {store_str_1_2} - {store_2_str} = {store_1_str}'
    f'\n\nВідповідь:'
    f'\nСклад 1: {store_1_str} товарів'
    f'\nСклад 2: {store_2_str} товарів'
    f'\nСклад 3: {store_3_str} товарів\n'
)
print("task 06:\n")
# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

years = 1.5
months = int(years * 12)
monthly_payment = 1179

total_cost = months * monthly_payment

print(f"Рішення задачі:\n"
      f"1. Тривалість виплат: {years} роки = {months} місяців"
      f"\n2. Щомісячний платіж: {monthly_payment} грн"
      f"\n3. Загальна вартість комп’ютера: {monthly_payment} грн * {months} = {total_cost} грн"
      f"\nВідповідь: {total_cost} грн – вартість комп’ютера\n")
# task 07
print("task 07:\n")
"""
Знайди остачу від ділення чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

data_a = "8019 : 8"
operation_a = 8019 % 8
print(f"a) При діленні {data_a} буде остача = {operation_a}")

data_b = "9907 : 9"
operation_b = 9907 % 9
print(f"b) При діленні {data_b} буде остача = {operation_b}")

data_c = "2789 : 5"
operation_c = 2789 % 5
print(f"c) При діленні {data_c} буде остача = {operation_c}")

data_d = "7248 : 6"
operation_d = 7248 % 6
print(f"d) При діленні {data_d} буде остача = {operation_d}")

data_e = "7128 : 5"
operation_e = 7128 % 5
print(f"e) При діленні {data_e} буде остача = {operation_e}")

data_f = "19224 : 9"
operation_f = 19224 % 9
print(f"f) При діленні {data_f} буде остача = {operation_f}\n")

print("task 08:\n")
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

large_pizza_qty = 4
large_pizza_price = 274

medium_pizza_qty = 2
medium_pizza_price = 218

juice_qty = 4
juice_price = 35

cake_qty = 1
cake_price = 350

water_qty = 3
water_price = 21

large_pizza_cost = large_pizza_qty * large_pizza_price
medium_pizza_cost = medium_pizza_qty * medium_pizza_price
juice_cost = juice_qty * juice_price
cake_cost = cake_qty * cake_price
water_cost = water_qty * water_price

total_cost = large_pizza_cost + medium_pizza_cost + juice_cost + cake_cost + water_cost

print(f"Щоб знайти загальну суму, розрахуємо вартість кожної позиції:"
      f"\n1. Вартість великих піц: ціну {large_pizza_price} грн множимо на кількість {large_pizza_qty} шт. і отримуємо {large_pizza_cost} грн."
      f"\n2. Вартість середніх піц: ціну {medium_pizza_price} грн множимо на кількість {medium_pizza_qty} шт. і отримуємо {medium_pizza_cost} грн."
      f"\n3. Вартість соку: ціну {juice_price} грн множимо на кількість {juice_qty} шт. і отримуємо {juice_cost} грн."
      f"\n4. Вартість торта: ціну {cake_price} грн множимо на кількість {cake_qty} шт. і отримуємо {cake_cost} грн."
      f"\n5. Вартість води: ціну {water_price} грн множимо на кількість {water_qty} шт. і отримуємо {water_cost} грн."
      f"\nТепер додаємо всі суми: {large_pizza_cost} + {medium_pizza_cost} + {juice_cost} + {cake_cost} + {water_cost}."
      f"\nЗагальна вартість замовлення: {total_cost} гривень.\n")

print("task 09:\n")
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
photos_per_page = 8

full_pages = total_photos // photos_per_page

print(f"Рішення задачі:"
      f"\nДізнаємось, скільки повних сторінок вийде, якщо одна сторінка може містити 8 форографій. "
      f"\nДля цього ділимо {total_photos} на {photos_per_page}:"
      f"\n{total_photos} / {photos_per_page} = {full_pages} повних сторінок"
      f"\nПідсумок: всього Ігорю знадобиться {full_pages} сторінок.\n")

print("task 10:\n")
# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
fuel_per_100km = 9
tank_capacity = 48

number_of_segments = distance // 100
total_fuel_needed = number_of_segments * fuel_per_100km
fuel_to_add = total_fuel_needed - tank_capacity
refills_needed = fuel_to_add // tank_capacity

print(f"Завдання 1: Скільки всього потрібно бензину?"
      f"\n1) Спочатку треба зрозуміти, скільки 'порцій' по 100 км є у нашому шляху {distance} км."
      f"\nДля цього ділимо: {distance} км / 100 км = {number_of_segments} таких 'порцій'."
      f"\n2) Ми знаємо, що на кожну таку 'порцію' йде {fuel_per_100km} літрів бензину."
      f"\nТепер множимо наші {number_of_segments} порцій на {fuel_per_100km} літрів: {number_of_segments} * {fuel_per_100km} = {total_fuel_needed} літрів.\n"
      f"\nНа всю подорож нам знадобиться {total_fuel_needed} літрів бензину.\n\n"
      f"Завдання 2: Скільки разів треба заїхати на заправку?"
      f"\n1) У нас вже є {tank_capacity} літрів у баку. А всього нам потрібно {total_fuel_needed} літрів."
      f"\nДізнаємось, скільки ще треба заправити: {total_fuel_needed} л - {tank_capacity} л = {fuel_to_add} літрів.\n"
      f"\n2) Отже, нам треба долити {fuel_to_add} літрів. Кожна заправка дає нам повний бак, тобто {tank_capacity} літрів."
      f"\nЩоб дізнатися кількість заправок, ділимо те, що треба долити, на об'єм бака: {fuel_to_add} л / {tank_capacity} л = {refills_needed} рази.\n"
      f"\nВідповідь: родині потрібно буде заїхати на заправку щонайменше {refills_needed} рази.")
