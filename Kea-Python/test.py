def my_sum(*args):
    print(args)
    result = 0
    for num in args:
        result += num
    print(result)
    return result

#my_sum(5,6)


def point(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k, v, sep='=')

#point(x=0, y=0, z=0)


import sys

port = sys.argv[2]
print("Port is ", port)


import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))