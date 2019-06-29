import re
import config


class TaskExtractor():
    def __init__(self, file_dictionary):
        self.files = file_dictionary

    def extract_tasks(self):
        print("Start processing files")
        extracted_tasks = []
        fileamount = len(self.files)
        processedfiles = 0
        for file in self.files:
            f = open(file['path'], "r")
            linenumber = 1
            for line in f:
                for taskpattern in config.task_occasions:
                    if re.search(taskpattern, line, re.IGNORECASE):
                        extracted_tasks.append(
                            {'filename': file['file'], 'task': line, 'line': linenumber, 'path': file['path']})
                linenumber += 1
            processedfiles += 1
            percentage = abs(processedfiles / fileamount)*100.0
            if percentage > 1:
                print("Processed %s percentage of all files" % percentage)
        return extracted_tasks
