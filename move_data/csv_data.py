import csv


class ReadCSV:
    def __init__(self, csv_filepath, dlm):
        """Читаем строки из csv-файла. Возвращаем в виде списка."""
        csv_data = []
        with open(csv_filepath, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=dlm)
            for row in csv_reader:
                csv_data.append(row)

        self.csv_data = csv_data
