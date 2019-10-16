import argparse
import re
import os
import glob
from pathlib import Path
file_list = []


def ignore_case(filename, word, path):
    pattern = re.compile(r"{}.*".format(word), re.IGNORECASE)
    os.chdir(path)
    f_path = glob.glob(filename)

    """Search file via wildcard"""
    for file in f_path:
        with open(file, 'r') as out:
            contents = out.read()
            matches = pattern.finditer(contents)

            for match in matches:
                print("{} \t {}".format(file, match.group(0)))


def grep(filename, word, path):
    """Search a word"""
    pattern = re.compile(r'{}.*'.format(word))
    os.chdir(path)
    f_path = glob.glob(filename)

    """Search file via wildcard"""
    for file in f_path:
        with open(file, 'r') as out:
            contents = out.read()
            matches = pattern.finditer(contents)

            for match in matches:
                print("{} \t {}".format(file, match.group(0)))


def main():
    """Argument Parser"""
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-ig", "--ignore", help="Ignore case sensitive.", action="store_true")
    parser.add_argument("word", type=str)
    parser.add_argument("filename", type=str)
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    """Function arguments"""
    if args.filename and args.word and args.path:
        grep(args.filename, args.word, args.path)
    elif args.ignore:
        ignore_case(args.filename, args.word, args.path)
    else:
        print("Error.")


if __name__ == "__main__":
    main()
