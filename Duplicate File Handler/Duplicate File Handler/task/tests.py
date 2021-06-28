from hstest.stage_test import StageTest
from hstest.check_result import CheckResult
from hstest import dynamic_test, TestedProgram
import os
import shutil

# dict for creating files
files = {
    'info.txt': {'path': ['root_folder'],
                 'content': 'eed110d0dbd1d89d1ffea807d1d88679_1'},
    'lost.json': {'path': ['root_folder'],
                  'content': '3a70ac2ebacf4174aa11dfbd1af835bd_1'},
    'phones.csv': {'path': ['root_folder'],
                   'content': '671ab9fbf94dc377568fb7b2928960c9_1'},
    'python.txt': {'path': ['root_folder'],
                   'content': 'd2c2ee4cbb368731f1a5399015160d7d_1'},
    'bikeshare.csv': {'path': ['root_folder', 'calc'],
                      'content': 'c03285172453d7278a85a5db4d06423c_1'},
    'server.php': {'path': ['root_folder', 'calc'],
                   'content': 'a5c662fe853b7ab48d68532791a86367'},
    'db_cities.js': {'path': ['root_folder', 'files'],
                     'content': 'f2e5cf58ae9b2d2fd0ae9bf8fa1774da'},
    'some_text.txt': {'path': ['root_folder', 'files'],
                      'content': 'd2c2ee4cbb368731f1a5399015160d7d'},
    'cars.json': {'path': ['root_folder', 'files', 'stage'],
                  'content': '3a70ac2ebacf4174aa11dfbd1af835bd'},
    'package-lock.json': {'path': ['root_folder', 'files', 'stage'],
                          'content': 'eebf1c62a13284ea1bcfe53820e83f11'},
    'index.js': {'path': ['root_folder', 'files', 'stage', 'src'],
                 'content': '797ac79aa6a3c2ef733fecbaff5a655f'},
    'libs.txt': {'path': ['root_folder', 'files', 'stage', 'src'],
                 'content': '4909fd0404ac7ebe1fb0c50447975a2a'},
    'reviewSlider.js': {'path': ['root_folder', 'files', 'stage', 'src'],
                        'content': 'abc96a9b62c4701f27cf7c8dbd484fdc'},
    'spoiler.js': {'path': ['root_folder', 'files', 'stage', 'src'],
                   'content': 'b614ccac263d3d78b60b37bf35e860f3'},
    'src.txt': {'path': ['root_folder', 'files', 'stage', 'src'],
                'content': 'eed110d0dbd1d89d1ffea807d1d88679_1'},
    'toggleMiniMenu.js': {'path': ['root_folder', 'files', 'stage', 'src'],
                          'content': '7eceb7dd5a0daaccc32739e1dcc6c3b0_1'},
    'extraversion.csv': {'path': ['root_folder', 'project'],
                         'content': 'fc88cf4d79437fa06e6cfdd80bd0eed2_1'},
    'index.html': {'path': ['root_folder', 'project'],
                   'content': '3f0f7b61205b863d2051845037541835_1'},
    'python_copy.txt': {'path': ['root_folder', 'project'],
                        'content': 'd2c2ee4cbb368731f1a5399015160d7d_1'}
}

root_dir_path = os.path.join('module', 'root_folder')


def create_files(path):
    # delete all root_folder
    if os.path.isdir(path):
        shutil.rmtree(path)

    # create files
    for key, dict_val in files.items():
        path = os.path.join('module', *dict_val['path'])
        if not os.path.isdir(path):
            os.makedirs(path)
        file_path = os.path.join(path, key)
        with open(file_path, 'a+') as f:
            f.write(dict_val['content'])


