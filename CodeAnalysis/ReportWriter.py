import csv


class ReportWriter():
    def __init__(self, file_name, delimiter):
        self.fileName = file_name
        self.delimiter = delimiter

    def write_dictionary(self, dictionary):
        """
        Creates a new csv file, with all dictionary values from the param list
        :param dictionary:
        """
        f = open(self.fileName, 'wb')
        try:
            keys = dictionary[0].keys()
            writer = csv.DictWriter(f, keys, delimiter=self.delimiter)
            writer.writeheader()
            writer.writerows(dictionary)
        finally:
            f.close()
