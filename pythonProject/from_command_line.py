import sys
import os

path = sys.argv[0]
splitted = os.path.split(path)

# print(splitted)

if __name__ == "__main__" and splitted[0] == '.':
    print('this is from command line')
else:
    print('from else')


