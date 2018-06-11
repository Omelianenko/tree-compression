from node import *
import numpy as np

class Coder:
    Fib = []
    n_nodes = -1

    def get_fib(self, num):
        for i in range(num):
            self.Fib.append(self.Fib[-1] + self.Fib[-2])
        return

    def __init__(self):
        self.Fib.append(0)
        self.Fib.append(1)
        self.Fib.append(1)
        self.Fib.append(2)
        self.get_fib(1000)

    def encode(self, data, v=-1):
        if v == -1:
            self.n_nodes = -1

        self.n_nodes += 1
        v = self.n_nodes

        cur = Node()

        isl, isr = data[v][0], data[v][1]
        cnt = isl + isr

        if cnt == 0:
            cur.code = 1
            cur.num = v
            return cur

        left, right = 0, 0

        if isl:
            cur.l = self.encode(data, v)
            left = cur.l.code

        if isr:
            cur.r = self.encode(data, v)
            right = cur.r.code


        if cnt == 2:
            num = self.find_fib(left + right)
            cur.code = (left + right) * self.Fib[num - 1] + right * self.Fib[num]
            # print(cur.code)
            # print(left + right, self.Fib[num - 1])
            # print(right, self.Fib[num])
        elif isl:
            num = self.find_fib(left)
            if num % 2 == 1:
                num += 1
            cur.code = left * self.Fib[num]
        elif isr:
            num = self.find_fib(right)
            if num % 2 == 0:
                num += 1
            cur.code = right * self.Fib[num]

        return cur

    def decode(self, num):
        v = Node()
        v.code = num

        if num == 1:
            return v

        if num == 2:
            leaf = Node()
            leaf.code = 1
            v.r = leaf
            return v

        if num == 3:
            leaf = Node()
            leaf.code = 1
            v.l = leaf
            return v

        a, b, t = self.find_a_b(num)

        if a <= 0 and t % 2 == 0:
            v.l = self.decode(b)
        elif a <= 0 and t % 2 == 1:
            v.r = self.decode(b)
        else:
            v.l = self.decode(a)
            v.r = self.decode(b)
        return v

    def get(self, _t, _num):
        t = int(_t)
        num = int(_num)
        k = 1 if t % 2 == 0 else -1

        f1 = self.Fib[t - 1]
        f2 = self.Fib[t]

        a1 = (k * f1 * num) % f2
        b = (num - a1 * f1) // f2
        a = (a1 - b)

        return np.array([a, b])

    def find_a_b(self, num):
        lbound = 1
        rbound = len(self.Fib) - 1

        while rbound - lbound > 1:
            mid = (lbound + rbound) // 2
            val = self.get(mid, num)
            if val[1] <= 0:
                rbound = mid - 1
            else:
                lbound = mid

        for i in [rbound, lbound]:
            val = self.get(i, num)
            if val[1] > 0:
                return val[0], val[1], i

        self.get_fib(num)
        return self.find_a_b(num)

    def find_fib(self, num):
        lbound = 0
        rbound = len(self.Fib) - 1
        while rbound - lbound > 1:
            mid = (lbound + rbound) // 2
            if self.Fib[mid] < num + 1:
                lbound = mid + 1
            else:
                rbound = mid
        if self.Fib[lbound] >= num + 1:
            return lbound
        elif self.Fib[rbound] >= num + 1:
            return rbound
        else:
            self.get_fib(num)
            return self.find_fib(num)