# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

new_record_in_list = ('Ivan', 'Polishchuk', 35, 'QA Engineer', 'Dnipro')
people_records.insert(0, new_record_in_list)

people_records[1], people_records[5] = people_records[5], people_records[1]
print(f"Swap indexes result is:\n")
for record in people_records:
  print(record)
  print()

if people_records[6][2] >= 30 and people_records[10][2] >= 30 and people_records[13][2] >= 30:
  print(f"All peoples in list on indexes 6, 10, 13 have age >= 30")
else:
  print(f"Not all peoples in list on indexes 6, 10, 13 have age >= 30.\nResult:\nfor index 6 is - {people_records[6][2]},\n"
  f"for index 10 is - {people_records[10][2]},\nfor index 13 is - {people_records[13][2]}")
