import numpy as np
from coder import *

coder = Coder()

def decode(s='decode'):
    fin = open(s + '.in', 'r')

    num = int(fin.read())
    root = coder.decode(num)

    fout = open(s + '.out', 'w')
    write_tree(fout, root)


def encode(s='encode'):
    fin = open(s + '.in', 'r')

    data = []
    for line in fin:
        l, r = map(int, line.split())
        cur = np.array([l, r])
        data.append(cur)
    root = coder.encode(data)

    fout = open(s + '.out', 'w')
    write_tree(fout, root)

encode('encode-0')
encode('encode-1')
decode('decode-0')
decode('decode-1')