import re
import config


class TaskExtractor():
    def __init__(self, file_dictionary):
        self.files = file_dictionary

    def extract_tasks(self):
        """
        Searches in each file for occuring patterns and saves them in a dictionary
        :return: list of dictionaries with all found tasks
        """
        print("Start processing files")
        extracted_tasks = []
        amount_of_files = len(self.files)
        amount_of_processed_files = 0
        for file in self.files:
            f = open(file['path'], "r")
            line_number = 1
            for line in f:
                for pattern in config.task_occasions:
                    if re.search(pattern, line, re.IGNORECASE):
                        line = line.lstrip()
                        extracted_tasks.append(
                            {'filename': file['file'], 'task': line, 'line': line_number, 'path': file['path']})
                line_number += 1
            amount_of_processed_files += 1
            percentage = abs(amount_of_processed_files / amount_of_files)*100.0
            if percentage > 1:
                print("Processed %s percentage of all files" % percentage)
        return extracted_tasks
