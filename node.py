class Node:
    l, r = None, None
    code = None
    num = None

    def __init__(self):
        pass


def write_tree(fout, v):
    if v is None:
        print('GG')
        return

    isl = v.l is not None
    isr = v.r is not None

    fout.writelines(str(int(isl)) + ' ' + str(int(isr)) + ' ' + str(v.code) + '\n')

    if isl:
        write_tree(fout, v.l)

    if isr:
        write_tree(fout, v.r)
