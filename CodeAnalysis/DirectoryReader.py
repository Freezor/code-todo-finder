import glob, os
import config

# Reader class for reading all files in starting directory and all sub-directories
class DirectoryReader():
    def __init__(self, path):
        self.path = path

    def read_all_files(self):
        """
        Reads all files in dictionary and sub-folders.
        Generates a list of dictionaries containing each file, matching the configured file types
        :return: dictionary list with {file; path}
        """
        extracted_files = []
        for root, dirs, files in os.walk(self.path):
            for file in files:
                for filetype in config.file_types:
                    if file.endswith(filetype):
                        complete_path = str(os.path.join(root, file))
                        extracted_files.append({'file': file, 'path': complete_path})
                        break
        return extracted_files