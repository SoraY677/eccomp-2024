import sys
import shutil


def main(origin, dest):
    shutil.copy(origin, dest)


if __name__ == '__main__':
    args = sys.argv
    main(args[1], args[2])
