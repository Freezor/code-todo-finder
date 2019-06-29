'''
    THIS IS THE GENERAL CONFIG FILE
    PLEASE ADAPT THESE CONFIGS TO YOUR LOCAL PROJECT REQUIREMENTS
'''
# Path to your project directory
directory_path = '/PATH/TO/DIRECTORY'
# List of file types you want to analyse
file_types = ['.cs', '.java', '.py']
# here you can change the layout your tasks are. May be changed to other strings, if you want to analyse different code usages
task_occasions = ['//TODO', '#TODO', '///TODO', '// TODO', '# TODO', '/// TODO']
# the delimuter, which will be used in the generated csv file
delimiter = ';'
# the name of the generated csv file
export_file_name = 'report.csv'
