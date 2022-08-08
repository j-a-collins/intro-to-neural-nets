import sys


def print_usage():
    print(
        """
Intro to Neural Networks helper package.
Basic usage:
nnhelper command [parameter1 [parameter2]]
Commands:
  info    Prints information about the notebooks
  code    Creates a file containing the code of a given code example
          in given location. Location is optional, example:
          nnhelper code 2 nnhelper/p02.py
          will create a file p02.py in a nnhelper folder containing
          the code of lesson 2
    """
    )


def info():
    print(
        """
  Intro to Neural Networks by Jack Collins
  https://stash/
  ---
  This package contains supplementary material related to the 
  the series of notebooks on neural networks.
    """
    )


# TODO Allow for export of code from particular lessons to a .py file
def code(lesson, path):
    pass


def main():

    if len(sys.argv) == 1:
        print_usage()
        return

    command = sys.argv[1].strip()

    if command == "info":
        info()
    elif command == "code" and len(sys.argv) < 3:
        print_usage()
    # elif command == 'code':
    #     code(*sys.argv[2:])
