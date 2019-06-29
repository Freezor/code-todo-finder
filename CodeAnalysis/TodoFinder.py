from CodeAnalysis.DirectoryReader import DirectoryReader
import config
from CodeAnalysis.ReportWriter import ReportWriter
from CodeAnalysis.TaskExtractor import TaskExtractor


def TodoFinder():
    print("START FILE READING")
    reader = DirectoryReader(config.directory_path)
    files = reader.read_all_files()
    print("FOUND %s FILES" % len(files))
    taskExtractor = TaskExtractor(files)
    extracted_tasks = taskExtractor.extract_tasks()
    print("EXTRACTED %s TASKS" % len(extracted_tasks))
    report_writer = ReportWriter(config.export_file_name, config.delimiter)
    report_writer.write_dicitionary(extracted_tasks)
    print("TASKS SAVED TO CSV FILE")
    print('END OF SCRIPT')


if __name__ == "__main__":
    TodoFinder()
