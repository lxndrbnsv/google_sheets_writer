import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Загружаем json-файл с данными для авторизации.
creds = ServiceAccountCredentials.from_json_keyfile_name(
        "creds.json",
        scope
    )
client = gspread.authorize(creds)


class Clear:
    def __init__(self, doc_name):
        """Очищает таблицу."""

        # Переменная doc_name содержит имя таблицы google-sheets, а
        # sheet1 - лист, с которым будут производиться операции.
        sheet = client.open(doc_name).sheet1
        sheet.clear()


class WriteRows:
    def __init__(self, doc_name, rows):
        """Запись данных в документ google-sheets."""

        # Переменная doc_name содержит имя таблицы google-sheets, а
        # sheet1 - лист, в который будут писаться данные.
        sheet = client.open(doc_name).sheet1

        # Перед записью данных чистим таблицу.
        sheet.clear()

        # Запись строк в таблицу. 1 - номер строки, с которой будет начинаться
        # запись.
        sheet.insert_rows(rows, 1)
