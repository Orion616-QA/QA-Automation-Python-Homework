import csv
import json
import logging
import xml.etree.ElementTree as ET
from pathlib import Path

folder_csv = Path("/Users/macbookpro13/PycharmProjects/QA-Automation-Python-Homework/lesson_13/csv_files")
folder_json = Path("/Users/macbookpro13/PycharmProjects/QA-Automation-Python-Homework/lesson_13/json_files")
folder_xml = Path("/Users/macbookpro13/PycharmProjects/QA-Automation-Python-Homework/lesson_13/xml_files")

result_csv = folder_csv / "result.csv"
json_validation_log = folder_json / "json_validation.log"

#Налаштування логерів для зберігання у файл та відображення в консоль
def setup_logger(name, handler_type, log_file=None, level=logging.INFO, mode="w"):
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        logger.handlers.clear()

    if handler_type == "file" and log_file:
        handler = logging.FileHandler(log_file, mode=mode)
    else:
        handler = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger

json_logger = setup_logger("json_logger", handler_type="file", log_file=json_validation_log)
console_logger = setup_logger("console_logger", handler_type="stream")


# Функція збирає дані із файлів CSV, прибирає дублікати та зберігає результат в окремий файл
def merge_csv_files(folder_csv: Path, result_csv: Path) -> None:
    unique_rows = []
    seen = set()

    for path in folder_csv.glob("*.csv"):

        with path.open("r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                row_tuple = tuple(row)
                if row_tuple not in seen:
                    seen.add(row_tuple)
                    unique_rows.append(row)

    with result_csv.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(unique_rows)

# Функція бере всі файли JSON із папки і логує помилки формату у окремий файл
def validate_json_files(folder_json: Path) -> None:
    for path in folder_json.glob("*.json"):
        try:
            with path.open("r") as f:
                json.load(f)
        except json.JSONDecodeError as e:
            json_logger.error(f"Файл {path.name} має невалідний JSON формат: {e}")

# Функція пошуку по group/number
def log_incoming_by_number(xml_file: Path, group_number: str) -> None:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for group in root.findall("group"):
            number = group.find("number")
            if number is not None and number.text == group_number:
                timing = group.find("timingExbytes")
                if timing is not None:
                    incoming = timing.find("incoming")
                    if incoming is not None:
                        console_logger.info(f"Group {group_number} has incoming: {incoming.text}")
                        return
                console_logger.info(f'Group {group_number} не має значення "incoming"')
                return

        console_logger.info(f"Group {group_number} не знайдено")