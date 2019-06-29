from CodeAnalysis.DirectoryReader import DirectoryReader
import config
from CodeAnalysis.ReportWriter import ReportWriter
from CodeAnalysis.TaskExtractor import TaskExtractor

def TodoFinder():
    """
    Main Method, that reads all given files, searches for Tasks in each chosen file type and exporting them to csv
    """
    print("START FILE READING")
    reader = DirectoryReader(config.directory_path)
    files = reader.read_all_files()
    print("FOUND %s FILES" % len(files))
    if len(files)>0:
        taskExtractor = TaskExtractor(files)
        extracted_tasks = taskExtractor.extract_tasks()
        print("EXTRACTED %s TASKS" % len(extracted_tasks))
        if len(extracted_tasks)>0:
            report_writer = ReportWriter(config.export_file_name, config.delimiter)
            report_writer.write_dictionary(extracted_tasks)
            print("TASKS SAVED TO CSV FILE")
    print('END OF SCRIPT')


if __name__ == "__main__":
    TodoFinder()
