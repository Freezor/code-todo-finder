import glob, os
import config


class DirectoryReader():
    def __init__(self, path):
        self.path = path

    def read_all_files(self):
        extracted_files = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                for filetype in config.file_types:
                    if file.endswith(filetype):
                        complete_path = str(os.path.join(root, file))
                        extracted_files.append({'file': file, 'path': complete_path})
                        break
        return extracted_files