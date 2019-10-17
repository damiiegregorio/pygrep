import argparse
import re
import os
import glob


def ignore_case(filename, word, path):
    """Search a word"""
    pattern = re.compile(r'{}.*'.format(word), re.I)
    os.chdir(path)
    f_path = glob.glob(filename)

    """Search file via wildcard"""
    for file in f_path:
        with open(file, 'r') as out:
            contents = out.read()
            matches = pattern.finditer(contents)

            for match in matches:
                found = "{} \t {}".format(file, match.group(0))
                print(found)


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
                found = "{} \t {}".format(file, match.group(0))
                print(found)


def main():
    """Argument Parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="Type a word to search", type=str)
    parser.add_argument("filename", help="File type/filename", type=str)
    parser.add_argument("path", nargs='?', help="path", type=str)
    parser.add_argument("-i", "--ignore", help="Ignores case sensitive.", action="store_true")
    args = parser.parse_args()

    """Function arguments"""

    if args.ignore:
        ignore_case(args.filename, args.word, args.path)
    else:
        grep(args.filename, args.word, args.path)


if __name__ == "__main__":
    main()
