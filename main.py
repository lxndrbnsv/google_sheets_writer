from move_data.csv_data import ReadCSV
from move_data.xlsx_data import ReadXLSX
from move_data.sheets import WriteRows, Clear


csv_filepath = "./files/test.csv"  # Путь к csv-файлу.
dlm = ","  # Разделитель в csv-файле.

xlsx_filepath = "./files/test.xlsx"  # Путь к xlsx-файлу.
sheet = "Sheet1"  # Лист в xlsx-файле.

doc_name = "api_test"  # Имя документа google-sheets.

if __name__ == "__main__":
    xlsx_data = ReadXLSX(xlsx_filepath=xlsx_filepath, sheet=sheet).xlsx_data
    csv_data = ReadCSV(csv_filepath=csv_filepath, dlm=dlm).csv_data

    WriteRows(doc_name=doc_name, rows=xlsx_data)
    # Clear(doc_name=doc_name)
