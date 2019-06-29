import csv


class ReportWriter():
    def __init__(self, file_name, delimiter):
        self.fileName = file_name
        self.delimiter = delimiter

    def write_dicitionary(self, dictionary):
        f = open(self.fileName, 'wb')
        try:
            keys = dictionary[0].keys()
            writer = csv.DictWriter(f, keys, delimiter=self.delimiter)
            writer.writeheader()
            writer.writerows(dictionary)
        finally:
            f.close()