# Tests
class DuplicateFileHandlerCheck(StageTest):
    @dynamic_test()
    def check_empty_arg(self):
        main = TestedProgram()
        output = main.start().lower()
        if 'not' in output and 'specified' in output:
            return CheckResult.correct()
        return CheckResult.wrong("You should check command line argument")

    @dynamic_test()
    def check_format_choice(self):
        main = TestedProgram()
        output = main.start(root_dir_path).lower()
        if 'format' in output:
            return CheckResult.correct()
        return CheckResult.wrong("You should read the user's choice of file format")

    @dynamic_test()
    def check_sorting_choice(self):
        main = TestedProgram()
        main.start(root_dir_path).lower()
        output = main.execute("csv").lower()
        if 'sort' in output and 'desc' in output and 'asc' in output and 'option' in output:
            output = main.execute("3").lower()
            if 'wrong' in output:
                return CheckResult.correct()
            return CheckResult.wrong("You should read and check the user's choice of sorting option")
        return CheckResult.wrong("You should print out sorting options and add input prompt message")

    @dynamic_test()
    def check_path(self):
        main = TestedProgram()
        main.start(root_dir_path).lower()
        main.execute("").lower()
        output = main.execute("2").lower().split('\n')
        for val in output:
            if '.' in val:
                if not os.path.exists(val):
                    return CheckResult.wrong(f"{val} path does not exist")
        return CheckResult.correct()

    @dynamic_test()
    def check_group_first_line(self):
        main = TestedProgram()
        main.start(root_dir_path).lower()
        main.execute("").lower()
        output = main.execute("2").lower().split('\n')
        output = [val for val in output if val]

        if not output:
            return CheckResult.wrong("After choosing ascending sorting order your output is empty!")

        if 'byte' in output[0]:
            return CheckResult.correct()
        return CheckResult.wrong(f"The first line of group of files should contain files size")

    @dynamic_test()
    def check_group_size(self):
        main = TestedProgram()
        main.start(root_dir_path).lower()
        main.execute("").lower()
        output = main.execute("2").lower().split('\n')
        output = [val for val in output if val]

        for val in output:
            if 'byte' in val and not any(i.isdigit() for i in val.split()):
                return CheckResult.wrong(f"There is no size in the line: {val}")

        return CheckResult.correct()

    @dynamic_test()
    def check_size(self):
        main = TestedProgram()
        main.start(root_dir_path).lower()
        main.execute("").lower()
        output = main.execute("2").lower().split('\n')
        output = [val for val in output if val]
        size = None

        for val in output:
            if 'byte' in val:
                for i in val.split():
                    if i.isdigit():
                        size = int(i)
            elif val and 'check' not in val:
                if not os.path.exists(val):
                    return CheckResult.wrong('Looks like you printed a file name that doesn\'t exist!')
                file_size = os.path.getsize(val)
                if size != file_size:
                    return CheckResult.wrong(f"{val} has wrong size group")
        return CheckResult.correct()

    @dynamic_test()
    def check_order_asc(self):
        main = TestedProgram()
        main.start(root_dir_path).lower()
        main.execute("").lower()
        output = main.execute("2").lower().split('\n')
        sizes = []
        size = None

        for val in output:
            if 'byte' in val:
                for i in val.split():
                    if i.isdigit():
                        size = int(i)

                sizes.append(size)

        if len(sizes) != 2:
            return CheckResult.wrong(f"Wrong number of groups of files")
        if sizes[0] == 32 and sizes[1] == 34:
            return CheckResult.correct()
        return CheckResult.wrong(f"Wrong sorting order of files")

    @dynamic_test()
    def check_order_desc(self):
        main = TestedProgram()
        main.start(root_dir_path).lower()
        main.execute("").lower()
        output = main.execute("1").lower().split('\n')
        sizes = []
        size = None

        for val in output:
            if 'byte' in val:
                for i in val.split():
                    if i.isdigit():
                        size = int(i)

                sizes.append(size)

        if len(sizes) != 2:
            return CheckResult.wrong(f"Wrong number of groups of files")
        if sizes[1] == 32 and sizes[0] == 34:
            return CheckResult.correct()
        return CheckResult.wrong(f"Wrong sorting order of files")

    @dynamic_test()
    def check_num(self):
        main = TestedProgram()
        main.start(root_dir_path).lower()
        main.execute("").lower()
        output = main.execute("2").lower().split('\n')
        num_files = []
        n = 0

        for val in output:
            if val and 'check' not in val:
                if 'byte' in val:
                    num_files.append(n)
                    n = 0
                else:
                    n += 1
        num_files.append(n)

        if num_files[1] != 9:
            return CheckResult.wrong(f"""Output contains wrong number of files with a size of 32 bytes. 
                                         Number of files in output: {num_files[1]}""")

        if num_files[2] != 10:
            return CheckResult.wrong(f"""Output contains wrong number of files with a size of 34 bytes. 
                                         Number of files in output: {num_files[2]}""")

        return CheckResult.correct()

    @dynamic_test()
    def check_format(self):
        main = TestedProgram()
        main.start(root_dir_path).lower()
        main.execute("csv").lower()
        output = main.execute("2").lower().split('\n')

        for val in output:
            if '.' in val and 'csv' not in val:
                return CheckResult.wrong(f"Wrong file format in {val}")

        return CheckResult.correct()

    def after_all_tests(self):
        try:
            if os.path.isdir(root_dir_path):
                shutil.rmtree(root_dir_path)
        except Exception as ignored:
            pass

    def generate(self):
        try:
            create_files(root_dir_path)
        except Exception as ignored:
            pass
        return []


if __name__ == '__main__':
    DuplicateFileHandlerCheck().run_tests()
