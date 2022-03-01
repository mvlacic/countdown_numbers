from countdown import countdown
import sys
if __name__ == '__main__':

    operations = countdown(int(sys.argv[1]), [int(i) for i in sys.argv[2:]])

    print(operations)