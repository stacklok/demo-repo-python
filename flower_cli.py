# Simple CLI command to print an ASCII flower
import sys

def print_flower():
    flower = '''
    , - ~ ~ ~ - ,
 ,'             ',
,'  _   _   _   _  ',
|  | `_' | `_' |  |
|  |  _  |  _  |  |
|  | | | | | | |  |
|  | |_| | |_| |  |
'   \ |   |   | /  '
 \  '-' '-' '-'  /
  \             /
   ` - . _ _ . - ' 
    '''
    print(flower)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "flower":
        print_flower()
    else:
        print("Usage: python -m demo flower")


if __name__ == "__main__":
    main()