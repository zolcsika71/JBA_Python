import os
import argparse
from collections import defaultdict


class FileParser:
    def __init__(self):
        self.path = None
        self.ext = None
        self.order = None
        self.sizes = defaultdict(list)

    def run(self):
        self.get_args()
        if self.path is None:
            print('Directory is not specified')
        else:
            self.get_ext()
            self.get_order()
            self.get_files()
            self.print_result()

    def get_ext(self):
        self.ext = '.' + input('Enter file format:\n')

    def get_order(self, display=True):
        if display:
            print('Size sorting options\n1. Descending\n2. Ascending')

        order = int(input('\nEnter a sorting option:\n'))

        if not (order == 1 or order == 2):
            print('\nWrong option')
            self.get_order(False)

        if order == 1:
            self.order = True
        else:
            self.order = False

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('path', type=str, help='Enter directory', default=None, nargs='?')

        args = parser.parse_args()

        self.path = args.path

    def get_files(self):
        for root, dirs, files in os.walk(self.path, topdown=True):
            for name in files:
                path = os.path.join(root, name)
                size = os.path.getsize(path)
                filename, file_extension = os.path.splitext(path)
                if self.ext == '.' or file_extension == self.ext:
                    self.sizes[size].append(path)

    def print_result(self):
        sizes = sorted(self.sizes.keys(), reverse=self.order)
        for size in sizes:
            print('\n')
            print(f'{size} bytes')
            for path in self.sizes[size]:
                print("".join(path))


FileParser().run()
