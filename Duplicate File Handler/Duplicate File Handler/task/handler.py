import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str, help='Enter directory', default=False, nargs='?')

args = parser.parse_args()


def get_files(path):
    # os.chdir(path)
    for root, dirs, files in os.walk(".", topdown=True):
        for name in files:
            print(os.path.join(path, root[2:], name))


if not args.dir:
    print('Directory is not specified')
else:
    # print(args.dir)
    get_files(args.dir)
