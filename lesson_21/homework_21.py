import datetime
import logging

source_file = "/Users/macbookpro13/PycharmProjects/QA-Automation-Python-Homework/lesson_21/hblog.txt"
result_file = "/Users/macbookpro13/PycharmProjects/QA-Automation-Python-Homework/lesson_21/hb_test.log"
key = "TSTFEED0300|7E3E|0400"

logging.basicConfig(
    filename=result_file,
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def compare_timestamps():
    # Витягуємо всі значення по ключу
    with open(source_file, 'r') as f:
        entries = [line for line in f if key in line]
    # Проходимось попарно, форматуємо в час та вираховуємо різницю
    for i in range(0, len(entries) - 1, 2):
        try:
            line1 = entries[i]
            line2 = entries[i + 1]

            time1_str = line1.split('Timestamp ')[1].split(' ')[0]
            time2_str = line2.split('Timestamp ')[1].split(' ')[0]

            time1 = datetime.datetime.strptime(time1_str, '%H:%M:%S')
            time2 = datetime.datetime.strptime(time2_str, '%H:%M:%S')

            time_diff = abs((time1 - time2).total_seconds())

            if 31 < time_diff < 33:
                logging.warning(f"Time difference between {time1_str} and {time2_str} is {time_diff} seconds")
            elif time_diff >= 33:
                logging.error(f"Time difference between {time1_str} and {time2_str} is {time_diff} seconds")

        except (IndexError, ValueError) as e:
            logging.error(f"Error processing entries: {e}")
            continue

compare_timestamps()